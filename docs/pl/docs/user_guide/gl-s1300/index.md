# Przewodnik użytkownika Convexa-S (GL-S1300)

## Opis produktu

Convexa-S (GL-S1300) to wyjątkowa brama inteligentnego domu z technologią beamforming Wi-Fi i opcjonalnym Bluetooth, która łączy wszystkie urządzenia IoT. Zapewnia łączną prędkość Wi-Fi 1267 Mb/s, 3 porty gigabitowe oraz obsługę MU-MIMO i Wi-Fi SON, pomagając eliminować martwe strefy sygnału. Dzięki 8 GB pamięci masowej i systemowi OpenWrt umożliwia korzystanie z VPN, pamięci sieciowej i konfigurowalnych rozwiązań, a także zdalne zarządzanie przez GoodCloud.

![gl-s1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s1300/hardware_info/s1300_interface.jpg){class="glboxshadow"}

## Specyfikacja

[Specyfikacja GL-S1300](https://www.gl-inet.com/products/gl-s1300/#specs){target="_blank"}

---

## Pierwsza konfiguracja

Wszystkie routery GL.iNet mają podobny proces konfiguracji. [Kliknij tutaj, aby dowiedzieć się więcej o pierwszej konfiguracji](../../faq/first_time_setup.md/).

---

## INTERNET

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **INTERNET** w menu po lewej stronie.

Na tej stronie możesz wybrać typ połączenia z internetem, taki jak Ethernet, Repeater, Tethering lub Cellular.

### Ethernet

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet, aby uzyskać dostęp do internetu. Ta metoda zazwyczaj zapewnia najszybsze i najbardziej niezawodne połączenie z internetem.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

### Repeater

Skonfiguruj router jako repeater, aby rozszerzyć zasięg istniejącej sieci Wi-Fi. W tym trybie urządzenie odbiera i retransmituje sygnał bezprzewodowy w swoim zasięgu, zwiększając obszar pokrycia. Ta metoda jest przydatna, gdy jeden router nie jest w stanie objąć zasięgiem całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md)

### Tethering

Podłącz port USB routera do smartfona z aktywną transmisją danych przez kabel USB, aby uzyskać dostęp do internetu. Ta metoda umożliwia wielu urządzeniom podłączonym do routera korzystanie z internetu z użyciem transmisji danych smartfona.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez USB tethering](../../interface_guide/internet_tethering.md)

### Cellular

Podłącz modem USB z obsługą sieci komórkowej do portu USB routera, aby uzyskać dostęp do internetu. Ta metoda jest przydatna do udostępniania połączenia internetowego z modemu USB wszystkim podłączonym urządzeniom.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez modem USB](../../interface_guide/internet_cellular.md)

### Multi-WAN

Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi (np. Ethernet i Repeater) jednocześnie. Jeśli połączenie internetowe o najwyższym priorytecie przestanie działać, router automatycznie przełączy się na inne połączenie. Jest to nazywane przełączeniem awaryjnym i zapewnia płynny, nieprzerwany dostęp do internetu.

Przejdź do [Multi-WAN](../../interface_guide/multi-wan.md), aby ustawić priorytet każdego połączenia internetowego.

Możesz również przełączyć tryb Multi-WAN z przełączenia awaryjnego na równoważenie obciążenia, co pozwala jednocześnie korzystać z wielu interfejsów sieciowych w celu zwiększenia całkowitej przepustowości routera.

---

## WIRELESS

Ustawienia sieci bezprzewodowej pozwalają zarządzać zabezpieczeniami głównej sieci Wi-Fi i sieci gościnnej. Są dostępne po przejściu do **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS

Sekcja **CLIENTS** pokazuje urządzenia podłączone do routera. Możesz je blokować lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu urządzeniami klienckimi](../../interface_guide/clients.md)

---

## VPN

Routery GL.iNet mają fabrycznie zainstalowane OpenVPN i WireGuard®, obsługując ponad 30 usług VPN. Automatycznie szyfrują cały ruch sieciowy w podłączonej sieci, w tym urządzeń gościnnych i urządzeń klienckich, które same nie obsługują szyfrowania VPN. Nasze routery mogą również działać jako serwery VPN, przekierowując ruch z urządzeń klienckich w zdalnych lokalizacjach do serwera VPN przez tunel VPN przed uzyskaniem dostępu do publicznego internetu.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Szczegółowe instrukcje konfiguracji krok po kroku znajdziesz w poniższych odnośnikach:

- [**Konfiguracja klienta OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Konfiguracja serwera OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Szczegółowe instrukcje konfiguracji krok po kroku znajdziesz w poniższych odnośnikach:

- [**Konfiguracja klienta WireGuard**](../../interface_guide/wireguard_client.md)
- [**Konfiguracja serwera WireGuard**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

Routery GL.iNet oferują szeroki zestaw dodatkowych funkcji, które upraszczają zarządzanie urządzeniem, poprawiają komfort korzystania z internetu, automatyzują aktualizacje oprogramowania układowego i nie tylko.

### Plug-ins

Przejdź do poradnika [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Przejdź do poradnika [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Przejdź do poradnika [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage

Przejdź do poradnika [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home

Przejdź do poradnika [**AdGuard Home**](../../interface_guide/adguardhome.md).

---

## NETWORK

### Firewall

Routery GL.iNet oferują wiele funkcji zapory sieciowej, które zapewniają bezpieczne połączenie i pełną kontrolę użytkownika. Umożliwiają konfigurowanie reguł zapory, w tym Port Forwarding, Open Ports i DMZ.

[Kliknij tutaj, aby dowiedzieć się więcej o zaporze sieciowej routerów GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Przejdź do poradnika [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Przejdź do poradnika [**LAN**](../../interface_guide/lan.md).

### DNS

Przejdź do poradnika [**DNS**](../../interface_guide/dns.md).

### Network Mode

Przejdź do poradnika [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Przejdź do poradnika [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

Strona Mac Address wcześniej nazywała się Mac Clone, a od wersji v4.2 została przemianowana na Mac Address.

Przejdź do poradnika [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Przejdź do poradnika [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Przejdź do poradnika [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

### Network Acceleration

Funkcja była wcześniej znana jako [Hardware Acceleration](../../interface_guide/hardware_acceleration.md).

Przejdź do poradnika [**Network Acceleration**](../../interface_guide/network_acceleration.md).

---

## SYSTEM

### Overview

Przejdź do poradnika [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet regularnie udostępnia aktualizacje oprogramowania układowego routerów, aby poprawiać wydajność, usuwać błędy i naprawiać luki w zabezpieczeniach.

Przejdź do poradnika [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Przejdź do poradnika [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Ta funkcja została przeniesiona do [**Security**](../../interface_guide/security.md) od wersji v4.5.

Przejdź do poradnika [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Przejdź do poradnika [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Przejdź do poradnika [**Log**](../../interface_guide/log.md).

### Security

Ta funkcja jest dostępna od wersji v4.5.

Przejdź do poradnika [**Security**](../../interface_guide/security.md).

### Reset Firmware

Przejdź do poradnika [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Przejdź do poradnika [**Advanced Settings**](../../interface_guide/advanced_settings.md).
