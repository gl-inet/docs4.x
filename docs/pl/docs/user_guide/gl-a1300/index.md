# Przewodnik użytkownika Slate Plus (GL-A1300)

## Opis produktu

Slate Plus (GL-A1300) to kieszonkowy router podróżny z wydajnym procesorem zoptymalizowanym pod kątem stabilności sieci i sprawnego szyfrowania VPN. Oferuje nasze najnowsze funkcje bezpieczeństwa i działa na najnowszej wersji systemu OpenWrt. Został zaprojektowany z myślą o osobach często podróżujących, które intensywnie korzystają z sieci VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

Pamiętaj, że zasilacz dołączony do zestawu zależy od kraju dostawy.

W opakowaniu znajdują się:

- 1 x instrukcja obsługi
- 1 x Slate Plus (GL-A1300)
- 1 x kabel Ethernet
- 1 x karta gwarancyjna
- 1 x zasilacz (wybrany typ wtyczki)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Wskaźniki LED

[Wskaźniki LED](../../faq/led.md#gl-a1300)

## Specyfikacja

[Specyfikacja GL-A1300](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

## Pierwsza konfiguracja

Wszystkie routery GL.iNet mają prosty i niemal identyczny proces konfiguracji. [Kliknij tutaj, aby dowiedzieć się więcej o pierwszej konfiguracji](../../faq/first_time_setup.md/).

Aby skonfigurować Slate Plus, możesz skorzystać z jednej z czterech obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering lub Cellular. Obejrzyj poniższy film instruktażowy.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## INTERNET

Interfejs konfiguracji internetu pozwala wybrać typ połączenia internetowego obsługiwany przez router.

Skonfiguruj połączenie z internetem, wybierając **INTERNET** w menu bocznym panelu administracyjnego routera.

Obsługiwane są cztery sposoby połączenia z internetem:

### Ethernet

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet. Ta metoda zazwyczaj zapewnia najszybsze i najbardziej niezawodne połączenie z internetem.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### Repeater

Rozszerz zasięg istniejącej sieci Wi-Fi, używając routera do odbierania sygnału bezprzewodowego w swoim zasięgu i przekazywania go dalej. Ta metoda jest najbardziej przydatna, gdy pojedynczy router nie obejmuje całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### Tethering

Udostępniaj połączenie internetowe podłączonym urządzeniom, przekazując dane komórkowe smartfona do routera przez kabel. Ta metoda jest najbardziej przydatna, gdy chcesz używać transmisji danych telefonu do dostępu do internetu.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### Cellular

Podłącz router do internetu, wkładając modem USB z obsługą sieci komórkowej do portu USB routera. Ta metoda jest najbardziej przydatna do współdzielenia internetu z modemu USB ze wszystkimi podłączonymi urządzeniami.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### Priorytet i równoważenie obciążenia

Przejdź do [Multi-WAN](../../interface_guide/multi-wan.md), aby ustawić priorytet każdej metody dostępu do internetu lub włączyć równoważenie obciążenia, gdy jednocześnie używanych jest kilka metod dostępu.

---

## WIRELESS

Ustawienia sieci bezprzewodowej pozwalają zarządzać zabezpieczeniami głównej sieci Wi‑Fi i sieci gościnnej. Możesz do nich przejść, wybierając **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS

Sekcja **CLIENTS** pokazuje urządzenia podłączone do routera. Możesz je blokować lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu urządzeniami klienckimi](../../interface_guide/clients.md)

---

## VPN

Routery GL.iNet mają fabrycznie zainstalowane OpenVPN i WireGuard®, obsługując ponad 30 usług VPN. Automatycznie szyfrują cały ruch sieciowy w podłączonej sieci, w tym urządzeń gościnnych i urządzeń klienckich, które same nie obsługują szyfrowania VPN. Nasze routery mogą także działać jako serwery VPN, przekierowując ruch z urządzeń klienckich w zdalnych lokalizacjach do serwera VPN przez tunel VPN przed uzyskaniem dostępu do publicznego internetu.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Skorzystaj z poniższych odnośników, aby przejść do instrukcji konfiguracji krok po kroku:

- [**Konfiguracja klienta OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Konfiguracja serwera OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Skorzystaj z poniższych odnośników, aby przejść do instrukcji konfiguracji krok po kroku:

- [**Konfiguracja klienta WireGuard**](../../interface_guide/wireguard_client.md)
- [**Konfiguracja serwera WireGuard**](../../interface_guide/wireguard_server.md)

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

### Parental Control

Przejdź do poradnika [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier

Przejdź do poradnika [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale

Przejdź do poradnika [**Tailscale**](../../interface_guide/tailscale.md).

---

## NETWORK

### Firewall

Routery GL.iNet oferują wiele funkcji zapory, które zapewniają bezpieczne połączenie i pełną kontrolę użytkownika. Umożliwiają konfigurowanie reguł zapory, w tym Port Forwarding, Open Ports i DMZ.

[Kliknij tutaj, aby dowiedzieć się więcej o zaporze w routerach GL.iNet](../../interface_guide/firewall.md)

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

Strona Mac Address wcześniej nazywała się Mac Clone i od wersji v4.2 została przemianowana na Mac Address.

Przejdź do poradnika [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Przejdź do poradnika [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Przejdź do poradnika [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Przejdź do poradnika [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet regularnie udostępnia aktualizacje oprogramowania układowego routerów, aby poprawiać wydajność, usuwać błędy i naprawiać podatności.

Przejdź do poradnika [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Przejdź do poradnika [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Ta funkcja została przeniesiona do [**Security**](../../interface_guide/security.md) od wersji v4.5.

Przejdź do poradnika [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Przejdź do poradnika [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings

Przejdź do poradnika [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Przejdź do poradnika [**Log**](../../interface_guide/log.md).

### Security

Ta funkcja jest dostępna od wersji v4.5.

Przejdź do poradnika [**Security**](../../interface_guide/security.md).

### Reset Firmware

Przejdź do poradnika [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Przejdź do poradnika [**Advanced Settings**](../../interface_guide/advanced_settings.md).
