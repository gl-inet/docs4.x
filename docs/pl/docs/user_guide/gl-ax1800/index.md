# Przewodnik użytkownika Flint (GL-AX1800)

## Omówienie produktu

Flint (GL-AX1800) to dwuzakresowy router Wi-Fi 6 z prędkością połączenia do 600 Mbps (2,4 GHz) + 1200 Mbps (5 GHz). Prędkość szyfrowania VPN sięga 667 Mbps, a urządzenie może działać jako serwer VPN. Flint idealnie sprawdza się przy intensywnym przesyłaniu danych, jednoczesnym podłączeniu wielu urządzeń oraz grach wymagających ultraniskich opóźnień.

![gl-ax1800 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ax1800/hardware_info/gl-ax1800_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Flint (GL-AX1800)
- 1 x instrukcja obsługi
- 1 x kabel Ethernet
- 1 x karta z podziękowaniem
- 1 x karta gwarancyjna
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![gl-ax1800 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ax1800/first_time_setup/ax1800_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Flint

Obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(W tym filmie do prezentacji konfiguracji użyto innego routera GL.iNet, ale kroki są takie same dla Flint i pozostałych modeli.)</small>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Połącz urządzenie (np. komputer, laptop lub smartfon) z routerem przez Wi-Fi albo Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie na spodzie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Podczas potwierdzania ustawień Wi‑Fi pamiętaj, że jeśli zmienisz dane sieci Wi‑Fi, konieczne będzie ponowne połączenie urządzenia z siecią routera przy użyciu zaktualizowanych danych logowania.

### 4. Konfiguracja połączenia z Internetem

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą panelu GL.iNet Web Admin Panel. Jeśli wolisz użyć aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Flint, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ax1800/internet/ax1800_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym (np. modemem).
    
    Po pomyślnym połączeniu z Internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ax1800/internet/ax1800_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wpisz hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z Internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem za pomocą istniejącej sieci Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ax1800/internet/ax1800_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering.
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering.
    
    Po pomyślnym połączeniu z Internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem za pomocą tetheringu USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ax1800/internet/ax1800_cellular.png){class="glboxshadow"}

    Podłącz modem USB z łącznością komórkową do portu USB routera. Jest to przydatne, gdy chcesz udostępniać Internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md).

## Jak skonfigurować VPN

Sieć VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Flint obsługuje OpenVPN, WireGuard i Tor.

=== "OpenVPN" 

    Flint (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych samouczków:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych samouczków:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na ochronę prywatności, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci przez użytkownika, co utrudnia śledzenie aktywności online.
    
    *[Jak skonfigurować Tor](../../interface_guide/tor.md).

## Sieć bezprzewodowa i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień zarówno dla sieci Wi-Fi 5 GHz, jak i 2,4 GHz, w tym włączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

    Aby skonfigurować Wireless, zapoznaj się z [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia blokowanie klienta i wykonywanie innych działań.

    Aby skonfigurować Clients, zapoznaj się z [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej komunikacji zdalnej i zdalnym zarządzaniu urządzeniami. Stworzona specjalnie do integracji z routerami GL.iNet, AstroWarp obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Skupiając się na zarządzaniu całą siecią i przyszłym wsparciu dla kontroli na poziomie sprzętowym, AstroWarp oferuje bardziej solidne i niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych i stabilnych sieci.

    Aby skonfigurować AstroWarp, zapoznaj się z [AstroWarp](../../interface_guide/astrowarp.md).

## Aplikacje

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego działania.
    
    Aby skonfigurować wtyczki, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamiczny DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest przydatny dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej.
    
    Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Sieć pamięci masowej to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć.
    
    Aby skonfigurować sieć pamięci masowej, zapoznaj się z [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie do blokowania reklam i trackerów w całej sieci, działające jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej.
    
    Aby skonfigurować AdGuard Home, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je. Obejmuje ograniczanie czasu korzystania z ekranu oraz blokowanie dostępu do określonych treści.

    Aby skonfigurować kontrolę rodzicielską, zapoznaj się z [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowanej programowo, które umożliwia tworzenie bezpiecznych sieci wirtualnych przez Internet, łącząc urządzenia tak, jakby znajdowały się w tej samej sieci lokalnej.
    
    Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.
    
    Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md). 

## Ustawienia sieciowe

=== "Port forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.
    
    Aby skonfigurować przekierowanie portów, zapoznaj się z [Port Forwards](../../interface_guide/port_forwarding.md). 

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. cellular, repeater i ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.
    
    Aby skonfigurować LAN, zapoznaj się z [Lan](../../interface_guide/lan.md). 

---

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz konfigurację ustawień zabezpieczeń, takich jak izolacja AP, dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z [Lan Tutorial](../../interface_guide/guest_network.md). 

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakiem DNS rebinding oraz nadpisanie ustawień DNS wszystkich klientów, zezwolenie niestandardowym DNS na zastąpienie DNS VPN, a także ustawienie trybu konfiguracji serwera DNS na automatyczny lub ręczne wskazanie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Port Management"

    Strona Port Management umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN na Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Aby zarządzać portami Ethernet, zapoznaj się z [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Tryb sieciowy odnosi się do ustawień konfiguracyjnych, które określają, w jaki sposób urządzenie łączy się z siecią i komunikuje z innymi urządzeniami.
    
    Aby skonfigurować tryb sieciowy, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana w celu zastąpienia IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne ze względu na rosnącą liczbę urządzeń podłączonych do Internetu.
    
    Aby skonfigurować IPV6, zapoznaj się z [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o takie funkcje jak AdGuard Home, szyfrowany DNS i klient VPN.
    
    Aby skonfigurować Drop-in Gateway, zapoznaj się z [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.
    
    Aby skonfigurować IGMP Snooping, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączanie i wyłączanie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemowe

=== "Overview"

    Strona Overview zapewnia kompleksowy przegląd bieżącego stanu routera oraz wskaźników wydajności. Na tej stronie możesz zobaczyć:

    * Średnie obciążenie CPU: monitoruj średnie obciążenie procesora routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: sprawdź, jaka część pamięci routera jest aktualnie używana, co pomaga w zarządzaniu zasobami.
    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Użycie pamięci flash: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że dostępna jest wystarczająca ilość miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, nazwę hosta, model, architekturę, wersję OpenWrt, wersję kernela, identyfikator urządzenia, MAC urządzenia i numer seryjny.
    * Zewnętrzna pamięć masowa: sprawdź stan zewnętrznych urządzeń pamięci masowej podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają kluczowe informacje i mechanizmy sterowania, pomagając skutecznie zarządzać pracą routera oraz ją monitorować.

    Szczegółowe instrukcje znajdziesz w [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, większe bezpieczeństwo i nowe funkcje. Strona oferuje dwie opcje aktualizacji:

    * Aktualizacja online oprogramowania: automatycznie sprawdza i instaluje najnowszą wersję firmware bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Lokalna aktualizacja oprogramowania: umożliwia ręczne przesłanie pliku firmware z komputera w celu zaktualizowania routera, dając kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router na bieżąco z najnowszymi usprawnieniami i poprawkami.

    Szczegółowe instrukcje znajdziesz w [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * Harmonogram diod LED: ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w określonych godzinach.
    * Zaplanowane ponowne uruchomienie: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram stanu Wi-Fi 5GHz: ustaw harmonogram sterowania pasmem Wi-Fi 5GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    * Harmonogram stanu Wi-Fi 2.4GHz: ustaw harmonogram sterowania pasmem Wi-Fi 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu może on lepiej odpowiadać Twoim potrzebom i preferencjom.

    Szczegółowe instrukcje znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie poprawnej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe są oznaczane czasem zgodnie z Twoim czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych zapisów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Strona obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki związane z działaniem i zdarzeniami kernela.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu internetowym i działaniu serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez wsparcie techniczne. Funkcja ta jest niezwykle przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w [Log](../../interface_guide/log.md).

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień bezpieczeństwa w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Ta strona zawiera opcje:

    * Hasło administratora: ustaw lub zmień hasło do interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj i ograniczaj dostęp do interfejsu routera z urządzeń podłączonych do sieci lokalnej.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera ze zdalnych lokalizacji przez Internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki w zabezpieczeniach i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do domyślnych ustawień aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa, korzystając z ustawień domyślnych bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Szczegółowe instrukcje znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md).
