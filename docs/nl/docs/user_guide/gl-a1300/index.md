# Gebruikershandleiding Slate Plus (GL-A1300) {#slate-plus-gl-a1300-user-guide}

## Productoverzicht {#product-overview}

Slate Plus (GL-A1300) is een compacte reisrouter met een krachtige CPU die is geoptimaliseerd voor netwerkstabiliteit en efficiënte verwerking van VPN-versleuteling. De router bevat onze nieuwste beveiligingsfuncties en gebruikt het nieuwste OpenWrt-besturingssysteem. Hij is ontworpen voor frequente reizigers die VPN-netwerken intensief gebruiken.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

Houd er rekening mee dat de meegeleverde adapter afhankelijk is van het land van levering.

De verpakking bevat:

- 1 x Gebruikershandleiding
- 1 x Slate Plus (GL-A1300)
- 1 x Ethernet-kabel
- 1 x Garantiekaart
- 1 x Voedingsadapter (geselecteerd stekkertype)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Ledindicatie {#led-indication}

[Ledindicatie](../../faq/led.md#gl-a1300)

## Specificaties {#specifications}

[Specificaties van GL-A1300](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

## Eerste installatie {#first-time-setup}

Alle GL.iNet-routers hebben een eenvoudig en vrijwel identiek installatieproces. [Klik hier voor informatie over de eerste installatie](../../faq/first_time_setup.md).

Gebruik een van de vier ondersteunde methoden voor internetverbindingen om Slate Plus in te stellen: Ethernet, Repeater, Tethering of Cellular. Bekijk deze installatievideo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## INTERNET {#internet}

In de interface voor internetconfiguratie kun je het type internetverbinding kiezen dat de router ondersteunt.

Configureer de internetverbinding door in het zijmenu van het webbeheerpaneel van de router **INTERNET** te selecteren.

De router ondersteunt de volgende vier methoden om verbinding met internet te maken:

### Ethernet {#ethernet}

Sluit de router met een Ethernet-kabel aan op een actieve modem of een actief netwerkapparaat om gegevens via Ethernet te verzenden. Deze methode biedt doorgaans de snelste en betrouwbaarste internetverbinding.

[Klik hier om te lezen hoe je via een Ethernet-kabel verbinding maakt met internet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Vergroot het bereik van een bestaand Wi-Fi-netwerk door de router draadloze signalen binnen zijn bereik te laten ontvangen en over een grotere afstand door te sturen. Deze methode is vooral nuttig wanneer één router onvoldoende bereik heeft voor het volledige gebruiksgebied.

[Klik hier om te lezen hoe je via een bestaand Wi-Fi-netwerk verbinding maakt met internet](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Bied verbonden apparaten internettoegang door de mobiele data van een smartphone via een kabel met de router te delen. Deze methode is vooral nuttig wanneer je de mobiele data van de telefoon wilt gebruiken voor internettoegang.

[Klik hier om te lezen hoe je via USB-tethering verbinding maakt met internet](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Sluit een USB-modem voor mobiele netwerken aan op de USB-poort van de router om de router met internet te verbinden. Deze methode is vooral nuttig om de internetverbinding van een USB-modem met alle verbonden apparaten te delen.

[Klik hier om te lezen hoe je via een USB-modem verbinding maakt met internet](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### Prioriteit en load balancing {#priority-and-load-balance}

Ga naar [Multi-WAN](../../interface_guide/multi-wan.md) om de prioriteit van elke methode voor internettoegang of de load balancing in te stellen wanneer meerdere methoden tegelijk worden gebruikt.

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

### AdGuard Home {#adguard-home}

Raadpleeg de tutorial [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Parental Control {#parental-control}

Raadpleeg de tutorial [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier {#zerotier}

Raadpleeg de tutorial [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale {#tailscale}

Raadpleeg de tutorial [**Tailscale**](../../interface_guide/tailscale.md).

---

## NETWORK {#network}

### Firewall {#firewall}

GL.iNet-routers bevatten meerdere firewallfuncties voor een beveiligde verbinding en volledig beheer. Je kunt firewallregels configureren, waaronder Port Forwarding, Open Ports en DMZ.

[Klik hier voor meer informatie over GL.iNet routers' firewall](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan}

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
