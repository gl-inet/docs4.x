# Przewodnik użytkownika Slate 7 Pro (GL-BE10000)

## Przegląd produktu

Slate 7 Pro (GL-BE10000) to przenośny, trójpasmowy router podróżny Wi‑Fi 7. Jako ulepszona wersja Slate 7 (GL-BE3600) ma większy ekran dotykowy na górze obudowy oraz 1 GB pamięci DDR4 RAM i 8 GB pamięci eMMC, co zapewnia stabilną pracę i zgodność z wtyczkami. Oferuje wysoką wydajność VPN — do 1100 Mb/s dla WireGuard® i 1000 Mb/s dla OpenVPN-DCO. Dzięki 2 portom Ethernet 2.5G (1 WAN + 1 LAN), 1 portowi USB-C 3.0 i obsłudze zasilania PD zapewnia wygodną i niezawodną łączność w podróży i zastosowaniach mobilnych.

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## Zawartość opakowania

W opakowaniu znajdują się:

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x instrukcja obsługi
- 1 x karta z podziękowaniem
- 1 x kabel Ethernet
- 1 x kabel zasilający
- 1 x zasilacz
- 4 x przejściówki (wtyki US, EU, UK i AU)

## Jak skonfigurować Slate 7 Pro

Aby skonfigurować Slate 7 Pro, skorzystaj z jednej z czterech obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Wykonaj poniższe kroki.

### 1. Włącz zasilanie

Połącz dwie części zasilacza. Podłącz go do routera i do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Ekran dotykowy

Po włączeniu routera na ekranie pojawi się logo GL.iNet, a następnie pasek postępu uruchamiania.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){class="glboxshadow" width="360"}

Gdy pasek postępu zostanie całkowicie wypełniony, urządzenie zakończy uruchamianie i wyświetli ekran powitalny. Postępuj zgodnie z komunikatami, aby ustawić hasło administratora i sieć Wi‑Fi.

![set admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){class="glboxshadow" width="360"}

![set WiFi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){class="glboxshadow" width="360"}

Następnie przejdziesz do ekranu głównego. Po lewej stronie wyświetlane są informacje systemowe w czasie rzeczywistym, w tym czas systemowy i prędkość sieci, a także kafelki skrótów do Wi‑Fi, Clients, VPN i innych funkcji. Po prawej stronie znajdują się kafelki skrótów do czterech trybów połączenia: Ethernet, Repeater, Tethering i Cellular.

![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){class="glboxshadow" width="360"}

Różne kolory czterech kafelków skrótów oznaczają różny stan sieci.

![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){class="glboxshadow" width="360"}

- **Niebieski**: aktywne / połączone z internetem
- **Żółty**: łączenie / problem z siecią
- **Biały**: połączenie nieaktywne

### 3. Podłącz urządzenie

Połącz urządzenie (np. komputer, laptop lub smartfon) z routerem przez Wi‑Fi albo Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi‑Fi

    Na swoim urządzeniu znajdź nazwę sieci Wi‑Fi routera na liście dostępnych sieci i wpisz hasło, aby do niej dołączyć. Domyślna nazwa sieci (SSID) i hasło są wydrukowane na etykiecie routera.

### 4. Zaloguj się do web Admin Panel

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

### 5. Konfiguracja internetu

Skonfiguruj Slate 7 Pro, korzystając z jednej z obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}

    1. Podłącz port WAN urządzenia Slate 7 Pro do urządzenia nadrzędnego (np. modemu operatora, przełącznika sieciowego albo gniazda Ethernet w ścianie) za pomocą kabla Ethernet.
    2. Slate 7 Pro automatycznie spróbuje pobrać parametry sieciowe, takie jak adres IP, brama i serwer DNS, aby nawiązać połączenie Ethernet.
    3. Po pomyślnym połączeniu z internetem sekcja Ethernet na ekranie głównym stanie się niebieska (aktywna). Możesz dotknąć pozycji Ethernet na ekranie głównym albo zalogować się do web Admin Panel, aby sprawdzić szczegóły połączenia.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. Dotknij **Repeater** na ekranie dotykowym. Router rozpocznie skanowanie dostępnych sieci Wi‑Fi.
    2. Wybierz sieć Wi‑Fi, której zasięg ma rozszerzać Slate 7 Pro.
    3. Wpisz hasło i dotknij **Apply**.
    4. Po pomyślnym połączeniu z internetem sekcja Repeater na ekranie głównym stanie się niebieska (aktywna). Możesz dotknąć pozycji Repeater na ekranie głównym albo zalogować się do web Admin Panel, aby sprawdzić szczegóły połączenia.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon albo modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Ustawień i włącz **USB Tethering** albo **Personal Hotspot**. W przypadku iPhone'a stuknij **Trust This Device**, jeśli pojawi się taki komunikat.
    3. Na ekranie dotykowym wybierz **Tethering** i dotknij **Connect**. Router połączy się z Twoim urządzeniem.
    4. Po pomyślnym połączeniu z internetem sekcja Tethering na ekranie głównym stanie się niebieska (aktywna). Możesz dotknąć pozycji Tethering na ekranie głównym albo zalogować się do web Admin Panel, aby sprawdzić szczegóły połączenia.

    **Uwaga**: Jeśli połączenie się nie powiedzie, upewnij się, że napięcie zasilania wynosi co najmniej 9V 3A, ponieważ zbyt niskie zasilanie może uniemożliwić uruchomienie portu USB. Powtórz powyższe kroki albo zaloguj się do web Admin Panel, aby sprawdzić stan połączenia Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. Podłącz modem USB sieci komórkowej do portu USB Slate 7 Pro. To przydatne rozwiązanie, jeśli chcesz udostępnić internet z modemu USB wszystkim podłączonym urządzeniom.
    2. Po pomyślnym połączeniu z internetem sekcja Cellular na ekranie głównym stanie się niebieska (aktywna). Możesz dotknąć pozycji Cellular na ekranie głównym albo zalogować się do web Admin Panel, aby sprawdzić szczegóły połączenia.

---

Poniżej znajdziesz omówienie funkcji dostępnych w web Admin Panel Slate 7 Pro.

## Wireless 

Strona Wireless umożliwia konfigurację ustawień sieci Wi‑Fi 6 GHz, 5 GHz i 2,4 GHz, w tym włączanie Wi‑Fi, ustawianie mocy TX, określanie nazwy sieci Wi‑Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi‑Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi‑Fi, szerokości pasma i kanału.

Dodatkowo Slate 7 Pro obsługuje MLO Wi‑Fi, czyli Multi-Link Operation, które łączy jednocześnie wiele sieci bezprzewodowych, aby zapewnić większą przepustowość i bardziej niezawodne połączenia.

Aby skonfigurować Wireless, zapoznaj się z [Wireless](../../interface_guide/wireless.md).

## Clients

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

Aby skonfigurować Clients, zapoznaj się z [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.

    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana funkcja sieciowa zintegrowana z routerami GL.iNet. Umożliwia wygodny zdalny dostęp do sieci domowej bez rejestracji i logowania. Korzysta z protokołu AmneziaWG z wbudowanym maskowaniem ruchu, dzięki czemu połączenie pozostaje stabilne i bezpieczne, dlatego AstroWarp świetnie sprawdza się jako rozwiązanie do niezawodnego zdalnego dostępu z dowolnego miejsca. Użytkownicy mogą skonfigurować sieć AstroWarp bezpośrednio z poziomu panelu administracyjnego routera GL.iNet. Wystarczy sparować routery przy użyciu kodu dostępu, aby bezpiecznie połączyć router podróżny z siecią domową w kilka sekund.

    Aby skonfigurować AstroWarp, zapoznaj się z [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Slate 7 Pro obsługuje protokoły OpenVPN i WireGuard.

=== "OpenVPN" 

    Slate 7 Pro (podobnie jak inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z tych instrukcji:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 Pro (podobnie jak inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką szybkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z tych instrukcji:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia jednoczesne skonfigurowanie routera z wieloma połączeniami internetowymi (np. Cellular, Repeater i Ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.

    Aby skonfigurować LAN, zapoznaj się z [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 albo 10.0.0.0/8, określenie adresów IP bramy i maski podsieci oraz konfigurację ustawień bezpieczeństwa, takich jak izolacja AP dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i zastąpienie ustawień DNS wszystkich klientów, zezwolenie, aby niestandardowy DNS zastępował DNS VPN, oraz ustawienie trybu konfiguracji serwera DNS na automatyczny albo ręczne określenie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN na Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Aby zarządzać portami Ethernet, zapoznaj się z [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Oferuje znacznie większą przestrzeń adresową, co pozwala obsłużyć praktycznie nieograniczoną liczbę unikalnych adresów IP, niezbędną przy stale rosnącej liczbie urządzeń podłączonych do internetu.

    Aby skonfigurować IPV6, zapoznaj się z [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania i kontrolowania ruchu multicast.

    Aby skonfigurować IGMP snooping, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Tryb sieciowy odnosi się do ustawień konfiguracji określających sposób, w jaki urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami.

    Aby skonfigurować tryb sieciowy, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera, oferując m.in. AdGuard Home, szyfrowany DNS i klienta VPN.

    Aby skonfigurować Drop-in Gateway, skorzystaj z poniższych linków:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.

    Aby skonfigurować Network Acceleration, zapoznaj się z [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) to podstawowa funkcja inteligentnego zarządzania siecią. Pozwala przezwyciężyć ograniczenia tradycyjnych routerów, które identyfikują jedynie adresy źródłowe lub docelowe, analizować szczegółowo ładunek pakietów danych oraz dokładnie rozpoznawać aplikacje i strony internetowe odwiedzane przez użytkownika dzięki porównaniu z biblioteką sygnatur, co umożliwia precyzyjną klasyfikację i kontrolę ruchu.

    Zintegrowana z [Netify](https://www.netify.ai/){target="_blank"}, funkcja DPI GL.iNet wykorzystuje lekką wbudowaną wtyczkę, co pozwala na efektywne wdrożenie. Dzięki internetowo aktualizowanej bazie sygnatur Netify zapewnia niezawodne zarządzanie, sprawiając, że kontrola sieci jest dokładniejsza i bardziej efektywna.

    Szczegółowe instrukcje znajdziesz w [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics oferuje inteligentny pulpit analityczny ruchu, który kategoryzuje i wizualizuje wykorzystanie sieci według aplikacji, pomagając monitorować ruch w czasie rzeczywistym i historyczny, aby lepiej rozumieć oraz kontrolować działanie sieci.

    Szczegółowe instrukcje znajdziesz w [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter zapewnia inteligentną ochronę online dzięki klasyfikacji opartej na DPI, automatycznie blokując szkodliwe lub złośliwe strony internetowe, aby utrzymać sieć w czystości i bezpieczeństwie.

    Szczegółowe instrukcje znajdziesz w [Content Filter](../../interface_guide/content_filter.md).

---

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować ich działanie. Obejmuje ograniczanie czasu spędzanego przed ekranem oraz blokowanie dostępu do określonych treści.

    Aby skonfigurować kontrolę rodzicielską, zapoznaj się z [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) optymalizuje przydział przepustowości, nadając priorytet krytycznym aktywnościom (np. połączeniom wideo, grom) podczas przeciążenia sieci, zmniejszając opóźnienia i poprawiając ogólną wydajność sieci. Pamiętaj, że dotyczy to lokalnego ruchu urządzeń klienckich oraz ruchu tunelu klienta VPN, ale nie ruchu odbieranego, gdy router działa jako serwer VPN.

    Szczegółowe instrukcje znajdziesz w [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i „bufferbloat”, zapewniając płynniejsze granie i połączenia głosowe.

    Szczegółowe instrukcje znajdziesz w [SQM](../../interface_guide/sqm.md).

## Security

=== "Port Forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w internecie dostęp do urządzeń w sieci prywatnej.

    Aby skonfigurować port forwarding, zapoznaj się z [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Management Control umożliwia konfigurację różnych ustawień bezpieczeństwa w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Ta strona obejmuje następujące opcje:

    * Local Access Control: Zarządzanie dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej oraz jego ograniczanie.
    * Remote Access Control: Konfigurowanie i ograniczanie dostępu do interfejsu routera ze zdalnych lokalizacji przez internet, co zwiększa ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: Kontrola tego, które porty są otwarte na routerze, co ogranicza potencjalne podatności i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w [Security](../../interface_guide/security.md).

=== "NAT Mode"

    Strona NAT Mode umożliwia włączanie lub wyłączanie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Mode](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego możliwości.

    Aby skonfigurować wtyczki, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to szczególnie przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej.

    Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage oznacza scentralizowane rozwiązanie do przechowywania danych, które pozwala wielu użytkownikom i urządzeniom uzyskiwać dostęp do plików oraz udostępniać je przez sieć.

    Aby skonfigurować Network Storage, zapoznaj się z [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie do blokowania reklam i elementów śledzących w całej sieci, działające jako serwer DNS filtrujący niepożądane treści na wszystkich urządzeniach podłączonych do sieci domowej.

    Aby skonfigurować AdGuard Home, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.

    Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie typu software-defined networking, które umożliwia tworzenie bezpiecznych, wirtualnych sieci przez internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej.

    Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, skrót od The Onion Router, to sieć ukierunkowana na prywatność, umożliwiająca anonimową komunikację przez internet. Przekierowuje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania użytkownika, co utrudnia śledzenie aktywności online.

    * [Jak skonfigurować Tor](../../interface_guide/tor.md)

## System

=== "Overview"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i wskaźników wydajności. Na tej stronie możesz sprawdzić:

    * CPU Average Load: Monitorowanie średniego obciążenia CPU routera, co pomaga ocenić wydajność i wykryć potencjalne wąskie gardła.
    * Memory Usage: Sprawdzenie, jaka część pamięci routera jest wykorzystywana, co ułatwia zarządzanie zasobami.
    * LED Control: Włączanie i wyłączanie diod LED routera, co pozwala dostosować wizualne wskaźniki urządzenia.
    * Flash Usage: Wyświetlanie wykorzystania pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: Dostęp do szczegółowych informacji o systemie routera, w tym czasu działania, nazwy hosta, modelu, architektury, wersji OpenWrt, wersji jądra, identyfikatora urządzenia, adresu MAC urządzenia i numeru seryjnego.
    * External Storage: Sprawdzenie stanu zewnętrznych urządzeń pamięci podłączonych do routera, takich jak dyski USB.

    Funkcje te zapewniają najważniejsze informacje i elementy sterowania, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Szczegółowe instrukcje znajdziesz w [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Admin Password umożliwia ustawienie lub zmianę hasła interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.

    Ze względów bezpieczeństwa zalecamy włączenie opcji **Prevent Weak Password**.

    Gdy opcja **Prevent Weak Password** jest włączona, nowe hasła muszą spełniać następujące wymagania.

    * Co najmniej 5 znaków i maksymalnie 63 znaki.
    * Dozwolone są litery (z rozróżnieniem wielkości), cyfry i symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Wymagane są co najmniej dwie z następujących kategorii: wielkie litery, małe litery, cyfry i symbole.

    Szczegółowe instrukcje znajdziesz w [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: Automatyczne sprawdzanie i instalowanie najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: Ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, co daje większą kontrolę nad wersją i czasem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router na bieżąco z najnowszymi ulepszeniami i poprawkami.

    Szczegółowe instrukcje znajdziesz w [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera według z góry określonego harmonogramu, zwiększając wygodę i efektywność. Główne funkcje tej strony obejmują:

    * LCD Display Schedule: Ustawienie harmonogramu automatycznego włączania lub wyłączania ekranu LCD routera, co ogranicza emisję światła w określonych porach.
    * Schedule Reboot: Skonfigurowanie automatycznego restartu routera w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Wi‑Fi Status Schedule: Ustawienie harmonogramu sterowania pasmami Wi‑Fi 6GHz / 5GHz / 2.4GHz / MLO, co pozwala lepiej zarządzać dostępnością sieci i zużyciem energii.

    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera i pozwalają dopasować je do konkretnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Display Management"

    Strona Display Management zapewnia pełen zestaw funkcji do zarządzania ekranem dotykowym i powiązanymi ustawieniami.

    ‒ Wallpaper: Dostosowanie tapety i stylu wybudzania ekranu.
    ‒ Brightness: Regulacja jasności ekranu dotykowego. Użyj suwaka albo wpisz konkretną wartość procentową, aby dopasować jasność do różnych warunków oświetleniowych.
    ‒ Auto Lock: Ustawienie czasu, po którym ekran zostanie automatycznie zablokowany przy braku aktywności. Zakres wynosi od 1 do 30 minut.
    ‒ Screen Always On: Włączenie lub wyłączenie opcji, czy ekran dotykowy ma pozostawać stale włączony, czy wyłączać się po okresie bezczynności.
    ‒ Enable Screen Passcode: Ustawienie kodu blokady ekranu dotykowego jako dodatkowej warstwy zabezpieczeń.

    Szczegółowe instrukcje znajdziesz w [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe są oznaczane zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla zachowania dokładnych zapisów i prawidłowego działania konfiguracji zależnych od czasu.

    Szczegółowe instrukcje znajdziesz w [Time Zone](../../interface_guide/time_zone.md).

---

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia skonfigurowanie fizycznego przycisku przełączania w routerze, dzięki czemu możesz przypisać mu konkretne funkcje i korzystać z nich szybko oraz wygodnie. To rozwiązanie zapewnia praktyczne skróty do typowych zadań i ustawień, poprawiając komfort użytkowania i upraszczając zarządzanie routerem.

    Szczegółowe instrukcje znajdziesz w [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca domyślne ustawienia aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów albo gdy chcesz rozpocząć od nowa z domyślną konfiguracją bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, pomagając w rozwiązywaniu problemów i monitorowaniu wydajności. Ta strona obejmuje:

    * System Log: Szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: Dzienniki związane z działaniem jądra systemu i jego zdarzeniami.
    * Crash Log: Rejestry awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: Dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: Dzienniki serwera WWW Nginx, jeśli jest używany przez router, opisujące ruch sieciowy i działanie serwera.

    Dodatkowo strona oferuje przycisk Export Log, który pozwala wyeksportować wszystkie zebrane logi do analizy przez pomoc techniczną. Ta funkcja jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnego wsparcia.

    Szczegółowe instrukcje znajdziesz w [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom szczegółowe dostrojenie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółową konfigurację sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Szczegółowe instrukcje znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md).
