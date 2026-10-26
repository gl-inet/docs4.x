# Användarhandbok för Slate Plus (GL-A1300) {#slate-plus-gl-a1300-user-guide}

## Produktöversikt {#product-overview}

Slate Plus (GL-A1300) är en reserouter i fickformat med en kraftfull processor som är optimerad för stabila nätverk och effektiv bearbetning av VPN-kryptering. Den innehåller våra senaste säkerhetsfunktioner och kör det senaste operativsystemet OpenWrt. Routern är utformad för dig som reser ofta och använder VPN-nätverk i stor omfattning.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

Observera att adaptern i förpackningen beror på leveranslandet.

Förpackningen innehåller:

- 1 x användarhandbok
- 1 x Slate Plus (GL-A1300)
- 1 x Ethernet-kabel
- 1 x garantikort
- 1 x nätadapter (vald kontakttyp)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## LED-indikering {#led-indication}

[LED-indikering](../../faq/led.md#gl-a1300)

## Specifikationer {#specifications}

[Specifikationer för GL-A1300](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

## Första konfigurationen {#first-time-setup}

Alla GL.iNet-routrar har en enkel och nästan identisk konfigurationsprocess. [Klicka här för att läsa om den första konfigurationen](../../faq/first_time_setup.md).

Konfigurera Slate Plus med någon av de fyra internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering eller Cellular. Se konfigurationsvideon nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## INTERNET {#internet}

I gränssnittet för internetkonfiguration kan du välja vilken typ av internetanslutning som routern stöder.

Konfigurera internetanslutningen genom att välja **INTERNET** på sidomenyn i routerns webbadministrationspanel.

Följande fyra sätt att ansluta till internet stöds:

### Ethernet {#ethernet}

Överför data via Ethernet genom att ansluta routern till ett aktivt modem eller en aktiv nätverksenhet med en Ethernet-kabel. Metoden ger vanligtvis den snabbaste och mest tillförlitliga internetanslutningen.

[Klicka här för att läsa om hur du ansluter till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Utöka täckningen för ett befintligt Wi-Fi-nätverk genom att låta routern ta emot trådlösa signaler inom räckvidden och vidarebefordra dem över ett större område. Metoden är särskilt användbar när en enda router inte har tillräcklig räckvidd för hela användningsområdet.

[Klicka här för att läsa om hur du ansluter till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Ge anslutna enheter internetåtkomst genom att dela en smartphones mobildata med routern via kabel. Metoden är särskilt användbar när du vill använda telefonens dataanslutning för internetåtkomst.

[Klicka här för att läsa om hur du ansluter till internet via internetdelning med USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Anslut routern till internet genom att sätta in ett USB-modem för mobilnät i routerns USB-port. Metoden är särskilt användbar för att dela USB-modemets internetanslutning med alla anslutna enheter.

[Klicka här för att läsa om hur du ansluter till internet via USB-modem](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### Prioritet och lastbalansering {#priority-and-load-balance}

Öppna [Multi-WAN](../../interface_guide/multi-wan.md) för att ange prioriteten för varje internetanslutningsmetod eller lastbalanseringen när flera metoder används samtidigt.

---

## WIRELESS {#wireless}

Med de trådlösa inställningarna kan du hantera nätverkssäkerheten för det primära Wi-Fi-nätverket och gästnätverket. Öppna inställningarna genom att välja **WIRELESS** på sidomenyn.

[Klicka här för att läsa mer om den trådlösa konfigurationen](../../interface_guide/wireless.md)

---

## CLIENTS {#clients}

Klienter är enheter som är anslutna till routern. Du kan blockera klienter eller begränsa deras nätverkshastighet. Öppna gränssnittet genom att klicka på **CLIENTS** på sidomenyn i routerns administratörspanel.

[Klicka här för att läsa mer om hur du hanterar enhetsklienter.](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNet-routrar levereras med OpenVPN och WireGuard® förinstallerade och stöder över 30 VPN-tjänster. När VPN-klienten är aktiverad kan routern kryptera trafiken för enheter i nätverket enligt dina VPN-principer, även för enheter som inte kan köra VPN-appar. Våra routrar kan också fungera som VPN-servrar och dirigera trafik från fjärranslutna klientenheter till VPN-servern via en VPN-tunnel innan trafiken når det offentliga internet.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Följ länkarna nedan för stegvisa konfigurationsanvisningar:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Följ länkarna nedan för stegvisa konfigurationsanvisningar:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

---

## Program {#applications}

GL.iNet-routrar innehåller många tilläggsfunktioner som förenklar enhetshanteringen, förbättrar internetupplevelsen och automatiserar firmwareuppdateringar.

### Plug-ins {#plug-ins}

Se guiden [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Se guiden [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Se guiden [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage {#network-storage}

Se guiden [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home {#adguard-home}

Se guiden [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Parental Control {#parental-control}

Se guiden [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier {#zerotier}

Se guiden [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale {#tailscale}

Se guiden [**Tailscale**](../../interface_guide/tailscale.md).

---

## NETWORK {#network}

### Firewall {#firewall}

GL.iNet-routrar innehåller flera brandväggsfunktioner som ger en säker anslutning och fullständig kontroll. Du kan konfigurera brandväggsregler för bland annat Port Forwarding, Open Ports och DMZ.

[Klicka här för att läsa mer om brandväggen i GL.iNet-routrar](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan}

Se guiden [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Se guiden [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Se guiden [**DNS**](../../interface_guide/dns.md).

### Network Mode {#network-mode}

Se guiden [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Se guiden [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

Sidan Mac Address hette tidigare Mac Clone men har kallats Mac Address sedan v4.2.

Se guiden [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Se guiden [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Se guiden [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Se guiden [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet uppdaterar regelbundet routrarnas firmware för att förbättra prestandan, åtgärda fel och korrigera sårbarheter.

Se guiden [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks {#scheduled-tasks}

Se guiden [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Funktionen har flyttats till [**Security**](../../interface_guide/security.md) sedan v4.5.

Se guiden [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Se guiden [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings {#toggle-button-settings}

Se guiden [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log {#log}

Se guiden [**Log**](../../interface_guide/log.md).

### Security {#security}

Funktionen är tillgänglig från och med v4.5.

Se guiden [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Se guiden [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Se guiden [**Advanced Settings**](../../interface_guide/advanced_settings.md).
