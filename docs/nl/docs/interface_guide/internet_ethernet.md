# Via een Ethernet-kabel verbinding maken met internet {#connect-to-the-internet-via-an-ethernet-cable}

Verbind de router met een breedbandnetwerk via een Ethernet-kabel die op de WAN-poort is aangesloten. De router ontvangt meestal automatisch een IP-adres via DHCP. Je kunt ook handmatig een statisch IP-adres of PPPoE configureren. Deze methode biedt hoge stabiliteit en snelheid en is ideaal voor thuis- en kantooromgevingen met een vaste breedbandaansluiting.

Volg de onderstaande stappen om je router via een Ethernet-kabel met internet te verbinden.

1. Sluit de WAN-poort van je router met een Ethernet-kabel aan op het upstream apparaat, zoals een internetmodem, router, netwerkswitch of Ethernet-aansluiting.

2. Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> het gedeelte **Ethernet**.

    Als de verbinding tot stand is gebracht, toont het gedeelte Ethernet netwerkgegevens, waaronder Protocol, IP Address, Gateway en DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Tip**: je kunt de WAN-poort zo nodig als LAN-poort instellen. Dit is nuttig wanneer je de router als [repeater](internet_repeater.md) gebruikt, omdat de fysieke WAN-poort dan niet wordt gebruikt. Door WAN naar LAN om te schakelen, krijg je een extra LAN-poort.

## Protocol {#protocol}

Er zijn drie protocollen: DHCP, Static en PPPoE. Klik op **Modify** om dit te wijzigen.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP is het standaard en meest gebruikte protocol. Het wijst via een client-serverarchitectuur automatisch IP-adressen en andere communicatieparameters aan netwerkapparaten toe.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static is nodig wanneer je internetprovider een vast IP-adres verstrekt of wanneer je netwerkgegevens, zoals IP Address, Gateway en Netmask, handmatig wilt configureren.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE is een protocol dat door veel internetproviders wordt gebruikt. Gewoonlijk verstrekken zij een modem en een gebruikersnaam en wachtwoord voor de internetconfiguratie.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Advanced {#advanced}

Naast de essentiële instellingen zijn er optionele geavanceerde instellingen voor de drie bovenstaande protocollen.

* **VLAN ID**: deze instelling is alleen vereist als de server van de provider een specifieke getagde VLAN ID voor de interface vereist.

* **TTL**: TTL (Time To Live) bepaalt hoe lang pakketten maximaal in het netwerk kunnen blijven. De router verlaagt standaard de TTL van inkomende pakketten van clientapparaten met 1 voordat hij ze doorstuurt. De TTL-instelling geldt alleen voor IPv4.

    **Opmerking**: stel hier een vaste waarde in als je de TTL wilt overschrijven of spoofen. Voer voor de meeste modellen de gewenste effectieve TTL plus 1 in om de automatische verlaging te compenseren. Mudi 7 (GL‑E5800) past de ingevoerde waarde ongewijzigd toe.

* **HL**: bij IPv6 beperkt het veld HL (Hop Limit) het aantal overdrachtshops van gegevenspakketten in het netwerk en werkt het als equivalent van TTL bij IPv4.

* **MTU**: de standaard-MTU is 1500 bytes.

## Ethernet Port {#ethernet-port}

Klik rechtsboven op het tandwielpictogram. De pagina [Ethernet Port](ethernet_port.md) wordt geopend, waar je de Ethernet-poorten van de router kunt beheren.

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

De pagina **WAN** toont de poortrol, WAN of LAN, MAC Mode, MAC Address en de onderhandelde snelheid van de netwerkpoort.

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

De pagina **LAN** toont de poortrol en de onderhandelde snelheid van de netwerkpoort.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/lan.png){class="glboxshadow"}

Raadpleeg [Ethernet Port](ethernet_port.md) voor meer informatie.

## Probleemoplossing {#troubleshooting}

Als een Ethernet-kabel op de WAN-poort is aangesloten maar internet niet beschikbaar is, verschijnt de onderstaande gele melding.

**"De interface is verbonden, maar internet is niet toegankelijk."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Voer de volgende stappen uit om dit probleem te verhelpen:

1. Controleer of het upstream apparaat internettoegang heeft.

2. Ga naar de pagina [Multi-WAN](multi-wan.md) om de status van de Ethernet-interface te controleren.

---

Gerelateerde artikelen

- [Internetpagina](internet.md)
- [Hoe stel je de prioriteit van elke methode voor internettoegang in?](multi-wan.md)
- [Hoe stel je load balancing in wanneer meerdere methoden voor internettoegang tegelijk worden gebruikt?](multi-wan.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
