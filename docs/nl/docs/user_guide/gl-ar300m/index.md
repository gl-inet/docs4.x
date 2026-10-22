# Gebruikershandleiding Shadow (GL-AR300M Series) {#shadow-gl-ar300m-series-user-guide}

## Productoverzicht {#product-overview}

Shadow (GL-AR300M-serie) is een compacte minirouter voor draagbaar en reisvriendelijk gebruik, met een draadloze overdrachtssnelheid tot 300Mbps. Shadow biedt geavanceerde beveiligingsfuncties, waaronder ondersteuning voor OpenVPN, WireGuard® en een DNS-server. Je kunt een openbaar netwerk omzetten in een privé-Wi-Fi-netwerk om veilig te surfen. Ook kun je VPN-configuratiebestanden van meer dan 30 VPN-serviceproviders uploaden en de router als VPN-client instellen. Dit biedt extra privacy en beveiliging door het verkeer tussen je apparaat en de VPN-server te versleutelen.

![ar300m overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/product_info/overview.png){class="glboxshadow"}

## Shadow instellen {#how-to-set-up-shadow}

Gebruik een van de vier ondersteunde methoden voor internetverbindingen om Shadow in te stellen: Ethernet, Repeater, Tethering of Cellular. Volg de onderstaande stappen.

### 1. Inschakelen {#1-power-on}

Sluit de Micro USB-voedingskabel aan op de voedingspoort van de router. Sluit het andere uiteinde aan op een 5V/2A-voedingsadapter (niet meegeleverd) en steek deze in een stopcontact.

### 2. Een apparaat verbinden {#2-connect-device}

Verbind een apparaat, zoals een computer, laptop of smartphone, via Wi-Fi of Ethernet met de router.

- Ethernet

    Sluit je apparaat met een Ethernet-kabel aan op de LAN-poort van de router.

- Wi-Fi

    Ga op je apparaat naar Settings -> WLAN, zoek de Wi-Fi-netwerknaam van je router in de lijst met beschikbare netwerken en voer het wachtwoord in. De standaardnetwerknaam en het wachtwoord staan op het label aan de onderkant van de router.

### 3. Aanmelden bij het webbeheerpaneel {#3-log-in-to-web-admin-panel}

Open een webbrowser, voer `192.168.8.1` in de adresbalk in en meld je aan. Kies je taal, stel het beheerderswachtwoord in en klik vervolgens op **Apply**.

Houd er rekening mee dat je het apparaat opnieuw met de Wi-Fi van de router moet verbinden als je de Wi-Fi-gegevens wijzigt. Gebruik daarvoor de bijgewerkte aanmeldingsgegevens.

### 4. Internet instellen {#4-internet-setup}

**Opmerking:** de volgende instructies gelden voor gebruikers die de router configureren via het GL.iNet Web Admin Panel. Als je liever de GL.iNet-app gebruikt, [download je de app](https://www.gl-inet.com/app/){target="_blank"} en volg je de instructies op het scherm.

Configureer je Shadow met een van de ondersteunde methoden voor internetverbindingen: Ethernet, Repeater, Tethering of Cellular. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je meerdere internetverbindingen in.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/ethernet.png){class="glboxshadow"}

    Sluit een Ethernet-kabel aan tussen de WAN-poort van je router en een upstream apparaat, zoals een modem.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Ethernet op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een Ethernet-kabel](../../interface_guide/internet_ethernet.md) voor uitgebreide instructies.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/repeater.png){class="glboxshadow"}

    1. Zoek op de pagina INTERNET van het webbeheerpaneel het gedeelte Repeater en klik op **Connect**.
    2. Selecteer een Wi-Fi-netwerk uit de beschikbare netwerken.
    3. Voer het wachtwoord in en klik op **Apply**.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Repeater op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een bestaand Wi-Fi-netwerk](../../interface_guide/internet_repeater.md) voor uitgebreide instructies.

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/tethering.png){class="glboxshadow"}

    1. Sluit je mobiele apparaat, zoals een smartphone of USB-dongle, met een USB-kabel aan op de USB-poort van de router.
    2. Ga op je mobiele apparaat naar Settings en schakel USB Tethering in.
    3. Klik op de pagina INTERNET van het webbeheerpaneel in het gedeelte Tethering op **Connect**.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Tethering op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via USB-tethering](../../interface_guide/internet_tethering.md) voor uitgebreide instructies.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/usb_modem.png){class="glboxshadow"}

    Met deze methode kun je de internetverbinding van een USB-modem delen met alle verbonden apparaten.

    1. Plaats een USB-modem voor mobiele netwerken in de USB-poort van de router.
    2. Zoek op de pagina INTERNET van het webbeheerpaneel het gedeelte Cellular en klik op **Connect**.
    3. Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Cellular op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een USB-modem](../../interface_guide/internet_cellular.md) voor uitgebreide instructies.

## Een VPN instellen {#how-to-set-up-a-vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk. Shadow en andere GL.iNet-routers ondersteunen OpenVPN en WireGuard.

=== "OpenVPN"

    Shadow en andere GL.iNet-routers ondersteunen het OpenVPN-protocol, dat een sterke beveiliging biedt. Volg deze tutorials om OpenVPN in te stellen:

    * [Een OpenVPN-client instellen](../../interface_guide/openvpn_client.md)
    * [Een OpenVPN-server instellen](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Shadow en andere GL.iNet-routers ondersteunen het WireGuard-protocol, dat hoge snelheden en gebruiksgemak biedt. Volg deze tutorials om WireGuard in te stellen:

    * [Een WireGuard-client instellen](../../interface_guide/wireguard_client.md)
    * [Een WireGuard-server instellen](../../interface_guide/wireguard_server.md)

## Toepassingen {#applications}

=== "Plug-ins"

    Plug-ins zijn aanvullende functies die de mogelijkheden van je router uitbreiden.

    Raadpleeg [Plug-ins](../../interface_guide/plugins.md) om plug-ins in te stellen.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecteert en actualiseert automatisch en in realtime het IP-adres dat aan een domein is gekoppeld. Het koppelt een domeinnaam aan het dynamische openbare IP-adres van je router, zodat je zonder statisch IP-adres op afstand toegang hebt tot je netwerk.

    Raadpleeg [Dynamic DNS](../../interface_guide/ddns.md) om Dynamic DNS in te stellen.

=== "GoodCloud"

    De cloudbeheerdienst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} van GL.iNet biedt een eenvoudige manier om GL.iNet-routers op afstand te openen en beheren.

    Raadpleeg [GoodCloud](../../interface_guide/cloud.md) om GoodCloud in te stellen.

## Netwerkinstellingen {#network-settings}

=== "Firewall"

    De pagina Firewall biedt essentiële beveiligingsverbeteringen voor je netwerk. De pagina bevat functies zoals Port Forwarding, Open Ports en DMZ. Met deze hulpmiddelen kun je de verkeersstroom van je netwerk beheren en aanpassen en de beveiliging verbeteren.

    * Port Forwarding: stuur specifiek internetverkeer door naar aangewezen apparaten in je netwerk om toegang te geven tot diensten zoals game- of webservers.
    * Open Ports: bewaak en bepaal welke poorten op je router openstaan om onbevoegde toegang en mogelijke beveiligingsrisico's te voorkomen.
    * DMZ (Demilitarized Zone): maak één apparaat vanaf internet bereikbaar door al het inkomende verkeer ernaartoe door te sturen.

    Raadpleeg [Firewall](../../interface_guide/firewall.md) om firewallinstellingen te configureren.

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Cellular, Repeater en Ethernet. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) om Multi-WAN in te stellen.

=== "LAN"

    Op de pagina LAN kun je de instellingen van het lokale netwerk van je router beheren en configureren. De belangrijkste functies op deze pagina zijn:

    * Router IP Address: wijzig het IP-adres van je router zodat het beter bij je netwerkconfiguratie past.
    * Netmask: stel het subnetmasker voor je netwerk in. Dit bepaalt de omvang van het netwerk en het bereik van IP-adressen.
    * DHCP: schakel het Dynamic Host Configuration Protocol in of configureer het. Dit protocol wijst automatisch IP-adressen toe aan apparaten in je netwerk.
    * Address Reservation: reserveer specifieke IP-adressen voor bepaalde apparaten, zodat deze altijd hetzelfde IP-adres van de DHCP-server krijgen.

    Raadpleeg [Lan](../../interface_guide/lan.md) om het LAN in te stellen.

---

=== "DNS"

    De pagina DNS biedt opties om de Domain Name System-instellingen van je router aan te passen en zo de beveiliging en prestaties te verbeteren. De belangrijkste functies op deze pagina zijn:

    * Encrypted DNS: configureer versleutelde DNS om je browsegegevens tegen controle of manipulatie te beschermen en zo privacy en beveiliging te bieden.
    * Manual DNS: stel handmatig de gewenste DNS-servers in voor aangepaste controle over DNS-query's en mogelijk snellere omzetting.
    * DNS Proxy: schakel de DNS-proxy in om DNS-verzoeken van je apparaten via een opgegeven DNS-server te routeren. Dit biedt extra controle over DNS-verkeer.

    Met deze instellingen kun je de DNS-prestaties en beveiliging van je netwerk op je specifieke behoeften afstemmen.

    Raadpleeg [DNS](../../interface_guide/dns.md) om DNS in te stellen.

=== "Network Mode"

    Op de pagina Network Mode kun je de router voor verschillende modi configureren, zodat je flexibel aan uiteenlopende netwerkbehoeften kunt voldoen. De beschikbare modi zijn:

    * Router: werkt als standaardrouter, beheert verkeer tussen je lokale netwerk en internet en biedt functies zoals NAT, firewall en DHCP.
    * Access Point: werkt als access point en breidt je bestaande bekabelde netwerk uit met draadloze connectiviteit zonder verkeer te routeren.
    * Extender: werkt als bereikvergroter, versterkt het signaal van je bestaande draadloze netwerk voor een groter bereik en voorkomt zones zonder dekking.
    * WDS (Wireless Distribution System): vergelijkbaar met Extender. Selecteer WDS als je hoofdrouter de WDS-modus ondersteunt.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) om de netwerkmodus in te stellen.

=== "IPv6"

    Op de pagina IPv6 kun je IPv6-instellingen voor je netwerk configureren en ondersteuning voor het nieuwste internetprotocol inschakelen. Je kunt IPv6 inschakelen en een van vier modi selecteren die bij je netwerkbehoeften past:

    * Native: ontvang rechtstreeks van je internetprovider een IPv6-adres voor eenvoudige en efficiënte native IPv6-connectiviteit.
    * Passthrough: laat IPv6-verkeer via de router door naar de apparaten in je netwerk. De verbinding wordt overbrugd zonder dat de router zelf de IPv6-routering afhandelt.
    * NAT6: gebruik Network Address Translation for IPv6 (NAT6) om interne en externe IPv6-adressen te vertalen, vergelijkbaar met de werking van NAT voor IPv4.
    * Static IPv6: configureer handmatig een statisch IPv6-adres voor je router voor een vast adres, consistente connectiviteit en eenvoudiger beheer van netwerkdiensten.

    Met deze instellingen profiteer je van de voordelen van IPv6, waaronder een grotere adresruimte, betere beveiligingsfuncties en hogere prestaties.

    Raadpleeg [IPv6](../../interface_guide/ipv6.md) om IPv6 in te stellen.

---

=== "MAC Address"

    Op de pagina MAC Address kun je de Media Access Control-adressen (MAC-adressen) van je router bekijken en beheren. De belangrijkste functies op deze pagina zijn:

    * Factory Default: toon de standaard-MAC-adressen voor de modi Ethernet en Repeater van de router als referentie voor de oorspronkelijke hardware-instellingen.
    * Clone: kloon het MAC-adres van een specifiek clientapparaat. Dit is vooral nuttig wanneer netwerktoegang tot bepaalde apparaten is beperkt.
    * Manual: geef handmatig een aangepast MAC-adres voor je router op. Je kunt ook de knop Random gebruiken om een willekeurig MAC-adres te genereren, voor meer flexibiliteit en privacy.

    Met deze functies kun je de MAC-adressen van je router effectief beheren en compatibiliteit en flexibiliteit in verschillende netwerkomgevingen waarborgen.

    Raadpleeg [MAC Address](../../interface_guide/mac_address.md) om het MAC-adres te beheren.

=== "Drop-in Gateway"

    Drop-in Gateway breidt de functies van je hoofdrouter uit met functies die deze mogelijk niet heeft, waaronder AdGuard Home, versleutelde DNS en VPN.

    Raadpleeg [Een Drop-in Gateway instellen](../../tutorials/how_to_set_up_drop_in_gateway.md) om Drop-in Gateway in te stellen.

=== "IGMP Snooping"

    Op de pagina IGMP Snooping kun je instellingen configureren die het beheer van multicastverkeer in je netwerk optimaliseren. IGMP Snooping luistert naar IGMP-protocolpakketten, haalt er informatie uit en maakt en onderhoudt Layer 2-doorstuurtabellen voor multicast. Hierdoor worden gegevens van een multicastgroep alleen doorgestuurd naar hosts die zich bij de groep hebben aangesloten en bereikt ongewenst multicastverkeer geen andere hosts.

    Deze instellingen helpen de netwerkprestaties en efficiëntie te optimaliseren, vooral in omgevingen met veel multicastverkeer, zoals videostreaming of online gaming.

    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) om IGMP snooping in te stellen.

## Systeeminstellingen {#system-settings}

=== "Overview"

    De pagina Overview biedt een uitgebreid overzicht van de huidige status en prestatiegegevens van je router. Op deze pagina kun je het volgende bekijken:

    * CPU Average Load: bewaak de gemiddelde belasting van de CPU van je router om de prestaties te beoordelen en mogelijke knelpunten op te sporen.
    * Memory Usage: controleer hoeveel geheugen van je router in gebruik is om het beheer van bronnen te ondersteunen.
    * Flash Usage: bekijk het gebruik van de flashopslag van de router en controleer of er voldoende ruimte is voor firmware en configuratiegegevens.
    * LED Control: schakel de leds van de router in of uit om de visuele indicatoren van het apparaat aan te passen.
    * System Info: bekijk uitgebreide informatie over het systeem van je router, waaronder firmwareversie, uptime en netwerkstatus.

    Deze functies bieden essentiële informatie en bedieningselementen om de werking van je router effectief te beheren en bewaken.

    Raadpleeg [Overview](../../interface_guide/system_overview.md) voor uitgebreide instructies.

=== "Upgrade"

    De pagina Upgrade wordt gebruikt om de firmware van je router bij te werken naar de nieuwste versie, voor betere prestaties en beveiliging en nieuwe functies. Deze pagina biedt twee opties voor upgrades:

    * Online Upgrade: controleer automatisch op de server van de fabrikant of de nieuwste firmwareversie beschikbaar is. Als deze online beschikbaar is, kun je de nieuwste versie installeren.
    * Local Upgrade: upload handmatig een firmwarebestand vanaf je computer om de router bij te werken. Zo bepaal je zelf de versie en het moment van de upgrade.

    Met deze opties houd je je router bijgewerkt met de nieuwste verbeteringen en correcties.

    Raadpleeg [Upgrade](../../interface_guide/upgrade.md) voor uitgebreide instructies.

=== "Scheduled Tasks"

    Op de pagina Scheduled Tasks kun je verschillende routerfuncties volgens een vooraf ingesteld schema automatiseren. Dit verhoogt het gemak en de efficiëntie. De belangrijkste functies op deze pagina zijn:

    * LED Display Schedule: stel een schema in om de leds van de router automatisch in of uit te schakelen en zo lichtvervuiling op bepaalde tijden te beperken.
    * Schedule Reboot: configureer de router om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.
    * 2.4GHz Wi-Fi Status Schedule: stel een schema in om de 2.4GHz-Wi-Fi-band te beheren en zo de beschikbaarheid van het netwerk en het energieverbruik beter te regelen.

    Met deze planningsopties heb je meer controle over de werking van je router en kun je deze afstemmen op je specifieke behoeften en voorkeuren.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor uitgebreide instructies.

---

=== "Admin Password"

    Op de pagina Admin Password kun je het wachtwoord voor de beheerinterface van je router instellen of wijzigen, zodat alleen bevoegde gebruikers de routerinstellingen kunnen openen en aanpassen. Dit wachtwoord is essentieel voor de beveiliging en integriteit van je netwerk en beschermt tegen onbevoegde toegang en configuratiewijzigingen.

    Raadpleeg [Admin Password](../../interface_guide/admin_password.md) voor uitgebreide instructies.

=== "Time Zone"

    Op de pagina Time Zone kun je de juiste tijdzone voor je router instellen. Hierdoor krijgen alle geplande taken, logboeken en systeemgebeurtenissen een nauwkeurig tijdstempel op basis van je lokale tijd. Deze instelling is essentieel voor nauwkeurige registraties en een correcte uitvoering van tijdgebonden configuraties.

    Raadpleeg [Time Zone](../../interface_guide/time_zone.md) voor uitgebreide instructies.

=== "Toggle Button Settings"

    Op de pagina Toggle Button Settings kun je de fysieke schakelaarknop van je router configureren en er specifieke functies aan toewijzen voor snelle toegang en bediening. De functie biedt handige snelkoppelingen voor veelvoorkomende taken en instellingen en vereenvoudigt het routerbeheer.

    Raadpleeg [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) voor uitgebreide instructies.

---

=== "Log"

    De pagina Log biedt toegang tot verschillende logboeken waarin activiteiten en gebeurtenissen van de router worden vastgelegd. Deze helpen bij probleemoplossing en prestatiebewaking. De pagina bevat:

    * System Log: uitgebreide logboeken van gebeurtenissen en activiteiten op systeemniveau.
    * Kernel Log: logboeken van activiteiten en gebeurtenissen van de kernel.
    * Crash Log: registraties van systeemcrashes en fouten die nuttig zijn bij de diagnose van kritieke problemen.
    * Cloud Log: logboeken van interacties en activiteiten met betrekking tot de GoodCloud-diensten die in de router zijn geïntegreerd.
    * Nginx Log: logboeken van de Nginx-webserver, als deze door de router wordt gebruikt, met gegevens over webverkeer en serveractiviteiten.

    Daarnaast bevat de pagina de knop Export Log, waarmee je alle verzamelde logboeken kunt exporteren voor analyse door technische ondersteuning. Deze functie is zeer waardevol voor het vaststellen van complexe problemen en het verkrijgen van professionele hulp.

    Raadpleeg [Log](../../interface_guide/log.md) voor uitgebreide instructies.

=== "Reset Firmware"

    Op de pagina Reset Firmware kun je de huidige firmwareversie van je router terugzetten naar de standaardinstellingen. Alle aangepaste configuraties worden daarbij gewist. Dit proces herstelt de standaardinstellingen van de firmwareversie die momenteel is geïnstalleerd. Dit kan nuttig zijn om aanhoudende problemen op te lossen of opnieuw te beginnen met de standaardconfiguratie van de huidige firmware.

    Raadpleeg [Reset Firmware](../../interface_guide/reset_firmware.md) voor uitgebreide instructies.

=== "Advanced Settings"

    De pagina Advanced Settings biedt via de OpenWrt LuCI-interface toegang tot geavanceerde configuratieopties. Ervaren gebruikers kunnen hiermee de instellingen en functies van hun router nauwkeurig aanpassen buiten de mogelijkheden van de basisinterface. Dit omvat uitgebreide netwerkconfiguraties, firewallinstellingen en andere geavanceerde systeemaanpassingen.

    Raadpleeg [Advanced Settings](../../interface_guide/advanced_settings.md) voor uitgebreide instructies.
