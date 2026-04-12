# Podręcznik użytkownika Mudi V2 (GL-E750V2)

**Uwaga:** Mudi V2 (GL-E750V2) i Mudi (GL-E750) działają na tym samym firmware. Jeśli używasz Mudi (GL-E750), [zaktualizuj firmware](https://dl.gl-inet.com/?model=e750), aby korzystać z najnowszych funkcji i możliwości.

## Przegląd produktu

Mudi V2 (GL-E750V2) to przenośny router podróżny 4G LTE zgodny z operatorami na całym świecie. Działa w pełni w oparciu o otwarte oprogramowanie OpenWrt i SDK 4.0 od GL.iNet, oferując rozbudowane możliwości dostosowania oraz szeroki zestaw funkcji. Mudi V2 (GL-E750V2) obsługuje prędkości Wi-Fi 300Mbps (2.4GHz) i 433Mbps (5GHz) oraz kartę MicroSD o pojemności do 1TB. Ma wbudowaną baterię 7000mAh. Obsługuje także multi-WAN (przełączenie awaryjne i równoważenie obciążenia), aby zapewnić stabilne połączenie wszystkim urządzeniom. 

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Przycisk

- Naciśnij przycisk zasilania przez **3 sekundy**: włącz urządzenie.

- Naciśnij przycisk zasilania przez **3-5 sekund**: przejdź do trybu czuwania.

- Naciśnij przycisk zasilania przez **ponad 5 sekund**: wyłącz urządzenie. 

    (Po naciśnięciu przez 3 sekundy ekran OLED najpierw wyświetli komunikat „Standby Mode On”. PRZYTRZYMUJ DALEJ przycisk zasilania, aż pod napisem „Standby Mode On” pojawi się „Shut Down”. Następnie rozpocznie się 3-sekundowe odliczanie i urządzenie się wyłączy.)

## Tryb czuwania

W trybie czuwania Mudi V2 (GL-E750V2) wyłącza Wi-Fi i 4G, aby oszczędzać energię. W tym trybie nie można połączyć się z Mudi V2 (GL-E750V2).

Aby włączyć lub wyłączyć tryb czuwania, naciśnij przycisk zasilania przez 3 sekundy. Na ekranie OLED zobaczysz komunikat „Standby Mode On” lub „Standby Mode Off”.

## Zawartość opakowania

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x przenośny router 4G LTE Mudi V2 (GL-E750V2)
- 1 x zasilacz 
- 4 x przejściówki (wtyczki US, EU, UK i AU)
- 1 x instrukcja obsługi
- 1 x karta gwarancyjna
- 1 x kabel Ethernet
- 1 x replikator portów USB-C 
- 1 x kabel USB-C do USB-C
- 1 x kabel USB-A do USB-C
- 1 x etui
- 1 x karta z podziękowaniem

---

## Pierwsze uruchomienie

Obejrzyj ten film lub wykonaj poniższe kroki, aby skonfigurować Mudi V2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włóż kartę SIM

Włóż kartę SIM oraz opcjonalną kartę MicroSD do Mudi V2 (GL-E750V2).

Uwaga: jeśli używasz karty SIM, musisz włożyć ją do urządzenia przed jego włączeniem. 

1. Obróć Mudi V2 (GL-E750V2) tylną stroną do góry.
2. Włóż palec w otwór przy krawędzi pokrywy.
3. Przesuwaj palec wzdłuż krawędzi.
4. Gdy pokrywa lekko się uniesie (mniej więcej z 25 do 30 stopni), pociągnij ją do góry, aby otworzyć obudowę.
5. Włóż kartę do gniazda zgodnie z oznaczeniem przy rogu.
6. Dociśnij pokrywę, aby zamknąć osłonę.

### 2. Włącz urządzenie

Naciśnij przycisk zasilania, aby włączyć urządzenie.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_power-on.png){class="glboxshadow"}

Gdy Mudi V2 (GL-E750V2) jest wyłączony, nadal możesz sprawdzić stan baterii, naciskając przycisk zasilania. Po naciśnięciu przycisku ekran LED pokaże stan baterii.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_battery.png){class="glboxshadow"}

Upewnij się, że używasz standardowego zasilacza 5V/2A. W przeciwnym razie urządzenie może działać nieprawidłowo.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET

Zaloguj się do panelu administracyjnego routera, a następnie przejdź do **INTERNET** w menu po lewej stronie. 

Ta strona umożliwia wybór typu połączenia z internetem, takiego jak Ethernet, Repeater, Tethering i Cellular.

### Ethernet

Podłącz router do aktywnego modemu lub aktywnego urządzenia sieciowego za pomocą kabla Ethernet, aby uzyskać dostęp do internetu. Ta metoda zazwyczaj zapewnia najszybsze i najbardziej niezawodne połączenie z internetem.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

Skonfiguruj router jako repeater, aby rozszerzyć zasięg istniejącej sieci Wi-Fi. W trybie repeatera urządzenie odbiera i retransmituje sygnały bezprzewodowe w swoim zasięgu, zwiększając obszar pokrycia. Ta metoda jest przydatna, gdy pojedynczy router nie obejmuje całego obszaru użytkowania.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

Podłącz port USB routera do smartfona z aktywną transmisją danych komórkowych za pomocą kabla USB, aby uzyskać dostęp do internetu. Ta metoda umożliwia wielu urządzeniom podłączonym do routera korzystanie z internetu z użyciem danych komórkowych smartfona.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular
 
Zdejmij tylną pokrywę Mudi V2 i włóż kartę SIM do gniazda SIM, aby połączyć urządzenie z internetem. Ta metoda jest przydatna, gdy chcesz udostępnić internet z jednej karty SIM wszystkim podłączonym urządzeniom.

[Kliknij tutaj, aby dowiedzieć się, jak połączyć się z internetem przez sieć komórkową](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

Aby używać fizycznej karty eSIM w routerze GL.iNet, kliknij tutaj: [Jak korzystać z fizycznej karty eSIM w routerach GL.iNet?](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

---

## WIRELESS

Ustawienia sieci bezprzewodowej umożliwiają zarządzanie zabezpieczeniami głównej sieci Wi-Fi i sieci Wi-Fi dla gości. Są dostępne po przejściu do **WIRELESS** w menu bocznym.

[Kliknij tutaj, aby dowiedzieć się więcej o konfiguracji sieci bezprzewodowej](../../interface_guide/wireless.md)

---

## CLIENTS

Klienci to urządzenia podłączone do routera. Możesz je blokować lub ograniczać ich prędkość sieciową. Interfejs jest dostępny po kliknięciu **CLIENTS** w menu bocznym panelu administracyjnego routera.

[Kliknij tutaj, aby dowiedzieć się więcej o zarządzaniu klientami urządzeń.](../../interface_guide/clients.md)

---

## VPN

Routery GL.iNet mają fabrycznie zainstalowane OpenVPN i WireGuard®, obsługując ponad 30 usług VPN. Automatycznie szyfrują cały ruch sieciowy w podłączonej sieci, w tym ruch urządzeń gościnnych i urządzeń klienckich, które same nie obsługują szyfrowania VPN. Nasze routery mogą także działać jako serwery VPN, przekierowując ruch z urządzeń klienckich w zdalnych lokalizacjach do serwera VPN przez tunel VPN przed uzyskaniem dostępu do publicznego internetu.

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

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

Routery GL.iNet oferują szeroki zakres dodatkowych funkcji, które upraszczają zarządzanie urządzeniami, poprawiają komfort korzystania z internetu, automatyzują aktualizacje firmware i nie tylko.

### Plug-ins

Przejdź do poradnika [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Przejdź do poradnika [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Przejdź do poradnika [**GoodCloud**](../../interface_guide/cloud.md).

---

## NETWORK

### Firewall

Routery GL.iNet oferują wiele funkcji zapory, które zapewniają bezpieczne połączenie i pełną kontrolę użytkownika. Umożliwiają one konfigurowanie reguł zapory, w tym Port Forwarding, Open Ports i DMZ.

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

Strona Mac Address była wcześniej nazywana Mac Clone i od wersji v4.2 nosi nazwę Mac Address.

Przejdź do poradnika [**MAC Address**](../../interface_guide/mac_address.md).

### IGMP Snooping

Przejdź do poradnika [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Przejdź do poradnika [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet regularnie udostępnia aktualizacje firmware swoich routerów, aby poprawiać wydajność, usuwać błędy i naprawiać luki w zabezpieczeniach.

Przejdź do poradnika [**Upgrade**](../../interface_guide/upgrade.md).

### OLED Screen Settings

Na tej stronie możesz dostosować informacje wyświetlane na ekranie OLED Mudi V2 (GL-E750V2). 


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

### Reset Firmware

Przejdź do poradnika [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Przejdź do poradnika [**Advanced Settings**](../../interface_guide/advanced_settings.md).


