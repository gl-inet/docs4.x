# Przewodnik użytkownika Cirrus (GL-AP1300) {#cirrus-gl-ap1300-user-guide}

## Przegląd produktu {#product-overview}

Cirrus (GL-AP1300) to sufitowy bezprzewodowy punkt dostępowy klasy biznesowej z rozwiązaniem Wi-Fi MU-MIMO. Wbudowane zasilanie PoE oraz funkcja Watchdog timer pozwalają spełnić wymagania większości zastosowań firmowych. Dzięki dopracowanemu systemowi zarządzania GoodCloud obsługa urządzenia jest bardzo łatwa i wygodna. Możesz włączyć zdalny i bezpieczny dostęp, gdziekolwiek jesteś i kiedykolwiek chcesz.

![gl-ap1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ap1300/hardware_info/ap1300_interface.jpg){class="glboxshadow"}

## Specyfikacja {#specifications}

[Specyfikacja GL-AP1300](https://www.gl-inet.com/products/gl-ap1300/#specs){target="_blank"}

---

## Pierwsza konfiguracja {#first-time-setup}

Wszystkie routery GL.iNet mają podobny proces konfiguracji. [Kliknij tutaj, aby dowiedzieć się więcej o pierwszej konfiguracji](../../faq/first_time_setup.md).

---

## INTERNET {#internet}

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **INTERNET** w menu po lewej stronie.

Ta strona umożliwia wybór typu połączenia internetowego, takiego jak Ethernet, Repeater, Tethering i Cellular, zależnie od modelu.

W przypadku Cirrus (GL-AP1300) dostępne są dwa typy połączeń: Ethernet i Repeater.

### Ethernet {#ethernet}

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet, aby uzyskać dostęp do Internetu. Ta metoda zwykle zapewnia najszybsze i najbardziej niezawodne połączenie z Internetem.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

### Repeater {#repeater}

Skonfiguruj router jako repeater, aby rozszerzyć zasięg istniejącej sieci Wi-Fi. W trybie repeatera urządzenie odbiera i retransmituje sygnał bezprzewodowy w swoim zasięgu, zwiększając tym samym obszar pokrycia. Ta metoda jest przydatna, gdy jeden router nie jest w stanie objąć zasięgiem całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą istniejącej sieci Wi-Fi](../../interface_guide/internet_repeater.md)

### Multi-WAN {#multi-wan}

Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi (np. Ethernet, Repeater) jednocześnie. Jeśli połączenie internetowe o najwyższym priorytecie przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Jest to również nazywane przełączeniem awaryjnym i zapewnia płynny, nieprzerwany dostęp do Internetu.

Przejdź do [Multi-WAN](../../interface_guide/multi-wan.md), aby ustawić priorytet każdego połączenia internetowego.

Alternatywnie możesz zmienić tryb Multi-WAN z Failover na Load Balance, co umożliwia jednoczesne korzystanie z wielu interfejsów sieciowych w celu zwiększenia całkowitej przepustowości routera.

---

## WIRELESS {#wireless}

Ustawienia sieci bezprzewodowej pozwalają zarządzać bezpieczeństwem głównej sieci Wi-Fi oraz sieci Guest Wi-Fi. Są dostępne po przejściu do **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS {#clients}

Klienci to urządzenia podłączone do routera. Możesz blokować klientów lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu urządzeniami klienckimi.](../../interface_guide/clients.md)

---

## VPN {#vpn}

Routery GL.iNet mają fabrycznie zainstalowane OpenVPN i WireGuard®, obsługujące ponad 30 usług VPN. Gdy klient VPN jest włączony, router może szyfrować ruch urządzeń w sieci, w tym urządzeń, na których nie można uruchomić aplikacji VPN, zgodnie z ustawieniami polityki VPN. Nasze routery mogą również działać jako serwer VPN, przekierowując ruch z urządzeń klienckich w zdalnych lokalizacjach do serwera VPN przez tunel VPN przed uzyskaniem dostępu do publicznego Internetu.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Szczegółowy przewodnik konfiguracji krok po kroku znajdziesz w poniższych linkach:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Szczegółowy przewodnik konfiguracji krok po kroku znajdziesz w poniższych linkach:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS {#applications}

Routery GL.iNet oferują szeroki zakres dodatkowych funkcji, które upraszczają zarządzanie urządzeniem, poprawiają komfort korzystania z Internetu, automatyzują aktualizacje firmware i nie tylko.

### Plug-ins {#plug-ins}

Zapoznaj się z poradnikiem [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Zapoznaj się z poradnikiem [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Zapoznaj się z poradnikiem [**GoodCloud**](../../interface_guide/cloud.md).

### AdGuard Home {#adguard-home}

Zapoznaj się z poradnikiem [**AdGuard Home**](../../interface_guide/adguardhome.md).

---

## NETWORK {#network}

### Firewall {#firewall}

Routery GL.iNet oferują wiele funkcji zapory sieciowej, aby zapewnić bezpieczne połączenie i pełną kontrolę użytkownika. Pozwalają konfigurować reguły zapory, w tym Port Forwarding, Open Ports i DMZ.

[Kliknij tutaj, aby dowiedzieć się więcej o zaporze sieciowej routerów GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Zapoznaj się z poradnikiem [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Zapoznaj się z poradnikiem [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Zapoznaj się z poradnikiem [**DNS**](../../interface_guide/dns.md).

### Network Mode {#network-mode}

Zapoznaj się z poradnikiem [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Zapoznaj się z poradnikiem [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

Strona Mac Address wcześniej nazywała się Mac Clone, a od wersji v4.2 została zmieniona na Mac Address.

Zapoznaj się z poradnikiem [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Zapoznaj się z poradnikiem [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Zapoznaj się z poradnikiem [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Zapoznaj się z poradnikiem [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet regularnie udostępnia aktualizacje firmware routerów, aby poprawić wydajność, usuwać błędy i naprawiać luki w zabezpieczeniach.

Zapoznaj się z poradnikiem [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks {#scheduled-tasks}

Zapoznaj się z poradnikiem [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Ta funkcja została przeniesiona do [**Security**](../../interface_guide/security.md) od wersji v4.5.

Zapoznaj się z poradnikiem [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Zapoznaj się z poradnikiem [**Time Zone**](../../interface_guide/time_zone.md).

### Log {#log}

Zapoznaj się z poradnikiem [**Log**](../../interface_guide/log.md).

### Security {#security}

Ta funkcja jest dostępna od wersji v4.5.

Zapoznaj się z poradnikiem [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Zapoznaj się z poradnikiem [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Zapoznaj się z poradnikiem [**Advanced Settings**](../../interface_guide/advanced_settings.md).
