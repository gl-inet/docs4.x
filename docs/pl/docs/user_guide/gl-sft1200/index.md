# Przewodnik użytkownika Opal (GL-SFT1200)

## Przegląd produktu

Opal (GL-SFT1200) to kieszonkowy router podróżny obsługujący bezprzewodową prędkość transmisji 1200 Mb/s. Został zaprojektowany w kompaktowej formie do użytku przenośnego i może spełnić potrzeby bezprzewodowego dostępu do Internetu małych firm, małych mieszkań lub podróżujących służbowo.

![gl-sft1200 interface](https://static.gl-inet.com/docs/router/en/3/setup/gl-sft1200/first_time_setup/gl-sft1200.jpg){class="glboxshadow"}

## Zawartość opakowania

- 1 x Opal (GL-SFT1200)
- 1 x Instrukcja obsługi
- 1 x Kabel Ethernet
- 1 x Karta z podziękowaniem
- 1 x Karta gwarancyjna
- 1 x Zasilacz
- 1 x Adapter (zależnie od kraju dostawy)

![gl-sft1200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/first_time_setup/sft1200_unboxing.jpg){class="glboxshadow"}

## Jak skonfigurować Opal

Obejrzyj poniższy film instruktażowy lub postępuj zgodnie z poniższymi krokami.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(W tym filmie wykorzystano inny router GL.iNet do demonstracji konfiguracji, ale kroki są takie same dla Opal i innych modeli routerów.)</small>

### 1. Włączenie zasilania

Złóż dwuczęściowy zasilacz. Podłącz go do routera i włóż do gniazdka. Router uruchomi się automatycznie.

### 2. Podłączenie urządzenia

Podłącz urządzenie (np. komputer, laptop lub smartfon) do routera za pomocą Wi-Fi lub kabla Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Ustawienia -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. Domyślną nazwę sieci i hasło znajdziesz na etykiecie na spodzie routera.

### 3. Logowanie do panelu administracyjnego

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język i ustaw hasło administratora, a następnie kliknij **Apply**.

Pamiętaj, że jeśli zmienisz dane sieci Wi-Fi, konieczne będzie ponowne połączenie urządzenia z siecią Wi-Fi routera przy użyciu zaktualizowanych danych.

### 4. Konfiguracja Internetu

**Uwaga:** Poniższe instrukcje dotyczą użytkowników konfigurujących router za pomocą panelu administracyjnego GL.iNet. Jeśli wolisz korzystać z aplikacji GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/){target="_blank"} i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

Skonfiguruj router Opal za pomocą jednej z obsługiwanych metod połączenia: Ethernet, Repeater, Tethering i Cellular. Jeśli chcesz korzystać z funkcji [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie internetowe.

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera a urządzeniem nadrzędnym, takim jak modem.
    
    Po pomyślnym połączeniu z Internetem w sekcji Ethernet na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w artykule [Połączenie z Internetem przez kabel Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_repeater.png){class="glboxshadow"}

    1. Na stronie INTERNET panelu administracyjnego znajdź sekcję Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wprowadź hasło, a następnie kliknij **Apply**.
    
    Po pomyślnym połączeniu z Internetem w sekcji Repeater na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w artykule [Połączenie z Internetem przez istniejącą sieć Wi-Fi](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_tethering.png){class="glboxshadow"}

    1. Podłącz urządzenie mobilne (np. smartfon lub modem USB) do portu USB routera za pomocą kabla USB.
    2. Na urządzeniu mobilnym przejdź do Ustawień i włącz Tethering USB.
    3. Na stronie INTERNET panelu administracyjnego kliknij **Connect** w sekcji Tethering.
    
    Po pomyślnym połączeniu z Internetem w sekcji Tethering na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w artykule [Połączenie z Internetem przez tethering USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_cellular.png){class="glboxshadow"}

    Podłącz modem USB z obsługą sieci komórkowej do portu USB routera. Jest to przydatne do udostępniania Internetu z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem w sekcji Cellular na stronie INTERNET pojawi się zielona kropka.

    Szczegółowe instrukcje znajdziesz w artykule [Połączenie z Internetem przez sieć komórkową](../../interface_guide/internet_cellular.md).

## Jak skonfigurować VPN

VPN (wirtualna sieć prywatna) tworzy bezpieczny, zaszyfrowany ruch między Twoim urządzeniem a serwerem VPN. Zapewnia dodatkową warstwę prywatności i bezpieczeństwa (klient VPN) oraz umożliwia dostęp do sieci zdalnej (serwer VPN). Opal obsługuje OpenVPN, WireGuard i Tor*.

=== "OpenVPN" 
    
    Opal (i inne routery GL.iNet) obsługuje protokół OpenVPN, który zapewnia silne zabezpieczenia. Aby skonfigurować OpenVPN, postępuj zgodnie z poniższymi poradnikami:

    * [Jak skonfigurować klienta OpenVPN](../../interface_guide/openvpn_client.md)
    * [Jak skonfigurować serwer OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Opal (i inne routery GL.iNet) obsługuje protokół WireGuard, który zapewnia wysoką prędkość i wygodę użytkowania. Aby skonfigurować WireGuard, postępuj zgodnie z poniższymi poradnikami:

    * [Jak skonfigurować klienta WireGuard](../../interface_guide/wireguard_client.md)
    * [Jak skonfigurować serwer WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor (The Onion Router) to sieć zorientowana na prywatność, umożliwiająca anonimową komunikację w Internecie. Kieruje ruch internetowy przez serię serwerów obsługiwanych przez ochotników (węzłów), aby ukryć lokalizację i aktywność użytkownika, utrudniając śledzenie działań online.

    **Uwaga:** Opal nie obsługuje Tor natywnie, ale użytkownicy mogą zainstalować Tor ręcznie za pomocą wtyczki. Kliknij [tutaj](../../interface_guide/tor.md#manual-install), aby uzyskać szczegóły.

## Sieć bezprzewodowa i klienci

=== "Wireless"

    Strona Wireless umożliwia konfigurację ustawień sieci Wi-Fi 5 GHz i 2,4 GHz, w tym włączanie Wi-Fi, ustawianie mocy TX, określanie nazwy sieci Wi-Fi (SSID), włączanie losowego BSSID, wybór trybu zabezpieczeń Wi-Fi i hasła, konfigurację widoczności SSID, wybór trybu Wi-Fi, pasma i kanału.

    Aby skonfigurować sieć bezprzewodową, zapoznaj się z poradnikiem [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Strona Clients wyświetla informacje o podłączonych urządzeniach. Dla każdego klienta pokazuje nazwę, adresy IP i MAC, prędkości pobierania i wysyłania, całkowity ruch oraz umożliwia zablokowanie klienta lub wykonanie innych czynności.

    Aby zarządzać klientami, zapoznaj się z poradnikiem [Clients](../../interface_guide/clients.md).

## Usługi chmurowe

=== "GoodCloud"

    Usługa GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia łatwy i prosty sposób zdalnego dostępu do routerów GL.iNet i zarządzania nimi.
    
    Aby skonfigurować GoodCloud, zapoznaj się z poradnikiem [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp to zaawansowana platforma sieciowa zaprojektowana w celu zapewnienia bezproblemowego zdalnego łączenia sieci i zdalnego zarządzania urządzeniami. Zbudowana specjalnie do integracji z routerami GL.iNet, AstroWarp obsługuje kompleksowe zarządzanie urządzeniami w całych sieciach, umożliwiając kontrolę zarówno urządzeń nadrzędnych, jak i podrzędnych. Koncentrując się na zarządzaniu całą siecią i przyszłej obsłudze kontroli na poziomie sprzętowym, AstroWarp oferuje bardziej niezawodne rozwiązanie do zarządzania urządzeniami i utrzymywania bezpiecznych, stabilnych sieci.
    
    Aby skonfigurować AstroWarp, zapoznaj się z poradnikiem [AstroWarp](../../interface_guide/astrowarp.md).

    **Uwaga:** Przed skorzystaniem z tej funkcji zaktualizuj firmware routera do wersji 1.7 lub nowszej.

## Aplikacje

=== "Plug-ins"

    Wtyczka (plug-in) to komponent oprogramowania, który dodaje określone funkcje lub możliwości do istniejącego programu, umożliwiając jego dostosowanie i rozszerzenie.
    
    Aby skonfigurować wtyczki, zapoznaj się z poradnikiem [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje adres IP powiązany z domeną w czasie rzeczywistym. Jest szczególnie przydatny dla użytkowników, którzy potrzebują stałego adresu IP do zdalnego dostępu do sieci.
    
    Aby skonfigurować Dynamic DNS, zapoznaj się z poradnikiem [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Sieciowa pamięć masowa to scentralizowane rozwiązanie do przechowywania danych, które umożliwia wielu użytkownikom i urządzeniom dostęp do plików i ich udostępnianie przez sieć.
    
    Aby skonfigurować sieciową pamięć masową, zapoznaj się z poradnikiem [Network Storage](../../interface_guide/network_storage.md).

    **Uwaga:** Przed skorzystaniem z tej funkcji zaktualizuj firmware routera do wersji 1.7 lub nowszej.

## Ustawienia sieciowe

=== "Port Forwarding"

    Przekierowanie portów umożliwia zdalnym serwerom i urządzeniom w Internecie dostęp do urządzeń w sieci prywatnej.
    
    Aby skonfigurować przekierowanie portów, zapoznaj się z poradnikiem [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN to funkcja sieciowa, która pozwala skonfigurować router z wieloma połączeniami internetowymi (np. Cellular, Repeater i Ethernet) jednocześnie. Jeśli bieżące połączenie internetowe przestanie działać, router automatycznie przełączy się na inne połączenie. Zapewnia to płynny, nieprzerwany dostęp do Internetu.

    Aby skonfigurować Multi-WAN, zapoznaj się z poradnikiem [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN (Local Area Network) to sieć łącząca komputery i urządzenia w ograniczonym obszarze geograficznym, takim jak dom lub biuro. Umożliwia szybki transfer danych i współdzielenie zasobów, pozwalając urządzeniom na efektywną komunikację.
    
    Aby skonfigurować LAN, zapoznaj się z poradnikiem [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Pozwala ustawić podsieć w zakresach prywatnych adresów IPv4 192.168.0.0/16, 172.16.0.0/12 lub 10.0.0.0/8, określić adresy IP bramy i maski podsieci oraz skonfigurować ustawienia zabezpieczeń, takie jak izolacja AP dla sieci gościnnej.

    Aby skonfigurować sieć gościnną, zapoznaj się z poradnikiem [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Strona DNS umożliwia ustawianie niestandardowych serwerów DNS, włączanie ochrony przed atakami DNS rebinding i nadpisywanie ustawień DNS wszystkich klientów, zezwalanie na nadpisywanie DNS VPN przez niestandardowy DNS oraz konfigurację trybu ustawień serwera DNS na automatyczny lub ręczne określanie serwerów DNS z połączenia Ethernet.

    Aby skonfigurować DNS, zapoznaj się z poradnikiem [DNS](../../interface_guide/dns.md).

=== "Port Management"

    Strona Port Management jest dostępna w wersji firmware v4.7 i nowszych.

    Ta strona umożliwia konfigurację portów WAN i LAN, ustawianie interfejsu WAN/LAN na Ethernet, określanie trybu MAC i adresu MAC dla interfejsu WAN oraz wyświetlanie wynegocjowanej prędkości portu sieciowego.

    Aby zarządzać portami Ethernet, zapoznaj się z poradnikiem [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Tryb sieci odnosi się do ustawień konfiguracyjnych określających sposób, w jaki urządzenie łączy się z siecią i komunikuje z innymi urządzeniami.
    
    Aby skonfigurować tryb sieci, zapoznaj się z poradnikiem [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6 (Internet Protocol version 6) to najnowsza wersja protokołu internetowego, zaprojektowana jako następca IPv4. Zapewnia znacznie większą przestrzeń adresową, umożliwiając praktycznie nieograniczoną liczbę unikalnych adresów IP, co jest niezbędne w obliczu rosnącej liczby urządzeń podłączonych do Internetu.
    
    Aby skonfigurować IPv6, zapoznaj się z poradnikiem [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcjonalność głównego routera, w tym AdGuard Home, szyfrowany DNS i klienta VPN.
    
    Aby skonfigurować Drop-in Gateway, zapoznaj się z poradnikiem [Jak skonfigurować Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP snooping to technika optymalizacji sieci stosowana w przełącznikach Ethernet do zarządzania i kontroli ruchu multicastowego.
    
    Aby skonfigurować IGMP snooping, zapoznaj się z poradnikiem [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Akceleracja sieciowa pozwala zmniejszyć obciążenie procesora i przyspieszyć przekazywanie pakietów ruchu sieciowego.
    
    Aby skonfigurować akcelerację sieciową, zapoznaj się z poradnikiem [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    Strona NAT Settings umożliwia włączanie lub wyłączanie funkcji Full Cone NAT i SIP ALG (Application Layer Gateway).

    Aby skonfigurować ustawienia NAT, zapoznaj się z poradnikiem [NAT Settings](../../interface_guide/nat_settings.md).

## Ustawienia systemowe

=== "Overview"

    Strona Overview zawiera kompleksowy przegląd bieżącego stanu i wskaźników wydajności routera. Na tej stronie możesz sprawdzić:

    * Średnie obciążenie CPU: Monitoruj średnie obciążenie procesora routera, co pomaga ocenić wydajność i zidentyfikować potencjalne wąskie gardła.
    * Użycie pamięci: Sprawdź, ile pamięci routera jest wykorzystywane, co ułatwia zarządzanie zasobami.
    * Sterowanie LED: Włączaj i wyłączaj diody LED routera, umożliwiając dostosowanie wizualnych wskaźników urządzenia.
    * Użycie pamięci Flash: Sprawdź wykorzystanie pamięci flash routera, upewniając się, że jest wystarczająco dużo miejsca na firmware i dane konfiguracyjne.
    * Informacje o urządzeniu: Dostęp do szczegółowych informacji o systemie routera, w tym czasu pracy, nazwy hosta, modelu, architektury, wersji OpenWrt, wersji jądra, identyfikatora urządzenia, adresu MAC i numeru seryjnego.
    * Pamięć zewnętrzna: Sprawdź stan urządzeń pamięci zewnętrznej podłączonych do routera, takich jak dyski USB lub karty TF.
    
    Te funkcje zapewniają istotne informacje i narzędzia kontroli, pomagając efektywnie zarządzać routerem i monitorować jego pracę.

    Szczegółowe instrukcje znajdziesz w artykule [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Strona Upgrade służy do aktualizacji firmware routera do najnowszej wersji, zapewniając lepszą wydajność, bezpieczeństwo i nowe funkcje. Ta strona oferuje dwie opcje aktualizacji:

    * Aktualizacja firmware online: Automatyczne sprawdzanie i instalacja najnowszej wersji firmware bezpośrednio z serwera producenta, upraszczające proces aktualizacji.
    * Lokalna aktualizacja firmware: Ręczne przesłanie pliku firmware z komputera w celu aktualizacji routera, dające kontrolę nad wersją i czasem aktualizacji.

    Te opcje pozwalają utrzymywać router z najnowszymi ulepszeniami i poprawkami.

    Szczegółowe instrukcje znajdziesz w artykule [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Strona Scheduled Tasks umożliwia automatyzację różnych funkcji routera według ustalonego harmonogramu, zwiększając wygodę i efektywność. Główne funkcje na tej stronie to:

    * Harmonogram wyświetlania LED: Ustaw harmonogram automatycznego włączania i wyłączania diod LED routera, redukując zanieczyszczenie świetlne o określonych porach.
    * Zaplanowany restart: Skonfiguruj automatyczny restart routera w określonych odstępach czasu, pomagając utrzymać optymalną wydajność i stabilność.
    * Harmonogram stanu Wi-Fi: Ustaw harmonogram sterowania pasmem Wi-Fi 5 GHz / 2,4 GHz, umożliwiając lepsze zarządzanie dostępnością sieci i zużyciem energii.
    
    Te opcje harmonogramowania zapewniają większą kontrolę nad działaniem routera, pozwalając dostosować go do indywidualnych potrzeb i preferencji.

    Szczegółowe instrukcje znajdziesz w artykule [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Strona Time Zone umożliwia ustawienie prawidłowej strefy czasowej routera, zapewniając dokładne znaczniki czasu dla wszystkich zaplanowanych zadań, logów i zdarzeń systemowych zgodnie z czasem lokalnym. To ustawienie jest kluczowe dla prowadzenia precyzyjnych zapisów i prawidłowego wykonywania konfiguracji opartych na czasie.

    Szczegółowe instrukcje znajdziesz w artykule [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Strona Toggle Button Settings umożliwia konfigurację fizycznego przełącznika na routerze, pozwalając przypisać do niego określone funkcje zapewniające szybki dostęp i kontrolę. Ta funkcja zapewnia wygodne skróty do typowych zadań i ustawień, ułatwiając zarządzanie routerem.

    Szczegółowe instrukcje znajdziesz w artykule [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    Strona Log zapewnia dostęp do różnych logów rejestrujących aktywność i zdarzenia routera, pomagając w rozwiązywaniu problemów i monitorowaniu wydajności. Strona zawiera:

    * System Log: Szczegółowe logi zdarzeń i aktywności na poziomie systemu.
    * Kernel Log: Logi związane z operacjami i zdarzeniami jądra.
    * Crash Log: Zapisy awarii i błędów systemu, przydatne do diagnozowania krytycznych problemów.
    * Cloud Log: Logi interakcji i aktywności związanych z usługami GoodCloud zintegrowanymi z routerem.
    * Nginx Log: Logi z serwera WWW Nginx, jeśli jest używany przez router, zawierające szczegóły ruchu sieciowego i operacji serwera.
    
    Ponadto strona zawiera przycisk Export Log, umożliwiający eksport wszystkich zebranych logów do analizy przez wsparcie techniczne. Ta funkcja jest nieoceniona przy diagnozowaniu złożonych problemów i uzyskiwaniu profesjonalnej pomocy.

    Szczegółowe instrukcje znajdziesz w artykule [Log](../../interface_guide/log.md).

---

=== "Security"

    Strona Security umożliwia konfigurację różnych ustawień zabezpieczeń w celu ochrony sieci i routera przed nieautoryzowanym dostępem. Strona zawiera opcje:

    * Admin Password: Ustaw lub zmień hasło interfejsu administracyjnego routera, aby tylko upoważnieni użytkownicy mogli modyfikować ustawienia.
    * Local Access Control: Zarządzaj i ograniczaj dostęp do interfejsu routera z urządzeń podłączonych do sieci lokalnej.
    * Remote Access Control: Konfiguruj i ograniczaj dostęp do interfejsu routera z lokalizacji zdalnych przez Internet, zwiększając bezpieczeństwo przed zagrożeniami zewnętrznymi.
    * Open Ports on Router: Kontroluj, które porty są otwarte na routerze, ograniczając potencjalne luki w zabezpieczeniach i nieautoryzowany dostęp.

    Te ustawienia pomagają utrzymać bezpieczne środowisko sieciowe, chroniąc zarówno router, jak i podłączone urządzenia.

    Szczegółowe instrukcje znajdziesz w artykule [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Strona Reset Firmware umożliwia przywrócenie bieżącej wersji firmware routera do ustawień domyślnych, usuwając wszystkie niestandardowe konfiguracje. Ten proces przywróci router do domyślnych ustawień aktualnie zainstalowanej wersji firmware. Może to być przydatne przy rozwiązywaniu uporczywych problemów lub przy rozpoczynaniu od nowa z domyślną konfiguracją bieżącego firmware.

    Szczegółowe instrukcje znajdziesz w artykule [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Strona Advanced Settings zapewnia dostęp do zaawansowanych opcji konfiguracji poprzez interfejs OpenWrt LuCI, umożliwiając doświadczonym użytkownikom precyzyjne dostosowywanie ustawień i funkcji routera wykraczające poza podstawowe opcje interfejsu. Obejmuje to szczegółowe konfiguracje sieciowe, ustawienia zapory sieciowej i inne zaawansowane dostosowania systemu.

    Szczegółowe instrukcje znajdziesz w artykule [Advanced Settings](../../interface_guide/advanced_settings.md).