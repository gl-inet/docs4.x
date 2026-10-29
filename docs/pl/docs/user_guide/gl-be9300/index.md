# Przewodnik użytkownika Flint 3 (GL-BE9300) {#flint-3-gl-be9300-user-guide}

## Przegląd produktu {#product-overview}

Flint 3 (GL-BE9300) to trójpasmowy router biurkowy Wi-Fi 7 przeznaczony do użytku domowego, małych biur i wymagających zastosowań. Obsługuje Wi-Fi 7 Multi-Link Operation (MLO), inteligentnie łącząc pasma 2.4GHz, 5GHz i 6GHz w jedno połączenie, aby ograniczyć zakłócenia i przeciążenie sieci. W połączeniu z 4K QAM oferuje teoretyczne prędkości trójpasmowe 688Mbps (2.4GHz), 2882Mbps (5GHz) oraz 5765Mbps (6GHz). Łączność MLO lub 6GHz zapewnia najwyższą wydajność, a pasmo 2.4GHz można przeznaczyć dla urządzeń IoT.

Router jest wyposażony w 5× portów Ethernet 2.5G (1 dedykowany WAN, 1 przełączalny WAN/LAN, 3 LAN), obsługuje konfiguracje dual-WAN z maksymalną współdzieloną przepustowością 5Gbps oraz 1× port USB 3.0, który rozszerza jego funkcjonalność. Dodatkowo ma fabrycznie zainstalowany AdGuard Home do blokowania reklam i mechanizmów śledzących, obsługuje Bark Parental Control oraz ponad 30 usług VPN, a także umożliwia zdalne zarządzanie przez GoodCloud — zapewniając doskonałą równowagę między wydajnością, praktycznością i bezpieczeństwem.

![gl-be9300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/hardware_info/be9300_interface.jpg){class="glboxshadow"}

## Zawartość opakowania {#package-contents}

- 1 x Flint 3 (GL-BE9300)
- 1 x Zasilacz
- 1 x Kabel Ethernet
- 1 x Instrukcja obsługi
- 1 x Kartka z podziękowaniem
- 1 x Przejściówka (zależnie od kraju dostawy)

Obejrzyj poniższy film z rozpakowania Flint 3.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qAq6IFtKtj0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Jak skonfigurować Flint 3 {#how-to-set-up-flint-3}

Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/WQqD-8NrAOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania {#1-power-on}

Złóż dwuczęściowy zasilacz. Podłącz go do routera i do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia {#2-connect-device}

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet. 

- Wi-Fi

    Na swoim urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło, aby połączyć się z siecią. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Logowanie do panelu administracyjnego {#3-log-in-to-web-admin-panel}

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

### 4. Konfiguracja Internetu {#4-internet-setup}

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router przez webowy panel administracyjny GL.iNet. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Flint 3, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_ethernet.jpg){class="glboxshadow"}

    Podłącz port WAN routera Flint 3 do urządzenia nadrzędnego (np. modemu) za pomocą kabla Ethernet. 
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Ethernet na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_repeater.jpg){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym przejdź do sekcji Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci. 
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Repeater na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_tethering.jpg){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering. 
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering. 
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Tethering na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_cellular.jpg){class="glboxshadow"}

    Podłącz modem komórkowy USB do portu USB routera Flint 3. To przydatne rozwiązanie, jeśli chcesz udostępnić Internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Cellular na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---
    
Poniżej znajdziesz przegląd funkcji dostępnych w webowym panelu administracyjnym Flint 3.

## Wireless {#wireless}

Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 6GHz, 5GHz i 2.4GHz, w tym włączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału. 
    
Dodatkowo Flint 3 obsługuje Wi-Fi MLO, czyli Multi-Link Operation, łącząc jednocześnie wiele sieci bezprzewodowych, aby uzyskać większą przepustowość i bardziej niezawodne połączenia.

Zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh to funkcja oparta na standardzie Wi-Fi EasyMesh™, która rozszerza zasięg Wi-Fi na cały dom i umożliwia płynny roaming. Jeśli masz kilka routerów GL.iNet, ustaw jeden jako router główny, a pozostałe jako węzły mesh, aby zapewnić płynny roaming Wi-Fi w całym domu.

Aby skonfigurować Mesh, zapoznaj się z [Mesh](../../interface_guide/mesh.md).

## Clients {#clients}

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity transfer oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi chmurowe {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account umożliwia łączenie urządzeń i usług chmurowych oraz zarządzanie nimi. Zapewnia łatwy dostęp do GoodCloud i glinet App, dzięki czemu można bezpiecznie i wygodnie zarządzać siecią z dowolnego miejsca i o każdej porze.

    Instrukcje konfiguracji zawiera strona [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi. 
    
    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS to zaawansowana funkcja sieciowa zapewniająca płynny zdalny dostęp i zarządzanie urządzeniami. Rozwiązanie zaprojektowano specjalnie do integracji z routerami GL.iNet i wykorzystuje ono protokół AmneziaWG z wbudowanym maskowaniem ruchu, aby zapewnić bezpieczne i stabilne połączenia. GoodPAS umożliwia zdalny dostęp do sieci domowej. Gdy router domowy pełni funkcję węzła wyjściowego GoodPAS, ruch internetowy wysyłany przez GoodPAS korzysta z publicznego adresu IP WAN tego routera.

    Instrukcje konfiguracji zawiera strona [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Flint 3 obsługuje OpenVPN i WireGuard.

=== "OpenVPN" 
    
    Flint 3 (oraz inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 3 (oraz inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu. 

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "Subnet"

    Ta strona umożliwia centralną konfigurację i zarządzanie sieciami **Main Network**, **Guest Network**, **IoT Network** oraz niestandardowymi **VLAN Networks**. Możesz tworzyć wiele podsieci i zarządzać nimi, aby izolować różne typy urządzeń lub ruchu.

    Instrukcje konfiguracji zawiera strona [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Zapoznaj się z poradnikiem [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding, nadpisanie ustawień DNS wszystkich klientów oraz zezwolenie niestandardowym serwerom DNS na zastąpienie DNS VPN. Możesz korzystać z serwerów DNS automatycznie uzyskanych z urządzeń nadrzędnych lub ręcznie wskazać niestandardowe serwery DNS.

    Zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Oferuje znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co ma kluczowe znaczenie przy stale rosnącej liczbie urządzeń podłączonych do Internetu. 
    
    Zapoznaj się z poradnikiem [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci używana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontrolowania. 
    
    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).
    
---

=== "Network Mode"

    Strona Network Mode umożliwia dostosowanie roli operacyjnej routera do różnych potrzeb wdrożeniowych. Można wybrać tryby przeznaczone do scenariuszy od domowego zasięgu Wi-Fi po firmowe sieci wielołączowe; każdy tryb włącza lub wyłącza określone funkcje routera w celu optymalizacji wydajności.

    Instrukcje konfiguracji zawiera strona [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera, zapewniając m.in. AdGuard Home, szyfrowany DNS i klienta VPN. 
    
    Aby skonfigurować Drop-in Gateway, skorzystaj z poniższych poradników:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.
    
    Zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md).

## Kontrola ruchu {#flow-control}

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

    Aby skonfigurować kontrolę rodzicielską, zapoznaj się z sekcją [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Bezpieczeństwo {#security}

=== "Port Forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.
    
    Zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL (Access Control List) umożliwia tworzenie reguł zarządzania ruchem na podstawie protokołów połączeń, adresów urządzeń i portów. Reguły określają, czy zezwalać na dostęp do sieci, czy go blokować. Jeśli kilka reguł ACL jest ze sobą sprzecznych, system stosuje regułę o wyższym priorytecie.

    Szczegółowe informacje zawiera strona [ACL](../../interface_guide/acl.md).

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

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i mechanizmów śledzących, które działa jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej. 
    
    Zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Bark"

    Usługa Bark zintegrowana z Flint 3 pomaga chronić cyfrowe środowisko dziecka i zapewnia kompleksową ochronę online. Zwykle wymaga płatnej subskrypcji. W ramach współpracy z Bark firma GL.iNet oferuje jednak plan Bark Home bezpłatnie na wybranych modelach routerów, w tym Flint 3, zapewniając zaawansowane monitorowanie i alerty bez dodatkowych opłat.

    Szczegółowe informacje zawiera strona [Bark](../../interface_guide/bark.md).

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

    * Średnie obciążenie CPU: monitoruj średnie obciążenie procesora routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: sprawdzaj, jaka część pamięci routera jest aktualnie wykorzystywana, co pomaga w zarządzaniu zasobami.
    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Użycie pamięci flash: sprawdzaj wykorzystanie pamięci flash routera, aby upewnić się, że dostępna jest wystarczająca ilość miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, hostname, model, architekturę, wersję OpenWrt, wersję kernela, device ID, device MAC i device S/N.
    * Pamięć zewnętrzna: sprawdzaj stan urządzeń pamięci zewnętrznej podłączonych do routera, takich jak dyski USB czy karty TF.
    
    Funkcje te zapewniają najważniejsze informacje i elementy sterujące, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Szczegółowe instrukcje znajdziesz w poradniku [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Admin Password umożliwia zarządzanie hasłem interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli zmieniać ustawienia.

    Szczegółowe informacje zawiera strona [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie dostępności najnowszej wersji firmware na serwerze producenta. Jeśli jest dostępna online, możesz ją zainstalować.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera, co daje większą kontrolę nad wersją i terminem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w poradniku [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje na tej stronie obejmują:

    * Harmonogram działania diod LED: ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć ilość światła w określonych godzinach.
    * Harmonogram restartu: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram statusu Wi-Fi: ustaw harmonogram sterowania pasmami Wi-Fi 6GHz / 5GHz / 2.4GHz / MLO, co ułatwia zarządzanie dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu dają większą kontrolę nad pracą routera, dzięki czemu można dostosować go do własnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w poradniku [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe otrzymują dokładne znaczniki czasu zgodne z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia precyzyjnych rejestrów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w poradniku [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa z domyślnymi ustawieniami obecnego firmware.

    Szczegółowe informacje zawiera strona [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Ta strona obejmuje:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem kernela i zdarzeniami systemowymi.
    * Crash Log: zapisy awarii i błędów systemu, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, przedstawiające ruch sieciowy i działanie serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez pomoc techniczną. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w poradniku [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera wykraczających poza podstawowy interfejs. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory sieciowej i inne zaawansowane dostosowania systemowe.

    Szczegółowe instrukcje znajdziesz w poradniku [Advanced Settings](../../interface_guide/advanced_settings.md).

## Deklaracja zgodności {#declaration-of-conformity}

Niniejszym GL TECHNOLOGIES (HONG KONG) LIMITED oświadcza, że typ urządzenia radiowego [Router Wi-Fi 7 BE9300, GL-BE9300] jest zgodny z zasadniczymi wymaganiami i innymi stosownymi postanowieniami dyrektywy 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
