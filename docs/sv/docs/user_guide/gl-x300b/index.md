# Användarhandbok för Collie (GL-X300B) {#collie-gl-x300b-user-guide}

## Produktöversikt {#product-overview}

Collie (GL-X300B) är en industriell mobilnätsgateway för drift vid höga temperaturer och i miljöer med möjliga fysiska risker. Collie finns i tre versioner för stationära inomhusanläggningar (GL-X300B-RS485/GL-X300B-BLE) eller transportfordon (GL-X300B-GPS). Collie passar för maskin-till-maskin-kommunikation mellan elektriska enheter i miljöer med kraftiga elektriska störningar.

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

**Vad är skillnaden mellan GL-X300B-RS485, GL-X300B-BLE och GL-X300B-GPS?**

![gl-x300b series](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b_series.png){class="glboxshadow"}

![gl-x300b comparison](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/model_comparison.png){class="glboxshadow"}

- **GL-X300B-RS485** har ett RS485-chip med RS485-gränssnitt. Modulen stöder dubbelriktad dataöverföring för olika enheter inom industriell automation och IoT och möjliggör datainsamling, styrning och övervakning.

- **GL-X300B-BLE** har tre externa rundstrålande antenner för 2.4GHz Wi-Fi-, 4G LTE- och BLE-kommunikation. De tar emot signaler från alla riktningar och ger stor flexibilitet vid placering i industrimiljöer.

- **GL-X300B-GPS** har fem externa antenner: två för 2.4GHz Wi-Fi, två för 4G LTE och en GPS-antenn. De utdragbara kabelanslutna antennerna kan placeras på flera ställen i ett fordon och minskar mottagningsluckor i städer med hög nätverkstäthet.

!!! Note

    BLE- och GPS-versionerna har en minsta beställningskvantitet.

    Välj rätt antennkontakt för enhetsversionen. Inkompatibla kontakter kan orsaka antennfel eller onormal signalprestanda. Antenngränssnitten för varje version anges nedan:

    - X300B‑GPS: 5 x SMB-hankontakter
    - X300B‑RS485: 2 x RP‑SMA-honkontakter, 1 x SMA-honkontakt
    - X300B‑BLE: 3 x RP‑SMA-honkontakter

    Antennen måste ha en kontakt av motsvarande typ. Använd en antenn med honkontakt när enhetsporten är hane och en antenn med hankontakt när enhetsporten är hona.

## Förpackningens innehåll {#package-contents}

- 1 x användarhandbok
- 1 x Collie (GL-X300B-RS485) (två års garanti)
- 1 x Ethernet-kabel
- 1 x extern 4G-antenn
- 2 x externa Wi-Fi-antenner
- 1 x kopplingsplint (grön)
- 1 x väggmonteringssats
- 1 x DIN-skenesats
- 1 x nätadapter
- 4 x adaptrar (US-, UK-, EU- och AU-kontakter) (tre månaders garanti)

![gl-x300b package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b-rs485_package.jpg){class="glboxshadow"}

## Specifikationer {#specifications}

[Specifikationer för GL-X300B](https://www.gl-inet.com/products/gl-x300b/#specs){target="_blank"}

## Antenninstallation {#antenna-installation}

!!! note "GL-X300B-RS485"

    **Collie (GL-X300B-RS485)** levereras med följande antenner:

    * 1 x extern 4G-antenn
    * 2 x externa Wi-Fi-antenner (2.4GHz)

    Följ stegen nedan för att installera antennerna.

    1. Anslut antennerna (i valfri ordning).

        - Anslut de två identiska Wi-Fi-antennerna till **2.4G**-portarna.
        - Anslut den enda 4G-antennen till **4G**-porten.

        ![x300b rs485 antennas](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/antenna_installation/x300b-rs485-back.png){class="gl-80-desktop glboxshadow"}

    2. Rikta antennerna uppåt för optimal prestanda.

!!! note "GL-X300B-BLE"

    **Collie (GL-X300B-BLE)** levereras med följande antenner:

    * 1 x extern 4G-antenn
    * 1 x extern Wi-Fi-antenn (2.4GHz)
    * 1 x extern BLE-antenn

    Följ stegen nedan för att installera antennerna.

    1. Anslut antennerna (i valfri ordning).

        - Anslut Wi-Fi-antennen till **2.4G**-porten.
        - Anslut den enda 4G-antennen till **4G**-porten.
        - Anslut BLE-antennen till **BLE**-porten.

        ![x300b ble antennas](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/antenna_installation/x300b-ble-back.png){class="gl-80-desktop glboxshadow"}

    2. Rikta antennerna uppåt för optimal prestanda.

!!! note "GL-X300B-GPS"

    **Collie (GL-X300B-GPS)** levereras med följande antenner:

    * 2 x externa 4G-antenner
    * 2 x externa Wi-Fi-antenner (2.4GHz)
    * 1 x extern GPS-antenn

    Följ stegen nedan för att installera antennerna.

    1. Anslut antennerna (i valfri ordning).

        - Anslut de två identiska Wi-Fi-antennerna till **2.4G**-portarna.
        - Anslut de två identiska 4G-antennerna till **4G**-portarna.
        - Anslut GPS-antennen till **GPS**-porten.

        ![x300b gps antennas](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/antenna_installation/x300b-gps-back.png){class="gl-80-desktop glboxshadow"}

    2. Placera antennerna korrekt och undvik att kablarna trasslar sig för optimal prestanda.

        ![x300b gps antennas](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/antenna_installation/x300b-gps.jpg){class="glboxshadow"}

## Första konfigurationen {#first-time-setup}

Alla GL.iNet-routrar har en liknande konfigurationsprocess. [Klicka här för att läsa om den första konfigurationen](../../faq/first_time_setup.md).

## INTERNET {#internet}

Logga in på routerns webbadministrationspanel och välj **INTERNET** på menyn till vänster.

På den här sidan kan du välja internetanslutningstyp, till exempel Ethernet, Repeater, Tethering eller Cellular, beroende på modell.

Collie (GL-X300B) stöder three anslutningstyper: Ethernet, Repeater, and Cellular.

### Ethernet {#ethernet}

Anslut routern till ett aktivt modem eller en aktiv nätverksenhet med en Ethernet-kabel för att få internetåtkomst. Metoden ger vanligtvis den snabbaste och mest tillförlitliga internetanslutningen.

[Klicka här för att läsa om hur du ansluter till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Konfigurera routern som repeater för att utöka täckningen för ett befintligt Wi-Fi-nätverk. Som repeater tar den emot och vidarebefordrar trådlösa signaler inom sin räckvidd och utökar därmed täckningen. Metoden är användbar när en enda router inte kan täcka hela användningsområdet.

[Klicka här för att läsa om hur du ansluter till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### Cellular {#cellular}

Sätt in ett SIM-kort i routerns SIM-kortplats för att ansluta den till internet. Metoden är användbar för att dela internetåtkomst från ett enda SIM-kort med alla anslutna enheter.

[Klicka här för att läsa om hur du ansluter till internet via mobilnät](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet, Repeater och Cellular) samtidigt. Om internetanslutningen med högst prioritet slutar fungera växlar routern automatiskt till en annan internetanslutning. Detta kallas även Failover och ger en smidig och oavbruten internetåtkomst.

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
