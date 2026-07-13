# Nie można połączyć się z maskowanym serwerem WireGuard

Maskowanie VPN to technika, która sprawia, że ruch VPN wygląda jak zwykły ruch internetowy. Obecnie niektóre routery GL.iNet obsługują protokół AmneziaWG, co pozwala skonfigurować serwer WireGuard z włączonym maskowaniem ruchu.

Jeśli nie możesz nawiązać połączenia z maskowanym serwerem WireGuard, wykonaj poniższe kroki rozwiązywania problemów.

1. **Upewnij się, że konfiguracja WireGuard zaimportowana do każdego klienta jest dedykowana.**

    Każdy klient wymaga osobnego pliku konfiguracji peer. Udostępnienie jednej konfiguracji wielu klientom spowoduje błędy połączenia.

    W razie potrzeby przejdź do **VPN** -> **WireGuard Server** -> **Profiles**, aby wyświetlić wyeksportowane profile.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Upewnij się, że klient może zweryfikować parametry maskowania.**

    Protokół AmneziaWG jest zgodny wstecz. Jeśli serwer WireGuard obsługuje tylko AmneziaWG v1.0, plik konfiguracji nadal przejdzie weryfikację po zaimportowaniu do klienta obsługującego v2.0.
        
    Jeśli jednak plik konfiguracji zawiera parametry maskowania AmneziaWG v2.0, upewnij się, że klient WireGuard obsługuje AmneziaWG v2.0. W przeciwnym razie weryfikacja parametrów może się nie powieść.

    !!! tip "Jak rozpoznać wersję AmneziaWG?"

        **V1.0**: Brak parametrów S3-S4; H1-H4 to pojedyncze stałe liczby całkowite.
        
        **V2.0**: Jest to V2.0, jeśli spełniony jest dowolny z poniższych warunków:
        
        - Zawiera parametry S3-S4
        - H1-H4 są ustawione jako zakresy liczbowe
        - Zawiera niestandardowe parametry I1-I5.
        
        > Uwaga: I1-I5 nie są generowane automatycznie. Użytkownicy mogą ręcznie dodać je jako dodatkowe linie w pliku konfiguracji, aby ruch AmneziaWG wyglądał jak inne popularne protokoły, takie jak QUIC lub WebRTC.

    Jeśli klient WireGuard jest routerem GL.iNet, sprawdź jego wersję AmneziaWG na dwa sposoby.

    ??? note "Sprawdzenie przez Router Web Admin Panel"

        1. Zaloguj się do Web Admin Panel routera.

        2. Przejdź do **VPN** -> **WireGuard Server** -> **Configuration** i sprawdź parametry maskowania. Jeśli konfiguracja zawiera **S3-S4** oraz **H1-H4** jako zakresy zmienne zamiast stałych wartości, router działa z AmneziaWG 2.0, jak pokazano poniżej.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            W przeciwnym razie używa AmneziaWG 1.0, jak pokazano poniżej.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Sprawdzenie poleceniem SSH"

        1. Zaloguj się do routera przez SSH.

        2. Uruchom `opkg list|grep awg` i sprawdź sufiks pakietu **kmod-amneziawg** w wyniku polecenia. Jeśli jest oznaczony jako **2.0**, router obsługuje AmneziaWG 2.0, jak pokazano poniżej.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            W przeciwnym razie działa z AmneziaWG 1.0, jak pokazano poniżej.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Dostosuj parametry maskowania.**

    Jeśli ręcznie skonfigurowano [parametry maskowania](amneziawg_obfuscation.md#parameter-overview), takie jak Jc, Jmin lub Jmax, na serwerze WireGuard, błędne ustawienia mogą powodować niepowodzenie handshake.

    Spróbuj zmienić te parametry maskowania i połączyć się ponownie, aby wykluczyć niezgodność parametrów. Do testów możesz też przywrócić domyślne ustawienia maskowania.

4. **Przetestuj połączenie w oficjalnej aplikacji AmneziaWG.**

    Wykonaj test porównawczy: zainstaluj oficjalną aplikację AmneziaWG, zaimportuj oryginalny plik konfiguracji wyeksportowany z serwera i spróbuj się połączyć.

    - Jeśli połączenie w oficjalnej aplikacji działa, plik konfiguracji jest poprawny. Problem może dotyczyć pierwotnego urządzenia klienckiego. Sprawdź jego łączność sieciową lub skontaktuj się z pomocą techniczną.

    - Jeśli połączenie nadal się nie udaje, problem pochodzi z konfiguracji serwera na routerze. Sprawdź ustawienia serwera i parametry maskowania.

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
