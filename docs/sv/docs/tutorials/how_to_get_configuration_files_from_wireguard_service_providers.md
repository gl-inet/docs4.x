# Så hämtar du konfigurationsfiler från WireGuard-tjänsteleverantörer {#how-to-get-configuration-files-from-wireguard-service-providers}

??? "AzireVPN"
    ### AzireVPN {#azirevpn}

    [Officiell webbplats](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Öppna [AzireVPNs officiella webbplats](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} och logga in. Öppna sedan [WireGuard Configuration generator](https://www.azirevpn.com/cfg/wireguard){target="_blank"}.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. Välj **IPv4** under IP-alternativet. Klicka sedan på **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-azirevpn).

    4. Du kan även konfigurera AzireVPN med [mobilappen](../faq/mobile_app.md).

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [Officiell webbplats](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN erbjuder ett enkelt sätt att använda företagets WireGuard-tjänst på en GL.iNet-router.

    1. Anslut till routern via [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}.

    2. Kopiera installationsadressen nedan, klistra in den i terminalen och tryck på Enter. (Högerklicka med musen för att klistra in.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. Installationen startar och du ombeds att ange användarnamn och lösenord. När du skriver eller klistrar in lösenordet syns ingen ändring i terminalen. Tryck bara på Enter när du har angett lösenordet.

    4. När installationen är klar går du till webbadministrationspanelen. Där finns en hide.me VPN-grupp som redan innehåller konfigurationsfiler. Anslut på samma sätt som med en vanlig konfigurationsfil.

    **Obs!** Nyckeln i Hide.me VPN-konfigurationsfilen skapas på nytt före varje anslutning och blir ogiltig när anslutningen kopplas från. Det går därför inte att ansluta genom att kopiera konfigurationsfilen till andra enheter.

    [Referenslänk](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad {#mullvad}

    [Officiell webbplats](https://mullvad.net/){target="_blank"}

    1. Öppna [Mullvads officiella webbplats](https://mullvad.net/){target="_blank"} och logga in. Öppna sedan [generatorn för WireGuard-konfigurationsfiler](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}.

    2. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-mullvad).

    3. Du kan även konfigurera Mullvad med [mobilappen](../faq/mobile_app.md).

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access) {#pia-private-internet-access}

    [Officiell webbplats](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    WireGuard-konfigurationer kan inte hämtas från webbplatsen. Konfigurera PIA VPN med [mobilappen](../faq/mobile_app.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark {#surfshark}

    [Officiell webbplats](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Om du använder [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} loggar du in, går till [den här sidan](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, klickar på **Router** och väljer **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. Välj **I don't have a key pair** i nästa fönster.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Välj **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. När nyckeln har skapats väljer du **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Välj slutligen platsen som du vill konfigurera och klicka på knappen **download** bredvid platsen. Konfigurationsfilerna hämtas.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-surfshark).

    [Referenslänk](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN {#airvpn}

    [Officiell webbplats](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Om du använder [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"} loggar du in på webbplatsen, går till [Client Area](https://airvpn.org/client/){target="_blank"} och klickar på [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Välj WireGuard under Protocols på sidan Config Generator.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Välj en server, bläddra längst ned på sidan och klicka på **Generate**. Konfigurationsfilen hämtas.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Astrill"
    ### Astrill {#astrill}

    [Officiell webbplats](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Om du använder [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"} loggar du in och öppnar sedan [den här sidan](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} för att skapa WireGuard-konfigurationer.

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "IVPN"
    ### IVPN {#ivpn}

    [Officiell webbplats](https://www.ivpn.net/){target="_blank"}

    Om du använder [IVPN](https://www.ivpn.net/){target="_blank"} måste du skapa WireGuard-konfigurationen manuellt. Följ guiden för ditt operativsystem.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "NVPN"
    ### NVPN {#nvpn}

    [Officiell webbplats](https://www.nvpn.net/){target="_blank"}

    Följ guiden [här](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} för att skapa konfigurationen.

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "OVPN"
    ### OVPN {#ovpn}

    [Officiell webbplats](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Logga in på [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} och leta reda på menyn nedan för att hämta WireGuard-konfigurationsfiler.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Klicka på **Generate WireGuard keys**, välj önskad server och hämta sedan konfigurationen.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Öppna konfigurationen i en textredigerare och kopiera innehållet.

        Konfigurationen kan innehålla IPv6-innehåll. Eftersom GL.iNet-routrar inte har fullständigt stöd för IPv6 bör du ta bort detta innehåll. Exemplet nedan visar IPv6-innehållet markerat.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    5. Du kan även konfigurera OVPN med [mobilappen](../faq/mobile_app.md).

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [Officiell webbplats](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Logga in och öppna sedan [Control panel](https://privatevpn.com/control-panel){target="_blank"}.

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. Välj en server.

        ![select a server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. Klicka på **GENERATE CONFIG** och kopiera sedan konfigurationen.

        ![generate config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [Officiell webbplats](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Öppna PrivadoVPNs webbplats och logga in.

    Leta reda på avsnittet Manual Configuration på instrumentpanelen och klicka på WireGuard. Välj servern som du vill ansluta till och klicka sedan på Download Configuration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [Officiell webbplats](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Om du använder [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} följer du guiden [här](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} för att skapa WireGuard-konfigurationsfilen.

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PureVPN"
    ### PureVPN {#purevpn}

    [Officiell webbplats](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Se [den här guiden](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} eller följ stegen nedan för att hämta PureVPN-konfigurationsfilen manuellt.

    1. Logga in på [PureVPN Member Area](https://my.puremember.com/){target="_blank"} med ditt konto. Klicka på **Manual Configuration** i menyn till vänster när du har loggat in.

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Välj önskad stad och klicka på **Download** till höger.

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. Välj **WireGuard** som protokoll i popup-fönstret.

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Välj **Linux** som enhetstyp och klicka på **Generate Configuration**. Konfigurationsfilen hämtas till den lokala enheten.

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

        **Obs!** WireGuard-konfigurationen upphör att gälla efter 30 minuter. Aktivera anslutningen inom giltighetstiden. Annars måste du skapa en ny konfiguration.

    Följ sedan [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) för att slutföra konfigurationen.

    [Referenslänk](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN {#spidervpn}

    [Officiell webbplats](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Logga in på [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) och leta reda på avsnittet för VPN-konfiguration. Följ stegen för att hämta konfigurationen.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Hämta VPN-konfigurationen.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "StarVPN"
    ### StarVPN {#starvpn}

    [Officiell webbplats](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Registrera ett konto hos StarVPN**

        Öppna företagets alternativ för [prisplaner](https://www.starvpn.com/#pricing){target="_blank"} och välj en VPN-plan som passar dina behov. Du kan registrera dig i kassan eller direkt [här](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Hämta WireGuard-konfigurationen**

        Logga in på StarVPN-medlemmarnas [instrumentpanel](https://www.starvpn.com/dashboard){target="_blank"}. Klicka på **WireGuard Config** för att hämta konfigurationsfilen. Varje plats innehåller en unik WireGuard-konfigurationsfil.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Tips**: Om du vill använda AmneziaWG-obfuskering klickar du på **AmneziaWG Config** för att hämta konfigurationsfilen. Varje plats innehåller en unik AmneziaWG-konfigurationsfil.

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Redigera konfigurationsfilen (valfritt)**

        Konfigurationen kan innehålla en IPv6-adress. Undvik kompatibilitets- och anslutningsproblem genom att öppna .conf-filen och ta bort IPv6-adressen enligt nedan.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Följ sedan [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) för att ladda upp konfigurationsfilen till GL.iNet-routern.

    Referenser:

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [Officiell webbplats](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Om du använder [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} loggar du in på [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}.

    2. Välj en plats i listrutan, klicka på **GENERATE** och öppna den hämtade textfilen.

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    4. Du kan även konfigurera StrongVPN med [mobilappen](../faq/mobile_app.md).

??? "TRUST.ZONE"
    ### TRUST.ZONE {#trustzone}

    [Officiell webbplats](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Öppna [https://trust.zone/setup](https://trust.zone/setup) och logga in.

    2. Bläddra ned till avsnittet WireGuard, välj önskad port och hämta sedan en konfiguration för en viss server eller en zip-fil med alla konfigurationer.

    3. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [Officiell webbplats](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Om du använder [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"} loggar du in på kontrollpanelen och letar reda på WireGuard Manager i menyn "Services".

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. Skapa och hämta konfigurationen.

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [Officiell webbplats](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Om du använder [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"} loggar du in på [User Office](https://my.keepsolid.com/){target="_blank"} > väljer programmet VPN Unlimited® > klickar på **Manage**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/01.jpg){class="glboxshadow"}

    2. Klicka på fältet under **Device** och klicka på **Manually create a new device…** > ange ett eget namn, till exempel WireGuard > välj önskad plats under **Server** > välj protokollet **WireGuard**® i listrutan > klicka på **Generate**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/02.jpg){class="glboxshadow"}

    3. Konfigurationsparametrarna visas sedan i textformat nedan.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/03.jpg){class="glboxshadow"}

        Sätt samman konfigurationen enligt nedan.

        <p>
        [Interface]<br>
        PrivateKey = <i>klistra in PrivateKey från User Office</i><br>
        ListenPort = <i>klistra in uppgifterna för ListenPort</i><br>
        Address = <i>klistra in informationen för Address</i><br>
        DNS = <i>klistra in DNS-uppgifterna från User Office</i><br>
        <br>
        [Peer]<br>
        PublicKey = <i>klistra in PublicKey från User Office</i><br>
        PresharedKey = <i>klistra in uppgifterna för PresharedKey</i><br>
        AllowedIPs = <i>klistra in uppgifterna för AllowedIPs</i><br>
        Endpoint = <i>klistra in informationen för Endpoint</i><br>
        </p>

    4. Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    [Referenslänk 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Referenslänk 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe {#windscribe}

    [Officiell webbplats](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Logga in på ditt Windscribe-medlemskonto [här](https://windscribe.com/login?auth_required){target="_blank"} och öppna sedan [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.

    2. Välj önskad serverplats och port och klicka sedan på **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Fortsätt enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "X-VPN"
    ### X-VPN {#x-vpn}

    [Officiell webbplats](https://xvpn.io/go?aff_id=nk5bu995){target="_blank"}

    X-VPN är integrerat i GL.iNet-routrar från firmware v4.11.

    Om routern använder firmware v4.11 eller senare kan du logga in på X-VPN direkt i GL.iNets webbadministrationspanel med en inloggningstoken. Klicka [här](../interface_guide/wireguard_client.md#set-up-x-vpn) för mer information.

    Om routern använder en firmwareversion som är äldre än v4.11 eller om du vill hämta en X-VPN-konfigurationsfil manuellt följer du stegen nedan.

    1. [Logga in](https://xvpn.io/login){target="_blank"} på X-VPN och gå sedan till **VPN** -> **VPN on Router**.

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn1.png){class="glboxshadow"}

    2. Leta reda på **Step 1** till höger och välj **WireGuard** som protokoll.

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn2.png){class="glboxshadow"}

    3. Välj önskad **Region** och **State/City** under **Step 2** och klicka sedan på **Search**.

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn3.png){class="glboxshadow"}

    4. Klicka på hämtningsknappen i sökresultatet för att hämta konfigurationsfilen för önskad server.

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "12VPX"
    ### 12VPX {#12vpx}

    [Officiell webbplats](https://12vpx.com/?aff=1174){target="_blank"}

    Om du använder [12VPX](https://12vpx.com/?aff=1174){target="_blank"} loggar du in och öppnar [den här sidan](https://12vpx.com/setup/wireguard){target="_blank"}. Där visas konfigurationerna för alla servrar.

    Fortsätt sedan enligt [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
