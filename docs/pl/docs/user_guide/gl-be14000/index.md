# Przewodnik użytkownika Flint 4 (GL-BE14000)

## Opis produktu

Flint 4 (GL‑BE14000) rozszerza możliwości routera domowego. Obsługuje trójzakresowe Wi‑Fi 7 z MLO i zapewnia maksymalne szybkości 688 Mbps (2.4 GHz) + 4323 Mbps (5 GHz) + 8646 Mbps (6 GHz). Do połączeń przewodowych służy kompletna, wielogigabitowa sieć szkieletowa: jeden port 10G SFP+ WAN/LAN, jeden port 10GE WAN/LAN, jeden port 2.5GE WAN/LAN, trzy porty 2.5GE LAN i cztery porty 1GE LAN. Wysokowydajna obsługa VPN zapewnia przepustowość do 1.5 Gbps zarówno dla WireGuard®, jak i OpenVPN DCO. Router ma również 2.4-calowy ekran dotykowy, który umożliwia monitorowanie stanu sieci w czasie rzeczywistym i wyświetlanie najważniejszych parametrów bezpośrednio na urządzeniu.

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## Zawartość opakowania

- 1 x Flint 4 (GL-BE14000)
- 1 x Zasilacz
- 1 x Kabel Ethernet
- 1 x Instrukcja obsługi
- 1 x Karta z podziękowaniem
- 1 x Przejściówka (odpowiednia dla kraju wysyłki)

Poniżej można obejrzeć film z rozpakowania Flint 4.

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Konfiguracja Flint 4

Obejrzyj film przedstawiający konfigurację lub wykonaj poniższe czynności.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączanie zasilania

Połącz dwie części zasilacza. Podłącz go do routera i gniazdka elektrycznego. Router uruchomi się automatycznie.

### 2. Podłączanie urządzenia

Połącz urządzenie, na przykład komputer, laptop lub smartfon, z routerem przez Wi-Fi albo Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera kablem Ethernet.

- Wi-Fi

    Na urządzeniu znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślna nazwa sieci (SSID) i hasło są wydrukowane na etykiecie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę, wpisz `192.168.8.1` na pasku adresu i zaloguj się. Ustaw hasło administratora oraz parametry Wi-Fi, a następnie kliknij **Apply**.

### 4. Konfiguracja Internetu

Skonfiguruj Flint 4, korzystając z jednej z obsługiwanych metod połączenia: Ethernet (SFP+), Ethernet (RJ45), Repeater, Tethering lub Cellular. Aby korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}
    
    Flint 4 ma port 10G SFP+ WAN/LAN przeznaczony do światłowodowych łączy nadrzędnych, szybkich połączeń dosyłowych przełączników i wydajnej rozbudowy sieci. Port jest domyślnie ustawiony jako WAN, ale w razie potrzeby można przełączyć go na LAN.

    Poniższy przykład przedstawia podłączenie portu 10G SFP+ routera Flint 4 do światłowodowego łącza operatora za pomocą transceivera optycznego i kabla światłowodowego. Inne rozwiązania opisano na stronie [Podłączanie portu 10G SFP+ w routerze Flint 4](../../faq/connecting_10g_sfp_plus_port_on_flint4.md).

    1. Włóż zgodny transceiver 10G SFP+ do portu SFP+ routera Flint 4, a następnie podłącz go do światłowodowego łącza operatora.  
    2. Flint 4 spróbuje automatycznie uzyskać przez DHCP parametry sieciowe (adres IP, bramę i DNS). Jeśli operator wymaga PPPoE lub statycznego adresu IP, odpowiednio zmień ustawienia połączenia WAN w panelu administracyjnym.
    3. Po nawiązaniu połączenia z Internetem sekcja Ethernet na stronie głównej ekranu dotykowego zmieni kolor na niebieski (aktywna). Dotknij Ethernet na ekranie albo zaloguj się do panelu administracyjnego, aby sprawdzić szczegóły połączenia.

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}
    
    1. Podłącz port WAN routera Flint 4 do urządzenia nadrzędnego, na przykład modemu operatora, przełącznika sieciowego lub ściennego gniazda Ethernet, za pomocą kabla Ethernet.
    2. Flint 4 spróbuje automatycznie uzyskać przez DHCP parametry sieciowe (adres IP, bramę i DNS). Jeśli operator wymaga PPPoE lub statycznego adresu IP, odpowiednio zmień ustawienia połączenia WAN w panelu administracyjnym.
    3. Po nawiązaniu połączenia z Internetem sekcja Ethernet na stronie głównej ekranu dotykowego zmieni kolor na niebieski (aktywna). Dotknij Ethernet na ekranie albo zaloguj się do panelu administracyjnego, aby sprawdzić szczegóły połączenia.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. Dotknij **Repeater** na ekranie. Router rozpocznie wyszukiwanie dostępnych sieci Wi-Fi.
    2. Wybierz sieć Wi-Fi, której zasięg ma rozszerzyć Flint 4.
    3. Wpisz hasło i dotknij **Apply**.
    4. Po nawiązaniu połączenia z Internetem sekcja Repeater na stronie głównej ekranu dotykowego zmieni kolor na niebieski (aktywna). Dotknij Repeater na ekranie albo zaloguj się do panelu administracyjnego, aby sprawdzić szczegóły połączenia.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne, na przykład smartfon, do portu USB routera Flint 4 za pomocą kabla USB.
    2. Na urządzeniu mobilnym otwórz Settings i włącz **USB Tethering** lub **Personal Hotspot**. Na iPhonie dotknij **Trust This Device**, jeśli pojawi się taki monit.
    3. Na ekranie Flint 4 wybierz **Tethering** i dotknij **Connect**. Router połączy się z urządzeniem.
    4. Po nawiązaniu połączenia z Internetem sekcja Tethering na stronie głównej ekranu dotykowego zmieni kolor na niebieski (aktywna). Dotknij Tethering na ekranie albo zaloguj się do panelu administracyjnego, aby sprawdzić szczegóły połączenia.

    **Uwaga**: jeśli połączenie nie powiedzie się, sprawdź, czy zasilacz ma parametry 12V 4A. Zbyt mała moc może uniemożliwić zasilenie portu USB. Powtórz powyższe czynności albo zaloguj się do panelu administracyjnego i sprawdź stan połączenia Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. Podłącz modem komórkowy lub modem USB do portu USB routera Flint 4. Umożliwia to udostępnienie połączenia internetowego z modemu USB wszystkim podłączonym urządzeniom.
    2. Po nawiązaniu połączenia z Internetem sekcja Cellular na stronie głównej ekranu dotykowego zmieni kolor na niebieski (aktywna). Dotknij Cellular na ekranie albo zaloguj się do panelu administracyjnego, aby sprawdzić szczegóły połączenia.

---

Poniżej przedstawiono funkcje dostępne w panelu administracyjnym Flint 4.

## Wireless

Strona Wireless umożliwia skonfigurowanie różnych sieci Wi-Fi routera Flint 4, w tym MLO Wi-Fi, Main Network, Guest Network i IoT Network.

Szczegółowe informacje zawiera strona [Wireless](../../interface_guide/wireless.md).

## Klienci

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adres IP i MAC, szybkość pobierania i wysyłania oraz całkowity ruch. Umożliwia również zablokowanie klienta lub wykonanie innych działań.

Szczegółowe informacje zawiera strona [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} umożliwia łatwy zdalny dostęp do routerów GL.iNet i zarządzanie nimi.
    
    Szczegółowe informacje zawiera strona [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana funkcja sieciowa zintegrowana z routerami GL.iNet. Zapewnia płynny zdalny dostęp do sieci domowej bez rejestracji i logowania. Protokół AmneziaWG z wbudowanym maskowaniem ruchu utrzymuje stabilność i bezpieczeństwo połączenia, zapewniając niezawodny zdalny dostęp w dowolnym miejscu. Sieć AstroWarp można skonfigurować bezpośrednio w panelu administracyjnym routera GL.iNet. Wystarczy sparować routery kodem dostępu, aby w kilka sekund bezpiecznie połączyć router podróżny z siecią domową.
    
    Szczegółowe informacje zawiera strona [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Flint 4 obsługuje protokoły OpenVPN i WireGuard.

=== "OpenVPN"
    
    Flint 4 i inne routery GL.iNet obsługują protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, zapoznaj się z poniższymi przewodnikami:

    * [Konfiguracja klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Konfiguracja serwera OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4 i inne routery GL.iNet obsługują szybki i wygodny protokół WireGuard. Aby skonfigurować WireGuard, zapoznaj się z poniższymi przewodnikami:

    * [Konfiguracja klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Konfiguracja serwera WireGuard](../../interface_guide/wireguard_server.md)

## Sieć

=== "Multi-WAN"

    Multi-WAN umożliwia jednoczesne skonfigurowanie wielu połączeń internetowych routera, na przykład komórkowego, Repeater i Ethernet. Jeśli bieżące połączenie przestanie działać, router automatycznie przełączy się na inne, zapewniając płynny i nieprzerwany dostęp do Internetu.

    Szczegółowe informacje zawiera strona [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Strona Subnet centralizuje zarządzanie LAN, Guest Network, IoT Network i niestandardowymi sieciami VLAN. Umożliwia tworzenie wielu podsieci i zarządzanie nimi w celu izolowania różnych typów urządzeń lub ruchu.

    Szczegółowe informacje zawiera strona [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia zarządzanie rolą portu Ethernet (WAN/LAN) i segmentacją VLAN oraz wyświetlanie takich informacji, jak adres MAC i wynegocjowana prędkość.

    Szczegółowe informacje zawiera strona [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding, zastąpienie ustawień DNS wszystkich klientów i zezwolenie niestandardowemu DNS na zastąpienie DNS sieci VPN. Umożliwia także automatyczne albo ręczne skonfigurowanie serwerów DNS połączenia Ethernet.

    Szczegółowe informacje zawiera strona [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, jest najnowszą wersją protokołu internetowego, która ma zastąpić IPv4. Zapewnia znacznie większą przestrzeń adresową i praktycznie nieograniczoną liczbę unikatowych adresów IP, co jest niezbędne ze względu na rosnącą liczbę urządzeń podłączonych do Internetu.
    
    Szczegółowe informacje zawiera strona [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multiemisji i sterowania nim.
    
    Szczegółowe informacje zawiera strona [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Network Mode oznacza różne role i funkcje operacyjne, które router może pełnić w zależności od wymagań wdrożenia sieci. Typowe tryby obejmują Router Mode, Extender Mode i Access Point Mode.
    
    Szczegółowe informacje zawiera strona [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway to elastyczna funkcja, która pozwala rozszerzyć możliwości istniejącego routera głównego bez jego wymiany lub ponownego konfigurowania. Ustawienie routera GL.iNet jako Drop-in Gateway pozwala dodać do istniejącej sieci zaawansowane funkcje, takie jak AdGuard Home, VPN i szyfrowany DNS.

    Aby skonfigurować Drop-in Gateway, skorzystaj z poniższych odsyłaczy.
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Konfiguracja Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network Acceleration zmniejsza obciążenie procesora i przyspiesza przekazywanie pakietów.
    
    Szczegółowe informacje zawiera strona [Network Acceleration](../../interface_guide/network_acceleration.md).

## Kontrola ruchu

=== "DPI Engine"

    DPI (Deep Packet Inspection) jest podstawą inteligentnego zarządzania siecią. Eliminuje ograniczenie tradycyjnych routerów, które rozpoznają jedynie adres źródłowy lub docelowy, analizując szczegółowo zawartość pakietów. Porównanie z biblioteką sygnatur pozwala dokładnie identyfikować aplikacje i witryny używane przez użytkowników oraz precyzyjnie klasyfikować i kontrolować ruch.
    
    Funkcja DPI GL.iNet jest zintegrowana z [Netify](https://www.netify.ai/){target="_blank"} i wykorzystuje lekki, wbudowany moduł umożliwiający wydajne wdrożenie. Aktualizowana online baza sygnatur Netify zapewnia niezawodne zarządzanie oraz dokładniejszą i wydajniejszą kontrolę sieci.

    Szczegółowe informacje zawiera strona [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics to inteligentny panel analizy ruchu, który klasyfikuje i przedstawia wykorzystanie sieci według aplikacji. Pomaga monitorować ruch bieżący i historyczny oraz lepiej kontrolować sieć.

    Szczegółowe informacje zawiera strona [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter zapewnia inteligentną ochronę online opartą na klasyfikacji DPI. Automatycznie blokuje szkodliwe lub złośliwe witryny, utrzymując sieć w bezpiecznym stanie.

    Szczegółowe informacje zawiera strona [Content Filter](../../interface_guide/content_filter.md).

---

=== "QoS"

    QoS (Quality of Service) optymalizuje przydział pasma, nadając priorytet kluczowym działaniom, takim jak rozmowy wideo lub gry, podczas przeciążenia sieci. Zmniejsza opóźnienia i poprawia ogólną wydajność. Funkcja obejmuje ruch klientów lokalnych i ruch tunelu klienta VPN, ale nie ruch odbierany, gdy router działa jako serwer VPN.

    Szczegółowe informacje zawiera strona [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i „bufferbloat”, zapewniając płynniejsze działanie gier i połączeń głosowych.

    Szczegółowe informacje zawiera strona [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je, między innymi przez ograniczanie czasu korzystania z ekranu i dostępu do określonych treści.

    Szczegółowe informacje zawiera strona [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Bezpieczeństwo

=== "Port Forwarding"

    Port Forwarding umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.
    
    Szczegółowe informacje zawiera strona [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL (Access Control List) umożliwia tworzenie reguł zarządzania ruchem na podstawie protokołów połączeń, adresów urządzeń i portów. Reguły określają, czy zezwalać na dostęp do sieci, czy go blokować. Jeśli kilka reguł ACL jest ze sobą sprzecznych, system stosuje regułę o wyższym priorytecie.

    Szczegółowe informacje zawiera strona [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access umożliwia konfigurowanie różnych ustawień zabezpieczeń chroniących sieć i router przed nieuprawnionym dostępem. Strona zawiera następujące opcje:

    * Local Access Control: zarządzanie i ograniczanie dostępu do interfejsu routera z urządzeń podłączonych do sieci lokalnej.
    * Remote Access Control: konfigurowanie i ograniczanie dostępu do interfejsu routera ze zdalnych lokalizacji przez Internet, co zwiększa ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontrolowanie portów otwartych na routerze, aby ograniczyć potencjalne luki i nieuprawniony dostęp.

    Szczegółowe informacje zawiera strona [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    Strona NAT Mode umożliwia włączenie lub wyłączenie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Szczegółowe informacje zawiera strona [NAT Mode](../../interface_guide/nat_settings.md).

## Aplikacje

=== "Plug-ins"

    Moduł to składnik oprogramowania, który dodaje określone funkcje do istniejącego programu, umożliwiając jego dostosowanie i rozszerzenie.
    
    Szczegółowe informacje zawiera strona [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest szczególnie przydatny dla użytkowników, którzy potrzebują stałego adresu do uzyskiwania dostępu do sieci zdalnej.
    
    Szczegółowe informacje zawiera strona [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików i udostępnianie ich przez sieć.
    
    Szczegółowe informacje zawiera strona [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie blokujące reklamy i moduły śledzące w całej sieci. Działa jako serwer DNS, filtrując niepożądane treści na wszystkich urządzeniach podłączonych do sieci domowej.
    
    Szczegółowe informacje zawiera strona [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    Usługa Bark zintegrowana z Flint 4 pomaga chronić cyfrowe środowisko dziecka i zapewnia kompleksową ochronę online. Zwykle wymaga płatnej subskrypcji. W ramach współpracy z Bark firma GL.iNet oferuje jednak plan Bark Home bezpłatnie na wybranych modelach routerów, w tym Flint 4, zapewniając zaawansowane monitorowanie i alerty bez dodatkowych opłat.

    Szczegółowe informacje zawiera strona [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.
    
    Szczegółowe informacje zawiera strona [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier to programowo definiowane rozwiązanie sieciowe, które umożliwia tworzenie bezpiecznych sieci wirtualnych przez Internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej.
    
    Szczegółowe informacje zawiera strona [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, czyli The Onion Router, to sieć ukierunkowana na ochronę prywatności, która umożliwia anonimową komunikację przez Internet. Kieruje ruch przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci, utrudniając śledzenie aktywności online.
    
    Szczegółowe informacje zawiera strona [Tor](../../interface_guide/tor.md).

## System

=== "Overview"

    Strona Overview przedstawia kompleksowy obraz bieżącego stanu routera i jego parametrów wydajności. Można na niej sprawdzić:

    * CPU Average Load: średnie obciążenie procesora routera, które pomaga ocenić wydajność i wykryć potencjalne wąskie gardła.
    * Memory Usage: ilość używanej pamięci routera, przydatną podczas zarządzania zasobami.
    * Flash Usage: wykorzystanie pamięci flash routera, aby upewnić się, że jest dostępne miejsce na oprogramowanie sprzętowe i dane konfiguracji.
    * Device Info: szczegółowe informacje o systemie, w tym czas działania, nazwa hosta, model, architektura, wersja OpenWrt, wersja jądra, identyfikator urządzenia, adres MAC urządzenia i numer seryjny.
    * External Storage: stan zewnętrznych urządzeń pamięci podłączonych do routera, takich jak nośniki USB lub karty TF.
    
    Funkcje te zapewniają informacje i elementy sterujące potrzebne do skutecznego zarządzania pracą routera i monitorowania jej.

    Szczegółowe informacje zawiera strona [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Admin Password umożliwia zarządzanie hasłem interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli zmieniać ustawienia.

    Szczegółowe informacje zawiera strona [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizowania oprogramowania sprzętowego routera do najnowszej wersji, co zapewnia lepszą wydajność i bezpieczeństwo oraz nowe funkcje. Dostępne są dwie opcje:

    * Firmware Online Upgrade: automatycznie sprawdza najnowszą wersję oprogramowania na serwerze producenta. Jeśli jest dostępna online, można ją zainstalować.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku oprogramowania z komputera oraz kontrolowanie wersji i czasu aktualizacji.

    Szczegółowe informacje zawiera strona [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzowanie różnych funkcji routera zgodnie ze zdefiniowanym harmonogramem. Najważniejsze opcje obejmują:

    * LCD Display Schedule: ustawienie harmonogramu automatycznego włączania lub wyłączania wyświetlacza LCD, aby ograniczyć niepożądane światło w określonych godzinach.
    * Schedule Reboot: skonfigurowanie automatycznego ponownego uruchamiania routera w określonych odstępach, co pomaga utrzymać optymalną wydajność i stabilność.
    * Wi-Fi Status Schedule: ustawienie harmonogramu sterowania pasmami Wi-Fi 6GHz / 5GHz / 2.4GHz / MLO, aby zarządzać dostępnością sieci i zmniejszyć zużycie energii.
    
    Opcje te zapewniają większą kontrolę nad działaniem routera i pozwalają dostosować je do określonych potrzeb.

    Szczegółowe informacje zawiera strona [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).
    
=== "Display Management"

    Strona Display Management udostępnia pełny zestaw funkcji do zarządzania ekranem dotykowym i jego ustawieniami.

    ‒ Wallpaper: dostosowanie tapety i stylu wyświetlania po wybudzeniu.
    ‒ Brightness: regulacja jasności ekranu za pomocą suwaka lub określonej wartości procentowej odpowiednio do warunków oświetlenia.
    ‒ Auto Lock: ustawienie opóźnienia automatycznego blokowania ekranu przy braku aktywności w zakresie od 1 minuty do 30 minut.
    ‒ Screen Always On: określenie, czy ekran ma pozostawać stale włączony, czy wyłączać się po okresie bezczynności.
    ‒ Enable Screen Passcode: ustawienie kodu dostępu do ekranu dotykowego jako dodatkowej warstwy zabezpieczeń.

    Szczegółowe informacje zawiera strona [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, aby wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe miały dokładne znaczniki czasu zgodne z czasem lokalnym. Jest to niezbędne do zachowania dokładnych zapisów i prawidłowego wykonywania konfiguracji opartych na czasie.

    Szczegółowe informacje zawiera strona [Time Zone](../../interface_guide/time_zone.md).

---

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie domyślnych ustawień bieżącej wersji oprogramowania i usunięcie wszystkich konfiguracji niestandardowych. Jest to przydatne podczas rozwiązywania trwałych problemów lub ponownego rozpoczynania konfiguracji od ustawień domyślnych zainstalowanej wersji.

    Szczegółowe informacje zawiera strona [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Strona Log zapewnia dostęp do dzienników rejestrujących działania i zdarzenia routera, co pomaga rozwiązywać problemy i monitorować wydajność. Obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki działań i zdarzeń jądra.
    * Crash Log: zapisy awarii i błędów systemu, przydatne podczas diagnozowania problemów krytycznych.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera internetowego Nginx, jeśli router go używa, zawierające informacje o ruchu internetowym i działaniach serwera.
    
    Przycisk Export Log umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez pomoc techniczną. Funkcja jest przydatna podczas diagnozowania złożonych problemów i uzyskiwania profesjonalnej pomocy.

    Szczegółowe informacje zawiera strona [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI. Doświadczeni użytkownicy mogą precyzyjnie dostosować ustawienia i funkcje routera poza podstawowymi opcjami interfejsu, w tym szczegółową konfigurację sieci, zapory i inne zaawansowane ustawienia systemowe.

    Szczegółowe informacje zawiera strona [Advanced Settings](../../interface_guide/advanced_settings.md).

## Deklaracja zgodności

Niniejszym GL TECHNOLOGIES (HONG KONG) LIMITED oświadcza, że typ urządzenia radiowego [BE14000 Wi-Fi 7 Router, GL-BE14000] jest zgodny z zasadniczymi wymaganiami i innymi stosownymi postanowieniami dyrektywy 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.

Dla UE:<br>
Maksymalna moc wyjściowa:<br>
CE: ≤20dBm EIRP (2.412GHz~2.472GHz); ≤23dBm EIRP (5.15GHz~5.35GHz); ≤30dBm EIRP (5.47GHz~5.725GHz); ≤13.98dBm (5.725GHz~5.85GHz); ≤23dBm EIRP (5.925GHz~6.425 GHz)
