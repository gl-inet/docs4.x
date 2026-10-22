# Gebruikershandleiding Slate (GL-AR750S) {#slate-gl-ar750s-user-guide}

## Productoverzicht {#product-overview}

Slate (GL-AR750S) is onze eerste dual-band Gigabit AC-reisrouter. De 3 x Gigabit Ethernet-poorten bieden onderweg hogere snelheden. De dubbele flash met 128MB biedt meer opslag en een hogere werksnelheid. De MicroSD (TF)-sleuf vergroot de opslagruimte tot 128GB.

![gl-ar750sinterface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/hardware_info/ar750s_interface.jpg){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

Houd er rekening mee dat de meegeleverde adapter afhankelijk is van het land van levering.

De verpakking bevat:

- 1 x Gebruikershandleiding
- 1 x Slate (GL-AR750S)
- 1 x Ethernet-kabel
- 1 x Bedankkaart
- 1 x Garantiekaart
- 1 x Voedingsadapter (geselecteerd stekkertype)

![gl-ar750s unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/first_time_setup/ar750s_unboxing.jpg){class="glboxshadow"}

## Specificaties {#specifications}

[Specificaties van GL-AR750S](https://www.gl-inet.com/products/gl-ar750s/#specs){target="_blank"}

## Eerste installatie {#first-time-setup}

Alle GL.iNet-routers hebben een vergelijkbaar installatieproces. [Klik hier voor informatie over de eerste installatie](../../faq/first_time_setup.md).

## INTERNET {#internet}

Meld je aan bij het webbeheerpaneel van de router en ga via het linkermenu naar **INTERNET**.

Op deze pagina kun je het type internetverbinding selecteren, zoals Ethernet, Repeater, Tethering of Cellular.

### Ethernet {#ethernet}

Sluit je router met een Ethernet-kabel aan op een actieve modem of een actief netwerkapparaat om internettoegang te krijgen. Deze methode biedt doorgaans de snelste en betrouwbaarste internetverbinding.

[Klik hier om te lezen hoe je via een Ethernet-kabel verbinding maakt met internet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Stel je router in als repeater om het bereik van een bestaand Wi-Fi-netwerk te vergroten. Als repeater ontvangt en verzendt de router draadloze signalen opnieuw binnen zijn bereik. Deze methode is nuttig wanneer één router niet het volledige gebruiksgebied kan dekken.

[Klik hier om te lezen hoe je via een bestaand Wi-Fi-netwerk verbinding maakt met internet](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Sluit de USB-poort van de router met een USB-kabel aan op een smartphone met actieve mobiele data om internettoegang te krijgen. Met deze methode kunnen meerdere apparaten die met de router zijn verbonden de mobiele data van de smartphone gebruiken.

[Klik hier om te lezen hoe je via USB-tethering verbinding maakt met internet](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Sluit een USB-modem voor mobiele netwerken aan op de USB-poort van de router om de router met internet te verbinden. Hiermee kun je de internetverbinding van de USB-modem delen met alle verbonden apparaten.

[Klik hier om te lezen hoe je via een USB-modem verbinding maakt met internet](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN is een netwerkfunctie waarmee je op je router meerdere internetverbindingen tegelijk kunt instellen, zoals Ethernet en Repeater. Als de internetverbinding met de hoogste prioriteit uitvalt, schakelt de router automatisch over naar een andere internetverbinding. Dit wordt ook Failover genoemd en zorgt voor soepele en ononderbroken internettoegang.

Ga naar [Multi-WAN](../../interface_guide/multi-wan.md) om de prioriteit van elke internetverbinding in te stellen.

Je kunt de Multi-WAN-modus ook wijzigen van Failover in Load Balance. Daarmee gebruik je meerdere netwerkinterfaces tegelijk om de totale bandbreedte van de router te vergroten.

---

## WIRELESS {#wireless}

Met de instellingen voor het draadloze netwerk kun je de netwerkbeveiliging van de primaire Wi-Fi en Guest Wi-Fi beheren. Open deze instellingen via **WIRELESS** in het zijmenu.

[Klik hier voor meer informatie over de configuratie van het draadloze netwerk](../../interface_guide/wireless.md)

---

## CLIENTS {#clients}

Clients zijn apparaten die met de router zijn verbonden. Je kunt clients blokkeren of hun netwerksnelheid beperken. Open de interface door in het zijmenu van het beheerpaneel van de router op **CLIENTS** te klikken.

[Klik hier voor meer informatie over het beheer van clientapparaten.](../../interface_guide/clients.md)

---

## VPN {#vpn}

OpenVPN en WireGuard® zijn vooraf op GL.iNet-routers geïnstalleerd en ondersteunen meer dan 30 VPN-diensten. Wanneer de VPN-client is ingeschakeld, kan de router volgens je VPN-beleidsinstellingen verkeer versleutelen voor apparaten in het netwerk, waaronder apparaten waarop geen VPN-apps kunnen worden uitgevoerd. Onze routers kunnen ook als VPN-server werken en verkeer van clientapparaten op externe locaties via een VPN-tunnel naar de VPN-server leiden voordat het openbare internet wordt geopend.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Raadpleeg de volgende links voor een stapsgewijze installatiehandleiding:

- [**OpenVPN-client instellen**](../../interface_guide/openvpn_client.md)
- [**OpenVPN-server instellen**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Raadpleeg de volgende links voor een stapsgewijze installatiehandleiding:

- [**WireGuard-client instellen**](../../interface_guide/wireguard_client.md)
- [**WireGuard-server instellen**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS {#applications}

GL.iNet-routers bevatten veel aanvullende functies die apparaatbeheer vereenvoudigen, de internetervaring verbeteren, firmware-updates automatiseren en meer.

### Plug-ins {#plug-ins}

Raadpleeg de tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Raadpleeg de tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Raadpleeg de tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage {#network-storage}

Raadpleeg de tutorial [**Network Storage**](../../interface_guide/network_storage.md).

### Parental Control {#parental-control}

Raadpleeg de tutorial [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier {#zerotier}

Raadpleeg de tutorial [**ZeroTier**](../../interface_guide/zerotier.md).

---

## NETWORK {#network}

### Firewall {#firewall}

GL.iNet-routers bevatten meerdere firewallfuncties voor een beveiligde verbinding en volledig beheer. Je kunt firewallregels configureren, waaronder Port Forwarding, Open Ports en DMZ.

[Klik hier voor meer informatie over GL.iNet routers' firewall](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Raadpleeg de tutorial [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Raadpleeg de tutorial [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Raadpleeg de tutorial [**DNS**](../../interface_guide/dns.md).

### Network Mode {#network-mode}

Raadpleeg de tutorial [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Raadpleeg de tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

De pagina Mac Address heette voorheen Mac Clone en is sinds v4.2 gewijzigd in Mac Address.

Raadpleeg de tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Raadpleeg de tutorial [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Raadpleeg de tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Raadpleeg de tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet brengt regelmatig firmware-updates voor zijn routers uit om de prestaties te verbeteren, fouten op te lossen en kwetsbaarheden te verhelpen.

Raadpleeg de tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks {#scheduled-tasks}

Raadpleeg de tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Deze functie is sinds v4.5 verplaatst naar [**Security**](../../interface_guide/security.md).

Raadpleeg de tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Raadpleeg de tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings {#toggle-button-settings}

Raadpleeg de tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log {#log}

Raadpleeg de tutorial [**Log**](../../interface_guide/log.md).

### Security {#security}

Deze functie is beschikbaar sinds v4.5.

Raadpleeg de tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Raadpleeg de tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Raadpleeg de tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
