# Användarhandbok för Cirrus (GL-AP1300) {#cirrus-gl-ap1300-user-guide}

## Produktöversikt {#product-overview}

Den takmonterade trådlösa åtkomstpunkten Cirrus (GL-AP1300) är en avancerad gateway i företagsklass med en MU-MIMO Wi-Fi-lösning. PoE-strömförsörjning och en inbyggd Watchdog-timer uppfyller de flesta användningsbehoven på företagsnivå. Det välutvecklade GoodCloud-hanteringssystemet gör enhetshanteringen enkel och smidig. Du kan aktivera säker fjärråtkomst var och när du vill.

![gl-ap1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ap1300/hardware_info/ap1300_interface.jpg){class="glboxshadow"}

## Specifikationer {#specifications}

[Specifikationer för GL-AP1300](https://www.gl-inet.com/products/gl-ap1300/#specs){target="_blank"}

---

## Första konfigurationen {#first-time-setup}

Alla GL.iNet-routrar har en liknande konfigurationsprocess. [Klicka här för att läsa om den första konfigurationen](../../faq/first_time_setup.md).

---

## INTERNET {#internet}

Logga in på routerns webbadministrationspanel och välj **INTERNET** på menyn till vänster.

På den här sidan kan du välja internetanslutningstyp, till exempel Ethernet, Repeater, Tethering eller Cellular, beroende på modell.

Cirrus (GL-AP1300) stöder two anslutningstyper: Ethernet and Repeater.

### Ethernet {#ethernet}

Anslut routern till ett aktivt modem eller en aktiv nätverksenhet med en Ethernet-kabel för att få internetåtkomst. Metoden ger vanligtvis den snabbaste och mest tillförlitliga internetanslutningen.

[Klicka här för att läsa om hur du ansluter till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md)

### Repeater {#repeater}

Konfigurera routern som repeater för att utöka täckningen för ett befintligt Wi-Fi-nätverk. Som repeater tar den emot och vidarebefordrar trådlösa signaler inom sin räckvidd och utökar därmed täckningen. Metoden är användbar när en enda router inte kan täcka hela användningsområdet.

[Klicka här för att läsa om hur du ansluter till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md)

### Multi-WAN {#multi-wan}

Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet och Repeater) samtidigt. Om internetanslutningen med högst prioritet slutar fungera växlar routern automatiskt till en annan internetanslutning. Detta kallas även Failover och ger en smidig och oavbruten internetåtkomst.

Öppna [Multi-WAN](../../interface_guide/multi-wan.md) för att ange prioriteten för varje internetanslutning.

Du kan även växla Multi-WAN-läget från Failover till Load Balance. Då kan du använda flera nätverksgränssnitt samtidigt och öka routerns totala bandbredd.

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

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## Program {#applications}

GL.iNet-routrar innehåller många tilläggsfunktioner som förenklar enhetshanteringen, förbättrar internetupplevelsen och automatiserar firmwareuppdateringar.

### Plug-ins {#plug-ins}

Se guiden [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Se guiden [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Se guiden [**GoodCloud**](../../interface_guide/cloud.md).

### AdGuard Home {#adguard-home}

Se guiden [**AdGuard Home**](../../interface_guide/adguardhome.md).

---

## NETWORK {#network}

### Firewall {#firewall}

GL.iNet-routrar innehåller flera brandväggsfunktioner som ger en säker anslutning och fullständig kontroll. Du kan konfigurera brandväggsregler för bland annat Port Forwarding, Open Ports och DMZ.

[Klicka här för att läsa mer om brandväggen i GL.iNet-routrar](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

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

### Log {#log}

Se guiden [**Log**](../../interface_guide/log.md).

### Security {#security}

Funktionen är tillgänglig från och med v4.5.

Se guiden [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Se guiden [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Se guiden [**Advanced Settings**](../../interface_guide/advanced_settings.md).
