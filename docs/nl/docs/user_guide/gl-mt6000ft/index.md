# Gebruikershandleiding Fortify (GL-MT6000) {#fortify-gl-mt6000-user-guide}

## Productoverzicht {#product-overview}

Fortify (GL-MT6000) is een Wi-Fi 6-router die gezamenlijk door GL.iNet en ExpressVPN wordt uitgebracht. Elk apparaat wordt geleverd met een gratis ExpressVPN-abonnement van één jaar. Je kunt het abonnement activeren en je account rechtstreeks via het webbeheerpaneel van de router verbinden. Wanneer een ExpressVPN-tunnel is verbonden, versleutelt en routeert de router het verkeer volgens je VPN-beleidsinstellingen via die tunnel.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

- 1 x Fortify (GL-MT6000)
- 1 x Gebruikershandleiding
- 1 x ExpressVPN-activeringshandleiding
- 1 x Ethernet-kabel
- 1 x Voedingsadapter
- 1 x Bedankkaart
- 1 x Adapter (afhankelijk van het land van levering)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/unboxing.png){class="glboxshadow"}

Bekijk hieronder de uitpakvideo van Fortify.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IQEfj7Hff7U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Fortify instellen {#how-to-set-up-fortify}

Bekijk deze installatievideo of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FymI3LCRMTA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Inschakelen {#1-power-on}

Zet de tweedelige voedingsadapter in elkaar. Sluit de adapter aan op je Fortify-router en steek de stekker in een stopcontact. De router start automatisch op.

### 2. Een apparaat verbinden {#2-connect-device}

Verbind een apparaat, zoals een computer, laptop of smartphone, via Wi-Fi of Ethernet met de router.

- Ethernet

    Sluit je apparaat met een Ethernet-kabel aan op de LAN-poort van de router.

- Wi-Fi

    Ga op je apparaat naar Settings -> WLAN, zoek de Wi-Fi-netwerknaam van je router in de lijst met beschikbare netwerken en voer het wachtwoord in om verbinding te maken. De standaardnetwerknaam en het wachtwoord staan op het label van de router.

### 3. Aanmelden bij het webbeheerpaneel {#3-log-in-to-web-admin-panel}

Open een webbrowser, voer `192.168.8.1` in de adresbalk in en meld je aan. Kies rechtsboven je taal, stel het beheerderswachtwoord in en klik op **Next**. Het wachtwoord moet 10–63 tekens lang zijn en ten minste twee van de volgende typen bevatten: hoofdletters, kleine letters, cijfers en speciale symbolen.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Stel je Wi-Fi in. Houd er rekening mee dat je het apparaat opnieuw met de Wi-Fi van de router moet verbinden als je de Wi-Fi-gegevens wijzigt. Gebruik daarvoor de bijgewerkte aanmeldingsgegevens.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Internet instellen {#4-internet-setup}

**Opmerking:** de volgende instructies gelden voor gebruikers die de router configureren via het GL.iNet web Admin Panel. Als je liever de [GL.iNet app](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"} gebruikt, download je de app en volg je de aanwijzingen op het scherm.

Configureer je Fortify met een van de ondersteunde methoden voor internetverbindingen: Ethernet, Repeater, Tethering of Cellular. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je meerdere internetverbindingen in.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Sluit een Ethernet-kabel aan tussen de WAN-poort van je Fortify-router en een upstream apparaat, zoals een modem.

    Zodra de internetverbinding tot stand is gebracht, brandt de led van de router continu wit.

    Raadpleeg [Verbinding maken met internet via een Ethernet-kabel](../../interface_guide/internet_ethernet.md) voor uitgebreide instructies.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Ga in het webbeheerpaneel naar INTERNET -> het gedeelte Repeater en klik op **Connect**.
    2. Selecteer een Wi-Fi-netwerk uit de beschikbare netwerken.
    3. Voer het wachtwoord in en klik op **Apply**.

    Zodra de internetverbinding tot stand is gebracht, brandt de led van de router continu wit.

    Raadpleeg [Verbinding maken met internet via een bestaand Wi-Fi-netwerk](../../interface_guide/internet_repeater.md) voor uitgebreide instructies.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Sluit je smartphone met een USB-kabel aan op de USB-poort van de router.
    2. Ga op je smartphone naar Settings en schakel USB Tethering in. Vertrouw dit apparaat op een iPhone en schakel Personal Hotspot in.
    3. Ga in het webbeheerpaneel naar INTERNET -> het gedeelte Tethering en klik op **Connect**.

    Zodra de internetverbinding tot stand is gebracht, brandt de led van de router continu wit.

    Raadpleeg [Verbinding maken met internet via USB-tethering](../../interface_guide/internet_tethering.md) voor uitgebreide instructies.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Sluit een mobiele USB-modem aan op de USB-poort van de router. Hiermee kun je de internetverbinding van een USB-modem delen met alle verbonden apparaten.

    Zodra de internetverbinding tot stand is gebracht, brandt de led van de router continu wit.

    Raadpleeg [Verbinding maken met internet via een mobiel netwerk](../../interface_guide/internet_cellular.md) voor uitgebreide instructies.

---

Hieronder vind je een overzicht van de functies in het webbeheerpaneel van Fortify.

## Wireless {#wireless}

Op de pagina Wireless kun je de Wi-Fi-netwerken van Fortify configureren, waaronder Main Network, Guest Network en IoT Network. Elk netwerk ondersteunt zowel de 2.4 GHz- als de 5 GHz-band.

Raadpleeg [Wireless](../../interface_guide/wireless.md) om Wireless in te stellen.

## Clients {#clients}

De pagina Clients toont informatie over verbonden apparaten, waaronder de apparaatnaam, het verbindingstype, de IP- en MAC-adressen, de download- en uploadsnelheid en het verkeer. Je kunt een bepaalde client ook met één klik blokkeren en andere handelingen uitvoeren.

Raadpleeg [Clients](../../interface_guide/clients.md) voor meer informatie.

## Clouddiensten {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} biedt een eenvoudige manier om je GL.iNet-routers op afstand te openen en beheren.

    Raadpleeg [GoodCloud](../../interface_guide/cloud.md) voor meer informatie.

=== "AstroWarp"

    AstroWarp is een functie voor naadloze externe netwerken op GL.iNet-routers. De functie gebruikt het AmneziaWG-protocol met ingebouwde verkeersobfuscatie en biedt altijd en overal stabiele en veilige externe toegang.

    Raadpleeg [AstroWarp](../../interface_guide/astrowarp.md) voor meer informatie.

## VPN {#vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk.

Fortify is geïntegreerd met [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, zodat je binnen enkele minuten een ExpressVPN-verbinding kunt activeren. Elk Fortify-apparaat wordt geleverd met een gratis ExpressVPN-abonnement van één jaar. Je kunt het abonnement activeren en je ExpressVPN-account rechtstreeks via het webbeheerpaneel van de router verbinden. Wanneer een ExpressVPN-tunnel is verbonden, versleutelt en routeert de router het verkeer volgens je VPN-beleidsinstellingen via die tunnel.

Raadpleeg [ExpressVPN Activation Guide](../../interface_guide/expressvpn_activation_guide.md) om het gratis abonnement te activeren en een VPN-tunnel in te stellen.

Raadpleeg [OpenVPN Server](../../interface_guide/openvpn_server.md) om een OpenVPN-server in te stellen.

Raadpleeg [WireGuard Server](../../interface_guide/wireguard_server.md) om een WireGuard-server in te stellen.

## Netwerk {#network}

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Cellular, Repeater en Ethernet. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) voor meer informatie.

=== "LAN"

    Een LAN (Local Area Network) is een netwerk dat computers en apparaten binnen een beperkt geografisch gebied, zoals een huis of kantoor, met elkaar verbindt. Dit is het lokale netwerk waarmee je apparaat verbinding maakt via de hoofd-Wi-Fi of een Ethernet-kabel. De pagina LAN bevat Basic Settings, DHCP Server Settings en Address Reservation.

    Raadpleeg [LAN](../../interface_guide/lan.md) voor meer informatie.

=== "Guest Network"

    Op de pagina Guest Network kun je een speciaal Wi-Fi-netwerk voor bezoekers maken. Dit netwerk is van het primaire netwerk gescheiden en biedt daardoor betere beveiliging en eenvoudige internettoegang. Je kunt een gastsubnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` of `10.0.0.0/8` en de IP-adressen van de gateway en het subnetmasker opgeven.

    Raadpleeg [Guest Network](../../interface_guide/guest_network.md) voor meer informatie.

=== "IoT Network"

    Op de pagina IoT Network kun je een speciaal Wi-Fi-netwerk voor IoT-apparaten maken. Dit netwerk is van het primaire netwerk gescheiden en biedt daardoor betere compatibiliteit en beveiliging.

    Raadpleeg [IoT Network](../../interface_guide/iot_network.md) voor meer informatie.

<br>

=== "DNS"

    De DNS-instellingen van je router bepalen hoe domeinnamen in IP-adressen worden omgezet. Op deze pagina kun je automatisch verkregen DNS-server(s) van upstream apparaten gebruiken, aangepaste DNS-servers instellen en DNS-prioriteiten configureren.

    Raadpleeg [DNS](../../interface_guide/dns.md) voor meer informatie.

=== "Ethernet Port"

    Op de pagina Ethernet Port kun je de rollen van Ethernet-poorten (WAN/LAN) beheren en poortgegevens, zoals het MAC-adres en de onderhandelde snelheid, bekijken.

    Raadpleeg [Ethernet Port](../../interface_guide/ethernet_port.md) voor meer informatie.

=== "IPv6"

    IPv6 (Internet Protocol version 6) is de nieuwste versie van het Internet Protocol en is ontwikkeld als opvolger van IPv4. Het biedt een veel grotere adresruimte en maakt daardoor een vrijwel onbeperkt aantal unieke IP-adressen mogelijk. Dit is noodzakelijk om het groeiende aantal apparaten met een internetverbinding te ondersteunen.

    Raadpleeg [IPV6](../../interface_guide/ipv6.md) voor meer informatie.

=== "IGMP Snooping"

    IGMP snooping is een techniek voor netwerkoptimalisatie die in Ethernet-switches wordt gebruikt om multicastverkeer te beheren en regelen.

    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) voor meer informatie.

<br>

=== "Network Mode"

    De netwerkmodus omvat de configuratie-instellingen die bepalen hoe een apparaat verbinding maakt met een netwerk en met andere apparaten communiceert.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) om de netwerkmodus in te stellen.

=== "Drop-in Gateway"

    Drop-in Gateway breidt de functies van je hoofdrouter uit met functies die deze mogelijk niet heeft, waaronder AdGuard Home, versleutelde DNS en VPN.

    Raadpleeg [Een drop-in gateway instellen](../../tutorials/how_to_set_up_drop_in_gateway.md) om een drop-in gateway in te stellen.

=== "Network Acceleration"

    Netwerkversnelling kan de CPU-belasting verlagen en het doorsturen van verkeerspakketten versnellen.

    Raadpleeg [Network Acceleration](../../interface_guide/network_acceleration.md) om netwerkversnelling in te stellen.

## Flow Control {#flow-control}

=== "DPI Engine"

    DPI (Deep Packet Inspection) is een kernfunctie voor intelligent netwerkbeheer. DPI omzeilt de beperking van traditionele routers, die alleen bron- of bestemmingsadressen identificeren, analyseert de inhoud van gegevenspakketten grondig en identificeert door vergelijking met een kenmerkenbibliotheek nauwkeurig welke toepassingen en websites gebruikers openen. Hierdoor zijn fijnmazige verkeersclassificatie en -regeling mogelijk.

    De DPI-functie van GL.iNet is geïntegreerd met [Netify](https://www.netify.ai/){target="_blank"} en gebruikt een lichte ingebouwde plug-in voor efficiënte implementatie. Dankzij de online bijgewerkte kenmerkendatabase van Netify biedt de functie betrouwbaar beheer, waardoor netwerkregeling nauwkeuriger en efficiënter wordt.

    Raadpleeg [DPI Engine](../../interface_guide/dpi_engine.md) voor meer informatie.

=== "Data Statistics"

    Data Statistics biedt een intelligent verkeersdashboard dat netwerkgebruik per toepassing categoriseert en visualiseert. Hiermee kun je realtime en historisch verkeer bewaken voor beter inzicht in en beheer van het netwerk.

    Raadpleeg [Data Statistics](../../interface_guide/data_statistics.md) voor meer informatie.

=== "Content Filter"

    Content Filter biedt intelligente online beveiliging op basis van DPI-classificatie en blokkeert automatisch schadelijke of kwaadaardige websites om je netwerk schoon en veilig te houden.

    Raadpleeg [Content Filter](../../interface_guide/content_filter.md) voor meer informatie.

<br>

=== "QoS"

    QoS (Quality of Service) optimaliseert de bandbreedtetoewijzing door tijdens netwerkcongestie prioriteit te geven aan belangrijke activiteiten, zoals videogesprekken en gaming. Hierdoor neemt de latentie af en verbeteren de algemene netwerkprestaties. Dit geldt voor lokaal clientverkeer en verkeer in de VPN Client-tunnel, maar niet voor verkeer dat wordt ontvangen wanneer de router als VPN Server werkt.

    Raadpleeg [QoS](../../interface_guide/qos.md) voor meer informatie.

=== "SQM"

    SQM (Smart Queue Management) beheert het netwerkverkeer van je router op intelligente wijze om de latentie en 'bufferbloat' te beperken. Zo verlopen games en spraakoproepen soepeler.

    Raadpleeg [SQM](../../interface_guide/sqm.md) voor meer informatie.

=== "Parental Control"

    Parental Control is bedoeld om je te helpen de apparaten van je kinderen te beheren. Je kunt onder meer de schermtijd beperken en toegang tot bepaalde inhoud blokkeren.

    Raadpleeg [Parental Control](../../interface_guide/parental_control_v4.9.md) voor meer informatie.

## Security {#security}

=== "Port forwarding"

    Met port forwarding kunnen externe servers en apparaten op internet toegang krijgen tot apparaten in een privénetwerk.

    Raadpleeg [Port Forwarding](../../interface_guide/port_forwarding.md) voor meer informatie.

=== "ACL"

    Met ACL, een afkorting van Access Control List, kun je regels maken om netwerkverkeer te beheren op basis van verbindingsprotocollen, apparaatadressen en poorten. De regels bepalen of netwerktoegang wordt toegestaan of geblokkeerd. Als meerdere ACL-regels conflicteren, past het systeem de regel met de hoogste prioriteit toe.

    Raadpleeg [ACL](../../interface_guide/acl.md) voor meer informatie.

=== "Admin Access"

    Met Admin Access kun je verschillende beveiligingsinstellingen configureren om je netwerk en router tegen onbevoegde toegang te beschermen. De pagina bevat de volgende opties:

    * Access Control: beheer en beperk de toegang tot de routerinterface vanaf apparaten die met je lokale netwerk zijn verbonden.
    * Remote Access Control: configureer en beperk toegang tot de routerinterface vanaf externe locaties via internet om de beveiliging tegen bedreigingen van buitenaf te verbeteren.
    * Open Ports on Router: bepaal welke poorten op de router geopend zijn om mogelijke kwetsbaarheden en onbevoegde toegang te beperken.

    Raadpleeg [Admin Access](../../interface_guide/admin_access.md) voor meer informatie.

=== "NAT Mode"

    Op de pagina NAT Mode kun je de functies Full Cone NAT en SIP ALG (Application Layer Gateway) in- of uitschakelen.

    Raadpleeg [NAT Mode](../../interface_guide/nat_settings.md) voor meer informatie.

## Toepassingen {#applications}

=== "Plug-ins"

    Een plug-in is een softwareonderdeel dat specifieke functies of mogelijkheden aan een bestaand computerprogramma toevoegt, zodat de mogelijkheden van het programma kunnen worden aangepast en uitgebreid.

    Raadpleeg [Plug-ins](../../interface_guide/plugins.md) voor meer informatie.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecteert en actualiseert automatisch en in realtime het IP-adres dat aan een domein is gekoppeld. Het koppelt een domeinnaam aan het dynamische openbare IP-adres van je router, zodat je zonder statisch IP-adres op afstand toegang hebt tot je netwerk.

    Raadpleeg [Dynamic DNS](../../interface_guide/ddns.md) voor meer informatie.

=== "Network Storage"

    Netwerkopslag is een centrale oplossing voor gegevensopslag waarmee meerdere gebruikers en apparaten via een netwerk bestanden kunnen openen en delen.

    Raadpleeg [Network Storage](../../interface_guide/network_storage.md) voor meer informatie.

=== "AdGuard Home"

    AdGuard Home blokkeert advertenties en trackers in het hele netwerk. De toepassing werkt als DNS-server en filtert ongewenste inhoud op alle apparaten die met een thuisnetwerk zijn verbonden.

    Raadpleeg [AdGuard Home](../../interface_guide/adguardhome.md) voor meer informatie.

<br>

=== "Bark"

    De dienst [Bark](https://www.bark.us/){target="_blank"} helpt de digitale wereld van je kind te beschermen en biedt uitgebreide online beveiliging. Normaal is hiervoor een betaald abonnement vereist. Door de samenwerking tussen GL.iNet en Bark is het Bark Home-abonnement echter gratis beschikbaar op Fortify (GL-MT6000), met geavanceerde bewaking en waarschuwingen zonder extra kosten.

    Raadpleeg [Bark](../../interface_guide/bark.md) voor meer informatie.

=== "Tailscale"

    Tailscale is een VPN-dienst waarmee je overal ter wereld veilig en eenvoudig toegang hebt tot je apparaten en toepassingen.

    Fortify (GL-MT6000) is geïntegreerd met Tailscale, zodat je de router aan een virtueel Tailscale-netwerk kunt toevoegen. Nadat de verbinding tot stand is gebracht, heb je op afstand toegang tot de router en zijn WAN- en LAN-bronnen.

    Raadpleeg [Tailscale](../../interface_guide/tailscale.md) voor meer informatie.

=== "ZeroTier"

    ZeroTier is een softwaregedefinieerde netwerkoplossing waarmee gebruikers via internet beveiligde virtuele netwerken kunnen maken en apparaten kunnen verbinden alsof ze zich in hetzelfde lokale netwerk bevinden.

    Raadpleeg [ZeroTier](../../interface_guide/zerotier.md) voor meer informatie.

=== "Tor"

    Tor, afgeleid van The Onion Router, is gratis opensourcesoftware voor anonieme communicatie. Hiermee kunnen gebruikers internet met meer privacy verkennen.

    Raadpleeg [Tor](../../interface_guide/tor.md) voor meer informatie.

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

    Raadpleeg [Overview](../../interface_guide/system_overview.md) voor meer informatie.

=== "Admin Password"

    Op de pagina Admin Password kun je het wachtwoord voor de beheerinterface van de router instellen of wijzigen.

    Raadpleeg [Admin Password](../../interface_guide/admin_password.md) voor meer informatie.

=== "Upgrade"

    De pagina Upgrade wordt gebruikt om de firmware van je router bij te werken naar de nieuwste versie, voor betere prestaties en beveiliging en nieuwe functies. Deze pagina biedt twee opties:

    * Firmware Online Upgrade: controleer automatisch op de server van de fabrikant of de nieuwste firmwareversie beschikbaar is. Als deze online beschikbaar is, kun je de nieuwste versie installeren.
    * Firmware Local Upgrade: upload handmatig een firmwarebestand vanaf je computer om de router bij te werken. Zo bepaal je zelf de versie en het moment van de upgrade.

    Raadpleeg [Upgrade](../../interface_guide/upgrade.md) voor meer informatie.

=== "Scheduled Tasks"

    Op de pagina Scheduled Tasks kun je verschillende routerfuncties volgens een vooraf ingesteld schema automatiseren. Dit verhoogt het gemak en de efficiëntie. De belangrijkste functies op deze pagina zijn:

    * LED Display Schedule: stel een schema in om de leds van de router automatisch in of uit te schakelen en zo lichtvervuiling op bepaalde tijden te beperken.
    * Schedule Reboot: configureer de router om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.
    * 5GHz / 2.4GHz Wi-Fi Status Schedule: stel een schema in om de 5GHz / 2.4GHz-Wi-Fi-band te beheren en zo de beschikbaarheid van het netwerk en het energieverbruik beter te regelen.

    Met deze planningsopties heb je meer controle over de werking van je router en kun je deze afstemmen op je specifieke behoeften en voorkeuren.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor meer informatie.

<br>

=== "Time Zone"

    Op de pagina Time Zone kun je de juiste tijdzone voor je router instellen. Hierdoor krijgen alle geplande taken, logboeken en systeemgebeurtenissen een nauwkeurig tijdstempel op basis van je lokale tijd. Deze instelling is essentieel voor nauwkeurige registraties en een correcte uitvoering van tijdgebonden configuraties.

    Raadpleeg [Time Zone](../../interface_guide/time_zone.md) voor meer informatie.

=== "Reset Firmware"

    Op de pagina Reset Firmware kun je de huidige firmwareversie van je router terugzetten naar de standaardinstellingen. Alle aangepaste configuraties worden daarbij gewist. Dit proces herstelt de standaardinstellingen van de firmwareversie die momenteel is geïnstalleerd. Dit kan nuttig zijn om aanhoudende problemen op te lossen of opnieuw te beginnen met de standaardconfiguratie van de huidige firmware.

    Raadpleeg [Reset Firmware](../../interface_guide/reset_firmware.md) voor meer informatie.

=== "Log"

    De pagina Log biedt toegang tot verschillende logboeken waarin activiteiten en gebeurtenissen van de router worden vastgelegd. Deze helpen bij probleemoplossing en prestatiebewaking. De pagina bevat:

    * System Log: uitgebreide logboeken van gebeurtenissen en activiteiten op systeemniveau.
    * Kernel Log: logboeken van activiteiten en gebeurtenissen van de kernel.
    * Crash Log: registraties van systeemcrashes en fouten die nuttig zijn bij de diagnose van kritieke problemen.
    * Cloud Log: logboeken van interacties en activiteiten met betrekking tot de GoodCloud-diensten die in de router zijn geïntegreerd.
    * Nginx Log: logboeken van de Nginx-webserver, als deze door de router wordt gebruikt, met gegevens over webverkeer en serveractiviteiten.

    Daarnaast bevat de pagina de knop Export Log, waarmee je alle verzamelde logboeken kunt exporteren voor analyse door technische ondersteuning. Deze functie is zeer waardevol voor het vaststellen van complexe problemen en het verkrijgen van professionele hulp.

    Raadpleeg [Log](../../interface_guide/log.md) voor meer informatie.

=== "Advanced Settings"

    De pagina Advanced Settings biedt via de OpenWrt LuCI-interface toegang tot geavanceerde configuratieopties. Ervaren gebruikers kunnen hiermee de instellingen en functies van hun router nauwkeurig aanpassen buiten de mogelijkheden van de basisinterface. Dit omvat uitgebreide netwerkconfiguraties, firewallinstellingen en andere geavanceerde systeemaanpassingen.

    Raadpleeg [Advanced Settings](../../interface_guide/advanced_settings.md) voor meer informatie.
