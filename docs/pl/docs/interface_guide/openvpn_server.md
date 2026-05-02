# Konfiguracja serwera OpenVPN na routerach GL.iNet

OpenVPN to otwartoźródłowy protokół VPN, który wykorzystuje techniki wirtualnej sieci prywatnej do tworzenia bezpiecznych połączeń site-to-site lub point-to-point.

Aby skonfigurować serwer OpenVPN na routerze GL.iNet, obejrzyj ten film lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Upewnij się, że masz publiczny adres IP {#make-sure-you-have-a-public-ip-address}

Kliknij [tutaj](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), aby sprawdzić, czy Twój dostawca Internetu przydziela Ci publiczny adres IP.

**Jeśli nie, router nie może zostać skonfigurowany jako serwer OpenVPN.**

Alternatywne metody:

1. Jeśli masz router główny, zaloguj się do niego i sprawdź, czy otrzymuje publiczny adres IP od dostawcy Internetu.
2. Poproś dostawcę Internetu o publiczny adres IP. Może to wiązać się z dodatkową opłatą.
3. Jeśli powyższe dwie metody nie działają (np. sieć znajduje się za CGNAT), możesz wypróbować nasze rozwiązanie SD-WAN [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Sprawdź, czy wymagane jest przekierowanie portów {#confirm-if-port-forwarding-is-required}

**Topologia sieci**

??? "GL.iNet jest routerem głównym"
    
    * Jeśli router GL.iNet jest routerem głównym w Twojej sieci, przekierowanie portów nie jest wymagane. Przejdź do [następnego kroku](#setup-openvpn-server).

??? " GL.iNet jest routerem podrzędnym"

    * Jeśli w sieci działa już router główny, a router GL.iNet jest skonfigurowany jako router dodatkowy, musisz skonfigurować [przekierowanie portów](../tutorials/how_to_set_up_port_forwarding.md) na routerze głównym.
    
    * Jeśli w sieci działa już router główny, a router GL.iNet znajduje się kilka poziomów niżej od routera głównego, skonfiguruj [przekierowanie portów](../tutorials/how_to_set_up_port_forwarding.md) na każdym poziomie pośrednim.

## Konfiguracja serwera OpenVPN {#setup-openvpn-server}

Zaloguj się do panelu administracyjnego i przejdź do **VPN** -> **OpenVPN Server**.

1. Kliknij **Generate Configuration** (tylko przy początkowej konfiguracji serwera VPN).

    ![ovpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_generate_config.png){class="glboxshadow"}

2. Zastosuj konfigurację.

    Domyślna konfiguracja sprawdza się w większości przypadków.
    
    Jeśli nie musisz jej modyfikować, kliknij na dole **Export Client Configuration** i przejdź do kroku 3.
    
    Jeśli zmodyfikowałeś konfigurację, kliknij **Apply** przed wyeksportowaniem konfiguracji klienta.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S lub Tun. Kliknij [tutaj](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md/#tap-s2s-vs-tun-mode), aby sprawdzić różnice.

    * **Protocol:** UDP lub TCP. Kliknij [tutaj](../faq/openvpn_tcp_udp.md), aby sprawdzić różnice.

    * **Authentication Mode:** Określa metodę uwierzytelniania używaną podczas łączenia klienta z serwerem. Dostępne są trzy opcje.

        - **Certificate Only**: Jeśli wybierzesz tę opcję, router automatycznie wygeneruje klucze certyfikatów serwera i klienta oraz osadzi je w pliku konfiguracyjnym klienta. Po przesłaniu konfiguracji do klienta nie są wymagane dodatkowe dane uwierzytelniające.

        - **Username/Password Only**: Jeśli wybierzesz tę opcję, router wygeneruje konfigurację klienta bez kluczy certyfikatów. Przed wyeksportowaniem konfiguracji klienta musisz najpierw dodać nazwę użytkownika i hasło na karcie Users. Podczas importowania konfiguracji do klienta trzeba będzie podać te dane uwierzytelniające.

        - **Username/Password and Certificate**: Jeśli wybierzesz tę opcję, przed wyeksportowaniem konfiguracji klienta musisz najpierw dodać nazwę użytkownika i hasło na karcie Users. Następnie router automatycznie wygeneruje klucze certyfikatów serwera i klienta oraz osadzi je w pliku konfiguracyjnym. Podczas importowania konfiguracji do klienta najpierw zostanie zweryfikowany klucz certyfikatu, a następnie nazwa użytkownika i hasło, co zapewnia dwuskładnikowe zabezpieczenie.
    
        Poniżej znajduje się przykład tworzenia użytkownika.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: W razie potrzeby możesz zmodyfikować dodatkowe ustawienia serwera.
    
        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Wyeksportuj konfigurację klienta.

    Kliknij **Export Client Configuration** na dole karty Configuration (lub najpierw zastosuj zmodyfikowaną konfigurację), a następnie pojawi się okno jak poniżej.

    ![openvpn export config](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_export_config.png){class="glboxshadow"}

    - Jeśli publiczny adres IP Twojej sieci często się zmienia, możesz włączyć [DDNS](ddns.md), aby używać domeny DDNS jako adresu serwera.

    - Od oprogramowania v4.8 możesz wskazać adres serwera, wybierając spośród publicznego adresu IP, domeny DDNS i bieżącego adresu WAN IP. Po zmianie adres serwera w pliku konfiguracyjnym zostanie jednocześnie zaktualizowany.
    
    Następnie kliknij **Download**, aby wyeksportować konfigurację.

4. Uruchom serwer OpenVPN.

    Kliknij przycisk **Start** w prawym górnym rogu strony OpenVPN Server, aby uruchomić serwer. Następnie przejdź do strony VPN Dashboard, aby sprawdzić jego stan i inne ustawienia.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Sprawdź, czy serwer OpenVPN działa prawidłowo

### Weryfikacja stanu serwera

Od oprogramowania v4.8 stan połączenia serwera możesz sprawdzić na stronie **OpenVPN Server**.

Jeśli są wyświetlane statystyki ruchu wysyłania i pobierania, oznacza to, że serwer OpenVPN działa.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

W przypadku oprogramowania v4.7 i starszego sprawdź stan połączenia serwera na stronie **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

### Weryfikacja adresu IP klienta

Aby potwierdzić poprawne połączenie z serwerem, zaimportuj wcześniej wyeksportowaną konfigurację OpenVPN do urządzenia w innej sieci (nie w tej samej sieci lokalnej co serwer). Następnie otwórz przeglądarkę, wyszukaj swój adres IP i lokalizację. Jeśli odpowiadają adresowi IP serwera VPN (zamiast adresowi IP dostawcy Internetu) i jego lokalizacji, połączenie VPN jest prawidłowe.

Najprostsza metoda to użycie smartfona z zainstalowaną oficjalną [aplikacją OpenVPN](https://openvpn.net/vpn-client/){target="_blank"}. Najpierw wyłącz Wi-Fi w smartfonie i połącz się z Internetem wyłącznie przez transmisję komórkową (4G/5G). Następnie otwórz aplikację OpenVPN, zaimportuj plik konfiguracyjny i nawiąż połączenie. Sprawdź, czy smartfon ma dostęp do Internetu i czy jego adres IP odpowiada adresowi IP serwera OpenVPN.

Podczas importowania pliku konfiguracyjnego do aplikacji OpenVPN może pojawić się komunikat jak poniżej. Kliknij **CONTINUE**, aby kontynuować, ponieważ certyfikat jest już osadzony w pliku konfiguracyjnym.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Jeśli połączenie się nie powiedzie, możliwych jest kilka typowych przyczyn:

* Dostawca Internetu nie przydziela Ci publicznego adresu IP. Sprawdź [tutaj](#make-sure-you-have-a-public-ip-address).
* Może być konieczne skonfigurowanie przekierowania portów. Sprawdź [tutaj](#confirm-if-port-forwarding-is-required).
* Port używany przez serwer OpenVPN jest blokowany przez dostawcę Internetu. Zmień go na inny lub skontaktuj się z dostawcą Internetu, aby uzyskać dalszą pomoc.
* W niektórych krajach lub regionach połączenia VPN mogą być blokowane.

## Dostęp klient-klient

**Topologia sieci**

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Włącz przełącznik **Client to Client** i wyeksportuj nową konfigurację do klientów, aby mogły się one teraz wzajemnie komunikować.

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## Instalacja aplikacji OpenVPN

Pobierz aplikację OpenVPN z [oficjalnej strony OpenVPN](https://openvpn.net/vpn-client/){target="_blank"}.

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
