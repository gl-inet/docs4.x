# Podręcznik użytkownika Marble (GL-B3000)

## Przegląd produktu

Router Marble (GL-B3000) to wyjątkowe urządzenie zaprojektowane w formie ramki na zdjęcie, dzięki czemu może eksponować ulubioną grafikę i jednocześnie stanowić ozdobę wnętrza. Oprócz atrakcyjnego wyglądu Marble (GL-B3000) zapewnia wysoką wydajność dzięki Wi-Fi 6 i obsłudze funkcji VPN.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Zawartość opakowania

- 1 x Marble (GL-B3000)
- 1 x instrukcja obsługi
- 1 x karta z podziękowaniem
- 1 x kabel Ethernet
- 1 x zestaw do montażu ściennego
- 1 x podkładka samoprzylepna
- 1 x podstawka pod router
- 1 x ramka na zdjęcie (opcjonalnie)
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Marble

Obejrzyj filmy dotyczące montażu i konfiguracji lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka. Router uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera za pomocą Wi-Fi lub kabla Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, odszukaj nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. (Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera).

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

### 4. Konfiguracja internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router przez panel GL.iNet Web Admin Panel. Jeśli wolisz użyć aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Marble, korzystając z jednej z obsługiwanych metod połączenia z internetem: Ethernet i Repeater. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj dwa połączenia internetowe.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}
    
    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem.
    
    Po prawidłowym połączeniu z internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez kabel Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. Na stronie INTERNET w panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wpisz hasło sieci, a następnie kliknij **Apply**.
    
    Po prawidłowym połączeniu z internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

---

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa jako klient VPN oraz umożliwia dostęp do zdalnej sieci jako serwer VPN. Marble (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard. Dodatkowo obsługuje również Tor.

=== "OpenVPN"

    Marble (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia silne zabezpieczenia. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble (i inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia dużą szybkość i wygodę. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor to usługa zorientowana na prywatność, umożliwiająca anonimowe przeglądanie internetu. Aby skonfigurować Tor, skorzystaj z poniższego poradnika:

    * [Jak skonfigurować Tor](../../interface_guide/tor.md)

---

## Sieć bezprzewodowa i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5 GHz i 2,4 GHz, w tym włączanie i wyłączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci (SSID), włączanie i wyłączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi, ustawienie hasła Wi-Fi, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

    Aby skonfigurować Wireless, zapoznaj się z [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę urządzenia, typ połączenia (np. Ethernet lub Wi-Fi), adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

    Aby skonfigurować Clients, zapoznaj się z [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    Ta funkcja jest dostępna od firmware v4.7.

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o płynnej pracy sieci zdalnych i zdalnym zarządzaniu urządzeniami. Została stworzona specjalnie do integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę urządzeń nadrzędnych i podrzędnych. Koncentrując się na zarządzaniu całosieciowym i przyszłym wsparciu sterowania na poziomie sprzętowym, AstroWarp oferuje solidniejsze i bardziej niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci.

## Aplikacje

=== "Plug-ins"

    Plug-ins to dodatkowe funkcje rozszerzające możliwości routera. Aby skonfigurować Plug-ins, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest szczególnie przydatny dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do zdalnej sieci. Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md).

---

=== "AdGuard Home"

    AdGuard Home to zewnętrzne narzędzie blokujące reklamy i mechanizmy śledzące, co pomaga zwiększyć bezpieczeństwo.
    
    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control to zestaw ustawień pomagających zarządzać urządzeniami dzieci i kontrolować sposób ich używania. Obejmuje ograniczanie czasu przed ekranem oraz blokowanie dostępu do określonych treści. Marble oferuje dwie opcje kontroli rodzicielskiej: lokalną wersję opracowaną przez GL.iNet oraz zintegrowaną wersję aplikacji Bark.

    Aby skonfigurować Parental Control, zapoznaj się z [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"
   
    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca. Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier to usługa VPN, która umożliwia podłączenie urządzeń do wirtualnej sieci. Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

---

## Ustawienia sieciowe

=== "Firewall"

    Strona Firewall zapewnia podstawowe ulepszenia bezpieczeństwa sieci. Obejmuje funkcje takie jak Port Forwarding, Open Ports i DMZ. Narzędzia te umożliwiają zarządzanie przepływem ruchu w sieci oraz zwiększają jej bezpieczeństwo.

    * Port Forwarding: przekierowuje określony ruch z internetu do wskazanych urządzeń w sieci, umożliwiając dostęp do usług takich jak serwery gier lub serwery WWW.
    * Open Ports: pozwala monitorować i kontrolować, które porty routera są otwarte, pomagając zapobiegać nieautoryzowanemu dostępowi i potencjalnym zagrożeniom.
    * DMZ (Demilitarized Zone): umieszcza urządzenie poza główną zaporą, zapewniając mu nieograniczony dostęp do internetu przy jednoczesnej ochronie pozostałej części sieci przed potencjalnymi zagrożeniami.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa pozwalająca skonfigurować router z wieloma połączeniami internetowymi jednocześnie (np. cellular, repeater i ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie. Zapewnia to płynny i nieprzerwany dostęp do internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN (Local Area Network) to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Strona LAN umożliwia zarządzanie i konfigurację ustawień sieci lokalnej routera. Dostępne są między innymi następujące funkcje:

    * Router IP Address: zmiana adresu IP routera tak, aby lepiej pasował do konfiguracji sieci.
    * Netmask: ustawienie maski podsieci, która określa wielkość sieci i zakres adresów IP.
    * DHCP: włączenie lub konfiguracja protokołu Dynamic Host Configuration Protocol, który automatycznie przypisuje adresy IP urządzeniom w sieci.
    * Address Reservation: rezerwacja określonych adresów IP dla wybranych urządzeń, aby zawsze otrzymywały ten sam adres z serwera DHCP.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [LAN](../../interface_guide/lan.md).

---

=== "Guest Network"

    Strona Guest Network umożliwia utworzenie i zarządzanie oddzielną siecią dla gości, zapewniając im dostęp do internetu przy zachowaniu bezpieczeństwa głównej sieci. Dostępne funkcje obejmują:

    * Gateway: ustawienie określonego zakresu adresów IP dla sieci gościnnej, aby odróżnić ją od sieci głównej.
    * DHCP: konfigurację protokołu Dynamic Host Configuration Protocol dla sieci gościnnej, który automatycznie przypisuje adresy IP urządzeniom łączącym się z tą siecią.

    Funkcje te pozwalają gościom korzystać z internetu bez wpływu na bezpieczeństwo i wydajność głównej sieci.
    
    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Strona DNS oferuje opcje dostosowania ustawień Domain Name System routera, poprawiając bezpieczeństwo i wydajność. Dostępne funkcje obejmują:

    * Encrypted DNS: konfigurację szyfrowanego DNS w celu ochrony danych przeglądania przed monitorowaniem lub manipulacją.
    * Manual DNS: ręczne ustawienie wybranych serwerów DNS, zapewniające większą kontrolę nad zapytaniami DNS i potencjalnie szybsze rozwiązywanie nazw.
    * DNS Proxy: włączenie proxy DNS do kierowania żądań DNS z urządzeń przez wskazany serwer DNS, zapewniającego dodatkową warstwę kontroli nad ruchem DNS.

    Ustawienia te pozwalają zoptymalizować wydajność i bezpieczeństwo DNS zgodnie z własnymi potrzebami.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Tryb sieciowy określa ustawienia konfiguracji decydujące o sposobie, w jaki urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami. Strona Network Mode umożliwia skonfigurowanie routera do pracy w różnych trybach, zapewniając elastyczność dla różnych potrzeb sieciowych. Dostępne tryby obejmują:

    * Router: praca jako standardowy router zarządzający ruchem między siecią lokalną a internetem oraz zapewniający funkcje takie jak NAT, firewall i DHCP.
    * Access Point: praca jako punkt dostępowy, który rozszerza istniejącą sieć przewodową o łączność bezprzewodową bez routingu ruchu.
    * Extender: praca jako wzmacniacz zasięgu, który zwiększa zasięg istniejącej sieci bezprzewodowej i eliminuje martwe strefy.
    * WDS (Wireless Distribution System): podobnie jak Extender; wybierz WDS, jeśli główny router obsługuje tryb WDS.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

---

=== "IPv6"

    IPv6 (Internet Protocol version 6) to najnowsza wersja protokołu internetowego. Strona IPv6 umożliwia konfigurację ustawień IPv6 w sieci. Na tej stronie możesz włączyć IPv6 i wybrać jeden z czterech trybów odpowiednich dla swojej sieci:

    * Native: pobieranie adresu IPv6 bezpośrednio od dostawcy internetu, zapewniające prostą i wydajną natywną łączność IPv6.
    * Passthrough: przepuszczanie ruchu IPv6 przez router do urządzeń w sieci, skutecznie mostkując połączenie bez obsługi routingu IPv6 przez sam router.
    * NAT6: wykorzystanie translacji adresów sieciowych dla IPv6 (NAT6) do translacji między wewnętrznymi i zewnętrznymi adresami IPv6, podobnie jak NAT działa w IPv4.
    * Static IPv6: ręczna konfiguracja statycznego adresu IPv6 routera, zapewniająca stały adres dla stabilnej łączności i łatwiejszego zarządzania usługami sieciowymi.

    Ustawienia te pomagają wykorzystać zalety IPv6, w tym większą przestrzeń adresową, ulepszone funkcje bezpieczeństwa i lepszą wydajność.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    Strona MAC Address umożliwia podgląd i zarządzanie adresami Media Access Control (MAC) powiązanymi z routerem. Dostępne funkcje obejmują:

    * Factory Default: wyświetlenie domyślnych adresów MAC dla trybów Ethernet i Repeater jako odniesienia do oryginalnych ustawień sprzętowych.
    * Clone: sklonowanie adresu MAC konkretnego urządzenia klienckiego. Jest to szczególnie przydatne w sytuacjach, gdy dostęp do sieci jest ograniczony do wybranych urządzeń.
    * Manual: ręczne podanie niestandardowego adresu MAC routera. Dodatkowo możesz użyć przycisku Random, aby wygenerować losowy adres MAC, co zapewnia większą elastyczność i prywatność.

    Funkcje te umożliwiają skuteczne zarządzanie adresami MAC routera, zapewniając zgodność i elastyczność w różnych środowiskach sieciowych.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność routera głównego o funkcje, których może on nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN. Aby skonfigurować Drop-in Gateway, zapoznaj się z [How to set up Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP Snooping to technika optymalizacji sieci stosowana do zarządzania i kontrolowania ruchu multicast. Strona IGMP Snooping umożliwia konfigurację ustawień optymalizujących zarządzanie ruchem multicast w sieci. IGMP Snooping nasłuchuje pakietów protokołu IGMP i wyodrębnia z nich informacje, tworząc oraz utrzymując tablice przekazywania multicast w warstwie 2. Dzięki temu dane grup multicast są przekazywane tylko do hostów, które dołączyły do danej grupy, co zapobiega kierowaniu niechcianego ruchu multicast do innych hostów.

    Ustawienia te pomagają zoptymalizować wydajność i efektywność sieci, szczególnie w środowiskach z dużą ilością ruchu multicast, takich jak strumieniowanie wideo lub gry online.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Akceleracja sieci pozwala zmniejszyć obciążenie procesora i przyspieszyć przekazywanie pakietów. Strona Network Acceleration umożliwia włączenie tej funkcji w celu poprawy ogólnej wydajności sieci. Należy jednak pamiętać, że włączenie akceleracji sieci może powodować konflikty z niektórymi funkcjami.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia konfigurację opcji Network Address Translation (NAT) w celu optymalizacji działania wybranych aplikacji i poprawy wydajności sieci. Dostępne ustawienia obejmują:

    * Enable Full Cone NAT: Full Cone NAT może pomóc zmniejszyć opóźnienia w grach, oferując bardziej bezpośrednią i mniej restrykcyjną ścieżkę dla ruchu sieciowego. Jednak włączenie Full Cone NAT może obniżyć poziom bezpieczeństwa, ponieważ ułatwia hostom zewnętrznym inicjowanie połączeń z urządzeniami wewnętrznymi.
    * Enable SIP ALG: Session Initiation Protocol Application Layer Gateway (SIP ALG) może pomóc ograniczyć problemy spowodowane przez wielokrotny NAT, które mogą wpływać na usługi VoIP. Jednak w większości przypadków SIP ALG nie przynosi korzyści i może powodować problemy, takie jak dźwięk tylko w jedną stronę, brak dzwonienia telefonów, rozłączanie połączeń lub przekierowywanie rozmów bezpośrednio do poczty głosowej.

    Ustawienia te pozwalają dostosować zachowanie NAT routera do potrzeb sieci, równoważąc poprawę wydajności z możliwymi konsekwencjami dla bezpieczeństwa i funkcjonalności.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [NAT Settins](../../interface_guide/nat_settings.md).

---

## Ustawienia systemowe

=== "Overview"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i jego parametrów wydajności. Możesz na niej sprawdzić:

    * CPU Average Load: średnie obciążenie procesora routera, co pomaga ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: ilość używanej pamięci routera, co pomaga w zarządzaniu zasobami.
    * Flash Usage: wykorzystanie pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * System Info: szczegółowe informacje o systemie routera, w tym wersję firmware, czas pracy i stan sieci.
    * LED Control: włączanie i wyłączanie diod LED routera, co pozwala dostosować wizualne wskaźniki urządzenia.
    
    Funkcje te zapewniają istotne informacje i narzędzia, które pomagają skutecznie zarządzać pracą routera i ją monitorować.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Dostępne są dwie opcje aktualizacji:

    * Online Upgrade: automatyczne sprawdzanie i instalacja najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Local Upgrade: ręczne wgranie pliku firmware z komputera, co daje większą kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router w aktualnym stanie, korzystając z najnowszych usprawnień i poprawek.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera według zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Dostępne funkcje obejmują:

    * LED Display Schedule: ustawienie harmonogramu automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w wybranych godzinach.
    * Schedule Reboot: skonfigurowanie automatycznego restartu routera w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Wi-Fi Status Schedule: ustawienie harmonogramu sterowania pasmem Wi-Fi, co pozwala lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Opcje te dają większą kontrolę nad działaniem routera, dzięki czemu można lepiej dopasować go do własnych potrzeb i preferencji.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie właściwej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe mają poprawne znaczniki czasu zgodne z Twoim czasem lokalnym. Jest to istotne dla zachowania dokładnych rejestrów i prawidłowego działania konfiguracji zależnych od czasu.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w diagnostyce i monitorowaniu wydajności. Obejmuje ona:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem i zdarzeniami jądra.
    * Crash Log: zapisy awarii i błędów systemu, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu WWW i działaniu serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który pozwala wyeksportować wszystkie zebrane logi do analizy przez wsparcie techniczne. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Log](../../interface_guide/log.md).

---

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień zabezpieczeń w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Obejmuje opcje takie jak:

    * Admin Password: ustawienie lub zmiana hasła do interfejsu administracyjnego routera, aby tylko upoważnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzanie dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i jego ograniczanie.
    * Remote Access Control: konfiguracja i ograniczanie dostępu do interfejsu routera z lokalizacji zdalnych przez internet, co zwiększa ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontrolowanie, które porty routera są otwarte, aby ograniczyć potencjalne podatności i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca ustawienia domyślne aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa z domyślnymi ustawieniami bieżącej wersji firmware.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostrojenie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółową konfigurację sieci, ustawienia zapory i inne zaawansowane dostosowania systemowe.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Advanced Settings](../../interface_guide/advanced_settings.md).

