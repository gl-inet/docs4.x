# Set Up OpenVPN Client on GL.iNet Routers {#set-up-openvpn-client-on-glinet-routers}

OpenVPN is an open‑source VPN protocol that uses virtual private network techniques to establish secure site‑to‑site or point‑to‑point connections.

Titta på videon eller följ stegen för att konfigurera OpenVPN Client.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Kontrollera att du har ett aktivt abonnemang hos en leverantör som stöder manuell OpenVPN-konfiguration. Kompatibla leverantörer finns [här](https://www.gl-inet.com/solutions/vpn/){target="_blank"}.

Hämta normalt konfigurationsfilen från leverantörens webbplats och ladda upp den till routern. Se [denna guide](#get-configuration-files-from-openvpn-service-providers) eller kontakta supporten.

Konfigurera via webbadministrationspanelen eller [mobilappen](../faq/mobile_app.md). Stegen nedan gäller webbpanelen.

---

In the web Admin Panel, navigate to **VPN** -> **OpenVPN Client**.

Med NordVPN klickar du på **NordVPN** och loggar in. Annars klickar du på **Add Manually** och laddar upp filer.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Set Up NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is a popular online VPN service for speed and security.

NordVPN-snabbkonfiguration är integrerad i GL.iNet. Ange tjänstuppgifterna från NordVPN Dashboard i webbpanelen eller appen för att hämta serverfiler utan manuell uppladdning.

1. Log in to your NordVPN web account [here](https://my.nordaccount.com/){target="_blank"}.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_login.png){class="glboxshadow"}

    Klicka på **NordVPN** på vänstermenyn i Nord Dashboard och sedan på **Set up NordVPN manually**.

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Verifiera e-postadressen, hitta **service credentials** och kopiera dem.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Logga in och öppna **VPN** -> **OpenVPN Client** -> **NordVPN**.

    Ange **service credentials** från steg 1, **INTE** kontots e-post och lösenord, och klicka på **Save and Continue**.

    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Välj protokoll, maximalt antal servrar per plats och platser och klicka på **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn2.png){class="glboxshadow"}

    It will download configuration files.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Once connected, a green dot will appear next to the configuration file.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

6. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Edit credentials.

    Klicka på kugghjulet för att ändra inloggningsuppgifterna.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Delete all files.

    Klicka på **Delete All** för att radera alla konfigurationsfiler.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Set Up OpenVPN Client Manually (for other providers) {#set-up-openvpn-client-manually-for-other-providers}

Om leverantören inte är integrerad hämtar du konfigurationsfilen från dess webbplats och laddar upp den till routern.

In the following steps, we will use [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} as an example.

1. Download a configuration file from Private Internet Access official website.

2. Logga in, öppna VPN -> OpenVPN Client och klicka på **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual1.png){class="glboxshadow"}

3. It will create a group on the left sidebar.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual2.png){class="glboxshadow"}

4. Set a descriptive name for the group (e.g., private internet access).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual3.png){class="glboxshadow"}

5. Ladda upp OpenVPN-filen, ange uppgifter vid behov och klicka på **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual4.png){class="glboxshadow"}

    - Det finns 4 typer av autentiseringsuppgifter:

        1. No authentication.

        2. Username and Password only.

        3. Passphrase only.

        4. Username, Password, and Passphrase.

    Den uppladdade filen visas.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual5.png){class="glboxshadow"}

6. Klicka på ikonen med tre punkter för att ansluta.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual6.png){class="glboxshadow"}

7. Once connected, a green dot will appear next to the configuration file.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual7.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

## Set Up OpenVPN Server on GL.iNet Router {#set-up-openvpn-server-on-glinet-router}

Med två GL.iNet-routrar kan en vara OpenVPN-server, vilket kräver offentlig IP, och den andra klient utan tredjepartstjänst.

For setting up OpenVPN server, please check [here](openvpn_server.md).

## Hämta konfigurationsfiler från OpenVPN-leverantörer {#get-configuration-files-from-openvpn-service-providers}

Vi har testat över 30 leverantörer och dokumenterat hur filerna hämtas.

Kontakta leverantörens support om den inte finns nedan.

??? "NordVPN"
    ### NordVPN {#nordvpn}

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Login to your NordVPN account**

        Logga in på [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} och öppna Nord Account Dashboard för service credentials.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_login.png){class="glboxshadow"}

        Klicka på NordVPN till vänster och sedan på **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Hitta och kopiera **Service credentials**.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Choose a NordVPN server and download the configuration file**

        Öppna **Server recommendation**, välj rekommenderad server och klicka på **Get setup configuration**.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_config_download.png){class="glboxshadow"}

        Välj **OpenVPN** och hämta UDP- eller TCP-konfigurationen.

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Hämta alla serverkonfigurationer [här](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Du kan även använda [mobilappen](../faq/mobile_app.md) för NordVPN.

??? "AirVPN"
    ### AirVPN {#airvpn}

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Login your AirVPN account

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Välj Config Generator, Linux och önskad server.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Nedladdningssidan för konfigurationsfilen visas.

        ![download config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill {#astrill}

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Information quoted from [Astrill official instruction](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Generate and Download Astrill Openvpn configuration ZIP

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Type a Description like OPENVPN_GUI.

    3. Click on ADD to my certificates button.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Once OpenVPN certificate is added, click on Download button.

        ![download certificate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN {#bolehvpn}

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

    Logga in på [Dashboard](https://users.bolehvpn.net/){target="_blank"}, välj formatet [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}, hämta och packa upp filerna.

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN {#cactusvpn}

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Download](https://www.cactusvpn.com/downloads/){target="_blank"} directly.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm {#cryptostorm}

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [Download](https://cryptostorm.is/configs/ecc/){target="_blank"} directly.

??? "CyberGhost"
    ### CyberGhost {#cyberghost}

    [Official Website](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Information quoted from [CyberGhost official instruction](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Login your CyberGhost VPN online account.

        ![login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Välj **VPN** till vänster, klicka på **Configure Device** och skapa serverkonfigurationen.

        ![config device](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Now create your server configuration, as described below:

        * **Protocol** : **OpenVPN**
        * **Country**: Välj landet som trafiken ska komma från; CyberGhost väljer server automatiskt.
        * **Server group**: Välj servergrupp och OpenVPN-protokoll (UDP eller TCP).

        **OpenVPN UDP** ger högre hastighet men kan orsaka avbrutna hämtningar. Det är standard.

        **OpenVPN TCP** är stabilare men långsammare. Välj vid återkommande frånkopplingar.

        Spara valda parametrar med **Save Configuration**.

    4. Klicka på **View Configuration** för genererade **OpenVPN**-uppgifter.

        ![view configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Anteckna följande efter konfigurationen:

        * **Server Group**: Landets serveradress, till exempel `12345-1-ca.cg-dialup.net`. CyberGhost väljer server automatiskt.
        * **Username**: Ett protokollspecifikt användarnamn, INTE det vanliga CyberGhost-användarnamnet.
        * **Password**: Ett protokollspecifikt lösenord, INTE det vanliga CyberGhost-lösenordet.

        Klicka på *Download Configuration* och hämta filen.

        ![save config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN {#expressvpn}

    [Official Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"} | [Get 30 days free](https://www.expressvpn.com/refer-a-friend/30-days-free?referrer_id=97477587){rel="sponsored" target="_blank"}

    1. Besök [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} och logga in.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Ange verifieringskoden** som skickas via e-post.

    2. Klicka på **Set up your devices** till vänster.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. Öppna **Advanced setup** under **Applications** och klicka på **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. **username**, **password** och **OpenVPN configuration files** visas.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Klicka på önskade platser för att hämta .ovpn-filer.

        **Håll webbläsarfönstret öppet** för senare konfiguration.

    [Refer link](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN {#fastestvpn}

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Hämta FastestVPN-filer för OpenVPN TCP och UDP [här](https://support.fastestvpn.com/download/fastestvpn_ovpn/).

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN {#finchvpn}

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. Login your FinchVPN account.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Öppna Download och klicka på Download under FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Choose Linux

        ![finchvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Välj protokoll, vanligtvis **Port 8484 over UDP**.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Markera att användarnamn och lösenord ska inkluderas innan filen hämtas.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN {#hideipvpn}

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. Login your HideIPVPN account.

    2. Öppna Package till vänster, klicka på paketet och kontrollera att det är aktivt.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. Fliken VPN visar VPN Login Details med användarnamn och lösenord för OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Scroll down to download OpenVPN config files.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Logga in på Hide.me och öppna Server Locations till vänster.

    2. Download the OpenVPN Configuration for Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield {#hotspot-shield}

    [Official Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Note: The Hotspot Shield Router configuration files are no longer available or supported. The following steps are here for legacy purposes for those that may still have the files installed.**

    1. Gå till [Hotspot Shield](https://www.hotspotshield.com/){target="_blank"}, klicka på Account och logga in.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Go to [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router){target="_blank"}

        Välj virtuell plats i Select location och klicka på "Download file". Ange användarnamn och lösenord när OpenVPN-klienten konfigureras.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Refer link](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router){target="_blank"}

??? "IPVANISH"
    ### IPVANISH {#ipvanish}

    [Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Hämta alla serverfiler [här](https://configs.ipvanish.com/configs/configs.zip). Arkivet innehåller .ovpn- och .crt-filer. Radera oanvända .ovpn-filer om arkivet är för stort.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Enskilda filer finns [här](https://www.ipvanish.com/software/configs/){target="_blank"}. Hämta även **ca.ipvanish.com.crt** och packa .crt- och .ovpn-filerna i ett zip-arkiv.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup){target="_blank"}

??? "IVACY"
    ### IVACY {#ivacy}

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    För Ivacy OpenVPN Client krävs:

    - Användarnamn för manuell OpenVPN-konfiguration från "Download Configuration".
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Lösenordet för Ivacy-kontot.
    - An OpenVPN configuration file

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/){target="_blank"}

??? "IVPN"
    ### IVPN {#ivpn}

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Download the [OpenVPN config files](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Find the Account ID on [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. När filen dras till Add a New OpenVPN Configuration anger du User Name och Password. User Name är Account ID som börjar med **ivpn**. Lösenordet kan till exempel vara **ivpn**.

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html){target="_blank"}

??? "OVPN"
    ### OVPN {#ovpn}

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    Logga in och hämta OpenVPN-filen via menyn nedan.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Välj server och hämta.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    Användarnamn och lösenord är samma som för OVPN.

??? "OysterVPN"
    ### OysterVPN {#oystervpn}

    [Official Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Öppna [OysterVPNs serverlista](https://support.oystervpn.com/server-list/){target="_blank"} och klicka på **Download .ovpn file**.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. Användarnamn och lösenord är samma som för OysterVPN.

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

??? "PIA (Private Internet Access)"
    ### PIA {#pia}

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Download](https://www.privateinternetaccess.com/openvpn/openvpn.zip) directly.

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Logga in och öppna **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank"} directly.

    Den officiella filen finns [här](https://privatevpn.com/client/PrivateVPN-TUN.zip). Filnamnet med specialtecknen `Bogotá` har bytt namn på grund av ett importfel.

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN has WireGuard service, we recommend to use WireGuard, checkout [here](wireguard_client.md)**.

    1. Login your [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} account.

    2. Klicka på **Download** till vänster.

    3. Choose Router platform, protocol etc, find your target country to download configuration file.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. OpenVPN-uppgifterna skiljer sig från Proton-inloggningen och finns under **Account -> OpenVPN/IKEv2 username**.

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN {#purevpn}

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    För PureVPN krävs OpenVPN-användarnamn, lösenord och konfigurationsfil från PureVPN-kontot.

    1. [Sign in to your PureVPN account.](https://my.purevpn.com/){target="_blank"}
    2. Klicka på **Subscriptions** till vänster.
    3. Bläddra ned till OpenVPN-användarnamn och lösenord.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. Klicka på **Manual Configuration** till vänster.
    5. Välj VPN-plats och klicka på **Download**.

    [Refer link](https://support.purevpn.com/openvpn-files){target="_blank"}

    GL.iNet routers don't support the [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"} feature of PureVPN, because it needs PPTP.

??? "SaferVPN"
    ### SaferVPN {#safervpn}

    [Official Website](https://safervpn.com/?a_aid=563){target="_blank"}

    Click [here](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup){target="_blank"} to download configuration files directly.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN {#starvpn}

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN erbjuder OpenVPN och WireGuard. WireGuard rekommenderas eftersom det ofta är snabbare. Se [här](wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    Följ stegen nedan om du föredrar OpenVPN.

    1. **Register an account with StarVPN**

        Öppna [prisplanerna](https://www.starvpn.com/#pricing){target="_blank"}, välj abonnemang och registrera dig vid betalning eller [här](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Download OpenVPN Configuration**

        Logga in på [dashboard](https://www.starvpn.com/dashboard){target="_blank"}, öppna **VPN Configuration** -> **OpenVPN Config** och kopiera OVPN-användarnamn och lösenord.

        ![download starvpn ovpn config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/ovpnconfigdl.png){class="glboxshadow"}

        Select UDP or TCP and download a configuration file.

        ![select udp or tcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/udp_tcp.png){class="glboxshadow"}

    3. **Edit configuration file**

        Vissa GL.iNet-routrar stöder inte IPv6. Ta bort IPv6-innehåll ur .ovpn-filen för att undvika problem.

        ![remove ipv6](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/remove_ipv6.png){class="glboxshadow"}

??? "StreamVPN"
    ### StreamVPN {#streamvpn}

    [Official Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Logga in på [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} och klicka på **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Click **VPN Router**, it will download a .zip archive file called `StreamVPN.zip`.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Note:** Only the configuration file name contains "Primary" work.

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Logga in på [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} och klicka på **Account Setup Instructions** i VPN Accounts Summary.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Find the Manual setup section, follow the steps to get configuration.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark {#surfshark}

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Find your login details**

        Surfshark service credentials skiljer sig från kontots e-post och lösenord och krävs för manuell OpenVPN-konfiguration.

        Logga in på [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} och öppna [denna sida](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"} för manuella uppgifter.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Choose a Surfshark server**

        Välj fliken **Locations** för alla Surfshark-servrar.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        It will ask to choose TCP or UDP. Click [here](../faq/openvpn_tcp_udp.md) to see the difference.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    Hämta alla konfigurationer [här](https://api.surfshark.com/v1/server/configurations).

    Tips! Om zip-filen är för stor kan du radera vissa .ovpn-filer eller ladda upp en enda .ovpn-fil.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac download configuration" src="https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate {#vpngate}

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    OpenVPN-filer listas på [VPN Gate](https://www.vpngate.net/en/) efter serverplats.

    1. Klicka på OpenVPN Config file i kolumnen **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Nedladdningssidan visas.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Safe"
    ### VPN Safe {#vpn-safe}

    [Officiell webbplats](https://secure.vpnsafe.net/aff.php?aff=6){target="_blank"}

    1. Logga in på **VPN Safe Dashboard** och klicka på din aktiva VPN-tjänst.

        ![vpnsafe1](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe1.png){class="glboxshadow"}

    2. Rulla ned på sidan Product Details till **OpenVPN Configuration**.

        ![vpnsafe2](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe2.png){class="glboxshadow"}

        ![vpnsafe3](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe3.png){class="glboxshadow"}

    3. Klicka på **UDP Configs** (rekommenderas) eller **TCP Configs** för att hämta alla UDP/TCP-konfigurationer som ett ZIP-arkiv. Packa upp det för att få alla tillgängliga konfigurationsfiler.

        ![vpnsafe4](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe4.jpg){class="glboxshadow"}

    4. Klicka på **UDP Servers** (rekommenderas) eller **TCP Servers** för att få en URL-lista över alla tillgängliga UDP/TCP-servrar.

        ![vpnsafe5](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe5.jpg){class="glboxshadow"}

    5. Välj den server du vill ansluta till i listrutan och klicka på **Download UDP/TCP Config** för att hämta en enskild UDP/TCP-konfiguration.

        ![vpnsafe6](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe6.jpg){class="glboxshadow"}

        ![vpnsafe7](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe7.jpg){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Information quoted from [VPN unlimited official instruction](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Logga in på User Office, klicka på Manage för VPN Unlimited och följ stegen:

    1. Select a device

        Välj eller skapa en enhet. Radera en gammal enhet eller köp fler platser om de är slut.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Choose the desired server location

        VPN Unlimited har över 400 servrar på över 70 platser. Här används Tyskland.

    3. Select the VPN protocol

        select OpenVPN protocol.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Create a configuration

        Klicka på Generate för alla nödvändiga VPN-data.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN {#vyprvpn}

    VyprVPN offers the OpenVPN files here: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    Zip-filen innehåller OpenVPN160 och OpenVPN256. Radera OpenVPN160 och ladda upp arkivet.

??? "Windscribe"
    ### Windscribe {#windscribe}

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Log in to your Windscribe membership account [here](https://windscribe.com/login?auth_required){target="_blank"}, then access the [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}.

    2. Välj serverplats, protokoll, port och OpenVPN-version och klicka på **Download Config** för en .ovpn-fil.

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Klicka på **Get Credentials** och kopiera uppgifterna eller håll sidan öppen.

    4. Then follow [this guide](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers) to continue.

??? "ZoogVPN"
    ### ZoogVPN {#zoogvpn}

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Logga in på [webbplatsen](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}, öppna [konfigurationssidan](https://app.zoogvpn.com/setup/configuration-files){target="_blank"} och hämta filen i TCP- eller UDP-kolumnen.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Följ sedan [guiden för OpenVPN Client](#set-up-openvpn-client-manually-for-other-providers). Användarnamn och lösenord är samma som på ZoogVPN.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
