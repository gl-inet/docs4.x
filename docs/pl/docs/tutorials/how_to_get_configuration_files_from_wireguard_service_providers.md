# Jak pobrać pliki konfiguracyjne od dostawców usług WireGuard

??? "AzireVPN"
    ### AzireVPN

    [Oficjalna strona](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Przejdź na [oficjalną stronę AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} i zaloguj się, następnie otwórz [generator konfiguracji WireGuard](https://www.azirevpn.com/cfg/wireguard){target="_blank"}

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. W opcji IP wybierz **IPv4**, a następnie kliknij **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-azirevpn), aby kontynuować.

    4. Możesz również użyć [aplikacji mobilnej](../faq/mobile_app.md), aby skonfigurować AzireVPN.

??? "Hide.me VPN"
    ### Hide.me VPN

    [Oficjalna strona](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN oferuje prosty sposób korzystania z usługi WireGuard na routerze GL.iNet.

    1. Połącz się z routerem przez [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}.

    2. Skopiuj poniższy adres URL instalacyjny, wklej go do terminala i naciśnij Enter. (Kliknięcie prawym przyciskiem myszy wkleja treść.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. Rozpocznie się instalacja, po czym zostaniesz poproszony o podanie nazwy użytkownika i hasła. Podczas wpisywania lub wklejania hasła terminal nie wyświetla żadnych znaków — po wpisaniu naciśnij Enter.

    4. Po zakończeniu przejdź do panelu administracyjnego w przeglądarce. Zobaczysz, że utworzono grupę Hide.me VPN z gotowymi plikami konfiguracyjnymi. Połącz się tak samo jak z każdym innym plikiem konfiguracyjnym.

    **Uwaga:** Klucz w pliku konfiguracyjnym Hide.me VPN jest generowany na nowo przed każdym połączeniem i traci ważność po rozłączeniu. Skopiowanie tego pliku konfiguracyjnego na inne urządzenie nie umożliwi nawiązania połączenia.

    [Odnośnik](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [Oficjalna strona](https://mullvad.net/){target="_blank"}

    1. Przejdź na [oficjalną stronę Mullvad](https://mullvad.net/){target="_blank"} i zaloguj się, następnie otwórz [generator plików konfiguracyjnych WireGuard](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}

    2. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md/#set-up-mullvad), aby kontynuować.
    3. Możesz też użyć [aplikacji mobilnej](../faq/mobile_app.md), aby skonfigurować Mullvad.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [Oficjalna strona](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Nie można pobrać konfiguracji WireGuard z tej strony internetowej, dlatego użyj [aplikacji mobilnej](../faq/mobile_app.md), aby skonfigurować PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [Oficjalna strona](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Jeśli korzystasz z [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, zaloguj się, a następnie przejdź na [tę stronę](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, kliknij **Router** i wybierz **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. W następnym oknie wybierz **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Wybierz **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Gdy para kluczy zostanie wygenerowana, wybierz **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Na koniec wybierz lokalizację, którą chcesz skonfigurować, i kliknij przycisk **download** obok tej lokalizacji. Dzięki temu pobierzesz pliki konfiguracyjne.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-surfshark).

    [Link referencyjny](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [Oficjalna strona](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Jeśli korzystasz z [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, zaloguj się na ich stronie internetowej, przejdź do [Client Area](https://airvpn.org/client/){target="_blank"} i kliknij [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Na stronie Config Generator w sekcji Protocols wybierz WireGuard.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Wybierz serwer, przewiń stronę do końca i kliknij przycisk **Generate**. Spowoduje to pobranie pliku konfiguracyjnego.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Astrill"
    ### Astrill

    [Oficjalna strona](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Jeśli korzystasz z [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, zaloguj się, a następnie otwórz [tę stronę](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"}, aby wygenerować konfiguracje WireGuard.

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "IVPN"
    ### IVPN

    [Oficjalna strona](https://www.ivpn.net/){target="_blank"}

    Jeśli korzystasz z [IVPN](https://www.ivpn.net/){target="_blank"}, musisz wygenerować konfigurację WireGuard ręcznie. Postępuj zgodnie z przewodnikiem odpowiednim dla swojego systemu operacyjnego.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "NVPN"
    ### NVPN

    [Oficjalna strona](https://www.nvpn.net/){target="_blank"}

    Postępuj zgodnie z przewodnikiem [tutaj](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"}, aby utworzyć konfigurację.

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "OVPN"
    ### OVPN

    [Oficjalna strona](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Zaloguj się na [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} i znajdź poniższe menu, aby uzyskać pliki konfiguracyjne WireGuard.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Kliknij **Generate WireGuard keys**, wybierz serwer, którego chcesz użyć, a następnie pobierz konfigurację.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Otwórz konfigurację w edytorze tekstu i skopiuj jej zawartość.

        Konfiguracja może zawierać ustawienia IPv6. Ponieważ routery GL.iNet nie obsługują IPv6 wystarczająco dobrze, usuń treść dotyczącą IPv6. Poniżej znajduje się przykład — zaznaczony fragment to właśnie ustawienia IPv6.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}
    
    4. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    5. Możesz też użyć [aplikacji mobilnej](../faq/mobile_app.md), aby skonfigurować OVPN.

??? "PrivateVPN"
    ### PrivateVPN

    [Oficjalna strona](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Zaloguj się, a następnie przejdź do [Control panel](https://privatevpn.com/control-panel){target="_blank"}.
    
        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. Wybierz serwer.
    
        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. Kliknij **GENERATE CONFIG**, a następnie skopiuj konfigurację.
    
        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PrivadoVPN"
    ### PrivadoVPN

    [Oficjalna strona](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Wejdź na stronę PrivadoVPN i zaloguj się.

    Na pulpicie znajdź sekcję Manual Configuration i kliknij WireGuard. Wybierz serwer, z którym chcesz się połączyć, a następnie kliknij Download Configration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Proton VPN"
    ### Proton VPN

    [Oficjalna strona](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Jeśli korzystasz z [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, skorzystaj z przewodnika [tutaj](https://protonvpn.com/support/wireguard-configurations/){target="_blank"}, aby wygenerować plik konfiguracyjny WireGuard.

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PureVPN"
    ### PureVPN

    [Oficjalna strona](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Skorzystaj z [tego przewodnika](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} lub z poniższych kroków, aby ręcznie uzyskać plik konfiguracyjny PureVPN.

    1. Zaloguj się na swoje konto w [PureVPN Member Area](https://my.puremember.com/){target="_blank"}. Po zalogowaniu kliknij **Manual Configuration** w menu po lewej stronie.

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Wybierz docelowe miasto i kliknij **Download** po prawej stronie.

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. W wyskakującym oknie wybierz **WireGuard** jako protokół.

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Wybierz **Linux** jako typ urządzenia, a następnie kliknij **Generate Configuration**. Plik konfiguracyjny zostanie pobrany na urządzenie lokalne.

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), aby dokończyć konfigurację.

    [Link referencyjny](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [Oficjalna strona](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Zaloguj się na [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff), znajdź sekcję pobierania konfiguracji VPN i wykonaj opisane tam kroki, aby uzyskać konfigurację.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Pobierz konfigurację VPN.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "StarVPN"
    ### StarVPN

    [Oficjalna strona](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Zarejestruj konto w StarVPN**

        Przejdź do opcji [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} i wybierz plan VPN odpowiadający Twoim potrzebom. Konto możesz założyć podczas płatności albo bezpośrednio [tutaj](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Pobierz konfigurację WireGuard**

        Zaloguj się do panelu klienta StarVPN [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. Kliknij **Wireguard Config**, aby pobrać plik konfiguracyjny. Każdy slot zawiera unikalny plik konfiguracyjny WireGuard.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Wskazówka:** Jeśli chcesz używać technik zaciemniania AmneziaWG, kliknij **AmneziaWG Config**, aby pobrać plik konfiguracyjny. Każdy slot zawiera unikalny plik konfiguracyjny AmneziaWG.
    
        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Edytuj plik konfiguracyjny (opcjonalnie)**
    
        Konfiguracja może zawierać adres IPv6. Aby uniknąć problemów ze zgodnością i łącznością, otwórz plik .conf i usuń adres IPv6, jak pokazano poniżej.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), aby przesłać plik konfiguracyjny do routera GL.iNet.

    Odnośniki:
    
    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [Oficjalna strona](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Jeśli korzystasz z [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, zaloguj się na [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}.
    
    2. Wybierz lokalizację z listy rozwijanej, kliknij **GENERATE**, a następnie otwórz pobrany plik tekstowy.
    
        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    4. Możesz też użyć [aplikacji mobilnej](../faq/mobile_app.md), aby skonfigurować StrongVPN.

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [Oficjalna strona](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Wejdź na [https://trust.zone/setup](https://trust.zone/setup) i zaloguj się.
    
    2. Przewiń do sekcji WireGuard, wybierz żądany port, a następnie pobierz konfigurację wybranego serwera lub plik ZIP ze wszystkimi konfiguracjami.

    3. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN.AC"
    ### VPN.AC

    [Oficjalna strona](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Jeśli korzystasz z [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, zaloguj się do panelu sterowania i znajdź WireGuard Manager w menu „Services”.
    
        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. Utwórz konfigurację i pobierz ją.
    
        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Oficjalna strona](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Jeśli korzystasz z [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, zaloguj się do [User Office](https://my.keepsolid.com/){target="_blank"} > wybierz aplikację VPN Unlimited® > kliknij **Manage**.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}
    
    2. Kliknij pole pod **Device** i wybierz **Manually create a new device…** > ustaw własną nazwę, na przykład WireGuard > wybierz odpowiednią lokalizację w polu **Server** > wybierz z listy rozwijanej protokół **WireGuard**® > kliknij **Generate**.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}
    
    3. Parametry konfiguracji pojawią się poniżej w formacie tekstowym.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        Złóż konfigurację według poniższego wzoru.

        <p>
        [Interface]</br>
        PrivateKey = <i>wklej PrivateKey z panelu User Office</i></br>
        ListenPort = <i>wklej wartość portu nasłuchu (ListenPort)</i></br>
        Address = <i>wklej informacje z pola Address</i></br>
        DNS = <i>wklej dane DNS z panelu User Office</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>wklej PublicKey z panelu User Office</i></br>
        PresharedKey = <i>wklej wartość PresharedKey</i></br>
        AllowedIPs = <i>wklej wartość AllowedIPs</i></br>
        Endpoint = <i>wklej informacje z pola Endpoint</i></br>
        </p>

    4. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).
 
    [Link referencyjny 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Link referencyjny 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [Oficjalna strona](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Zaloguj się do swojego konta Windscribe [tutaj](https://windscribe.com/login?auth_required){target="_blank"}, a następnie otwórz [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}. 
    
    2. Wybierz lokalizację serwera i port, którego chcesz użyć, a następnie kliknij **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "12VPX"
    ### 12VPX

    [Oficjalna strona](https://12vpx.com/?aff=1174){target="_blank"}

    Jeśli korzystasz z [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, zaloguj się i otwórz [tę stronę](https://12vpx.com/setup/wireguard){target="_blank"}, gdzie zobaczysz konfiguracje wszystkich serwerów.

    Następnie postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
