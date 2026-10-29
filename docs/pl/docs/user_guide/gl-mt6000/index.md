# Przewodnik użytkownika Flint 2 (GL-MT6000) {#flint-2-gl-mt6000-user-guide}

## Omówienie produktu {#product-overview}

Flint 2 (GL-MT6000) to router Wi-Fi 6 do domu i biura, idealnie sprawdzający się przy intensywnej transmisji danych, dużej liczbie jednocześnie podłączonych urządzeń oraz w środowiskach wymagających bardzo niskich opóźnień, takich jak gry online. Flint 2 oferuje błyskawiczne prędkości WireGuard VPN do 900Mbps. Obsługuje także zaawansowane mechanizmy redundancji sieciowej, w tym Multi-WAN, przełączenie awaryjne i Load balance, aby zapewnić nieprzerwaną pracę sieci.

![gl-mt6000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/hardware_info/gl-mt6000_interface.jpg){class="glboxshadow"}

## Zawartość opakowania {#package-contents}

- 1 x Flint 2 (GL-MT6000)
- 1 x instrukcja obsługi
- 1 x karta z podziękowaniem
- 1 x kabel Ethernet
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![gl-mt6000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/first_time_setup/gl-mt6000_unboxing.jpg){class="glboxshadow"}

Obejrzyj poniżej film z rozpakowania Flint 2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ru1O-zxKgKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Jak skonfigurować Flint 2 {#how-to-set-up-flint-2}

Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(W tym filmie do demonstracji konfiguracji użyto innego routera GL.iNet, ale kroki są takie same dla Flint 2 i innych modeli routerów.)</small>

### 1. Włącz zasilanie {#1-power-on}

Złóż dwuczęściowy zasilacz. Podłącz go do routera i do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłącz urządzenie {#2-connect-device}

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet. 

- Wi-Fi

    Na swoim urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło, aby połączyć się z siecią. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Zaloguj się do web Admin Panel {#3-log-in-to-web-admin-panel}

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**. 

Podczas potwierdzania danych Wi-Fi pamiętaj, że jeśli zmienisz informacje o Wi-Fi, konieczne będzie ponowne połączenie urządzenia z siecią Wi-Fi routera przy użyciu zaktualizowanych danych uwierzytelniających.

### 4. Konfiguracja internetu {#4-internet-setup}

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router przez GL.iNet Web Admin Panel. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Flint 2, korzystając z jednej z obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem. 
    
    Po pomyślnym połączeniu z internetem zielona kropka pojawi się w sekcji Ethernet na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w artykule [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w web Admin Panel przejdź do sekcji Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci. 
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z internetem zielona kropka pojawi się w sekcji Repeater na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w artykule [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering. 
    3. Na stronie INTERNET w web Admin Panel kliknij **Connect** w sekcji Tethering. 
    
    Po pomyślnym połączeniu z internetem zielona kropka pojawi się w sekcji Tethering na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w artykule [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_cellular.png){class="glboxshadow"}

    Podłącz modem komórkowy USB do portu USB routera. To przydatne rozwiązanie, jeśli chcesz udostępnić internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z internetem zielona kropka pojawi się w sekcji Cellular na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w artykule [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md). 

---

## DNS {#dns}

Ustawienia DNS routera określają sposób rozwiązywania nazw domen na adresy IP. Na tej stronie możesz korzystać z serwerów DNS uzyskanych automatycznie z urządzeń nadrzędnych lub ustawić własne. Możesz również skonfigurować opcje DNS i edytować statyczne reguły hostów.

Więcej informacji znajdziesz w sekcji [DNS](../../interface_guide/dns_v4.11.md).

## Wireless {#wireless}

Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5GHz i 2.4GHz, w tym włączanie i wyłączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie i wyłączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi, ustawianie hasła Wi-Fi, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

Zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh to funkcja oparta na standardzie Wi-Fi EasyMesh™, która rozszerza zasięg Wi-Fi na cały dom i umożliwia płynny roaming. Jeśli masz kilka routerów GL.iNet, ustaw jeden jako router główny, a pozostałe jako węzły mesh, aby zapewnić płynny roaming Wi-Fi w całym domu.

Więcej informacji znajdziesz w sekcji [Mesh](../../interface_guide/mesh.md).

## CLIENTS {#clients}

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę urządzenia, typ połączenia (tj. przez Ethernet lub Wi-Fi), adresy IP i MAC, prędkości pobierania i wysyłania, całkowity transfer oraz umożliwia rezerwację adresu IP, zablokowanie klienta lub wykonanie innych działań.

Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi chmurowe {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account umożliwia łączenie urządzeń i usług chmurowych oraz zarządzanie nimi. Zapewnia łatwy dostęp do GoodCloud i glinet App, dzięki czemu można bezpiecznie i wygodnie zarządzać siecią z dowolnego miejsca i o każdej porze.

    Instrukcje konfiguracji zawiera strona [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi. 
    
    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS to zaawansowana funkcja sieciowa zapewniająca płynny zdalny dostęp i zarządzanie urządzeniami. Rozwiązanie zaprojektowano specjalnie do integracji z routerami GL.iNet i wykorzystuje ono protokół AmneziaWG z wbudowanym maskowaniem ruchu, aby zapewnić bezpieczne i stabilne połączenia. GoodPAS umożliwia zdalny dostęp do sieci domowej. Gdy router domowy pełni funkcję węzła wyjściowego GoodPAS, ruch internetowy wysyłany przez GoodPAS korzysta z publicznego adresu IP WAN tego routera.

    Instrukcje konfiguracji zawiera strona [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Flint 2 (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard.

=== "OpenVPN" 

    Flint 2 (oraz inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 2 (oraz inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Sieć {#network}

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu. 

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    Strona LAN umożliwia scentralizowaną konfigurację sieci głównej, sieci gościnnej, sieci IoT i niestandardowych sieci VLAN oraz zarządzanie nimi. Możesz tworzyć wiele podsieci i zarządzać nimi, aby izolować różne typy urządzeń lub ruchu.

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Zapoznaj się z poradnikiem [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Oferuje znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co ma kluczowe znaczenie przy stale rosnącej liczbie urządzeń podłączonych do internetu.

    Szczegółowe instrukcje znajdziesz w artykule [IPV6](../../interface_guide/ipv6.md).

<br>

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.

    Szczegółowe instrukcje znajdziesz w artykule [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Strona Network Mode umożliwia dostosowanie roli operacyjnej routera do różnych potrzeb wdrożeniowych. Można wybrać tryby przeznaczone do scenariuszy od domowego zasięgu Wi-Fi po firmowe sieci wielołączowe; każdy tryb włącza lub wyłącza określone funkcje routera w celu optymalizacji wydajności.

    Instrukcje konfiguracji zawiera strona [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera, w tym AdGuard Home, szyfrowany DNS i klienta VPN.

    Aby skonfigurować Drop-in Gateway, skorzystaj z poniższych poradników:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Konfiguracja Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Akceleracja sieciowa może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.

    Szczegółowe instrukcje znajdziesz w artykule [Network Acceleration](../../interface_guide/network_acceleration.md).

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

<br>

=== "QoS"

    QoS (Quality of Service) optymalizuje przydział pasma, nadając priorytet kluczowym działaniom, takim jak rozmowy wideo lub gry, podczas przeciążenia sieci. Zmniejsza opóźnienia i poprawia ogólną wydajność. Funkcja obejmuje ruch klientów lokalnych i ruch tunelu klienta VPN, ale nie ruch odbierany, gdy router działa jako serwer VPN.

    Szczegółowe informacje zawiera strona [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i „bufferbloat”, zapewniając płynniejsze działanie gier i połączeń głosowych.

    Szczegółowe informacje zawiera strona [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować ich użycie. Obejmuje to ograniczanie czasu korzystania z ekranu oraz blokowanie dostępu do określonych treści. 

    Aby skonfigurować kontrolę rodzicielską, zapoznaj się z sekcją [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Bezpieczeństwo {#security}

=== "Security Scan"

    Security Scan przeprowadza kontrolę bezpieczeństwa routera. Ocenia jego ustawienia zabezpieczeń i generuje wynik oceny bezpieczeństwa wraz z alertami o zagrożeniach i sugestiami optymalizacji. Możesz dostosować konfigurację na podstawie wyników skanowania, aby poprawić bezpieczeństwo routera.

    Więcej informacji znajdziesz w sekcji [Security Scan](../../interface_guide/security_scan.md).

=== "ACL"

    ACL (Access Control List) umożliwia tworzenie reguł zarządzania ruchem na podstawie protokołów połączeń, adresów urządzeń i portów. Reguły określają, czy zezwalać na dostęp do sieci, czy go blokować. Jeśli kilka reguł ACL jest ze sobą sprzecznych, system stosuje regułę o wyższym priorytecie.

    Szczegółowe informacje zawiera strona [ACL](../../interface_guide/acl.md).

=== "Port Forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej. 

    Aby skonfigurować przekierowanie portów, zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md).

<br>

=== "UPnP"

    UPnP (Universal Plug and Play) umożliwia zgodnym urządzeniom i aplikacjom LAN automatyczne żądanie mapowania portów na routerach GL.iNet. Mapowania te przekierowują przychodzący ruch WAN na określone adresy IP i porty LAN, umożliwiając klientom zewnętrznym łączenie się z lokalnymi usługami bez ręcznego konfigurowania reguł przekierowania portów.

    Więcej informacji znajdziesz w sekcji [UPnP](../../interface_guide/upnp.md).

=== "Admin Access"

    Admin Access umożliwia konfigurowanie różnych ustawień zabezpieczeń chroniących sieć i router przed nieuprawnionym dostępem. Strona zawiera następujące opcje:

    * Local Access Control: zarządzaj dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i ograniczaj go.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera z lokalizacji zdalnych przez Internet, zwiększając bezpieczeństwo przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki i nieautoryzowany dostęp.

    Szczegółowe informacje zawiera strona [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    Strona NAT Mode umożliwia włączenie albo wyłączenie funkcji Full Cone NAT i SIP ALG.

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Mode](../../interface_guide/nat_settings.md).

## Applications {#applications}

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie. 
    
    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Mapuje nazwę domeny na dynamiczny publiczny adres IP routera, dzięki czemu możesz zdalnie uzyskiwać dostęp do swojej sieci bez statycznego adresu IP. 
    
    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage oznacza scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć. 
    
    Zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md).

<br>

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i mechanizmów śledzących, które działa jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej. 
    
    Zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca. 
    
    Zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieciowe definiowane programowo, które umożliwia tworzenie bezpiecznych, wirtualnych sieci przez Internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej. 
    
    Zapoznaj się z poradnikiem [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na prywatność, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów obsługiwanych przez wolontariuszy (węzłów), aby ukryć lokalizację i sposób korzystania z sieci przez użytkownika, utrudniając śledzenie aktywności online. 

    Szczegółowe informacje zawiera strona [Tor](../../interface_guide/tor.md).

## System {#system}

=== "Overview"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i wskaźników wydajności. Na tej stronie możesz sprawdzić:

    * Średnie obciążenie CPU: monitorowanie średniego obciążenia procesora routera pomaga ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: sprawdzenie, jaka część pamięci routera jest aktualnie wykorzystywana, pomaga w zarządzaniu zasobami.
    * Sterowanie diodami LED: włączanie lub wyłączanie diod LED routera umożliwia dostosowanie wizualnych wskaźników urządzenia.
    * Użycie pamięci flash: podgląd wykorzystania pamięci flash routera pozwala upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: dostęp do szczegółowych informacji o systemie routera, w tym czasu pracy, nazwy hosta, modelu, architektury, wersji OpenWrt, wersji jądra, identyfikatora urządzenia, adresu MAC urządzenia i numeru seryjnego.
    * Pamięć zewnętrzna: sprawdzenie stanu zewnętrznych nośników danych podłączonych do routera, takich jak dyski USB lub karty TF.

    Funkcje te zapewniają najważniejsze informacje i elementy sterujące, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Szczegółowe instrukcje znajdziesz w artykule [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Admin Password umożliwia zarządzanie hasłem interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli zmieniać ustawienia.

    Szczegółowe informacje zawiera strona [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie dostępności najnowszej wersji firmware na serwerze producenta. Jeśli jest dostępna online, możesz ją zainstalować.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera, co daje większą kontrolę nad wersją i terminem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w artykule [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje na tej stronie obejmują:

    * Harmonogram działania diod LED: ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć ilość światła w określonych godzinach.
    * Harmonogram restartu: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram statusu Wi-Fi 5GHz / 2.4GHz: ustaw harmonogram sterowania pasmami Wi-Fi 5GHz / 2.4GHz, co ułatwia zarządzanie dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu dają większą kontrolę nad pracą routera, dzięki czemu można dostosować go do własnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w artykule [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe otrzymują dokładne znaczniki czasu zgodne z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia precyzyjnych rejestrów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w artykule [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa z domyślnymi ustawieniami obecnego firmware.

    Szczegółowe instrukcje znajdziesz w artykule [Reset Firmware](../../interface_guide/reset_firmware.md).

<br>

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Ta strona obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki związane z działaniem jądra i zdarzeniami systemowymi.
    * Crash Log: zapisy awarii i błędów systemu, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera WWW Nginx, jeśli jest używany przez router, przedstawiające ruch sieciowy i działanie serwera.

    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez pomoc techniczną. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w artykule [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera wykraczających poza podstawowy interfejs. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory sieciowej i inne zaawansowane dostosowania systemowe.

    Szczegółowe instrukcje znajdziesz w artykule [Advanced Settings](../../interface_guide/advanced_settings.md).

## Deklaracja zgodności {#declaration-of-conformity}

Niniejszym GL TECHNOLOGIES (HONG KONG) LIMITED oświadcza, że typ urządzenia radiowego [AX6000 Wireless Router, GL-MT6000] jest zgodny z zasadniczymi wymaganiami i innymi stosownymi postanowieniami dyrektywy 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
