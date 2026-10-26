# Gebruikershandleiding GL-S200 {#gl-s200-user-guide}

## Productoverzicht {#product-overview}

GL-S200 is een compacte Thread-gateway met ondersteuning voor het BLE-protocol. De gateway gebruikt het sterk aanpasbare OpenWrt-besturingssysteem en ondersteunt apparaatbeheer via de cloud. Het veelzijdige ontwerp maakt verbinding met verschillende smarthome-apparaten of grote aantallen apparaten in slimme gebouwen mogelijk.

![gl-s200 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_interface.jpg){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

Houd er rekening mee dat de meegeleverde adapter afhankelijk is van het land van levering.

De verpakking bevat:

- 1 x Gebruikershandleiding
- 1 x GL-S200
- 1 x Ethernet-kabel
- 1 x Bedankkaart
- 1 x Garantiekaart
- 1 x Voedingsadapter (geselecteerd stekkertype)

![gl-s200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/first_time_setup/s200_unboxing.jpg){class="glboxshadow"}

Bekijk de [uitpakvideo](../../video_library/unboxing_first_set_up.md#gl-s200) van GL-S200.

## Specificaties {#specifications}

[Specificaties van GL-S200](https://www.gl-inet.com/products/gl-s200/#specs){target="_blank"}

## PCB-pintoewijzing {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="contentUrl" data-size="1500x1235">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="thumbnail" alt="gl-s200 pinout" loading="lazy" />
    </a>
  </figure>
</div>

## Pintoewijzing van GL Thread Dev Board {#gl-thread-dev-board-pinout}

![gl thread dev board pinout](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl_thread_dev_board_pinout.jpg){class="glboxshadow"}

---

## Eerste installatie {#first-time-setup}

Alle GL.iNet-routers hebben een vergelijkbaar installatieproces. [Klik hier voor informatie over de eerste installatie](../../faq/first_time_setup.md).

---

## INTERNET {#internet}

Meld je aan bij het webbeheerpaneel van de router en ga via het linkermenu naar **INTERNET**.

Op deze pagina kun je afhankelijk van je model het type internetverbinding selecteren, zoals Ethernet, Repeater, Tethering of Cellular.

GL-S200 ondersteunt twee typen verbindingen: Ethernet en Repeater.

### Ethernet {#ethernet}

Sluit je router met een Ethernet-kabel aan op een actieve modem of een actief netwerkapparaat om internettoegang te krijgen. Deze methode biedt doorgaans de snelste en betrouwbaarste internetverbinding.

[Klik hier om te lezen hoe je via een Ethernet-kabel verbinding maakt met internet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Stel je router in als repeater om het bereik van een bestaand Wi-Fi-netwerk te vergroten. Als repeater ontvangt en verzendt de router draadloze signalen opnieuw binnen zijn bereik. Deze methode is nuttig wanneer één router niet het volledige gebruiksgebied kan dekken.

[Klik hier om te lezen hoe je via een bestaand Wi-Fi-netwerk verbinding maakt met internet](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_repeater.png){class="glboxshadow"}

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

## Thread Mesh {#thread-mesh}

Raadpleeg [Thread Mesh](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/thread_mesh/) in de IoT-documentatie.

---

## GL Dev Board {#gl-dev-board}

Raadpleeg [GL Dev Board](https://docs.gl-inet.com/iot/en/iot_dev_board/) in de IoT-documentatie.

---

## Bluetooth {#bluetooth}

Raadpleeg [Bluetooth](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/bluetooth/) in de IoT-documentatie.

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

### IPv6 {#ipv6}

Raadpleeg de tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

De pagina Mac Address heette voorheen Mac Clone en is sinds v4.2 gewijzigd in Mac Address.

Raadpleeg de tutorial [**MAC Address**](../../interface_guide/mac_address.md).

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
