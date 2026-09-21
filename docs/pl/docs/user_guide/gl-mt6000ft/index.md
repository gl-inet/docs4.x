# Podręcznik użytkownika Fortify (GL-MT6000)

## Przegląd produktu

Fortify (GL-MT6000) to router Wi-Fi 6 pod wspólną marką wydany wspólnie przez GL.iNet i ExpressVPN. Do każdej jednostki dołączona jest bezpłatna roczna subskrypcja ExpressVPN. Użytkownicy mogą wykupić subskrypcję i połączyć swoje konta bezpośrednio w internetowym panelu administracyjnym routera. Po aktywacji cały ruch przechodzący przez router będzie wykorzystywał szybką sieć ExpressVPN i solidne szyfrowanie, aby chronić całe połączenie sieciowe i prywatność w Internecie.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Jak skonfigurować Fortify

### 1. Włącz

Złóż razem dwuczęściowy zasilacz. Podłącz go do routera Fortify i podłącz do gniazdka. Uruchomi się automatycznie.

### 2. Podłącz urządzenie

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernetu

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na swoim urządzeniu przejdź do Ustawienia -> WLAN, znajdź nazwę sieci Wi-Fi swojego routera na liście dostępnych sieci i wprowadź hasło, aby dołączyć do sieci. Domyślną nazwę sieci i hasło można znaleźć na etykiecie routera.

### 3. Zaloguj się do internetowego panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. W prawym górnym rogu wybierz swój język, ustaw hasło administratora, a następnie kliknij **Next**. Hasło musi mieć długość 10–63 znaków i zawierać co najmniej dwa z następujących elementów: wielkie litery, małe litery, cyfry i symbole specjalne.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Skonfiguruj Wi-Fi. Pamiętaj, że jeśli zmienisz informacje o Wi-Fi, konieczne będzie ponowne połączenie urządzenia z siecią Wi-Fi routera przy użyciu zaktualizowanych danych uwierzytelniających.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Konfiguracja Internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pośrednictwem internetowego panelu administracyjnego GL.iNet. Jeśli wolisz aplikację [GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, pobierz ją i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Fortify, korzystając z jednej z obsługiwanych metod połączenia internetowego: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet pomiędzy portem WAN routera Fortify a urządzeniem nadrzędnym, takim jak modem.

    Po pomyślnym nawiązaniu połączenia z Internetem dioda LED routera zacznie świecić na biało.

    Szczegółowe instrukcje można znaleźć w [Podłączanie do Internetu za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. W panelu administracyjnym WWW przejdź do sekcji INTERNET -> Repeater i kliknij **Connect**.
    2. Wybierz Wi-Fi z dostępnych sieci.
    3. Wprowadź hasło, a następnie kliknij **Apply**.

    Po pomyślnym nawiązaniu połączenia z Internetem dioda LED routera zacznie świecić na biało.

    Szczegółowe instrukcje można znaleźć w artykule [Połącz się z Internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Podłącz smartfon do portu USB routera za pomocą kabla USB.
    2. Na smartfonie przejdź do Ustawień i włącz Tethering przez USB. W przypadku iPhone'a zaufaj temu urządzeniu i włącz Hotspot osobisty.
    3. W panelu administracyjnym WWW przejdź do sekcji INTERNET -> Tethering i kliknij **Connect**.

    Po pomyślnym nawiązaniu połączenia z Internetem dioda LED routera zacznie świecić na biało.

    Szczegółowe instrukcje można znaleźć w artykule [Połącz się z Internetem przez tethering przez USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Podłącz modem komórkowy USB do portu USB routera. Jest to przydatne do udostępniania Internetu z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym nawiązaniu połączenia z Internetem dioda LED routera zacznie świecić na biało.

    Szczegółowe instrukcje można znaleźć w [Połącz się z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md).

---

Poniżej znajduje się przegląd funkcji internetowego panelu administracyjnego Fortify.

## Bezprzewodowe

Strona Bezprzewodowa umożliwia skonfigurowanie sieci Wi-Fi Fortify, w tym sieci głównej, sieci dla gości i sieci IoT. Każda sieć obsługuje pasma 2,4 GHz i 5 GHz.

Aby skonfigurować połączenie bezprzewodowe, patrz [Bezprzewodowe](../../interface_guide/wireless.md).

## Klienci

Strona Klienci wyświetla informacje o podłączonych urządzeniach, w tym nazwę urządzenia, typ połączenia, adresy IP i MAC, prędkość pobierania i wysyłania, ruch, a także zapewnia możliwość zablokowania określonego klienta jednym kliknięciem lub wykonania innych czynności.

Aby uzyskać szczegółowe informacje, zobacz [Klienci](../../interface_guide/clients.md).

## Usługi w chmurze

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu i zarządzania routerami GL.iNet.

    Szczegółowe informacje można znaleźć w [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to funkcja stworzona z myślą o płynnej zdalnej pracy sieciowej na routerach GL.iNet. Przyjmuje protokół AmneziaWG z wbudowanym zaciemnianiem ruchu, zapewniając stabilny i bezpieczny zdalny dostęp w dowolnym miejscu i czasie.

    Aby uzyskać szczegółowe informacje, zobacz [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

VPN (virtual private network) ustanawia bezpieczne, szyfrowane tunele ruchu pomiędzy Twoim urządzeniem lokalnym a serwerem VPN. Dodaje dodatkową warstwę prywatności i bezpieczeństwa do klienta VPN i umożliwia dostęp do zdalnej sieci serwerów VPN.

Fortify integruje się z [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, umożliwiając aktywację połączenia ExpressVPN w ciągu kilku minut. Każde urządzenie Fortify jest objęte bezpłatną roczną subskrypcją ExpressVPN. Możesz wykupić subskrypcję i połączyć swoje konto ExpressVPN bezpośrednio w internetowym panelu administracyjnym routera. Po włączeniu połączenia VPN cały ruch kierowany przez router będzie korzystał z szybkich serwerów ExpressVPN i solidnego szyfrowania, aby zabezpieczyć całą sieć i prywatność w Internecie.

Aby skorzystać z bezpłatnej subskrypcji i skonfigurować tunel VPN, zapoznaj się z [Przewodnikiem aktywacji ExpressVPN](../../interface_guide/expressvpn_activation_guide.md).

Aby skonfigurować serwer OpenVPN, zapoznaj się z [Serwerem OpenVPN](../../interface_guide/openvpn_server.md).

Aby skonfigurować serwer WireGuard, patrz [Serwer WireGuard](../../interface_guide/wireguard_server.md).

## Sieć

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. komórkowym, Repeater i Ethernet) jednocześnie. Jeśli Twoje obecne połączenie internetowe ulegnie awarii, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Aby uzyskać szczegółowe informacje, zobacz [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN lub sieć lokalna to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Jest to sieć lokalna, do której dołącza Twoje urządzenie po podłączeniu do głównej sieci Wi-Fi lub za pomocą kabla Ethernet. Strona LAN obejmuje ustawienia podstawowe, ustawienia serwera DHCP i rezerwację adresów.

    Aby uzyskać szczegółowe informacje, zobacz [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Strona Sieć dla gości umożliwia utworzenie dedykowanej sieci Wi-Fi dla gości. Odizolowany od sieci podstawowej, zwiększa bezpieczeństwo, zapewniając jednocześnie wygodny dostęp do Internetu. Można ustawić podsieć gościa w zakresach adresów prywatnych IPv4 `192.168.0.0/16`, `172.16.0.0/12` lub `10.0.0.0/8`, określić adresy IP bramy i maski sieci.

    Aby uzyskać szczegółowe informacje, zobacz [Sieć dla gości](../../interface_guide/guest_network.md).

=== "IoT Network"

    Strona Sieć IoT umożliwia utworzenie dedykowanej sieci Wi-Fi dla urządzeń IoT. Odizolowany od sieci podstawowej, zapewnia lepszą kompatybilność i większe bezpieczeństwo.

    Aby uzyskać szczegółowe informacje, zobacz [Sieć IoT](../../interface_guide/iot_network.md).

<br>

=== "DNS"

    Ustawienia DNS na routerze kontrolują sposób tłumaczenia nazw domen na adresy IP. Ta strona umożliwia korzystanie z serwera DNS (s) uzyskiwanego automatycznie z urządzeń nadrzędnych lub ustawianie niestandardowych i konfigurowanie priorytetów DNS.

    Aby uzyskać szczegółowe informacje, zobacz [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Strona Port Ethernet umożliwia zarządzanie rolami portów Ethernet (WAN/LAN) i przeglądanie szczegółów portu, takich jak adres MAC i wynegocjowana prędkość.

    Aby uzyskać szczegółowe informacje, zobacz [Port Ethernet](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, czyli protokół internetowy w wersji 6, to najnowsza wersja protokołu internetowego zaprojektowana w celu zastąpienia protokołu IPv4. Zapewnia znacznie większą przestrzeń adresową, pozwalając na praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne do obsługi rosnącej liczby urządzeń podłączonych do Internetu.

    Aby uzyskać szczegółowe informacje, zobacz [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania i kontrolowania ruchu multiemisji.

    Aby uzyskać szczegółowe informacje, zobacz [IGMP Snooping](../../interface_guide/igmp_snooping.md).

<br>

=== "Network Mode"

    Tryb sieciowy odnosi się do ustawień konfiguracyjnych określających sposób, w jaki urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami.

    Aby skonfigurować tryb sieciowy, patrz [Tryb sieciowy](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN.

    Informacje na temat konfigurowania bramy typu drop-in można znaleźć w artykule [Jak skonfigurować bramkę typu drop-in](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    Przyspieszenie sieci może zmniejszyć obciążenie procesora i przyspieszyć przekazywanie pakietów ruchu.

    Aby skonfigurować przyspieszenie sieci, zapoznaj się z [Przyspieszenie sieci](../../interface_guide/network_acceleration.md).

## Kontrola przepływu

=== "DPI Engine"

    DPI (Deep Packet Inspection) to podstawowa funkcja inteligentnego zarządzania siecią. Może pokonać ograniczenia tradycyjnych routerów (które identyfikują tylko adres źródłowy lub docelowy), dogłębnie analizować ładunki pakietów danych i dokładnie identyfikować aplikacje i strony internetowe, do których uzyskują dostęp użytkownicy, poprzez porównanie bibliotek funkcji, umożliwiając udoskonaloną klasyfikację i kontrolę ruchu.

    Zintegrowana z [Netify](https://www.netify.ai/){target="_blank"} funkcja GL.iNet DPI wykorzystuje lekką wbudowaną wtyczkę zapewniającą efektywne wdrożenie. Dzięki aktualizowanej online bazie danych sygnatur Netify umożliwia niezawodne zarządzanie, dzięki czemu kontrola sieci jest dokładniejsza i wydajniejsza.

    Aby uzyskać szczegółowe informacje, zobacz [Silnik DPI](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics oferuje inteligentny panel analiz ruchu, który kategoryzuje i wizualizuje wykorzystanie sieci przez aplikacje, pomagając monitorować ruch w czasie rzeczywistym i historyczny, co zapewnia lepszą świadomość i kontrolę sieci.

    Aby uzyskać szczegółowe informacje, zobacz [Statystyki danych](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Filtr zawartości zapewnia inteligentne bezpieczeństwo w Internecie oparte na klasyfikacji opartej na DPI, automatycznie blokując szkodliwe lub złośliwe strony internetowe, aby utrzymać czystość i bezpieczeństwo sieci.

    Aby uzyskać szczegółowe informacje, zobacz [Filtr treści](../../interface_guide/content_filter.md).

<br>

=== "QoS"

    QoS (Quality of Service) optymalizuje alokację przepustowości, nadając priorytet krytycznym działaniom (np. rozmowom wideo i grom) podczas przeciążenia sieci, redukując opóźnienia i poprawiając ogólną wydajność sieci. Należy pamiętać, że dotyczy to ruchu klientów lokalnych i ruchu tunelowego klienta VPN, ale nie ruchu odbieranego, gdy router działa jako serwer VPN.

    Aby uzyskać szczegółowe informacje, zobacz [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i „przepełnienie bufora”, zapewniając płynniejszą grę i połączenia głosowe.

    Szczegółowe informacje można znaleźć w [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Kontrola rodzicielska została zaprojektowana, aby pomóc Ci zarządzać i kontrolować urządzenia Twoich dzieci. Obejmuje to ograniczenie czasu spędzanego przed ekranem i dostęp do niektórych treści.

    Aby uzyskać szczegółowe informacje, zobacz [Kontrola rodzicielska](../../interface_guide/parental_control_v4.9.md).

## Bezpieczeństwo

=== "Port forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.

    Aby uzyskać szczegółowe informacje, zobacz [Przekierowanie portów](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, skrót od listy kontroli dostępu, umożliwia tworzenie reguł zarządzania ruchem sieciowym w oparciu o protokoły połączeń, adresy urządzeń i porty. Kontroluje, czy zezwolić, czy zablokować dostęp do sieci. Jeśli istnieje konflikt wielu reguł ACL, system stosuje tę, która ma wyższy priorytet.

    Aby uzyskać szczegółowe informacje, zobacz [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Dostęp administracyjny umożliwia skonfigurowanie różnych ustawień zabezpieczeń w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Na tej stronie dostępne są następujące opcje:

    * Kontrola dostępu: Zarządzaj i ograniczaj dostęp do interfejsu routera z urządzeń podłączonych do Twojej sieci lokalnej.
    * Zdalna kontrola dostępu: konfiguruj i ograniczaj dostęp do interfejsu routera ze zdalnych lokalizacji za pośrednictwem Internetu, zwiększając bezpieczeństwo przed zagrożeniami zewnętrznymi.
    * Otwórz porty na routerze: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki w zabezpieczeniach i nieautoryzowany dostęp.

    Aby uzyskać szczegółowe informacje, zobacz [Dostęp administratora](../../interface_guide/admin_access.md).

=== "NAT Mode"

    Strona Tryb NAT umożliwia włączenie lub wyłączenie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Aby uzyskać szczegółowe informacje, zobacz [Tryb NAT](../../interface_guide/nat_settings.md).

## Aplikacje

=== "Plug-ins"

    Wtyczka to składnik oprogramowania, który dodaje określone cechy lub funkcjonalności do istniejącego programu komputerowego, umożliwiając dostosowywanie i zwiększanie jego możliwości.

    Aby uzyskać szczegółowe informacje, zobacz [Wtyczki](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamiczny DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest to przydatne dla użytkowników, którzy potrzebują statycznego adresu IP, aby uzyskać dostęp do zdalnej sieci.

    Aby uzyskać szczegółowe informacje, zobacz [Dynamiczny DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Magazyn sieciowy oznacza scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików i udostępnianie ich w sieci.

    Aby uzyskać szczegółowe informacje, zobacz [Pamięć sieciowa](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home to ogólnosieciowe rozwiązanie blokujące reklamy i moduły śledzące, które działa jako serwer DNS i filtruje niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej.

    Aby uzyskać szczegółowe informacje, zobacz [Strona główna AdGuard](../../interface_guide/adguardhome.md).

<br>

=== "Bark"

    Usługa [Bark](https://www.bark.us/){target="_blank"} może pomóc chronić cyfrowy świat Twojego dziecka i zapewnić kompleksową ochronę w Internecie. Zwykle wymaga płatnej subskrypcji. Jednakże w ramach partnerstwa GL.iNet z firmą Bark oferujemy bezpłatny plan Bark Home na urządzeniu Fortify (GL-MT6000), zapewniający zaawansowane monitorowanie i alerty bez dodatkowych kosztów.

    Aby uzyskać szczegółowe informacje, zobacz [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale to usługa VPN, dzięki której posiadane urządzenia i aplikacje są dostępne w dowolnym miejscu na świecie, bezpiecznie i bez wysiłku.

    Fortify (GL-MT6000) integruje się z Tailscale, umożliwiając dołączenie routera do wirtualnej sieci Tailscale. Po podłączeniu możesz uzyskać do niego zdalny dostęp, w tym do zasobów sieci WAN i LAN.

    Aby uzyskać szczegółowe informacje, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieciowe definiowane programowo, które umożliwia użytkownikom tworzenie bezpiecznych sieci wirtualnych za pośrednictwem Internetu, łącząc urządzenia tak, jakby znajdowały się w tej samej sieci lokalnej.

    Aby uzyskać szczegółowe informacje, zobacz [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor (nazwa pochodzi od The Onion Router) to bezpłatne oprogramowanie typu open source umożliwiające anonimową komunikację. Pomaga użytkownikom przeglądać Internet z zachowaniem prywatności.

    Szczegóły znajdziesz w [Tor](../../interface_guide/tor.md).

## Systemu

=== "Overview"

    Strona Przegląd zawiera kompleksowy przegląd bieżącego stanu i wskaźników wydajności routera. Na tej stronie możesz zobaczyć:

    * Średnie obciążenie procesora: Monitoruj średnie obciążenie procesora routera, pomagając ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: Sprawdź, ile pamięci routera jest zajęte, pomagając w zarządzaniu zasobami.
    * Sterowanie diodami LED: włącza lub wyłącza diody LED routera, umożliwiając dostosowanie wskaźników wizualnych urządzenia.
    * Użycie pamięci flash: Wyświetl wykorzystanie pamięci flash routera, sprawdzając, czy jest wystarczająca ilość miejsca na oprogramowanie sprzętowe i dane konfiguracyjne.
    * Informacje o urządzeniu: Uzyskaj dostęp do szczegółowych informacji o systemie routera, w tym o czasie pracy, nazwie hosta, modelu, architekturze, wersji OpenWrt, wersji jądra, identyfikatorze urządzenia, adresie MAC urządzenia i numerze seryjnym urządzenia.
    * Pamięć zewnętrzna: Sprawdź stan wszelkich zewnętrznych urządzeń pamięci masowej podłączonych do routera, takich jak dyski USB lub karty TF.

    Funkcje te zapewniają niezbędny wgląd i kontrolę, pomagając w skutecznym zarządzaniu i monitorowaniu działania routera.

    Aby uzyskać szczegółowe informacje, zobacz [Przegląd](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Hasło administratora umożliwia ustawienie lub zmianę hasła do interfejsu administracyjnego routera.

    Aby uzyskać szczegółowe informacje, zobacz [Hasło administratora](../../interface_guide/admin_password.md).

=== "Upgrade"

    Strona Aktualizacja służy do aktualizacji oprogramowania sprzętowego routera do najnowszej wersji, co zapewnia lepszą wydajność, bezpieczeństwo i nowe funkcje. Na tej stronie dostępne są dwie opcje:

    * Aktualizacja oprogramowania sprzętowego online: automatycznie sprawdzaj i instaluj najnowszą wersję oprogramowania sprzętowego bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Lokalna aktualizacja oprogramowania sprzętowego: ręcznie prześlij plik oprogramowania sprzętowego z komputera, aby zaktualizować router, zapewniając kontrolę nad wersją i czasem aktualizacji.

    Aby uzyskać szczegółowe informacje, zobacz [Aktualizacja](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Zaplanowane zadania umożliwia automatyzację różnych funkcji routera w oparciu o wstępnie zdefiniowany harmonogram, zwiększając wygodę i wydajność. Najważniejsze funkcje na tej stronie obejmują:

    * Harmonogram wyświetlania LED: Ustaw harmonogram automatycznego włączania i wyłączania świateł LED routera, redukując zanieczyszczenie światłem w określonych porach.
    * Zaplanuj ponowne uruchomienie: Skonfiguruj router tak, aby automatycznie uruchamiał się ponownie w określonych odstępach czasu, pomagając zachować optymalną wydajność i stabilność.
    * Harmonogram stanu Wi-Fi 5 GHz / 2,4 GHz: Ustaw harmonogram kontroli pasma Wi-Fi 5 GHz / 2,4 GHz, co pozwala na lepsze zarządzanie dostępnością sieci i zużyciem energii.

    Te opcje planowania zapewniają większą kontrolę nad działaniem routera, zapewniając, że spełnia on Twoje specyficzne potrzeby i preferencje.

    Aby uzyskać szczegółowe informacje, zobacz [Zaplanowane zadania](../../interface_guide/scheduled_tasks.md).

<br>

=== "Time Zone"

    Strona Strefa czasowa umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe są dokładnie oznaczone czasem lokalnym. To ustawienie jest kluczowe dla zachowania precyzyjnych zapisów i prawidłowego wykonania konfiguracji opartych na czasie.

    Aby uzyskać szczegółowe informacje, zobacz [Strefa czasowa](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Strona Resetuj oprogramowanie układowe umożliwia zresetowanie bieżącej wersji oprogramowania sprzętowego routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji oprogramowania. Może to być przydatne do rozwiązywania utrzymujących się problemów lub rozpoczynania od nowa z domyślną konfiguracją bieżącego oprogramowania sprzętowego.

    Aby uzyskać szczegółowe informacje, zobacz [Resetuj oprogramowanie sprzętowe](../../interface_guide/reset_firmware.md).

=== "Log"

    Strona Dziennik zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, pomagając w rozwiązywaniu problemów i monitorowaniu wydajności. Ta strona zawiera:

    * Dziennik systemowy: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Dziennik jądra: Dzienniki związane z operacjami i zdarzeniami jądra.
    * Dziennik awarii: Zapisy awarii i błędów systemu, przydatne do diagnozowania krytycznych problemów.
    * Cloud Log: Logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Dziennik Nginx: Dzienniki z serwera WWW Nginx, jeśli są używane przez router, zawierające szczegółowe informacje o ruchu sieciowym i operacjach serwera.

    Dodatkowo na stronie znajduje się przycisk Eksportuj Log, pozwalający na eksport wszystkich zebranych logów do analizy przez wsparcie techniczne. Funkcja ta jest nieoceniona przy diagnozowaniu skomplikowanych problemów i uzyskaniu profesjonalnej pomocy.

    Aby uzyskać szczegółowe informacje, zobacz [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Strona Ustawienia zaawansowane zapewnia dostęp do zaawansowanych opcji konfiguracji poprzez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom dostrojenie ustawień i funkcjonalności routera wykraczających poza podstawowe opcje interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory sieciowej i inne zaawansowane dostosowania systemu.

    Aby uzyskać szczegółowe informacje, zobacz [Ustawienia zaawansowane](../../interface_guide/advanced_settings.md).
