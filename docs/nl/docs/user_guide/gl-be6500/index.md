# Gebruikershandleiding Flint 3e (GL-BE6500) {#flint-3e-gl-be6500-user-guide}

## Productoverzicht {#product-overview}

Flint 3e (GL-BE6500) is een dual-band Wi-Fi 7-desktoprouter voor thuisgebruikers en kleine kantoren. De router ondersteunt Multi-Link Operation (MLO), waarmee compatibele apparaten verbindingen op zowel de 2.4 GHz- als de 5 GHz-band kunnen gebruiken om de gevolgen van interferentie en congestie te beperken. De 4K-QAM-modulatie biedt onder verder gelijke omstandigheden tot 20% hogere theoretische datasnelheden dan de 1024-QAM-modulatie van Wi-Fi 6. De router ondersteunt een gecombineerde theoretische dual-band datasnelheid van maximaal 6452 Mbps, met 4×4 MIMO en een kanaalbreedte van 160 MHz op de 5 GHz-band. De werkelijke snelheden zijn afhankelijk van de mogelijkheden van clients en de netwerkomstandigheden.

Met 5× 2.5G Ethernet-poorten en 1× USB 3.0-poort ondersteunt de router snelle bekabelde verbindingen en opslaguitbreiding. Daarnaast is hij compatibel met meer dan 30 VPN-diensten, biedt hij krachtige VPN-prestaties tot 680Mbps met WireGuard® en OpenVPN-DCO en wordt gratis Bark Parental Control meegeleverd. Zo worden prestaties, gebruiksgemak en beveiliging goed gecombineerd.

![gl-be6500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/hardware_info/be6500_interface.jpg){class="glboxshadow"}

**Opmerking**: Flint 3e en Flint 3 verschillen uiterlijk door de zeefdruk: de zeefdruk op Flint 3e is blauw en die op Flint 3 is wit.

## Inhoud van de verpakking {#package-contents}

- 1 x Flint 3e (GL-BE6500)
- 1 x Voedingsadapter
- 1 x Ethernet-kabel
- 1 x Gebruikershandleiding
- 1 x Bedankkaart
- 1 x Adapter (afhankelijk van het land van levering)

Bekijk hieronder de uitpakvideo van Flint 3e.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-E0LtWqshk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Flint 3e instellen {#how-to-set-up-flint-3e}

Bekijk deze installatievideo of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R40QsUFYuUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Inschakelen {#1-power-on}

Zet de tweedelige voedingsadapter in elkaar. Sluit de adapter aan op je router en steek de stekker in een stopcontact. De router start automatisch op.

### 2. Een apparaat verbinden {#2-connect-device}

Verbind een apparaat, zoals een computer, laptop of smartphone, via Wi-Fi of Ethernet met de router.

- Ethernet

    Sluit je apparaat met een Ethernet-kabel aan op de LAN-poort van de router.

- Wi-Fi

    Ga op je apparaat naar Settings -> WLAN, zoek de Wi-Fi-netwerknaam van je router in de lijst met beschikbare netwerken en voer het wachtwoord in om verbinding te maken. De standaardnetwerknaam en het wachtwoord staan op het label van de router.

### 3. Aanmelden bij het webbeheerpaneel {#3-log-in-to-web-admin-panel}

Open een webbrowser, voer `192.168.8.1` in de adresbalk in en meld je aan. Kies je taal, stel het beheerderswachtwoord in en klik vervolgens op **Apply**.

### 4. Internet instellen {#4-internet-setup}

**Opmerking:** de volgende instructies gelden voor gebruikers die de router configureren via het GL.iNet Web Admin Panel. Als je liever de GL.iNet-app gebruikt, [download je de app](https://www.gl-inet.com/app/){target="_blank"} en volg je de instructies op het scherm.

Configureer je Flint 3e met een van de ondersteunde methoden voor internetverbindingen: Ethernet, Repeater, Tethering of Cellular. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je meerdere internetverbindingen in.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_ethernet.jpg){class="glboxshadow"}

    Sluit de WAN-poort van Flint 3e met een Ethernet-kabel aan op een upstream apparaat, zoals een modem.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Ethernet op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een Ethernet-kabel](../../interface_guide/internet_ethernet.md) voor uitgebreide instructies.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_repeater.jpg){class="glboxshadow"}

    1. Zoek op de pagina INTERNET van het webbeheerpaneel het gedeelte Repeater en klik op **Connect**.
    2. Selecteer een Wi-Fi-netwerk uit de beschikbare netwerken.
    3. Voer het wachtwoord in en klik op **Apply**.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Repeater op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een bestaand Wi-Fi-netwerk](../../interface_guide/internet_repeater.md) voor uitgebreide instructies.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_tethering.jpg){class="glboxshadow"}

    1. Sluit je mobiele apparaat, zoals een smartphone of USB-dongle, met een USB-kabel aan op de USB-poort van de router.
    2. Ga op je mobiele apparaat naar Settings en schakel USB Tethering in.
    3. Klik op de pagina INTERNET van het webbeheerpaneel in het gedeelte Tethering op **Connect**.

    Zodra de router met internet is verbonden, verschijnt in het gedeelte Tethering op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via USB-tethering](../../interface_guide/internet_tethering.md) voor uitgebreide instructies.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_cellular.jpg){class="glboxshadow"}

    Sluit een mobiele USB-modem aan op de USB-poort van Flint 3e. Hiermee kun je de internetverbinding van de USB-modem delen met alle verbonden apparaten.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Cellular op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een mobiel netwerk](../../interface_guide/internet_cellular.md) voor uitgebreide instructies.

---

Hieronder vind je een overzicht van de functies in het webbeheerpaneel van Flint 3e.

## Wireless {#wireless}

Op de pagina Wireless kun je instellingen voor het 5 GHz- en 2.4 GHz-Wi-Fi-netwerk configureren. Je kunt Wi-Fi inschakelen, het TX-vermogen instellen, de Wi-Fi-naam (SSID) opgeven, een willekeurige BSSID inschakelen, de Wi-Fi-beveiligingsmodus en het wachtwoord selecteren, de zichtbaarheid van de SSID configureren en de Wi-Fi-modus, bandbreedte en het kanaal kiezen.

Daarnaast ondersteunt Flint 3e MLO Wi-Fi (Multi-Link Operation), waarmee meerdere draadloze netwerken tegelijk worden gecombineerd voor meer bandbreedte en betrouwbaardere verbindingen.

Raadpleeg [Wireless](../../interface_guide/wireless.md) om Wireless in te stellen.

## Clients {#clients}

De pagina Clients toont informatie over verbonden apparaten. Voor elke client worden de naam, het IP- en MAC-adres, de download- en uploadsnelheid en het totale verkeer weergegeven. Je kunt de client ook blokkeren en andere handelingen uitvoeren.

Raadpleeg [Clients](../../interface_guide/clients.md) om Clients in te stellen.

## Clouddiensten {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} biedt een eenvoudige manier om GL.iNet-routers op afstand te openen en beheren.

    Raadpleeg [GoodCloud](../../interface_guide/cloud.md) om GoodCloud in te stellen.

=== "AstroWarp"

    AstroWarp is een geavanceerd netwerkplatform voor naadloze externe netwerken en extern apparaatbeheer. AstroWarp is speciaal ontwikkeld voor integratie met GL.iNet-routers en ondersteunt uitgebreid apparaatbeheer voor volledige netwerken, waaronder het beheer van boven- en onderliggende apparaten. Door zich te richten op netwerkbreed beheer en toekomstige ondersteuning voor beheer op hardwareniveau biedt AstroWarp een robuustere en betrouwbaardere oplossing voor apparaatbeheer en het onderhouden van veilige, stabiele netwerken.

    Raadpleeg [AstroWarp](../../interface_guide/astrowarp.md) om AstroWarp in te stellen.

## VPN {#vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk. Flint 3e ondersteunt OpenVPN en WireGuard.

=== "OpenVPN"

    Flint 3e en andere GL.iNet-routers ondersteunen het OpenVPN-protocol, dat een sterke beveiliging biedt. Volg deze tutorials om OpenVPN in te stellen:

    * [Een OpenVPN-client instellen](../../interface_guide/openvpn_client.md)
    * [Een OpenVPN-server instellen](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 3e en andere GL.iNet-routers ondersteunen het WireGuard-protocol, dat hoge snelheden en gebruiksgemak biedt. Volg deze tutorials om WireGuard in te stellen:

    * [Een WireGuard-client instellen](../../interface_guide/wireguard_client.md)
    * [Een WireGuard-server instellen](../../interface_guide/wireguard_server.md)

## Netwerk {#network}

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Ethernet, Tethering en Cellular. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) om Multi-WAN in te stellen.

=== "LAN"

    Een LAN (Local Area Network) is een netwerk dat computers en apparaten binnen een beperkt geografisch gebied, zoals een huis of kantoor, met elkaar verbindt. Het maakt snelle gegevensoverdracht en het delen van bronnen mogelijk, zodat apparaten efficiënt met elkaar kunnen communiceren.
    
    Raadpleeg [LAN](../../interface_guide/lan.md) om het LAN in te stellen.

=== "Guest Network"

    Je kunt een subnet instellen binnen de privé-IPv4-adresbereiken 192.168.0.0/16, 172.16.0.0/12 of 10.0.0.0/8. Ook kun je de IP-adressen van de gateway en het subnetmasker opgeven en beveiligingsinstellingen, zoals AP-isolatie, voor het gastnetwerk configureren.

    Raadpleeg [Guest Network](../../interface_guide/guest_network.md) om het gastnetwerk in te stellen.

=== "IoT Network"

    Hiermee kun je een apart Wi-Fi-netwerk voor IoT-apparaten maken. Het is geïsoleerd van het hoofdnetwerk en biedt betere compatibiliteit en beveiliging.

    Raadpleeg [IoT Network](../../interface_guide/iot_network.md) om het IoT Network in te stellen.

---

=== "DNS"

    Op de pagina DNS kun je aangepaste DNS-servers instellen, bescherming tegen DNS-rebindingaanvallen inschakelen, de DNS-instellingen van alle clients overschrijven en toestaan dat aangepaste DNS de VPN-DNS overschrijft. Je kunt DNS-servers gebruiken die automatisch van upstreamapparaten zijn verkregen of handmatig aangepaste DNS-servers opgeven.

    Raadpleeg [DNS](../../interface_guide/dns.md) om DNS in te stellen.

=== "Ethernet Port"

    Op de pagina Ethernet Port kun je de WAN- en LAN-poorten configureren, de WAN/LAN-interface op Ethernet instellen, de MAC-modus en het MAC-adres voor de WAN-interface opgeven en de onderhandelde snelheid van de netwerkpoort weergeven.

    Raadpleeg [Ethernet Port](../../interface_guide/ethernet_port.md) om Ethernet-poorten te beheren.

=== "IPv6"

    IPv6 (Internet Protocol version 6) is de nieuwste versie van het Internet Protocol en is ontwikkeld als opvolger van IPv4. Het biedt een veel grotere adresruimte en maakt daardoor een vrijwel onbeperkt aantal unieke IP-adressen mogelijk. Dit is noodzakelijk om het groeiende aantal apparaten met een internetverbinding te ondersteunen.

    Raadpleeg [IPV6](../../interface_guide/ipv6.md) om IPV6 in te stellen.

=== "IGMP Snooping"

    IGMP snooping is een techniek voor netwerkoptimalisatie die in Ethernet-switches wordt gebruikt om multicastverkeer te beheren en regelen.
    
    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) om IGMP snooping in te stellen.

---

=== "Network Mode"

    De netwerkmodus omvat de configuratie-instellingen die bepalen hoe een apparaat verbinding maakt met een netwerk en met andere apparaten communiceert.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) om de netwerkmodus in te stellen.

=== "Drop-in gateway"

    Drop-in Gateway breidt de functies van je hoofdrouter uit met AdGuard Home, versleutelde DNS en een VPN-client.
    
    Raadpleeg de volgende links om een drop-in gateway in te stellen:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Een drop-in gateway instellen](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Netwerkversnelling kan de CPU-belasting verlagen en het doorsturen van verkeerspakketten versnellen.

    Raadpleeg [Network Acceleration](../../interface_guide/network_acceleration.md) om netwerkversnelling in te stellen.

## Flow Control {#flow-control}

=== "DPI Engine"

    DPI (Deep Packet Inspection) is een kernfunctie voor intelligent netwerkbeheer. DPI omzeilt de beperking van traditionele routers, die alleen bron- of bestemmingsadressen identificeren, analyseert de inhoud van gegevenspakketten grondig en identificeert door vergelijking met een kenmerkenbibliotheek nauwkeurig welke toepassingen en websites gebruikers openen. Hierdoor zijn fijnmazige verkeersclassificatie en -regeling mogelijk.
    
    De DPI-functie van GL.iNet is geïntegreerd met [Netify](https://www.netify.ai/){target="_blank"} en gebruikt een lichte ingebouwde plug-in voor efficiënte implementatie. Dankzij de online bijgewerkte kenmerkendatabase van Netify biedt de functie betrouwbaar beheer, waardoor netwerkregeling nauwkeuriger en efficiënter wordt.

    Raadpleeg [DPI Engine](../../interface_guide/dpi_engine.md) voor uitgebreide instructies.

=== "Data Statistics"

    Data Statistics biedt een intelligent verkeersdashboard dat netwerkgebruik per toepassing categoriseert en visualiseert. Hiermee kun je realtime en historisch verkeer bewaken voor beter inzicht in en beheer van het netwerk.

    Raadpleeg [Data Statistics](../../interface_guide/data_statistics.md) voor uitgebreide instructies.

=== "Content Filter"

    Content Filter biedt intelligente online beveiliging op basis van DPI-classificatie en blokkeert automatisch schadelijke of kwaadaardige websites om je netwerk schoon en veilig te houden.

    Raadpleeg [Content Filter](../../interface_guide/content_filter.md) voor uitgebreide instructies.

---

=== "QoS"

    QoS (Quality of Service) optimaliseert de bandbreedtetoewijzing door tijdens netwerkcongestie prioriteit te geven aan belangrijke activiteiten, zoals videogesprekken en gaming. Hierdoor neemt de latentie af en verbeteren de algemene netwerkprestaties. Dit geldt voor lokaal clientverkeer en verkeer in de VPN Client-tunnel, maar niet voor verkeer dat wordt ontvangen wanneer de router als VPN Server werkt.

    Raadpleeg [QoS](../../interface_guide/qos.md) voor uitgebreide instructies.

=== "SQM"

    SQM (Smart Queue Management) beheert het netwerkverkeer van je router op intelligente wijze om de latentie en 'bufferbloat' te beperken. Zo verlopen games en spraakoproepen soepeler.

    Raadpleeg [SQM](../../interface_guide/sqm.md) voor uitgebreide instructies.

=== "Parental Control"

    Parental Control is bedoeld om je te helpen de apparaten van je kinderen te beheren. Je kunt onder meer de schermtijd beperken en toegang tot bepaalde inhoud blokkeren.

    Raadpleeg [Parental Control](../../interface_guide/parental_control_v4.9.md) om ouderlijk toezicht in te stellen.

## Security {#security}

=== "Port Forwarding"

    Met port forwarding kunnen externe servers en apparaten op internet toegang krijgen tot apparaten in een privénetwerk.

    Raadpleeg [Port Forwarding](../../interface_guide/port_forwarding.md) om port forwarding in te stellen.

=== "ACL"

    Met ACL, een afkorting van Access Control List, kun je regels maken om netwerkverkeer te beheren op basis van verbindingsprotocollen, apparaatadressen en poorten. De regels bepalen of netwerktoegang wordt toegestaan of geblokkeerd. Als meerdere ACL-regels conflicteren, past het systeem de regel met de hoogste prioriteit toe.

    Raadpleeg [ACL](../../interface_guide/acl.md) voor meer informatie.

=== "Admin Access"

    Met Admin Access kun je verschillende beveiligingsinstellingen configureren om je netwerk en router tegen onbevoegde toegang te beschermen. De pagina bevat de volgende opties:

    * Local Access Control: beheer en beperk de toegang tot de routerinterface vanaf apparaten die met je lokale netwerk zijn verbonden.
    * Remote Access Control: configureer en beperk toegang tot de routerinterface vanaf externe locaties via internet om de beveiliging tegen bedreigingen van buitenaf te verbeteren.
    * Open Ports on Router: bepaal welke poorten op de router geopend zijn om mogelijke kwetsbaarheden en onbevoegde toegang te beperken.

    Raadpleeg [Admin Access](../../interface_guide/admin_access.md) voor meer informatie.

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

---

=== "AdGuard Home"

    AdGuard Home blokkeert advertenties en trackers in het hele netwerk. De toepassing werkt als DNS-server en filtert ongewenste inhoud op alle apparaten die met een thuisnetwerk zijn verbonden.

    Raadpleeg [AdGuard Home](../../interface_guide/adguardhome.md) om AdGuard Home in te stellen.

=== "Bark"

    De in Flint 3e geïntegreerde dienst Bark helpt de digitale wereld van je kind te beschermen en biedt uitgebreide online beveiliging. Normaal is hiervoor een betaald abonnement vereist. Door de samenwerking met Bark biedt GL.iNet het Bark Home-abonnement echter gratis aan op bepaalde routermodellen, waaronder Flint 3e. Dit biedt geavanceerde bewaking en waarschuwingen zonder extra kosten.

    Raadpleeg [Bark](../../interface_guide/bark.md) voor meer informatie.

=== "Tailscale"

    Tailscale is een VPN-dienst waarmee je overal toegang hebt tot je apparaten en toepassingen.
    
    Raadpleeg [Tailscale](../../interface_guide/tailscale.md) om Tailscale in te stellen.

=== "ZeroTier"

    ZeroTier is een softwaregedefinieerde netwerkoplossing waarmee gebruikers via internet beveiligde virtuele netwerken kunnen maken en apparaten kunnen verbinden alsof ze zich in hetzelfde lokale netwerk bevinden.
    
    Raadpleeg [ZeroTier](../../interface_guide/zerotier.md) om ZeroTier in te stellen.

=== "Tor"

    Tor, een afkorting van The Onion Router, is een privacygericht netwerk dat anonieme communicatie via internet mogelijk maakt. Internetverkeer wordt via een reeks door vrijwilligers beheerde servers (nodes) geleid om de locatie en het gebruik van de gebruiker te verhullen. Hierdoor zijn online activiteiten moeilijk te traceren.
    
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

    Raadpleeg [Overview](../../interface_guide/system_overview.md) voor uitgebreide instructies.

=== "Admin Password"

    Op de pagina Admin Password kun je het wachtwoord voor de beheerinterface van de router beheren, zodat alleen bevoegde gebruikers instellingen kunnen wijzigen.

    Raadpleeg [Admin Password](../../interface_guide/admin_password.md) voor meer informatie.

=== "Upgrade"

    De pagina Upgrade wordt gebruikt om de firmware van je router bij te werken naar de nieuwste versie, voor betere prestaties en beveiliging en nieuwe functies. Deze pagina biedt twee opties voor upgrades:

    * Firmware Online Upgrade: controleer automatisch op de server van de fabrikant of de nieuwste firmwareversie beschikbaar is. Als deze online beschikbaar is, kun je de nieuwste versie installeren.
    * Firmware Local Upgrade: upload handmatig een firmwarebestand vanaf je computer om de router bij te werken. Zo bepaal je zelf de versie en het moment van de upgrade.

    Met deze opties houd je je router bijgewerkt met de nieuwste verbeteringen en correcties.

    Raadpleeg [Upgrade](../../interface_guide/upgrade.md) voor uitgebreide instructies.

=== "Scheduled Tasks"

    Op de pagina Scheduled Tasks kun je verschillende routerfuncties volgens een vooraf ingesteld schema automatiseren. Dit verhoogt het gemak en de efficiëntie. De belangrijkste functies op deze pagina zijn:

    * LED Display Schedule: stel een schema in om de leds van de router automatisch in of uit te schakelen en zo lichtvervuiling op bepaalde tijden te beperken.
    * Schedule Reboot: configureer de router om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.
    * Wi-Fi Status Schedule: stel een schema in om de 5GHz / 2.4GHz / MLO-Wi-Fi-band te beheren en zo de beschikbaarheid van het netwerk en het energieverbruik beter te regelen.

    Met deze planningsopties heb je meer controle over de werking van je router en kun je deze afstemmen op je specifieke behoeften en voorkeuren.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor uitgebreide instructies.

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
