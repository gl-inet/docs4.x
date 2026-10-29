# Przewodnik użytkownika Slate Plus (GL-A1300) {#slate-plus-gl-a1300-user-guide}

## Opis produktu {#product-overview}

Slate Plus (GL-A1300) to kieszonkowy router podróżny z wydajnym procesorem zoptymalizowanym pod kątem stabilności sieci i sprawnego szyfrowania VPN. Oferuje nasze najnowsze funkcje bezpieczeństwa i działa na najnowszej wersji systemu OpenWrt. Został zaprojektowany z myślą o osobach często podróżujących, które intensywnie korzystają z sieci VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Zawartość opakowania {#package-contents}

Pamiętaj, że zasilacz dołączony do zestawu zależy od kraju dostawy.

W opakowaniu znajdują się:

- 1 x instrukcja obsługi
- 1 x Slate Plus (GL-A1300)
- 1 x kabel Ethernet
- 1 x karta z podziękowaniem
- 1 x karta gwarancyjna
- 1 x zasilacz
- 1 x przejściówka (zależnie od kraju dostawy)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Slate Plus {#how-to-set-up-slate-plus}

Obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Dodatkowe wskazówki znajdziesz w sekcji [Pierwsza konfiguracja](../../faq/first_time_setup.md).

### 1. Włączenie zasilania {#1-power-on}

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka elektrycznego. Urządzenie uruchomi się automatycznie.

### 2. Podłączenie urządzenia {#2-connect-device}

Połącz urządzenie (np. komputer, laptop lub smartfon) z routerem przez Wi-Fi albo Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie na spodzie routera.

### 3. Logowanie do panelu administracyjnego {#3-log-in-to-web-admin-panel}

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Podczas potwierdzania ustawień Wi‑Fi pamiętaj, że jeśli zmienisz dane sieci Wi‑Fi, konieczne będzie ponowne połączenie urządzenia z siecią routera przy użyciu zaktualizowanych danych logowania.

### 4. Konfiguracja połączenia z Internetem {#4-internet-setup}

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą panelu GL.iNet Web Admin Panel. Jeśli wolisz użyć aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Slate Plus, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym (np. modemem).
    
    Po pomyślnym połączeniu z Internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem za pomocą kabla Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wpisz hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z Internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem za pomocą istniejącej sieci Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering.
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering.
    
    Po pomyślnym połączeniu z Internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem za pomocą tetheringu USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

    Podłącz modem USB z łącznością komórkową do portu USB routera. Jest to przydatne, gdy chcesz udostępniać Internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w [Połącz z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md).

---

## Wireless {#wireless}

Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5 GHz i 2.4 GHz, w tym włączanie Wi-Fi, ustawianie mocy nadawania, nazwy Wi-Fi (SSID), trybu zabezpieczeń i hasła Wi-Fi, widoczności SSID, trybu Wi-Fi, szerokości pasma i kanału.

Aby skonfigurować Wireless, zapoznaj się z [Wireless](../../interface_guide/wireless_v4.8.md).

## CLIENTS {#clients}

Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia blokowanie klienta i wykonywanie innych działań.

Aby skonfigurować Clients, zapoznaj się z [Clients](../../interface_guide/clients.md).

## VPN {#vpn}

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany tunel między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN), a także umożliwia dostęp do sieci zdalnej (serwer VPN). Slate Plus (podobnie jak inne routery GL.iNet) obsługuje OpenVPN i WireGuard. Dodatkowo obsługuje także Tor.

=== "OpenVPN"

    Slate Plus (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate Plus (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, czyli The Onion Router, to sieć nastawiona na ochronę prywatności, która umożliwia anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów (węzłów) obsługiwanych przez wolontariuszy, aby ukryć lokalizację i sposób korzystania z sieci przez użytkownika, co utrudnia śledzenie aktywności online.
    
    * [Jak skonfigurować Tor](../../interface_guide/tor.md).

## Aplikacje {#applications}

=== "Plug-ins"

    Wtyczka to komponent oprogramowania, który dodaje określone funkcje do istniejącego programu komputerowego, umożliwiając dostosowanie i rozszerzenie jego możliwości.
    
    Aby skonfigurować wtyczki, zapoznaj się z [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamiczny DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Mapuje nazwę domeny na dynamiczny publiczny adres IP routera, dzięki czemu możesz zdalnie uzyskiwać dostęp do swojej sieci bez statycznego adresu IP.
    
    Aby skonfigurować Dynamic DNS, zapoznaj się z [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Usługa chmurowa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z [GoodCloud](../../interface_guide/cloud.md).

=== "Network Storage"

    Sieć pamięci masowej to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików oraz ich współdzielenie przez sieć.
    
    Aby skonfigurować sieć pamięci masowej, zapoznaj się z [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home to rozwiązanie do blokowania reklam i trackerów w całej sieci, działające jako serwer DNS filtrujący niechciane treści na wszystkich urządzeniach podłączonych do sieci domowej.
    
    Aby skonfigurować AdGuard Home, zapoznaj się z [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci i kontrolować je, między innymi przez ograniczanie czasu korzystania z ekranu i dostępu do określonych treści.

    Aby skonfigurować Parental Control, zapoznaj się z [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier to rozwiązanie sieci definiowanej programowo, które umożliwia tworzenie bezpiecznych sieci wirtualnych przez Internet, łącząc urządzenia tak, jakby znajdowały się w tej samej sieci lokalnej.
    
    Aby skonfigurować ZeroTier, zapoznaj się z [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale to usługa VPN, która umożliwia dostęp do urządzeń i aplikacji z dowolnego miejsca.
    
    Aby skonfigurować Tailscale, zapoznaj się z [Tailscale](../../interface_guide/tailscale.md).

## Sieć {#network}

=== "Firewall"

    Strona Firewall zapewnia podstawowe ulepszenia bezpieczeństwa sieci. Obejmuje funkcje takie jak Port Forwarding, Open Ports i DMZ. Narzędzia te umożliwiają zarządzanie przepływem ruchu w sieci oraz zwiększają jej bezpieczeństwo.

    * Port Forwarding: przekierowuje określony ruch z internetu do wskazanych urządzeń w sieci, umożliwiając dostęp do usług takich jak serwery gier lub serwery WWW.
    * Open Ports: pozwala monitorować i kontrolować, które porty routera są otwarte, pomagając zapobiegać nieautoryzowanemu dostępowi i potencjalnym zagrożeniom.
    * DMZ (Demilitarized Zone): udostępnia jedno urządzenie w Internecie, przekierowując do niego cały ruch przychodzący.

    Zapoznaj się z poradnikiem [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi jednocześnie (np. Ethernet, Repeater i Tethering). Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, czyli Local Area Network, to sieć łącząca komputery i urządzenia na ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, dzięki czemu urządzenia mogą sprawnie komunikować się ze sobą.
    
    Aby skonfigurować LAN, zapoznaj się z [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Umożliwia ustawienie podsieci w prywatnych zakresach adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określenie adresów IP bramy i maski sieci oraz konfigurację ustawień zabezpieczeń, takich jak izolacja AP, dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    Strona DNS umożliwia ustawienie niestandardowych serwerów DNS, włączenie ochrony przed atakami DNS rebinding, nadpisanie ustawień DNS wszystkich klientów oraz zezwolenie niestandardowym serwerom DNS na zastąpienie DNS VPN. Możesz korzystać z serwerów DNS automatycznie uzyskanych z urządzeń nadrzędnych lub ręcznie wskazać niestandardowe serwery DNS.

    Aby skonfigurować DNS, zapoznaj się z [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Tryb sieciowy odnosi się do ustawień konfiguracyjnych, które określają, w jaki sposób urządzenie łączy się z siecią i komunikuje z innymi urządzeniami.
    
    Aby skonfigurować tryb sieciowy, zapoznaj się z [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, czyli Internet Protocol version 6, to najnowsza wersja protokołu internetowego zaprojektowana w celu zastąpienia IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne ze względu na rosnącą liczbę urządzeń podłączonych do Internetu.
    
    Aby skonfigurować IPV6, zapoznaj się z [IPV6](../../interface_guide/ipv6.md).

=== "MAC Address"

    Strona MAC Address umożliwia podgląd i zarządzanie adresami Media Access Control (MAC) powiązanymi z routerem. Dostępne funkcje obejmują:

    * Factory Default: wyświetlenie domyślnych adresów MAC dla trybów Ethernet i Repeater jako odniesienia do oryginalnych ustawień sprzętowych.
    * Clone: sklonowanie adresu MAC konkretnego urządzenia klienckiego. Jest to szczególnie przydatne w sytuacjach, gdy dostęp do sieci jest ograniczony do wybranych urządzeń.
    * Manual: ręczne podanie niestandardowego adresu MAC routera. Dodatkowo możesz użyć przycisku Random, aby wygenerować losowy adres MAC, co zapewnia większą elastyczność i prywatność.

    Funkcje te umożliwiają skuteczne zarządzanie adresami MAC routera, zapewniając zgodność i elastyczność w różnych środowiskach sieciowych.

    Zapoznaj się z poradnikiem [MAC Address](../../interface_guide/mac_address.md).

---

=== "Drop-in Gateway"

    Drop-in gateway rozszerza funkcjonalność głównego routera, w tym o AdGuard Home, szyfrowany DNS i klienta VPN.
    
    Aby skonfigurować Drop-in Gateway, skorzystaj z poniższych poradników:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Konfiguracja Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania ruchem multicast i jego kontroli.
    
    Aby skonfigurować IGMP Snooping, zapoznaj się z [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączanie i wyłączanie funkcji Full Cone NAT oraz SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zapoznaj się z [NAT Settings](../../interface_guide/nat_settings.md).

## System {#system}

=== "Overview"

    Strona Overview zapewnia kompleksowy przegląd bieżącego stanu routera oraz wskaźników wydajności. Na tej stronie możesz zobaczyć:

    * CPU Average Load: średnie obciążenie procesora routera, które pomaga ocenić wydajność i wykryć potencjalne wąskie gardła.
    * Użycie pamięci: sprawdź, jaka część pamięci routera jest aktualnie używana, co pomaga w zarządzaniu zasobami.
    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Użycie pamięci flash: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że dostępna jest wystarczająca ilość miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: uzyskaj szczegółowe informacje o systemie routera, w tym czas działania, nazwę hosta, model, architekturę, wersję OpenWrt, wersję kernela, identyfikator urządzenia, MAC urządzenia i numer seryjny.
    * Zewnętrzna pamięć masowa: sprawdź stan zewnętrznych urządzeń pamięci masowej podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Funkcje te zapewniają kluczowe informacje i mechanizmy sterowania, pomagając skutecznie zarządzać pracą routera oraz ją monitorować.

    Szczegółowe instrukcje znajdziesz w [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, większe bezpieczeństwo i nowe funkcje. Strona oferuje dwie opcje aktualizacji:

    * Aktualizacja online oprogramowania: automatyczne sprawdzanie dostępności najnowszej wersji firmware na serwerze producenta. Jeśli jest dostępna online, możesz ją zainstalować.
    * Lokalna aktualizacja oprogramowania: umożliwia ręczne przesłanie pliku firmware z komputera w celu zaktualizowania routera, dając kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router na bieżąco z najnowszymi usprawnieniami i poprawkami.

    Szczegółowe instrukcje znajdziesz w [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * Harmonogram diod LED: ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w określonych godzinach.
    * Zaplanowane ponowne uruchomienie: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram stanu Wi-Fi: Ustaw harmonogram sterowania pasmem Wi-Fi 5 GHz / 2,4 GHz, umożliwiając lepsze zarządzanie dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu może on lepiej odpowiadać Twoim potrzebom i preferencjom.

    Szczegółowe instrukcje znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie poprawnej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe są oznaczane czasem zgodnie z Twoim czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych zapisów i prawidłowego działania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przełącznika na routerze, pozwalając przypisać do niego określone funkcje zapewniające szybki dostęp i kontrolę. Ta funkcja zapewnia wygodne skróty do typowych zadań i ustawień, ułatwiając zarządzanie routerem.

    Szczegółowe instrukcje znajdziesz w artykule [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Strona obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki związane z działaniem i zdarzeniami kernela.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu internetowym i działaniu serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez wsparcie techniczne. Funkcja ta jest niezwykle przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w [Log](../../interface_guide/log.md).

---

=== "Security"

    **Uwaga**: Ta funkcja jest dostępna od wersji v4.5.

    Strona Security umożliwia konfigurację różnych ustawień bezpieczeństwa w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Ta strona zawiera opcje:

    * Hasło administratora: ustaw lub zmień hasło do interfejsu administracyjnego routera, aby tylko uprawnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: zarządzaj i ograniczaj dostęp do interfejsu routera z urządzeń podłączonych do sieci lokalnej.
    * Remote Access Control: konfiguruj i ograniczaj dostęp do interfejsu routera ze zdalnych lokalizacji przez Internet, zwiększając ochronę przed zagrożeniami zewnętrznymi.

    Ustawienia te pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.
    
    Szczegółowe instrukcje znajdziesz w [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do domyślnych ustawień aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa, korzystając z ustawień domyślnych bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Szczegółowe instrukcje znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md).
