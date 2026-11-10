# AmneziaWG-obfuskering {#amneziawg-obfuscation}

AmneziaWG är ett WireGuard-baserat VPN-protokoll med inbyggd trafikobfuskering. Obfuskeringsparametrarna styr hur trafiken döljs för att undvika identifiering vid restriktiv nätverksinspektion.

Nedan beskrivs AmneziaWG och skillnaderna mellan versionerna i detalj.

## Varför AmneziaWG? {#why-amneziawg}

Föregångaren WireGuard har etablerat sig som ett snabbt och tillförlitligt VPN-protokoll tack vare sin kompakta kodbas och höga effektivitet. Dess fasta pakethuvuden och förutsägbara paketstorlekar skapar dock ett mönster som är lätt att känna igen. DPI-system kan utan problem identifiera paketen och omedelbart avsluta anslutningarna, vilket är ett allvarligt problem i länder med strikt internetcensur.

AmneziaWG behåller den ursprungliga WireGuard-implementationens enkla arkitektur och höga prestanda men lägger till en särskild obfuskeringsmodul som döljer VPN-trafikens mönster. Det hjälper privat- och företagsanvändare att skydda sin integritet på internet och behålla stabila anslutningar i restriktiva nätverksmiljöer.

Kortfattat:

- Protokollet maskerar VPN-egenskaper så att internetleverantörer, brandväggar och Deep Packet Inspection (DPI) inte kan identifiera dem.

- VPN-anslutningen ser ut som vanlig webbtrafik, vilket förbättrar stabiliteten och anslutningsgraden i begränsade nätverk.

## AmneziaWG V2.0 {#amneziawg-v20}

### Översikt {#amneziawg-v20-overview}

<font color="red">**Obs!** GL.iNet-routrar med firmware v4.9.0 eller senare stöder AmneziaWG 2.0.</font>

AmneziaWG 2.0 behåller obfuskeringsmekanismerna från v1.0: serien med skräppaket (**Jc**, **Jmin**, **Jmax**) och slumpmässiga prefix för Init- och Response-paket (**S1–S2**). Följande mekanismer döljer de delar av anslutningen som fortfarande var förutsägbara:

* **S3–S4**: slumpmässiga prefix för Cookie- och Data-paket. I v1.0 fick bara Init- och Response-paketen utfyllnad. Därför var Cookie-paketen exakt 64 byte långa och Data-paketen exakt lika långa som nyttolasten.

* **H1–H4 som intervall**: huvudvärdet för varje pakettyp väljs från ett intervall i stället för att vara ett fast tal. Vid mottagning godtas alla värden inom respektive intervall. De fyra intervallen får inte överlappa varandra.

* **I1–I5**: användardefinierade UDP-paket som skickas före varje handskakning. Sessionen börjar därmed med trafik som liknar ett vanligt UDP-protokoll i stället för en WireGuard-handskakning.

Förbättringarna gör VPN-trafiken svårare att identifiera samtidigt som WireGuards höga hastighet och låga latens behålls.

!!! Tip "Hur skiljer du mellan AmneziaWG 1.0 och 2.0?"

    **V1.0**: Inga S3-S4-parametrar. H1-H4 är fasta heltal.

    **V2.0**: Det är V2.0 om något av följande villkor är uppfyllt:

    - Parametrarna S3-S4 ingår
    - H1-H4 är angivna som numeriska intervall
    - Anpassade I1-I5-parametrar ingår.

    > Obs! I1-I5 genereras inte automatiskt. Du kan lägga till dem manuellt som extra rader i konfigurationsfilen för att få AmneziaWG-trafiken att likna andra vanliga protokoll, till exempel QUIC eller WebRTC.

### Parametrar {#amneziawg-v20-parameters}

| Parameter    | Beskrivning                    | Begränsningar     | Genereras automatiskt   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Antalet skräppaket innan klienten inleder handskakningen (för att störa identifiering av trafikegenskaper) | 1~128 | 4~12 |
| Jmin         | Minsta storlek för slumpmässiga skräppaket (byte). Måste konfigureras tillsammans med Jmax för att definiera skräppaketens storlek | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Största storlek för slumpmässiga skräppaket     | 0 ≤ Jmin < Jmax < 1280         | 0≤ Jmin < Jmax < 1280 |
| S1           | Slumpmässiga prefix för Init-paket         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Slumpmässiga prefix för Response-paket     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Slumpmässiga prefix för Cookie-paket       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Slumpmässiga prefix för Data-paket         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamiska huvuden för pakettyper, med slumpmässiga värden (v1.0) eller intervall (v2.0)   | 5~2147483647; H1, H2, H3 och H4 måste skilja sig från varandra | 5~2147483647 |
| I1~I5        | Signaturpaket för protokollimitation | godtycklig bytesekvens i hexadecimal form             | Ej tillämpligt |

Exempel på en obfuskeringssektion för v2.0:

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

Referens: [Officiell AmneziaWG-dokumentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Översikt {#amneziawg-v31-overview}

<font color="red">**Obs!** GL.iNet-routrar med firmware v4.11.1 eller senare stöder AmneziaWG 3.1.</font>

AmneziaWG 3.1 behåller alla obfuskeringsmekanismer från v2.0: slumpmässiga prefix för varje pakettyp (**S1–S4**), dynamiska pakethuvuden (**H1–H4**), signaturpaketen som skickas före handskakningen (**I1–I5**) och serien med skräppaket (**Jc**, **Jmin**, **Jmax**). Följande nya mekanismer gör det svårare att känna igen trafiken på dess mönster:

- **Skydd av pakethuvuden**: använder ChaCha20 för att dölja fält i WireGuard-paketens huvuden som annars skulle förbli okrypterade.
- **Utfyllnad av innehåll**: lägger till en slumpmässig mängd utfyllnad i transportdatapaket, inom det utrymme som MTU medger.
- **Anpassade tidsinställningar**: låter dig ange värden eller intervall för nyckelbyte, nya handskakningsförsök, meddelanden som håller anslutningen vid liv och relaterade anslutningsfunktioner. Använd helst de automatiskt genererade värdena på både servern och klienten.
- **Slumpmässiga suffix**: lägger till suffix av varierande längd i handskakningspaket och transportdatapaket för att få paketstorlekarna att variera ytterligare.
- **Inaktivera cookies**: låter en enhet sluta skicka cookiesvar under handskakningen. Enheten kan fortfarande ta emot cookiesvar och hantera resten av handskakningen.

### Parametrar {#amneziawg-v31-parameters}

AmneziaWG V3.1 introducerar följande parametrar.

| Parameter | Beskrivning | Begränsningar | Intervall eller värde för GL.iNet |
| --------- | ----------- | ------------- | -------------------------------- |
| `HeaderProtectionKey` | Aktiverar ChaCha20-baserat skydd för fält i pakethuvuden som annars är okrypterade | Exakt 32 byte. När skyddet är aktiverat måste S1, S2, S3 och S4 vara angivna, vart och ett med ett värde ≥ 12. Den rekommenderade kombinationen är `H1=1`, `H2=2`, `H3=3`, `H4=4`. Då inaktiveras mekanismen för anpassade pakethuvuden och meddelandetypen döljs i stället av skyddet för pakethuvuden | Nyckel på 32 byte |
| `ContentPaddingAddition` | Lägger till ett slumpmässigt antal byte i varje transportdatapaket. Antalet väljs inom det angivna intervallet för varje paket | `range<uint16>`, 0–65535, min ≤ max. `0` eller `0-0` inaktiverar funktionen | 0–65535 (exempel: `10-50`) |
| `RekeyAfterTime` | Hur länge den aktuella nyckeln används innan ett aktivt nyckelbyte inleds (sekunder) | `range<uint16>`, 0–65535, min ≤ max. `0` eller `0-0` använder WireGuards standardvärde | 100–150 (WireGuards standardvärde: 120) |
| `RekeyTimeout` | Hur länge en enskild handskakningsbegäran väntar på svar innan ett nytt försök görs (sekunder) | `range<uint16>`, 0–65535, min ≤ max. `0` eller `0-0` använder WireGuards standardvärde | 4–7 (WireGuards standardvärde: 5) |
| `RejectAfterTime` | Hur länge anslutningen kan gå utan att ta emot data innan en ny handskakning inleds (sekunder) | `range<uint16>`, 0–65535, min ≤ max. `0` eller `0-0` använder WireGuards standardvärde | 180–240 (WireGuards standardvärde: 180) |
| `KeepaliveTimeout` | Hur länge anslutningen kan gå utan att skicka data innan ett internt meddelande skickas för att hålla anslutningen vid liv (sekunder) | `range<uint16>`, 0–65535, min ≤ max. `0` eller `0-0` använder WireGuards standardvärde | 8–20 (WireGuards standardvärde: 10) |
| `MaxHandshakeAttempts` | Högsta antal nya handskakningsförsök | `range<uint16>`, 0–65535, min ≤ max. `0` eller `0-0` använder WireGuards standardvärde | 12–18 (WireGuards standardvärde: 18) |
| `RandomTrailers` | Lägger till ett varierande antal byte i slutet av paketen: slumpmässiga data i handskakningspaket och nollor efter det inre IP-paketet i transportpaket. Suffixets längd väljs dynamiskt så att MTU inte överskrids på någon sida | `off` inaktiverar funktionen. När funktionen är aktiverad rekommenderas `S1 = S2 = S3 = S4` för att minska risken för att varierande paketstorlekar gör att pakettypen identifieras felaktigt | `on` / `off` |
| `DisableCookies` | Hindrar den lokala enheten från att skicka cookiesvar under handskakningen. Mottagningen av cookiesvar från motparten och övrig hantering av handskakningen påverkas inte | `off` inaktiverar funktionen. S3/H3 måste fortfarande ha giltiga värden eftersom de kan användas vid mottagning | `on` / `off` |

**Anmärkningar**

* Du kan låta routern generera värden inom intervallen i den sista kolumnen. `RandomTrailers` och `DisableCookies` aktiveras eller inaktiveras per enhet.
* `HeaderProtectionKey` måste vara identisk på klienten och servern.
* Under drift ersätts tidsvärden utanför de angivna intervallen med slumpmässiga värden inom intervallen. Ett anpassat värde kanske därför inte används exakt som det angavs.
* Både `ContentPaddingAddition` och `S4` ändrar transportpaketets längd, men påverkar olika delar av paketet och kan användas samtidigt.
* Skydd av pakethuvuden kan kombineras med dynamiska `H`-värden. `H1–H4` kan förbli dynamiska, även om `1/2/3/4` är den rekommenderade inställningen.

---

Exempel på en obfuskeringssektion för v3.1:

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

Referens: [Officiell AmneziaWG-dokumentation](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}


---

Relaterad artikel:

- [Konfigurera VPN-obfuskering på GL.iNet-routrar](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
