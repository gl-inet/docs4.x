# AmneziaWG-obfuscatie {#amneziawg-obfuscation}

AmneziaWG is een op WireGuard gebaseerd VPN-protocol met ingebouwde verkeersobfuscatie. De obfuscatieparameters bepalen hoe het verkeer wordt verhuld om detectie bij strenge netwerkinspectie te omzeilen.

Hieronder lees je wat AmneziaWG is en hoe de versies van elkaar verschillen.

## Waarom AmneziaWG? {#why-amneziawg}

De voorloper van AmneziaWG, WireGuard, is dankzij de compacte code en hoge efficiëntie een snel en betrouwbaar VPN-protocol. De vaste pakketheaders en voorspelbare pakketgrootten vormen echter een gemakkelijk herkenbaar patroon. DPI-systemen kunnen deze pakketten eenvoudig herkennen en verbindingen direct beëindigen, wat een ernstig probleem is in landen met strenge internetcensuur.

AmneziaWG behoudt de eenvoudige architectuur en hoge prestaties van WireGuard en voegt een speciale obfuscatiemodule toe om patronen in VPN-verkeer te verbergen. Hierdoor kunnen particuliere en zakelijke gebruikers hun onlineprivacy beschermen en stabiele verbindingen behouden in beperkende netwerkomgevingen.

Samengevat:

- Het verhult VPN-kenmerken om detectie door internetproviders, firewalls of deep packet inspection (DPI) te voorkomen.

- De VPN-verbinding lijkt op normaal webverkeer, waardoor de stabiliteit en slagingskans in beperkte netwerken verbeteren.

## AmneziaWG V2.0 {#amneziawg-v20}

### Overzicht {#amneziawg-v20-overview}

<font color="red">**Opmerking**: GL.iNet-routers met firmware v4.9.0 of hoger ondersteunen AmneziaWG 2.0.</font>

AmneziaWG 2.0 behoudt de obfuscatiemechanismen van v1.0: de reeks junkpakketten (**Jc**, **Jmin**, **Jmax**) en de willekeurige voorvoegsels voor Init- en Response-pakketten (**S1–S2**). De volgende mechanismen verhullen de delen van de verbinding die nog voorspelbaar waren:

* **S3–S4**: willekeurige voorvoegsels voor Cookie- en Data-pakketten. In v1.0 kregen alleen Init- en Response-pakketten opvulling. Daardoor waren Cookie-pakketten precies 64 bytes lang en hadden Data-pakketten precies de lengte van hun payload.

* **H1–H4 als bereiken**: voor elk pakkettype wordt de headerwaarde uit een bereik gekozen. Bij ontvangst wordt elke waarde binnen het betreffende bereik geaccepteerd. De vier bereiken mogen elkaar niet overlappen.

* **I1–I5**: door de gebruiker gedefinieerde UDP-pakketten die vóór elke handshake worden verzonden. Daardoor begint de sessie met verkeer dat lijkt op dat van een gangbaar UDP-protocol in plaats van met een WireGuard-handshake.

Deze verbeteringen maken VPN-verkeer moeilijker te detecteren, met behoud van de hoge snelheid en lage latentie van WireGuard.

!!! Tip "Hoe onderscheid je AmneziaWG 1.0 en 2.0?"

    **V1.0**: er zijn geen S3-S4-parameters; voor H1-H4 is elk een vast geheel getal ingesteld.

    **V2.0**: het is V2.0 als aan een van de onderstaande voorwaarden wordt voldaan:

    - De configuratie bevat S3-S4-parameters.
    - H1-H4 zijn ingesteld als numerieke bereiken.
    - De configuratie bevat aangepaste I1-I5-parameters.

    > Opmerking: I1-I5 worden niet automatisch gegenereerd. Je kunt ze handmatig als extra regels aan het configuratiebestand toevoegen om AmneziaWG-verkeer op andere veelgebruikte protocollen zoals QUIC of WebRTC te laten lijken.

### Parameters {#amneziawg-v20-parameters}

| Parameter | Beschrijving | Beperkingen | Automatisch gegenereerd |
| --------- | ------------ | ----------- | ---------------------- |
| Jc | Het aantal junkpakketten voordat de client de handshake start (om detectie van verkeerskenmerken te verstoren) | 1~128 | 4~12 |
| Jmin | Minimale grootte van willekeurige junkpakketten in bytes; moet samen met Jmax worden ingesteld om de pakketgrootte te bepalen | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax | Maximale grootte van willekeurige junkpakketten | 0 ≤ Jmin < Jmax < 1280 | 0≤ Jmin < Jmax < 1280 |
| S1 | Willekeurige voorvoegsels voor Init-pakketten | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Willekeurige voorvoegsels voor Response-pakketten | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Willekeurige voorvoegsels voor Cookie-pakketten | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Willekeurige voorvoegsels voor Data-pakketten | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | Dynamische headers voor pakkettypen; willekeurige waarden (v1.0) of bereiken (v2.0) | 5~2147483647; H1, H2, H3 en H4 moeten verschillend zijn | 5~2147483647 |
| I1~I5 | Signatuurpakketten om protocollen na te bootsen | Willekeurige reeks bytes in hexadecimale notatie | N.v.t. |

Voorbeeld van een obfuscatiesectie voor v2.0:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1318795025-1318795156
H2 = 1029272944-1029273095
H3 = 966737016-966737098
H4 = 282229905-429495047
```

Bron: [Officiële AmneziaWG-documentatie](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Overzicht {#amneziawg-v31-overview}

<font color="red">**Opmerking**: GL.iNet-routers met firmware v4.11.1 of hoger ondersteunen AmneziaWG 3.1.</font>

AmneziaWG 3.1 behoudt alle obfuscatiemechanismen van v2.0: willekeurige voorvoegsels voor elk pakkettype (**S1–S4**), dynamische headers (**H1–H4**), de signatuurpakketten vóór de handshake (**I1–I5**) en de reeks junkpakketten (**Jc**, **Jmin**, **Jmax**). De volgende mechanismen maken het moeilijker om verkeer aan zijn kenmerken te herkennen:

- **Headerbescherming**: gebruikt ChaCha20 om velden in WireGuard-pakketheaders te verhullen die anders onversleuteld blijven.
- **Opvulling van inhoud**: voegt een willekeurige hoeveelheid opvulling toe aan transportdatapakketten, voor zover er ruimte is binnen de MTU.
- **Instelbare tijden**: maakt het mogelijk waarden of bereiken in te stellen voor sleutelvernieuwing, nieuwe handshakepogingen, keepalives en verwant verbindingsgedrag. Gebruik bij voorkeur de automatisch gegenereerde waarden op zowel de server als de client.
- **Willekeurige achtervoegsels**: voegt achtervoegsels van variabele lengte toe aan handshakepakketten en transportdatapakketten om de pakketgrootte verder te laten variëren.
- **Cookies uitschakelen**: laat een apparaat stoppen met het versturen van cookieantwoorden tijdens de handshake. Het apparaat blijft cookieantwoorden ontvangen en de rest van de handshake verwerken.

### Parameters {#amneziawg-v31-parameters}

AmneziaWG V3.1 introduceert de volgende parameters.

| Parameter | Beschrijving | Beperkingen | Bereik of waarde van GL.iNet |
| --------- | ------------ | ----------- | --------------------------- |
| `HeaderProtectionKey` | Schakelt bescherming met ChaCha20 in voor velden in pakketheaders die anders onversleuteld blijven | Precies 32 bytes. Als de bescherming is ingeschakeld, moeten S1, S2, S3 en S4 allemaal zijn ingesteld op een waarde ≥ 12. De aanbevolen combinatie is `H1=1`, `H2=2`, `H3=3`, `H4=4`. Hiermee wordt het mechanisme voor aangepaste headers uitgeschakeld en verhult de headerbescherming het berichttype | Sleutel van 32 bytes |
| `ContentPaddingAddition` | Voegt aan elk transportdatapakket een willekeurig aantal bytes uit het ingestelde bereik toe | `range<uint16>`, 0–65535, min ≤ max; `0` of `0-0` schakelt deze functie uit | 0–65535 (voorbeeld: `10-50`) |
| `RekeyAfterTime` | Tijd dat de huidige sleutel wordt gebruikt voordat actieve sleutelvernieuwing wordt gestart (seconden) | `range<uint16>`, 0–65535, min ≤ max; bij `0` of `0-0` geldt de standaardwaarde van WireGuard | 100–150 (standaardwaarde van WireGuard: 120) |
| `RekeyTimeout` | Tijd dat een afzonderlijk handshakeverzoek op een antwoord wacht voordat een nieuwe poging wordt gedaan (seconden) | `range<uint16>`, 0–65535, min ≤ max; bij `0` of `0-0` geldt de standaardwaarde van WireGuard | 4–7 (standaardwaarde van WireGuard: 5) |
| `RejectAfterTime` | Tijd zonder ontvangen gegevens waarna de verbinding een nieuwe handshake start (seconden) | `range<uint16>`, 0–65535, min ≤ max; bij `0` of `0-0` geldt de standaardwaarde van WireGuard | 180–240 (standaardwaarde van WireGuard: 180) |
| `KeepaliveTimeout` | Tijd zonder verzonden gegevens waarna een intern keepalivebericht wordt verzonden (seconden) | `range<uint16>`, 0–65535, min ≤ max; bij `0` of `0-0` geldt de standaardwaarde van WireGuard | 8–20 (standaardwaarde van WireGuard: 10) |
| `MaxHandshakeAttempts` | Maximaal aantal nieuwe handshakepogingen | `range<uint16>`, 0–65535, min ≤ max; bij `0` of `0-0` geldt de standaardwaarde van WireGuard | 12–18 (standaardwaarde van WireGuard: 18) |
| `RandomTrailers` | Voegt een variabel aantal bytes toe aan het einde van pakketten: willekeurige gegevens bij handshakepakketten en nullen na het ingesloten IP-pakket bij transportpakketten. De lengte van het achtervoegsel wordt zo gekozen dat de MTU aan geen van beide kanten wordt overschreden | `off` schakelt deze functie uit. Bij inschakeling wordt `S1 = S2 = S3 = S4` aanbevolen om het risico te beperken dat willekeurige pakketgroottes leiden tot een onjuiste herkenning van het pakkettype | `on` / `off` |
| `DisableCookies` | Voorkomt dat het lokale apparaat cookieantwoorden tijdens de handshake verzendt. Het ontvangen van cookieantwoorden van de peer en de overige verwerking van de handshake veranderen niet | `off` schakelt deze functie uit. S3/H3 moeten geldige waarden houden, omdat ze bij ontvangst nog gebruikt kunnen worden | `on` / `off` |

**Opmerkingen**

* Je kunt de router waarden laten genereren binnen de bereiken in de laatste kolom. `RandomTrailers` en `DisableCookies` schakel je per apparaat in of uit.
* `HeaderProtectionKey` moet op de client en de server identiek zijn.
* Tijdens gebruik worden tijdwaarden buiten de vermelde bereiken vervangen door willekeurige waarden binnen de bereiken. Een aangepaste waarde wordt dus mogelijk niet precies toegepast zoals ingevoerd.
* `ContentPaddingAddition` en `S4` wijzigen allebei de lengte van transportpakketten, maar werken op verschillende delen van het pakket en kunnen tegelijk worden gebruikt.
* Headerbescherming kan samengaan met dynamische `H`-waarden: `H1–H4` kunnen dynamisch blijven, al is `1/2/3/4` de aanbevolen instelling.

---

Voorbeeld van een obfuscatiesectie voor v3.1:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

Bron: [Officiële AmneziaWG-documentatie](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Gerelateerd artikel:

- [VPN-obfuscatie instellen op GL.iNet-routers](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
