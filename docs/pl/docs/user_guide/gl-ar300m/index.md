# Przewodnik użytkownika Shadow (GL-AR300M Series)

## Przegląd produktu

Shadow (seria GL-AR300M) to kieszonkowy mini router zaprojektowany z myślą o mobilności i podróżach, obsługujący bezprzewodową transmisję do 300Mbps. Shadow oferuje zaawansowane funkcje bezpieczeństwa, w tym obsługę OpenVPN, WireGuard® i serwera DNS. Umożliwia nie tylko przekształcenie publicznej sieci w prywatną sieć Wi-Fi do bezpiecznego surfowania, ale także przesyłanie plików konfiguracyjnych VPN od ponad 30 dostawców usług VPN i skonfigurowanie urządzenia jako klienta VPN, co zapewnia dodatkową warstwę prywatności i bezpieczeństwa poprzez tworzenie szyfrowanego ruchu między Twoim urządzeniem a serwerem VPN.

![ar300m illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/product_info/mt300n_v2_overview.png){class="glboxshadow"}

## Jak skonfigurować Shadow

Aby skonfigurować Shadow, użyj jednej z czterech obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Wykonaj poniższe kroki. 

### 1. Włączenie zasilania

Podłącz przewód zasilający Micro USB do portu zasilania routera, następnie podłącz drugi koniec do zasilacza 5V/2A (brak w zestawie) i włóż go do gniazdka elektrycznego. 

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera przez Wi-Fi albo Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet. 

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. Domyślną nazwę sieci i hasło znajdziesz na naklejce na spodzie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**. 

Pamiętaj, że jeśli zmienisz ustawienia Wi‑Fi, musisz ponownie połączyć urządzenie z siecią Wi‑Fi routera przy użyciu zaktualizowanych danych.

### 4. Konfiguracja internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router przez panel GL.iNet Web Admin Panel. Jeśli wolisz używać aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj Shadow, korzystając z jednej z obsługiwanych metod połączenia z internetem: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/ethernet.png){class="glboxshadow"}
    
    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem. 
    
    Po pomyślnym połączeniu z internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Połącz z internetem przez kabel Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET w web Admin Panel znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci. 
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Połącz z internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB. 
    2. Na urządzeniu mobilnym przejdź do Settings i włącz USB Tethering. 
    3. Na stronie INTERNET w web Admin Panel kliknij **Connect** w sekcji Tethering. 
    
    Po pomyślnym połączeniu z internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Połącz z internetem przez USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/usb_modem.png){class="glboxshadow"}

    Ta metoda jest przydatna do udostępniania internetu z modemu USB wszystkim podłączonym urządzeniom.

    1. Włóż modem USB z obsługą sieci komórkowej do portu USB routera.
    2. Na stronie INTERNET w web Admin Panel znajdź sekcję Cellular i kliknij **Connect**.
    3. Po pomyślnym połączeniu z internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Połącz z internetem przez modem USB](../../interface_guide/internet_cellular.md).

## Jak skonfigurować VPN 

VPN (wirtualna sieć prywatna) tworzy bezpieczny, szyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Shadow (i inne routery GL.iNet) obsługuje OpenVPN i WireGuard.

=== "OpenVPN" 

    Shadow (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia silne zabezpieczenia. Skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Shadow (i inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia dużą szybkość i wygodę. Skorzystaj z poniższych poradników:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

## Aplikacje

=== "Plug-ins"

    Plug-ins to dodatkowe funkcje rozszerzające możliwości routera.
    
    Przejdź do poradnika [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest najbardziej przydatny dla użytkowników, którzy potrzebują statycznego adresu IP do uzyskiwania dostępu do sieci zdalnej.
    
    Przejdź do poradnika [Dynamic DNS](../../interface_guide/ddns.md). 

=== "GoodCloud"

    Usługa zarządzania chmurowego GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu do routerów GL.iNet oraz zarządzania nimi.
    
    Przejdź do poradnika [GoodCloud](../../interface_guide/cloud.md).

## Ustawienia sieciowe

=== "Firewall"

    Strona Firewall zapewnia podstawowe ulepszenia bezpieczeństwa sieci. Obejmuje funkcje takie jak Port Forwarding, Open Ports i DMZ. Narzędzia te pozwalają zarządzać ruchem sieciowym i dostosowywać go, a także zwiększać poziom bezpieczeństwa.

    * Port Forwarding: Przekierowuj określony ruch z internetu do wskazanych urządzeń w sieci, aby umożliwić dostęp do usług takich jak serwery gier lub serwery WWW.
    * Open Ports: Monitoruj i kontroluj, które porty na routerze są otwarte, aby zapobiegać nieautoryzowanemu dostępowi i potencjalnym zagrożeniom.
    * DMZ (Demilitarized Zone): Umieść urządzenie poza główną zaporą, aby miało nieograniczony dostęp do internetu, jednocześnie chroniąc resztę sieci przed potencjalnymi zagrożeniami.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa umożliwiająca jednoczesne skonfigurowanie wielu połączeń internetowych (np. cellular, repeater i ethernet) w tym samym czasie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie internetowe. Zapewnia to płynny i nieprzerwany dostęp do internetu. 

    Przejdź do poradnika [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    Strona LAN umożliwia zarządzanie i konfigurowanie ustawień sieci lokalnej routera. Najważniejsze funkcje dostępne na tej stronie to:

    * Router IP Address: Zmień adres IP routera, aby lepiej dopasować go do konfiguracji swojej sieci.
    * Netmask: Ustaw maskę podsieci dla swojej sieci, która określa rozmiar sieci i zakres adresów IP.
    * DHCP: Włącz lub skonfiguruj protokół Dynamic Host Configuration Protocol, który automatycznie przypisuje adresy IP urządzeniom w sieci.
    * Address Reservation: Zarezerwuj określone adresy IP dla konkretnych urządzeń, aby zawsze otrzymywały ten sam adres IP z serwera DHCP.

    Przejdź do poradnika [LAN](../../interface_guide/lan.md). 

---

=== "DNS"

    Strona DNS udostępnia opcje dostosowywania ustawień Domain Name System routera, zwiększając zarówno bezpieczeństwo, jak i wydajność. Najważniejsze funkcje dostępne na tej stronie to:

    * Encrypted DNS: Skonfiguruj zaszyfrowany DNS, aby chronić dane przeglądania przed monitorowaniem lub manipulacją, zapewniając prywatność i bezpieczeństwo.
    * Manual DNS: Ręcznie ustaw wybrane serwery DNS, aby mieć większą kontrolę nad zapytaniami DNS i potencjalnie skrócić czas rozwiązywania nazw.
    * DNS Proxy: Włącz proxy DNS, aby kierować żądania DNS z urządzeń przez określony serwer DNS, zapewniając dodatkową warstwę kontroli nad ruchem DNS.

    Ustawienia te pozwalają zoptymalizować wydajność i bezpieczeństwo DNS w sieci zgodnie z własnymi potrzebami.

    Przejdź do poradnika [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Strona Network Mode pozwala skonfigurować router do pracy w różnych trybach, zapewniając elastyczność w zależności od potrzeb sieciowych. Dostępne tryby obejmują:

    * Router: Działa jako standardowy router, zarządzając ruchem między siecią lokalną a internetem oraz udostępniając funkcje takie jak NAT, zapora i DHCP.
    * Access Point: Działa jako punkt dostępowy, rozszerzając istniejącą sieć przewodową o łączność bezprzewodową bez routowania ruchu.
    * Extender: Działa jako wzmacniacz zasięgu, zwiększając sygnał istniejącej sieci bezprzewodowej, aby objąć większy obszar i wyeliminować martwe strefy.
    * WDS (Wireless Distribution System): Działa podobnie do Extender; wybierz WDS, jeśli główny router obsługuje tryb WDS.

    Przejdź do poradnika [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    Strona IPv6 umożliwia skonfigurowanie ustawień IPv6 w sieci, zapewniając obsługę najnowszego protokołu internetowego. Na tej stronie możesz włączyć IPv6 i wybrać jeden z czterech trybów dopasowanych do wymagań sieci:

    * Native: Uzyskaj adres IPv6 bezpośrednio od dostawcy internetu, co umożliwia prostą i wydajną natywną łączność IPv6.
    * Passthrough: Pozwól, aby ruch IPv6 przechodził przez router do urządzeń w sieci, skutecznie mostkując połączenie bez obsługi routingu IPv6 przez sam router.
    * NAT6: Korzystaj z translacji adresów sieciowych dla IPv6 (NAT6), aby tłumaczyć wewnętrzne i zewnętrzne adresy IPv6 podobnie jak NAT działa dla IPv4.
    * Static IPv6: Ręcznie skonfiguruj statyczny adres IPv6 routera, zapewniając stały adres dla stabilnej łączności i łatwiejszego zarządzania usługami sieciowymi.

    Ustawienia te pomagają wykorzystać zalety IPv6, w tym większą przestrzeń adresową, ulepszone funkcje bezpieczeństwa i lepszą wydajność.

    Przejdź do poradnika [IPv6](../../interface_guide/network_mode.md).

---

=== "MAC Address"

    Strona MAC Address umożliwia wyświetlanie i zarządzanie adresami MAC powiązanymi z routerem. Najważniejsze funkcje dostępne na tej stronie to:

    * Factory Default: Wyświetl domyślne adresy MAC dla trybów Ethernet i Repeater routera jako odniesienie do oryginalnych ustawień sprzętowych.
    * Clone: Sklonuj adres MAC określonego urządzenia klienckiego. Jest to szczególnie przydatne w sytuacjach, gdy dostęp do sieci jest ograniczony do wybranych urządzeń.
    * Manual: Ręcznie określ niestandardowy adres MAC dla routera. Dodatkowo możesz użyć przycisku Random, aby wygenerować losowy adres MAC, co zapewnia elastyczność i większą prywatność.

    Funkcje te pozwalają skutecznie zarządzać adresami MAC routera, zapewniając zgodność i elastyczność w różnych środowiskach sieciowych.

    Przejdź do poradnika [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera o funkcje, których może nie mieć, w tym AdGuard Home, zaszyfrowany DNS i VPN. 
    
    Przejdź do poradnika [How to set up Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    Strona IGMP Snooping umożliwia konfigurację ustawień optymalizujących zarządzanie ruchem multicast w sieci. IGMP Snooping nasłuchuje pakietów protokołu IGMP i wyodrębnia z nich informacje, tworząc i utrzymując tablice przekazywania multicast warstwy 2. Dzięki temu dane grup multicast są przekazywane wyłącznie do hostów, które dołączyły do danej grupy, co zapobiega kierowaniu niechcianego ruchu multicast do innych hostów.

    Ustawienia te pomagają zoptymalizować wydajność i efektywność sieci, szczególnie w środowiskach z dużym natężeniem ruchu multicast, takich jak strumieniowanie wideo lub gry online.

    Przejdź do poradnika [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Ustawienia systemowe

=== "Overview"

    Strona Przegląd zapewnia kompleksowy podgląd bieżącego stanu routera i wskaźników jego wydajności. Na tej stronie możesz zobaczyć:

    * CPU Average Load: Monitoruj średnie obciążenie CPU routera, aby ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Memory Usage: Sprawdź, jaka część pamięci routera jest używana, co pomaga w zarządzaniu zasobami.
    * Flash Usage: Zobacz wykorzystanie pamięci flash routera, aby upewnić się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * LED Control: Włączaj lub wyłączaj diody LED routera, dostosowując wizualne wskaźniki urządzenia.
    * System Info: Uzyskaj szczegółowe informacje o systemie routera, w tym wersję firmware, czas pracy i stan sieci.
    
    Funkcje te zapewniają niezbędny wgląd i kontrolę, pomagając skutecznie zarządzać pracą routera i ją monitorować.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Aktualizacja służy do aktualizacji firmware routera do najnowszej wersji, zapewniającej lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Online Upgrade: Automatycznie sprawdź i zainstaluj najnowszą wersję firmware bezpośrednio z serwera producenta, upraszczając proces aktualizacji.
    * Local Upgrade: Ręcznie prześlij plik firmware z komputera, aby zaktualizować router, zachowując kontrolę nad wersją i momentem aktualizacji.

    Opcje te pozwalają utrzymywać router w aktualnym stanie dzięki najnowszym usprawnieniom i poprawkom.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Zaplanowane zadania pozwala automatyzować funkcje routera zgodnie z wcześniej ustalonym harmonogramem, zwiększając wygodę i efektywność. Najważniejsze funkcje na tej stronie to:

    * LED Display Schedule: Ustaw harmonogram automatycznego włączania lub wyłączania diod LED routera, aby ograniczyć zanieczyszczenie światłem w określonych godzinach.
    * Schedule Reboot: Skonfiguruj automatyczne ponowne uruchamianie routera w określonych odstępach czasu, co pomaga utrzymać optymalną wydajność i stabilność.
    * 2.4GHz Wi-Fi Status Schedule: Ustaw harmonogram sterowania pasmem Wi-Fi 2.4GHz, aby lepiej zarządzać dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramu zapewniają większą kontrolę nad działaniem routera i pomagają dostosować je do własnych potrzeb.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    Strona Hasło administratora umożliwia ustawienie lub zmianę hasła do interfejsu administracyjnego routera, dzięki czemu tylko upoważnieni użytkownicy mogą uzyskiwać dostęp do ustawień routera i je modyfikować. Hasło to ma kluczowe znaczenie dla zachowania bezpieczeństwa i integralności sieci, chroniąc przed nieautoryzowanym dostępem i zmianami konfiguracji.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    Strona Strefa czasowa umożliwia ustawienie właściwej strefy czasowej routera, dzięki czemu wszystkie zaplanowane zadania, dzienniki i zdarzenia systemowe będą oznaczane zgodnie z czasem lokalnym. Ustawienie to ma kluczowe znaczenie dla prowadzenia dokładnych rejestrów i prawidłowego wykonywania konfiguracji zależnych od czasu.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Strona Ustawienia przełącznika umożliwia skonfigurowanie fizycznego przełącznika routera, przypisując do niego określone funkcje zapewniające szybki dostęp i wygodne sterowanie. Funkcja ta udostępnia praktyczne skróty do typowych zadań i ustawień, poprawiając komfort użytkowania i upraszczając zarządzanie routerem.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    Strona Dziennik zapewnia dostęp do różnych dzienników rejestrujących działania i zdarzenia routera, co pomaga w rozwiązywaniu problemów i monitorowaniu wydajności. Ta strona obejmuje:

    * System Log: Szczegółowe dzienniki zdarzeń i działań na poziomie systemu.
    * Kernel Log: Dzienniki związane z działaniem i zdarzeniami jądra.
    * Crash Log: Rejestry awarii i błędów systemu przydatne przy diagnozowaniu krytycznych problemów.
    * Cloud Log: Dzienniki interakcji i działań związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: Dzienniki serwera WWW Nginx, jeśli jest używany przez router, opisujące ruch WWW i operacje serwera.
    
    Dodatkowo strona zawiera przycisk Export Log, który umożliwia wyeksportowanie wszystkich zebranych dzienników do analizy przez wsparcie techniczne. Funkcja ta jest niezwykle przydatna przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    Strona Przywracanie firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Proces ten przywraca router do domyślnych ustawień aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub gdy chcesz zacząć od nowa z domyślną konfiguracją bieżącego firmware.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Ustawienia zaawansowane zapewnia dostęp do zaawansowanych opcji konfiguracji przez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowanie ustawień i funkcji routera poza podstawowymi opcjami interfejsu. Obejmuje to szczegółowe konfiguracje sieci, ustawienia zapory i inne zaawansowane dostosowania systemu.

    Aby uzyskać szczegółowe instrukcje konfiguracji, zapoznaj się z [Advanced Settings](../../interface_guide/advanced_settings.md).
