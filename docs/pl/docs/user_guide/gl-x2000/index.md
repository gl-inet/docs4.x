# Przewodnik użytkownika Spitz Plus (GL-X2000)

## Przegląd produktu

Spitz Plus (GL-X2000) to bramka komórkowa 4G LTE z obsługą dwóch kart SIM i Wi-Fi 6, zaprojektowana z myślą o szybkich i niezawodnych połączeniach — szczególnie na obszarach oddalonych i podczas podróży. Dzięki agregacji 3 pasm (3-Carrier Aggregation) router jednocześnie przesyła dane na trzech pasmach, zapewniając trzykrotnie większą dostępną przepustowość i unikając zatorów. Oferuje cztery metody dostępu do internetu: Cellular (karty SIM), Ethernet, Repeater i Tethering. Obsługuje Multi-WAN (przełączanie awaryjne i load balancing), VPN (OpenVPN i WireGuard), kontrolę rodzicielską, AdGuard Home, przekierowanie portów, Tailscale i wiele więcej.

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Spitz Plus (GL-X2000)
- 1 x Instrukcja obsługi
- 4 x Anteny zewnętrzne
- 1 x Karta z podziękowaniem
- 1 x Kabel Ethernet
- 1 x Zestaw montażowy na ścianę
- 1 x Podkładka samoprzylepna
- 4 x Śruby
- 1 x Zasilacz
- 1 x Przejściówka (zależnie od kraju dostawy)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_unboxing.jpg){class="glboxshadow"}

## Wskaźniki LED 

| Stan                                                                          | Zasilanie                            | Internet                    | 2.4GHz                      | 5GHz                        |Cellular | 
| ----------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | ------- |
| Normalny (połączony z internetem)                                             | Zielony                              | Zielony                     | Zielony                     | Zielony                     | Zielony |
| Brak połączenia z internetem                                                  | Zielony                              | Wyłączony                   | Zielony                     | Zielony                     | Zielony |
| Aktualizacja firmware                                                         | Zielony                              | Miga na zielono (co 0,5 s)  | Miga na zielono (co 0,5 s)  | Miga na zielono (co 0,5 s)  | Zielony | 
| Resetowanie routera (przytrzymaj przycisk „reset" ponad 3 s)                  | Miga na zielono (co 1 s)            | Zielony                     | Zielony                     | Zielony                     | Zielony |
| Przywracanie ustawień fabrycznych (przytrzymaj przycisk „reset" przez 10 s)   | Szybkie miganie na zielono (co 0,25 s) | Zielony                  | Zielony                     | Zielony                     | Zielony | 

## Jak skonfigurować Spitz Plus

Aby skonfigurować Spitz Plus, użyj jednej z czterech obsługiwanych metod połączenia z internetem: Cellular (wymagana karta SIM), Ethernet, Repeater i Tethering. Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Ten film przedstawia konfigurację Spitz Plus przez sieć komórkową. Jeśli chcesz skonfigurować Spitz Plus inną metodą połączenia, zapoznaj się z poniższymi krokami.)</small>

!!! note "Przed rozpoczęciem wykonaj następujące kroki (jeśli łączysz się przez sieć komórkową):"

    Do połączenia z internetem przez sieć komórkową wymagana jest co najmniej jedna karta nano SIM. Gdy masz już przygotowaną kartę (lub karty) nano SIM, wykonaj następujące kroki:
    
    1. Aktywuj kartę(-y) SIM, jeśli wymaga tego operator.
    2. Wyłącz router.
    3. Włóż kartę(-y) SIM do gniazd SIM. (**Uwaga:** W danym momencie aktywna jest tylko jedna karta SIM. Druga karta SIM pełni jedynie funkcję zapasową.)

### 1. Włącz zasilanie

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka elektrycznego. Router uruchomi się automatycznie.

### 2. Podłącz urządzenie

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet. 

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. (Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.)

    Na urządzeniu znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło, aby dołączyć do sieci. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Zaloguj się do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu — wejdziesz do panelu GL.iNet Web Admin Panel. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**. 

### 4. Konfiguracja internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą panelu GL.iNet Web Admin Panel. Jeśli wolisz używać aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Spitz Plus, korzystając z jednej z obsługiwanych metod połączenia z internetem: Cellular, Ethernet, Repeater i Tethering. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    Jeśli włożyłeś kartę SIM do routera, połączenie z internetem powinno zostać nawiązane automatycznie. Nazwa operatora SIM oraz zielona kropka powinny pojawić się w sekcji Cellular.
    
    Jeśli nie, wyłącz router, ponownie włóż kartę SIM i włącz go. 
    
    Szczegółowe instrukcje znajdziesz w [Połącz z internetem przez sieć komórkową](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models).

    **Uwaga**: Funkcja eSIM w Spitz Plus jest dostępna od wersji firmware v4.7 i nowszych. Dowiedz się, jak korzystać z fizycznej karty eSIM w routerze GL.iNet [tutaj](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    W razie problemów zapoznaj się z [Przewodnikiem rozwiązywania problemów z siecią komórkową](../../faq/cellular_network_troubleshooting_guide.md). 

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}
    
    Podłącz kabel Ethernet między portem WAN routera Spitz Plus a urządzeniem nadrzędnym (np. modemem). 
    
    Po pomyślnym połączeniu z internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. Na stronie INTERNET w panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci. 
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering. 
    3. Na stronie INTERNET w panelu administracyjnym kliknij **Connect** w sekcji Tethering. 
    
    Po pomyślnym połączeniu z internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z internetem przez tethering USB](../../interface_guide/internet_tethering.md).

---

Poniżej znajduje się przegląd funkcji dostępnych w panelu administracyjnym Spitz Plus.

## Wireless

Strona Wireless umożliwia konfigurację ustawień zarówno sieci Wi-Fi 5 GHz, jak i 2,4 GHz, w tym włączanie/wyłączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie/wyłączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi, ustawianie hasła Wi-Fi, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

Aby skonfigurować ustawienia Wireless, zobacz [Wireless](../../interface_guide/wireless.md).

## Clients

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę urządzenia, typ połączenia (tj. Ethernet lub Wi-Fi), adresy IP i MAC, szybkość pobierania i wysyłania, całkowity ruch oraz umożliwia rezerwację IP, zablokowanie klienta lub wykonanie innych działań.

Aby skonfigurować ustawienia Clients, zobacz [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi. 
    
    Aby skonfigurować GoodCloud, zobacz [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej zdalnej komunikacji sieciowej i zdalnym zarządzaniu urządzeniami. Została stworzona specjalnie do integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią i przyszłemu wsparciu dla sterowania na poziomie sprzętowym AstroWarp oferuje solidniejsze i bardziej niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci. 
    
    Aby skonfigurować AstroWarp, zobacz [AstroWarp](../../interface_guide/astrowarp.md).

    **Uwaga**: Aby korzystać z AstroWarp, zaktualizuj firmware Spitz Plus do wersji v4.8 lub nowszej.

## VPN 

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Spitz Plus obsługuje OpenVPN i WireGuard. 

=== "OpenVPN" 
    
    Spitz Plus (oraz inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [Jak skonfigurować serwer OpenVPN](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"
    
    Spitz Plus (oraz inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką szybkość i wygodę. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [Jak skonfigurować serwer WireGuard](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

## Aplikacje

=== "Plug-ins"

    Plug-in to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego działania. 
    
    Aby skonfigurować Plug-ins, zobacz [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej. 
    
    Aby skonfigurować Dynamic DNS, zobacz [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Magazyn sieciowy to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich udostępnianie przez sieć. 
    
    Aby skonfigurować magazyn sieciowy, zobacz [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to narzędzie firm trzecich, które blokuje reklamy i śledzenie, zapewniając Ci bezpieczeństwo. Aby dowiedzieć się, jak włączyć AdGuard Home, zobacz [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/). 

=== "Parental Control"

    Parental Control to zestaw ustawień zaprojektowanych, aby pomóc w zarządzaniu urządzeniami dzieci i kontrolowaniu ich. Obejmuje to ograniczanie czasu spędzanego przed ekranem oraz ograniczanie dostępu do określonych treści. Spitz Plus oferuje dwie opcje kontroli rodzicielskiej: wersję lokalną opracowaną przez GL.iNet oraz zintegrowaną wersję Bark — aplikacji do kontroli rodzicielskiej. 

    Aby skonfigurować kontrolę rodzicielską, zobacz [Parental controls](../../interface_guide/parental_control.md). 

=== "Tailscale"

    Spitz Plus obsługuje Tailscale od wersji firmware v4.7 i nowszych.
    
    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca. 
    
    Aby skonfigurować Tailscale, zobacz [Tailscale](../../interface_guide/parental_control.md). 

=== "eSIM"

    Spitz Plus obsługuje funkcję eSIM od wersji firmware v4.7 i nowszych. 
    
    Aby dowiedzieć się, jak skonfigurować i zarządzać eSIM na swoim urządzeniu, zapoznaj się z [tym poradnikiem](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
## Ustawienia sieci

=== "Port forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w internecie dostęp do urządzeń w sieci prywatnej. Aby skonfigurować przekierowanie portów, zobacz [Port Forwards](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards). 

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia jednoczesne skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Dzięki temu dostęp do internetu pozostaje płynny i nieprzerwany. 

    Aby skonfigurować Multi-WAN, zobacz [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą. 
    
    Aby skonfigurować LAN, zobacz [Lan Tutorial](../../interface_guide/lan.md). 

---

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz skonfigurowanie ustawień zabezpieczeń, takich jak izolacja AP dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zobacz [Lan Tutorial](../../interface_guide/guest_network.md). 

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i zastąpienie ustawień DNS wszystkich klientów, zezwolenie niestandardowemu DNS na zastępowanie DNS VPN oraz skonfigurowanie trybu ustawień serwera DNS jako automatycznego lub ręczne określenie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zobacz [DNS](../../interface_guide/dns.md).

=== "Port Management"

    Strona Port Management umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie wynegocjowanej szybkości portu sieciowego.

    Aby zarządzać portami Ethernet, zobacz [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Tryb sieci odnosi się do ustawień konfiguracyjnych określających, w jaki sposób urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami. 
    
    Aby skonfigurować tryb sieci, zobacz [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając użycie praktycznie nieograniczonej liczby unikalnych adresów IP, co jest niezbędne przy stale rosnącej liczbie urządzeń podłączonych do internetu. 
    
    Aby skonfigurować IPV6, zobacz [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może on nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN. Aby skonfigurować Drop-in Gateway, zobacz [Jak skonfigurować Drop-in Gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/). 

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i kontrolowania go. 
    
    Aby skonfigurować IGMP snooping, zobacz [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Akceleracja sprzętowa polega na wykorzystaniu wyspecjalizowanych komponentów sprzętowych do wydajniejszego wykonywania określonych zadań niż procesory ogólnego przeznaczenia. 
    
    Aby skonfigurować akcelerację sieci, zobacz [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączenie lub wyłączenie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zobacz [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemu

=== "Overview"

    Strona Overview zapewnia kompleksowy wgląd w bieżący stan routera i jego wskaźniki wydajności. Na tej stronie możesz zobaczyć:

    * CPU Average Load: monitoruj średnie obciążenie CPU routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: sprawdź, jaka część pamięci routera jest używana, co pomaga w zarządzaniu zasobami.
    * LED Control: włączaj lub wyłączaj diody LED routera, dostosowując wskaźniki świetlne urządzenia.
    * Flash Usage: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, hostname, model, architekturę, wersję OpenWrt, wersję kernela, ID urządzenia, MAC urządzenia i S/N urządzenia.
    * External Storage: sprawdź stan zewnętrznych urządzeń pamięci masowej podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają kluczowe informacje i mechanizmy sterowania, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Szczegółowe instrukcje znajdziesz w [Overview](../../interface_guide/system_overview.md){target="_blank"}.

=== "Upgrade"

    Strona Upgrade służy do aktualizowania firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje następujące opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie i instalowanie najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, co daje kontrolę nad wersją aktualizacji i momentem jej wykonania.
    * Module Online Upgrade: automatyczne sprawdzanie i instalowanie najnowszej wersji modułu 4G/5G bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Module Local Upgrade: ręczne przesłanie pliku modułu z komputera w celu aktualizacji modułu 4G/5G.

    Opcje te pozwalają utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w [Upgrade](../../interface_guide/upgrade.md){target="_blank"}.

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * LED Display Schedule: ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć zanieczyszczenie światłem w określonych godzinach.
    * Schedule Reboot: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Wi-Fi Status Schedule: ustaw harmonogram sterowania pasmem Wi-Fi 5GHz / 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu można dopasować je do własnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie właściwej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe będą poprawnie oznaczane zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych rejestrów oraz prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Ta strona obejmuje:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem kernela i jego zdarzeniami.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, zawierające szczegóły ruchu internetowego i działania serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez pomoc techniczną. Ta funkcja jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w [Log](../../interface_guide/log.md){target="_blank"}.

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień zabezpieczeń, aby chronić sieć i router przed nieautoryzowanym dostępem. Ta strona zawiera opcje takie jak:

    * Admin Password: ustaw lub zmień hasło do interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i ograniczaj go.
    * Remote Access Control: skonfiguruj i ogranicz dostęp do interfejsu routera z lokalizacji zdalnych przez internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne podatności i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    Strona Reset Firmware umożliwia zresetowanie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub przy rozpoczynaniu pracy od nowa z domyślną konfiguracją bieżącej wersji firmware.

    Szczegółowe instrukcje znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"}.

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji za pośrednictwem interfejsu OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory oraz inne zaawansowane dostosowania systemowe.

    Szczegółowe instrukcje znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}.
