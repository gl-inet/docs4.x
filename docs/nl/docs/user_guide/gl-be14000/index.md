# Gebruikershandleiding Flint 4 (GL-BE14000) {#flint-4-gl-be14000-user-guide}

## Productoverzicht {#product-overview}

Flint 4 (GL-BE14000) geeft een nieuwe invulling aan de thuisrouter. De tri-band Wi-Fi 7 met MLO levert pieksnelheden van 688 Mbps (2.4 GHz) + 4323 Mbps (5 GHz) + 8646 Mbps (6 GHz). Voor bekabelde verbindingen heeft de router een volledige multi-gig backbone met één 10G SFP+ WAN/LAN-poort, één 10GE WAN/LAN-poort, één 2.5GE WAN/LAN-poort, drie 2.5GE LAN-poorten en vier 1GE LAN-poorten. De krachtige VPN-ondersteuning levert met zowel WireGuard® als OpenVPN DCO een doorvoer tot 1.5 Gbps. Het ingebouwde 2.4-inch touchscreen maakt realtime bewaking van de netwerkstatus mogelijk en toont belangrijke netwerkgegevens rechtstreeks op het apparaat.

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

- 1 x Flint 4 (GL-BE14000)
- 1 x Voedingsadapter
- 1 x Ethernet-kabel
- 1 x Gebruikershandleiding
- 1 x Bedankkaart
- 1 x Adapter (afhankelijk van het land van levering)

Bekijk hieronder de uitpakvideo van Flint 4.

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Flint 4 instellen {#how-to-set-up-flint-4}

Bekijk deze installatievideo of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Inschakelen {#1-power-on}

Zet de tweedelige voedingsadapter in elkaar. Sluit de adapter aan op je router en steek de stekker in een stopcontact. De router start automatisch op.

### 2. Een apparaat verbinden {#2-connect-device}

Verbind een apparaat, zoals een computer, laptop of smartphone, via Wi-Fi of Ethernet met de router.

- Ethernet

    Sluit je apparaat met een Ethernet-kabel aan op de LAN-poort van de router.

- Wi-Fi

    Zoek op je apparaat de Wi-Fi-netwerknaam van de router in de lijst met beschikbare netwerken en voer het wachtwoord in om verbinding te maken. De standaardnetwerknaam (SSID) en het wachtwoord staan op het label van de router.

### 3. Aanmelden bij het webbeheerpaneel {#3-log-in-to-web-admin-panel}

Open een webbrowser, voer `192.168.8.1` in de adresbalk in en meld je aan. Stel het beheerderswachtwoord en de Wi-Fi-gegevens in en klik vervolgens op **Apply**.

### 4. Internet instellen {#4-internet-setup}

Configureer je Flint 4 met een van de ondersteunde methoden voor internetverbindingen: Ethernet (SFP+), Ethernet (RJ45), Repeater, Tethering of Cellular. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je meerdere internetverbindingen in.

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}

    Flint 4 heeft een 10G SFP+ WAN/LAN-poort voor glasvezeluplinks, snelle switchbackhaul en krachtige netwerkuitbreiding. Deze poort is standaard ingesteld op WAN en kan indien nodig naar LAN worden omgeschakeld.

    Hieronder zie je een voorbeeld waarbij de 10G SFP+-poort van Flint 4 via een optische transceiver en glasvezelkabel met de glasvezeluplink van de internetprovider wordt verbonden. Raadpleeg [De 10G SFP+-poort op Flint 4 aansluiten](../../faq/connecting_10g_sfp_plus_port_on_flint4.md) voor meer oplossingen.

    1. Plaats een compatibele 10G SFP+-transceiver in de SFP+-poort van Flint 4 en verbind deze vervolgens met de glasvezeluplink van je internetprovider.
    2. Flint 4 probeert automatisch via DHCP netwerkparameters (IP-adres, gateway en DNS) te verkrijgen. Als je internetprovider PPPoE of statische IP-adressering vereist, pas je de instellingen van de WAN-verbinding in het webbeheerpaneel dienovereenkomstig aan.
    3. Zodra de internetverbinding tot stand is gebracht, wordt het gedeelte Ethernet op de startpagina van het touchscreen blauw (actief). Tik op het touchscreen op Ethernet of meld je aan bij het webbeheerpaneel om de verbindingsgegevens te bekijken.

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}

    1. Sluit de WAN-poort van Flint 4 met een Ethernet-kabel aan op een upstream apparaat, zoals een internetmodem, netwerkswitch of Ethernet-wandaansluiting.
    2. Flint 4 probeert automatisch via DHCP netwerkparameters (IP-adres, gateway en DNS) te verkrijgen. Als je internetprovider PPPoE of statische IP-adressering vereist, pas je de instellingen van de WAN-verbinding in het webbeheerpaneel dienovereenkomstig aan.
    3. Zodra de internetverbinding tot stand is gebracht, wordt het gedeelte Ethernet op de startpagina van het touchscreen blauw (actief). Tik op het touchscreen op Ethernet of meld je aan bij het webbeheerpaneel om de verbindingsgegevens te bekijken.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. Tik op het touchscreen op **Repeater**. Het apparaat scant vervolgens naar beschikbare Wi-Fi-netwerken.
    2. Selecteer het Wi-Fi-netwerk dat je met Flint 4 wilt uitbreiden.
    3. Voer het wachtwoord in en tik op **Apply**.
    4. Zodra de internetverbinding tot stand is gebracht, wordt het gedeelte Repeater op de startpagina van het touchscreen blauw (actief). Tik op het touchscreen op Repeater of meld je aan bij het webbeheerpaneel om de verbindingsgegevens te bekijken.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. Sluit een mobiel apparaat, zoals een smartphone, met een USB-kabel aan op de USB-poort van Flint 4.
    2. Ga op je mobiele apparaat naar Settings en schakel **USB Tethering** of **Personal Hotspot** in. Tik op een iPhone op **Trust This Device** als daarom wordt gevraagd.
    3. Selecteer op het touchscreen van Flint 4 **Tethering** en tik op **Connect**. De router maakt vervolgens verbinding met je apparaat.
    4. Zodra de internetverbinding tot stand is gebracht, wordt het gedeelte Tethering op de startpagina van het touchscreen blauw (actief). Tik op het touchscreen op Tethering of meld je aan bij het webbeheerpaneel om de verbindingsgegevens te bekijken.

    **Opmerking**: controleer bij een mislukte verbinding of je een voedingsadapter van 12V/4A gebruikt. Bij onvoldoende voeding kan de USB-poort het aangesloten apparaat mogelijk niet goed van stroom voorzien. Herhaal vervolgens de bovenstaande stappen of meld je aan bij het webbeheerpaneel om de status van de Tethering-verbinding te controleren.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. Sluit een mobiele modem of USB-dongle aan op de USB-poort van Flint 4. Hiermee kun je de internetverbinding van een USB-modem delen met alle verbonden apparaten.
    2. Zodra de internetverbinding tot stand is gebracht, wordt het gedeelte Cellular op de startpagina van het touchscreen blauw (actief). Tik op het touchscreen op Cellular of meld je aan bij het webbeheerpaneel om de verbindingsgegevens te bekijken.

---

Hieronder vind je een overzicht van de functies in het webbeheerpaneel van Flint 4.

## Wireless {#wireless}

Op de pagina Wireless kun je verschillende Wi-Fi-netwerken voor Flint 4 configureren, waaronder MLO Wi-Fi, Main Network, Guest Network en IoT Network.

Raadpleeg [Wireless](../../interface_guide/wireless.md) voor meer informatie.

## Clients {#clients}

De pagina Clients toont informatie over verbonden apparaten. Voor elke client worden de naam, het IP- en MAC-adres, de download- en uploadsnelheid en het totale verkeer weergegeven. Je kunt de client ook blokkeren en andere handelingen uitvoeren.

Raadpleeg [Clients](../../interface_guide/clients.md) voor meer informatie.

## Clouddiensten {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} biedt een eenvoudige manier om GL.iNet-routers op afstand te openen en beheren.

    Raadpleeg [GoodCloud](../../interface_guide/cloud.md) voor meer informatie.

=== "AstroWarp"

    AstroWarp is een geavanceerde netwerkfunctie die in GL.iNet-routers is geïntegreerd. De functie biedt naadloze externe toegang tot je thuisnetwerk zonder registratie of aanmelding. Het AmneziaWG-protocol met ingebouwde verkeersobfuscatie houdt je verbinding stabiel en veilig en is daardoor ideaal voor betrouwbare externe toegang, waar je ook bent. Je kunt rechtstreeks via het beheerpaneel van de GL.iNet-router een AstroWarp-netwerk instellen. Koppel je routers met een toegangscode om je reisrouter binnen enkele seconden veilig met je thuisnetwerk te verbinden.

    Raadpleeg [AstroWarp](../../interface_guide/astrowarp.md) voor meer informatie.

## VPN {#vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk. Flint 4 ondersteunt OpenVPN- en WireGuard-protocollen.

=== "OpenVPN"

    Flint 4 en andere GL.iNet-routers ondersteunen het OpenVPN-protocol, dat een sterke beveiliging biedt. Volg deze tutorials om OpenVPN in te stellen:

    * [Een OpenVPN-client instellen](../../interface_guide/openvpn_client.md)
    * [Een OpenVPN-server instellen](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4 en andere GL.iNet-routers ondersteunen het WireGuard-protocol, dat hoge snelheden en gebruiksgemak biedt. Volg deze tutorials om WireGuard in te stellen:

    * [Een WireGuard-client instellen](../../interface_guide/wireguard_client.md)
    * [Een WireGuard-server instellen](../../interface_guide/wireguard_server.md)

## Netwerk {#network}

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Cellular, Repeater en Ethernet. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) voor meer informatie.

=== "Subnet"

    De pagina Subnet centraliseert het beheer van LAN, Guest Network, IoT Network en aangepaste VLAN Networks. Je kunt meerdere subnets maken en beheren om verschillende soorten apparaten of verkeer van elkaar te scheiden.

    Raadpleeg [Subnet](../../interface_guide/subnet.md) voor meer informatie.

=== "Ethernet Port"

    Op de pagina Ethernet Port kun je de rol van Ethernet-poorten (WAN/LAN) en VLAN-segmentatie beheren en poortgegevens, zoals het MAC-adres en de onderhandelde snelheid, bekijken.

    Raadpleeg [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md) voor meer informatie.

---

=== "DNS"

    Op de pagina DNS kun je aangepaste DNS-servers instellen, bescherming tegen DNS-rebindingaanvallen inschakelen, de DNS-instellingen van alle clients overschrijven en toestaan dat aangepaste DNS de VPN-DNS overschrijft. Je kunt DNS-servers gebruiken die automatisch van upstreamapparaten zijn verkregen of handmatig aangepaste DNS-servers opgeven.

    Raadpleeg [DNS](../../interface_guide/dns.md) voor meer informatie.

=== "IPv6"

    IPv6 (Internet Protocol version 6) is de nieuwste versie van het Internet Protocol en is ontwikkeld als opvolger van IPv4. Het biedt een veel grotere adresruimte en maakt daardoor een vrijwel onbeperkt aantal unieke IP-adressen mogelijk. Dit is noodzakelijk om het groeiende aantal apparaten met een internetverbinding te ondersteunen.

    Raadpleeg [IPV6](../../interface_guide/ipv6.md) voor meer informatie.

=== "IGMP Snooping"

    IGMP snooping is een techniek voor netwerkoptimalisatie die in Ethernet-switches wordt gebruikt om multicastverkeer te beheren en regelen.

    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) voor meer informatie.

---

=== "Network Mode"

    De netwerkmodus bepaalt de verschillende rollen en functies die een router kan vervullen voor uiteenlopende netwerkimplementaties. Veelgebruikte modi zijn Router, Extender en Access Point.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) voor meer informatie.

=== "Drop-in Gateway"

    Drop-in Gateway is een flexibele functie waarmee je de mogelijkheden van een bestaande hoofdrouter kunt uitbreiden zonder deze te vervangen of opnieuw te configureren. Door een GL.iNet-router als Drop-in Gateway in te stellen, kun je geavanceerde functies aan de bestaande netwerkinfrastructuur toevoegen, zoals AdGuard Home, VPN en versleutelde DNS.

    Raadpleeg de onderstaande links om een drop-in gateway in te stellen.

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Een drop-in gateway instellen](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Netwerkversnelling kan de CPU-belasting verlagen en het doorsturen van verkeerspakketten versnellen.

    Raadpleeg [Network Acceleration](../../interface_guide/network_acceleration.md) voor meer informatie.

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

---

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

=== "Port Forwarding"

    Met port forwarding kunnen externe servers en apparaten op internet toegang krijgen tot apparaten in een privénetwerk.

    Raadpleeg [Port Forwarding](../../interface_guide/port_forwarding.md) voor meer informatie.

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

---

=== "AdGuard Home"

    AdGuard Home blokkeert advertenties en trackers in het hele netwerk. De toepassing werkt als DNS-server en filtert ongewenste inhoud op alle apparaten die met een thuisnetwerk zijn verbonden.

    Raadpleeg [AdGuard Home](../../interface_guide/adguardhome.md) voor meer informatie.

=== "Bark"

    De in Flint 4 geïntegreerde dienst Bark helpt de digitale wereld van je kind te beschermen en biedt uitgebreide online beveiliging. Normaal is hiervoor een betaald abonnement vereist. Door de samenwerking met Bark biedt GL.iNet het Bark Home-abonnement echter gratis aan op bepaalde routermodellen, waaronder Flint 4. Dit biedt geavanceerde bewaking en waarschuwingen zonder extra kosten.

    Raadpleeg [Bark](../../interface_guide/bark.md) voor meer informatie.

=== "Tailscale"

    Tailscale is een VPN-dienst waarmee je overal toegang hebt tot je apparaten en toepassingen.

    Raadpleeg [Tailscale](../../interface_guide/tailscale.md) voor meer informatie.

=== "ZeroTier"

    ZeroTier is een softwaregedefinieerde netwerkoplossing waarmee gebruikers via internet beveiligde virtuele netwerken kunnen maken en apparaten kunnen verbinden alsof ze zich in hetzelfde lokale netwerk bevinden.

    Raadpleeg [ZeroTier](../../interface_guide/zerotier.md) voor meer informatie.

=== "Tor"

    Tor, een afkorting van The Onion Router, is een privacygericht netwerk dat anonieme communicatie via internet mogelijk maakt. Internetverkeer wordt via een reeks door vrijwilligers beheerde servers (nodes) geleid om de locatie en het gebruik van de gebruiker te verhullen. Hierdoor zijn online activiteiten moeilijk te traceren.

    Raadpleeg [Tor](../../interface_guide/tor.md) voor meer informatie.

## Systeem {#system}

=== "Overview"

    De pagina Overview biedt een uitgebreid overzicht van de huidige status en prestatiegegevens van je router. Op deze pagina kun je het volgende bekijken:

    * CPU Average Load: bewaak de gemiddelde belasting van de CPU van je router om de prestaties te beoordelen en mogelijke knelpunten op te sporen.
    * Memory Usage: controleer hoeveel geheugen van je router in gebruik is om het beheer van bronnen te ondersteunen.
    * Flash Usage: bekijk het gebruik van de flashopslag van de router en controleer of er voldoende ruimte is voor firmware en configuratiegegevens.
    * Device Info: bekijk uitgebreide systeeminformatie over je router, waaronder uptime, hostnaam, model, architectuur, OpenWrt-versie, kernelversie, apparaat-ID, MAC-adres van het apparaat en serienummer van het apparaat.
    * External Storage: controleer de status van externe opslagapparaten die op de router zijn aangesloten, zoals USB-stations of TF-kaarten.

    Deze functies bieden essentiële informatie en bedieningselementen om de werking van je router effectief te beheren en bewaken.

    Raadpleeg [Overview](../../interface_guide/system_overview.md) voor meer informatie.

=== "Admin Password"

    Op de pagina Admin Password kun je het wachtwoord voor de beheerinterface van de router beheren, zodat alleen bevoegde gebruikers instellingen kunnen wijzigen.

    Raadpleeg [Admin Password](../../interface_guide/admin_password.md) voor meer informatie.

=== "Upgrade"

    De pagina Upgrade wordt gebruikt om de firmware van je router bij te werken naar de nieuwste versie, voor betere prestaties en beveiliging en nieuwe functies. Deze pagina biedt twee opties voor upgrades:

    * Firmware Online Upgrade: controleer automatisch op de server van de fabrikant of de nieuwste firmwareversie beschikbaar is. Als deze online beschikbaar is, kun je de nieuwste versie installeren.
    * Firmware Local Upgrade: upload handmatig een firmwarebestand vanaf je computer om de router bij te werken. Zo bepaal je zelf de versie en het moment van de upgrade.

    Raadpleeg [Upgrade](../../interface_guide/upgrade.md) voor meer informatie.

---

=== "Scheduled Tasks"

    Op de pagina Scheduled Tasks kun je verschillende routerfuncties volgens een vooraf ingesteld schema automatiseren. Dit verhoogt het gemak en de efficiëntie. De belangrijkste functies op deze pagina zijn:

    * LCD Display Schedule: stel een schema in om het lcd-scherm van de router automatisch in of uit te schakelen en zo lichtvervuiling op bepaalde tijden te beperken.
    * Schedule Reboot: configureer de router om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.
    * Wi-Fi Status Schedule: stel een schema in om de 6GHz / 5GHz / 2.4GHz / MLO-Wi-Fi-band te beheren, de beschikbaarheid van het netwerk te regelen en het energieverbruik te verminderen.

    Met deze planningsopties heb je meer controle over de werking van je router en kun je deze afstemmen op je specifieke behoeften en voorkeuren.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor meer informatie.

=== "Display Management"

    De pagina Display Management biedt een volledig pakket functies om het touchscreen en de bijbehorende instellingen te beheren.

    ‒ Wallpaper: pas de achtergrond en de weergavestijl bij activering aan.
    ‒ Brightness: pas de helderheid van het touchscreen aan. Gebruik de schuifregelaar of voer een percentage in dat bij de lichtomstandigheden past.
    ‒ Auto Lock: stel in na hoeveel tijd zonder activiteit het scherm automatisch wordt vergrendeld. Het bereik is 1 tot 30 minuten.
    ‒ Screen Always On: schakel deze optie in of uit om te bepalen of het touchscreen continu aan blijft of na inactiviteit wordt uitgeschakeld.
    ‒ Enable Screen Passcode: stel een toegangscode voor het touchscreen in voor extra beveiliging.

    Raadpleeg [Display Management](../../interface_guide/display_management.md) voor meer informatie.

=== "Time Zone"

    Op de pagina Time Zone kun je de juiste tijdzone voor je router instellen. Hierdoor krijgen alle geplande taken, logboeken en systeemgebeurtenissen een nauwkeurig tijdstempel op basis van je lokale tijd. Deze instelling is essentieel voor nauwkeurige registraties en een correcte uitvoering van tijdgebonden configuraties.

    Raadpleeg [Time Zone](../../interface_guide/time_zone.md) voor meer informatie.

---

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
