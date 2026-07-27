# Instrukcja użytkownika Fortify (GL-MT6000)

## Przegląd produktu

Fortify (GL-MT6000) to router Wi-Fi 6 marki łączonej wydany wspólnie przez GL.iNet i ExpressVPN. Każde urządzenie zawiera bezpłatną roczną subskrypcję ExpressVPN. Użytkownicy mogą zrealizować subskrypcję i powiązać konto bezpośrednio w panelu administracyjnym WWW routera. Po aktywacji cały ruch przechodzący przez router korzysta z szybkiej sieci i silnego szyfrowania ExpressVPN, aby chronić całe połączenie sieciowe i prywatność online.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Konfiguracja Fortify

### 1. Włącz zasilanie

Złóż dwuczęściowy zasilacz. Podłącz go do routera Fortify i do gniazdka elektrycznego. Router uruchomi się automatycznie.

### 2. Podłącz urządzenie

Podłącz urządzenie, na przykład komputer, laptop lub smartfon, do routera przez Wi-Fi lub Ethernet.

- Ethernet

    Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

- Wi-Fi

    Na urządzeniu przejdź do Settings -> WLAN, znajdź nazwę sieci Wi-Fi routera na liście dostępnych sieci i wprowadź hasło. Domyślna nazwa sieci i hasło są wydrukowane na etykiecie routera.

### 3. Zaloguj się do panelu administracyjnego WWW

Otwórz przeglądarkę internetową, wpisz `192.168.8.1` w pasku adresu i zaloguj się. Wybierz język w prawym górnym rogu, ustaw hasło administratora i kliknij **Next**. Hasło musi mieć od 10 do 63 znaków i zawierać co najmniej dwa typy znaków: wielkie litery, małe litery, cyfry i symbole specjalne.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Skonfiguruj Wi-Fi. Jeśli zmienisz informacje Wi-Fi, musisz ponownie połączyć urządzenie z Wi-Fi routera, używając zaktualizowanych danych logowania.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Konfiguracja Internetu

**Note:** Poniższe instrukcje dotyczą konfiguracji routera przez panel administracyjny WWW GL.iNet. Jeśli wolisz użyć [aplikacji GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, pobierz ją i postępuj zgodnie z instrukcjami na ekranie.

Skonfiguruj Fortify jedną z obsługiwanych metod połączenia z Internetem: Ethernet, Repeater, Tethering lub Cellular. Jeśli chcesz używać [Multi-WAN](../../interface_guide/multi-wan.md), skonfiguruj więcej niż jedno połączenie z Internetem.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Podłącz kabel Ethernet między portem WAN routera Fortify a urządzeniem nadrzędnym, takim jak modem.

    Po pomyślnym połączeniu z Internetem dioda LED routera świeci stałym białym światłem.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. W panelu administracyjnym WWW przejdź do sekcji INTERNET -> Repeater i kliknij **Connect**.
    2. Wybierz sieć Wi-Fi z listy dostępnych sieci.
    3. Wprowadź hasło, a następnie kliknij **Apply**.

    Po pomyślnym połączeniu z Internetem dioda LED routera świeci stałym białym światłem.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Podłącz smartfon do portu USB routera za pomocą kabla USB.
    2. Na smartfonie przejdź do Settings i włącz USB Tethering. Na iPhonie zaufaj temu urządzeniu i włącz Personal Hotspot.
    3. W panelu administracyjnym WWW przejdź do sekcji INTERNET -> Tethering i kliknij **Connect**.

    Po pomyślnym połączeniu z Internetem dioda LED routera świeci stałym białym światłem.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Podłącz modem komórkowy USB do portu USB routera, aby udostępnić Internet z modemu USB wszystkim podłączonym urządzeniom.

    Po pomyślnym połączeniu z Internetem dioda LED routera świeci stałym białym światłem.

    Szczegółowe instrukcje znajdziesz w [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Poniżej znajduje się przegląd funkcji w panelu administracyjnym WWW Fortify.

## Wireless

Strona Wireless umożliwia konfigurację sieci Wi-Fi Fortify, w tym Main Network, Guest Network i IoT Network. Każda sieć obsługuje pasma 2,4 GHz i 5 GHz.

Aby skonfigurować Wireless, zobacz [Wireless](../../interface_guide/wireless_v4.9.md).

## Clients

Strona Clients pokazuje informacje o podłączonych urządzeniach, takie jak nazwa urządzenia, typ połączenia, adresy IP i MAC, prędkości pobierania i wysyłania oraz ruch. Umożliwia też blokowanie wybranych klientów jednym kliknięciem i wykonywanie innych działań.

Szczegóły znajdziesz w [Clients](../../interface_guide/clients.md).

## Usługi w chmurze

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zapewnia prosty sposób zdalnego dostępu i zarządzania routerami GL.iNet.

    Szczegóły znajdziesz w [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp służy do płynnej zdalnej pracy sieciowej na routerach GL.iNet. Wykorzystuje protokół AmneziaWG z wbudowaną obfuskacją ruchu, zapewniając stabilny i bezpieczny zdalny dostęp.

    Szczegóły znajdziesz w [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

VPN (virtual private network) tworzy bezpieczne, szyfrowane tunele ruchu między urządzeniem lokalnym a serwerem VPN. Zwiększa prywatność i bezpieczeństwo klienta VPN oraz umożliwia dostęp do zdalnej sieci serwera VPN.

Fortify integruje się z [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, umożliwiając aktywację połączenia ExpressVPN w kilka minut. Każde urządzenie Fortify zawiera bezpłatną roczną subskrypcję ExpressVPN, którą można zrealizować i powiązać z kontem w panelu administracyjnym WWW.

Aby zrealizować bezpłatną subskrypcję i skonfigurować tunel VPN, zobacz [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md).

Aby skonfigurować serwer OpenVPN, zobacz [OpenVPN Server](../../interface_guide/openvpn_server.md).

Aby skonfigurować serwer WireGuard, zobacz [WireGuard Server](../../interface_guide/wireguard_server.md).

## Sieć

=== "Multi-WAN"

    Multi-WAN umożliwia jednoczesne używanie wielu połączeń internetowych, takich jak cellular, repeater i ethernet. Jeśli bieżące połączenie przestanie działać, router automatycznie przełączy się na inne połączenie.

    Szczegóły znajdziesz w [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN to sieć lokalna, do której urządzenie dołącza po połączeniu z głównym Wi-Fi lub kablem Ethernet. Strona LAN obejmuje Basic Settings, DHCP Server Settings i Address Reservation.

    Szczegóły znajdziesz w [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Guest Network tworzy dedykowaną sieć Wi-Fi dla gości. Jest odizolowana od sieci głównej i pozwala ustawić podsieć gościnną w prywatnych zakresach IPv4, takich jak `192.168.0.0/16`, `172.16.0.0/12` lub `10.0.0.0/8`.

    Szczegóły znajdziesz w [Guest Network](../../interface_guide/guest_network.md).

=== "IoT Network"

    IoT Network umożliwia utworzenie dedykowanej sieci Wi-Fi dla urządzeń IoT, odizolowanej od sieci głównej w celu poprawy zgodności i bezpieczeństwa.

    Szczegóły znajdziesz w [IoT Network](../../interface_guide/iot_network.md).

<br>

=== "DNS"

    Ustawienia DNS kontrolują tłumaczenie nazw domen na adresy IP. Możesz używać serwerów DNS uzyskanych automatycznie, ustawić własne serwery i skonfigurować priorytety DNS.

    Szczegóły znajdziesz w [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Ethernet Port umożliwia zarządzanie rolami portów WAN/LAN i wyświetlanie szczegółów portów, takich jak adres MAC i wynegocjowana prędkość.

    Szczegóły znajdziesz w [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6 to najnowsza wersja protokołu internetowego, zapewniająca znacznie większą przestrzeń adresową niż IPv4.

    Szczegóły znajdziesz w [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP Snooping to technika optymalizacji sieci używana w przełącznikach Ethernet do zarządzania ruchem multicast.

    Szczegóły znajdziesz w [IGMP Snooping](../../interface_guide/igmp_snooping.md).

<br>

=== "Network Mode"

    Network Mode określa sposób, w jaki urządzenie łączy się z siecią i komunikuje z innymi urządzeniami.

    Konfigurację opisano w [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway rozszerza funkcje głównego routera o AdGuard Home, szyfrowany DNS i VPN.

    Konfigurację opisano w [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    Network Acceleration może zmniejszyć obciążenie CPU i przyspieszyć przekazywanie pakietów.

    Konfigurację opisano w [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) analizuje zawartość pakietów, aby dokładniej identyfikować aplikacje i strony internetowe na podstawie biblioteki sygnatur. Funkcja DPI GL.iNet integruje się z [Netify](https://www.netify.ai/){target="_blank"}.

    Szczegóły znajdziesz w [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics kategoryzuje i wizualizuje użycie sieci według aplikacji, pomagając monitorować ruch bieżący i historyczny.

    Szczegóły znajdziesz w [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter korzysta z klasyfikacji opartej na DPI, aby automatycznie blokować szkodliwe lub złośliwe strony internetowe.

    Szczegóły znajdziesz w [Content Filter](../../interface_guide/content_filter.md).

<br>

=== "QoS"

    QoS nadaje priorytet ważnym aktywnościom, takim jak rozmowy wideo lub gry, podczas przeciążenia sieci. Dotyczy to ruchu lokalnych klientów i ruchu tuneli VPN Client, ale nie ruchu odbieranego, gdy router działa jako VPN Server.

    Szczegóły znajdziesz w [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) zarządza ruchem sieciowym, aby zmniejszyć opóźnienia i bufferbloat.

    Szczegóły znajdziesz w [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control pomaga zarządzać urządzeniami dzieci, ograniczać czas korzystania z ekranu i blokować dostęp do określonych treści.

    Szczegóły znajdziesz w [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Bezpieczeństwo

=== "Port forwarding"

    Port forwarding pozwala zdalnym serwerom i urządzeniom w Internecie uzyskiwać dostęp do urządzeń w sieci prywatnej.

    Szczegóły znajdziesz w [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL (Access Control List) umożliwia tworzenie reguł zarządzających ruchem sieciowym według protokołów, adresów urządzeń i portów. Jeśli kilka reguł ACL jest sprzecznych, system stosuje regułę o wyższym priorytecie.

    Szczegóły znajdziesz w [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access obejmuje ustawienia zabezpieczeń chroniące sieć i router przed nieautoryzowanym dostępem, w tym Access Control, Remote Access Control oraz Open Ports on Router.

    Szczegóły znajdziesz w [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    NAT Mode pozwala włączyć lub wyłączyć Full Cone NAT oraz SIP ALG.

    Szczegóły znajdziesz w [NAT Mode](../../interface_guide/nat_settings.md).

## Aplikacje

=== "Plug-ins"

    Plug-in to komponent oprogramowania dodający określone funkcje do istniejącego programu lub systemu.

    Szczegóły znajdziesz w [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatycznie wykrywa i aktualizuje w czasie rzeczywistym adres IP powiązany z domeną.

    Szczegóły znajdziesz w [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage zapewnia scentralizowaną pamięć masową, do której wielu użytkowników i urządzeń może uzyskiwać dostęp oraz udostępniać pliki w sieci.

    Szczegóły znajdziesz w [Network Storage](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home blokuje reklamy i trackery w całej sieci, działając jako serwer DNS filtrujący niepożądane treści.

    Szczegóły znajdziesz w [AdGuard Home](../../interface_guide/adguardhome.md).

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} pomaga chronić cyfrowy świat dziecka. W ramach współpracy GL.iNet z Bark, Fortify (GL-MT6000) oferuje plan Bark Home bezpłatnie.

    Szczegóły znajdziesz w [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale umożliwia bezpieczny dostęp do własnych urządzeń i aplikacji z dowolnego miejsca. Fortify (GL-MT6000) może dołączyć do wirtualnej sieci Tailscale, umożliwiając zdalny dostęp do zasobów WAN i LAN.

    Szczegóły znajdziesz w [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier tworzy bezpieczne sieci wirtualne przez Internet, łącząc urządzenia tak, jakby znajdowały się w tej samej sieci lokalnej.

    Szczegóły znajdziesz w [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor to bezpłatne oprogramowanie open source do anonimowej komunikacji i bardziej prywatnego korzystania z Internetu.

    Szczegóły znajdziesz w [Tor](../../interface_guide/tor.md).

## System

=== "Overview"

    Overview pokazuje aktualny stan i parametry routera, w tym CPU Average Load, Memory Usage, LED Control, Flash Usage, Device Info oraz External Storage.

    Szczegóły znajdziesz w [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Admin Password umożliwia ustawienie lub zmianę hasła interfejsu administracyjnego routera.

    Szczegóły znajdziesz w [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Upgrade służy do aktualizacji firmware routera. Obejmuje Firmware Online Upgrade i Firmware Local Upgrade.

    Szczegóły znajdziesz w [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Scheduled Tasks automatyzuje funkcje routera według harmonogramu, w tym LED Display Schedule, Schedule Reboot oraz 5GHz / 2.4GHz Wi-Fi Status Schedule.

    Szczegóły znajdziesz w [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

<br>

=== "Time Zone"

    Time Zone ustawia prawidłową strefę czasową dla zadań zaplanowanych, dzienników i zdarzeń systemowych.

    Szczegóły znajdziesz w [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Reset Firmware przywraca bieżący firmware do ustawień domyślnych i usuwa konfiguracje niestandardowe.

    Szczegóły znajdziesz w [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Log zapewnia dostęp do System Log, Kernel Log, Crash Log, Cloud Log i Nginx Log. Przycisk Export Log eksportuje zebrane dzienniki do analizy przez pomoc techniczną.

    Szczegóły znajdziesz w [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Advanced Settings otwiera interfejs OpenWrt LuCI do konfiguracji zaawansowanej.

    Szczegóły znajdziesz w [Advanced Settings](../../interface_guide/advanced_settings.md).
