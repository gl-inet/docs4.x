# Przewodnik użytkownika Beryl 7 (GL-MT3600BE)

## Przegląd produktu

Beryl 7 (GL-MT3600BE) to dwupasmowy przenośny router podróżny Wi-Fi 7, zaprojektowany specjalnie z myślą o zastosowaniach mobilnych, takich jak podróże służbowe i wakacje. Jako ulepszona wersja Beryl AX obsługuje technologie Wi-Fi 7, w tym Multi-Link Operation (MLO) oraz 4K QAM, osiągając teoretyczne dwupasmowe prędkości 688Mbps (2.4GHz) + 2882Mbps (5GHz), co pozwala sprostać wymaganiom szybkich zastosowań, takich jak streaming 8K i gry mobilne.

Router napędzany jest czterordzeniowym procesorem MediaTek i wyposażony w 512MB pamięci NAND flash, co zapewnia stabilną wielozadaniowość i kompatybilność z różnymi wtyczkami OpenWrt. Ma 2x porty Ethernet 2.5G oraz 1x port USB 3.0, dzięki czemu sprawdza się zarówno przy szybkich połączeniach przewodowych, jak i przy rozszerzaniu pamięci masowej. Dzięki zgodności z PD może być zasilany standardowym przewodem od ładowarki do telefonu, co zmniejsza wagę i liczbę akcesoriów w bagażu. Router może jednocześnie obsługiwać ponad 120 urządzeń, a jego smukła, przenośna konstrukcja została stworzona z myślą o podróży.

![gl-mt3600be interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/hardware_info/mt3600be_interface.png){class="glboxshadow"}

## Zawartość opakowania

- 1 x Beryl 7 (GL-MT3600BE)
- 1 x Zasilacz
- 1 x Kabel Ethernet
- 1 x Instrukcja obsługi
- 1 x Kartka z podziękowaniem
- 3 x Przejściówki (wtyczki EU, UK i AU)

Obejrzyj poniższy film z rozpakowania Beryl 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xZHmP3B8VlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Jak skonfigurować Beryl 7

Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ey-Z3MEOPpw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz komputer lub urządzenie mobilne do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet. 

- Wi-Fi

    Na swoim urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło, aby połączyć się z siecią. (Domyślną nazwę sieci i hasło znajdziesz na etykiecie.)

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

### 4. Konfiguracja Internetu

**Note:** Poniższe instrukcje dotyczą użytkowników konfigurujących router przez webowy panel administracyjny GL.iNet. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Beryl 7, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_ethernet.png){class="glboxshadow"}
    
    Podłącz port WAN routera Beryl 7 do urządzenia nadrzędnego (np. modemu) za pomocą kabla Ethernet.
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Ethernet na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym przejdź do sekcji Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci. 
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Repeater na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB Beryl 7 za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering. 
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering. 
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Tethering na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_cellular.png){class="glboxshadow"}

    Podłącz modem komórkowy USB do portu USB Beryl 7. To przydatne rozwiązanie, jeśli chcesz udostępnić Internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Cellular na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w poradniku [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Poniżej znajdziesz przegląd funkcji dostępnych w webowym panelu administracyjnym Beryl 7.

## Wireless

Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5GHz i 2.4GHz, w tym włączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

Dodatkowo Beryl 7 obsługuje Wi-Fi MLO, czyli Multi-Link Operation, łącząc jednocześnie wiele sieci bezprzewodowych, aby uzyskać większą przepustowość i bardziej niezawodne połączenia.

Zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md).

## Clients

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity transfer oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi. 
    
    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej pracy w sieci zdalnej oraz zdalnym zarządzaniu urządzeniami. Stworzona specjalnie do integracji z routerami GL.iNet, AstroWarp obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią oraz planowanemu wsparciu dla kontroli na poziomie sprzętowym AstroWarp oferuje solidniejsze i bardziej niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci. 
    
    Zapoznaj się z poradnikiem [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany tunel dla ruchu między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Beryl 7 obsługuje OpenVPN, WireGuard i Tor.

=== "OpenVPN" 

    Beryl 7 (oraz inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Beryl 7 (oraz inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na prywatność, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów obsługiwanych przez wolontariuszy (węzłów), aby ukryć lokalizację i sposób korzystania z sieci przez użytkownika, utrudniając śledzenie aktywności online. 
    
    * [How to set up Tor](../../interface_guide/tor.md)

## Applications

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie. 
    
    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskania dostępu do sieci zdalnej. 
    
    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage oznacza scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć. 
    
    Zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i mechanizmów śledzących, które działa jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej. 
    
    Zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować ich użycie. Obejmuje to ograniczanie czasu korzystania z ekranu oraz blokowanie dostępu do określonych treści.

    Zapoznaj się z poradnikiem [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieciowe definiowane programowo, które umożliwia tworzenie bezpiecznych, wirtualnych sieci przez Internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej. 
    
    Zapoznaj się z poradnikiem [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca. 
    
    Zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md).

## Network

=== "Port forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej. 
    
    Zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md). 

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu. 

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą. 
    
    Zapoznaj się z poradnikiem [Lan](../../interface_guide/lan.md). 

---

=== "Guest Network"

    Strona Guest Network umożliwia ustawienie podsieci w zakresie prywatnych adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz skonfigurowanie ustawień zabezpieczeń, takich jak izolacja AP dla sieci gościnnej.

    Zapoznaj się z poradnikiem [Guest Network](../../interface_guide/guest_network.md). 

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakiem DNS rebinding oraz nadpisywanie ustawień DNS wszystkich klientów, zezwolenie na nadpisanie DNS VPN przez niestandardowy DNS, a także ustawienie trybu konfiguracji serwera DNS na automatyczny lub ręczne określenie serwerów DNS dla połączenia Ethernet.

    Zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Zapoznaj się z poradnikiem [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "Network Mode"

    Network mode odnosi się do ustawień konfiguracyjnych określających, w jaki sposób urządzenie łączy się z siecią i komunikuje z innymi urządzeniami. 
    
    Zapoznaj się z poradnikiem [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Oferuje znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co ma kluczowe znaczenie przy stale rosnącej liczbie urządzeń podłączonych do Internetu. 
    
    Zapoznaj się z poradnikiem [IPV6](../../interface_guide/network_mode.md).

---

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN. 
    
    Zapoznaj się z poniższymi poradnikami:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci używana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontrolowania. 
    
    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Network acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.
    
    Zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączenie lub wyłączenie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Zapoznaj się z poradnikiem [NAT Settings](../../interface_guide/nat_settings.md).

## System

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

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatycznie sprawdza i instaluje najnowszą wersję firmware bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera, co daje większą kontrolę nad wersją i terminem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Szczegółowe instrukcje znajdziesz w poradniku [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje na tej stronie obejmują:

    * Harmonogram działania diod LED: ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć ilość światła w określonych godzinach.
    * Harmonogram restartu: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram statusu Wi-Fi: ustaw harmonogram sterowania pasmami Wi-Fi 5GHz / 2.4GHz / MLO, co ułatwia zarządzanie dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu dają większą kontrolę nad pracą routera, dzięki czemu można dostosować go do własnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w poradniku [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe otrzymują dokładne znaczniki czasu zgodne z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia precyzyjnych rejestrów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w poradniku [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przycisku przełączania na routerze, dzięki czemu możesz przypisać mu określone funkcje w celu szybkiego dostępu i sterowania. Ta funkcja zapewnia wygodne skróty do typowych zadań i ustawień, poprawiając wygodę korzystania z urządzenia i upraszczając zarządzanie routerem.

    Szczegółowe instrukcje znajdziesz w poradniku [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Ta strona obejmuje:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem kernela i zdarzeniami systemowymi.
    * Crash Log: zapisy awarii i błędów systemu, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, przedstawiające ruch sieciowy i działanie serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez pomoc techniczną. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w poradniku [Log](../../interface_guide/log.md).

---

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień zabezpieczeń, aby chronić sieć i router przed nieautoryzowanym dostępem. Ta strona obejmuje opcje takie jak:

    * Admin Password: ustaw lub zmień hasło do panelu administracyjnego routera, aby tylko upoważnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i ograniczaj go.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera z lokalizacji zdalnych przez Internet, zwiększając bezpieczeństwo przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w poradniku [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa z domyślnymi ustawieniami obecnego firmware.

    Szczegółowe instrukcje znajdziesz w poradniku [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera wykraczających poza podstawowy interfejs. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory sieciowej i inne zaawansowane dostosowania systemowe.

    Szczegółowe instrukcje znajdziesz w poradniku [Advanced Settings](../../interface_guide/advanced_settings.md).
