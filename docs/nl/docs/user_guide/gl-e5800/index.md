# Gebruikershandleiding Mudi 7 (GL-E5800) {#mudi-7-gl-e5800-user-guide}

## Productoverzicht {#product-overview}

Mudi 7 is een draagbare 5G NR Wi-Fi 7-reisrouter voor mensen die veel onderweg zijn en zakenreizigers. De router biedt betrouwbare privénetwerken die gegevens tegen cyberdreigingen beschermen. Met zeer snel 5G, automatische dual-simoverschakeling (failover) en Wi-Fi 7 (320MHz-kanalen en 4K QAM) biedt hij stabiele, snelle verbindingen voor snelle downloads, 4K-streaming en videoconferenties zonder vertraging, ook in drukke gebieden.

Via het touchscreen van Mudi 7 kun je realtime het datagebruik, de signaalsterkte, verbonden apparaten en clientsnelheid bewaken en instellingen met eenvoudige tikken aanpassen.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

- 1 x Mudi 7 (GL-E5800)
- 1 x Accu
- 1 x 10Gbps USB-C-kabel
- 1 x Reisetui
- 1 x Gebruikershandleiding

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Bekijk hieronder de uitpakvideo van Mudi 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Mudi 7 instellen {#how-to-set-up-mudi-7}

Bekijk deze installatievideo of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Simkaart installeren {#1-install-sim-card}

Installeer een of meer nano-simkaarten in Mudi 7. Als je liever eSIM gebruikt, sla je dit over en ga je verder met stap 2.

Gebruik eerst de kleine inkeping rechtsonder in het achterdeksel als aangrijpingspunt. Wrik langs de naad om een opening te maken, open het achterdeksel en verwijder vervolgens de accu van Mudi 7.

!!! Warning

    Stop met het gebruik van het apparaat als de accu is opgezwollen, lekt, ongewoon heet of beschadigd is of moeilijk kan worden verwijderd. Probeer de accu niet te verwijderen. Raadpleeg [Veiligheid van de accu](#battery-safety).

![small notch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/notch.png){class="glboxshadow"}

![remove battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery1.png){class="glboxshadow"}

Plaats vervolgens de nano-simkaart(en). Gebruik bij één kaart bij voorkeur SIM 1.

![sim slots](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/sim-slots.png){class="glboxshadow"}

Plaats ten slotte de accu en het deksel terug.

![restore battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery2.png){class="glboxshadow"}

### 2. Inschakelen {#2-power-on}

Houd de Power-knop **3 seconden** ingedrukt of sluit een voedingsadapter aan.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power-button.png){class="glboxshadow"}

### 3. Basisinstellingen {#3-basic-settings}

Volg de instructies op het scherm om basisinstellingen te configureren, waaronder **screen passcode**, **admin password**, **Wi-Fi name**, **Wi-Fi password** en **frequency bands**.

**Tip**: het standaardbeheerderswachtwoord bestaat uit de laatste 9 tekens van het serienummer van het apparaat, gevolgd door een #-teken. Je kunt het standaardwachtwoord gebruiken of een aangepast wachtwoord instellen.

### 4. Internet instellen {#4-internet-setup}

Configureer je Mudi 7 met een van de ondersteunde methoden voor internetverbindingen: Cellular, Ethernet, Repeater, Tethering of USB Ethernet. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je meerdere internetverbindingen in.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}

    Mudi 7 heeft een **ingebouwde eSIM** en **twee nano‑simkaartsleuven**. Je kunt verbinding met internet maken door een eSIM-pakket te kopen, waarvoor geen fysieke simkaart nodig is, of nano‑simkaarten plaatsen voor toegang tot het mobiele 5G-netwerk.

    **eSIM instellen**:

    1. Ga op het touchscreen naar **Cellular** -> **SIM Card Switch** en zet de schakelaar om om **eSIM in te schakelen**.

        ![enable esim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/lcd_enable_esim.png){class="glboxshadow" width="590"}

    2. Meld je aan bij het [webbeheerpaneel](./index.md#log-in-to-web-admin-panel) en ga naar **INTERNET** -> **Cellular** -> **eSIM Management**.

        ![esim management](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/esim_management.png){class="glboxshadow" width="590"}

    3. Klik onderaan het pop-upvenster op **Add eSIM Profile**.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile1.png){class="glboxshadow" width="590"}

        **Opmerking**: zorg dat je apparaat met internet is verbonden voordat je gaat uploaden. Door een netwerkfout mislukt het uploaden van het eSIM-configuratiebestand.

        Upload je eSIM-profiel via een QR-code of activeringscode en klik op **Install**. De meeste eSIM-profielen kunnen slechts eenmaal worden gedownload en toegevoegd.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile2.png){class="glboxshadow"}

        **Tip**: als je nog geen eSIM-profiel hebt gekocht, kun je er een kopen in de eSIM Profile Recommended Store.

        ![recommended store](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/recommended_store.png){class="glboxshadow" width="590"}

    4. Ga na het uploaden naar **Cellular** en klik op **SIM Card Switch**.

        ![sim card switch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/sim_card_switch.png){class="glboxshadow" width="590"}

        Selecteer in het pop-upvenster **eSIM** als actieve simkaart en klik op **Apply**.

        ![active sim card](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/active_sim_card.png){class="glboxshadow"}

    5. De router maakt verbinding via dit eSIM-profiel. Wacht en controleer of de verbinding tot stand wordt gebracht.

    **Nano‑sim instellen**:

    6. Verwijder het achterdeksel en de accu, plaats de nano-simkaart in de sleuf en plaats de accu terug.

    7. De router maakt automatisch verbinding via deze nano‑simkaart. Wacht en controleer of de verbinding tot stand wordt gebracht.

    Zodra de internetverbinding tot stand is gebracht, verschijnen de signaalbalken en de mobiele status rechtsboven op het touchscreen. Je kunt de verbindingsgegevens ook in het webbeheerpaneel bekijken.

    Raadpleeg [Verbinding maken met internet via een mobiel netwerk](../../interface_guide/internet_cellular.md) voor uitgebreide instructies.

    !!! note

        1. De ingebouwde eSIM en SIM 2 sluiten elkaar uit en kunnen niet tegelijk worden geactiveerd. De eSIM is standaard uitgeschakeld. Als je de eSIM inschakelt, werkt SIM 2 niet, ook niet als er een simkaart is geplaatst.
        2. Omdat Mudi 7 een ingebouwde eSIM heeft, wordt een fysieke SIMPoYo eSIM-kaart op Mudi 7 herkend als een gewone simkaart zonder eSIM-functionaliteit.

=== "Ethernet"

    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Sluit de Ethernet-poort van Mudi 7 met een Ethernet-kabel aan op een upstream netwerkbron, zoals een internetmodem, netwerkswitch of Ethernet-wandaansluiting.
    2. Ga op het touchscreen of in het webbeheerpaneel naar **Network** -> **Ethernet Ports**, stel de poortrol in op **WAN** en klik op **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Zodra de internetverbinding tot stand is gebracht, verschijnt rechtsboven op het touchscreen een pictogram van een Ethernet-poort. Je kunt de verbindingsgegevens ook in het webbeheerpaneel bekijken.

    Raadpleeg [Verbinding maken met internet via een Ethernet-kabel](../../interface_guide/internet_ethernet.md) voor uitgebreide instructies.

=== "Repeater"

    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. Ga op het touchscreen of in het webbeheerpaneel naar **Internet** -> **Repeater** en klik op **Connect**. Mudi 7 scant vervolgens naar beschikbare Wi-Fi-netwerken.
    2. Selecteer het Wi-Fi-netwerk dat je met Mudi 7 wilt uitbreiden.
    3. Voer het wachtwoord in en klik op **Apply**.
    4. Zodra de internetverbinding tot stand is gebracht, verschijnt rechtsboven op het touchscreen een Wi-Fi-pictogram. Je kunt de verbindingsgegevens ook in het webbeheerpaneel bekijken.

    Raadpleeg [Verbinding maken met internet via een bestaand Wi-Fi-netwerk](../../interface_guide/internet_repeater.md) voor uitgebreide instructies.

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Sluit je mobiele apparaat, zoals een smartphone of USB-dongle, met een USB-kabel aan op de USB-C-poort van Mudi 7.
    2. Ga op je mobiele apparaat naar Settings en schakel **USB Tethering** in. Tik op een iPhone op **Trust This Device** als daarom wordt gevraagd.
    3. Selecteer **Host (USB OTG) mode** wanneer je op het touchscreen om een USB-modus wordt gevraagd. Mudi 7 maakt vervolgens automatisch verbinding met je apparaat. Herhaal de bovenstaande stappen als er geen verbinding wordt gemaakt, of meld je aan bij het webbeheerpaneel en controleer de Tethering-verbinding op de pagina INTERNET.

        Klik [hier](../../tutorials/what_is_usb-c_otg_and_how_to_share_your_network_via_usb-c_otg.md) voor meer informatie over de verschillen tussen USB-modi.

    4. Zodra de internetverbinding tot stand is gebracht, verschijnt rechtsboven op het touchscreen een kettingschakelpictogram. Je kunt de verbindingsgegevens ook in het webbeheerpaneel bekijken.

    Raadpleeg [Verbinding maken met internet via USB-tethering](../../interface_guide/internet_tethering.md) voor uitgebreide instructies.

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 heeft een USB-C-poort met **OTG-ondersteuning**, waarmee je een tweede Ethernet-poort voor Dual-Ethernet WAN kunt toevoegen. Hiervoor is een **afzonderlijk verkrijgbare USB‑C-naar-Ethernet-adapter** vereist.

    <small>*USB OTG (On-The-Go) is een USB-standaard waarmee compatibele apparaten, zoals routers, kunnen wisselen tussen de host- en randapparaatrol. Hierdoor zijn rechtstreekse gegevensoverdracht en stroominteractie zonder afzonderlijk hostapparaat mogelijk.</small>

    1. Sluit met een USB-C-naar-Ethernet-adapter een upstream netwerkbron, zoals een internetmodem, netwerkswitch of Ethernet-wandaansluiting, aan op de USB-C-poort van Mudi 7.
    2. Ga op het touchscreen of in het webbeheerpaneel naar **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, stel de poortrol in op **WAN** en klik op **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 maakt vervolgens automatisch verbinding met je apparaat. Herhaal de bovenstaande stappen als er geen verbinding wordt gemaakt, of meld je aan bij het webbeheerpaneel en controleer de USB Ethernet-verbinding op de pagina INTERNET.
    4. Zodra de internetverbinding tot stand is gebracht, verschijnen rechtsboven op het touchscreen een USB-pictogram en een Ethernet-poortpictogram. Je kunt de verbindingsgegevens ook in het webbeheerpaneel bekijken.

    Klik [hier](../../tutorials/what_is_usb-c_otg_and_how_to_share_your_network_via_usb-c_otg.md) voor meer informatie over USB-C OTG op Mudi 7.

## Firmware-upgrade {#firmware-upgrade}

!!! Note "Houd vóór het upgraden rekening met het volgende:"

    1. Selecteer op de upgradepagina **Keep Settings** om de configuraties van Mudi 7 te behouden.
    2. Selecteer Keep Settings niet bij een downgrade, omdat er compatibiliteitsproblemen kunnen optreden.
    3. Een firmware-upgrade verbruikt een bepaalde hoeveelheid data. Als de databundel van je simkaart beperkt is, raden we aan de router via een andere methode met internet te verbinden, zoals Repeater of USB Tethering, om extra dataverbruik te voorkomen.

Je kunt de firmware van Mudi 7 via het touchscreen of het webbeheerpaneel upgraden.

### Upgraden via het touchscreen {#upgrade-via-touchscreen}

1. Verbind Mudi 7 met internet.

2. Nadat de verbinding tot stand is gebracht, controleert het systeem automatisch op beschikbare firmware-updates. Als nieuwe firmware beschikbaar is, verschijnt een melding op het scherm. Klik in het pop-upvenster op **Go to Upgrade** om door te gaan.

    ![go to upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade1.png){class="glboxshadow" width="300"}

3. Als het pop-upvenster niet verschijnt, klik je op het startscherm op **More** -> **About Device** -> **Version & Upgrade** -> **Download & Upgrade**. Volg daarna de instructies op het scherm om de firmware te upgraden.

    ![download & upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade2.png){class="glboxshadow" width="300"}

### Upgraden via het web {#upgrade-via-web}

Meld je aan bij het webbeheerpaneel en ga naar **SYSTEM** -> **Upgrade**. Je kunt de firmware van je router online of lokaal upgraden.

Raadpleeg [deze pagina](../../interface_guide/upgrade.md) voor meer informatie.

## Fabrieksreset {#factory-reset}

Je kunt Mudi 7 op drie manieren resetten: rechtstreeks via het touchscreen, met de Reset-knop of via het webbeheerpaneel.

**Opmerking**: zorg dat Mudi 7 volledig is opgestart voordat je een reset uitvoert. Druk NIET direct na het inschakelen op de resetknop, omdat hierdoor de U-Boot-failsafemodus kan worden geactiveerd.

Bekijk deze video of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3Kx_StIFLqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Resetten via het touchscreen {#reset-via-touchscreen}

1. Tik op de startpagina op **More**.

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset1.png){class="glboxshadow" width="300"}

2. Scrol op de pagina More naar beneden en tik op **Reset**.

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset2.png){class="glboxshadow" width="300"}

3. Tik opnieuw op Reset om te bevestigen. De router wordt gereset en start vervolgens opnieuw op.

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset3.png){class="glboxshadow" width="300"}

### Resetten met de knop {#reset-via-button}

1. Verwijder het achterdeksel. De resetknop bevindt zich op de hieronder weergegeven plaats.

    ![reset button](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

2. Voer naar behoefte een soft reset of fabrieksreset uit.

    - **Soft Reset**: als je de netwerkverbinding opnieuw wilt starten zonder gegevens te wissen, houd je de resetknop **4 seconden** ingedrukt en laat je deze vervolgens los om het netwerk te herstellen. Let tijdens het indrukken op de aanwijzingen op het scherm en volg deze. De netwerkinterface wordt opnieuw gestart terwijl je Wi-Fi-instellingen, VPN-configuraties (uitgeschakeld), systeeminstellingen en andere gegevens behouden blijven. Als Wi-Fi is uitgeschakeld, herstelt een soft reset Wi-Fi naar de standaard ingeschakelde status. Je kunt een soft reset ook gebruiken om het apparaat snel van een niet-routermodus naar de routermodus om te schakelen.

    - **Factory Reset**: houd de resetknop **10 seconden** ingedrukt en laat deze vervolgens los om een harde reset uit te voeren. Let tijdens het indrukken op de aanwijzingen op het scherm en volg deze. Alle instellingen worden gewist. Ga voorzichtig te werk.

### Resetten via het web {#reset-via-web}

1. Meld je aan bij het webbeheerpaneel en ga naar **SYSTEM** -> **Reset Firmware**.

2. Klik op **Delete All and Reboot**. De router wordt gereset en start vervolgens opnieuw op.

    ![web reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/web_reset.png){class="glboxshadow"}

## Aanmelden bij het webbeheerpaneel {#log-in-to-web-admin-panel}

Je kunt je aanmelden bij het webbeheerpaneel van Mudi 7 om meer instellingen te configureren of controleren.

Verbind eerst een apparaat, zoals een computer, laptop of smartphone, via Wi-Fi, een Ethernet-kabel of een USB-kabel met Mudi 7.

- **Wi-Fi**

    - <u>QR-code</u>: scan met je apparaat de QR-code op het scherm van Mudi 7. Klik vervolgens op je apparaat op "Join" om verbinding te maken.
    - <u>Manual Connect</u>: ga op je apparaat naar Settings -> WLAN, zoek de Wi-Fi-netwerknaam van Mudi 7 in de lijst met beschikbare netwerken en voer het wachtwoord in om verbinding te maken. De standaardnetwerknaam en het wachtwoord staan op het label.

- **Ethernet**

    Sluit je apparaat met een Ethernet-kabel aan op de Ethernet-poort van Mudi 7, die standaard als LAN-poort werkt.

- **USB**

    Sluit je apparaat met een USB-kabel aan op de USB-C-poort van Mudi 7. Via de USB-C-poort met OTG-ondersteuning kun je in de volgende stap de WebGUI van Mudi 7 openen.

Open vervolgens een webbrowser en voer `192.168.8.1` in de adresbalk in om de aanmeldpagina te openen. Selecteer je taal, stel het beheerderswachtwoord in en klik op **Apply**.

Je bent nu aangemeld bij het webbeheerpaneel van Mudi 7.

Hieronder vind je een overzicht van de functies in het webbeheerpaneel van Mudi 7.

## Wireless {#wireless}

Op de pagina Wireless kun je instellingen voor de 6 GHz-, 5 GHz- en 2.4 GHz-Wi-Fi-netwerken configureren. Je kunt Wi-Fi inschakelen, het TX-vermogen instellen, de Wi-Fi-naam (SSID) opgeven, een willekeurige BSSID inschakelen, de Wi-Fi-beveiligingsmodus en het wachtwoord selecteren, de zichtbaarheid van de SSID configureren en de Wi-Fi-modus, bandbreedte en het kanaal kiezen.

Raadpleeg [Wireless](../../interface_guide/wireless.md) om Wireless in te stellen.

**Opmerking**: de instellingen voor het draadloze netwerk van Mudi 7 verschillen op enkele punten van die van andere GL.iNet Wi-Fi 7-routers.

1. Door hardwarebeperkingen van de chipset kunnen 5 GHz- en 6 GHz-Wi-Fi niet tegelijk worden ingeschakeld.
2. Wanneer Repeater is ingeschakeld, wordt Guest Network automatisch uitgeschakeld.
3. Schakel Wi-Fi volgens de regelgeving naar de modus Outdoor wanneer je het buiten gebruikt. Hierdoor kan het bereik afnemen. Je kunt Usage Environment (Indoor of Outdoor) bovenaan de pagina Wireless wijzigen.

## Clients {#clients}

De pagina Clients toont informatie over verbonden apparaten. Voor elke client worden de naam, het IP- en MAC-adres, de download- en uploadsnelheid en het totale verkeer weergegeven. Je kunt de client ook blokkeren en andere handelingen uitvoeren.

Raadpleeg [Clients](../../interface_guide/clients.md) om Clients in te stellen.

## Clouddiensten {#cloud-services}

=== "GoodCloud"

    De cloudbeheerdienst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} van GL.iNet biedt een eenvoudige manier om GL.iNet-routers op afstand te openen en beheren.

    Raadpleeg [GoodCloud](../../interface_guide/cloud.md) om GoodCloud in te stellen.

=== "AstroWarp"

    AstroWarp is een geavanceerd netwerkplatform voor naadloze externe netwerken en extern apparaatbeheer. AstroWarp is speciaal ontwikkeld voor integratie met GL.iNet-routers en ondersteunt uitgebreid apparaatbeheer voor volledige netwerken, waaronder het beheer van boven- en onderliggende apparaten. Door zich te richten op netwerkbreed beheer en toekomstige ondersteuning voor beheer op hardwareniveau biedt AstroWarp een robuustere en betrouwbaardere oplossing voor apparaatbeheer en het onderhouden van veilige, stabiele netwerken.

    Raadpleeg [AstroWarp](../../interface_guide/astrowarp.md) om AstroWarp in te stellen.

## VPN {#vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk. Mudi 7 ondersteunt OpenVPN en WireGuard.

=== "OpenVPN"

    Mudi 7 en andere GL.iNet-routers ondersteunen het OpenVPN-protocol, dat een sterke beveiliging biedt. Volg deze tutorials om OpenVPN in te stellen:

    * [Een OpenVPN-client instellen](../../interface_guide/openvpn_client.md)
    * [Een OpenVPN-server instellen](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mudi 7 en andere GL.iNet-routers ondersteunen het WireGuard-protocol, dat hoge snelheden en gebruiksgemak biedt. Volg deze tutorials om WireGuard in te stellen:

    * [Een WireGuard-client instellen](../../interface_guide/wireguard_client.md)
    * [Een WireGuard-server instellen](../../interface_guide/wireguard_server.md)

## Netwerk {#network}

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Ethernet, Repeater, Tethering, Cellular en USB Ethernet. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) om Multi-WAN in te stellen.

=== "LAN"

    Een LAN (Local Area Network) is een netwerk dat computers en apparaten binnen een beperkt geografisch gebied, zoals een huis of kantoor, met elkaar verbindt. Het maakt snelle gegevensoverdracht en het delen van bronnen mogelijk, zodat apparaten efficiënt met elkaar kunnen communiceren.

    Raadpleeg [Lan](../../interface_guide/lan.md) om het LAN in te stellen.

=== "Guest Network"

    Je kunt een subnet instellen binnen de privé-IPv4-adresbereiken 192.168.0.0/16, 172.16.0.0/12 of 10.0.0.0/8. Ook kun je de IP-adressen van de gateway en het subnetmasker opgeven en beveiligingsinstellingen, zoals AP-isolatie, voor het gastnetwerk configureren.

    Raadpleeg [Guest Network](../../interface_guide/guest_network.md) om het gastnetwerk in te stellen.

---

=== "DNS"

    Op de pagina DNS kun je aangepaste DNS-servers instellen, bescherming tegen DNS-rebindingaanvallen inschakelen, de DNS-instellingen van alle clients overschrijven en toestaan dat aangepaste DNS de VPN-DNS overschrijft. Je kunt DNS-servers gebruiken die automatisch van upstreamapparaten zijn verkregen of handmatig aangepaste DNS-servers opgeven.

    Raadpleeg [DNS](../../interface_guide/dns.md) om DNS in te stellen.

=== "Ethernet Port"

    Op de pagina Ethernet Port kun je de rol van de Ethernet-poort instellen, bijvoorbeeld WAN of LAN, de MAC-modus en het MAC-adres voor de WAN-interface wijzigen en de onderhandelde poortsnelheid weergeven.

    Mudi 7 heeft één Ethernet-poort die standaard als LAN-poort werkt. Je kunt deze indien nodig via het touchscreen of webbeheerpaneel naar WAN omschakelen.

    Raadpleeg [Ethernet Port](../../interface_guide/ethernet_port.md) om Ethernet-poorten te beheren.

=== "IPv6"

    IPv6, een afkorting van Internet Protocol version 6, is de nieuwste versie van het Internet Protocol en is ontwikkeld als opvolger van IPv4. Het biedt een veel grotere adresruimte en maakt daardoor een vrijwel onbeperkt aantal unieke IP-adressen mogelijk. Dit is noodzakelijk om het groeiende aantal apparaten met een internetverbinding te ondersteunen.

    Raadpleeg [IPV6](../../interface_guide/ipv6.md) om IPV6 in te stellen.

---

=== "IGMP Snooping"

    IGMP snooping is een techniek voor netwerkoptimalisatie die in Ethernet-switches wordt gebruikt om multicastverkeer te beheren en regelen.

    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) om IGMP snooping in te stellen.

=== "Network Mode"

    De netwerkmodus is de configuratie die bepaalt hoe een apparaat verbinding maakt met een netwerk en met andere apparaten communiceert.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) om de netwerkmodus in te stellen.

    **Opmerking**: Mudi 7 ondersteunt de modi Router, Access Point en Extender. De WDS-modus wordt niet ondersteund.

=== "Drop-in gateway"

    Drop-in Gateway breidt de functies van je hoofdrouter uit met AdGuard Home, versleutelde DNS en een VPN-client.

    Raadpleeg de volgende links om een drop-in gateway in te stellen:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Een drop-in gateway instellen](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Netwerkversnelling kan de CPU-belasting verlagen en het doorsturen van verkeerspakketten versnellen.

    Raadpleeg [Network Acceleration](../../interface_guide/network_acceleration.md) om netwerkversnelling in te stellen.

## Flow Control {#flow-control}

=== "Parental Control"

    Parental Control is bedoeld om je te helpen de apparaten van je kinderen te beheren. Je kunt onder meer de schermtijd beperken en toegang tot bepaalde inhoud blokkeren.

    Raadpleeg [Parental Control](../../interface_guide/parental_control.md) om ouderlijk toezicht in te stellen.

## Security {#security}

=== "Port Forwarding"

    Met port forwarding kunnen externe servers en apparaten op internet toegang krijgen tot apparaten in een privénetwerk.

    Raadpleeg [Port Forwarding](../../interface_guide/port_forwarding.md) om port forwarding in te stellen.

=== "Management Control"

    Met Management Control kun je verschillende beveiligingsinstellingen configureren om je netwerk en router tegen onbevoegde toegang te beschermen. De pagina bevat de volgende opties:

    * Local Access Control: beheer en beperk de toegang tot de routerinterface vanaf apparaten die met je lokale netwerk zijn verbonden.
    * Remote Access Control: configureer en beperk toegang tot de routerinterface vanaf externe locaties via internet om de beveiliging tegen bedreigingen van buitenaf te verbeteren.
    * Open Ports on Router: bepaal welke poorten op de router geopend zijn om mogelijke kwetsbaarheden en onbevoegde toegang te beperken.

    Met deze instellingen onderhoud je een veilige netwerkomgeving en bescherm je zowel de router als de verbonden apparaten.

    Raadpleeg [Security](../../interface_guide/security.md) voor uitgebreide instructies.

=== "NAT Mode"

    Op de pagina NAT Mode kun je de functies Full Cone NAT en SIP ALG in- of uitschakelen.

    Raadpleeg [NAT Mode](../../interface_guide/nat_settings.md) om de NAT-instellingen te configureren.

## Toepassingen {#applications}

=== "Plug-ins"

    Een plug-in is een softwareonderdeel dat specifieke functies of mogelijkheden aan een bestaand computerprogramma toevoegt, zodat de mogelijkheden van het programma kunnen worden aangepast en uitgebreid.

    Raadpleeg [Plug-ins](../../interface_guide/plugins.md) om plug-ins in te stellen.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecteert en actualiseert automatisch en in realtime het IP-adres dat aan een domein is gekoppeld. Het koppelt een domeinnaam aan het dynamische openbare IP-adres van je router, zodat je zonder statisch IP-adres op afstand toegang hebt tot je netwerk.

    Raadpleeg [Dynamic DNS](../../interface_guide/ddns.md) om Dynamic DNS in te stellen.

=== "Network Storage"

    Netwerkopslag is een centrale oplossing voor gegevensopslag waarmee meerdere gebruikers en apparaten via een netwerk bestanden kunnen openen en delen.

    Raadpleeg [Network Storage](../../interface_guide/network_storage.md) om netwerkopslag in te stellen.

---

=== "AdGuard Home"

    AdGuard Home blokkeert advertenties en trackers in het hele netwerk. De toepassing werkt als DNS-server en filtert ongewenste inhoud op alle apparaten die met een thuisnetwerk zijn verbonden.

    Raadpleeg [AdGuard Home](../../interface_guide/adguardhome.md) om AdGuard Home in te stellen.

=== "ZeroTier"

    ZeroTier is een softwaregedefinieerde netwerkoplossing waarmee gebruikers via internet beveiligde virtuele netwerken kunnen maken en apparaten kunnen verbinden alsof ze zich in hetzelfde lokale netwerk bevinden.

    Raadpleeg [ZeroTier](../../interface_guide/zerotier.md) om ZeroTier in te stellen.

=== "Tailscale"

    Tailscale is een VPN-dienst waarmee je overal toegang hebt tot je apparaten en toepassingen.

    Raadpleeg [Tailscale](../../interface_guide/tailscale.md) om Tailscale in te stellen.

=== "Tor"

    Tor, een afkorting van The Onion Router, is een privacygericht netwerk dat anonieme communicatie via internet mogelijk maakt. Internetverkeer wordt via een reeks door vrijwilligers beheerde servers (nodes) geleid om de locatie en het gebruik van de gebruiker te verhullen. Hierdoor zijn online activiteiten moeilijk te traceren.

    Raadpleeg [Tor](../../interface_guide/tor.md) om Tor in te stellen.

## Systeem {#system}

=== "Overview"

    De pagina Overview biedt een uitgebreid overzicht van de huidige status en prestatiegegevens van je router. Op deze pagina kun je het volgende bekijken:

    * CPU Average Load: bewaak de gemiddelde belasting van de CPU van je router om de prestaties te beoordelen en mogelijke knelpunten op te sporen.
    * Memory Usage: controleer hoeveel geheugen van je router in gebruik is om het beheer van bronnen te ondersteunen.
    * LED Control: schakel de leds van de router in of uit om de visuele indicatoren van het apparaat aan te passen.
    * Flash Usage: bekijk het gebruik van de flashopslag van de router en controleer of er voldoende ruimte is voor firmware en configuratiegegevens.
    * Device Info: bekijk uitgebreide systeeminformatie over je router, waaronder uptime, hostnaam, model, architectuur, OpenWrt-versie, kernelversie, apparaat-ID, MAC-adres van het apparaat en serienummer van het apparaat.
    * External Storage: controleer de status van externe opslagapparaten die op de router zijn aangesloten, zoals USB-stations of TF-kaarten.

    Deze functies bieden essentiële informatie en bedieningselementen om de werking van je router effectief te beheren en bewaken.

    Raadpleeg [Overview](../../interface_guide/system_overview.md) voor uitgebreide instructies.

=== "Admin Password"

    Op de pagina Admin Password kun je het wachtwoord voor de beheerinterface van de router instellen of wijzigen.

    Het beheerderswachtwoord moet aan de volgende eisen voldoen:

    * Minimaal 10 en maximaal 63 tekens.
    * De volgende tekens zijn toegestaan: letters (hoofdlettergevoelig), cijfers en symbolen `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Er zijn ten minste twee van de volgende typen vereist: hoofdletters, kleine letters, cijfers en symbolen.

=== "Upgrade"

    De pagina Upgrade wordt gebruikt om de firmware van je router bij te werken naar de nieuwste versie, voor betere prestaties en beveiliging en nieuwe functies. Deze pagina biedt twee opties voor upgrades:

    * Firmware Online Upgrade: controleer automatisch op de server van de fabrikant of de nieuwste firmwareversie beschikbaar is. Als deze online beschikbaar is, kun je de nieuwste versie installeren.
    * Firmware Local Upgrade: upload handmatig een firmwarebestand vanaf je computer om de router bij te werken. Zo bepaal je zelf de versie en het moment van de upgrade.

    Met deze opties houd je je router bijgewerkt met de nieuwste verbeteringen en correcties.

    Raadpleeg [Upgrade](../../interface_guide/upgrade.md) voor uitgebreide instructies.

---

=== "Scheduled Tasks"

    Op de pagina Scheduled Tasks kun je de router configureren om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor uitgebreide instructies.

    **Opmerking**: Mudi 7 ondersteunt geen schema voor het ledscherm of de Wi-Fi-status.

=== "Display Management"

    Op de pagina Display Management kun je het touchscreen en de bijbehorende instellingen beheren.

    - Wallpaper: pas de achtergrond en de weergavestijl bij activering aan.
    - Brightness: pas de helderheid van het touchscreen aan. Gebruik de schuifregelaar of voer een percentage in dat bij de lichtomstandigheden past.
    - Personalised Signature: voeg aangepaste tekst aan het touchscreen toe voor een persoonlijke stijl of snelle identificatie.
    - Auto Lock: stel in na hoeveel tijd zonder activiteit het scherm automatisch wordt vergrendeld. Het bereik is 15 seconden tot 5 minuten.
    - Passcode: stel een toegangscode voor het touchscreen in voor extra beveiliging.

    Raadpleeg [Display Management](../../interface_guide/display_management.md) voor uitgebreide instructies.

=== "USB & Power"

    Op de pagina USB & Power kun je USB-instellingen en energiebeheer voor je router configureren, zoals het USB-protocol, de stroomrichting, time-outs bij inactiviteit en het stand-bygedrag.

    Raadpleeg [USB & Power](../../interface_guide/usb_power.md) voor uitgebreide instructies.

---

=== "Time Zone"

    Op de pagina Time Zone kun je de juiste tijdzone voor je router instellen. Hierdoor krijgen alle geplande taken, logboeken en systeemgebeurtenissen een nauwkeurig tijdstempel op basis van je lokale tijd. Deze instelling is essentieel voor nauwkeurige registraties en een correcte uitvoering van tijdgebonden configuraties.

    Raadpleeg [Time Zone](../../interface_guide/time_zone.md) voor uitgebreide instructies.

=== "Reset Firmware"

    Op de pagina Reset Firmware kun je de huidige firmwareversie van je router terugzetten naar de standaardinstellingen. Alle aangepaste configuraties worden daarbij gewist. Dit proces herstelt de standaardinstellingen van de firmwareversie die momenteel is geïnstalleerd. Dit kan nuttig zijn om aanhoudende problemen op te lossen of opnieuw te beginnen met de standaardconfiguratie van de huidige firmware.

    Raadpleeg [Reset Firmware](../../interface_guide/reset_firmware.md) voor uitgebreide instructies.

=== "Log"

    De pagina Log biedt toegang tot verschillende logboeken waarin activiteiten en gebeurtenissen van de router worden vastgelegd. Deze helpen bij probleemoplossing en prestatiebewaking. De pagina bevat:

    * System Log: uitgebreide logboeken van gebeurtenissen en activiteiten op systeemniveau.
    * Kernel Log: logboeken van activiteiten en gebeurtenissen van de kernel.
    * Crash Log: registraties van systeemcrashes en fouten die nuttig zijn bij de diagnose van kritieke problemen.
    * Cloud Log: logboeken van interacties en activiteiten met betrekking tot de GoodCloud-diensten die in de router zijn geïntegreerd.
    * Nginx Log: logboeken van de Nginx-webserver, als deze door de router wordt gebruikt, met gegevens over webverkeer en serveractiviteiten.

    Daarnaast bevat de pagina de knop Export Log, waarmee je alle verzamelde logboeken kunt exporteren voor analyse door technische ondersteuning. Deze functie is zeer waardevol voor het vaststellen van complexe problemen en het verkrijgen van professionele hulp.

    Raadpleeg [Log](../../interface_guide/log.md) voor uitgebreide instructies.

=== "Advanced Settings"

    De pagina Advanced Settings biedt via de OpenWrt LuCI-interface toegang tot geavanceerde configuratieopties. Ervaren gebruikers kunnen hiermee de instellingen en functies van hun router nauwkeurig aanpassen buiten de mogelijkheden van de basisinterface. Dit omvat uitgebreide netwerkconfiguraties, firewallinstellingen en andere geavanceerde systeemaanpassingen.

    Raadpleeg [Advanced Settings](../../interface_guide/advanced_settings.md) voor uitgebreide instructies.

## Veiligheid van de accu {#battery-safety}

Stop met het gebruiken en opladen van Mudi 7 als de accu is opgezwollen, lekt, ongewoon heet of beschadigd is of een ongebruikelijke geur afgeeft.

- Druk niet op de accu, buig of doorboor hem niet, plet hem niet en oefen er geen druk op uit.
- Gebruik geen gereedschap om tegen een opgezwollen of beschadigde accu te wrikken.
- Probeer een accu die is opgezwollen, vastzit, lekt, heet is of anderszins niet veilig kan worden gehanteerd niet te verwijderen.
- Gooi een beschadigde lithium-ionaccu niet bij het huishoudelijk afval of de gewone recycling.
- Verstuur een opgezwollen of beschadigde accu niet via een gewone pakketdienst.
- Neem contact op met [GL.iNet Support](https://www.gl-inet.com/contacts/) voor hulp met de garantie en de vervolgstappen.

Plaats een beschadigde accu die al is verwijderd niet terug. Neem contact op met een lokale inzamelplaats voor batterijen of huishoudelijk gevaarlijk afval die beschadigde lithium-ionaccu's aanvaardt.

Als de accu rookt, snel heet wordt, sist, brandt of anderszins direct gevaar oplevert, ga je bij het apparaat vandaan en neem je contact op met de lokale hulpdiensten.
