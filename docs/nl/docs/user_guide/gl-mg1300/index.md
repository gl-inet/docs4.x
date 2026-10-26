# Gebruikershandleiding Mango 2 (GL-MG1300) {#mango-2-gl-mg1300-user-guide}

## Productoverzicht {#product-overview}

Mango 2 (GL-MG1300) is de eerste dual-band Wi‑Fi 5-mini-reisrouter van GL.iNet en heeft een uiterst dun, draagbaar ontwerp. De theoretische dual-band snelheden bedragen 400 Mbps (2.4 GHz) en 866 Mbps (5 GHz), met een 2×2 MIMO-configuratie. OpenVPN en WireGuard zijn vooraf geïnstalleerd, meer dan 30 VPN-diensten worden ondersteund om netwerkverkeer te versleutelen wanneer de VPN-client is ingeschakeld, en extern beheer via GoodCloud is mogelijk. Zo worden prestaties, gebruiksgemak en beveiliging goed gecombineerd.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

- 1 x Mango 2 (GL-MG1300)
- 1 x Gebruikershandleiding
- 1 x USB-C-naar-USB-C-voedingskabel
- 1 x Bedankkaart

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/unboxing.png){class="glboxshadow"}

Bekijk hieronder de uitpakvideo van Mango 2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xwHgLdWPwPc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Mango 2 instellen {#how-to-set-up-mango-2}

Gebruik een van de vier ondersteunde methoden voor internetverbindingen om Mango 2 in te stellen: Ethernet, Repeater, Tethering of Cellular. Volg de onderstaande stappen.

### 1. Inschakelen {#1-power-on}

Sluit de USB Type-C-voedingskabel aan op de voedingspoort van de router. Sluit het andere uiteinde aan op een 5V/2A-voedingsadapter (niet meegeleverd) en steek deze in een stopcontact.

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

Configureer je Mango 2 met een van de ondersteunde methoden voor internetverbindingen: Ethernet, Repeater, Tethering of Cellular. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je meerdere internetverbindingen in.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Sluit de WAN-poort van Mango 2 met een Ethernet-kabel aan op een upstream apparaat, zoals een modem.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Ethernet op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een Ethernet-kabel](../../interface_guide/internet_ethernet.md) voor uitgebreide instructies.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. Zoek op de pagina INTERNET van het webbeheerpaneel het gedeelte Repeater en klik op **Connect**.
    2. Selecteer een Wi-Fi-netwerk uit de beschikbare netwerken.
    3. Voer het wachtwoord in en klik op **Apply**.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Repeater op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een bestaand Wi-Fi-netwerk](../../interface_guide/internet_repeater.md) voor uitgebreide instructies.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Sluit je mobiele apparaat, zoals een smartphone of USB-dongle, met een USB-kabel aan op de USB-poort van de router.
    2. Ga op je mobiele apparaat naar Settings en schakel **USB Tethering** of **Personal Hotspot** in. Tik op een iPhone op **Trust This Device** als daarom wordt gevraagd.
    3. Klik op de pagina INTERNET van het webbeheerpaneel in het gedeelte Tethering op **Connect**.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Tethering op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via USB-tethering](../../interface_guide/internet_tethering.md) voor uitgebreide instructies.

=== "Cellular"

     ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Op Mango 2 kun je rechtstreeks een USB-C-modem aansluiten. Gebruik een USB-C-naar-USB-A-adapter om een USB-A-modem aan te sluiten.

    Sluit een mobiele USB-modem aan op de USB-poort van Mango 2. Hiermee kun je de internetverbinding van de USB-modem delen met alle verbonden apparaten.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Cellular op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een mobiel netwerk](../../interface_guide/internet_cellular.md) voor uitgebreide instructies.

---

Hieronder vind je een overzicht van de functies in het webbeheerpaneel van Mango 2.

## Wireless {#wireless}

Op de pagina Wireless kun je verschillende Wi-Fi-netwerken configureren, waaronder Main Network, Guest Network en IoT Network. Voor elk type Wi-Fi-netwerk kun je de 5 GHz- en 2.4 GHz-band afzonderlijk configureren. Je kunt elke band inschakelen en basisinstellingen configureren, zoals de Wi-Fi-SSID, beveiligingsmodus en het wachtwoord, en een willekeurige BSSID inschakelen.

Raadpleeg [Wireless](../../interface_guide/wireless.md) om Wireless in te stellen.

## Clients {#clients}

De pagina Clients toont informatie over verbonden apparaten. Voor elke client worden de naam, het IP- en MAC-adres, de download- en uploadsnelheid en het totale verkeer weergegeven. Je kunt de client ook blokkeren en andere handelingen uitvoeren.

Raadpleeg [Clients](../../interface_guide/clients.md) om Clients in te stellen.

## Clouddiensten {#cloud-services}

=== "GL.iNet Account"

    Met GL.iNet Account kun je je apparaten en clouddiensten verbinden en beheren. Je hebt naadloos toegang tot GoodCloud en de glinet App, voor een veilige en verbeterde ervaring. Zo kun je je netwerk altijd en overal eenvoudiger beheren.

    Raadpleeg [GL.iNet Account](../../interface_guide/glinet_account.md) om GL.iNet Account in te stellen.

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} biedt een eenvoudige manier om GL.iNet-routers op afstand te openen en beheren.

=== "GoodPAS"

    GoodPAS is een geavanceerde netwerkfunctie voor naadloze externe toegang en apparaatbeheer. GoodPAS is speciaal ontwikkeld voor integratie met GL.iNet-routers en gebruikt het AmneziaWG-protocol met ingebouwde verkeersobfuscatie voor veilige en stabiele verbindingen. Met GoodPAS heb je op afstand toegang tot je thuisnetwerk. Wanneer je thuisrouter als GoodPAS exit node werkt, gebruikt internetverkeer dat via GoodPAS wordt verzonden het openbare WAN-IP-adres van die router.

    Raadpleeg [GoodPAS](../../interface_guide/goodpas.md) om GoodPAS in te stellen.

## VPN {#vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk. Mango 2 ondersteunt OpenVPN en WireGuard.

=== "OpenVPN"

    Mango 2 en andere GL.iNet-routers ondersteunen het OpenVPN-protocol, dat een sterke beveiliging biedt. Volg deze tutorials om OpenVPN in te stellen:

    * [Een OpenVPN-client instellen](../../interface_guide/openvpn_client.md)
    * [Een OpenVPN-server instellen](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2 en andere GL.iNet-routers ondersteunen het WireGuard-protocol, dat hoge snelheden en gebruiksgemak biedt. Volg deze tutorials om WireGuard in te stellen:

    * [Een WireGuard-client instellen](../../interface_guide/wireguard_client.md)
    * [Een WireGuard-server instellen](../../interface_guide/wireguard_server.md)

## Netwerk {#network}

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Cellular, Repeater en Ethernet. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) om Multi-WAN in te stellen.


=== "Subnet"

    Subnet centraliseert het beheer van LAN, Guest Network, IoT Network en aangepaste VLAN Networks. Je kunt meerdere subnets maken en beheren om verschillende soorten apparaten of verkeer van elkaar te scheiden.

    Raadpleeg [Subnet](../../interface_guide/subnet.md) om het subnet in te stellen.

=== "Ethernet Port"

    Op de pagina Ethernet Port kun je de WAN- en LAN-poorten configureren, de WAN/LAN-interface op Ethernet instellen, de MAC-modus en het MAC-adres voor de WAN-interface opgeven en de onderhandelde snelheid van de netwerkpoort weergeven.

    Raadpleeg [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md) om de Ethernet-poort in te stellen.
---

=== "DNS"

    Op de pagina DNS kun je aangepaste DNS-servers instellen, bescherming tegen DNS-rebindingaanvallen inschakelen en de DNS-instellingen van alle clients overschrijven. Je kunt aangepaste DNS-instellingen de VPN-DNS laten overschrijven en de DNS-servermodus op automatisch instellen of handmatig DNS-servers uit de Ethernet-verbinding opgeven.

    Raadpleeg [DNS](../../interface_guide/dns.md) om DNS in te stellen.

=== "IPv6"

    IPv6 (Internet Protocol version 6) is de nieuwste versie van het Internet Protocol en is ontwikkeld als opvolger van IPv4. Het biedt een veel grotere adresruimte en maakt daardoor een vrijwel onbeperkt aantal unieke IP-adressen mogelijk. Dit is noodzakelijk om het groeiende aantal apparaten met een internetverbinding te ondersteunen.

    Raadpleeg [IPV6](../../interface_guide/ipv6.md) om IPV6 in te stellen.

=== "IGMP Snooping"

    IGMP snooping is een techniek voor netwerkoptimalisatie die in Ethernet-switches wordt gebruikt om multicastverkeer te beheren en regelen.

    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) om IGMP snooping in te stellen.

---

=== "Network Mode"

    Op de pagina Network Mode kun je de operationele rol van de router configureren voor verschillende netwerkimplementaties. Je kunt kiezen uit modi voor uiteenlopende situaties, van Wi-Fi-dekking thuis tot multi-link netwerken voor bedrijven. Elke modus schakelt specifieke routerfuncties in of uit om de prestaties te optimaliseren.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) om de netwerkmodus in te stellen.

=== "Network Acceleration"

    Netwerkversnelling kan de CPU-belasting verlagen en het doorsturen van verkeerspakketten versnellen.

    Raadpleeg [Network Acceleration](../../interface_guide/network_acceleration.md) om netwerkversnelling in te stellen.

## Flow Control {#flow-control}

=== "Parental Control"

    Parental Control is bedoeld om je te helpen de apparaten van je kinderen te beheren. Je kunt onder meer de schermtijd beperken en toegang tot bepaalde inhoud blokkeren.

    Raadpleeg [Parental Control](../../interface_guide/parental_control_v4.9.md) om ouderlijk toezicht in te stellen.

## Security {#security}

=== "Port Forwarding"

    Met port forwarding kunnen externe servers en apparaten op internet toegang krijgen tot apparaten in een privénetwerk.

    Raadpleeg [Port Forwarding](../../interface_guide/port_forwarding.md) om port forwarding in te stellen.

=== "Admin Access"

    Met Admin Access kun je verschillende beveiligingsinstellingen configureren om je netwerk en router tegen onbevoegde toegang te beschermen.

    Raadpleeg [Admin Access](../../interface_guide/admin_access.md) om beheerderstoegang in te stellen.

=== "NAT Mode"

    Op de pagina NAT Mode kun je de functies Full Cone NAT en SIP ALG (Application Layer Gateway) in- of uitschakelen.

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

=== "Tailscale"

    Tailscale is een VPN-dienst waarmee je overal toegang hebt tot je apparaten en toepassingen.

    Raadpleeg [Tailscale](../../interface_guide/tailscale.md) om Tailscale in te stellen.

## Systeem {#system}

=== "Overview"

    De pagina Overview biedt een uitgebreid overzicht van de huidige status en prestatiegegevens van je router. Op deze pagina kun je het volgende bekijken:

    * CPU Average Load: bewaak de gemiddelde belasting van de CPU van je router om de prestaties te beoordelen en mogelijke knelpunten op te sporen.
    * Memory Usage: controleer hoeveel geheugen van je router in gebruik is om het beheer van bronnen te ondersteunen.
    * LED Control: schakel de leds van de router in of uit om de visuele indicatoren van het apparaat aan te passen.
    * Flash: bekijk het gebruik van de flashopslag van de router en controleer of er voldoende ruimte is voor firmware en configuratiegegevens.
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

    Op de pagina Scheduled Tasks kun je verschillende routerfuncties volgens een vooraf ingesteld schema automatiseren. Dit verhoogt het gemak en de efficiëntie. De belangrijkste functies op deze pagina zijn:

    * LED Control: schakel de leds van de router in of uit om de visuele indicatoren van het apparaat aan te passen.
    * Schedule Reboot: configureer de router om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.
    * Wi-Fi Status Schedule: stel een schema in om de 5GHz / 2.4GHz-band te beheren en zo de beschikbaarheid van het netwerk en het energieverbruik beter te regelen.

    Met deze planningsopties heb je meer controle over de werking van je router en kun je deze afstemmen op je specifieke behoeften en voorkeuren.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor uitgebreide instructies.

=== "Time Zone"

    Op de pagina Time Zone kun je de juiste tijdzone voor je router instellen. Hierdoor krijgen alle geplande taken, logboeken en systeemgebeurtenissen een nauwkeurig tijdstempel op basis van je lokale tijd. Deze instelling is essentieel voor nauwkeurige registraties en een correcte uitvoering van tijdgebonden configuraties.

    Raadpleeg [Time Zone](../../interface_guide/time_zone.md) voor uitgebreide instructies.

=== "Toggle Button Settings"

    Op de pagina Toggle Button Settings kun je de fysieke schakelaarknop van je router configureren en er specifieke functies aan toewijzen voor snelle toegang en bediening. De functie biedt handige snelkoppelingen voor veelvoorkomende taken en instellingen en vereenvoudigt het routerbeheer.

    Raadpleeg [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) voor uitgebreide instructies.

---

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
