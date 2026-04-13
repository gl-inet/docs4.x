# Przewodnik użytkownika Brume 2 (GL-MT2500/GL-MT2500A)

## Przegląd produktu

Brume 2 (GL-MT2500/GL-MT2500A) to lekka i wydajna brama VPN działająca na systemie OpenWrt v21.02. Ma kompaktową konstrukcję, dzięki czemu doskonale nadaje się do hostowania serwera VPN w domu lub uruchamiania SD-WAN (Site-to-Site) w małych i średnich przedsiębiorstwach.

![gl-mt2500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Brume 2 (GL-MT2500/GL-MT2500A)
- 1 x instrukcja obsługi
- 1 x kabel Ethernet
- 1 x karta z podziękowaniem
- 1 x karta gwarancyjna
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

Na poniższej ilustracji pokazano model GL-MT2500A jako przykład.

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Brume 2

Aby skonfigurować Brume 2, użyj jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Tethering lub Cellular. Funkcja Repeater nie jest obsługiwana, ponieważ Brume 2 nie ma modułu Wi-Fi. Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/rpi_loOwUQM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania

Połącz dwuczęściowy zasilacz. Podłącz go do routera i do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer lub laptop) do portu LAN routera za pomocą kabla Ethernet. 

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**. 

### 4. Konfiguracja Internetu

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}
    
    Podłącz kabel Ethernet między portem WAN routera a urządzeniem upstream, takim jak modem. 
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Ethernet na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Ustawień i włącz USB Tethering.
    3. Na stronie INTERNET webowego panelu administracyjnego routera kliknij **Connect** w sekcji Tethering. 
    
    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Tethering na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

    Podłącz modem USB do sieci komórkowej do portu USB routera. Jest to przydatne, gdy chcesz współdzielić Internet z modemu USB ze wszystkimi podłączonymi urządzeniami.

    Po pomyślnym połączeniu z Internetem zielona kropka pojawi się w sekcji Cellular na stronie INTERNET.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

**Uwaga:** Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedną metodę połączenia z Internetem. 

## Jak skonfigurować VPN 

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Brume 2 (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard. Dodatkowo obsługuje Tor.

=== "OpenVPN" 

    Brume 2 (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 2 (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, skrót od The Onion Router, to sieć ukierunkowana na prywatność, umożliwiająca anonimową komunikację przez Internet. Przekierowuje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania użytkownika, co utrudnia śledzenie aktywności online. 
    
    * [How to set up Tor](../../interface_guide/tor.md).

## CLIENTS

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę urządzenia, adresy IP i MAC, prędkość pobierania i wysyłania, całkowity ruch oraz umożliwia rezerwację adresu IP, blokowanie klienta i wykonywanie innych działań.

Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi w chmurze

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi. 
    
    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o płynnej pracy zdalnej sieci i zdalnym zarządzaniu urządzeniami. Stworzona specjalnie do integracji z routerami GL.iNet, AstroWarp obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę urządzeń nadrzędnych i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią oraz przyszłemu wsparciu dla sterowania na poziomie sprzętowym AstroWarp oferuje bardziej niezawodne i solidne rozwiązanie do zarządzania urządzeniami oraz utrzymania bezpiecznych i stabilnych sieci. 
    
    Zapoznaj się z poradnikiem [AstroWarp](../../interface_guide/astrowarp.md).

## APPLICATIONS

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego możliwości. 
    
    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest to przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej. 
    
    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage oznacza scentralizowane rozwiązanie do przechowywania danych, które pozwala wielu użytkownikom i urządzeniom uzyskiwać dostęp do plików oraz udostępniać je przez sieć. 
    
    Zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie do blokowania reklam i elementów śledzących w całej sieci, działające jako serwer DNS filtrujący niepożądane treści na wszystkich urządzeniach podłączonych do sieci domowej. 
    
    Zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control to zestaw ustawień zaprojektowanych, aby pomóc Ci zarządzać urządzeniami dzieci i kontrolować je. Obejmuje ograniczanie czasu spędzanego przed ekranem oraz blokowanie dostępu do określonych treści. Brume 2 oferuje dwie opcje kontroli rodzicielskiej: lokalną wersję opracowaną przez GL.iNet oraz zintegrowaną wersję aplikacji Bark do kontroli rodzicielskiej.

    Zapoznaj się z poradnikiem [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie typu software-defined networking, które umożliwia tworzenie bezpiecznych, wirtualnych sieci przez Internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej. 
    
    Zapoznaj się z poradnikiem [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca. 
    
    Zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md).

## Ustawienia sieciowe

=== "Port forwarding"

    Port forwarding umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej. Aby skonfigurować tę funkcję, zapoznaj się z poradnikiem [Port Forwards](../../interface_guide/port_forwarding.md). 

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi jednocześnie (np. Cellular, Repeater i Ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu. 

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN (Local Area Network) to sieć łącząca komputery i urządzenia na ograniczonym obszarze, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą. 
    
    Zapoznaj się z poradnikiem [Lan Tutorial](../../interface_guide/lan.md). 

---

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz konfigurację ustawień zabezpieczeń, takich jak AP isolation, dla sieci gościnnej.

    Aby skonfigurować sieć LAN, zapoznaj się z poradnikiem [Lan Tutorial](../../interface_guide/guest_network.md). 

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i zastąpienie ustawień DNS wszystkich klientów, zezwolenie, aby niestandardowy DNS zastępował DNS VPN, oraz ustawienie trybu konfiguracji serwera DNS na automatyczny albo ręczne określenie serwerów DNS z połączenia Ethernet.

    Zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "Network Port Management"

    Strona Network Port Management umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN na Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

---

=== "Network Mode"

    Network mode odnosi się do ustawień konfiguracji określających sposób, w jaki urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami. 
    
    Zapoznaj się z poradnikiem [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana jako następca IPv4. Oferuje znacznie większą przestrzeń adresową, co pozwala obsłużyć praktycznie nieograniczoną liczbę unikalnych adresów IP, niezbędną przy stale rosnącej liczbie urządzeń podłączonych do Internetu. 
    
    Zapoznaj się z poradnikiem [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może nie posiadać, w tym AdGuard Home, szyfrowany DNS i VPN. 
    
    Szczegółowe instrukcje znajdziesz w [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania i kontrolowania ruchu multicast. 
    
    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Hardware acceleration oznacza wykorzystanie wyspecjalizowanych komponentów sprzętowych do wykonywania określonych zadań bardziej efektywnie niż w przypadku procesorów ogólnego przeznaczenia. 
    
    Zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączanie lub wyłączanie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Zapoznaj się z poradnikiem [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemowe

=== "Overview"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i wskaźników wydajności. Na tej stronie możesz sprawdzić:

    * CPU Average Load: Monitorowanie średniego obciążenia CPU routera, co pomaga ocenić wydajność i wykryć potencjalne wąskie gardła.
    * Memory Usage: Sprawdzenie, jaka część pamięci routera jest wykorzystywana, co ułatwia zarządzanie zasobami.
    * LED Control: Włączanie i wyłączanie diod LED routera, co pozwala dostosować wizualne wskaźniki urządzenia.
    * Flash Usage: Wyświetlanie wykorzystania pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: Dostęp do szczegółowych informacji o systemie routera, w tym czasu działania, nazwy hosta, modelu, architektury, wersji OpenWrt, wersji jądra, identyfikatora urządzenia, adresu MAC urządzenia i numeru seryjnego.
    * External Storage: Sprawdzenie stanu urządzeń pamięci zewnętrznej podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają najważniejsze informacje i elementy sterowania, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Szczegółowe instrukcje znajdziesz w [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: Automatyczne sprawdzanie i instalowanie najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: Ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, co daje większą kontrolę nad wersją i czasem aktualizacji.

    Dzięki tym opcjom możesz utrzymywać router na bieżąco z najnowszymi ulepszeniami i poprawkami.

    Szczegółowe instrukcje znajdziesz w [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację funkcji routera według z góry określonego harmonogramu, zwiększając wygodę i efektywność. Główne funkcje tej strony obejmują:

    * LED Display Schedule: Ustawienie harmonogramu automatycznego włączania lub wyłączania diod LED routera, co ogranicza emisję światła w określonych porach.
    * Schedule Reboot: Skonfigurowanie automatycznego restartu routera w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.

    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera i pozwalają dopasować je do konkretnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe są oznaczane zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla zachowania dokładnych zapisów i prawidłowego działania konfiguracji zależnych od czasu.

    Szczegółowe instrukcje znajdziesz w [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, pomagając w rozwiązywaniu problemów i monitorowaniu wydajności. Ta strona obejmuje:

    * System Log: Szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: Dzienniki związane z działaniem jądra systemu i jego zdarzeniami.
    * Crash Log: Rejestry awarii i błędów systemu, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: Dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: Dzienniki serwera WWW Nginx, jeśli jest używany przez router, opisujące ruch internetowy i działanie serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia eksport wszystkich zebranych logów do analizy przez wsparcie techniczne. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w [Log](../../interface_guide/log.md).

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień bezpieczeństwa w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Ta strona obejmuje opcje:

    * Admin Password: Ustawienie lub zmiana hasła interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: Zarządzanie dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej oraz jego ograniczanie.
    * Remote Access Control: Konfigurowanie i ograniczanie dostępu do interfejsu routera ze zdalnych lokalizacji przez Internet, co zwiększa ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: Kontrola tego, które porty są otwarte na routerze, co ogranicza potencjalne podatności i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    Strona Reset Firmware umożliwia zresetowanie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca ustawienia domyślne aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz zacząć od nowa z domyślną konfiguracją bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostrojenie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółową konfigurację sieci, ustawienia zapory sieciowej i inne zaawansowane dostosowania systemu.

    Szczegółowe instrukcje znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md).
