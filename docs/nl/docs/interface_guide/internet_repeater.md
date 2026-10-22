# Via Repeater verbinding maken met een bestaand Wi-Fi-netwerk {#connect-to-the-internet-via-an-existing-wi-fi-by-repeater}

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Met Repeater verbind je de router met een bestaand draadloos netwerk, bijvoorbeeld gratis Wi-Fi in een hotel of café.

Repeater werkt standaard in de WISP-modus (Wireless Internet Service Provider). De router maakt een eigen subnet en werkt als firewall om je tegen het openbare netwerk te beschermen.

## Basisstappen {#basic-steps}

Meld je aan bij het webbeheerpaneel van de router, ga naar **INTERNET** -> het gedeelte **Repeater** en klik op **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Kies in de lijst met beschikbare netwerken het Wi-Fi-netwerk waarmee je verbinding wilt maken.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

!!! note

    1. De pagina toont de Wi-Fi-kanalen die je router ondersteunt. Controleer of het netwerk waarmee je verbinding wilt maken een van deze kanalen gebruikt. Anders verschijnt het mogelijk niet in de lijst.

    2. Houd bij het zoeken naar een iPhone Personal Hotspot het iPhone-scherm ontgrendeld, zodat continu Wi-Fi-beacons worden verzonden. Anders detecteert de router de hotspot mogelijk niet.

Voer het juiste Wi-Fi-wachtwoord in en klik op **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Als de gewenste Wi-Fi-SSID niet in Available Network staat, klik je rechtsboven op **Join Other Network** en voer je de SSID en andere vereiste gegevens handmatig in. Raadpleeg [deze stappen](#join-other-network) voor meer informatie.

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Raadpleeg [For Public Hotspot](#for-public-hotspot) voor verbinding met een openbare hotspot in bijvoorbeeld een hotel, luchthaven of winkelcentrum.

Raadpleeg [Advanced Settings](#advanced-settings) voor overige instellingen.

Als het wachtwoord correct is, wordt de verbinding na enige tijd tot stand gebracht.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Voor openbare hotspots {#for-public-hotspot}

Bij verbinding met een openbare hotspot met captive portal kunnen de volgende functies de kans op een geslaagde verbinding vergroten.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    Deze functie is beschikbaar sinds v4.6.

    Wanneer deze optie is ingeschakeld, activeert de router automatisch Login Mode for Public Hotspots als er wel verbinding met een hotspot is maar geen internettoegang. **In deze modus worden sommige diensten onderbroken en wordt DNS automatisch ingesteld.** Hierdoor kan je netwerkactiviteit zichtbaar worden voor de hotspotaanbieder, zoals een hotel of winkelcentrum.

    Ook als deze optie niet is ingeschakeld, vraagt de router deze modus te activeren wanneer een captive portal wordt gedetecteerd en aanmelden mislukt.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    Wanneer dit is ingeschakeld, doet de router zich voor als het clientapparaat waarmee je het beheerpaneel opent door het MAC-adres van dat apparaat na te bootsen.

- **MAC Mode**

    Je kunt kiezen welk MAC-adres de router gebruikt voor de verbinding met de openbare hotspot.

    - **Factory**: gebruikt het oorspronkelijke MAC-adres dat in de fabriek aan het apparaat is toegewezen.

    - **Clone**: kloont het MAC-adres van een clientapparaat voor de verbinding. Voer het gewenste adres handmatig in als het niet in de lijst staat.

        **Opmerking**: veel moderne apparaten gebruiken bij Wi-Fi-verbindingen willekeurige MAC-adressen, vaak Private Wi-Fi Address of random hardware address genoemd. Het hier weergegeven MAC-adres komt daardoor mogelijk niet overeen met het fysieke MAC-adres.

    - **Random**: genereert automatisch een willekeurig MAC-adres voor de verbinding.

    Bij het opslaan van de netwerkconfiguratie wordt MAC Mode, inclusief een gekloond of willekeurig MAC-adres, aan de betreffende SSID gekoppeld. Je kunt deze instellingen per SSID op elk moment handmatig wijzigen.

- **Auto Update MAC**: als deze optie is ingeschakeld, kan het MAC-adres automatisch worden bijgewerkt.

## Advanced Settings {#advanced-settings}

Bij het verbinden met het netwerk zijn aanvullende opties beschikbaar.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: schakel dit in om het huidige herhaalde Wi-Fi-netwerk te onthouden.

* **Lock BSSID**: wanneer dit is ingeschakeld, maakt de router alleen verbinding met het specifieke access point dat bij de geselecteerde BSSID hoort, ook als andere access points dezelfde SSID gebruiken.

* **Manually Set Static IP**: wanneer dit is ingeschakeld, kun je voor de Repeater-verbinding handmatig een vast IPv4-adres, subnetmasker, gateway en DNS-servers instellen in plaats van deze automatisch te verkrijgen.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL (Time To Live) bepaalt hoe lang pakketten maximaal in het netwerk kunnen blijven en wordt volgens de eisen van de provider ingevuld. De router stuurt standaard de TTL van het inkomende clientapparaat min één door. TTL geldt alleen voor IPv4.

    **Opmerking**: stel hier een vaste waarde in als camouflage nodig is. Voer voor de meeste modellen de gewenste effectieve TTL plus 1 in om de automatische verlaging te compenseren. Mudi 7 (GL‑E5800) past de ingevoerde waarde ongewijzigd toe.

* **HL**: bij IPv6 beperkt het veld HL (Hop Limit) het aantal overdrachtshops van gegevenspakketten in het netwerk en is het gelijkwaardig aan TTL bij IPv4.

* **MTU**: de standaardwaarde is 1500.

## Repeater-opties {#repeater-options}

Klik rechtsboven op het tandwielpictogram om Repeater-opties te configureren.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

De pagina kan per firmwareversie verschillen.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching to Other Saved Networks**: wanneer dit is ingeschakeld, maakt de router automatisch verbinding met andere opgeslagen netwerken als het huidige Wi-Fi-netwerk niet beschikbaar is.

* **Band Selection**: als je handmatig een band selecteert, scant en gebruikt de router alleen Wi-Fi-netwerken in deze frequentieband.

## Bekende netwerken beheren {#manage-known-network}

Klik op **Switch Network** om bekende netwerken te beheren.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Je kunt ook in het gedeelte Repeater op **Connect** klikken als er geen netwerk verbonden is.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Klik in het gedeelte **Known Networks** op het prullenbakpictogram om een bekend netwerk te verwijderen of op het tandwielpictogram om het netwerk te configureren.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Verbinding maken met een ander netwerk {#join-other-network}

Als de SSID niet in Available Networks staat of verborgen is, klik je op **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Voer de SSID in, selecteer Security en voer zo nodig het wachtwoord in.

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

Afhankelijk van het model zijn er twee of drie opties voor **Security**.

* None: er is geen wachtwoord vereist.
* WPA/WPA2/WPA3: veelgebruikt en door bijna alle Wi-Fi-netwerken ondersteund.
* WPA/WPA2/WPA3 Enterprise: vereist Extensible Authentication Protocol (EAP) voor verificatie. Voor de verbinding zijn een geldige gebruikersnaam en wachtwoord nodig. Dit wordt meestal in bedrijfs- of campusnetwerken gebruikt.

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    Klik [hier](../tutorials/eap.md){target="_blank"} voor uitgebreide instructies over het herhalen van EAP-netwerken.

## Opnieuw verbinden {#reconnection}

In de volgende gevallen probeert de router periodiek automatisch opnieuw verbinding te maken met Wi-Fi. Je kunt dit zo nodig handmatig uitschakelen. Verwijder bij fouten in de SSID of het wachtwoord het netwerk uit Known Networks.

1. Tijdens de Repeater-installatie is een onjuiste SSID of een onjuist wachtwoord ingevoerd.

2. De router is na de eerste verbinding buiten het bereik van de upstream router verplaatst.

3. De upstream router heeft de SSID of het wachtwoord gewijzigd of beperkt na de verbinding de toegang.

Het proces voor opnieuw verbinden bestaat uit een wachtfase, scanfase en verbindingsfase.

1. Wachtfase: de router wacht totdat opnieuw verbinding kan worden gemaakt.

2. Scanfase: in de gescande frequentieband kan pakketverlies optreden. Nieuwe apparaten kunnen verbindingsproblemen ondervinden. Bij GL-AXT1800/GL-AX1800 wordt Guest Wi-Fi tijdelijk uitgeschakeld.

3. Verbindingsfase: de hoofd-Wi-Fi in de doelband kan tijdens het opnieuw verbinden enkele seconden wegvallen.

**Opmerking**: problemen treden meestal in de scan- en verbindingsfase op.

## Probleemoplossing {#troubleshooting}

Als de router als repeater met een Wi-Fi-netwerk is verbonden maar internet niet beschikbaar is, verschijnt de onderstaande gele melding.

**"De interface is verbonden, maar internet is niet toegankelijk."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Voer de volgende stappen uit om dit probleem te verhelpen:

1. Controleer of het upstream apparaat, het Wi-Fi-netwerk waarmee de router is verbonden, internettoegang heeft.

2. Ga naar de pagina [Multi-WAN](multi-wan.md) om de status van de Repeater-interface te controleren.

## DFS {#dfs}

**DFS** (Dynamic Frequency Selection) schakelt automatisch van Wi‑Fi-kanaal om interferentie met radarsignalen te vermijden. Bij verbinding met upstream 5G-Wi-Fi volgt de Wi-Fi van de router het upstream netwerk bij het wel of niet gebruiken van een DFS-kanaal.

* Als upstream Wi-Fi een DFS-kanaal gebruikt en kan worden gescand, gebruikt de 5G-Wi-Fi van de router hetzelfde kanaal.

* De 5G-Wi-Fi van de router schakelt naar een niet-DFS-kanaal als upstream Wi-Fi niet kan worden gescand of de verbinding mislukt.

??? "Ondersteunde modellen"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Niet-ondersteunde modellen"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Gerelateerde artikelen

- [Internetpagina](internet.md)
- [Hoe stel je de prioriteit van elke methode voor internettoegang in?](multi-wan.md)
- [Hoe stel je load balancing in wanneer meerdere methoden voor internettoegang tegelijk worden gebruikt?](multi-wan.md)
- [De LAN- en Wi-Fi-MAC-adressen vinden](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
