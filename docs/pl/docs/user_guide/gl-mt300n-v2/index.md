# Przewodnik użytkownika Mango (GL-MT300N-V2)

## Przegląd produktu

Mango (GL-MT300N-V2) to kieszonkowy mini router zaprojektowany z myślą o mobilności i podróżach, obsługujący bezprzewodową transmisję z prędkością do 300Mbps. Mango oferuje zaawansowane funkcje bezpieczeństwa, w tym obsługę OpenVPN, WireGuard® oraz serwera DNS. Umożliwia nie tylko przekształcenie publicznej sieci w prywatną sieć Wi-Fi do bezpiecznego surfowania po Internecie, ale także przesyłanie plików konfiguracyjnych VPN od ponad 30 dostawców usług VPN i ustawienie routera jako klienta VPN, zapewniając dodatkową warstwę prywatności i bezpieczeństwa dzięki szyfrowanemu połączeniu między urządzeniem a serwerem VPN.

![mt300n-v2 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/product_info/mt300n_v2_overview.png){class="glboxshadow"}

## Jak skonfigurować Mango

Aby skonfigurować Mango, użyj jednej z czterech obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering oraz Cellular. Wykonaj poniższe kroki.

### 1. Włączenie zasilania

Podłącz przewód zasilający Micro USB do portu zasilania routera, a następnie drugi koniec do zasilacza 5V/2A (brak w zestawie) i do gniazdka elektrycznego.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wpisz hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie znajdującej się na spodzie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Pamiętaj, że jeśli zmienisz ustawienia Wi‑Fi, konieczne będzie ponowne połączenie urządzenia z siecią Wi-Fi routera przy użyciu zaktualizowanych danych.

### 4. Konfiguracja Internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą webowego panelu administracyjnego GL.iNet. Jeśli wolisz użyć aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Mango, korzystając z jednej z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering oraz Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem.

    Po pomyślnym połączeniu z Internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md), aby uzyskać szczegółowe instrukcje.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w webowym panelu administracyjnym znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wpisz hasło, a następnie kliknij **Apply**.

    Po pomyślnym połączeniu z Internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md), aby uzyskać szczegółowe instrukcje.

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering.
    3. Na stronie INTERNET w webowym panelu administracyjnym kliknij **Connect** w sekcji Tethering.

    Po pomyślnym połączeniu z Internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md), aby uzyskać szczegółowe instrukcje.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/usb_modem.png){class="glboxshadow"}

    Ta metoda jest przydatna do udostępniania Internetu z modemu USB wszystkim podłączonym urządzeniom.

    1. Włóż modem USB z obsługą sieci komórkowej do portu USB routera.
    2. Na stronie INTERNET w webowym panelu administracyjnym znajdź sekcję Cellular i kliknij **Connect**.
    3. Po pomyślnym połączeniu z Internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Zapoznaj się z poradnikiem [Connect to the Internet via a USB modem](../../interface_guide/internet_cellular.md), aby uzyskać szczegółowe instrukcje.

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczne, szyfrowane połączenie między urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Mango (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard.

=== "OpenVPN"

    Mango (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia wysoki poziom bezpieczeństwa. Aby skonfigurować OpenVPN, skorzystaj z poniższych poradników:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango (i inne routery GL.iNet) obsługuje protokół WireGuard, który oferuje wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, skorzystaj z poniższych poradników:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

## Aplikacje

=== "Plug-ins"

    Plug-ins to dodatkowe funkcje rozszerzające możliwości routera.

    Zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną. Jest szczególnie przydatny dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskania dostępu do sieci zdalnej.

    Zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Usługa chmurowa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty i wygodny sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.

    Zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

## Ustawienia sieci

=== "Firewall"

    Strona Firewall zapewnia najważniejsze funkcje bezpieczeństwa dla sieci. Obejmuje takie funkcje jak Port Forwarding, Open Ports oraz DMZ. Narzędzia te pozwalają zarządzać ruchem sieciowym i dostosowywać jego przepływ, a także zwiększać bezpieczeństwo sieci.

    * Port Forwarding: przekierowuje określony ruch z Internetu do wskazanych urządzeń w sieci, umożliwiając dostęp do usług takich jak serwery gier lub serwery WWW.
    * Open Ports: pozwala monitorować i kontrolować, które porty routera są otwarte, pomagając zapobiegać nieautoryzowanemu dostępowi i potencjalnym zagrożeniom bezpieczeństwa.
    * DMZ (Demilitarized Zone): umieszcza urządzenie poza główną zaporą, umożliwiając mu nieograniczony dostęp do Internetu, a jednocześnie chroniąc pozostałą część sieci przed potencjalnymi zagrożeniami.

    Zapoznaj się z poradnikiem [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która umożliwia skonfigurowanie routera z wieloma połączeniami internetowymi (np. Cellular, Repeater i Ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do Internetu.

    Zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Strona LAN umożliwia zarządzanie i konfigurację ustawień sieci lokalnej routera. Najważniejsze funkcje dostępne na tej stronie obejmują:

    * Adres IP routera: zmień adres IP routera, aby lepiej dopasować go do konfiguracji sieci.
    * Maska sieci: ustaw maskę podsieci, która określa wielkość sieci i zakres adresów IP.
    * DHCP: włącz lub skonfiguruj protokół Dynamic Host Configuration Protocol, który automatycznie przypisuje adresy IP urządzeniom w sieci.
    * Rezerwacja adresów: zarezerwuj określone adresy IP dla konkretnych urządzeń, aby zawsze otrzymywały ten sam adres IP z serwera DHCP.

    Zapoznaj się z poradnikiem [Lan](../../interface_guide/lan.md).

---

=== "DNS"

    Strona DNS umożliwia dostosowanie ustawień systemu nazw domen routera, zwiększając zarówno bezpieczeństwo, jak i wydajność. Najważniejsze funkcje dostępne na tej stronie obejmują:

    * Encrypted DNS: skonfiguruj szyfrowany DNS, aby chronić dane przeglądania przed monitorowaniem lub manipulacją, zapewniając prywatność i bezpieczeństwo.
    * Manual DNS: ręcznie ustaw wybrane serwery DNS, co zapewnia większą kontrolę nad zapytaniami DNS i może skrócić czas rozwiązywania nazw.
    * DNS Proxy: włącz proxy DNS, aby kierować żądania DNS z urządzeń przez określony serwer DNS, zapewniając dodatkową warstwę kontroli nad ruchem DNS.

    Ustawienia te pozwalają zoptymalizować wydajność i bezpieczeństwo DNS w sieci zgodnie z konkretnymi potrzebami.

    Zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Strona Network Mode umożliwia skonfigurowanie routera do pracy w różnych trybach, zapewniając elastyczność potrzebną w różnych scenariuszach sieciowych. Dostępne tryby obejmują:

    * Router: działa jako standardowy router, zarządzając ruchem między siecią lokalną a Internetem oraz zapewniając funkcje takie jak NAT, zapora i DHCP.
    * Access Point: działa jako punkt dostępowy, rozszerzając istniejącą sieć przewodową o łączność bezprzewodową bez routowania ruchu.
    * Extender: działa jako wzmacniacz zasięgu, zwiększając sygnał istniejącej sieci bezprzewodowej, aby objąć większy obszar i wyeliminować martwe strefy.
    * WDS (Wireless Distribution System): podobnie jak Extender; wybierz WDS, jeśli główny router obsługuje tryb WDS.

    Zapoznaj się z poradnikiem [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    Strona IPv6 umożliwia konfigurację ustawień IPv6 w sieci, zapewniając obsługę najnowszego protokołu internetowego. Na tej stronie możesz włączyć IPv6 i wybrać jeden z czterech trybów odpowiednich dla wymagań sieci:

    * Native: uzyskaj adres IPv6 bezpośrednio od dostawcy Internetu, co pozwala na prostą i wydajną natywną łączność IPv6.
    * Passthrough: pozwól, aby ruch IPv6 przechodził przez router do urządzeń w sieci, skutecznie mostkując połączenie bez obsługi routingu IPv6 przez sam router.
    * NAT6: wykorzystaj translację adresów sieciowych dla IPv6 (NAT6), tłumacząc wewnętrzne i zewnętrzne adresy IPv6 podobnie jak NAT działa dla IPv4.
    * Static IPv6: ręcznie skonfiguruj statyczny adres IPv6 dla routera, zapewniając stały adres dla stabilnej łączności i łatwiejszego zarządzania usługami sieciowymi.

    Ustawienia te pomagają wykorzystać zalety IPv6, w tym większą przestrzeń adresową, lepsze funkcje bezpieczeństwa i wyższą wydajność.

    Zapoznaj się z poradnikiem [IPv6](../../interface_guide/network_mode.md).

---

=== "MAC Address"

    Strona MAC Address umożliwia wyświetlanie i zarządzanie adresami MAC powiązanymi z routerem. Najważniejsze funkcje dostępne na tej stronie obejmują:

    * Factory Default: wyświetla domyślne adresy MAC routera dla trybów Ethernet i Repeater, zapewniając odniesienie do oryginalnych ustawień sprzętowych.
    * Clone: klonuje adres MAC konkretnego urządzenia klienckiego. Jest to szczególnie przydatne w sytuacjach, gdy dostęp do sieci jest ograniczony do wybranych urządzeń.
    * Manual: umożliwia ręczne określenie niestandardowego adresu MAC dla routera. Dodatkowo możesz użyć przycisku Random, aby wygenerować losowy adres MAC, co zapewnia większą elastyczność i prywatność.

    Funkcje te umożliwiają skuteczne zarządzanie adresami MAC routera, zapewniając zgodność i elastyczność w różnych środowiskach sieciowych.

    Zapoznaj się z poradnikiem [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może nie posiadać, w tym AdGuard Home, szyfrowany DNS oraz VPN.

    Zapoznaj się z poradnikiem [How to set up Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    Strona IGMP Snooping umożliwia konfigurację ustawień optymalizujących zarządzanie ruchem multicast w sieci. IGMP Snooping nasłuchuje pakietów protokołu IGMP i wyodrębnia z nich informacje, tworząc oraz utrzymując tablice przekazywania multicastu warstwy 2. Dzięki temu dane grup multicast są przekazywane wyłącznie do hostów, które dołączyły do danej grupy, co zapobiega docieraniu niepożądanego ruchu multicast do innych hostów.

    Ustawienia te pomagają zoptymalizować wydajność i efektywność sieci, zwłaszcza w środowiskach z dużym natężeniem ruchu multicast, takich jak strumieniowanie wideo lub gry online.

    Zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Ustawienia systemowe

=== "Overview"

    Strona Overview zapewnia kompleksowy przegląd bieżącego stanu routera oraz wskaźników wydajności. Na tej stronie możesz zobaczyć:

    * Średnie obciążenie CPU: monitoruj średnie obciążenie procesora routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: sprawdź, jaka część pamięci routera jest aktualnie używana, co pomaga w zarządzaniu zasobami.
    * Użycie pamięci flash: sprawdź wykorzystanie pamięci flash routera, aby upewnić się, że dostępna jest wystarczająca ilość miejsca na firmware i dane konfiguracyjne.
    * Sterowanie diodami LED: włączaj lub wyłączaj diody LED routera, aby dostosować wizualne wskaźniki urządzenia.
    * Informacje o systemie: uzyskaj szczegółowe informacje o systemie routera, w tym wersję firmware, czas działania i stan sieci.

    Funkcje te zapewniają kluczowe informacje i mechanizmy sterowania, pomagając skutecznie zarządzać pracą routera oraz ją monitorować.

    Zapoznaj się z poradnikiem [Overview](../../interface_guide/system_overview.md), aby uzyskać szczegółowe instrukcje.

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, co zapewnia lepszą wydajność, większe bezpieczeństwo i nowe funkcje. Strona oferuje dwie opcje aktualizacji:

    * Online Upgrade: automatycznie sprawdza i instaluje najnowszą wersję firmware bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Local Upgrade: umożliwia ręczne przesłanie pliku firmware z komputera w celu zaktualizowania routera, dając kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router na bieżąco z najnowszymi usprawnieniami i poprawkami.

    Zapoznaj się z poradnikiem [Upgrade](../../interface_guide/upgrade.md), aby uzyskać szczegółowe instrukcje.

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera na podstawie zdefiniowanego harmonogramu, zwiększając wygodę i efektywność. Najważniejsze funkcje tej strony obejmują:

    * Harmonogram diod LED: ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, aby ograniczyć emisję światła w określonych godzinach.
    * Zaplanowane ponowne uruchomienie: skonfiguruj router tak, aby uruchamiał się ponownie automatycznie w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * Harmonogram stanu Wi-Fi 2.4GHz: ustaw harmonogram sterowania pasmem Wi-Fi 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.

    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera, dzięki czemu może on lepiej odpowiadać Twoim potrzebom i preferencjom.

    Zapoznaj się z poradnikiem [Scheduled Tasks](../../interface_guide/scheduled_tasks.md), aby uzyskać szczegółowe instrukcje.

---

=== "Admin Password"

    Strona Admin Password umożliwia ustawienie lub zmianę hasła do interfejsu administracyjnego routera, zapewniając, że tylko uprawnieni użytkownicy mogą uzyskiwać dostęp do ustawień routera i je modyfikować. To hasło ma kluczowe znaczenie dla utrzymania bezpieczeństwa i integralności sieci, chroniąc przed nieautoryzowanym dostępem i zmianami konfiguracji.

    Zapoznaj się z poradnikiem [Admin Password](../../interface_guide/admin_password.md), aby uzyskać szczegółowe instrukcje.

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie poprawnej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe są oznaczane czasem zgodnie z czasem lokalnym. To ustawienie ma kluczowe znaczenie dla prowadzenia dokładnych zapisów i prawidłowego działania konfiguracji opartych na czasie.

    Zapoznaj się z poradnikiem [Time Zone](../../interface_guide/time_zone.md), aby uzyskać szczegółowe instrukcje.

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przycisku przełącznika na routerze, pozwalając przypisać mu określone funkcje dla szybkiego dostępu i sterowania. Funkcja ta zapewnia wygodne skróty do typowych zadań i ustawień, poprawiając komfort użytkowania oraz upraszczając zarządzanie routerem.

    Zapoznaj się z poradnikiem [Toggle Button Settings](../../interface_guide/toggle_button_settings.md), aby uzyskać szczegółowe instrukcje.

---

=== "Log"

    Strona Log zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Strona obejmuje:

    * System Log: szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: dzienniki związane z działaniem i zdarzeniami kernela.
    * Crash Log: zapisy awarii systemu i błędów, przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: dzienniki serwera WWW Nginx, jeśli jest używany przez router, zawierające informacje o ruchu internetowym i działaniu serwera.

    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez wsparcie techniczne. Funkcja ta jest niezwykle przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Zapoznaj się z poradnikiem [Log](../../interface_guide/log.md), aby uzyskać szczegółowe instrukcje.

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do ustawień domyślnych aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz rozpocząć konfigurację od nowa, korzystając z ustawień domyślnych bieżącego firmware.

    Zapoznaj się z poradnikiem [Reset Firmware](../../interface_guide/reset_firmware.md), aby uzyskać szczegółowe instrukcje.

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Zapoznaj się z poradnikiem [Advanced Settings](../../interface_guide/advanced_settings.md), aby uzyskać szczegółowe instrukcje.