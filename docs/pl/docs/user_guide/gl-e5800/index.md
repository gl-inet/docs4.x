# Przewodnik użytkownika Mudi 7 (GL-E5800)

## Omówienie produktu

Mudi 7 to przenośny router podróżny 5G NR Wi-Fi 7 zaprojektowany z myślą o osobach często podróżujących i użytkownikach biznesowych. Zapewnia niezawodną, prywatną sieć, która pomaga chronić dane przed cyberzagrożeniami. Oferuje superszybką łączność 5G, automatyczne przełączanie dwóch kart SIM (przełączenie awaryjne) oraz Wi-Fi 7 (kanały 320 MHz i 4K QAM), dzięki czemu zapewnia stabilne i szybkie połączenie, szybkie pobieranie, strumieniowanie 4K oraz wideokonferencje bez opóźnień nawet w zatłoczonych miejscach.

Wyposażony w ekran dotykowy Mudi 7 umożliwia monitorowanie w czasie rzeczywistym zużycia danych, siły sygnału, podłączonych urządzeń i prędkości klientów, a także zmianę ustawień za pomocą prostych dotknięć, zapewniając intuicyjną i bezproblemową obsługę.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Zawartość opakowania

- 1 x Mudi 7 (GL-E5800)
- 1 x akumulator
- 1 x kabel USB-C 10 Gbps
- 1 x etui podróżne
- 1 x instrukcja obsługi

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Obejrzyj poniżej film z rozpakowania Mudi 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Jak skonfigurować Mudi 7

Obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Zainstaluj kartę SIM

Włóż kartę Nano-SIM lub karty Nano-SIM do Mudi 7. Jeśli wolisz korzystać z eSIM, pomiń ten krok i przejdź do kroku 2.

Najpierw zdejmij pokrywę baterii, a następnie wyjmij akumulator Mudi 7.

Następnie włóż kartę Nano-SIM lub karty Nano-SIM. Jeśli używasz tylko jednej karty, włóż ją do gniazda SIM 1.

Na koniec włóż z powrotem akumulator i załóż pokrywę.

![install nano-sim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/install_nano-sim.png){class="glboxshadow"}

### 2. Włącz zasilanie

Naciśnij i przytrzymaj przycisk zasilania przez **3 sekundy** albo podłącz zasilacz.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power_on.png){class="glboxshadow"}

### 3. Ustawienia podstawowe

Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby skonfigurować podstawowe ustawienia, w tym **kod blokady ekranu**, **hasło administratora**, **nazwę Wi-Fi**, **hasło Wi-Fi** oraz **pasma częstotliwości**.

**Wskazówka**: Domyślne hasło administratora to ostatnie 9 znaków numeru seryjnego urządzenia (S/N), po których występuje znak #. Możesz użyć hasła domyślnego albo ustawić własne.

### 4. Konfiguracja internetu

Skonfiguruj Mudi 7, korzystając z jednej z obsługiwanych metod połączenia z internetem: Cellular, Ethernet, Repeater, Tethering oraz USB Ethernet. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}
    
    Mudi 7 ma **wbudowaną kartę eSIM** oraz **dwa gniazda Nano-SIM**. Z internetem możesz połączyć się, kupując pakiet eSIM (bez fizycznej karty SIM), albo wkładając karty Nano-SIM, aby uzyskać dostęp do mobilnej sieci 5G.
    
    - eSIM: Na ekranie dotykowym przejdź do **Cellular** -> **Active SIM Card**, włącz eSIM, a następnie prześlij profil eSIM przez web Admin Panel albo kup go w eSIM Profile Store.

    - Nano-SIM: Zdejmij tylną pokrywę Mudi 7, wyjmij akumulator, włóż kartę Nano-SIM do gniazda, a następnie ponownie zamontuj akumulator.

    Po pomyślnym połączeniu z internetem paski siły sygnału i stan połączenia komórkowego pojawią się w prawym górnym rogu ekranu dotykowego. Szczegóły połączenia możesz też sprawdzić w web Admin Panel.

    Szczegółowe instrukcje znajdziesz w artykule [Połącz z internetem przez sieć komórkową](../../interface_guide/internet_cellular.md).

    !!! note

        1. Wbudowana karta eSIM i SIM 2 wzajemnie się wykluczają i nie mogą być aktywne jednocześnie. eSIM jest domyślnie wyłączona. Jeśli włączysz eSIM, SIM 2 nie będzie działać nawet wtedy, gdy karta SIM jest włożona.
        2. Ponieważ Mudi 7 ma wbudowaną kartę eSIM, fizyczna karta eSIM SIMPoYo będzie rozpoznawana w Mudi 7 jako zwykła karta SIM bez funkcji eSIM.

=== "Ethernet"
    
    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Podłącz port Ethernet Mudi 7 do źródła sieci nadrzędnej (np. modemu operatora, przełącznika sieciowego albo gniazda Ethernet w ścianie) za pomocą kabla Ethernet.
    2. Na ekranie dotykowym albo w web Admin Panel przejdź do **Network** -> **Ethernet Ports**, ustaw rolę portu na **WAN** i kliknij **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Po pomyślnym połączeniu z internetem w prawym górnym rogu ekranu dotykowego pojawi się ikona portu Ethernet. Szczegóły połączenia możesz też sprawdzić w web Admin Panel.

    Szczegółowe instrukcje znajdziesz w artykule [Połącz z internetem przez kabel Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"
    
    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. Na ekranie dotykowym albo w web Admin Panel przejdź do **Internet** -> **Repeater** i kliknij **Connect**. Mudi 7 rozpocznie skanowanie dostępnych sieci Wi-Fi.
    2. Wybierz sieć Wi-Fi, której zasięg ma rozszerzać Mudi 7.
    3. Wpisz hasło i kliknij **Apply**.
    4. Po pomyślnym połączeniu z internetem w prawym górnym rogu ekranu dotykowego pojawi się ikona Wi-Fi. Szczegóły połączenia możesz też sprawdzić w web Admin Panel.

    Szczegółowe instrukcje znajdziesz w artykule [Połącz z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon albo modem USB) do portu USB-C Mudi 7 za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Ustawień i włącz **USB Tethering**. Jeśli korzystasz z iPhone'a, po wyświetleniu monitu stuknij **Trust This Device**.
    3. Mudi 7 połączy się wtedy automatycznie z Twoim urządzeniem. Jeśli połączenie nie zostanie nawiązane, powtórz powyższe kroki albo zaloguj się do web Admin Panel i sprawdź połączenie Tethering na stronie INTERNET.
    4. Po pomyślnym połączeniu z internetem w prawym górnym rogu ekranu dotykowego pojawi się ikona łańcucha. Szczegóły połączenia możesz też sprawdzić w web Admin Panel.

    Szczegółowe instrukcje znajdziesz w artykule [Połącz z internetem przez tethering USB](../../interface_guide/internet_tethering.md).

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 jest wyposażony w port USB-C z obsługą **OTG**, który pozwala dodać drugi port Ethernet dla Dual-Ethernet WAN. Wymaga to **sprzedawanego osobno adaptera USB-C-to-Ethernet**.

    <small>*USB OTG (On-The-Go) to standard USB, który umożliwia zgodnym urządzeniom, takim jak routery, przełączanie się między rolą hosta a urządzenia peryferyjnego, co pozwala na bezpośrednią transmisję danych i zasilania bez osobnego urządzenia hosta.</small>

    1. Podłącz źródło sieci nadrzędnej (np. modem operatora, przełącznik sieciowy albo gniazdo Ethernet w ścianie) do portu USB-C Mudi 7 za pomocą adaptera USB-C-to-Ethernet.
    2. Na ekranie dotykowym albo w web Admin Panel przejdź do **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, ustaw rolę portu na **WAN** i kliknij **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 połączy się wtedy automatycznie z urządzeniem. Jeśli połączenie nie zostanie nawiązane, powtórz powyższe kroki albo zaloguj się do web Admin Panel i sprawdź połączenie USB Ethernet na stronie INTERNET.
    4. Po pomyślnym połączeniu z internetem w prawym górnym rogu ekranu dotykowego pojawią się ikona USB oraz ikona portu Ethernet. Szczegóły połączenia możesz też sprawdzić w web Admin Panel.

## Naprawa i reset

Za pomocą fizycznego przycisku reset możesz przywrócić łączność sieciową albo zresetować Mudi 7 do ustawień fabrycznych.

**Uwaga**: Przed wykonaniem resetu upewnij się, że Mudi 7 zakończył pełne uruchamianie. NIE naciskaj przycisku reset od razu po włączeniu zasilania, ponieważ może to uruchomić tryb failsafe U-Boot.

Zdejmij tylną pokrywę, a zobaczysz przycisk reset pokazany poniżej.

![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

!!! note "Naprawa sieci"

    Naciśnij i przytrzymaj przycisk reset przez **4 sekundy**, a następnie zwolnij go, aby naprawić sieć. Podczas przytrzymywania przycisku zwracaj uwagę na komunikaty na ekranie i postępuj zgodnie z instrukcjami.

    Spowoduje to ponowne uruchomienie interfejsu sieciowego z zachowaniem ustawień Wi-Fi, konfiguracji VPN (wyłączonych), ustawień systemowych itp.

    **Uwaga**:

    1. Jeśli Wi-Fi zostało wyłączone, reset programowy przywróci domyślny stan włączonego Wi-Fi.

    2. Reset programowy można też wykorzystać do szybkiego przełączenia urządzenia z trybu innego niż router do trybu routera.

!!! note "Reset urządzenia"

    Naciśnij i przytrzymaj przycisk reset przez **10 sekund**, a następnie zwolnij go, aby wykonać pełny reset. Podczas przytrzymywania przycisku zwracaj uwagę na komunikaty na ekranie i postępuj zgodnie z instrukcjami.
    
    Spowoduje to usunięcie wszystkich ustawień. Zachowaj ostrożność.

## Zaloguj się do web Admin Panel

Możesz zalogować się do web Admin Panel Mudi 7, aby skonfigurować więcej ustawień lub sprawdzić szczegóły urządzenia.

Najpierw podłącz urządzenie (np. komputer, laptop albo smartfon) do Mudi 7 przez Wi-Fi, kabel Ethernet albo kabel USB.

- **Wi-Fi**

    - <u>Kod QR</u>: Zeskanuj kod QR wyświetlany na ekranie Mudi 7 za pomocą swojego urządzenia. Następnie kliknij na urządzeniu „Join”, aby się połączyć.
    - <u>Połączenie ręczne</u>: Na swoim urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi Mudi 7 na liście dostępnych sieci i wpisz hasło, aby dołączyć do sieci. (Domyślna nazwa sieci i hasło są wydrukowane na etykiecie).

- **Ethernet**

    Podłącz urządzenie do portu Ethernet Mudi 7 (domyślnie LAN) za pomocą kabla Ethernet.

- **USB**

    Podłącz urządzenie do portu USB-C Mudi 7 za pomocą kabla USB. Port USB-C z obsługą OTG umożliwia dostęp do panelu WebGUI Mudi 7 w następnym kroku.

Następnie otwórz przeglądarkę internetową i wpisz `192.168.8.1` w pasku adresu, aby przejść do strony logowania. Wybierz język, ustaw hasło administratora i kliknij **Apply**.

Następnie zostaniesz zalogowany do web Admin Panel Mudi 7.

Poniżej znajdziesz omówienie funkcji dostępnych w web Admin Panel Mudi 7.

## Wireless

Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 6 GHz, 5 GHz i 2,4 GHz, w tym włączanie Wi-Fi, ustawienie mocy TX, określenie nazwy sieci Wi-Fi (SSID), włączenie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

Aby skonfigurować Wireless, zapoznaj się z [Wireless](../../interface_guide/wireless.md).

**Uwaga**: Ustawienia sieci bezprzewodowej w Mudi 7 różnią się nieco od ustawień innych routerów GL.iNet Wi-Fi 7.

1. Ze względu na ograniczenia sprzętowe chipsetu Wi-Fi 5 GHz i 6 GHz nie mogą być włączone jednocześnie.
2. Gdy Repeater jest włączony, Guest Network zostanie automatycznie wyłączona.
3. Zgodnie z przepisami podczas korzystania z Wi-Fi na zewnątrz należy przełączyć je w tryb Outdoor. Może to zmniejszyć zasięg sygnału. Ustawienie Usage Environment (Indoor lub Outdoor) możesz zmienić u góry strony Wireless.

## Clients

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, łączny ruch oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

Aby skonfigurować Clients, zapoznaj się z [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa zarządzania chmurowego GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób na zdalny dostęp do routerów GL.iNet oraz zarządzanie nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o płynnej pracy zdalnej sieci i zdalnym zarządzaniu urządzeniami. Została stworzona specjalnie do integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Koncentrując się na zarządzaniu całą siecią oraz przyszłej obsłudze kontroli na poziomie sprzętowym, AstroWarp oferuje solidniejsze i bardziej niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych i stabilnych sieci.
    
    Aby skonfigurować AstroWarp, zapoznaj się z [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany tunel ruchu między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Mudi 7 obsługuje OpenVPN i WireGuard.

=== "OpenVPN"
    
    Mudi 7 (podobnie jak inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z tych instrukcji:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Mudi 7 (podobnie jak inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką szybkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z tych instrukcji:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia jednoczesne skonfigurowanie routera z wieloma połączeniami internetowymi (np. Ethernet, Repeater, Tethering, Cellular i USB Ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.
    
    Aby skonfigurować LAN, zapoznaj się z [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski podsieci oraz skonfigurowanie ustawień bezpieczeństwa, takich jak izolacja AP dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i zastąpienie ustawień DNS wszystkich klientów, zezwolenie na zastępowanie DNS VPN przez niestandardowy DNS oraz skonfigurowanie trybu ustawień serwera DNS jako automatycznego lub ręczne określenie serwerów DNS dla połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia ustawienie roli portu Ethernet (czyli używanie go jako WAN lub LAN), przełączanie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie wynegocjowanej prędkości portu.

    Mudi 7 ma jeden port Ethernet, który domyślnie działa jako LAN. W razie potrzeby możesz przełączyć go na port WAN na ekranie dotykowym albo w web Admin Panel.

    Aby zarządzać portami Ethernet, zapoznaj się z [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne przy stale rosnącej liczbie urządzeń podłączonych do internetu.
    
    Aby skonfigurować IPV6, zapoznaj się z [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.
    
    Aby skonfigurować IGMP snooping, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network Mode to konfiguracja określająca, w jaki sposób urządzenie łączy się z siecią i komunikuje z innymi urządzeniami.
    
    Aby skonfigurować Network Mode, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

    **Uwaga**: Mudi 7 obsługuje tryby Router, Access Point oraz Extender. Nie obsługuje trybu WDS.

=== "Drop-in gateway"

    Drop-in gateway rozszerza funkcjonalność głównego routera, w tym o AdGuard Home, szyfrowany DNS i klienta VPN.
    
    Aby skonfigurować drop-in gateway, zapoznaj się z tymi odnośnikami:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Jak skonfigurować drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network Acceleration może zmniejszyć obciążenie procesora i przyspieszyć przekazywanie pakietów ruchu.
    
    Aby skonfigurować Network Acceleration, zapoznaj się z [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je. Obejmuje ograniczanie czasu spędzanego przed ekranem oraz blokowanie dostępu do określonych treści.

    Aby skonfigurować Parental Control, zapoznaj się z [Parental Control](../../interface_guide/parental_control.md).

## Security

=== "Port Forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w internecie dostęp do urządzeń w sieci prywatnej.
    
    Aby skonfigurować port forwarding, zapoznaj się z [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Strona Management Control umożliwia konfigurację różnych ustawień bezpieczeństwa, aby chronić sieć i router przed nieautoryzowanym dostępem. Obejmuje następujące opcje:

    * Local Access Control: zarządzanie dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej oraz jego ograniczanie.
    * Remote Access Control: konfiguracja i ograniczanie dostępu do interfejsu routera z lokalizacji zdalnych przez internet, co zwiększa ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontrola tego, które porty są otwarte na routerze, aby ograniczyć potencjalne luki w zabezpieczeniach i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe i chronić zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w artykule [Security](../../interface_guide/security.md).

=== "NAT Mode"

    Strona NAT Mode umożliwia włączenie albo wyłączenie funkcji Full Cone NAT i SIP ALG.

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Mode](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie.
    
    Aby skonfigurować wtyczki, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest szczególnie przydatny dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej.
    
    Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć.
    
    Aby skonfigurować Network Storage, zapoznaj się z [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i trackerów, które pełni rolę serwera DNS filtrującego niepożądane treści na wszystkich urządzeniach podłączonych do sieci domowej.
    
    Aby skonfigurować AdGuard Home, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowane programowo, które umożliwia użytkownikom tworzenie bezpiecznych, wirtualnych sieci przez internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej.
    
    Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.
    
    Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, czyli The Onion Router, to sieć skoncentrowana na prywatności, która umożliwia anonimową komunikację przez internet. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację użytkownika i sposób korzystania z sieci, co utrudnia śledzenie aktywności online.
    
    Aby skonfigurować Tor, zapoznaj się z [Tor](../../interface_guide/tor.md).

## System

=== "Overview"

    Strona Overview zapewnia kompleksowy przegląd bieżącego stanu routera i wskaźników jego wydajności. Na tej stronie możesz zobaczyć:

    * CPU Average Load: monitorowanie średniego obciążenia procesora routera, co pomaga ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: sprawdzenie, ile pamięci routera jest aktualnie używane, co ułatwia zarządzanie zasobami.
    * LED Control: włączanie i wyłączanie diod LED routera, co pozwala dostosować wizualne wskaźniki urządzenia.
    * Flash Usage: podgląd wykorzystania pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: dostęp do szczegółowych informacji o systemie routera, w tym czasu pracy, nazwy hosta, modelu, architektury, wersji OpenWrt, wersji jądra, identyfikatora urządzenia, adresu MAC urządzenia i numeru seryjnego urządzenia.
    * External Storage: sprawdzenie stanu wszystkich zewnętrznych nośników pamięci podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają niezbędny wgląd i kontrolę, pomagając skutecznie zarządzać działaniem routera i je monitorować.

    Szczegółowe instrukcje znajdziesz w artykule [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Strona Admin Password umożliwia ustawienie albo zmianę hasła do interfejsu administracyjnego routera.

    Hasło administratora musi spełniać następujące wymagania:

    * Minimum 10 znaków i maksimum 63 znaki.
    * Dozwolone są litery (z rozróżnianiem wielkości liter), cyfry i symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Wymagane są co najmniej dwa z następujących elementów: wielkie litery, małe litery, cyfry i symbole.

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, wyższy poziom bezpieczeństwa i nowe funkcje. Ta strona oferuje dwie metody aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzenie i zainstalowanie najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, co daje większą kontrolę nad wersją i terminem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router w aktualnym stanie i korzystać z najnowszych poprawek oraz ulepszeń.

    Szczegółowe instrukcje znajdziesz w artykule [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia skonfigurowanie routera tak, aby automatycznie uruchamiał się ponownie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.

    Szczegółowe instrukcje znajdziesz w artykule [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

    **Uwaga**: Mudi 7 nie obsługuje harmonogramu wyświetlania LED ani harmonogramu stanu Wi-Fi.

=== "Display Management"

    Strona Display Management umożliwia zarządzanie ekranem dotykowym i powiązanymi z nim ustawieniami.
    
    - Wallpaper: dostosowanie tapety i stylu wybudzania ekranu.
    - Brightness: regulacja jasności ekranu dotykowego. Użyj suwaka albo wpisz wartość procentową, aby dopasować jasność do różnych warunków oświetleniowych.
    - Personalised Signature: dodanie własnego tekstu na ekranie dotykowym, aby nadać urządzeniu indywidualny charakter albo ułatwić jego identyfikację.
    - Auto Lock: ustawienie opóźnienia automatycznej blokady ekranu w przypadku braku aktywności. Zakres wynosi od 15 sekund do 5 minut.
    - Passcode: ustawienie kodu dostępu do ekranu dotykowego dla dodatkowej warstwy zabezpieczeń.

    Szczegółowe instrukcje znajdziesz w artykule [Display Management](../../interface_guide/display_management.md).

=== "USB & Power"

    Strona USB & Power umożliwia konfigurację ustawień związanych z USB i zarządzaniem zasilaniem routera, takich jak protokół USB, kierunek zasilania, limity czasu bezczynności i zachowanie w trybie gotowości.

    Szczegółowe instrukcje znajdziesz w artykule [USB & Power](../../interface_guide/usb_power.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej dla routera, tak aby wszystkie zaplanowane zadania, logi i zdarzenia systemowe miały prawidłowe znaczniki czasu zgodne z czasem lokalnym. Ustawienie to ma kluczowe znaczenie dla zachowania dokładnych zapisów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w artykule [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, co usuwa wszystkie własne konfiguracje. Proces ten przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów albo wtedy, gdy chcesz zacząć od nowa z domyślną konfiguracją bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w artykule [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Obejmuje ona:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem jądra systemu i jego zdarzeniami.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, opisujące ruch WWW i operacje serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez dział wsparcia technicznego. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w artykule [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, dzięki czemu bardziej zaawansowani użytkownicy mogą szczegółowo dostosować ustawienia i funkcje routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieciowe, ustawienia zapory i inne zaawansowane ustawienia systemowe.

    Szczegółowe instrukcje znajdziesz w artykule [Advanced Settings](../../interface_guide/advanced_settings.md).
