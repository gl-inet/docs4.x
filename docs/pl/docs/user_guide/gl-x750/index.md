# Instrukcja użytkownika Spitz (GL-X750)

## Omówienie produktu

Spitz to bezprzewodowy router 3G/4G dual-band, szeroko stosowany w obszarze inteligentnego domu i IoT. Działa na systemie OpenWRT OS, dzięki czemu możesz skompilować własne oprogramowanie dopasowane do różnych scenariuszy zastosowań. Ma wbudowany moduł mini PCIe 3G/4G, który obsługuje różnych operatorów i może być używany na całym świecie.

Spitz V2 (GL-X750V2) to zaawansowana wersja Spitz (GL-X750). Jest wyposażona w przeprojektowaną płytę PCBA i zoptymalizowane anteny poprawiające wydajność 4G.

![gl-x750 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/x750v2_interface.jpg){class="glboxshadow"}

## Specyfikacje

[GL-X750 specifications](https://www.gl-inet.com/products/gl-x750/#specs){target="_blank"}

---

## Pierwsze uruchomienie

Wszystkie routery GL.iNet mają podobny proces konfiguracji. [Kliknij tutaj, aby dowiedzieć się więcej o pierwszej konfiguracji](../../faq/first_time_setup.md/).

---

## INTERNET

Zaloguj się do panelu administracyjnego routera i przejdź do **INTERNET** w menu po lewej stronie.

Ta strona pozwala wybrać typ połączenia z Internetem, taki jak Ethernet, Repeater, Tethering i Cellular.

### Ethernet

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet, aby uzyskać dostęp do Internetu. Ta metoda zwykle zapewnia najszybsze i najbardziej niezawodne połączenie internetowe.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_ethernet.png){class="glboxshadow"}

### Repeater

Skonfiguruj router jako repeater, aby rozszerzyć zasięg istniejącej sieci Wi-Fi. Jako repeater odbiera i retransmituje sygnał bezprzewodowy w swoim zasięgu, rozszerzając tym samym pokrycie. Ta metoda jest przydatna, gdy pojedynczy router nie obejmuje całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_repeater.png){class="glboxshadow"}

### Tethering

Podłącz port USB routera do smartfona z aktywną transmisją danych komórkowych za pomocą kabla USB, aby uzyskać dostęp do Internetu. Ta metoda umożliwia wielu urządzeniom podłączonym do routera korzystanie z Internetu przez transmisję danych smartfona.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem przez tethering USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_tethering.png){class="glboxshadow"}

### Cellular
 
Włóż kartę SIM do gniazda karty SIM routera, aby połączyć go z Internetem. Ta metoda jest przydatna do udostępniania dostępu do Internetu z jednej karty SIM wszystkim podłączonym urządzeniom.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN to funkcja sieciowa, która umożliwia jednoczesne skonfigurowanie routera z wieloma połączeniami internetowymi (np. Ethernet, Repeater i Cellular). Jeśli połączenie internetowe o najwyższym priorytecie przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Nazywa się to również Failover i zapewnia płynny, nieprzerwany dostęp do Internetu.

Przejdź do [Multi-WAN](../../interface_guide/multi-wan.md), aby ustawić priorytet dla każdego połączenia internetowego.

Alternatywnie możesz zmienić tryb Multi-WAN z Failover na Load Balance, co umożliwia jednoczesne korzystanie z wielu interfejsów sieciowych w celu zwiększenia całkowitej przepustowości routera.

---

## WIRELESS

Ustawienia sieci bezprzewodowej pozwalają zarządzać zabezpieczeniami głównej sieci Wi-Fi i sieci Wi-Fi dla gości. Są dostępne po przejściu do **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS

Klienci to urządzenia podłączone do routera. Możesz blokować klientów lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu urządzeniami klienckimi.](../../interface_guide/clients.md)

---

## VPN

Routery GL.iNet są fabrycznie wyposażone w OpenVPN i WireGuard® oraz obsługują ponad 30 usług VPN. Automatycznie szyfrują cały ruch sieciowy w podłączonej sieci, w tym urządzenia gościnne i klienckie, które nie obsługują samodzielnie szyfrowania VPN. Nasze routery mogą również działać jako serwery VPN, przekierowując ruch z urządzeń klienckich w zdalnych lokalizacjach do serwera VPN przez tunel VPN przed uzyskaniem dostępu do publicznego Internetu.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Zapoznaj się z poniższymi linkami, aby uzyskać instrukcję konfiguracji krok po kroku:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard

Zapoznaj się z poniższymi linkami, aby uzyskać instrukcję konfiguracji krok po kroku:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

Routery GL.iNet zawierają szeroki zakres dodatkowych funkcji, które upraszczają zarządzanie urządzeniem, poprawiają komfort korzystania z Internetu, automatyzują aktualizacje oprogramowania i nie tylko.

### Plug-ins

Zapoznaj się z samouczkiem [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Zapoznaj się z samouczkiem [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Zapoznaj się z samouczkiem [**GoodCloud**](../../interface_guide/cloud.md).

### Parental Control

Zapoznaj się z samouczkiem [**Parental Control**](../../interface_guide/parental_control.md).

---

## NETWORK

### Firewall

Routery GL.iNet oferują wiele funkcji zapory, aby zapewnić bezpieczne połączenie i pełną kontrolę użytkownika. Pozwalają one konfigurować reguły zapory, w tym Port Forwarding, Open Ports i DMZ.

[Kliknij tutaj, aby dowiedzieć się więcej o zaporze routerów GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Zapoznaj się z samouczkiem [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Zapoznaj się z samouczkiem [**LAN**](../../interface_guide/lan.md).

### DNS

Zapoznaj się z samouczkiem [**DNS**](../../interface_guide/dns.md).

### Network Mode

Zapoznaj się z samouczkiem [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Zapoznaj się z samouczkiem [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

Strona Mac Address była wcześniej nazywana Mac Clone i od wersji v4.2 została zmieniona na Mac Address.

Zapoznaj się z samouczkiem [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Zapoznaj się z samouczkiem [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Zapoznaj się z samouczkiem [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Zapoznaj się z samouczkiem [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet regularnie udostępnia aktualizacje oprogramowania routerów, aby poprawiać wydajność, usuwać błędy i naprawiać luki w zabezpieczeniach.

Zapoznaj się z samouczkiem [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Zapoznaj się z samouczkiem [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Ta funkcja została przeniesiona do [**Security**](../../interface_guide/security.md) od wersji v4.5.

Zapoznaj się z samouczkiem [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Zapoznaj się z samouczkiem [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Zapoznaj się z samouczkiem [**Log**](../../interface_guide/log.md).

### Security

Ta funkcja jest dostępna od wersji v4.5.

Zapoznaj się z samouczkiem [**Security**](../../interface_guide/security.md).

### Reset Firmware

Zapoznaj się z samouczkiem [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Zapoznaj się z samouczkiem [**Advanced Settings**](../../interface_guide/advanced_settings.md).
