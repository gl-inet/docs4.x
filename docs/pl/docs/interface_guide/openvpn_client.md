# Konfiguracja klienta OpenVPN na routerach GL.iNet

OpenVPN to otwartoźródłowy protokół VPN, który wykorzystuje techniki wirtualnych sieci prywatnych do ustanawiania bezpiecznych połączeń site-to-site lub punkt-punkt.

Aby skonfigurować klienta OpenVPN na routerze GL.iNet, obejrzyj poniższy film lub wykonaj opisane kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Przed rozpoczęciem upewnij się, że masz aktywną subskrypcję u dostawcy usług VPN obsługującego ręczną konfigurację OpenVPN. Kliknij [tutaj](https://www.gl-inet.com/solutions/vpn/){target="_blank"}, aby sprawdzić dostawców OpenVPN kompatybilnych z GL.iNet.

Zazwyczaj musisz najpierw odwiedzić oficjalną stronę subskrybowanego dostawcy usług VPN, uzyskać plik konfiguracyjny i przesłać go do routera, aby skonfigurować go jako klienta OpenVPN. Jeśli nie wiesz, jak uzyskać plik konfiguracyjny, skorzystaj z [poniższego łącza](#get-configuration-files-from-openvpn-service-providers) lub skontaktuj się z pomocą techniczną dostawcy.

Klienta OpenVPN możesz skonfigurować za pomocą panelu administratora lub [aplikacji mobilnej](../faq/mobile_app.md). Poniżej przedstawiono kroki konfiguracji za pomocą panelu administratora.

---

W panelu administratora przejdź do **VPN** -> **OpenVPN Client**.

Jeśli masz subskrypcję NordVPN, kliknij **NordVPN**, aby się zalogować; w przeciwnym razie kliknij **Add Manually**, aby przesłać pliki konfiguracyjne OpenVPN.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Konfiguracja NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} to popularny serwis VPN ceniony za prędkość i bezpieczeństwo.

Szybka konfiguracja NordVPN jest zintegrowana z panelem administracyjnym routerów GL.iNet. Pliki konfiguracyjne dla wszystkich serwerów NordVPN możesz pobrać online, wprowadzając dane logowania konta (uzyskane z panelu NordVPN) w panelu administratora routera lub aplikacji mobilnej, bez konieczności ręcznego przesyłania plików.

1. Zaloguj się do swojego konta NordVPN [tutaj](https://my.nordaccount.com/){target="_blank"}.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

    Po zalogowaniu, na panelu Nord, kliknij **NordVPN**, a następnie kliknij **Set up NordVPN manually**.

    ![nord dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Znajdziesz tam **dane logowania do usługi**. Skopiuj je do późniejszego użycia.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Zaloguj się do panelu administratora routera, przejdź do VPN -> OpenVPN Client -> NordVPN. Wprowadź **dane logowania do usługi** uzyskane w kroku 1 (uwaga: to **NIE** są dane logowania do konta e-mail/hasło), a następnie kliknij **Save and Continue**.
   
    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Wybierz protokół, maksymalną liczbę serwerów dla każdej lokalizacji i lokalizacje, a następnie kliknij **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

    Pliki konfiguracyjne zostaną pobrane.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Nawiąż połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby nawiązać połączenie.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Szczegóły połączenia VPN zostaną wyświetlone na **VPN Dashboard**.

    ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. Aktualizuj serwery.

    Możesz kliknąć **Update Servers**, aby uzyskać najnowszą listę dostępnych serwerów i uniknąć błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Edytuj dane logowania.

    Kliknij ikonę koła zębatego, aby edytować dane logowania.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Usuń wszystkie pliki.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Ręczna konfiguracja klienta OpenVPN (dla innych dostawców)

Jeśli Twój dostawca usług OpenVPN nie jest zintegrowany z naszym panelem administracyjnym, odwiedź najpierw oficjalną stronę subskrybowanego dostawcy, aby uzyskać plik konfiguracyjny. Następnie prześlij go do routera, aby skonfigurować klienta OpenVPN.

W poniższych krokach jako przykładu używamy [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}.

1. Pobierz plik konfiguracyjny z oficjalnej strony Private Internet Access.

2. Zaloguj się do panelu administratora routera, przejdź do VPN -> OpenVPN Client i kliknij **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. Na lewym pasku bocznym zostanie utworzona grupa.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. Nadaj grupie opisową nazwę (np. private internet access).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. Prześlij plik konfiguracyjny OpenVPN. Jeśli wymagane są dane uwierzytelniające, wprowadź je, a następnie kliknij **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}

    - Dostępne są 4 typy danych uwierzytelniających:

        1. Bez uwierzytelniania.
        
        2. Tylko nazwa użytkownika i hasło.
        
        3. Tylko hasło (Passphrase).

        4. Nazwa użytkownika, hasło i Passphrase.

    Plik konfiguracyjny zostanie wyświetlony po przesłaniu.
     
    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. Kliknij ikonę trzech kropek po prawej stronie, aby nawiązać połączenie.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

    Szczegóły połączenia VPN zostaną wyświetlone na **VPN Dashboard**.

    ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## Konfiguracja serwera OpenVPN na routerze GL.iNet

Jeśli masz dwa routery GL.iNet, możesz skonfigurować jeden jako serwer OpenVPN (wymagany publiczny adres IP), a drugi jako klienta OpenVPN. W ten sposób możesz nawiązać własne połączenie VPN bez subskrybowania zewnętrznych usług VPN.

Informacje na temat konfigurowania serwera OpenVPN znajdziesz [tutaj](openvpn_server.md).

## Pobieranie plików konfiguracyjnych od dostawców usług OpenVPN {#get-configuration-files-from-openvpn-service-providers}

Przetestowaliśmy ponad 30 dostawców usług OpenVPN i udokumentowaliśmy kroki uzyskiwania plików konfiguracyjnych. Jeśli nie wiesz, jak uzyskać plik konfiguracyjny, skorzystaj z poniższych instrukcji.

Jeśli subskrybowany dostawca nie znajduje się na poniższej liście, skontaktuj się z jego pomocą techniczną.

??? "NordVPN"
    ### NordVPN

    [Oficjalna strona](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Zaloguj się do konta NordVPN**

        Zaloguj się na [oficjalnej stronie](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}, przejdź do panelu Nord Account, gdzie znajdziesz dane logowania do usługi.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        Po zalogowaniu do panelu Nord kliknij NordVPN po lewej stronie, a następnie kliknij **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Znajdź **Service credentials**. Skopiuj je – będą potrzebne podczas przesyłania konfiguracji.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Wybierz serwer NordVPN i pobierz plik konfiguracyjny**

        Przejdź do zakładki **Server recommendation**. Zostanie zaproponowany serwer optymalny dla Twojej sieci wraz z dostępnymi protokołami do pobrania. Kliknij **Get setup configuration**, aby kontynuować.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        W oknie podręcznym wybierz protokół **OpenVPN** i pobierz konfigurację UDP lub TCP.

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Wszystkie konfiguracje serwerów możesz pobrać [tutaj](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

    [Link do instrukcji](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Możesz również użyć [aplikacji mobilnej](../faq/mobile_app.md) do konfiguracji NordVPN.

??? "AirVPN"
    ### AirVPN

    [Oficjalna strona](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Zaloguj się na swoje konto AirVPN.

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Wybierz Config Generator po lewej stronie, następnie wybierz Linux jako system operacyjny. Następnie wybierz preferowany serwer.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Zostanie wyświetlona strona pobierania pliku konfiguracyjnego.

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [Oficjalna strona](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Informacje zaczerpnięte z [oficjalnej instrukcji Astrill](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Wygeneruj i pobierz plik ZIP konfiguracji Astrill OpenVPN.

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Wpisz opis, np. OPENVPN_GUI.

    3. Kliknij przycisk **ADD to my certificates**.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Po dodaniu certyfikatu OpenVPN kliknij przycisk **Download**.

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [Oficjalna strona](https://www.bolehvpn.net/){target="_blank"}

    Zaloguj się do [panelu](https://users.bolehvpn.net/){target="_blank"}, pobierz pliki konfiguracyjne i wybierz format [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Po pobraniu rozpakuj pliki zip.

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

    [Link do instrukcji](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [Oficjalna strona](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    Pobierz bezpośrednio [tutaj](https://www.cactusvpn.com/downloads/){target="_blank"}.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [Oficjalna strona](https://cryptostorm.is/){target="_blank"}

    Pobierz bezpośrednio [tutaj](https://cryptostorm.is/configs/ecc/){target="_blank"}.

??? "CyberGhost"
    ### CyberGhost

    [Oficjalna strona](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Informacje zaczerpnięte z [oficjalnej instrukcji CyberGhost](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Zaloguj się do swojego konta online CyberGhost VPN.

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Wybierz "**VPN**" z menu po lewej stronie, następnie kliknij "**Configure Device**" i utwórz konfigurację serwera w opisany poniżej sposób:

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Utwórz konfigurację serwera zgodnie z poniższymi ustawieniami:

        * **Protocol** : **OpenVPN**
        * **Country** : Ponieważ połączenia z natywnym protokołem mogą używać tylko jednego serwera, musisz wybrać kraj, z którego chcesz surfować; CyberGhost automatycznie wybierze serwer w tym kraju.
        * **Server group** : Wybierz grupę serwerów i protokół OpenVPN (UDP lub TCP).

        **OpenVPN UDP** zapewnia wyższą prędkość niż wersja TCP, ale w niektórych przypadkach może powodować przerwy w pobieraniu. Jest to ustawienie domyślne.
        
        **OpenVPN TCP** zapewnia bardziej stabilne połączenia niż wersja UDP, ale jest nieco wolniejszy. Wybierz tę wersję, jeśli masz powtarzające się problemy z połączeniem, takie jak nagłe rozłączenia.

        Po wybraniu żądanych parametrów zapisz je klikając **Save Configuration**.

    4. Aby wyświetlić wygenerowane dane logowania **OpenVPN** na panelu konfiguracyjnym, kliknij **View Configuration**.

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Po skonfigurowaniu preferencji połączenia zanotuj następujące informacje:

        * **Server Group** : Adres kraju (serwera), z którym chcesz się połączyć, np. „12345-1-ca.cg-dialup.net". Adres zmienia się w zależności od wybranego kraju. Konkretny serwer zostanie automatycznie wybrany przez CyberGhost.
        * **Username** : Nazwa użytkownika wygenerowana wyłącznie dla tego protokołu. To NIE jest regularna nazwa użytkownika konta CyberGhost – służy tylko do uwierzytelniania na serwerach CyberGhost przez konfiguracje ręczne. Będzie potrzebna podczas konfigurowania OpenVPN na routerach GL.iNet.
        * **Password** : Hasło wygenerowane wyłącznie do użytku z protokołem. To NIE jest regularne hasło konta CyberGhost – służy tylko do uwierzytelniania na serwerach CyberGhost przez konfiguracje ręczne. Będzie potrzebne podczas konfigurowania OpenVPN na routerach GL.iNet.

        Po zakończeniu pobierz plik konfiguracyjny, klikając *Download Configuration*.

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN

    [Oficjalna strona](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    Informacje zaczerpnięte z [oficjalnej instrukcji ExpressVPN](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Przejdź na stronę [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} i zaloguj się za pomocą danych logowania ExpressVPN.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Wprowadź kod weryfikacyjny** przesłany na Twój adres e-mail.

    2. W sekcji „Set up your devices" kliknij **More**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3.  Kliknij **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4.  Zobaczysz swój **username**, **password** i listę **plików konfiguracyjnych OpenVPN**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Kliknij wybrane lokalizacje, aby pobrać pliki .ovpn.

        **Pozostaw to okno przeglądarki otwarte**. Informacje te będą potrzebne podczas konfiguracji.

    [Link do instrukcji](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN

    [Oficjalna strona](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Pobierz folder zip z plikami konfiguracyjnymi FastestVPN dla OpenVPN TCP i UDP [tutaj](https://support.fastestvpn.com/download/fastestvpn_ovpn/).

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, usuń część plików .ovpn z archiwum lub prześlij pojedynczy plik .ovpn.

    [Link do instrukcji](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [Oficjalna strona](https://www.finchvpn.com/){target="_blank"}

    1. Zaloguj się na swoje konto FinchVPN.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Przejdź na stronę Download i kliknij Download w sekcji FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Wybierz Linux.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Wybierz protokół zgodnie z preferencjami. Zazwyczaj możesz wybrać pierwszą opcję **Port 8484 over UDP**.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Przed pobraniem pliku zaznacz pole, aby dołączyć nazwę użytkownika i hasło.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [Oficjalna strona](https://www.hideipvpn.com/){target="_blank"}

    1. Zaloguj się na swoje konto HideIPVPN.

    2. Przejdź do sekcji Package po lewej stronie, kliknij swój pakiet i upewnij się, że jest aktywny.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. Na karcie VPN znajdziesz dane logowania VPN (nazwa użytkownika i hasło) używane podczas połączenia OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Przewiń w dół, aby pobrać pliki konfiguracyjne OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [Oficjalna strona](https://hide.me/?friend=glinet){target="_blank"}

    1. Zaloguj się na swoje konto Hide.me i znajdź Server Locations po lewej stronie.

    2. Pobierz konfigurację OpenVPN dla systemu Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [Oficjalna strona](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Uwaga: Pliki konfiguracyjne routera Hotspot Shield nie są już dostępne ani obsługiwane. Poniższe kroki zachowano wyłącznie dla użytkowników, którzy nadal mają zainstalowane te pliki.**

    1. Przejdź na stronę [https://www.hotspotshield.com/](https://www.hotspotshield.com/) i kliknij Account. Zaloguj się, jeśli zostaniesz o to poproszony.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Przejdź na stronę [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router).

        W menu Select location wybierz lokalizację wirtualną, której będzie używał router. Następnie kliknij "Download file". Plik konfiguracyjny (config.ovpn) zostanie pobrany na Twój komputer. Nazwa użytkownika i hasło będą potrzebne podczas konfigurowania klienta OpenVPN na routerze.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Link do instrukcji](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [Oficjalna strona](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Możesz pobrać wszystkie pliki konfiguracyjne dla wszystkich serwerów [tutaj](https://configs.ipvanish.com/configs/configs.zip); archiwum zawiera wszystkie pliki konfiguracyjne serwerów (.ovpn) oraz plik certyfikatu (.crt). Plik .zip może być duży dla niektórych modeli – usuń pliki konfiguracyjne (.ovpn) serwerów, których nie będziesz używać.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Możesz też pobrać pliki konfiguracyjne poszczególnych serwerów [tutaj](https://www.ipvanish.com/software/configs/), ale będziesz musiał również pobrać plik **ca.ipvanish.com.crt**. Przed przesłaniem do routera skompresuj plik **ca.ipvanish.com.crt** i plik .ovpn do archiwum .zip.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Link do instrukcji](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [Oficjalna strona](https://billing.ivacy.com/page/22852){target="_blank"}

    Aby skonfigurować klienta OpenVPN za pomocą Ivacy, potrzebne będą:

    - Twoja nazwa użytkownika do ręcznej konfiguracji OpenVPN, wyświetlana w oknie „Download Configuration".
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Twoje hasło (to samo, które używasz do logowania do konta Ivacy).
    - Plik konfiguracyjny OpenVPN.

    [Link do instrukcji](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [Oficjalna strona](https://www.ivpn.net/){target="_blank"}

    1. Pobierz [pliki konfiguracyjne OpenVPN](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Znajdź ID konta w [obszarze klienta IVPN](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Podczas przeciągania pliku konfiguracyjnego do Add a New OpenVPN Configuration zostaniesz poproszony o podanie nazwy użytkownika i hasła. Nazwa użytkownika to Twój Account ID zaczynający się od liter **ivpn**. Hasłem może być cokolwiek, np. **ivpn**.

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Link do instrukcji](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad"
    ### Mullvad

    [Oficjalna strona](https://mullvad.net/en){target="_blank"}

    1. Przejdź na stronę [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"} i zaloguj się za pomocą danych logowania Mullvad.

    2. Wybierz konfigurację OpenVPN.

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. Wybierz **Linux** i wybierz lokalizację serwera.

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [Oficjalna strona](https://www.ovpn.com/en?ref=glinet){target="_blank"}
    
    Po zalogowaniu możesz łatwo uzyskać pliki konfiguracyjne OpenVPN, klikając poniższe menu.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Wybierz serwer i pobierz plik.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    Nazwa użytkownika i hasło są takie same jak te używane do logowania do OVPN.

??? "OysterVPN"
    ### OysterVPN

    [Oficjalna strona](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Przejdź na [stronę z listą serwerów OysterVPN](https://support.oystervpn.com/server-list/){target="_blank"}, kliknij **Download .ovpn file**, aby pobrać plik konfiguracyjny.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. Nazwa użytkownika i hasło do połączenia OpenVPN są takie same jak te używane do logowania do OysterVPN.

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

??? "PIA (Private Internet Access)"
    ### PIA

    [Oficjalna strona](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Pobierz bezpośrednio [tutaj](https://www.privateinternetaccess.com/openvpn/openvpn.zip).

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Oficjalna strona](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Po zalogowaniu możesz łatwo znaleźć opcję **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

??? "PrivateVPN"
    ### PrivateVPN

    [Oficjalna strona](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    Pobierz bezpośrednio [tutaj](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank}.

    [Tutaj](https://privatevpn.com/client/PrivateVPN-TUN.zip) znajduje się oficjalny link do pobrania. Ze względu na błąd napotkany podczas importowania do routera (nazwa pliku zawiera znaki specjalne „Bogotá"), zmieniliśmy nazwę i udostępniamy powyższy link. Błąd ten zostanie naprawiony w przyszłych wersjach.

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

??? "Proton VPN"
    ### Proton VPN

    [Oficjalna strona](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN obsługuje WireGuard – zalecamy skorzystanie z WireGuard, sprawdź [tutaj](wireguard_client.md#wireguard-providers)**.

    1. Zaloguj się na swoje konto [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}.

    2. Kliknij **Download** po lewej stronie.

    3. Wybierz platformę Router, protokół itd. i znajdź docelowy kraj, aby pobrać plik konfiguracyjny.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. Dane logowania do połączenia OpenVPN różnią się od tych używanych do logowania do panelu Proton. Znajdziesz je w sekcji **Account -> OpenVPN/IKEv2 username**.

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [Oficjalna strona](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Aby skonfigurować klienta OpenVPN za pomocą PureVPN, potrzebna będzie nazwa użytkownika i hasło OpenVPN oraz plik konfiguracyjny, które możesz znaleźć na swoim koncie PureVPN.
   
    1. [Zaloguj się do swojego konta PureVPN](https://my.purevpn.com/).
    2. Z lewego paska bocznego kliknij **Subscriptions**.
    3. Przewiń w dół, aby znaleźć swoją nazwę użytkownika i hasło OpenVPN.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. Z lewego paska bocznego kliknij **Manual Configuration**.
    5. Wybierz lokalizację VPN i kliknij **Download**, aby pobrać plik konfiguracyjny.

    [Link do instrukcji](https://support.purevpn.com/openvpn-files)

    Routery GL.iNet nie obsługują funkcji [dedykowanego adresu IP](https://www.purevpn.com/dedicated-ip){target="_blank"} PureVPN, ponieważ wymaga ona protokołu PPTP.

??? "SaferVPN"
    ### SaferVPN

    [Oficjalna strona](https://safervpn.com/?a_aid=563){target="_blank"}

    Kliknij [tutaj](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup), aby bezpośrednio pobrać pliki konfiguracyjne.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [Oficjalna strona](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN oferuje usługę VPN z protokołami OpenVPN i WireGuard. Zalecamy WireGuard, ponieważ jest zazwyczaj szybszy niż OpenVPN. Sprawdź [tutaj](wireguard_client.md#starvpn).

    Jeśli preferujesz protokół OpenVPN, wykonaj poniższe kroki, aby pobrać plik konfiguracyjny.

    1. **Zarejestruj konto StarVPN**

        Przejdź do ich [opcji cenowych](https://www.starvpn.com/#pricing){target="_blank"} i wybierz plan VPN odpowiedni dla Twoich potrzeb. Możesz zarejestrować się podczas realizacji zamówienia lub bezpośrednio [tutaj](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Pobierz konfigurację OpenVPN**

        Zaloguj się do obszaru członkowskiego StarVPN w [panelu](https://www.starvpn.com/dashboard){target="_blank"}. Na panelu znajdź sekcję **VPN Configuration** i kliknij **OpenVPN Config**. Skopiuj nazwę użytkownika i hasło OVPN – będą potrzebne do uwierzytelnienia podczas przesyłania pliku do routera GL.iNet.

        ![download starvpn ovpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/ovpnconfigdl.png){class="glboxshadow"}

        Wybierz UDP lub TCP i pobierz plik konfiguracyjny.

        ![select udp or tcp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/udp_tcp.png){class="glboxshadow"}

    3. **Edytuj plik konfiguracyjny**
    
        Niektóre routery GL.iNet nie obsługują IPv6. Aby uniknąć problemów ze zgodnością i łącznością, otwórz plik konfiguracyjny .ovpn i usuń treści związane z IPv6, jak pokazano poniżej.

        ![remove ipv6](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/remove_ipv6.png){class="glboxshadow"}
        
??? "StreamVPN"
    ### StreamVPN

    [Oficjalna strona](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Zaloguj się do swojego konta [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} – zobaczysz informacje o subskrypcji. Kliknij **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Kliknij **VPN Router** – zostanie pobrany plik archiwum .zip o nazwie `StreamVPN.zip`.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Uwaga:** Używaj wyłącznie pliku konfiguracyjnego, którego nazwa zawiera słowo „Primary".

??? "StrongVPN"
    ### StrongVPN

    [Oficjalna strona](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Zaloguj się do swojego konta [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} – zobaczysz podsumowanie kont VPN. Kliknij **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Znajdź sekcję Manual setup i wykonaj opisane kroki, aby uzyskać konfigurację.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark

    [Oficjalna strona](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Znajdź swoje dane logowania**

        Dane logowania do usługi Surfshark różnią się od danych konta Surfshark (adresu e-mail i hasła). Będziesz potrzebować danych logowania do usługi Surfshark, aby połączyć się z VPN za pomocą metody ręcznej konfiguracji OpenVPN w routerze.

        Zaloguj się na [oficjalnej stronie](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, przejdź na [tę stronę](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, gdzie znajdziesz wszystkie wymagane szczegóły do ręcznego połączenia.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Wybierz serwer Surfshark**

        Wybierz zakładkę **Locations**, gdzie zobaczysz wszystkie serwery Surfshark.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        Zostaniesz poproszony o wybór TCP lub UDP. Kliknij [tutaj](../faq/openvpn_tcp_udp.md), aby zobaczyć różnicę.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    Wszystkie konfiguracje możesz pobrać [tutaj](https://api.surfshark.com/v1/server/configurations) bezpośrednio.

    Wskazówka: jeśli plik zip jest zbyt duży do przesłania, możesz usunąć część plików .ovpn z archiwum lub przesłać pojedynczy plik .ovpn.

    [Link do instrukcji](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC

    [Oficjalna strona](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    Pobierz [tutaj](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [Oficjalna strona](https://www.vpngate.net/en/){target="_blank"}

    Pliki konfiguracyjne OpenVPN są wyświetlane na [stronie VPN Gate](https://www.vpngate.net/en/) według lokalizacji serwera.

    1. Kliknij plik konfiguracyjny OpenVPN w kolumnie **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Zostanie wyświetlona strona pobierania.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Oficjalna strona](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Informacje zaczerpnięte z [oficjalnej instrukcji VPN Unlimited](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Zaloguj się do User Office, kliknij Manage przy usłudze VPN Unlimited i wykonaj kilka prostych kroków:

    1. Wybierz urządzenie.

        Wybierz urządzenie z listy lub utwórz nowe. Jeśli nie masz wolnych slotów, usuń stare urządzenie lub kup dodatkowe sloty.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Wybierz żądaną lokalizację serwera.
    
        VPN Unlimited oferuje szeroki wybór serwerów – ponad 400 w ponad 70 lokalizacjach. W tym przykładzie wybierzemy Niemcy.

    3. Wybierz protokół VPN.

        Wybierz protokół OpenVPN.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Utwórz konfigurację.

        Kliknij Generate, a otrzymasz wszystkie dane potrzebne do skonfigurowania połączenia VPN.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPN udostępnia pliki OpenVPN tutaj: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    Dostarczony plik zip zawiera dwa foldery z plikami .ovpn: OpenVPN160 i OpenVPN256. Usuń folder OpenVPN160 z pliku zip, a następnie prześlij go do routera GL.iNet w zwykły sposób.

??? "Windscribe"
    ### Windscribe

    [Oficjalna strona](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Zaloguj się do swojego konta Windscribe [tutaj](https://windscribe.com/login?auth_required){target="_blank"}, a następnie przejdź do [generatora konfiguracji OpenVPN](https://windscribe.com/getconfig/openvpn){target="_blank"}.
    
    2. Wybierz lokalizację serwera, protokół (UDP/TCP), port (np. 1194) i wersję OpenVPN (najlepiej nowszą), a następnie kliknij **Download Config**. Na Twoje urządzenie zostanie pobrany plik z rozszerzeniem „.ovpn".

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Kliknij przycisk **Get Credentials** na tej samej stronie. Otrzymasz odpowiednie dane uwierzytelniające, które będą potrzebne w panelu administratora routera podczas przesyłania pliku konfiguracyjnego. Skopiuj je lub pozostaw otwartą tę stronę.

    4. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers), aby kontynuować.

??? "ZoogVPN"
    ### ZoogVPN

    [Oficjalna strona](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Zaloguj się na [oficjalnej stronie](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}, a następnie przejdź na [stronę plików konfiguracyjnych OpenVPN](https://app.zoogvpn.com/setup/configuration-files){target="_blank"} – znajdziesz tam wszystkie serwery. Pobierz plik konfiguracyjny z kolumny TCP lub UDP.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Następnie postępuj zgodnie z [przewodnikiem konfiguracji klienta OpenVPN na routerze GL.iNet](#setup-openvpn-client) – nazwa użytkownika i hasło są takie same jak te używane do logowania na stronie ZoogVPN.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.