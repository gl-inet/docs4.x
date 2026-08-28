# Przewodnik użytkownika Mango 2 (GL-MG1300)

## Przegląd produktu

Mango 2 (GL-MG1300) to pierwszy dwupasmowy minirouter podróżny Wi-Fi 5 firmy GL.iNet, wyróżniający się wyjątkowo cienką i przenośną konstrukcją. Oferuje teoretyczne prędkości 400 Mb/s (2,4 GHz) i 866 Mb/s (5 GHz) w konfiguracji MIMO 2×2. Ma fabrycznie zainstalowane OpenVPN i WireGuard, obsługuje ponad 30 usług VPN, automatycznie szyfruje cały ruch sieciowy i umożliwia zdalne zarządzanie przez GoodCloud, łącząc wydajność, funkcjonalność i bezpieczeństwo.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Mango 2 (GL-MG1300)
- 1 x Instrukcja obsługi
- 1 x Przewód zasilający USB-C–USB-C
- 1 x Karta z podziękowaniem

## Jak skonfigurować Mango 2

Aby skonfigurować Mango 2, użyj jednej z czterech obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering lub Cellular. Wykonaj poniższe czynności.

### 1. Włączenie zasilania

Podłącz przewód zasilający USB Type-C do portu zasilania routera. Drugi koniec podłącz do zasilacza 5 V/2 A (brak w zestawie), a następnie do gniazdka elektrycznego.

### 2. Podłączenie urządzenia

Połącz urządzenie (np. komputer, laptop lub smartfon) z routerem przez Wi-Fi lub Ethernet.

- Ethernet

    Połącz urządzenie z portem LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. Domyślna nazwa sieci i hasło są wydrukowane na etykiecie na spodzie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język, ustaw hasło administratora, a następnie kliknij **Apply**.

Jeśli zmienisz dane Wi-Fi, połącz urządzenie ponownie z siecią Wi-Fi routera przy użyciu zaktualizowanych danych logowania.

### 4. Konfiguracja Internetu

**Uwaga:** Poniższe instrukcje dotyczą konfiguracji routera za pomocą GL.iNet Web Admin Panel. Jeśli wolisz używać aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami na ekranie.

Skonfiguruj Mango 2 za pomocą jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering lub Cellular. Aby korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Podłącz port WAN routera Mango 2 do urządzenia nadrzędnego (np. modemu) za pomocą kabla Ethernet.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Ethernet na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym przejdź do sekcji Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wprowadź hasło, a następnie kliknij **Apply**.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Repeater na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB Mango 2 za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Settings i włącz **USB Tethering** lub **Personal Hotspot**. Na iPhonie stuknij **Trust This Device**, jeśli pojawi się taki monit.
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Tethering na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Do Mango 2 można podłączyć modem USB-C bezpośrednio albo użyć adaptera USB-C–USB-A w celu podłączenia modemu USB-A.

    Podłącz modem komórkowy USB do portu USB Mango 2. To przydatne rozwiązanie, jeśli chcesz udostępnić Internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Cellular na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Poniżej przedstawiono funkcje panelu administracyjnego Mango 2.

## Wireless

Strona Wireless umożliwia konfigurację sieci Main Network, Guest Network i IoT Network. Dla każdego typu sieci Wi-Fi można niezależnie skonfigurować pasma 5 GHz i 2,4 GHz. Można też włączyć i określić podstawowe ustawienia każdego pasma, takie jak SSID Wi-Fi, tryb zabezpieczeń, hasło i losowy BSSID.

Zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md).

## Clients

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity transfer oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GL.iNet Account"

    GL.iNet Account umożliwia łączenie urządzeń i usług chmurowych oraz zarządzanie nimi. Zapewnia łatwy dostęp do GoodCloud i glinet App, dzięki czemu można bezpiecznie i wygodnie zarządzać siecią z dowolnego miejsca i o każdej porze.

    Instrukcje konfiguracji zawiera strona [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} umożliwia łatwy zdalny dostęp do routerów GL.iNet i zarządzanie nimi.

=== "GoodPAS"

    GoodPAS to zaawansowana funkcja sieciowa zapewniająca płynny zdalny dostęp i zarządzanie urządzeniami. Rozwiązanie zaprojektowano specjalnie do integracji z routerami GL.iNet i wykorzystuje ono protokół AmneziaWG z wbudowanym maskowaniem ruchu, aby zapewnić bezpieczne i stabilne połączenia. Bezpiecznie udostępnia sieć domową z dowolnego miejsca na świecie, umożliwiając dostęp do zasobów domowych, podczas gdy cały ruch wygląda tak, jakby pochodził z publicznego adresu IP domu.

## VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Mango 2 obsługuje OpenVPN i WireGuard.

=== "OpenVPN"

    Mango 2 (oraz inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2 (oraz inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Sieć

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Subnet centralizuje zarządzanie sieciami LAN, Guest Network, IoT Network i niestandardowymi sieciami VLAN, umożliwiając tworzenie wielu podsieci i zarządzanie nimi w celu odizolowania różnych typów urządzeń lub ruchu.

    Instrukcje konfiguracji zawiera strona [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Zapoznaj się z poradnikiem [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakiem DNS rebinding oraz nadpisywanie ustawień DNS wszystkich klientów, zezwolenie na nadpisanie DNS VPN przez niestandardowy DNS, a także ustawienie trybu konfiguracji serwera DNS na automatyczny lub ręczne określenie serwerów DNS dla połączenia Ethernet.

    Zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Oferuje znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co ma kluczowe znaczenie przy stale rosnącej liczbie urządzeń podłączonych do Internetu.

    Zapoznaj się z poradnikiem [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci używana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontrolowania.

    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Strona Network Mode umożliwia dostosowanie roli operacyjnej routera do różnych potrzeb wdrożeniowych. Można wybrać tryby przeznaczone do scenariuszy od domowego zasięgu Wi-Fi po firmowe sieci wielołączowe; każdy tryb włącza lub wyłącza określone funkcje routera w celu optymalizacji wydajności.

    Instrukcje konfiguracji zawiera strona [Network Mode](../../interface_guide/network_mode.md).

=== "Network Acceleration"

    Network acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.

    Zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md).

## Kontrola przepływu

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować ich użycie. Obejmuje to ograniczanie czasu korzystania z ekranu oraz blokowanie dostępu do określonych treści.

    Zapoznaj się z poradnikiem [Parental controls](../../interface_guide/parental_control.md).

## Bezpieczeństwo

=== "Port Forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.

    Zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Admin Access"

    Admin Access umożliwia konfigurację różnych ustawień zabezpieczeń chroniących sieć i router przed nieautoryzowanym dostępem.

    Instrukcje konfiguracji zawiera strona [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    Strona NAT Settings umożliwia włączenie lub wyłączenie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Zapoznaj się z poradnikiem [NAT Settings](../../interface_guide/nat_settings.md).

## Aplikacje

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie.

    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskania dostępu do sieci zdalnej.

    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage oznacza scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć.

    Zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.

    Zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md).

## System

=== "Overview"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i wskaźników wydajności. Na tej stronie możesz sprawdzić:

    * Średnie obciążenie CPU: monitoruj średnie obciążenie procesora routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: sprawdzaj, jaka część pamięci routera jest aktualnie wykorzystywana, co pomaga w zarządzaniu zasobami.
    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Flash: sprawdzaj wykorzystanie pamięci flash routera, aby upewnić się, że dostępna jest wystarczająca ilość miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, hostname, model, architekturę, wersję OpenWrt, wersję kernela, device ID, device MAC i device S/N.
    * Pamięć zewnętrzna: sprawdzaj stan urządzeń pamięci zewnętrznej podłączonych do routera, takich jak dyski USB czy karty TF.

    Funkcje te zapewniają najważniejsze informacje i elementy sterujące, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Szczegółowe instrukcje znajdziesz w poradniku [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Admin Password umożliwia ustawienie lub zmianę hasła interfejsu administracyjnego routera.

    Hasło administratora musi spełniać następujące wymagania:

    * Co najmniej 10 i nie więcej niż 63 znaki.
    * Dozwolone są litery (wielkość liter ma znaczenie), cyfry i symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Wymagane są co najmniej dwa z następujących typów: wielkie litery, małe litery, cyfry i symbole.

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatycznie sprawdza i instaluje najnowszą wersję firmware bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera, co daje większą kontrolę nad wersją i terminem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w poradniku [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje na tej stronie obejmują:

    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Harmonogram restartu: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram statusu Wi-Fi: ustaw harmonogram sterowania pasmami Wi-Fi 5GHz / 2.4GHz , co ułatwia zarządzanie dostępnością sieci i zużyciem energii.

    Te opcje harmonogramu dają większą kontrolę nad pracą routera, dzięki czemu można dostosować go do własnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w poradniku [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe otrzymują dokładne znaczniki czasu zgodne z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia precyzyjnych rejestrów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w poradniku [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przycisku przełączania na routerze, dzięki czemu możesz przypisać mu określone funkcje w celu szybkiego dostępu i sterowania. Ta funkcja zapewnia wygodne skróty do typowych zadań i ustawień, poprawiając wygodę korzystania z urządzenia i upraszczając zarządzanie routerem.

    Szczegółowe instrukcje znajdziesz w poradniku [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa z domyślnymi ustawieniami obecnego firmware.

    Szczegółowe instrukcje znajdziesz w poradniku [Reset Firmware](../../interface_guide/reset_firmware.md).

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

---

**Deklaracja zgodności**

Niniejszym GL TECHNOLOGIES (HONG KONG) LIMITED oświadcza, że typ urządzenia radiowego [Dwuzakresowy mini router podróżny, GL‑MG1300] jest zgodny z zasadniczymi wymaganiami i innymi odpowiednimi przepisami dyrektywy 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
