# Przewodnik użytkownika Spitz AX (GL-X3000)

## Przegląd produktu

Spitz AX (GL-X3000) to bramka komórkowa Wi-Fi 6 z obsługą dwóch kart SIM, zaprojektowana z myślą o szybkim i niezawodnym połączeniu, szczególnie w odległych lokalizacjach i podczas podróży. Oferuje cztery metody dostępu do Internetu: Cellular (karty SIM), Ethernet, Repeater i Tethering. Obsługuje Multi-WAN (przełączenie awaryjne i równoważenie obciążenia), VPN (OpenVPN i WireGuard), kontrolę rodzicielską, AdGuard Home, przekierowanie portów, Tailscale i wiele więcej.

![x3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/hardware_info/gl-x3000_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Spitz AX (GL-X3000)
- 1 x instrukcja obsługi
- 1 x karta z podziękowaniem
- 1 x kabel Ethernet
- 1 x zestaw do montażu ściennego
- 1 x zasilacz
- 4 x adaptery

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/first_time_setup/x3000_unboxing.jpg){class="glboxshadow"}

## Wskaźniki LED

| Stan urządzenia                                  | Power                  | Internet               | 2.4GHz                 | 5GHz                   | Cellular               | 
| ------------------------------------------------ | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| Połączenie z Internetem (Cellular aktywny)        | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       |
| Połączenie z Internetem (Cellular nieaktywny)     | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | Wyłączona              |
| Brak połączenia z Internetem                      | Zielona — świeci       | Wyłączona              | Zielona — świeci       | Zielona — świeci       | Wyłączona              |
| Aktualizacja firmware                             | Zielona — świeci       | Miga co 0,5 s         | Miga co 0,5 s         | Miga co 0,5 s         | Zielona — świeci       | 
| Reset sieci (przytrzymaj reset < 3 s)             | Miga co 1 s           | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       |
| Reset fabryczny (przytrzymaj reset przez 10 s)    | Miga co 0,25 s        | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | Zielona — świeci       | 

**Wskazówka**: Gdy router jest połączony z Internetem, migająca dioda 2.4GHz lub 5GHz oznacza, że urządzenia Wi-Fi są podłączone i aktywnie przesyłają dane.

## Jak skonfigurować Spitz AX

Obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/64C7dqHG2EI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!! note "Przed rozpoczęciem wykonaj te kroki (jeśli łączysz się przez sieć komórkową)"

    Do połączenia z Internetem przez sieć komórkową wymagana jest co najmniej jedna karta nano SIM. Gdy masz już kartę (lub karty) nano SIM, wykonaj następujące kroki:
    
    1. Aktywuj kartę (karty) SIM, jeśli wymaga tego operator.
    2. Wyłącz router.
    3. Włóż kartę (karty) SIM do gniazd kart SIM. (**Uwaga:** W danym momencie aktywna jest tylko jedna karta SIM. Druga karta pełni jedynie funkcję zapasową.)

### 1. Włącz zasilanie

Złóż dwuczęściowy zasilacz. Podłącz go do routera, a następnie do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłącz urządzenie

Połącz urządzenie (np. komputer, laptop lub smartfon) z routerem przez Wi-Fi albo Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Zaloguj się do webowego panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz w pasku adresu `192.168.8.1` i zaloguj się. Wybierz język, ustaw hasło administratora, a następnie kliknij **Apply**.

Podczas potwierdzania ustawień Wi‑Fi pamiętaj, że po zmianie danych sieci Wi‑Fi trzeba będzie ponownie połączyć urządzenie z routerem przy użyciu zaktualizowanych danych logowania.

### 4. Konfiguracja Internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą webowego panelu administracyjnego GL.iNet. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Spitz AX, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Cellular, Ethernet, Repeater i Tethering. Jeśli chcesz używać funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_cellular.jpg){class="glboxshadow"}

    Jeśli karta SIM została już włożona do routera, połączenie z Internetem powinno zostać nawiązane automatycznie. (W sekcji Cellular powinna pojawić się nazwa operatora i zielona kropka.)
    
    Jeśli nie, kliknij opcję **Auto Setup**, gdy się pojawi.
    
    Szczegółowe instrukcje znajdziesz w poradniku [Jak połączyć się z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models).

    Dowiedz się, jak korzystać z fizycznej karty eSIM w routerze GL.iNet, [tutaj](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    W przypadku problemów zapoznaj się z [Przewodnikiem rozwiązywania problemów z siecią komórkową](../../faq/cellular_network_troubleshooting_guide.md).

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_ethernet.jpg){class="glboxshadow"}
    
    Połącz port WAN routera z urządzeniem nadrzędnym (np. modemem) za pomocą kabla Ethernet.
    
    Po pomyślnym połączeniu z Internetem w sekcji Ethernet na stronie **INTERNET** pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w poradniku [Jak połączyć się z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_repeater.jpg){class="glboxshadow"}

    1. Na stronie **INTERNET** w webowym panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wpisz hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z Internetem w sekcji Repeater na stronie **INTERNET** pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w poradniku [Jak połączyć się z Internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_tethering.jpg){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do **Settings** i włącz USB Tethering.
    3. Na stronie **INTERNET** w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering.
    
    Po pomyślnym połączeniu z Internetem w sekcji Tethering na stronie **INTERNET** pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w poradniku [Jak połączyć się z Internetem przez tethering USB](../../interface_guide/internet_tethering.md).

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany tunel między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN), a także umożliwia dostęp do sieci zdalnej (serwer VPN). Spitz AX (podobnie jak inne routery GL.iNet) obsługuje OpenVPN i WireGuard. Dodatkowo obsługuje także Tor.

=== "OpenVPN"

    Spitz AX (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Spitz AX (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na prywatność, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci, dzięki czemu śledzenie aktywności online jest utrudnione.
    
    * [Jak skonfigurować Tor](../../interface_guide/tor.md).

## Ustawienia sieci bezprzewodowej i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5 GHz i 2.4 GHz, w tym włączanie i wyłączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

    Aby skonfigurować Wireless, zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia blokowanie klienta i wykonywanie innych działań.

    Aby skonfigurować Clients, zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej zdalnej łączności i zdalnym zarządzaniu urządzeniami. Została opracowana specjalnie z myślą o integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią i przyszłemu wsparciu kontroli na poziomie sprzętowym AstroWarp oferuje bardziej solidne i niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci.
    
    Aby skonfigurować AstroWarp, zapoznaj się z poradnikiem [AstroWarp](../../interface_guide/astrowarp.md).

## Aplikacje

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie.
    
    Aby skonfigurować Plug-ins, zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to przydatne dla użytkowników, którzy potrzebują statycznego adresu IP, aby uzyskać dostęp do sieci zdalnej.
    
    Aby skonfigurować Dynamic DNS, zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Pamięć sieciowa to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich udostępnianie przez sieć.
    
    Aby skonfigurować pamięć sieciową, zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i trackerów, które pełni rolę serwera DNS i filtruje niepożądane treści na wszystkich urządzeniach podłączonych do sieci domowej.
    
    Aby skonfigurować AdGuard Home, zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control to zestaw ustawień umożliwiających zarządzanie urządzeniami dzieci i kontrolowanie ich działania. Obejmuje ograniczanie czasu spędzanego przed ekranem oraz blokowanie dostępu do wybranych treści.

    Aby skonfigurować Parental Control, zapoznaj się z poradnikiem [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieciowe definiowane programowo, które umożliwia tworzenie bezpiecznych, wirtualnych sieci przez Internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej.
    
    Aby skonfigurować ZeroTier, zapoznaj się z poradnikiem [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.
    
    Aby skonfigurować Tailscale, zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM Management"

    Aby dowiedzieć się, jak skonfigurować i zarządzać eSIM na swoim urządzeniu, zapoznaj się z [tym poradnikiem](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Ustawienia sieci

=== "Przekierowanie portów"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej. Aby skonfigurować przekierowanie portów, zapoznaj się z poradnikiem [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi jednocześnie (np. komórkowym, przez repeater i Ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.
    
    Aby skonfigurować LAN, zapoznaj się z poradnikiem [Lan Tutorial](../../interface_guide/lan.md).

---

=== "Sieć gościnna"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz konfigurację ustawień zabezpieczeń, takich jak izolacja AP dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z poradnikiem [Lan Tutorial](../../interface_guide/guest_network.md).

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i nadpisanie ustawień DNS wszystkich klientów, zezwolenie, aby niestandardowy DNS zastępował DNS VPN, a także ustawienie trybu konfiguracji serwera DNS na automatyczny lub ręczne wskazanie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN na Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Aby zarządzać portami Ethernet, zapoznaj się z poradnikiem [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Tryb sieci"

    Tryb sieci odnosi się do ustawień konfiguracyjnych określających, w jaki sposób urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami.
    
    Aby skonfigurować tryb sieci, zapoznaj się z poradnikiem [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając przydzielenie praktycznie nieograniczonej liczby unikalnych adresów IP, co jest niezbędne wobec stale rosnącej liczby urządzeń podłączonych do Internetu.
    
    Aby skonfigurować IPv6, zapoznaj się z poradnikiem [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o takie funkcje jak AdGuard Home, szyfrowany DNS i VPN.
    
    Aby skonfigurować Drop-in Gateway, zapoznaj się z poradnikiem [Jak skonfigurować Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.
    
    Aby skonfigurować IGMP Snooping, zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Przyspieszenie sieci"

    Przyspieszenie sprzętowe polega na wykorzystaniu specjalizowanych komponentów sprzętowych do efektywniejszego wykonywania określonych zadań niż procesory ogólnego przeznaczenia.
    
    Aby skonfigurować przyspieszenie sieci, zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "Ustawienia NAT"

    Strona NAT Settings umożliwia włączenie lub wyłączenie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zapoznaj się z poradnikiem [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemu

=== "Przegląd"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i jego parametrów wydajnościowych. Na tej stronie możesz sprawdzić:

    * CPU Average Load: monitoruj średnie obciążenie procesora routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: sprawdź, ile pamięci routera jest aktualnie używane, co ułatwia zarządzanie zasobami.
    * LED Control: włączaj lub wyłączaj diody LED routera, dostosowując sposób sygnalizacji urządzenia.
    * Flash Usage: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, hostname, model, architekturę, wersję OpenWrt, wersję jądra, identyfikator urządzenia, adres MAC urządzenia i numer seryjny.
    * External Storage: sprawdź stan zewnętrznych nośników danych podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają niezbędny wgląd i kontrolę, pomagając skutecznie zarządzać działaniem routera i je monitorować.

    Szczegółowe instrukcje znajdziesz w poradniku [Overview](../../interface_guide/system_overview.md).

=== "Aktualizacja"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje następujące opcje aktualizacji:

    * Firmware Online Upgrade: automatycznie sprawdza dostępność najnowszej wersji firmware na serwerze producenta i instaluje ją, upraszczając cały proces.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera, dzięki czemu masz kontrolę nad wersją i momentem aktualizacji.
    * Module Online Upgrade: automatycznie sprawdza dostępność najnowszej wersji modułu 4G/5G na serwerze producenta i instaluje ją, upraszczając cały proces.
    * Module Local Upgrade: umożliwia ręczne przesłanie pliku modułu z komputera w celu aktualizacji modułu 4G/5G.

    Dzięki tym opcjom możesz utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w poradniku [Upgrade](../../interface_guide/upgrade.md).

=== "Zaplanowane zadania"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera według zdefiniowanego harmonogramu, co zwiększa wygodę i efektywność. Kluczowe funkcje na tej stronie obejmują:

    * LED Display Schedule: ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w określonych godzinach.
    * Schedule Reboot: skonfiguruj automatyczne ponowne uruchamianie routera w określonych odstępach czasu, aby utrzymać optymalną wydajność i stabilność.
    * 5GHz Wi-Fi Status Schedule: ustaw harmonogram sterowania pasmem Wi-Fi 5GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    * 2.4GHz Wi-Fi Status Schedule: ustaw harmonogram sterowania pasmem Wi-Fi 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu dają większą kontrolę nad działaniem routera i pomagają dopasować jego pracę do konkretnych potrzeb.

    Szczegółowe instrukcje znajdziesz w poradniku [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Strefa czasowa"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe będą oznaczane zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla zachowania dokładnych zapisów i prawidłowego działania konfiguracji zależnych od czasu.

    Szczegółowe instrukcje znajdziesz w poradniku [Time Zone](../../interface_guide/time_zone.md).

=== "Logi"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania routera i zdarzenia, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Ta strona obejmuje:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem jądra systemu.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, opisujące ruch WWW i operacje serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez wsparcie techniczne. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w poradniku [Log](../../interface_guide/log.md).

=== "Bezpieczeństwo"

    Strona Security umożliwia skonfigurowanie różnych ustawień bezpieczeństwa, aby chronić sieć i router przed nieautoryzowanym dostępem. Ta strona obejmuje opcje:

    * Admin Password: ustaw lub zmień hasło do interfejsu administracyjnego routera, aby tylko upoważnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i ograniczaj go.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera z lokalizacji zdalnych przez Internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki bezpieczeństwa i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w poradniku [Security](../../interface_guide/security.md).

---

=== "Resetowanie firmware"

    Strona Reset Firmware umożliwia zresetowanie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć pracę od nowa z domyślną konfiguracją bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w poradniku [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Ustawienia zaawansowane"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółową konfigurację sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Szczegółowe instrukcje znajdziesz w poradniku [Advanced Settings](../../interface_guide/advanced_settings.md).