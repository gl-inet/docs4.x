# Gebruikershandleiding Marble (GL-B3000) {#marble-gl-b3000-user-guide}

## Productoverzicht {#product-overview}

De Marble-router (GL-B3000) is op zichzelf een kunstwerk en is slim vormgegeven als fotolijst voor je favoriete afbeelding, zodat hij je woonruimte verfraait. Marble (GL-B3000) is niet alleen aantrekkelijk vormgegeven, maar biedt ook uitstekende prestaties met Wi-Fi 6 en VPN-ondersteuning.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

- 1 x Marble (GL-B3000)
- 1 x Gebruikershandleiding
- 1 x Bedankkaart
- 1 x Ethernet-kabel
- 1 x Wandmontageset
- 1 x Kleefpad
- 1 x Routerstandaard
- 1 x Fotolijst (optioneel)
- 1 x Voedingsadapter
- 1 x Adapter (afhankelijk van het land van levering)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Marble instellen {#how-to-set-up-marble}

Bekijk deze installatievideo's of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Inschakelen {#1-power-on}

Zet de tweedelige voedingsadapter in elkaar. Sluit de adapter aan op je router en steek de stekker in een stopcontact. De router start automatisch op.

### 2. Een apparaat verbinden {#2-connect-device}

Verbind een apparaat, zoals een computer, laptop of smartphone, via Wi-Fi of een Ethernet-kabel met de router.

- Ethernet

    Sluit je apparaat met een Ethernet-kabel aan op de LAN-poort van de router.

- Wi-Fi

    Ga op je apparaat naar Settings -> WLAN, zoek de Wi-Fi-netwerknaam van de router in de lijst met beschikbare netwerken en voer het wachtwoord in. De standaardnetwerknaam en het wachtwoord staan op het label van de router.

### 3. Aanmelden bij het webbeheerpaneel {#3-log-in-to-web-admin-panel}

Open een webbrowser, voer `192.168.8.1` in de adresbalk in en meld je aan. Kies je taal, stel het beheerderswachtwoord in en klik vervolgens op **Apply**.

### 4. Internet instellen {#4-internet-setup}

**Opmerking:** de volgende instructies gelden voor gebruikers die de router configureren via het GL.iNet Web Admin Panel. Als je liever de GL.iNet-app gebruikt, [download je de app](https://www.gl-inet.com/app/){target="_blank"} en volg je de instructies op het scherm.

Configureer je Marble met een van de ondersteunde methoden voor internetverbindingen: Ethernet of Repeater. Als je de functie [Multi-WAN](../../interface_guide/multi-wan.md) wilt gebruiken, stel je twee internetverbindingen in.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}

    Sluit een Ethernet-kabel aan tussen de WAN-poort van je router en een upstream apparaat, zoals een modem.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Ethernet op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een Ethernet-kabel](../../interface_guide/internet_ethernet.md) voor uitgebreide instructies.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. Zoek op de pagina INTERNET van het webbeheerpaneel het gedeelte Repeater en klik op **Connect**.
    2. Selecteer een Wi-Fi-netwerk uit de beschikbare netwerken.
    3. Voer het netwerkwachtwoord in en klik op **Apply**.

    Zodra de internetverbinding tot stand is gebracht, verschijnt in het gedeelte Repeater op de pagina INTERNET een groene stip.

    Raadpleeg [Verbinding maken met internet via een bestaand Wi-Fi-netwerk](../../interface_guide/internet_repeater.md) voor uitgebreide instructies.

---

## Wireless {#wireless}

Op de pagina Wireless kun je instellingen voor de Wi-Fi-netwerken op 5 GHz en 2.4 GHz configureren, waaronder het in- en uitschakelen van Wi-Fi, het zendvermogen, de Wi-Fi-naam (SSID), de Wi-Fi-beveiligingsmodus en het wachtwoord, de zichtbaarheid van de SSID, de Wi-Fi-modus, bandbreedte en het kanaal.

Raadpleeg [Wireless](../../interface_guide/wireless_v4.8.md) om Wireless in te stellen.

## Clients {#clients}

De pagina Clients toont informatie over verbonden apparaten. Voor elke client worden de apparaatnaam, het verbindingstype (via Ethernet of Wi-Fi), de IP- en MAC-adressen, de download- en uploadsnelheid en het totale verkeer weergegeven. Je kunt de client ook blokkeren en andere handelingen uitvoeren.

Raadpleeg [Clients](../../interface_guide/clients.md) om Clients in te stellen.

## VPN {#vpn}

Een VPN (virtual private network) maakt een beveiligde, versleutelde verbinding voor verkeer tussen je apparaat en de VPN-server. Een VPN biedt extra privacy en beveiliging via een VPN-client en geeft je via een VPN-server toegang tot een extern netwerk. Marble en andere GL.iNet-routers ondersteunen OpenVPN en WireGuard. Daarnaast wordt Tor ondersteund.

=== "OpenVPN"

    Marble en andere GL.iNet-routers ondersteunen het OpenVPN-protocol, dat een sterke beveiliging biedt. Volg deze tutorials om OpenVPN in te stellen:

    * [Een OpenVPN-client instellen](../../interface_guide/openvpn_client.md)
    * [Een OpenVPN-server instellen](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble en andere GL.iNet-routers ondersteunen het WireGuard-protocol, dat hoge snelheden en gebruiksgemak biedt. Volg deze tutorials om WireGuard in te stellen:

    * [Een WireGuard-client instellen](../../interface_guide/wireguard_client.md)
    * [Een WireGuard-server instellen](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor is een privacygerichte dienst waarmee je anoniem internet kunt gebruiken. Volg deze tutorials om Tor in te stellen:

    * [Tor instellen](../../interface_guide/tor.md)

## Toepassingen {#applications}

=== "Plug-ins"

    Plug-ins zijn aanvullende functies die de mogelijkheden van je router uitbreiden. Raadpleeg [Plug-ins](../../interface_guide/plugins.md) om plug-ins in te stellen.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecteert en actualiseert automatisch en in realtime het IP-adres dat aan een domein is gekoppeld. Het koppelt een domeinnaam aan het dynamische openbare IP-adres van je router, zodat je zonder statisch IP-adres op afstand toegang hebt tot je netwerk. Raadpleeg [Dynamic DNS](../../interface_guide/ddns.md) om Dynamic DNS in te stellen.

=== "GoodCloud"

    De dienst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} van GL.iNet biedt een eenvoudige manier om GL.iNet-routers op afstand te openen en beheren.
    
    Raadpleeg [GoodCloud](../../interface_guide/cloud.md) om GoodCloud in te stellen.

=== "AdGuard Home"

    AdGuard Home is een hulpmiddel van derden dat advertenties en tracking blokkeert om je te beschermen.
    
    Raadpleeg [AdGuard Home](../../interface_guide/adguardhome.md) om te lezen hoe je AdGuard Home inschakelt.

---

=== "Parental Control"

    Ouderlijk toezicht is een groep instellingen waarmee je de apparaten van je kinderen kunt beheren. Je kunt onder meer de schermtijd beperken en toegang tot bepaalde inhoud blokkeren. Marble biedt twee opties voor ouderlijk toezicht: de lokale versie van GL.iNet en de geïntegreerde versie van Bark, een app voor ouderlijk toezicht.

    Raadpleeg [Parental controls](../../interface_guide/parental_control.md) om ouderlijk toezicht in te stellen.

=== "ZeroTier"

    ZeroTier is een VPN-dienst waarmee je apparaten met een virtueel netwerk kunt verbinden. Raadpleeg [ZeroTier](../../interface_guide/zerotier.md) om ZeroTier in te stellen.

=== "Tailscale"

    Tailscale is een VPN-dienst waarmee je overal toegang hebt tot je apparaten en toepassingen. Raadpleeg [Tailscale](../../interface_guide/tailscale.md) om Tailscale in te stellen.

## Netwerk {#network}

=== "Firewall"

    De pagina Firewall biedt essentiële beveiligingsverbeteringen voor je netwerk. De pagina bevat functies zoals Port Forwarding, Open Ports en DMZ. Met deze hulpmiddelen kun je de verkeersstroom van je netwerk beheren en aanpassen en de beveiliging verbeteren.

    * Port Forwarding: stuur specifiek internetverkeer door naar aangewezen apparaten in je netwerk om toegang te geven tot diensten zoals game- of webservers.
    * Open Ports: bewaak en bepaal welke poorten op je router openstaan om onbevoegde toegang en mogelijke beveiligingsrisico's te voorkomen.
    * DMZ (Demilitarized Zone): maak één apparaat vanaf internet bereikbaar door al het inkomende verkeer ernaartoe door te sturen.

    Raadpleeg [Firewall](../../interface_guide/firewall.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Multi-WAN"

    Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Ethernet en Repeater. Als de huidige internetverbinding uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit zorgt voor soepele en ononderbroken internettoegang.

    Raadpleeg [Multi-WAN](../../interface_guide/multi-wan.md) om Multi-WAN in te stellen.

=== "LAN"

    Op de pagina LAN kun je de instellingen van het lokale netwerk van je router beheren en configureren. De belangrijkste functies op deze pagina zijn:

    * Router IP Address: wijzig het IP-adres van je router zodat het beter bij je netwerkconfiguratie past.
    * Netmask: stel het subnetmasker voor je netwerk in. Dit bepaalt de omvang van het netwerk en het bereik van IP-adressen.
    * DHCP: schakel het Dynamic Host Configuration Protocol in of configureer het. Dit protocol wijst automatisch IP-adressen toe aan apparaten in je netwerk.
    * Address Reservation: reserveer specifieke IP-adressen voor bepaalde apparaten, zodat deze altijd hetzelfde IP-adres van de DHCP-server krijgen.

    Raadpleeg [LAN](../../interface_guide/lan.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Guest Network"

    Op de pagina Guest Network kun je een afzonderlijk netwerk voor gasten maken en beheren. Zij krijgen internettoegang terwijl je hoofdnetwerk beveiligd blijft. De belangrijkste functies op deze pagina zijn:

    * Gateway: stel het IP-adres van de gateway voor het gastnetwerk in.
    * DHCP: configureer het Dynamic Host Configuration Protocol voor het gastnetwerk om automatisch IP-adressen toe te wijzen aan apparaten die verbinding maken.

    Het gastnetwerk biedt gasten internettoegang en isoleert hun verkeer van je hoofdnetwerk om mogelijke gevolgen voor de beveiliging en prestaties daarvan te beperken.
    
    Raadpleeg [Guest Network](../../interface_guide/guest_network.md) voor uitgebreide installatie-instructies en meer informatie.

---

=== "DNS"

    De pagina DNS biedt opties om de Domain Name System-instellingen van je router aan te passen en zo de beveiliging en prestaties te verbeteren. De belangrijkste functies op deze pagina zijn:

    * Encrypted DNS: configureer versleutelde DNS om je browsegegevens tegen controle of manipulatie te beschermen en zo privacy en beveiliging te bieden.
    * Manual DNS: stel handmatig de gewenste DNS-servers in voor aangepaste controle over DNS-query's en mogelijk snellere omzetting.
    * DNS Proxy: schakel de DNS-proxy in om DNS-verzoeken van je apparaten via een opgegeven DNS-server te routeren. Dit biedt extra controle over DNS-verkeer.

    Met deze instellingen kun je de DNS-prestaties en beveiliging van je netwerk op je specifieke behoeften afstemmen.

    Raadpleeg [DNS](../../interface_guide/dns.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Network Mode"

    Op de pagina Network Mode kun je de router voor verschillende modi configureren, zodat je flexibel aan uiteenlopende netwerkbehoeften kunt voldoen. De beschikbare modi zijn:

    * Router: werkt als standaardrouter, beheert verkeer tussen je lokale netwerk en internet en biedt functies zoals NAT, firewall en DHCP.
    * Access Point: werkt als access point en breidt je bestaande bekabelde netwerk uit met draadloze connectiviteit zonder verkeer te routeren.
    * Extender: werkt als bereikvergroter, versterkt het signaal van je bestaande draadloze netwerk voor een groter bereik en voorkomt zones zonder dekking.
    * WDS (Wireless Distribution System): vergelijkbaar met Extender. Selecteer WDS als je hoofdrouter de WDS-modus ondersteunt.

    Raadpleeg [Network Mode](../../interface_guide/network_mode.md) voor uitgebreide installatie-instructies en meer informatie.

=== "IPv6"

    Op de pagina IPv6 kun je IPv6-instellingen voor je netwerk configureren en ondersteuning voor het nieuwste internetprotocol inschakelen. Je kunt IPv6 inschakelen en een van vier modi selecteren die bij je netwerkbehoeften past:

    * Native: ontvang rechtstreeks van je internetprovider een IPv6-adres voor eenvoudige en efficiënte native IPv6-connectiviteit.
    * Passthrough: laat IPv6-verkeer via de router door naar de apparaten in je netwerk. De verbinding wordt overbrugd zonder dat de router zelf de IPv6-routering afhandelt.
    * NAT6: gebruik Network Address Translation for IPv6 (NAT6) om interne en externe IPv6-adressen te vertalen, vergelijkbaar met de werking van NAT voor IPv4.
    * Static IPv6: configureer handmatig een statisch IPv6-adres voor je router voor een vast adres, consistente connectiviteit en eenvoudiger beheer van netwerkdiensten.

    Deze modi bieden flexibele IPv6-configuratieopties voor verschillende netwerkomgevingen.

    Raadpleeg [IPv6](../../interface_guide/ipv6.md) voor uitgebreide installatie-instructies en meer informatie.

=== "MAC Address"

    Op de pagina MAC Address kun je de Media Access Control-adressen (MAC-adressen) van je router bekijken en beheren. De belangrijkste functies op deze pagina zijn:

    * Factory Default: toon de standaard-MAC-adressen voor de modi Ethernet en Repeater van de router als referentie voor de oorspronkelijke hardware-instellingen.
    * Clone: kloon het MAC-adres van een specifiek clientapparaat. Dit is vooral nuttig wanneer netwerktoegang tot bepaalde apparaten is beperkt.
    * Manual: geef handmatig een aangepast MAC-adres voor je router op. Je kunt ook de knop Random gebruiken om een willekeurig MAC-adres te genereren, voor meer flexibiliteit en privacy.

    Met deze functies kun je de MAC-adressen van je router effectief beheren en compatibiliteit en flexibiliteit in verschillende netwerkomgevingen waarborgen.

    Raadpleeg [MAC Address](../../interface_guide/mac_address.md) voor uitgebreide installatie-instructies en meer informatie.

---

=== "Drop-in Gateway"

    Drop-in Gateway breidt de functies van je hoofdrouter uit met functies die deze mogelijk niet heeft, waaronder AdGuard Home, versleutelde DNS en VPN. Raadpleeg [Een Drop-in Gateway instellen](../../tutorials/how_to_set_up_drop_in_gateway.md) om Drop-in Gateway in te stellen.

=== "IGMP Snooping"

    Op de pagina IGMP Snooping kun je instellingen configureren die het beheer van multicastverkeer in je netwerk optimaliseren. IGMP Snooping luistert naar IGMP-protocolpakketten, haalt er informatie uit en maakt en onderhoudt Layer 2-doorstuurtabellen voor multicast. Hierdoor worden gegevens van een multicastgroep alleen doorgestuurd naar hosts die zich bij de groep hebben aangesloten en bereikt ongewenst multicastverkeer geen andere hosts.

    Deze instellingen helpen de netwerkprestaties en efficiëntie te optimaliseren, vooral in omgevingen met veel multicastverkeer, zoals videostreaming of online gaming.

    Raadpleeg [IGMP Snooping](../../interface_guide/igmp_snooping.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Network Acceleration"

    Op de pagina Network Acceleration kun je functies inschakelen die de CPU-belasting verlagen en het doorsturen van verkeerspakketten versnellen, waardoor de algemene netwerkprestaties verbeteren. Netwerkversnelling kan echter met bepaalde functies conflicteren.

    Raadpleeg [Network Acceleration](../../interface_guide/network_acceleration.md) voor uitgebreide installatie-instructies en meer informatie.

=== "NAT Settings"

    Op de pagina NAT Settings kun je opties voor Network Address Translation (NAT) configureren om specifieke toepassingen te optimaliseren en de netwerkprestaties te verbeteren. De belangrijkste instellingen op deze pagina zijn:

    * Enable Full Cone NAT: Full Cone NAT kan de latentie van games verlagen door netwerkverkeer een directer en minder beperkt pad te bieden. Het inschakelen van Full Cone NAT kan echter minder veilig zijn, omdat externe hosts dan eenvoudiger verbindingen met interne apparaten kunnen starten.
    * Enable SIP ALG: de Session Initiation Protocol Application Layer Gateway (SIP ALG) kan problemen door meerdere NAT-lagen beperken die VoIP-diensten kunnen beïnvloeden. In de meeste gevallen biedt SIP ALG echter geen voordeel en kan het problemen veroorzaken, zoals eenzijdig geluid, telefoons die bij een oproep niet overgaan, verbroken verbindingen en oproepen die rechtstreeks naar de voicemail gaan.

    Met deze instellingen kun je het NAT-gedrag van je router afstemmen op de behoeften van je netwerk en verbeterde prestaties afwegen tegen mogelijke gevolgen voor beveiliging en functionaliteit.

    Raadpleeg [NAT Settings](../../interface_guide/nat_settings.md) voor uitgebreide installatie-instructies en meer informatie.

## Systeem {#system}

=== "Overview"

    De pagina Overview biedt een uitgebreid overzicht van de huidige status en prestatiegegevens van je router. Op deze pagina kun je het volgende bekijken:

    * CPU Average Load: bewaak de gemiddelde belasting van de CPU van je router om de prestaties te beoordelen en mogelijke knelpunten op te sporen.
    * Memory Usage: controleer hoeveel geheugen van je router in gebruik is om het beheer van bronnen te ondersteunen.
    * Flash Usage: bekijk het gebruik van de flashopslag van de router en controleer of er voldoende ruimte is voor firmware en configuratiegegevens.
    * System Info: bekijk uitgebreide informatie over het systeem van je router, waaronder firmwareversie, uptime en netwerkstatus.
    * LED Control: schakel de leds van de router in of uit om de visuele indicatoren van het apparaat aan te passen.

    Deze functies bieden essentiële informatie en bedieningselementen om de werking van je router effectief te beheren en bewaken.

    Raadpleeg [Overview](../../interface_guide/system_overview.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Upgrade"

    De pagina Upgrade wordt gebruikt om de firmware van je router bij te werken naar de nieuwste versie, voor betere prestaties en beveiliging en nieuwe functies. Deze pagina biedt twee opties voor upgrades:

    * Online Upgrade: controleer automatisch op de server van de fabrikant of de nieuwste firmwareversie beschikbaar is. Als deze online beschikbaar is, kun je de nieuwste versie installeren.
    * Local Upgrade: upload handmatig een firmwarebestand vanaf je computer om de router bij te werken. Zo bepaal je zelf de versie en het moment van de upgrade.

    Met deze opties houd je je router bijgewerkt met de nieuwste verbeteringen en correcties.

    Raadpleeg [Upgrade](../../interface_guide/upgrade.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Scheduled Tasks"

    Op de pagina Scheduled Tasks kun je verschillende routerfuncties volgens een vooraf ingesteld schema automatiseren. Dit verhoogt het gemak en de efficiëntie. De belangrijkste functies op deze pagina zijn:

    * LED Display Schedule: stel een schema in om de leds van de router automatisch in of uit te schakelen en zo lichtvervuiling op bepaalde tijden te beperken.
    * Schedule Reboot: configureer de router om met ingestelde intervallen automatisch opnieuw op te starten. Dit helpt optimale prestaties en stabiliteit te behouden.
    * 5GHz Wi-Fi Status Schedule: maak een schema om de 5GHz-Wi-Fi-band op bepaalde tijden in of uit te schakelen en zo het netwerkgebruik en de energie-efficiëntie te optimaliseren.
    * 2.4GHz Wi-Fi Status Schedule: stel een schema in om de 2.4GHz-Wi-Fi-band te beheren en zo de beschikbaarheid van het netwerk en het energieverbruik beter te regelen.
    
    Met deze planningsopties heb je meer controle over de werking van je router en kun je deze afstemmen op je specifieke behoeften en voorkeuren.

    Raadpleeg [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Time Zone"

    Op de pagina Time Zone kun je de juiste tijdzone voor je router instellen. Hierdoor krijgen alle geplande taken, logboeken en systeemgebeurtenissen een nauwkeurig tijdstempel op basis van je lokale tijd. Deze instelling is essentieel voor nauwkeurige registraties en een correcte uitvoering van tijdgebonden configuraties.

    Raadpleeg [Time Zone](../../interface_guide/time_zone.md) voor uitgebreide installatie-instructies en meer informatie.

---

=== "Log"

    De pagina Log biedt toegang tot verschillende logboeken waarin activiteiten en gebeurtenissen van de router worden vastgelegd. Deze helpen bij probleemoplossing en prestatiebewaking. De pagina bevat:

    * System Log: uitgebreide logboeken van gebeurtenissen en activiteiten op systeemniveau.
    * Kernel Log: logboeken van activiteiten en gebeurtenissen van de kernel.
    * Crash Log: registraties van systeemcrashes en fouten die nuttig zijn bij de diagnose van kritieke problemen.
    * Cloud Log: logboeken van interacties en activiteiten met betrekking tot de GoodCloud-diensten die in de router zijn geïntegreerd.
    * Nginx Log: logboeken van de Nginx-webserver, als deze door de router wordt gebruikt, met gegevens over webverkeer en serveractiviteiten.

    Daarnaast bevat de pagina de knop Export Log, waarmee je alle verzamelde logboeken kunt exporteren voor analyse door technische ondersteuning. Deze functie is zeer waardevol voor het vaststellen van complexe problemen en het verkrijgen van professionele hulp.

    Raadpleeg [Log](../../interface_guide/log.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Security"

    Op de pagina Security kun je verschillende beveiligingsinstellingen configureren om je netwerk en router tegen onbevoegde toegang te beschermen. De pagina bevat opties voor:

    * Admin Password: stel het wachtwoord voor de beheerinterface van de router in of wijzig het, zodat alleen bevoegde gebruikers instellingen kunnen wijzigen.
    * Local Access Control: beheer en beperk de toegang tot de routerinterface vanaf apparaten die met je lokale netwerk zijn verbonden.
    * Remote Access Control: configureer en beperk toegang tot de routerinterface vanaf externe locaties via internet om de beveiliging tegen bedreigingen van buitenaf te verbeteren.

    Met deze instellingen onderhoud je een veilige netwerkomgeving en bescherm je zowel de router als de verbonden apparaten.

    Raadpleeg [Security](../../interface_guide/security.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Reset Firmware"

    Op de pagina Reset Firmware kun je de huidige firmwareversie van je router terugzetten naar de standaardinstellingen. Alle aangepaste configuraties worden daarbij gewist. Dit proces herstelt de standaardinstellingen van de firmwareversie die momenteel is geïnstalleerd. Dit kan nuttig zijn om aanhoudende problemen op te lossen of opnieuw te beginnen met de standaardconfiguratie van de huidige firmware.

    Raadpleeg [Reset Firmware](../../interface_guide/reset_firmware.md) voor uitgebreide installatie-instructies en meer informatie.

=== "Advanced Settings"

    De pagina Advanced Settings biedt via de OpenWrt LuCI-interface toegang tot geavanceerde configuratieopties. Ervaren gebruikers kunnen hiermee de instellingen en functies van hun router nauwkeurig aanpassen buiten de mogelijkheden van de basisinterface. Dit omvat uitgebreide netwerkconfiguraties, firewallinstellingen en andere geavanceerde systeemaanpassingen.

    Raadpleeg [Advanced Settings](../../interface_guide/advanced_settings.md) voor uitgebreide installatie-instructies en meer informatie.
