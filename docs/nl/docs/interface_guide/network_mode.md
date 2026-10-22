# Network Mode {#network-mode}

Ga links in het webbeheerpaneel naar **NETWORK** -> **Network Mode**.

Network Mode bepaalt de rollen en functies van een router voor verschillende implementaties, van Wi-Fi-dekking thuis tot multi-link netwerken voor bedrijven. Elke modus schakelt specifieke functies in of uit om prestaties te optimaliseren.

!!! note

    1. Na wijziging van de netwerkmodus moet je mogelijk alle clientapparaten opnieuw verbinden.

    2. **In Access Point-, WDS- of Bridge-modus kun je het webbeheerpaneel niet via het oorspronkelijke LAN-IP-adres openen.** Meld je aan bij de upstream router, zoek het toegewezen IP-adres en gebruik dit voor het webbeheerpaneel. Houd zonder toegang tot de upstream router de resetknop 4 seconden ingedrukt om naar de standaard Router-modus terug te keren.

    3. **In een niet-routermodus zijn de volgende functies niet beschikbaar**: Access Control (Allowlist en Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration en NAT Settings.

## Modellen met Wi-Fi {#for-models-with-wi-fi}

De meeste draadloze GL.iNet-routers hebben Wi-Fi, met uitzondering van enkele modellen.

Modellen met Wi-Fi ondersteunen gewoonlijk Router, Access Point, Extender en WDS. Sommige modellen ondersteunen WDS niet.

![network mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: de standaardmodus voor de meeste thuis- en kleine kantoorrouters. Deze maakt een privé-LAN en werkt als gateway tussen internet en verbonden apparaten.

    In Router Mode zijn NAT, DHCP en een ingebouwde firewall actief. Het apparaat verbindt met een upstream lijn, wijst automatisch privé-IP-adressen toe en beveiligt het privénetwerk.

    ---

- **Access Point**: verbindt de router via een LAN-kabel met een bekabeld netwerk en zendt een draadloos signaal uit om Wi-Fi-dekking te vergroten.

    In Access Point-modus zijn NAT en DHCP uitgeschakeld. De router werkt als draadloze zender en switch, niet als zelfstandige gateway.

    Na overschakeling naar Access Point kun je het webbeheerpaneel niet via het oorspronkelijke LAN-IP-adres openen. Zoek via de upstream router het toegewezen IP-adres. Houd zonder toegang tot de upstream router de resetknop 4 seconden ingedrukt om naar Router terug te keren.

    Raadpleeg [Mesh versus Extender versus Access Point](mesh.md#mesh-vs-extender-vs-access-point-mode) voor een vergelijking van connectiviteit, prestaties en beheer.

    !!! tip

        Bij meerdere access points beïnvloeden plaatsing, kanaalselectie, overlappende dekking en zendvermogen roaming en prestaties. Raadpleeg [Wi-Fi-dekking, access points en zendvermogen begrijpen](../tutorials/understanding_wifi_coverage_access_points_and_transmit_power.md).

    ---

- **Extender**: vergroot de Wi-Fi-dekking van een bestaand netwerk en voorkomt zones zonder signaal.

    In Extender-modus verbindt het apparaat met een bestaand Wi-Fi-netwerk en stuurt het verkeer door zonder Ethernet-verbinding met de hoofdrouter. Als upstream verbinding en clients dezelfde radio en hetzelfde kanaal delen, kost ontvangst en hertransmissie extra airtime en kan de doorvoer dalen.

    Raadpleeg [Mesh versus Extender versus Access Point](mesh.md#mesh-vs-extender-vs-access-point-mode) voor een vergelijking van connectiviteit, prestaties en beheer.

    In Extender-modus blijft het webbeheerpaneel via het oorspronkelijke LAN-IP-adres toegankelijk.

    ---

- **WDS**: Wireless Distribution System vergroot net als Extender draadloos de dekking, maar ondersteunt bridging tussen meerdere compatibele routers. Gebruik dit als de upstream router WDS ondersteunt.

    Deze modus is geschikt voor gebouwen met meerdere verdiepingen of kleine kantoorterreinen waar meerdere routers één draadloos netwerk vormen. Anders dan Extender kunnen gekoppelde WDS-routers signalen verzenden en ontvangen voor naadloze dekking met meerdere knooppunten.

    Na overschakeling naar WDS kun je het webbeheerpaneel niet via het oorspronkelijke LAN-IP-adres openen. Zoek via de upstream router het toegewezen IP-adres. Houd zonder toegang tot de upstream router de resetknop 4 seconden ingedrukt om naar Router terug te keren.

## Modellen zonder Wi-Fi {#for-models-without-wi-fi}

Modellen zonder Wi-Fi, zoals GL-MT5000, GL-MT2500 en GL-MT2500A, ondersteunen Access Point, Extender en WDS niet, maar wel Router en Bridge.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: de standaardmodus voor de meeste thuis- en kleine kantoorrouters. Deze maakt een privé-LAN en werkt als gateway tussen internet en verbonden apparaten.

    In Router Mode zijn NAT, DHCP en een ingebouwde firewall actief. Het apparaat verbindt met een upstream lijn, wijst automatisch privé-IP-adressen toe en beveiligt het privénetwerk.

    ---

- **Bridge**: verbindt de router met een bekabeld netwerk en laat deze als bridge tussen netwerkapparaten werken.

    In deze modus werkt de router als switch en stuurt gegevens tussen apparaten door zonder NAT, firewall of DHCP. Apparaten in hetzelfde netwerk communiceren via de router als eenvoudig verbindingspunt.

    Na overschakeling naar Bridge kun je het webbeheerpaneel niet via het oorspronkelijke LAN-IP-adres openen. Zoek via de upstream router het toegewezen IP-adres. Houd zonder toegang tot de upstream router de resetknop 4 seconden ingedrukt om naar Router terug te keren.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
