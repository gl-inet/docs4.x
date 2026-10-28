# Set Up OpenVPN Client on GL.iNet Routers {#set-up-openvpn-client-on-glinet-routers}

OpenVPN is an open‑source VPN protocol that uses virtual private network techniques to establish secure site‑to‑site or point‑to‑point connections.

Bekijk deze video of volg de onderstaande stappen om een OpenVPN-client op een GL.iNet-router in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Controleer voordat je begint of je een actief abonnement hebt bij een VPN-serviceprovider die handmatige OpenVPN-configuratie ondersteunt. Klik [hier](https://www.gl-inet.com/solutions/vpn/){target="_blank"} voor OpenVPN-providers die compatibel zijn met GL.iNet.

Gewoonlijk ga je eerst naar de officiële website van je VPN-serviceprovider en download je het configuratiebestand. Upload dit vervolgens naar je router om deze als OpenVPN-client in te stellen. Raadpleeg [deze informatie](#get-configuration-files-from-openvpn-service-providers) of neem contact op met de ondersteuning van de provider als je niet weet hoe je het configuratiebestand verkrijgt.

Je kunt een OpenVPN-client instellen via het webbeheerpaneel of de [mobiele app](../faq/mobile_app.md). Hieronder staan de stappen voor het webbeheerpaneel.

---

In the web Admin Panel, navigate to **VPN** -> **OpenVPN Client**.

Als je een NordVPN-abonnement hebt, klik je op **NordVPN** om je aan te melden. Klik anders op **Add Manually** om de OpenVPN-configuratiebestanden te uploaden.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Set Up NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is een populaire online VPN-dienst voor snelheid en beveiliging.

De snelle installatie van NordVPN is geïntegreerd in het beheerpaneel van GL.iNet-routers. Voer de accountgegevens uit het NordVPN Dashboard in via het webbeheerpaneel of de mobiele app van de router om online configuratiebestanden voor alle NordVPN-servers op te halen. Je hoeft dan geen bestanden handmatig te uploaden.

1. Log in to your NordVPN web account [here](https://my.nordaccount.com/){target="_blank"}.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_login.png){class="glboxshadow"}

    Klik na het aanmelden bij het Nord Dashboard in het linkermenu op **NordVPN** en daarna op **Set up NordVPN manually**.

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Je vindt daar de **service credentials**. Verifieer eerst je e-mailadres om deze gegevens op te halen en kopieer ze voor later gebruik.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Meld je aan bij het webbeheerpaneel van je router en ga naar **VPN** -> **OpenVPN Client** -> **NordVPN**.

    Voer de **service credentials** uit stap 1 in. Dit zijn **NIET** het e-mailadres en wachtwoord van je account. Klik daarna op **Save and Continue**.

    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Selecteer het protocol, het maximale aantal servers per locatie en de locaties en klik op **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn2.png){class="glboxshadow"}

    It will download configuration files.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Start a connection.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Once connected, a green dot will appear next to the configuration file.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

6. Update servers.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Edit credentials.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Delete all files.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Set Up OpenVPN Client Manually (for other providers) {#set-up-openvpn-client-manually-for-other-providers}

Als je OpenVPN-serviceprovider niet in het beheerpaneel is geïntegreerd, haal je het configuratiebestand eerst op via de officiële website van de provider. Upload dit vervolgens naar de router om een OpenVPN-client in te stellen.

In the following steps, we will use [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} as an example.

1. Download a configuration file from Private Internet Access official website.

2. Meld je aan bij het webbeheerpaneel van je router, ga naar VPN -> OpenVPN Client en klik op **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual1.png){class="glboxshadow"}

3. It will create a group on the left sidebar.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual2.png){class="glboxshadow"}

4. Geef de groep een duidelijke naam, bijvoorbeeld private internet access.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual3.png){class="glboxshadow"}

5. Upload je OpenVPN-configuratiebestand. Voer zo nodig de aanmeldgegevens in en klik op **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual4.png){class="glboxshadow"}

    - Er zijn 4 soorten aanmeldgegevens voor verificatie:

        1. No authentication.

        2. Username and Password only.

        3. Passphrase only.

        4. Username, Password, and Passphrase.

    Vervolgens zie je het geüploade configuratiebestand.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual5.png){class="glboxshadow"}

6. Klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual6.png){class="glboxshadow"}

7. Once connected, a green dot will appear next to the configuration file.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual7.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

## Set Up OpenVPN Server on GL.iNet Router {#set-up-openvpn-server-on-glinet-router}

Als je twee GL.iNet-routers hebt, kun je de ene als OpenVPN-server instellen, waarvoor een openbaar IP-adres vereist is, en de andere als OpenVPN-client. Zo maak je een eigen VPN-verbinding zonder abonnement op een externe VPN-dienst.

Raadpleeg [deze pagina](openvpn_server.md) om een OpenVPN-server in te stellen.

## Configuratiebestanden van OpenVPN-serviceproviders verkrijgen {#get-configuration-files-from-openvpn-service-providers}

We hebben meer dan 30 OpenVPN-serviceproviders getest en de stappen voor het verkrijgen van configuratiebestanden vastgelegd. Volg de onderstaande stappen als je niet weet hoe je een configuratiebestand verkrijgt.

Neem voor verdere hulp contact op met de ondersteuning van je serviceprovider als deze hieronder niet wordt vermeld.

??? "NordVPN"
    ### NordVPN {#nordvpn}

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Login to your NordVPN account**

        Meld je aan op de [officiële website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} en ga naar het Nord Account Dashboard. Daar vind je de servicegegevens.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_login.png){class="glboxshadow"}

        Klik na het aanmelden bij het Nord-dashboard links op NordVPN en daarna op **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Zoek de **Service credentials** en kopieer deze voor het uploaden van configuraties.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Choose a NordVPN server and download the configuration file**

        Open het tabblad **Server recommendation**. Op basis van je netwerk wordt een server aanbevolen en kun je beschikbare protocollen downloaden. Klik op **Get setup configuration** om door te gaan.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_config_download.png){class="glboxshadow"}

        Selecteer in het pop-upvenster het protocol **OpenVPN** en download de UDP- of TCP-configuratie.

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Je kunt [hier](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip) de configuraties van alle servers downloaden.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Je kunt NordVPN ook instellen via de [mobiele app](../faq/mobile_app.md).

??? "AirVPN"
    ### AirVPN {#airvpn}

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Login your AirVPN account

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Kies links Config Generator en selecteer Linux als besturingssysteem. Kies daarna de gewenste server.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. De downloadpagina van het configuratiebestand wordt weergegeven.

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

    Meld je aan bij het [Dashboard](https://users.bolehvpn.net/){target="_blank"}, download je configuratiebestanden en selecteer de indeling [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Pak de zipbestanden na het downloaden uit.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

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

    2. Selecteer "**VPN**" in het linkermenu, klik op "**Configure Device**" en maak de serverconfiguratie zoals hieronder beschreven:

        ![config device](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Now create your server configuration, as described below:

        * **Protocol** : **OpenVPN**
        * **Country**: omdat een native protocolverbinding slechts met één server kan worden gebruikt, kies je het land van waaruit je wilt surfen. CyberGhost selecteert automatisch een server in dit land.
        * **Server group**: kies de servergroep en het OpenVPN-protocol, UDP of TCP, dat je wilt gebruiken.

        **OpenVPN UDP** biedt een hogere snelheid dan de TCP-versie, maar kan in sommige gevallen leiden tot mislukte downloads. Dit is de standaardinstelling.

        **OpenVPN TCP** biedt stabielere verbindingen dan de UDP-versie, maar is iets trager. Kies deze versie als de verbinding regelmatig onverwacht wordt verbroken.

        Sla de gekozen parameters op met **Save Configuration**.

    4. Klik op **View Configuration** om de **OpenVPN**-aanmeldgegevens te bekijken die in het configuratiedashboard voor je zijn gegenereerd.

        ![view configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Let na het instellen van je verbindingsvoorkeuren op het volgende:

        * **Server Group**: dit is het adres van het land of de server waarmee je verbinding wilt maken, bijvoorbeeld '12345-1-ca.cg-dialup.net'. Het adres verschilt per land dat je in de vorige stap kiest. CyberGhost selecteert automatisch de specifieke server.
        * **Username**: een gebruikersnaam die alleen voor dit protocol is gegenereerd. Dit is NIET de normale gebruikersnaam van je CyberGhost-account en wordt alleen gebruikt voor verificatie bij CyberGhost-servers via Manual Configurations. Je hebt deze nodig om OpenVPN op GL.iNet-routers in te stellen.
        * **Password**: een wachtwoord dat alleen voor dit protocol is gegenereerd. Dit is NIET het normale wachtwoord van je CyberGhost-account en wordt alleen gebruikt voor verificatie bij CyberGhost-servers via Manual Configurations. Je hebt dit nodig om OpenVPN op GL.iNet-routers in te stellen.

        Download daarna het configuratiebestand. Klik hiervoor op *Download Configuration* en sla het bestand op je computer op.

        ![save config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN {#expressvpn}

    [Official Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"} | [Get 30 days free](https://www.expressvpn.com/refer-a-friend/30-days-free?referrer_id=97477587){rel="sponsored" target="_blank"}

    1. Ga naar de website van [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} en meld je aan met je ExpressVPN-gegevens.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Voer de verificatiecode in** die naar je e-mailadres is verzonden.

    2. Klik in de linkernavigatiebalk op **Set up your devices**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. Vouw onder **Applications** de optie **Advanced setup** uit en klik op **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. Je ziet je **username**, **password** en een lijst met **OpenVPN configuration files**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Klik op de gewenste locatie(s) om de .ovpn-bestanden te downloaden.

        **Houd dit browservenster geopend**. Je hebt deze informatie later tijdens de installatie nodig.

    [Refer link](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN {#fastestvpn}

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Download [hier](https://support.fastestvpn.com/download/fastestvpn_ovpn/) de FastestVPN-configuratiebestanden voor OpenVPN TCP en UDP als zipbestand.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN {#finchvpn}

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. Login your FinchVPN account.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Ga naar de downloadpagina en klik onder FinchVPN OpenVPN Config op Download.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Choose Linux

        ![finchvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Kies het gewenste protocol. Gewoonlijk kun je de eerste optie kiezen: **Port 8484 over UDP**.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Schakel het selectievakje in om je gebruikersnaam en wachtwoord op te nemen voordat je het bestand downloadt.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN {#hideipvpn}

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. Login your HideIPVPN account.

    2. Ga links naar Package, klik op je pakket en controleer of het actief is.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. Op het tabblad VPN staan onder VPN Login Details de gebruikersnaam en het wachtwoord voor de OpenVPN-verbinding.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Scroll down to download OpenVPN config files.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Meld je aan bij je Hide.me-account en zoek links Server Locations.

    2. Download de OpenVPN Configuration voor Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield {#hotspot-shield}

    [Official Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Note: The Hotspot Shield Router configuration files are no longer available or supported. The following steps are here for legacy purposes for those that may still have the files installed.**

    1. Ga naar [https://www.hotspotshield.com/](https://www.hotspotshield.com/){target="_blank"} en klik op Account. Meld je aan als daarom wordt gevraagd.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Go to [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router){target="_blank"}

        Open de keuzelijst Select location en kies de virtuele locatie die de router gebruikt. Klik daarna op "Download file". Het configuratiebestand config.ovpn wordt naar je computer gedownload. Voer de gebruikersnaam en het wachtwoord in wanneer je de OpenVPN-client op de router instelt.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Refer link](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router){target="_blank"}

??? "IPVANISH"
    ### IPVANISH {#ipvanish}

    [Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Je kunt [hier](https://configs.ipvanish.com/configs/configs.zip) de configuratiebestanden voor alle servers downloaden. Het pakket bevat alle serverconfiguraties (.ovpn) en een certificaatbestand (.crt). Het .zip-bestand kan voor sommige modellen te groot zijn. Verwijder daarom de configuraties van servers die je niet gebruikt.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Je kunt [hier](https://www.ipvanish.com/software/configs/){target="_blank"} ook afzonderlijke serverconfiguraties downloaden, maar je moet daarnaast **ca.ipvanish.com.crt** downloaden. Pak **ca.ipvanish.com.crt** en de .ovpn-configuratiebestanden vóór het uploaden naar de router samen in een .zip-archief.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup){target="_blank"}

??? "IVACY"
    ### IVACY {#ivacy}

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    Voor het instellen van een OpenVPN-client met Ivacy heb je het volgende nodig:

    - Je gebruikersnaam voor de handmatige OpenVPN-configuratie, weergegeven in het venster "Download Configuration"
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Je wachtwoord, hetzelfde wachtwoord waarmee je je bij je Ivacy-account aanmeldt
    - An OpenVPN configuration file

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/){target="_blank"}

??? "IVPN"
    ### IVPN {#ivpn}

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Download the [OpenVPN config files](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Find the Account ID on [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Wanneer je het configuratiebestand naar Add a New OpenVPN Configuration sleept, wordt om User Name en Password gevraagd. De User Name is je Account ID dat begint met **ivpn**. Het wachtwoord mag een willekeurige waarde zijn, bijvoorbeeld **ivpn**.

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html){target="_blank"}

??? "OVPN"
    ### OVPN {#ovpn}

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    Meld je aan en klik op het onderstaande menu om het OpenVPN-configuratiebestand op te halen.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Kies de server en download het bestand.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    De gebruikersnaam en het wachtwoord zijn dezelfde gegevens waarmee je je bij OVPN aanmeldt.

??? "OysterVPN"
    ### OysterVPN {#oystervpn}

    [Official Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Open [de OysterVPN-serverlijst](https://support.oystervpn.com/server-list/){target="_blank"} en klik op **Download .ovpn file** om het configuratiebestand te downloaden.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. De gebruikersnaam en het wachtwoord voor de OpenVPN-verbinding zijn dezelfde gegevens waarmee je je bij OysterVPN aanmeldt.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

??? "PIA (Private Internet Access)"
    ### PIA {#pia}

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Download](https://www.privateinternetaccess.com/openvpn/openvpn.zip) directly.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Meld je aan. Daarna vind je eenvoudig **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank"} directly.

    [Hier](https://privatevpn.com/client/PrivateVPN-TUN.zip) staat de officiële downloadlink. Door een fout bij het importeren op de router bevatte een bestandsnaam de speciale tekens in 'Bogotá'. We hebben het bestand hernoemd en de downloadlink hierboven geplaatst. Deze fout wordt in een toekomstige versie opgelost.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN has WireGuard service, we recommend to use WireGuard, checkout [here](wireguard_client.md)**.

    1. Login your [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} account.

    2. Klik links op **Download**.

    3. Choose Router platform, protocol etc, find your target country to download configuration file.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. De gegevens voor de OpenVPN-verbinding zijn niet dezelfde als die voor het Proton-dashboard. Je vindt de juiste gegevens onder **Account -> OpenVPN/IKEv2 username**.

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN {#purevpn}

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Voor het instellen van een OpenVPN-client met PureVPN heb je je OpenVPN-gebruikersnaam, wachtwoord en een configuratiebestand nodig. Je vindt deze in je PureVPN-account.

    1. [Sign in to your PureVPN account.](https://my.purevpn.com/){target="_blank"}
    2. Klik in de linkerzijbalk op **Subscriptions**.
    3. Scrol omlaag naar je OpenVPN-gebruikersnaam en -wachtwoord.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. Klik in de linkerzijbalk op **Manual Configuration**.
    5. Selecteer een VPN-locatie en klik op **Download** om het configuratiebestand te downloaden.

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

    StarVPN biedt een VPN-dienst met de protocollen OpenVPN en WireGuard. We raden WireGuard aan omdat dit doorgaans sneller is dan OpenVPN. Raadpleeg [deze informatie](wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    Volg de onderstaande stappen om het configuratiebestand te downloaden als je liever het OpenVPN-protocol gebruikt.

    1. **Register an account with StarVPN**

        Ga naar de [abonnementsopties](https://www.starvpn.com/#pricing){target="_blank"} en kies een VPN-abonnement dat bij je past. Je kunt je tijdens het afrekenen of rechtstreeks [hier](https://www.starvpn.com/dashboard/register.php){target="_blank"} registreren.

    2. **Download OpenVPN Configuration**

        Meld je aan bij het [dashboard](https://www.starvpn.com/dashboard){target="_blank"} voor StarVPN-leden. Zoek op het dashboard het gedeelte **VPN Configuration** en klik op **OpenVPN Config**. Kopieer de OVPN-gebruikersnaam en het wachtwoord. Je hebt deze nodig voor verificatie wanneer je het bestand naar je GL.iNet-router uploadt.

        ![download starvpn ovpn config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/ovpnconfigdl.png){class="glboxshadow"}

        Select UDP or TCP and download a configuration file.

        ![select udp or tcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/udp_tcp.png){class="glboxshadow"}

    3. **Edit configuration file**

        Sommige GL.iNet-routers ondersteunen IPv6 niet. Open het .ovpn-configuratiebestand en verwijder de IPv6-gerelateerde inhoud zoals hieronder weergegeven om compatibiliteits- en verbindingsproblemen te voorkomen.

        ![remove ipv6](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/remove_ipv6.png){class="glboxshadow"}

??? "StreamVPN"
    ### StreamVPN {#streamvpn}

    [Official Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Meld je aan bij je [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}-account om je abonnementsgegevens te bekijken. Klik op **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Click **VPN Router**, it will download a .zip archive file called `StreamVPN.zip`.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Note:** Only the configuration file name contains "Primary" work.

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Meld je aan bij je [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}-account om VPN Accounts Summary te bekijken. Klik op **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Find the Manual setup section, follow the steps to get configuration.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark {#surfshark}

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Find your login details**

        De Surfshark-servicegegevens verschillen van de gegevens van je Surfshark-account, namelijk je e-mailadres en wachtwoord. Je hebt de Surfshark-servicegegevens nodig om via de handmatige OpenVPN-configuratie van de router verbinding met de VPN te maken.

        Meld je aan op de [officiële website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} en ga naar [deze pagina](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}. Daar vind je alle gegevens voor een handmatige verbinding.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Choose a Surfshark server**

        Open het tabblad **Locations**. Daar zie je alle Surfshark-servers.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        It will ask to choose TCP or UDP. Click [here](../faq/openvpn_tcp_udp.md) to see the difference.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    Je kunt alle configuraties rechtstreeks [hier](https://api.surfshark.com/v1/server/configurations) downloaden.

    Tip: als het zipbestand te groot is om te uploaden, verwijder je enkele .ovpn-bestanden uit het .zip-bestand of upload je één .ovpn-bestand.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac download configuration" src="https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate {#vpngate}

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    De OpenVPN-configuratiebestanden staan op de [VPN Gate-website](https://www.vpngate.net/en/) gerangschikt op serverlocatie.

    1. Klik in de kolom **OpenVPN** op OpenVPN Config file.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. De downloadpagina wordt weergegeven.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Safe"
    ### VPN Safe {#vpn-safe}

    [Officiële website](https://secure.vpnsafe.net/aff.php?aff=6){target="_blank"}

    1. Meld je aan bij het **VPN Safe Dashboard** en klik op je actieve VPN-dienst.

        ![vpnsafe1](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe1.png){class="glboxshadow"}

    2. Scrol op de pagina Product Details naar **OpenVPN Configuration**.

        ![vpnsafe2](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe2.png){class="glboxshadow"}

        ![vpnsafe3](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe3.png){class="glboxshadow"}

    3. Klik op **UDP Configs** (aanbevolen) of **TCP Configs** om alle UDP/TCP-configuraties als ZIP-archief te downloaden. Pak het archief uit om alle beschikbare configuratiebestanden te krijgen.

        ![vpnsafe4](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe4.jpg){class="glboxshadow"}

    4. Klik op **UDP Servers** (aanbevolen) of **TCP Servers** om een URL-lijst van alle beschikbare UDP/TCP-servers te krijgen.

        ![vpnsafe5](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe5.jpg){class="glboxshadow"}

    5. Selecteer in de vervolgkeuzelijst de server waarmee je verbinding wilt maken en klik op **Download UDP/TCP Config** om één UDP/TCP-configuratie te downloaden.

        ![vpnsafe6](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe6.jpg){class="glboxshadow"}

        ![vpnsafe7](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnsafe/vpnsafe7.jpg){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Information quoted from [VPN unlimited official instruction](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Meld je eerst aan bij je User Office, klik bij de dienst VPN Unlimited op Manage en volg deze stappen:

    1. Select a device

        Kies een apparaat uit de lijst of maak een nieuw apparaat. Verwijder een oud apparaat of koop extra plaatsen als je geen vrije plaatsen meer hebt.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Choose the desired server location

        VPN Unlimited biedt meer dan 400 servers op meer dan 70 locaties. In dit voorbeeld kiezen we Duitsland.

    3. Select the VPN protocol

        select OpenVPN protocol.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Create a configuration

        Klik op Generate om alle gegevens voor het instellen van een VPN-verbinding te verkrijgen.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN {#vyprvpn}

    VyprVPN offers the OpenVPN files here: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    Het geleverde zipbestand bevat twee mappen met .ovpn-bestanden: OpenVPN160 en OpenVPN256. Verwijder de map OpenVPN160 uit het zipbestand en upload het daarna zoals gewoonlijk naar de GL.iNet-router.

??? "Windscribe"
    ### Windscribe {#windscribe}

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Log in to your Windscribe membership account [here](https://windscribe.com/login?auth_required){target="_blank"}, then access the [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}.

    2. Selecteer de gewenste serverlocatie, het protocol UDP of TCP, de poort, bijvoorbeeld 1194, en de OpenVPN-versie, bij voorkeur de nieuwste. Klik vervolgens op **Download Config**. Er wordt een bestand met de extensie ".ovpn" naar je lokale apparaat gedownload.

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Klik op dezelfde pagina op **Get Credentials**. Je krijgt de bijbehorende aanmeldgegevens. Deze worden later in het webbeheerpaneel van de router gebruikt voor verificatie wanneer je het configuratiebestand uploadt. Kopieer de gegevens of houd deze webpagina geopend.

    4. Then follow [this guide](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers) to continue.

??? "ZoogVPN"
    ### ZoogVPN {#zoogvpn}

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Meld je aan op de [officiële website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"} en open daarna de [pagina met OpenVPN-configuratiebestanden](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}. Daar vind je alle servers. Download het configuratiebestand in de kolom TCP of UDP.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Volg daarna de [handleiding voor het instellen van OpenVPN Client op een GL.iNet-router](#set-up-openvpn-client-manually-for-other-providers). De gebruikersnaam en het wachtwoord zijn dezelfde gegevens waarmee je je op de ZoogVPN-website aanmeldt.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
