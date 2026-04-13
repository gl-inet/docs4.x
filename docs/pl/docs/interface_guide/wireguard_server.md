# Konfiguracja serwera WireGuard na routerach GL.iNet

WireGuard® to wyjątkowo prosty, a zarazem szybki i nowoczesny VPN wykorzystujący najnowsze rozwiązania kryptograficzne. Został zaprojektowany tak, aby był szybszy, prostszy, lżejszy i bardziej użyteczny niż IPsec, a przy tym pozwalał uniknąć jego złożoności. Ma również zapewniać wyraźnie wyższą wydajność niż OpenVPN.

Aby skonfigurować serwer WireGuard na routerze GL.iNet, obejrzyj ten film lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Upewnij się, że masz publiczny adres IP {#make-sure-you-have-a-public-ip-address}

Kliknij [tutaj](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), aby sprawdzić, czy Twój dostawca Internetu przydziela Ci publiczny adres IP.

**Jeśli nie, router nie może zostać skonfigurowany jako serwer WireGuard.**

Alternatywne metody:

1. Jeśli masz router główny, zaloguj się do niego i sprawdź, czy otrzymuje publiczny adres IP od dostawcy Internetu.
2. Poproś dostawcę Internetu o publiczny adres IP. Może to wiązać się z dodatkową opłatą.
3. Jeśli powyższe dwie metody nie działają (np. sieć znajduje się za CGNAT), możesz wypróbować nasze rozwiązanie SD-WAN [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Sprawdź, czy wymagane jest przekierowanie portów {#confirm-if-port-forwarding-is-required}

**Topologia sieci**

??? "GL.iNet jest routerem głównym"
    
    * Jeśli router GL.iNet jest routerem głównym w Twojej sieci, przekierowanie portów nie jest wymagane. Przejdź do [następnego kroku](#set-up-wireguard-server).

??? " GL.iNet jest routerem podrzędnym"

    * Jeśli w sieci działa już router główny, a router GL.iNet jest skonfigurowany jako router dodatkowy, musisz skonfigurować [przekierowanie portów](../tutorials/how_to_set_up_port_forwarding.md) na routerze głównym.
    
    * Jeśli w sieci działa już router główny, a router GL.iNet znajduje się kilka poziomów niżej od routera głównego, skonfiguruj [przekierowanie portów](../tutorials/how_to_set_up_port_forwarding.md) na każdym poziomie pośrednim.

## Konfiguracja serwera WireGuard {#set-up-wireguard-server}

Zaloguj się do panelu administracyjnego i przejdź do **VPN** -> **WireGuard Server**.

1. Kliknij **Generate Configuration** (tylko przy początkowej konfiguracji serwera VPN).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Sprawdź konfigurację.

    Domyślna konfiguracja sprawdza się w większości przypadków, jak pokazano poniżej. Nie ma potrzeby zmieniać adresu IPv4, jeśli nie koliduje on z bramą routera nadrzędnego.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    (IPv6 w routerach GL.iNet jest domyślnie wyłączone. Jeśli chcesz używać adresu IPv6, najpierw włącz IPv6 na routerze.)
    
    Jeśli zauważysz, że adres IPv4 koliduje z bramą routera nadrzędnego, zmień go na inny, na przykład **10.1.0.1/24**, a następnie kliknij **Apply**. Upewnij się, że zapis CIDR „/24” jest zachowany, aby uniknąć problemów z łącznością.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Na przykład, jeśli nad routerem GL.iNet działa router Xfinity, jego adres IP może wynosić 10.0.0.1. Będzie to kolidować z adresem IP tunelu serwera WireGuard po skonfigurowaniu routera GL.iNet jako serwera WireGuard, dlatego trzeba wprowadzić powyższą zmianę.
    
    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Dodaj profil.

    Przejdź do karty **Profiles** i kliknij przycisk **Add**, aby wygenerować profil dla swojego urządzenia.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    Ustaw opisową nazwę i kliknij **Apply**, aby kontynuować.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}
    
    Jeśli chcesz ustawić opcje zaawansowane, kliknij **Set More**. Następnie kliknij **Apply**, aby kontynuować.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Dodaj reguły tras, jeśli to konieczne"

        W większości przypadków dodawanie reguł tras nie jest konieczne.
        
        Jeśli chcesz uzyskać z serwera dostęp do urządzeń LAN klienta WireGuard, przejdź do karty **Route Rules** na stronie **WireGuard Server** i skonfiguruj reguły tras. Kliknij [tutaj](../tutorials/wireguard_server_access_to_client_lan_side.md), aby uzyskać więcej instrukcji.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        W przeciwnym razie przejdź do kroku 4, aby pobrać konfigurację klienta.

4. Pobierz konfigurację.

    Po dodaniu profilu i kliknięciu **Apply** zostanie wygenerowany plik konfiguracyjny w trzech formatach: kod QR, zwykły tekst i plik .conf. Wybierz preferowaną metodę pobrania pliku konfiguracyjnego.

    - **Kod QR**: odpowiedni dla urządzeń końcowych (np. smartfona, tabletu, laptopa) z zainstalowaną aplikacją WireGuard. Jeśli chcesz skonfigurować dane urządzenie jako klienta WireGuard, po prostu otwórz aplikację WireGuard, zeskanuj kod QR, a konfiguracja zostanie zaimportowana automatycznie.
    
        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Zwykły tekst**: w tej formie możesz przejrzeć szczegóły konfiguracji i wygodnie skopiować je w inne miejsce do ręcznej konfiguracji, na przykład do aplikacji WireGuard lub routera GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **Plik .conf**: kliknij **Download**, aby zapisać plik .conf na urządzeniu lokalnym. To również wygodna forma, którą można bezpośrednio przesłać do aplikacji WireGuard lub routera GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    W razie potrzeby możesz wskazać adres serwera, wybierając spośród publicznego adresu IP, domeny DDNS i bieżącego adresu WAN IP. Funkcja ta jest dostępna od oprogramowania v4.8. Po zmianie adres serwera w pliku konfiguracyjnym zostanie jednocześnie zaktualizowany.
    
    Na przykład, jeśli publiczny adres IP Twojej sieci często się zmienia, zaleca się włączenie [DDNS](ddns.md) i używanie domeny DDNS jako adresu serwera.
    
    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Uruchom serwer WireGuard.

    Kliknij przycisk **Start** w prawym górnym rogu, aby uruchomić serwer WireGuard.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    Stan połączenia będzie wyświetlany na tej samej stronie.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Sprawdź, czy serwer WireGuard działa prawidłowo

### Weryfikacja stanu serwera

Od oprogramowania v4.8 stan połączenia serwera możesz sprawdzić na stronie **WireGuard Server**.

Jeśli są wyświetlane statystyki ruchu wysyłania i pobierania oraz lista połączonych urządzeń online, oznacza to, że serwer WireGuard działa i że są do niego podłączeni klienci WireGuard.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

Jeśli widzisz 0 ruchu i 0 klientów, oznacza to, że żaden klient WireGuard nie jest połączony.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

W przypadku oprogramowania v4.7 i starszego sprawdź stan połączenia serwera na stronie **VPN Dashboard**.

### Weryfikacja adresu IP klienta

Aby potwierdzić poprawne połączenie z serwerem, zaimportuj wcześniej wyeksportowaną konfigurację WireGuard do urządzenia w innej sieci (nie w tej samej sieci lokalnej co serwer). Następnie otwórz przeglądarkę, wyszukaj swój adres IP i lokalizację. Jeśli odpowiadają adresowi IP serwera VPN (zamiast adresowi IP dostawcy Internetu) i jego lokalizacji, połączenie VPN jest prawidłowe.

Najprostsza metoda to użycie smartfona z zainstalowaną oficjalną [aplikacją WireGuard](https://www.wireguard.com/install){target="_blank"}. Najpierw wyłącz Wi-Fi w smartfonie i połącz się z Internetem wyłącznie przez transmisję komórkową (4G/5G). Następnie otwórz aplikację WireGuard, zaimportuj plik konfiguracyjny i nawiąż połączenie. Sprawdź, czy smartfon ma dostęp do Internetu i czy jego adres IP odpowiada adresowi IP serwera WireGuard.

Jeśli połączenie się nie powiedzie, możliwych jest kilka typowych przyczyn:

* Dostawca Internetu nie przydziela Ci publicznego adresu IP. Sprawdź [tutaj](#make-sure-you-have-a-public-ip-address).
* Może być konieczne skonfigurowanie przekierowania portów. Sprawdź [tutaj](#confirm-if-port-forwarding-is-required).
* Port używany przez serwer WireGuard jest blokowany przez dostawcę Internetu. Zmień go na inny lub skontaktuj się z dostawcą Internetu, aby uzyskać dalszą pomoc.
* W niektórych krajach lub regionach połączenia VPN mogą być blokowane.

## Instalacja aplikacji WireGuard

Pobierz aplikację WireGuard z [oficjalnej strony WireGuard](https://www.wireguard.com/install){target="_blank"}.

---

WireGuard® jest zastrzeżonym znakiem towarowym Jasona A. Donenfelda.

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
