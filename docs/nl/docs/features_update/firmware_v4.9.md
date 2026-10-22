# Firmware v4.9 {#firmware-v49}

Deze release is gericht op nauwkeurigere netwerkregeling, beter verkeersbeheer, betere netwerkbeveiliging en een vernieuwde gebruikersinterface. Dit alles zorgt voor een betere algehele gebruikerservaring.

Download de nieuwste firmware via het [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control {#flow-control}

Flow Control is een kernmodule voor netwerkbeheer waarmee netwerkverkeer nauwkeurig kan worden geïdentificeerd, bewaakt, gereguleerd en gefilterd. De module optimaliseert de toewijzing van netwerkbronnen, voorkomt bandbreedtecongestie en standaardiseert de toegang tot het netwerk, wat zorgt voor een soepelere, veiligere en beter beheersbare netwerkervaring. In firmware v4.9 is deze module geïntegreerd met meerdere praktische functies voor uitgebreid verkeersbeheer.

De module Flow Control omvat DPI Engine, Data Statistics, Content Filter, QoS, SQM en Parental Control.

### DPI Engine {#dpi-engine}

Traditionele routers identificeren alleen bron- en bestemmingsadressen. DPI (Deep Packet Inspection) analyseert daarentegen de inhoud van pakketten grondig en identificeert toepassingen en websites nauwkeurig met behulp van een bibliotheek voor kenmerkherkenning. Hierdoor zijn fijnmazige classificatie en regeling van verkeer mogelijk.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

GL.iNet DPI is geïntegreerd met [Netify](https://www.netify.ai/){target="_blank"} en gebruikt een lichte ingebouwde plug-in voor efficiënte implementatie. Dankzij de online bijgewerkte kenmerkendatabase van Netify biedt het betrouwbaar beheer, waardoor netwerkregeling nauwkeuriger en efficiënter wordt.

### Data Statistics {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) biedt een overzichtelijk verkeersdashboard dat het netwerkgebruik per toepassing en protocol identificeert. Je kunt historische trends over 1 uur, 1 dag en 7 dagen bekijken, gebruiksranglijsten weergeven, het verkeer per apparaat bewaken en ongewenste apps met één klik blokkeren.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter {#content-filter}

[Content Filter](../interface_guide/content_filter.md) is een intelligente online beveiligingsfunctie op basis van DPI-classificatie. De functie blokkeert automatisch schadelijke en kwaadaardige websites om je netwerk schoon en veilig te houden. Ook worden aangepaste regels ondersteund om specifieke apps, domeinen of IP-adressen te blokkeren.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) optimaliseert de bandbreedtetoewijzing door tijdens netwerkcongestie prioriteit te geven aan belangrijke activiteiten, zoals videogesprekken en gaming. Hierdoor neemt de latentie af en verbeteren de algemene netwerkprestaties.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) beheert het netwerkverkeer van je router op intelligente wijze om de latentie en 'bufferbloat' te beperken. Zo verlopen games en spraakoproepen soepeler.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control {#parental-control}

[Parental Control](../interface_guide/parental_control_v4.9.md) stond voorheen in het menu **Applications**. In firmware v4.9 is de functie verplaatst naar het menu **Flow Control**, omdat deze de bijgewerkte DPI-engine gebruikt om ongeschikte toepassingen en netwerkinhoud nauwkeurig te identificeren en blokkeren. Hierdoor kan toegang professioneler en nauwkeuriger op basis van verkeer worden beperkt.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN {#vpn}

In firmware v4.9 zijn de onderliggende routeringslogica en interactieve interface van de VPN-module grondig verbeterd. Mogelijke routeringsconflicten zijn opgelost, de configuratielogica is vereenvoudigd en de bediening is intuïtiever geworden.

De aanpassingen worden hieronder beschreven.

### Geïsoleerde VPN-tunnel {#isolated-vpn-tunnel}

Elke VPN-tunnel werkt als een onafhankelijke groep zonder failover tussen groepen. Zodra netwerkverkeer met een bepaalde VPN-groep overeenkomt, schakelt het niet automatisch over naar andere VPN-groepen als de huidige tunnel uitvalt. Hierdoor blijft de verkeersroutering stabiel en voorspelbaar.

**Opmerking**: het traditionele beleid 'Not Use VPN' is in firmware v4.9 verwijderd. Daarmee vervalt overbodige configuratie en worden routeringsconflicten door meerdere, complexe tunnelregels voorkomen.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### Failover van VPN-profielen {#vpn-profile-failover}

Eén VPN-tunnelgroep kan meerdere configuratieprofielen bevatten. Je kunt de prioriteit van elk profiel binnen dezelfde groep aanpassen. Hierdoor vindt automatisch interne failover plaats als één profiel uitvalt en blijft de VPN-verbinding actief.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Vernieuwd dashboard {#redesigned-dashboard}

Het [VPN Dashboard](../interface_guide/vpn_dashboard.md) in firmware v4.9 is volledig vernieuwd en heeft een intuïtievere indeling. De tunnelstatus, verbindingsgegevens en configuratie-items worden duidelijker weergegeven, waardoor dagelijks gebruik en beheer aanzienlijk efficiënter worden. Bovendien is Kill Switch in de nieuwe architectuur standaard ingeschakeld voor alle VPN-tunnels, zodat je verkeer altijd beschermd blijft.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0 {#amneziawg-20}

Firmware v4.9 introduceert officieel het protocol AmneziaWG 2.0, met meerdere nieuwe parameters voor verkeersobfuscatie. Het bijgewerkte protocol omzeilt detectie door DPI en andere systemen voor verkeersidentificatie effectief. Dit verbetert de verhulling van de verbinding en de weerstand tegen interferentie aanzienlijk. Hierdoor kunnen stabiele en betrouwbare VPN-verbindingen tot stand worden gebracht in regio’s met netwerkbeperkingen en in complexe netwerkomgevingen.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## IoT Network {#iot-network}

Met [IoT Network](../interface_guide/iot_network.md) in firmware v4.9 kun je een onafhankelijk, speciaal Wi-Fi-netwerk voor slimme IoT-apparaten maken. Dit netwerk is fysiek en logisch van het primaire netwerk gescheiden. Zo voorkom je dat IoT-apparaten bronnen van het hoofdnetwerk gebruiken of beveiligingsrisico’s introduceren. Deze optimalisatie biedt bredere compatibiliteit met verschillende slimme IoT-clients en verbetert de algehele beveiliging van het thuisnetwerk.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL {#acl}

[ACL](../interface_guide/acl.md), een afkorting van Access Control List, is een belangrijke functie voor netwerkbeveiligingsbeheer. Je kunt aangepaste toegangsregels maken om intern en extern netwerkverkeer te beheren op basis van verbindingsprotocollen, IP-adressen van apparaten en poorten. De functie ondersteunt nauwkeurig rechtenbeheer om specifieke vormen van netwerktoegang toe te staan of te blokkeren. Als meerdere ACL-regels met elkaar conflicteren, voert het systeem automatisch de regel met de hoogste prioriteit uit om het beleid correct toe te passen.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL en Port Forwarding hebben een ander hoofddoel. ACL richt zich op netwerkbeveiligingsbeheer door de toegangsrechten van apparaten en verkeer te regelen. Port Forwarding wordt gebruikt om netwerkbronnen om te leiden: extern netwerkverkeer wordt doorgestuurd naar opgegeven lokale eindapparaten om externe toegang tot lokale netwerkdiensten mogelijk te maken.

## Wireless {#wireless}

De gebruikersinterface van [Wireless](../interface_guide/wireless.md) is volledig vernieuwd met een vereenvoudigde indeling en uniforme visuele stijl. Dit vermindert de complexiteit van de bediening en maakt de interface aanzienlijk eenvoudiger en gebruiksvriendelijker.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## Encrypted DNS {#encrypted-dns}

[Encrypted DNS](../interface_guide/dns.md#encrypted-dns) is uitgebreid met meer versleutelingsprotocollen, waaronder DoH, DoT en DoQ. Daarnaast zijn meer officiële DNS-serviceproviders geïntegreerd en is handmatige configuratie van aangepaste versleutelde DNS-servers toegevoegd om aan uiteenlopende behoeften voor veilige domeinnaamomzetting te voldoen.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node {#tailscale-exit-node}

GL.iNet-routers kunnen nu als Tailscale exit node worden gebruikt. Al het uitgaande internetverkeer van apparaten in de Tailnet kan via het openbare IP-adres van de router worden geleid. Hierdoor kan de internetuitgang van het volledige Tailscale-netwerk centraal en veilig worden beheerd. Raadpleeg [deze pagina](../interface_guide/tailscale.md#run-exit-node) voor meer informatie.

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
