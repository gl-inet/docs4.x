# Podręcznik użytkownika Slate AX (GL-AXT1800)

## Przegląd produktu

Slate AX (GL-AXT1800) to pierwszy przenośny router Wi-Fi 6 zaprojektowany przez GL.iNet. Jest wyposażony w czterordzeniowy procesor IPQ6000 1.2GHz i działa na OpenWrt 23.05. Dzięki najnowszej technologii Wi-Fi 6 możesz korzystać z większej przepustowości dla podłączonych urządzeń oraz szybszej łączności bezprzewodowej zarówno w podróży, jak i w domu.

![gl-axt1800 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/hardware_info/gl-axt1800_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Slate AX (GL-AXT1800)
- 1 x Podręcznik użytkownika
- 1 x kabel Ethernet
- 1 x karta z podziękowaniem
- 1 x karta gwarancyjna
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![gl-axt1800 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/first_time_setup/axt1800_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Slate AX

Obejrzyj ten film instruktażowy lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f7DYULL6ZSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka. Router uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera za pomocą Wi-Fi lub kabla Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. Domyślną nazwę sieci oraz hasło znajdziesz na etykiecie na spodzie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Podczas potwierdzania ustawień Wi-Fi pamiętaj, że jeśli zmienisz dane Wi-Fi, musisz ponownie połączyć urządzenie z siecią Wi-Fi routera, używając zaktualizowanych danych logowania.

### 4. Konfiguracja internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą panelu administracyjnego GL.iNet. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Slate AX, korzystając z jednej z obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem.

    Po pomyślnym połączeniu z internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wprowadź hasło, a następnie kliknij **Apply**.

    Po pomyślnym połączeniu z internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering.
    3. Na stronie INTERNET w panelu administracyjnym kliknij **Connect** w sekcji Tethering.

    Po pomyślnym połączeniu z internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez tethering USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_cellular.png){class="glboxshadow"}

    Podłącz modem komórkowy USB do portu USB routera. To przydatne rozwiązanie, jeśli chcesz udostępniać internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Połącz z internetem przez sieć komórkową](../../interface_guide/internet_cellular.md).

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN), a także umożliwia dostęp do sieci zdalnej (serwer VPN). Slate AX obsługuje OpenVPN, WireGuard i Tor.

=== "OpenVPN"

    Slate AX obsługuje protokół OpenVPN, który zapewnia silne zabezpieczenia. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate AX obsługuje protokół WireGuard, który zapewnia dużą szybkość i wygodę. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, skrót od The Onion Router, to sieć zorientowana na prywatność, umożliwiająca anonimową komunikację w internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i aktywność użytkownika, co utrudnia śledzenie działań online.

    * [Jak skonfigurować Tor](../../interface_guide/tor.md).

---

## Sieć bezprzewodowa i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5 GHz i 2.4 GHz, w tym włączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, szybkość pobierania i wysyłania, całkowity ruch oraz umożliwia zablokowanie klienta lub wykonanie innych działań.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.

    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej zdalnej komunikacji sieciowej i zdalnym zarządzaniu urządzeniami. Została stworzona specjalnie do integracji z routerami GL.iNet i obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Dzięki naciskowi na zarządzanie całą siecią i przyszłemu wsparciu dla sterowania na poziomie sprzętowym AstroWarp oferuje solidniejsze i bardziej niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci.

    Aby skonfigurować AstroWarp, zapoznaj się z [AstroWarp](../../interface_guide/astrowarp.md).

## Aplikacje

=== "Plug-ins"

    Plug-in to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając jego dostosowanie i rozszerzenie.

    Aby skonfigurować Plug-ins, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest to szczególnie przydatne dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej.

    Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Magazyn sieciowy to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich udostępnianie przez sieć.

    Aby skonfigurować pamięć sieciową, zapoznaj się z [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to działające w całej sieci rozwiązanie do blokowania reklam i trackerów, które działa jako serwer DNS, filtrując niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej.

    Aby skonfigurować AdGuard Home, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je. Obejmuje to ograniczanie czasu spędzanego przed ekranem oraz ograniczanie dostępu do określonych treści.

    Aby skonfigurować kontrolę rodzicielską, zapoznaj się z [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowanej programowo, które umożliwia użytkownikom tworzenie bezpiecznych, wirtualnych sieci przez internet i łączenie urządzeń tak, jakby znajdowały się w tej samej sieci lokalnej.

    Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.

    Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

## Ustawienia sieciowe

=== "Port Forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w internecie dostęp do urządzeń w sieci prywatnej.

    Aby skonfigurować przekierowanie portów, zapoznaj się z [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa pozwalająca skonfigurować router z wieloma połączeniami internetowymi, takimi jak Cellular, Repeater i Ethernet. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie. Dzięki temu dostęp do internetu pozostaje płynny i nieprzerwany.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN (Local Area Network) to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.

    Aby skonfigurować LAN, zapoznaj się z [LAN](../../interface_guide/lan.md).

---

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresu IP bramy i maski sieci oraz skonfigurowanie ustawień zabezpieczeń, takich jak izolacja AP dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding i zastąpienie ustawień DNS wszystkich klientów, zezwolenie niestandardowemu DNS na zastępowanie DNS VPN oraz skonfigurowanie trybu ustawień serwera DNS jako automatycznego lub ręczne określenie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Port Management"

    Strona Port Management umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN jako Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie wynegocjowanej szybkości portu sieciowego.

    Aby skonfigurować zarządzanie portami Ethernet, zapoznaj się z [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Tryb sieciowy określa ustawienia konfiguracji decydujące o sposobie, w jaki urządzenie łączy się z siecią i komunikuje się z innymi urządzeniami.

    Aby skonfigurować tryb sieciowy, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6 (Internet Protocol version 6) to najnowsza wersja protokołu internetowego, zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając użycie praktycznie nieograniczonej liczby unikalnych adresów IP, co jest niezbędne przy stale rosnącej liczbie urządzeń podłączonych do internetu.

    Aby skonfigurować IPv6, zapoznaj się z [IPv6](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in Gateway rozszerza funkcjonalność routera głównego o funkcje, których może on nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN.

    Aby skonfigurować Drop-in Gateway, zapoznaj się z następującymi materiałami:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Jak skonfigurować Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP Snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i kontrolowania go.

    Aby skonfigurować IGMP Snooping, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączenie lub wyłączenie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemowe

=== "Overview"

    Strona Przegląd zapewnia kompleksowy obraz bieżącego stanu routera i wskaźników wydajności. Na tej stronie możesz zobaczyć:

    * CPU Average Load: monitoruj średnie obciążenie CPU routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: sprawdź, jaka część pamięci routera jest używana, co pomaga w zarządzaniu zasobami.
    * LED Control: włączaj lub wyłączaj diody LED routera, dostosowując wskaźniki świetlne urządzenia.
    * Flash Usage: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Device Info: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, hostname, model, architekturę, wersję OpenWrt, wersję kernela, ID urządzenia, MAC urządzenia i S/N urządzenia.
    * External Storage: sprawdź stan zewnętrznych urządzeń pamięci masowej podłączonych do routera, takich jak dyski USB lub karty TF.

    Funkcje te zapewniają kluczowe informacje i mechanizmy sterowania, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Aktualizacja służy do aktualizacji firmware routera do najnowszej wersji, zapewniając lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatyczne sprawdzanie i instalowanie najnowszej wersji firmware bezpośrednio z serwera producenta, co upraszcza proces aktualizacji.
    * Firmware Local Upgrade: ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, co daje kontrolę nad wersją aktualizacji i momentem jej wykonania.

    Opcje te pozwalają utrzymywać router w aktualnym stanie i korzystać z najnowszych ulepszeń oraz poprawek.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * LED Display Schedule: ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć zanieczyszczenie światłem w określonych godzinach.
    * Schedule Reboot: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Wi-Fi Status Schedule: ustaw harmonogram sterowania pasmami Wi-Fi 5GHz / 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.

    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu można dopasować je do własnych potrzeb i preferencji.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie właściwej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, logi i zdarzenia systemowe będą poprawnie oznaczane zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych rejestrów oraz prawidłowego działania konfiguracji opartych na czasie.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przycisku przełączania na routerze, pozwalając przypisać mu określone funkcje w celu szybkiego dostępu i sterowania. Funkcja ta zapewnia wygodne skróty do typowych zadań i ustawień, poprawiając komfort użytkowania oraz upraszczając zarządzanie routerem.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących działania i zdarzenia routera, co ułatwia rozwiązywanie problemów i monitorowanie wydajności. Ta strona obejmuje:

    * System Log: szczegółowe logi zdarzeń i działań na poziomie systemu.
    * Kernel Log: logi związane z działaniem kernela i jego zdarzeniami.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: logi interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: logi serwera WWW Nginx, jeśli jest używany przez router, zawierające szczegóły ruchu internetowego i działania serwera.

    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych logów do analizy przez pomoc techniczną. Ta funkcja jest bardzo przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Log](../../interface_guide/log.md).

---

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień zabezpieczeń, aby chronić sieć i router przed nieautoryzowanym dostępem. Ta strona zawiera opcje takie jak:

    * Admin Password: ustaw lub zmień hasło do interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj dostępem do interfejsu routera z urządzeń podłączonych do sieci lokalnej i ograniczaj go.
    * Remote Access Control: skonfiguruj i ogranicz dostęp do interfejsu routera z lokalizacji zdalnych przez internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne podatności i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia zresetowanie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub przy rozpoczynaniu pracy od nowa z domyślną konfiguracją bieżącej wersji firmware.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji za pośrednictwem interfejsu OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory oraz inne zaawansowane dostosowania systemowe.

    Aby uzyskać szczegółowe instrukcje, zapoznaj się z [Advanced Settings](../../interface_guide/advanced_settings.md).

