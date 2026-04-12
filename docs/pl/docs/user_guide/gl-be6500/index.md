# Podręcznik użytkownika Flint 3e (GL-BE6500)

## Przegląd produktu

Flint 3e (GL-BE6500) to dwupasmowy router biurkowy Wi‑Fi 7 przeznaczony dla użytkowników domowych i małych biur. Obsługuje technologię Wi‑Fi 7 Multi-Link Operation (MLO), która inteligentnie łączy kanały 2,4 GHz i 5 GHz w jedno połączenie. Jednoczesne wykorzystanie zasobów obu pasm ogranicza zakłócenia i przeciążenia, a 4K QAM zapewnia łączną prędkość dwupasmową 6453 Mb/s — o 20% wyższą niż w Wi‑Fi 6. Ulepszone pasmo 5 GHz (4x4 MIMO, 160 MHz) znacząco poprawia także wydajność na większe odległości.

Wyposażony w 5 portów Ethernet 2,5G i 1 port USB 3.0, router obsługuje szybkie połączenia przewodowe i rozbudowę pamięci. Dodatkowo jest kompatybilny z ponad 30 usługami VPN i zapewnia wydajność VPN do 680 Mb/s w WireGuard® oraz OpenVPN-DCO, a także zawiera bezpłatną kontrolę rodzicielską Bark, oferując dobry balans między wydajnością, praktycznością i bezpieczeństwem.

![gl-be6500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/hardware_info/be6500_interface.jpg){class="glboxshadow"}

**Uwaga**: Różnica w wyglądzie między Flint 3e a Flint 3 polega na nadruku na obudowie: nadruk na Flint 3e jest niebieski, natomiast na Flint 3 jest biały.

## Zawartość opakowania

- 1 x Flint 3e (GL-BE6500)
- 1 x zasilacz
- 1 x kabel Ethernet
- 1 x podręcznik użytkownika
- 1 x karta z podziękowaniem
- 1 x przejściówka (w zależności od kraju dostawy)

Zobacz poniżej film z rozpakowania Flint 3e.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-E0LtWqshk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Jak skonfigurować Flint 3e

Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R40QsUFYuUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka. Router uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera za pomocą Wi‑Fi lub kabla Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do **Settings** -> **WLAN**, odszukaj nazwę sieci Wi‑Fi routera na liście dostępnych sieci i wpisz hasło, aby połączyć się z siecią. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

### 4. Konfiguracja internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router przez GL.iNet Web Admin Panel. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Flint 3e, korzystając z jednej z obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_ethernet.jpg){class="glboxshadow"}

    Podłącz port WAN routera Flint 3e do urządzenia nadrzędnego (np. modemu) za pomocą kabla Ethernet.
    
    Po pomyślnym połączeniu z internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez kabel Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_repeater.jpg){class="glboxshadow"}

    1. Na stronie INTERNET w web Admin Panel znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi‑Fi z listy dostępnych sieci.
    3. Wpisz hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez istniejącą sieć Wi‑Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_tethering.jpg){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do **Settings** i włącz USB Tethering.
    3. Na stronie INTERNET w web Admin Panel kliknij **Connect** w sekcji Tethering.
    
    Po pomyślnym połączeniu z internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_cellular.jpg){class="glboxshadow"}

    Podłącz modem USB z obsługą sieci komórkowej do portu USB routera Flint 3e. Ta metoda jest przydatna, gdy chcesz udostępnić internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez połączenie komórkowe](../../interface_guide/internet_cellular.md).

---

Poniżej znajduje się przegląd funkcji dostępnych w panelu administracyjnym Flint 3e.

## Sieć bezprzewodowa

Strona Wireless umożliwia konfigurację ustawień sieci Wi‑Fi 5 GHz i 2,4 GHz, w tym włączanie Wi‑Fi, ustawianie mocy TX, określanie nazwy sieci Wi‑Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi‑Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi‑Fi, szerokości pasma i kanału.
    
Dodatkowo Flint 3e obsługuje MLO Wi‑Fi, czyli Multi-Link Operation, które łączy jednocześnie wiele sieci bezprzewodowych w celu uzyskania wyższej przepustowości i bardziej niezawodnych połączeń.

Aby skonfigurować Wireless, zapoznaj się z [Wireless](../../interface_guide/wireless.md).

## Klienci

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia blokowanie klienta lub wykonywanie innych działań.

Aby skonfigurować Clients, zapoznaj się z [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o płynnej łączności zdalnej i zdalnym zarządzaniu urządzeniami. Została opracowana specjalnie do integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę urządzeń nadrzędnych i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią oraz przyszłemu wsparciu kontroli na poziomie sprzętowym AstroWarp oferuje bardziej solidne i niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci.
    
    Aby skonfigurować AstroWarp, zapoznaj się z [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN), a także umożliwia dostęp do sieci zdalnej (serwer VPN). Flint 3e obsługuje OpenVPN, WireGuard i Tor.

=== "OpenVPN"
    
    Flint 3e (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia silne zabezpieczenia. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Flint 3e (i inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia dużą szybkość i wygodę. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, skrót od The Onion Router, to sieć zorientowana na prywatność, umożliwiająca anonimową komunikację w internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci, co utrudnia śledzenie aktywności online.
    
    * [Jak skonfigurować Tor](../../interface_guide/tor.md)

## Aplikacje

=== "Plug-ins"

    Plug-in to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie.
    
    Aby skonfigurować Plug-ins, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest to szczególnie przydatne dla użytkowników, którzy potrzebują statycznego adresu IP, aby uzyskać dostęp do sieci zdalnej.
    
    Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Pamięć sieciowa to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich udostępnianie przez sieć.
    
    Aby skonfigurować Network Storage, zapoznaj się z [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i trackerów, które działa jako serwer DNS filtrujący niepożądane treści na wszystkich urządzeniach podłączonych do sieci domowej.
    
    Aby skonfigurować AdGuard Home, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować sposób ich używania. Obejmuje to ograniczanie czasu spędzanego przed ekranem oraz blokowanie dostępu do określonych treści.

    Aby skonfigurować Parental Control, zapoznaj się z [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieciowe definiowane programowo, które umożliwia tworzenie bezpiecznych, wirtualnych sieci przez internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej.
    
    Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.
    
    Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

## Ustawienia sieciowe

=== "Port forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w internecie dostęp do urządzeń w sieci prywatnej.
    
    Aby skonfigurować port forwarding, zapoznaj się z [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa pozwalająca skonfigurować router z wieloma połączeniami internetowymi jednocześnie (np. cellular, repeater i ethernet). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie. Zapewnia to płynny i nieprzerwany dostęp do internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN (Local Area Network) to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.
    
    Aby skonfigurować LAN, zapoznaj się z [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz konfigurację ustawień bezpieczeństwa, takich jak AP isolation, dla sieci gościnnej.

    Aby skonfigurować Guest Network, zapoznaj się z [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i zastąpienie ustawień DNS wszystkich klientów, zezwolenie na to, by własny DNS zastępował DNS z VPN, a także ustawienie trybu konfiguracji serwera DNS na automatyczny lub ręczne wskazanie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Strona Ethernet Port umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN na Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie negocjowanej prędkości portu sieciowego.

    Aby zarządzać portami Ethernet, zapoznaj się z [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Tryb sieciowy określa ustawienia konfiguracji, które decydują o tym, w jaki sposób urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami.
    
    Aby skonfigurować Network Mode, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6 (Internet Protocol version 6) to najnowsza wersja protokołu internetowego, zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne przy stale rosnącej liczbie urządzeń podłączonych do internetu.
    
    Aby skonfigurować IPv6, zapoznaj się z [IPv6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność routera głównego, oferując m.in. AdGuard Home, szyfrowany DNS i klienta VPN.
    
    Aby skonfigurować Drop-in Gateway, zapoznaj się z poniższymi materiałami:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP Snooping to technika optymalizacji sieci używana w przełącznikach Ethernet do zarządzania i kontrolowania ruchu multicast.
    
    Aby skonfigurować IGMP Snooping, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Akceleracja sieci pozwala zmniejszyć obciążenie procesora i przyspieszyć przekazywanie pakietów.
    
    Aby skonfigurować Network Acceleration, zapoznaj się z [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączanie lub wyłączanie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Aby skonfigurować NAT Settings, zapoznaj się z [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemowe

=== "Overview"

    Strona Overview zapewnia kompleksowy podgląd bieżącego stanu routera i jego parametrów wydajności. Możesz na niej sprawdzić:

    * CPU Average Load: średnie obciążenie procesora routera, co pomaga ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: ilość używanej pamięci routera, co pomaga w zarządzaniu zasobami.
    * LED Control: włączanie i wyłączanie diod LED routera, co pozwala dostosować wizualne wskaźniki urządzenia.
    * Flash Usage: wykorzystanie pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: szczegółowe informacje o systemie routera, w tym czas pracy, hostname, model, architekturę, wersję OpenWrt, wersję jądra, identyfikator urządzenia, adres MAC urządzenia i numer seryjny.
    * External Storage: stan wszelkich zewnętrznych urządzeń pamięci podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają istotne informacje i narzędzia, które pomagają skutecznie zarządzać pracą routera i ją monitorować.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, aby zapewnić lepszą wydajność, bezpieczeństwo i nowe funkcje. Dostępne są dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie i instalacja najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: ręczne wgranie pliku firmware z komputera, co daje większą kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router w aktualnym stanie, korzystając z najnowszych usprawnień i poprawek.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera według zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Dostępne funkcje obejmują:

    * LED Display Schedule: ustawienie harmonogramu automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w wybranych godzinach.
    * Schedule Reboot: skonfigurowanie automatycznego restartu routera w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Wi-Fi Status Schedule: ustawienie harmonogramu sterowania pasmami Wi‑Fi 5 GHz / 2,4 GHz / MLO, co pozwala lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Opcje te dają większą kontrolę nad działaniem routera, dzięki czemu można lepiej dopasować go do własnych potrzeb i preferencji.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie właściwej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe mają poprawne znaczniki czasu zgodne z Twoim czasem lokalnym. Jest to istotne dla zachowania dokładnych rejestrów i prawidłowego działania konfiguracji zależnych od czasu.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w diagnostyce i monitorowaniu wydajności. Obejmuje ona:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem i zdarzeniami jądra.
    * Crash Log: zapisy awarii i błędów systemu, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu WWW i działaniu serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który pozwala wyeksportować wszystkie zebrane logi do analizy przez wsparcie techniczne. Funkcja ta jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Log](../../interface_guide/log.md).

---

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień zabezpieczeń w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Obejmuje opcje takie jak:

    * Admin Password: ustawienie lub zmiana hasła do interfejsu administracyjnego routera, aby tylko upoważnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzanie dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i jego ograniczanie.
    * Remote Access Control: konfiguracja i ograniczanie dostępu do interfejsu routera z lokalizacji zdalnych przez internet, co zwiększa ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontrolowanie, które porty routera są otwarte, aby ograniczyć potencjalne podatności i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca ustawienia domyślne aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa z domyślnymi ustawieniami bieżącej wersji firmware.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostrojenie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółową konfigurację sieci, ustawienia zapory i inne zaawansowane dostosowania systemowe.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Advanced Settings](../../interface_guide/advanced_settings.md).

