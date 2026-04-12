# Przewodnik użytkownika GL-S200

## Przegląd produktu

GL-S200 to zminiaturyzowana brama Thread obsługująca protokół BLE, działająca na wysoce konfigurowalnym systemie operacyjnym OpenWrt, z obsługą zarządzania urządzeniami w chmurze. Posiada wszechstronną konstrukcję umożliwiającą podłączenie różnych urządzeń inteligentnego domu lub masowe połączenia urządzeń w inteligentnych budynkach.

![gl-s200 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

Należy pamiętać, że dołączony zasilacz zależy od kraju dostawy.

Opakowanie zawiera:

- 1 x Instrukcja obsługi
- 1 x GL-S200
- 1 x Kabel Ethernet
- 1 x Karta z podziękowaniem
- 1 x Karta gwarancyjna
- 1 x Zasilacz (wybrany typ wtyczki)

![gl-s200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/first_time_setup/s200_unboxing.jpg){class="glboxshadow"}

Obejrzyj [film z rozpakowywania](../../video_library/unboxing_first_set_up.md#gl-s200) GL-S200.

## Specyfikacja

[Specyfikacja GL-S200](https://www.gl-inet.com/products/gl-s200/#specs){target="_blank"}

## PCB Pinout

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="contentUrl" data-size="1500x1235">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="thumbnail" alt="gl-s200 pinout" loading="lazy" />
    </a>
  </figure>
</div>

## GL Thread Dev Board Pinout

![gl thread dev board pinout](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl_thread_dev_board_pinout.jpg){class="glboxshadow"}

---

## Pierwsza konfiguracja

Wszystkie routery GL.iNet mają podobny proces konfiguracji. [Kliknij tutaj, aby dowiedzieć się więcej o pierwszej konfiguracji](../../faq/first_time_setup.md/).

---

## INTERNET

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **INTERNET** w menu po lewej stronie.

Ta strona umożliwia wybór typu połączenia internetowego, takiego jak Ethernet, Repeater, Tethering i Cellular, zależnie od modelu.

W przypadku GL-S200 dostępne są dwa typy połączeń: Ethernet i Repeater.

### Ethernet

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet, aby uzyskać dostęp do Internetu. Ta metoda zwykle zapewnia najszybsze i najbardziej niezawodne połączenie z Internetem.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_ethernet.png){class="glboxshadow"}

### Repeater

Skonfiguruj router jako repeater, aby rozszerzyć zasięg istniejącej sieci Wi-Fi. W trybie repeatera urządzenie odbiera i retransmituje sygnał bezprzewodowy w swoim zasięgu, zwiększając tym samym obszar pokrycia. Ta metoda jest przydatna, gdy jeden router nie jest w stanie objąć zasięgiem całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z Internetem za pomocą istniejącej sieci Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_repeater.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi (np. Ethernet, Repeater) jednocześnie. Jeśli połączenie internetowe o najwyższym priorytecie przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Jest to również nazywane przełączeniem awaryjnym i zapewnia płynny, nieprzerwany dostęp do Internetu.

Przejdź do [Multi-WAN](../../interface_guide/multi-wan.md), aby ustawić priorytet każdego połączenia internetowego.

Alternatywnie możesz zmienić tryb Multi-WAN z Failover na Load Balance, co umożliwia jednoczesne korzystanie z wielu interfejsów sieciowych w celu zwiększenia całkowitej przepustowości routera.

---

## WIRELESS

Ustawienia sieci bezprzewodowej pozwalają zarządzać bezpieczeństwem głównej sieci Wi-Fi oraz sieci sieci Wi-Fi dla gości. Są dostępne po przejściu do **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS

Klienci to urządzenia podłączone do routera. Możesz blokować klientów lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu urządzeniami klienckimi.](../../interface_guide/clients.md)

---

## Thread Mesh

Zapoznaj się z dokumentacją [Thread Mesh](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/thread_mesh/) w IoT Docs.

---

## GL Dev Board

Zapoznaj się z dokumentacją [GL Dev Board](https://docs.gl-inet.com/iot/en/iot_dev_board/) w IoT Docs.

---

## Bluetooth

Zapoznaj się z dokumentacją [Bluetooth](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/bluetooth/) w IoT Docs.

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

### IPv6

Zapoznaj się z poradnikiem [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

Strona Mac Address wcześniej nazywała się Mac Clone, a od wersji v4.2 została zmieniona na Mac Address.

Zapoznaj się z poradnikiem [**MAC Address**](../../interface_guide/mac_address.md).

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

### Toggle Button Settings

Zapoznaj się z poradnikiem [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Zapoznaj się z poradnikiem [**Log**](../../interface_guide/log.md).

### Security

Ta funkcja jest dostępna od wersji v4.5.

Zapoznaj się z poradnikiem [**Security**](../../interface_guide/security.md).

### Reset Firmware

Zapoznaj się z poradnikiem [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Zapoznaj się z poradnikiem [**Advanced Settings**](../../interface_guide/advanced_settings.md).

