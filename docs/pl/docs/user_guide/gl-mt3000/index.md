# Przewodnik użytkownika Beryl AX (GL-MT3000)

## Przegląd produktu

Beryl AX (GL-MT3000) to kompaktowy router podróżny AX3000 wykorzystujący standard Wi-Fi 6. Jest ulepszoną wersją modelu Beryl (GL-MT1300). Pracuje na dwurdzeniowym procesorze MT7981B 1.3GHz i oferuje ponad dwukrotnie wyższą łączną prędkość Wi-Fi. Został zaprojektowany z myślą o rodzinach intensywnie korzystających z Wi-Fi, a dzięki niewielkim rozmiarom świetnie sprawdza się również w podróży.

![gl-mt3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/hardware_info/mt3000_interface.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Beryl AX (GL-MT3000)
- 1 x instrukcja obsługi
- 1 x kabel Ethernet
- 1 x karta z podziękowaniem
- 1 x karta gwarancyjna
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![gl-MT3000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/first_time_setup/mt3000_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Beryl AX

Obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Podczas potwierdzania ustawień Wi‑Fi pamiętaj, że jeśli zmienisz dane sieci Wi-Fi, konieczne będzie ponowne połączenie urządzenia z siecią Wi-Fi routera przy użyciu zaktualizowanych danych.

### 4. Konfiguracja Internetu

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

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Beryl AX (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard. Dodatkowo obsługuje również Tor.

=== "OpenVPN"

    Beryl AX (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Beryl AX (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na ochronę prywatności, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci przez użytkownika, co utrudnia śledzenie aktywności online.

    * [How to set up Tor](../../interface_guide/tor.md)

## Sieć bezprzewodowa i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień zarówno dla sieci Wi-Fi 5 GHz, jak i 2.4 GHz, w tym włączanie i wyłączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie i wyłączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi, ustawianie hasła Wi-Fi, konfigurację widoczności SSID oraz wybór trybu Wi-Fi, szerokości pasma i kanału.

    Zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md), aby uzyskać szczegółowe instrukcje.

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę urządzenia, typ połączenia (tj. przez Ethernet lub Wi-Fi), adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia rezerwację IP, blokowanie klienta i wykonywanie innych działań.

    Zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md), aby uzyskać szczegółowe instrukcje.

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.

    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md), aby uzyskać szczegółowe instrukcje.

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana z myślą o bezproblemowej komunikacji zdalnej i zdalnym zarządzaniu urządzeniami. Stworzona specjalnie do integracji z routerami GL.iNet, AstroWarp obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Koncentrując się na zarządzaniu całymi sieciami oraz przyszłym wsparciu kontroli na poziomie sprzętowym, AstroWarp oferuje bardziej solidne i niezawodne rozwiązanie do zarządzania urządzeniami oraz utrzymywania bezpiecznych, stabilnych sieci.

    Zapoznaj się z poradnikiem [AstroWarp](../../interface_guide/astrowarp.md), aby uzyskać szczegółowe instrukcje.

## Aplikacje

=== "Plug-ins"

    Plug-in to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego działania.

    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md), aby uzyskać szczegółowe instrukcje.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest przydatny dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskania dostępu do sieci zdalnej.

    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md), aby uzyskać szczegółowe instrukcje.

=== "Network Storage"

    Network Storage to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć.

    Zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md), aby uzyskać szczegółowe instrukcje.

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie do blokowania reklam i trackerów w całej sieci, działające jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej.

    Zapoznaj się z poradnikiem [AdGuard Home](../../interface_guide/adguardhome.md), aby uzyskać szczegółowe instrukcje.

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je. Obejmuje ograniczanie czasu korzystania z ekranu oraz blokowanie dostępu do określonych treści.

    Zapoznaj się z poradnikiem [Parental Control](../../interface_guide/parental_control.md), aby uzyskać szczegółowe instrukcje.

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowanej programowo, które umożliwia tworzenie bezpiecznych sieci wirtualnych przez Internet, łącząc urządzenia tak, jakby znajdowały się w tej samej sieci lokalnej.

    Zapoznaj się z poradnikiem [ZeroTier](../../interface_guide/zerotier.md), aby uzyskać szczegółowe instrukcje.

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.

    Zapoznaj się z poradnikiem [Tailscale](../../interface_guide/tailscale.md), aby uzyskać szczegółowe instrukcje.

## Ustawienia sieci

=== "Port forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.

    Zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md), aby uzyskać szczegółowe instrukcje.

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. Cellular, Repeater i Ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md), aby uzyskać szczegółowe instrukcje.

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.

    Zapoznaj się z poradnikiem [Lan](../../interface_guide/lan.md), aby uzyskać szczegółowe instrukcje.

---

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz konfigurację ustawień zabezpieczeń, takich jak izolacja AP, dla sieci gościnnej.

    Zapoznaj się z poradnikiem [Guest Network](../../interface_guide/guest_network.md), aby uzyskać szczegółowe instrukcje.

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakiem DNS rebinding oraz nadpisanie ustawień DNS wszystkich klientów, zezwolenie niestandardowym serwerom DNS na zastąpienie DNS VPN, a także ustawienie trybu konfiguracji serwera DNS na automatyczny lub ręczne wskazanie serwerów DNS z połączenia Ethernet.

    Zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md), aby uzyskać szczegółowe instrukcje.

=== "Port Management"

    Strona Port Management umożliwia konfigurację portów WAN i LAN, ustawienie interfejsu WAN/LAN na Ethernet, określenie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlenie wynegocjowanej prędkości portu sieciowego.

    Zapoznaj się z poradnikiem [Port Management](../../interface_guide/ethernet_port.md), aby uzyskać szczegółowe instrukcje.

---

=== "Network Mode"

    Tryb sieciowy odnosi się do ustawień konfiguracyjnych, które określają, w jaki sposób urządzenie łączy się z siecią i komunikuje z innymi urządzeniami.

    Zapoznaj się z poradnikiem [Network Mode](../../interface_guide/network_mode.md), aby uzyskać szczegółowe instrukcje.

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana w celu zastąpienia IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne ze względu na rosnącą liczbę urządzeń podłączonych do Internetu.

    Zapoznaj się z poradnikiem [IPV6](../../interface_guide/network_mode.md), aby uzyskać szczegółowe instrukcje.

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o takie funkcje jak AdGuard Home, szyfrowany DNS i klient VPN.

    Zapoznaj się z poradnikiem [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md), aby uzyskać szczegółowe instrukcje.

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.

    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md), aby uzyskać szczegółowe instrukcje.

=== "Network Acceleration"

    Network Acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów ruchu.

    Zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md), aby uzyskać szczegółowe instrukcje.

=== "NAT Settings"

    Strona NAT Settings umożliwia włączanie i wyłączanie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Zapoznaj się z poradnikiem [NAT Settings](../../interface_guide/nat_settings.md), aby uzyskać szczegółowe instrukcje.

## Ustawienia systemowe

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

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, większe bezpieczeństwo i nowe funkcje. Strona oferuje dwie opcje aktualizacji:

    * Firmware Online Upgrade: automatycznie sprawdza i instaluje najnowszą wersję firmware bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Firmware Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera w celu zaktualizowania routera, dając kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router na bieżąco z najnowszymi usprawnieniami i poprawkami.

    Zapoznaj się z poradnikiem [Upgrade](../../interface_guide/upgrade.md), aby uzyskać szczegółowe instrukcje.

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * Harmonogram diod LED: ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w określonych godzinach.
    * Zaplanowane ponowne uruchomienie: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram stanu sieci Wi-Fi: ustaw harmonogram sterowania pasmem Wi-Fi 5GHz / 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.

    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu może on lepiej odpowiadać Twoim potrzebom i preferencjom.

    Zapoznaj się z poradnikiem [Scheduled Tasks](../../interface_guide/scheduled_tasks.md), aby uzyskać szczegółowe instrukcje.

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie poprawnej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe są oznaczane czasem zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych zapisów i prawidłowego działania konfiguracji opartych na czasie.

    Zapoznaj się z poradnikiem [Time Zone](../../interface_guide/time_zone.md), aby uzyskać szczegółowe instrukcje.

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przycisku przełącznika na routerze, pozwalając przypisać mu określone funkcje dla szybkiego dostępu i sterowania. Funkcja ta zapewnia wygodne skróty do typowych zadań i ustawień, poprawiając komfort użytkowania oraz upraszczając zarządzanie routerem.

    Zapoznaj się z poradnikiem [Toggle Button Settings](../../interface_guide/toggle_button_settings.md), aby uzyskać szczegółowe instrukcje.

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Strona obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki związane z działaniem i zdarzeniami kernela.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu internetowym i działaniu serwera.

    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez wsparcie techniczne. Funkcja ta jest niezwykle przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Zapoznaj się z poradnikiem [Log](../../interface_guide/log.md), aby uzyskać szczegółowe instrukcje.

---

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień bezpieczeństwa w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Ta strona zawiera opcje:

    * Admin Password: ustaw lub zmień hasło do interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj i ograniczaj dostęp do interfejsu routera z urządzeń podłączonych do sieci lokalnej.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera ze zdalnych lokalizacji przez Internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki w zabezpieczeniach i nieautoryzowany dostęp.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Zapoznaj się z poradnikiem [Security](../../interface_guide/security.md), aby uzyskać szczegółowe instrukcje.

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa, korzystając z ustawień domyślnych bieżącego firmware.

    Zapoznaj się z poradnikiem [Reset Firmware](../../interface_guide/reset_firmware.md), aby uzyskać szczegółowe instrukcje.

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Zapoznaj się z poradnikiem [Advanced Settings](../../interface_guide/advanced_settings.md), aby uzyskać szczegółowe instrukcje.
