# Användarhandbok för Mudi V2 (GL-E750V2) {#mudi-v2-gl-e750v2-user-guide}

**Obs!** Mudi V2 (GL-E750V2) och Mudi (GL-E750) kör samma firmware. Om du använder Mudi (GL-E750) bör du [uppgradera firmware](https://dl.gl-inet.com/?model=e750) för att använda de senaste funktionerna.

## Produktöversikt {#product-overview}

Mudi V2 (GL-E750V2) är en bärbar 4G LTE-reserouter som är kompatibel med operatörer i hela världen. Den kör OpenWrt och GL.iNets SDK 4.0 med helt öppen källkod och erbjuder anpassningsmöjligheter och många funktioner. Mudi V2 stöder Wi-Fi-hastigheter på 300Mbps (2.4GHz) och 433Mbps (5GHz) samt MicroSD-kort på upp till 1TB. Den har ett inbyggt batteri på 7000mAh och stöder Multi-WAN (failover och lastbalansering) för en stabil anslutning för alla enheter.

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Knapp {#button}

- Håll strömknappen intryckt i **3 sekunder**: Slå på enheten.

- Håll strömknappen intryckt i **3-5 sekunder**: Aktivera Standby Mode.

- Håll strömknappen intryckt i **mer än 5 sekunder**: Stäng av enheten.

    (När du håller knappen intryckt i 3 sekunder visas först ”Standby Mode On” på OLED-skärmen. FORTSÄTT HÅLLA strömknappen intryckt tills ”Shut Down” visas under ”Standby Mode On”. Enheten räknar ned 3 sekunder och stängs av.)

## Vänteläge {#standby-mode}

I Standby Mode stänger Mudi V2 (GL-E750V2) av Wi-Fi och 4G för att spara ström. Det går inte att ansluta till Mudi V2 i detta läge.

Slå på eller av Standby Mode genom att hålla strömknappen intryckt i 3 sekunder. ”Standby Mode On” eller ”Standby Mode Off” visas på OLED-skärmen.

## Förpackningens innehåll {#package-contents}

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x bärbar 4G LTE-router Mudi V2 (GL-E750V2)
- 1 x nätadapter
- 4 x adaptrar (US-, EU-, UK- och AU-kontakter)
- 1 x användarhandbok
- 1 x garantikort
- 1 x Ethernet-kabel
- 1 x USB-C-portreplikator
- 1 x USB-C-till-USB-C-kabel
- 1 x USB-A-till-USB-C-kabel
- 1 x förvaringspåse
- 1 x tackkort

---

## Första konfigurationen {#first-time-setup}

Titta på videon eller följ stegen för att konfigurera Mudi V2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Sätt in ett SIM-kort {#1-insert-a-sim-card}

Sätt in ett SIM-kort och ett valfritt MicroSD-kort i Mudi V2 (GL-E750V2).

Obs! Om du använder ett SIM-kort måste du sätta in det i enheten innan den slås på.

1. Vänd Mudi V2 (GL-E750V2) med baksidan uppåt.
2. För in ett finger i hålet nära kanten på locket.
3. För fingret längs kanten.
4. När locket har lyfts något (ungefär 25 till 30 grader) drar du upp det för att öppna.
5. Sätt in kortet i kortplatsen enligt symbolen nära hörnet.
6. Tryck ned locket för att stänga bakstycket.

### 2. Slå på {#2-power-on}

Tryck på strömknappen för att slå på enheten.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_power-on.png){class="glboxshadow"}

När Mudi V2 (GL-E750V2) är avstängd kan du fortfarande kontrollera batteristatusen genom att trycka på strömknappen. OLED-skärmen visar batteristatusen.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_battery.png){class="glboxshadow"}

Använd en standardnätadapter på 5V/2A. Annars kan funktionsfel uppstå.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET {#internet}

Logga in på routerns webbadministrationspanel och välj **INTERNET** på menyn till vänster.

På den här sidan kan du välja internetanslutningstyp, till exempel Ethernet, Repeater, Tethering eller Cellular.

### Ethernet {#ethernet}

Anslut routern till ett aktivt modem eller en aktiv nätverksenhet med en Ethernet-kabel för att få internetåtkomst. Metoden ger vanligtvis den snabbaste och mest tillförlitliga internetanslutningen.

[Klicka här för att läsa om hur du ansluter till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Konfigurera routern som repeater för att utöka täckningen för ett befintligt Wi-Fi-nätverk. Som repeater tar den emot och vidarebefordrar trådlösa signaler inom sin räckvidd och utökar därmed täckningen. Metoden är användbar när en enda router inte kan täcka hela användningsområdet.

[Klicka här för att läsa om hur du ansluter till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Anslut routerns USB-port till en smartphone med aktiv mobildata via en USB-kabel för att få internetåtkomst. Metoden gör att flera enheter som är anslutna till routern kan använda smarttelefonens mobildata för internetåtkomst.

[Klicka här för att läsa om hur du ansluter till internet via internetdelning med USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Ta bort bakstycket från Mudi V2 och sätt in ett SIM-kort i SIM-kortplatsen för att ansluta till internet. Metoden är användbar för att dela internetåtkomst från ett enda SIM-kort med alla anslutna enheter.

[Klicka här för att läsa om hur du ansluter till internet via mobilnät](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_cellular.png){class="glboxshadow"}

Information om hur du använder ett fysiskt eSIM-kort på GL.iNet-routern finns här: [Använd ett fysiskt eSIM-kort med GL.iNet-routrar](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

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

### IGMP Snooping {#igmp-snooping}

Se guiden [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Se guiden [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet uppdaterar regelbundet routrarnas firmware för att förbättra prestandan, åtgärda fel och korrigera sårbarheter.

Se guiden [**Upgrade**](../../interface_guide/upgrade.md).

### OLED-skärminställningar {#oled-screen-settings}

På den här sidan kan du ange vilken information som visas på OLED-skärmen på Mudi V2 (GL-E750V2).


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

### Reset Firmware {#reset-firmware}

Se guiden [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Se guiden [**Advanced Settings**](../../interface_guide/advanced_settings.md).
