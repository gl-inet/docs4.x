# Przewodnik użytkownika Puli AX (GL-XE3000)

## Przegląd produktu

Puli AX (GL-XE3000) to najwyższej klasy router komórkowy 5G z Wi-Fi 6, który przenosi szybkość internetu na zupełnie nowy poziom! Dzięki wbudowanemu akumulatorowi o pojemności 6400 mAh / 7,4 V / 47,4 Wh możesz cieszyć się nieprzerwanym połączeniem internetowym jeszcze dłużej. Osiąga błyskawiczne prędkości Wi-Fi do 574 Mbps (2.4GHz) i 2402 Mbps (5GHz), z łączną maksymalną prędkością Wi-Fi wynoszącą 3000 Mbps. Wyposażony w moduł 5G NR zapewnia ciągłość połączenia z internetem, nawet w przypadku awarii łącza Ethernet.

![xe3000_interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/hardware_info/xe3000_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Puli AX (GL-XE3000)
- 1 x Instrukcja obsługi
- 1 x Karta z podziękowaniem
- 1 x Kabel Ethernet
- 1 x Zestaw montażowy na ścianę
- 1 x Zasilacz
- 4 x Przejściówki

![xe3000_unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/first_time_setup/xe3000_unboxing.jpg){class="glboxshadow"}

## Wskaźniki LED 

[Stan wskaźników LED](../../faq/led.md#gl-xe3000){target="_blank"}

## Jak skonfigurować Puli AX

Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/N-p9NaXZmIM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!! note "Przed rozpoczęciem wykonaj następujące kroki (jeśli łączysz się przez sieć komórkową)"

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

    Na urządzeniu znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Zaloguj się do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**. 

Podczas potwierdzania danych Wi‑Fi pamiętaj, że jeśli zmienisz informacje o Wi‑Fi, musisz ponownie połączyć urządzenie z siecią Wi‑Fi routera, używając zaktualizowanych danych logowania.

### 4. Konfiguracja internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą panelu GL.iNet Web Admin Panel. Jeśli wolisz używać aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Puli AX, korzystając z jednej z obsługiwanych metod połączenia z internetem: Cellular, Ethernet, Repeater i Tethering. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_cellular.png){class="glboxshadow"}

    Jeśli włożyłeś już kartę SIM do routera, połączenie z internetem powinno zostać nawiązane automatycznie. Nazwa operatora SIM oraz zielona kropka powinny pojawić się w sekcji Cellular. 
    
    Jeśli nie, wyłącz router, ponownie włóż kartę SIM i włącz go.
    
    Szczegółowe instrukcje znajdziesz w [Połącz z internetem przez sieć komórkową](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models).

    Dowiedz się, jak korzystać z fizycznej karty eSIM w routerze GL.iNet [tutaj](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    W razie problemów zapoznaj się z [Przewodnikiem rozwiązywania problemów z siecią komórkową](../../faq/cellular_network_troubleshooting_guide.md). 

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_ethernet.png){class="glboxshadow"}
    
    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem. 

    Po pomyślnym połączeniu z internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci. 
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering. 
    3. Na stronie INTERNET w panelu administracyjnym kliknij **Connect** w sekcji Tethering.  
    
    Po pomyślnym połączeniu z internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z internetem przez tethering USB](../../interface_guide/internet_tethering.md).

---

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Puli AX (oraz inne routery GL.iNet) obsługuje OpenVPN i WireGuard. Dodatkowo obsługuje Tor.

=== "OpenVPN" 

    Puli AX (oraz inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:
    
    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Puli AX (oraz inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką szybkość i wygodę. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, skrót od The Onion Router, to sieć nastawiona na ochronę prywatności, która umożliwia anonimową komunikację przez internet. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i aktywność użytkownika, co utrudnia śledzenie działań online. 
    
    * [Jak skonfigurować Tor](../../interface_guide/tor.md).

## Sieć bezprzewodowa i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień zarówno sieci Wi-Fi 5 GHz, jak i 2,4 GHz, w tym włączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

    Aby skonfigurować ustawienia Wireless, zobacz [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, szybkość pobierania i wysyłania, całkowity ruch oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

    Aby skonfigurować ustawienia Clients, zobacz [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi. 
    
    Aby skonfigurować GoodCloud, zobacz [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej zdalnej komunikacji sieciowej i zdalnym zarządzaniu urządzeniami. Została stworzona specjalnie do integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią i przyszłemu wsparciu dla sterowania na poziomie sprzętowym AstroWarp oferuje solidniejsze i bardziej niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci.
    
    Aby skonfigurować AstroWarp, zobacz [AstroWarp](../../interface_guide/astrowarp.md).

## Aplikacje

=== "Plug-ins"

    Plug-in to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego działania. 
    
    Aby skonfigurować Plug-ins, zobacz [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to szczególnie przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej. 
    
    Aby skonfigurować Dynamic DNS, zobacz [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Magazyn sieciowy to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich udostępnianie przez sieć. 
    
    Aby skonfigurować magazyn sieciowy, zobacz [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i trackerów, które działa jako serwer DNS, filtrując niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej. 
    
    Aby skonfigurować AdGuard Home, zobacz [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je. Obejmuje to ograniczanie czasu spędzanego przed ekranem oraz ograniczanie dostępu do określonych treści.

    Aby skonfigurować kontrolę rodzicielską, zobacz [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowanej programowo, które umożliwia użytkownikom tworzenie bezpiecznych, wirtualnych sieci przez internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej. 
    
    Aby skonfigurować ZeroTier, zobacz [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca. 
    
    Aby skonfigurować Tailscale, zobacz [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM Management"

    Aby dowiedzieć się, jak skonfigurować i zarządzać eSIM na swoim urządzeniu, zapoznaj się z [tym poradnikiem](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Ustawienia sieci

=== "Port forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w internecie dostęp do urządzeń w sieci prywatnej. Aby skonfigurować przekierowanie portów, zobacz [Port Forwards](../../interface_guide/port_forwarding.md). 

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia jednoczesne skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Dzięki temu dostęp do internetu pozostaje płynny i nieprzerwany. 

    Aby skonfigurować Multi-WAN, zobacz [Multi-WAN](../../interface_guide/multi-wan.md). 

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

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie wynegocjowanej szybkości portu sieciowego.

    Aby zarządzać portami Ethernet, zobacz [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Tryb sieci odnosi się do ustawień konfiguracyjnych określających, w jaki sposób urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami. 
    
    Aby skonfigurować tryb sieci, zobacz [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając użycie praktycznie nieograniczonej liczby unikalnych adresów IP, co jest niezbędne przy stale rosnącej liczbie urządzeń podłączonych do internetu. 
    
    Aby skonfigurować IPV6, zobacz [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może on nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN. 
    
    Aby skonfigurować Drop-in Gateway, zobacz [Jak skonfigurować Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

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

    Szczegółowe instrukcje znajdziesz w [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizowania firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje następujące opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie i instalowanie najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, co daje kontrolę nad wersją aktualizacji i momentem jej wykonania.
    * Module Online Upgrade: automatyczne sprawdzanie i instalowanie najnowszej wersji modułu 4G/5G bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Module Local Upgrade: ręczne przesłanie pliku modułu z komputera w celu aktualizacji modułu 4G/5G.

    Opcje te pozwalają utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * LED Display Schedule: ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć zanieczyszczenie światłem w określonych godzinach.
    * Schedule Reboot: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * 5GHz Wi-Fi Status Schedule: ustaw harmonogram sterowania pasmem Wi-Fi 5GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    * 2.4GHz Wi-Fi Status Schedule: ustaw harmonogram sterowania pasmem Wi-Fi 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu można dopasować je do własnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie właściwej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe będą poprawnie oznaczane zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych rejestrów oraz prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Ta strona obejmuje:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem kernela i jego zdarzeniami.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, zawierające szczegóły ruchu internetowego i działania serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez pomoc techniczną. Ta funkcja jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w [Log](../../interface_guide/log.md).

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

    Szczegółowe instrukcje znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji za pośrednictwem interfejsu OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory oraz inne zaawansowane dostosowania systemowe.

    Szczegółowe instrukcje znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md).

