# Przewodnik użytkownika Collie (GL-X300B)

## Przegląd produktu

Collie (GL-X300B) to przemysłowa brama komórkowa zaprojektowana do pracy w wysokich temperaturach i warunkach potencjalnych zagrożeń fizycznych. Istnieją trzy wersje Collie, przeznaczone do pracy w stacjonarnych obiektach wewnętrznych (GL-X300B-RS485 / GL-X300B-BLE) lub w pojazdach transportowych (GL-X300B-GPS). Collie idealnie nadaje się do komunikacji maszyna-maszyna między urządzeniami elektrycznymi w środowiskach o wysokim poziomie zakłóceń elektromagnetycznych.

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

**Czym różnią się GL-X300B-RS485, GL-X300B-BLE i GL-X300B-GPS?**

![gl-x300b series](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b_series.png){class="glboxshadow"}

![gl-x300b comparison](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/model_comparison.png){class="glboxshadow"}

- **GL-X300B-RS485** zawiera układ RS485 z interfejsem RS485. Moduł obsługuje dwukierunkową transmisję danych z różnych urządzeń w dziedzinie automatyki przemysłowej i IoT, realizując funkcje zbierania danych, sterowania i monitorowania.

- **GL-X300B-BLE** jest wyposażony w trzy zewnętrzne anteny dookólne do komunikacji Wi-Fi 2,4 GHz, 4G LTE i BLE, odbierające sygnały ze wszystkich kierunków i zapewniające dużą elastyczność montażu w środowisku przemysłowym.

- **GL-X300B-GPS** jest wyposażony w pięć anten zewnętrznych, w tym dwie anteny Wi-Fi 2,4 GHz, dwie anteny 4G LTE i jedną antenę GPS. Rozszerzalne anteny przewodowe idealnie nadają się do rozmieszczenia w wielu punktach odbioru wewnątrz pojazdu, minimalizując martwe strefy sygnału podczas podróży przez miasta o dużej gęstości sieci.

!!! Note

    Wersje BLE i GPS są dostępne przy minimalnej ilości zamówienia.

## Zawartość opakowania

- 1 x Instrukcja obsługi
- 1 x Collie (GL-X300B-RS485) (2-letnia gwarancja)
- 1 x Kabel Ethernet
- 1 x Zewnętrzna antena 4G
- 2 x Zewnętrzna antena Wi-Fi
- 1 x Kostka zaciskowa (zielona)
- 1 x Zestaw do montażu ściennego
- 1 x Zestaw do montażu na szynie DIN
- 1 x Zasilacz
- 4 x Adaptery wtyczek (US, UK, EU i AU) (3-miesięczna gwarancja)

![gl-x300b package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b-rs485_package.jpg){class="glboxshadow"}

## Specyfikacja

[Specyfikacja GL-X300B](https://www.gl-inet.com/products/gl-x300b/#specs){target="_blank"}

## Pierwsza konfiguracja

Wszystkie routery GL.iNet mają podobny proces konfiguracji. [Kliknij tutaj, aby dowiedzieć się więcej o pierwszej konfiguracji](../../faq/first_time_setup.md/).

## INTERNET

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **INTERNET** w menu po lewej stronie.

Ta strona umożliwia wybór typu połączenia internetowego, takiego jak Ethernet, Repeater, Tethering i Cellular, zależnie od modelu.

W przypadku Collie (GL-X300B) dostępne są trzy typy połączeń: Ethernet, Repeater i Cellular.

### Ethernet

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet, aby uzyskać dostęp do Internetu. Ta metoda zwykle zapewnia najszybsze i najbardziej niezawodne połączenie z Internetem.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### Repeater

Skonfiguruj router jako repeater, aby rozszerzyć zasięg istniejącej sieci Wi-Fi. W trybie repeatera urządzenie odbiera i retransmituje sygnał bezprzewodowy w swoim zasięgu, zwiększając tym samym obszar pokrycia. Ta metoda jest przydatna, gdy jeden router nie jest w stanie objąć zasięgiem całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą istniejącej sieci Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### Cellular

Włóż kartę SIM do gniazda karty SIM routera, aby połączyć go z Internetem. Ta metoda jest przydatna do udostępniania dostępu do Internetu z pojedynczej karty SIM wszystkim podłączonym urządzeniom.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi (np. Ethernet, Repeater i Cellular) jednocześnie. Jeśli połączenie internetowe o najwyższym priorytecie przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Jest to również nazywane przełączeniem awaryjnym i zapewnia płynny, nieprzerwany dostęp do Internetu.

Przejdź do [Multi-WAN](../../interface_guide/multi-wan.md), aby ustawić priorytet każdego połączenia internetowego.

Alternatywnie możesz zmienić tryb Multi-WAN z Failover na Load Balance, co umożliwia jednoczesne korzystanie z wielu interfejsów sieciowych w celu zwiększenia całkowitej przepustowości routera.

---

## WIRELESS

Ustawienia sieci bezprzewodowej pozwalają zarządzać bezpieczeństwem głównej sieci Wi-Fi oraz sieci Guest Wi-Fi. Są dostępne po przejściu do **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS

Klienci to urządzenia podłączone do routera. Możesz blokować klientów lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu urządzeniami klienckimi.](../../interface_guide/clients.md)

---

## VPN

Routery GL.iNet mają fabrycznie zainstalowane OpenVPN i WireGuard®, obsługujące ponad 30 usług VPN. Automatycznie szyfrują cały ruch sieciowy w podłączonej sieci, w tym urządzenia gościnne i urządzenia klienckie, które same nie obsługują szyfrowania VPN. Nasze routery mogą również działać jako serwer VPN, przekierowując ruch z urządzeń klienckich w zdalnych lokalizacjach do serwera VPN przez tunel VPN przed uzyskaniem dostępu do publicznego Internetu.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Szczegółowy przewodnik konfiguracji krok po kroku znajdziesz w poniższych linkach:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard

Szczegółowy przewodnik konfiguracji krok po kroku znajdziesz w poniższych linkach:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

Routery GL.iNet oferują szeroki zakres dodatkowych funkcji, które upraszczają zarządzanie urządzeniem, poprawiają komfort korzystania z Internetu, automatyzują aktualizacje firmware i nie tylko.

### Plug-ins

Zapoznaj się z poradnikiem [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Zapoznaj się z poradnikiem [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Zapoznaj się z poradnikiem [**GoodCloud**](../../interface_guide/cloud.md).

---

## NETWORK

### Firewall

Routery GL.iNet oferują wiele funkcji zapory sieciowej, aby zapewnić bezpieczne połączenie i pełną kontrolę użytkownika. Pozwalają konfigurować reguły zapory, w tym Port Forwarding, Open Ports i DMZ.

[Kliknij tutaj, aby dowiedzieć się więcej o zaporze sieciowej routerów GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Zapoznaj się z poradnikiem [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Zapoznaj się z poradnikiem [**LAN**](../../interface_guide/lan.md).

### DNS

Zapoznaj się z poradnikiem [**DNS**](../../interface_guide/dns.md).

### Network Mode

Zapoznaj się z poradnikiem [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Zapoznaj się z poradnikiem [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

Strona Mac Address wcześniej nazywała się Mac Clone, a od wersji v4.2 została zmieniona na Mac Address.

Zapoznaj się z poradnikiem [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Zapoznaj się z poradnikiem [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Zapoznaj się z poradnikiem [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Zapoznaj się z poradnikiem [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet regularnie udostępnia aktualizacje firmware routerów, aby poprawić wydajność, usuwać błędy i naprawiać luki w zabezpieczeniach.

Zapoznaj się z poradnikiem [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Zapoznaj się z poradnikiem [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Ta funkcja została przeniesiona do [**Security**](../../interface_guide/security.md) od wersji v4.5.

Zapoznaj się z poradnikiem [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Zapoznaj się z poradnikiem [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Zapoznaj się z poradnikiem [**Log**](../../interface_guide/log.md).

### Security

Ta funkcja jest dostępna od wersji v4.5.

Zapoznaj się z poradnikiem [**Security**](../../interface_guide/security.md).

### Reset Firmware

Zapoznaj się z poradnikiem [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Zapoznaj się z poradnikiem [**Advanced Settings**](../../interface_guide/advanced_settings.md).
