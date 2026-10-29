# Przewodnik użytkownika Beryl AX (GL-MT3000) {#beryl-ax-gl-mt3000-user-guide}

## Przegląd produktu {#product-overview}

Beryl AX (GL-MT3000) to kompaktowy router podróżny AX3000 wykorzystujący standard Wi-Fi 6. Jest ulepszoną wersją modelu Beryl (GL-MT1300). Pracuje na dwurdzeniowym procesorze MT7981B 1.3GHz i oferuje ponad dwukrotnie wyższą łączną prędkość Wi-Fi. Został zaprojektowany z myślą o rodzinach intensywnie korzystających z Wi-Fi, a dzięki niewielkim rozmiarom świetnie sprawdza się również w podróży.

![gl-mt3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/hardware_info/mt3000_interface.jpg){class="glboxshadow"}

## Zawartość opakowania {#package-contents}

- 1 x Beryl AX (GL-MT3000)
- 1 x instrukcja obsługi
- 1 x kabel Ethernet
- 1 x karta z podziękowaniem
- 1 x karta gwarancyjna
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![gl-MT3000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/first_time_setup/mt3000_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Beryl AX {#how-to-set-up-beryl-ax}

Obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania {#1-power-on}

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia {#2-connect-device}

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Logowanie do panelu administracyjnego {#3-log-in-to-web-admin-panel}

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Podczas potwierdzania ustawień Wi‑Fi pamiętaj, że jeśli zmienisz dane sieci Wi-Fi, konieczne będzie ponowne połączenie urządzenia z siecią Wi-Fi routera przy użyciu zaktualizowanych danych.

### 4. Konfiguracja Internetu {#4-internet-setup}

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą webowego panelu administracyjnego GL.iNet. Jeśli wolisz użyć aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Beryl AX, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym (np. modemem).

    Po pomyślnym połączeniu z Internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md), aby uzyskać szczegółowe instrukcje.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wpisz hasło, a następnie kliknij **Apply**.

    Po pomyślnym połączeniu z Internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md), aby uzyskać szczegółowe instrukcje.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering.
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering.

    Po pomyślnym połączeniu z Internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md), aby uzyskać szczegółowe instrukcje.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_cellular.png){class="glboxshadow"}

    Podłącz modem USB z łącznością komórkową do portu USB routera. Ta metoda jest przydatna do udostępniania Internetu z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md), aby uzyskać szczegółowe instrukcje.

## DNS {#dns}

Ustawienia DNS routera określają sposób rozwiązywania nazw domen na adresy IP. Na tej stronie możesz korzystać z serwerów DNS uzyskanych automatycznie z urządzeń nadrzędnych lub ustawić własne. Możesz również skonfigurować opcje DNS i edytować statyczne reguły hostów.

Więcej informacji znajdziesz w sekcji [DNS](../../interface_guide/dns_v4.11.md).

## Wireless {#wireless}

Strona Wireless umożliwia konfigurację ustawień zarówno dla sieci Wi-Fi 5 GHz, jak i 2.4 GHz, w tym włączanie i wyłączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie i wyłączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi, ustawianie hasła Wi-Fi, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

Zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md), aby uzyskać szczegółowe instrukcje.

## Mesh {#mesh}

Mesh to funkcja oparta na standardzie Wi-Fi EasyMesh™, która rozszerza zasięg Wi-Fi na cały dom i umożliwia płynny roaming. Jeśli masz kilka routerów GL.iNet, ustaw jeden jako router główny, a pozostałe jako węzły mesh, aby zapewnić płynny roaming Wi-Fi w całym domu.

Więcej informacji znajdziesz w sekcji [Mesh](../../interface_guide/mesh.md).

## CLIENTS {#clients}

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę urządzenia, typ połączenia (tj. przez Ethernet lub Wi-Fi), adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia rezerwację IP, blokowanie klienta i wykonywanie innych działań.

Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md), aby uzyskać szczegółowe instrukcje.

## Usługi chmurowe {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account umożliwia łączenie urządzeń i usług chmurowych oraz zarządzanie nimi. Zapewnia łatwy dostęp do GoodCloud i glinet App, dzięki czemu można bezpiecznie i wygodnie zarządzać siecią z dowolnego miejsca i o każdej porze.

    Instrukcje konfiguracji zawiera strona [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.

    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md), aby uzyskać szczegółowe instrukcje.

=== "GoodPAS"

    GoodPAS to zaawansowana funkcja sieciowa zapewniająca płynny zdalny dostęp i zarządzanie urządzeniami. Rozwiązanie zaprojektowano specjalnie do integracji z routerami GL.iNet i wykorzystuje ono protokół AmneziaWG z wbudowanym maskowaniem ruchu, aby zapewnić bezpieczne i stabilne połączenia. GoodPAS umożliwia zdalny dostęp do sieci domowej. Gdy router domowy pełni funkcję węzła wyjściowego GoodPAS, ruch internetowy wysyłany przez GoodPAS korzysta z publicznego adresu IP WAN tego routera.

    Instrukcje konfiguracji zawiera strona [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Beryl AX (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard.

=== "OpenVPN"

    Beryl AX (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Beryl AX (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Sieć {#network}

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. Cellular, Repeater i Ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md), aby uzyskać szczegółowe instrukcje.

=== "LAN"

    Strona LAN umożliwia scentralizowaną konfigurację sieci głównej, sieci gościnnej, sieci IoT i niestandardowych sieci VLAN oraz zarządzanie nimi. Możesz tworzyć wiele podsieci i zarządzać nimi, aby izolować różne typy urządzeń lub ruchu.

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie wynegocjowanej szybkości portu sieciowego.

    Zapoznaj się z poradnikiem [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana w celu zastąpienia IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne ze względu na rosnącą liczbę urządzeń podłączonych do Internetu.

    Zapoznaj się z poradnikiem [IPV6](../../interface_guide/ipv6.md), aby uzyskać szczegółowe instrukcje.

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.

    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md), aby uzyskać szczegółowe instrukcje.

=== "Network Mode"

    Strona Network Mode umożliwia dostosowanie roli operacyjnej routera do różnych potrzeb wdrożeniowych. Można wybrać tryby przeznaczone do scenariuszy od domowego zasięgu Wi-Fi po firmowe sieci wielołączowe; każdy tryb włącza lub wyłącza określone funkcje routera w celu optymalizacji wydajności.

    Instrukcje konfiguracji zawiera strona [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o takie funkcje jak AdGuard Home, szyfrowany DNS i klient VPN.

    Aby skonfigurować Drop-in Gateway, skorzystaj z poniższych poradników:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Konfiguracja Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network Acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.

    Zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md), aby uzyskać szczegółowe instrukcje.

## Kontrola ruchu {#flow-control}

=== "Network Quality"

    Panel Network Quality monitoruje jakość połączenia internetowego w czasie rzeczywistym. Ocenia szybkość reakcji, opóźnienia i wydajność DNS, wykrywając zerwania połączenia i utratę pakietów. Te wskaźniki pomagają identyfikować niestabilność sieci i problemy z łącznością, których same testy przepustowości mogą nie wykryć.

    Więcej informacji znajdziesz w sekcji [Network Quality](../../interface_guide/network_quality.md).

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

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je. Obejmuje ograniczanie czasu korzystania z ekranu oraz blokowanie dostępu do określonych treści.

    Aby skonfigurować kontrolę rodzicielską, zapoznaj się z sekcją [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Bezpieczeństwo {#security}

=== "Security Scan"

    Security Scan przeprowadza kontrolę bezpieczeństwa routera. Ocenia jego ustawienia zabezpieczeń i generuje wynik oceny bezpieczeństwa wraz z alertami o zagrożeniach i sugestiami optymalizacji. Możesz dostosować konfigurację na podstawie wyników skanowania, aby poprawić bezpieczeństwo routera.

    Więcej informacji znajdziesz w sekcji [Security Scan](../../interface_guide/security_scan.md).

=== "ACL"

    ACL (Access Control List) umożliwia tworzenie reguł zarządzania ruchem na podstawie protokołów połączeń, adresów urządzeń i portów. Reguły określają, czy zezwalać na dostęp do sieci, czy go blokować. Jeśli kilka reguł ACL jest ze sobą sprzecznych, system stosuje regułę o wyższym priorytecie.

    Szczegółowe informacje zawiera strona [ACL](../../interface_guide/acl.md).

=== "Port Forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.

    Zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md), aby uzyskać szczegółowe instrukcje.

---

=== "UPnP"

    UPnP (Universal Plug and Play) umożliwia zgodnym urządzeniom i aplikacjom LAN automatyczne żądanie mapowania portów na routerach GL.iNet. Mapowania te przekierowują przychodzący ruch WAN na określone adresy IP i porty LAN, umożliwiając klientom zewnętrznym łączenie się z lokalnymi usługami bez ręcznego konfigurowania reguł przekierowania portów.

    Więcej informacji znajdziesz w sekcji [UPnP](../../interface_guide/upnp.md).

=== "Admin Access"

    Admin Access umożliwia konfigurowanie różnych ustawień zabezpieczeń chroniących sieć i router przed nieuprawnionym dostępem. Strona zawiera następujące opcje:

    * Local Access Control: zarządzaj i ograniczaj dostęp do interfejsu routera z urządzeń podłączonych do sieci lokalnej.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera ze zdalnych lokalizacji przez Internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki w zabezpieczeniach i nieautoryzowany dostęp.

    Szczegółowe informacje zawiera strona [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    Strona NAT Mode umożliwia włączenie albo wyłączenie funkcji Full Cone NAT i SIP ALG.

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Mode](../../interface_guide/nat_settings.md).

## Aplikacje {#applications}

=== "Plug-ins"

    Plug-in to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego działania.

    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md), aby uzyskać szczegółowe instrukcje.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Mapuje nazwę domeny na dynamiczny publiczny adres IP routera, dzięki czemu możesz zdalnie uzyskiwać dostęp do swojej sieci bez statycznego adresu IP.

    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md), aby uzyskać szczegółowe instrukcje.

=== "Network Storage"

    Network Storage to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć.

    Zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md), aby uzyskać szczegółowe instrukcje.

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie do blokowania reklam i trackerów w całej sieci, działające jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej.

    Zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md), aby uzyskać szczegółowe instrukcje.

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.

    Zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md), aby uzyskać szczegółowe instrukcje.

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowanej programowo, które umożliwia tworzenie bezpiecznych sieci wirtualnych przez Internet, łącząc urządzenia tak, jakby znajdowały się w tej samej sieci lokalnej.

    Zapoznaj się z poradnikiem [ZeroTier](../../interface_guide/zerotier.md), aby uzyskać szczegółowe instrukcje.

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na ochronę prywatności, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci przez użytkownika, co utrudnia śledzenie aktywności online.

    Aby skonfigurować Tor, zapoznaj się z [Tor](../../interface_guide/tor.md).

## System {#system}

=== "Overview"

    Strona Overview zapewnia kompleksowy przegląd bieżącego stanu routera oraz wskaźników wydajności. Na tej stronie możesz zobaczyć:

    * Średnie obciążenie CPU: monitoruj średnie obciążenie procesora routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: sprawdź, jaka część pamięci routera jest aktualnie używana, co pomaga w zarządzaniu zasobami.
    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Użycie pamięci flash: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że dostępna jest wystarczająca ilość miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, nazwę hosta, model, architekturę, wersję OpenWrt, wersję kernela, identyfikator urządzenia, adres MAC urządzenia i numer seryjny.
    * Zewnętrzna pamięć masowa: sprawdź stan zewnętrznych urządzeń pamięci masowej podłączonych do routera, takich jak dyski USB lub karty TF.

    Funkcje te zapewniają kluczowe informacje i mechanizmy sterowania, pomagając skutecznie zarządzać pracą routera oraz ją monitorować.

    Zapoznaj się z poradnikiem [Overview](../../interface_guide/system_overview.md), aby uzyskać szczegółowe instrukcje.

=== "Admin Password"

    Strona Admin Password umożliwia zarządzanie hasłem interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli zmieniać ustawienia.

    Szczegółowe informacje zawiera strona [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, większe bezpieczeństwo i nowe funkcje. Strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie dostępności najnowszej wersji firmware na serwerze producenta. Jeśli jest dostępna online, możesz ją zainstalować.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera w celu zaktualizowania routera, dając kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router na bieżąco z najnowszymi usprawnieniami i poprawkami.

    Zapoznaj się z poradnikiem [Upgrade](../../interface_guide/upgrade.md), aby uzyskać szczegółowe instrukcje.

---

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * Harmonogram diod LED: ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w określonych godzinach.
    * Zaplanowane ponowne uruchomienie: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram stanu sieci Wi-Fi: ustaw harmonogram sterowania pasmem Wi-Fi 5GHz / 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.

    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu może on lepiej odpowiadać Twoim potrzebom i preferencjom.

    Zapoznaj się z poradnikiem [Scheduled Tasks](../../interface_guide/scheduled_tasks.md), aby uzyskać szczegółowe instrukcje.

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie poprawnej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe są oznaczane czasem zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych zapisów i prawidłowego działania konfiguracji opartych na czasie.

    Zapoznaj się z poradnikiem [Time Zone](../../interface_guide/time_zone.md), aby uzyskać szczegółowe instrukcje.

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przycisku przełącznika na routerze, pozwalając przypisać mu określone funkcje dla szybkiego dostępu i sterowania. Funkcja ta zapewnia wygodne skróty do typowych zadań i ustawień, poprawiając komfort użytkowania oraz upraszczając zarządzanie routerem.

    Zapoznaj się z poradnikiem [Toggle Button Settings](../../interface_guide/toggle_button_settings.md), aby uzyskać szczegółowe instrukcje.

---

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa, korzystając z ustawień domyślnych bieżącego firmware.

    Zapoznaj się z poradnikiem [Reset Firmware](../../interface_guide/reset_firmware.md), aby uzyskać szczegółowe instrukcje.

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Strona obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki związane z działaniem i zdarzeniami kernela.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu internetowym i działaniu serwera.

    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez wsparcie techniczne. Funkcja ta jest niezwykle przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Zapoznaj się z poradnikiem [Log](../../interface_guide/log.md), aby uzyskać szczegółowe instrukcje.

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Zapoznaj się z poradnikiem [Advanced Settings](../../interface_guide/advanced_settings.md), aby uzyskać szczegółowe instrukcje.

## Deklaracja zgodności {#declaration-of-conformity}

Niniejszym GL TECHNOLOGIES (HONG KONG) LIMITED oświadcza, że typ urządzenia radiowego [Router Wi-Fi 6 AX3000, GL-MT3000] jest zgodny z zasadniczymi wymaganiami oraz innymi odpowiednimi postanowieniami dyrektywy 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
