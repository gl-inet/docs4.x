# Gebruikershandleiding Mudi V2 (GL-E750V2) {#mudi-v2-gl-e750v2-user-guide}

**Opmerking:** Mudi V2 (GL-E750V2) en Mudi (GL-E750) gebruiken dezelfde firmware. Als je Mudi (GL-E750) gebruikt, [werk je de firmware bij](https://dl.gl-inet.com/?model=e750) om de nieuwste functies te gebruiken.

## Productoverzicht {#product-overview}

Mudi V2 (GL-E750V2) is een draagbare 4G LTE-reisrouter die compatibel is met providers wereldwijd. De volledig opensource router gebruikt OpenWrt en GL.iNet SDK 4.0 en biedt aanpassingsmogelijkheden en diverse functies. Mudi V2 (GL-E750V2) ondersteunt Wi-Fi-snelheden van 300Mbps (2.4GHz) en 433Mbps (5GHz) en een MicroSD-kaart tot 1TB. De router heeft een ingebouwde accu van 7000mAh. Multi-WAN (failover en load balance) zorgt voor een soepele verbinding voor al je apparaten.

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Knop {#button}

- Houd de aan-uitknop **3 seconden** ingedrukt om het apparaat in te schakelen.

- Houd de aan-uitknop **3-5 seconden** ingedrukt om Standby Mode te activeren.

- Houd de aan-uitknop **meer dan 5 seconden** ingedrukt om het apparaat uit te schakelen.

    (Na 3 seconden verschijnt eerst “Standby Mode On” op het OLED-scherm. HOUD de aan-uitknop INGEDRUKT totdat onder "Standby Mode On" de tekst "Shut Down" verschijnt. Het apparaat telt 3 seconden af en wordt uitgeschakeld.)

## Standby Mode {#standby-mode}

In Standby Mode schakelt Mudi V2 (GL-E750V2) Wi-Fi en 4G uit om energie te besparen. In deze modus kun je geen verbinding maken met Mudi V2 (GL-E750V2).

Houd de aan-uitknop 3 seconden ingedrukt om Standby Mode in of uit te schakelen. Op het OLED-scherm verschijnt “Standby Mode On” of “Standby Mode Off”.

## Inhoud van de verpakking {#package-contents}

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Mudi V2 (GL-E750V2) portable 4G LTE router
- 1 x Voedingsadapter
- 4 x Adapters (US-, EU-, UK- en AU-stekkers)
- 1 X Gebruikershandleiding
- 1 x Garantiekaart
- 1 x Ethernet-kabel
- 1 x USB-C-poortreplicator
- 1 x USB-C-naar-USB-C-kabel
- 1 x USB-A-naar-USB-C-kabel
- 1 x Opbergtas
- 1 x Bedankkaart

---

## Eerste installatie {#first-time-setup}

Bekijk deze video of volg de stappen om Mudi V2 in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Een simkaart plaatsen {#1-insert-a-sim-card}

Plaats een simkaart en eventueel een MicroSD-kaart in Mudi V2 (GL-E750V2).

Opmerking: als je een simkaart gebruikt, moet je deze in het apparaat plaatsen voordat je het inschakelt.

1. Draai Mudi V2 (GL-E750V2) om.
2. Steek je vinger in de opening bij de rand van het deksel.
3. Schuif langs de rand.
4. Trek het deksel omhoog om het te openen wanneer het iets omhoogkomt, tot ongeveer 25 à 30 graden.
5. Plaats de kaart in de kaartsleuf zoals aangegeven door het symbool bij de hoek.
6. Druk het deksel omlaag om het te sluiten.

### 2. Inschakelen {#2-power-on}

Druk op de aan-uitknop om het apparaat in te schakelen.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_power-on.png){class="glboxshadow"}

Wanneer Mudi V2 (GL-E750V2) is uitgeschakeld, kun je de accustatus nog steeds controleren door op de aan-uitknop te drukken. Het OLED-scherm toont dan de accustatus.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_battery.png){class="glboxshadow"}

Gebruik een standaard 5V/2A-voedingsadapter. Een andere adapter kan storingen veroorzaken.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET {#internet}

Meld je aan bij het webbeheerpaneel van de router en ga via het linkermenu naar **INTERNET**.

Op deze pagina kun je het type internetverbinding selecteren, zoals Ethernet, Repeater, Tethering of Cellular.

### Ethernet {#ethernet}

Sluit je router met een Ethernet-kabel aan op een actieve modem of een actief netwerkapparaat om internettoegang te krijgen. Deze methode biedt doorgaans de snelste en betrouwbaarste internetverbinding.

[Klik hier om te lezen hoe je via een Ethernet-kabel verbinding maakt met internet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Stel je router in als repeater om het bereik van een bestaand Wi-Fi-netwerk te vergroten. Als repeater ontvangt en verzendt de router draadloze signalen opnieuw binnen zijn bereik. Deze methode is nuttig wanneer één router niet het volledige gebruiksgebied kan dekken.

[Klik hier om te lezen hoe je via een bestaand Wi-Fi-netwerk verbinding maakt met internet](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Sluit de USB-poort van de router met een USB-kabel aan op een smartphone met actieve mobiele data om internettoegang te krijgen. Met deze methode kunnen meerdere apparaten die met de router zijn verbonden de mobiele data van de smartphone gebruiken.

[Klik hier om te lezen hoe je via USB-tethering verbinding maakt met internet](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Verwijder het achterdeksel van Mudi V2 en plaats een simkaart in de simkaartsleuf om verbinding met internet te maken. Hiermee kun je de internetverbinding van één simkaart delen met alle verbonden apparaten.

[Klik hier om te lezen hoe je via een mobiel netwerk verbinding maakt met internet](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_cellular.png){class="glboxshadow"}

Klik hier om een fysieke eSIM-kaart op je GL.iNet-router te gebruiken: [Een fysieke eSIM-kaart gebruiken met GL.iNet-routers](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

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

### IGMP Snooping {#igmp-snooping}

Raadpleeg de tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Raadpleeg de tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet brengt regelmatig firmware-updates voor zijn routers uit om de prestaties te verbeteren, fouten op te lossen en kwetsbaarheden te verhelpen.

Raadpleeg de tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Instellingen voor het OLED-scherm {#oled-screen-settings}

Op deze pagina kun je aanpassen welke informatie op het OLED-scherm van Mudi V2 (GL-E750V2) wordt weergegeven.


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

### Reset Firmware {#reset-firmware}

Raadpleeg de tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Raadpleeg de tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
