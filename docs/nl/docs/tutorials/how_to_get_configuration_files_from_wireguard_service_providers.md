# Configuratiebestanden verkrijgen van WireGuard-serviceproviders {#how-to-get-configuration-files-from-wireguard-service-providers}

??? "AzireVPN"
    ### AzireVPN {#azirevpn}

    [Officiële website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Ga naar de [officiële website van AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}, meld je aan en open vervolgens de [WireGuard Configuration generator](https://www.azirevpn.com/cfg/wireguard){target="_blank"}.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. Selecteer bij de IP-optie **IPv4**. Klik vervolgens op **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-azirevpn) om door te gaan.

    4. Je kunt AzireVPN ook met de [mobiele app](../faq/mobile_app.md) instellen.

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [Officiële website](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN biedt een eenvoudige manier om de WireGuard-service op een GL.iNet-router te gebruiken.

    1. Maak via [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"} verbinding met de router.

    2. Kopieer de onderstaande installatie-URL, plak deze in de terminal en druk op Enter. Met de rechtermuisknop plak je de tekst.

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. De installatie wordt gestart en vervolgens wordt om je gebruikersnaam en wachtwoord gevraagd. Tijdens het typen of plakken van het wachtwoord verschijnt er niets in de terminal. Druk na het invoeren op Enter.

    4. Ga na voltooiing naar het webbeheerpaneel. Er is een hide.me VPN-groep gemaakt met configuratiebestanden. Maak op dezelfde manier verbinding als met elk ander configuratiebestand.

    **Opmerking:** de sleutel in het Hide.me VPN-configuratiebestand wordt vóór elke verbinding opnieuw gegenereerd en wordt na het verbreken van de verbinding ongeldig. Als je dit configuratiebestand naar andere apparaten kopieert, kunnen deze daarom geen verbinding maken.

    [Referentiekoppeling](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad {#mullvad}

    [Officiële website](https://mullvad.net/){target="_blank"}

    1. Ga naar de [officiële website van Mullvad](https://mullvad.net/){target="_blank"}, meld je aan en open vervolgens de [generator voor WireGuard-configuratiebestanden](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}.

    2. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-mullvad) om door te gaan.

    3. Je kunt Mullvad ook met de [mobiele app](../faq/mobile_app.md) instellen.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access) {#pia-private-internet-access}

    [Officiële website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Je kunt de WireGuard-configuraties niet via de website downloaden. Gebruik de [mobiele app](../faq/mobile_app.md) om PIA VPN in te stellen.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark {#surfshark}

    [Officiële website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Als je [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} gebruikt, meld je je aan en ga je naar [deze pagina](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}. Klik op **Router** en selecteer **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. Selecteer in het volgende venster **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Selecteer **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Selecteer **Choose a location** nadat de sleutel is gegenereerd.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Kies de locatie die je wilt instellen en klik naast de locatie op **download**. Je kunt de configuratiebestanden vervolgens downloaden.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-surfshark) om door te gaan.

    [Referentiekoppeling](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN {#airvpn}

    [Officiële website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Als je [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"} gebruikt, meld je je aan bij de website. Ga naar de [Client Area](https://airvpn.org/client/){target="_blank"} en klik op [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Selecteer op de pagina Config Generator WireGuard in het gedeelte Protocols.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Selecteer een server, scrol naar het einde en klik op **Generate**. Het configuratiebestand wordt gedownload.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "Astrill"
    ### Astrill {#astrill}

    [Officiële website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Als je [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"} gebruikt, meld je je aan en open je [deze pagina](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} om WireGuard-configuraties te genereren.

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "IVPN"
    ### IVPN {#ivpn}

    [Officiële website](https://www.ivpn.net/){target="_blank"}

    Als je [IVPN](https://www.ivpn.net/){target="_blank"} gebruikt, moet je de WireGuard-configuratie handmatig genereren. Volg de handleiding voor je besturingssysteem.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "NVPN"
    ### NVPN {#nvpn}

    [Officiële website](https://www.nvpn.net/){target="_blank"}

    Volg de handleiding [hier](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} om de configuratie te maken.

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "OVPN"
    ### OVPN {#ovpn}

    [Officiële website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Meld je aan bij [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} en zoek het onderstaande menu om WireGuard-configuratiebestanden te verkrijgen.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Klik op **Generate WireGuard keys**, kies de gewenste server en download de configuratie.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Open de configuratie in een teksteditor en kopieer de inhoud.

        De configuratie kan IPv6-inhoud bevatten. Omdat GL.iNet-routers IPv6 niet volledig ondersteunen, moet je deze IPv6-inhoud verwijderen. In het onderstaande voorbeeld is de IPv6-inhoud gemarkeerd.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

    5. Je kunt OVPN ook met de [mobiele app](../faq/mobile_app.md) instellen.

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [Officiële website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Meld je aan en open het [Control panel](https://privatevpn.com/control-panel){target="_blank"}.

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. Selecteer een server.

        ![select a server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. Klik op **GENERATE CONFIG** en kopieer vervolgens de configuratie.

        ![generate config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [Officiële website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Ga naar de PrivadoVPN-website en meld je aan.

    Zoek in het dashboard het gedeelte Manual Configuration en klik op WireGuard. Selecteer de server waarmee je verbinding wilt maken en klik op Download Configuration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [Officiële website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Als je [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} gebruikt, volg je de handleiding [hier](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} om het WireGuard-configuratiebestand te genereren.

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "PureVPN"
    ### PureVPN {#purevpn}

    [Officiële website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Raadpleeg [deze handleiding](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} of volg de onderstaande stappen om het PureVPN-configuratiebestand handmatig te verkrijgen.

    1. Meld je met je account aan bij de [PureVPN Member Area](https://my.puremember.com/){target="_blank"}. Klik na het aanmelden in het linkermenu op **Manual Configuration**.

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Selecteer de gewenste plaats en klik rechts op **Download**.

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. Selecteer in het pop-upvenster **WireGuard** als protocol.

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Selecteer **Linux** als apparaattype en klik op **Generate Configuration**. Het configuratiebestand wordt naar je lokale apparaat gedownload.

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

        **Opmerking**: de WireGuard-configuratie verloopt na 30 minuten. Activeer de verbinding binnen de geldigheidsduur. Anders moet je een nieuwe configuratie genereren.

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om de configuratie te voltooien.

    [Referentiekoppeling](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN {#spidervpn}

    [Officiële website](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Meld je aan bij [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) en zoek het gedeelte voor je VPN-configuratie. Volg de stappen om de configuratie te verkrijgen.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Download de VPN-configuratie.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "StarVPN"
    ### StarVPN {#starvpn}

    [Officiële website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Een account bij StarVPN registreren**

        Ga naar de beschikbare [abonnementen](https://www.starvpn.com/#pricing){target="_blank"} en kies een VPN-abonnement dat bij je behoeften past. Je kunt je bij het afrekenen of rechtstreeks [hier](https://www.starvpn.com/dashboard/register.php){target="_blank"} registreren.

    2. **De WireGuard-configuratie downloaden**

        Meld je aan bij het [dashboard](https://www.starvpn.com/dashboard){target="_blank"} voor StarVPN-leden. Klik op **WireGuard Config** om het configuratiebestand te downloaden. Elke sleuf bevat een uniek WireGuard-configuratiebestand.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Tips**: als je AmneziaWG-obfuscatietechnieken wilt gebruiken, klik je op **AmneziaWG Config** om het configuratiebestand te downloaden. Elke sleuf bevat een uniek AmneziaWG-configuratiebestand.

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Het configuratiebestand bewerken (optioneel)**

        De configuratie kan een IPv6-adres bevatten. Open het .conf-bestand en verwijder het IPv6-adres zoals hieronder om compatibiliteits- en verbindingsproblemen te voorkomen.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om het configuratiebestand naar je GL.iNet-router te uploaden.

    Referenties:

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [Officiële website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Als je [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} gebruikt, meld je je aan bij [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}.

    2. Selecteer een locatie in de vervolgkeuzelijst, klik op **GENERATE** en open het gedownloade tekstbestand.

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

    4. Je kunt StrongVPN ook met de [mobiele app](../faq/mobile_app.md) instellen.

??? "TRUST.ZONE"
    ### TRUST.ZONE {#trustzone}

    [Officiële website](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Ga naar [https://trust.zone/setup](https://trust.zone/setup) en meld je aan.

    2. Scrol naar het gedeelte WireGuard, kies de gewenste poort en download vervolgens een configuratie van een specifieke server of een zipbestand met alle configuraties.

    3. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [Officiële website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Als je [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"} gebruikt, meld je je aan bij het configuratiescherm en zoek je WireGuard Manager in het menu "Services".

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. Maak de configuratie en download deze.

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [Officiële website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Als je [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"} gebruikt, meld je je aan bij je [User Office](https://my.keepsolid.com/){target="_blank"} > selecteer je de toepassing VPN Unlimited® > en klik je op **Manage**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/01.jpg){class="glboxshadow"}

    2. Klik op het veld onder **Device** en klik op **Manually create a new device…** > voer een aangepaste naam in, bijvoorbeeld WireGuard > kies de gewenste locatie bij **Server** > selecteer het protocol **WireGuard**® in de vervolgkeuzelijst > en klik op **Generate**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/02.jpg){class="glboxshadow"}

    3. De configuratieparameters worden vervolgens hieronder in tekstindeling weergegeven.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/03.jpg){class="glboxshadow"}

        Combineer de configuratie als volgt.

        <p>
        [Interface]<br>
        PrivateKey = <i>plak de PrivateKey uit je User Office</i><br>
        ListenPort = <i>plak de ListenPort-gegevens</i><br>
        Address = <i>plak de Address-informatie</i><br>
        DNS = <i>plak de DNS-gegevens uit de User Office</i><br>
        <br>
        [Peer]<br>
        PublicKey = <i>plak de PublicKey uit de User Office</i><br>
        PresharedKey = <i>plak de PresharedKey-gegevens</i><br>
        AllowedIPs = <i>plak de AllowedIPs-gegevens</i><br>
        Endpoint = <i>plak de Endpoint-informatie</i><br>
        </p>

    4. Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

    [Referentiekoppeling 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Referentiekoppeling 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe {#windscribe}

    [Officiële website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Meld je [hier](https://windscribe.com/login?auth_required){target="_blank"} aan bij je Windscribe-account en open vervolgens de [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.

    2. Selecteer de serverlocatie en poort die je wilt gebruiken en klik op **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Volg [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "X-VPN"
    ### X-VPN {#x-vpn}

    [Officiële website](https://xvpn.io/go?aff_id=nk5bu995){target="_blank"}

    X-VPN is vanaf firmware v4.11 geïntegreerd in GL.iNet-routers.

    Als je router firmware v4.11 of nieuwer gebruikt, kun je je met een aanmeldingstoken rechtstreeks in het GL.iNet-webbeheerpaneel aanmelden bij X-VPN. Klik [hier](../interface_guide/wireguard_client.md#set-up-x-vpn) voor meer informatie.

    Volg de onderstaande stappen als je router firmware ouder dan v4.11 gebruikt of als je handmatig een X-VPN-configuratiebestand wilt downloaden.

    1. [Meld je aan](https://xvpn.io/login){target="_blank"} bij X-VPN en ga naar **VPN** -> **VPN on Router**.

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn1.png){class="glboxshadow"}

    2. Zoek rechts **Step 1** en selecteer **WireGuard** als protocol.

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn2.png){class="glboxshadow"}

    3. Kies bij **Step 2** de gewenste **Region** en **State/City** en klik op **Search**.

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn3.png){class="glboxshadow"}

    4. Klik in de zoekresultaten op de downloadknop om het configuratiebestand voor de gewenste server op te halen.

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

??? "12VPX"
    ### 12VPX {#12vpx}

    [Officiële website](https://12vpx.com/?aff=1174){target="_blank"}

    Als je [12VPX](https://12vpx.com/?aff=1174){target="_blank"} gebruikt, meld je je aan en open je [deze pagina](https://12vpx.com/setup/wireguard){target="_blank"}. Hier zie je de configuraties van alle servers.

    Volg daarna [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) om door te gaan.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
