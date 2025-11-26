# How to Set Up OpenVPN Client on GL.iNet Router

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

OpenVPN is an open-source VPN protocol that makes use of virtual private network (VPN) techniques to establish safe site-to-site or point-to-point connections. 

We recommend WireGuard over OpenVPN because it is much faster. For setting up a WireGuard Client, please check [here](wireguard_client.md).

Before you start, ensure you have an active subscription with a VPN service provider that supports OpenVPN manual configuration. Click [here](https://www.gl-inet.com/solutions/vpn/){target="_blank"} to check the OpenVPN providers compatible with GL.iNet.

Generally, you need to visit the official website of the VPN service provider you subscribed first, obtain the configuration file, and upload it to the router to set it as OpenVPN Client. If you don't know how to get the configuration file, refer to [this link](#get-configuration-files-from-openvpn-service-providers) or ask their support.

You can set up your GL.iNet router as OpenVPN client through the web admin panel or [mobile app](../faq/mobile_app.md). This article focuses on setting up OpenVPN client through the web admin panel.

In the web Admin Panel, navigate to **VPN** -> **OpenVPN Client**. 

Click the **NordVPN** button to log in if you have a NordVPN subscription, or click **Add Manually** to upload the OpenVPN configuration files.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Set Up NordVPN

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is a popular online VPN service for speed and security.

NordVPN quick setup is integrated into the admin panel of GL.iNet routers. You can acquire configuration files for all NordVPN servers online by entering your account credentials (obtained from the NordVPN Dashboard) in the router's web admin panel or mobile app, eliminating the need for manual file uploads.

1. Log in to your NordVPN web account [here](https://my.nordaccount.com/){target="_blank"}.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

    After login, on the Nord Dashboard, click **NordVPN**, then click **Set up NordVPN manually**.

    ![nord dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    You will find the **service credentials**. Copy them for later use.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Log in to your router's web admin panel, navigate to VPN -> OpenVPN Client -> NordVPN. Input the **service credentials** obtained in step 1 (Note: It is **NOT** the login account email/password), then click **Save and Continue**.
   
    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Select protocol, max server count of each location and locations, then click **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

    It will download configuration files.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Start a connection.

    Select a preferred server, and click the three-dot icon on the right to start a connection.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Once connected, a green dot will appear next to the configuration file.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Edit credentials.

    Click the gear icon to edit your login credentials.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Delete all files.

    You can click **Delete All** to delete all configuration files with one click.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Set Up OpenVPN Client Manually (for other providers)

If your OpenVPN service provider is not integrated into our admin panel, please first visit the official website of your subscribed service provider to obtain the configuration file. Next, upload it to the router to set up an OpenVPN client.

In the following steps, we will use [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} as an example.

1. Download a configuration file from Private Internet Access official website.

2. Log in to your router's web admin panel, navigate to VPN -> OpenVPN Client, and click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. It will create a group on the left sidebar.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. Set a descriptive name for the group (e.g., private internet access).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. Upload your OpenVPN configuration file. Input the credentials if required, then click **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}

    - There are 4 types of credentials for authentication:

        1. No authentication.
        
        2. Username and Password only. 
        
        3. Passphrase only.

        4. Username, Password, and Passphrase.

    Then you will see the configuration file uploaded.
     
    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. Click the three-dot icon on the right to start a connection.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. Once connected, a green dot will appear next to the configuration file.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## Set Up OpenVPN Server on GL.iNet Router

If you have two GL.iNet routers, you may consider setting one as an OpenVPN server (a public IP is required), and the other as an OpenVPN client. In this way, you can establish your own VPN connection without subscribing to third-party VPN services.

For setting up OpenVPN server, please check [here](openvpn_server.md).

## Get Configuration Files from OpenVPN Service Providers

We have tested 30+ OpenVPN service providers and documented the steps to obtain configuration files. If you are unsure how to get the configuration file, please refer to the steps below.

If the service provider you subscribed to is not listed below, please contact their support for further assistance.

??? "NordVPN"
    ### NordVPN

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Login to your NordVPN account**

        Log in to the [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}, go to the Nord Account Dashboard, where you will find the service credentials.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        After login to Nord dashboard, click NordVPN on the left side, then click **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Find the **Service credentials**. Copy them in case you need to use them for configuration uploads.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Choose a NordVPN server and download the configuration file**

        Go to **Server recommendation** tab. It will recommend a server base on your network and provide available protocols for you to download. Click on **Get setup configuration** to continue.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        In the pop-up window, select **OpenVPN** protocol and download UDP or TCP config. 

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    You can download all servers configs [here](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    You can also use [mobile app](../faq/mobile_app.md) to setup NordVPN.

??? "AirVPN"
    ### AirVPN

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Login your AirVPN acoount

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Choose Config Generator on the left and then choose Linux as your operating system. Next, choose your preferred server.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. You will be able to see the download page of the configuration file.

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Information quoted from [Astrill official instruction](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Generate and Download Astrill Openvpn configuration ZIP

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Type a Description like OPENVPN_GUI.

    3. Click on ADD to my certificates button.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Once OpenVPN certificate is added, click on Download button.

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

    Login in [Dashboard](https://users.bolehvpn.net/){target="_blank"}, download your configuration files and select the [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"} format. Extract the zip files after completing the download.

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Download](https://www.cactusvpn.com/downloads/){target="_blank"} directly.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [Download](https://cryptostorm.is/configs/ecc/){target="_blank"} directly.

??? "CyberGhost"
    ### CyberGhost

    [Official Website](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Information quoted from [CyberGhost official instruction](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Login your CyberGhost VPN online account.

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Select "**VPN**" from the left-side menu, then click "**Configure Device**" and create your server configuration, as described below:

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Now create your server configuration, as described below:

        * **Protocol** : **OpenVPN**
        * **Country** : Since native protocol connections may only be used with exactly one server you now have to choose the country you want to surf from; the server to be used in this country will be chosen by CyberGhost automatically.
        * **Server group** : Choose the server group and the OpenVPN protocol (UDP or TCP) you want to use

        **OpenVPN UDP** allows higher speed than the TCP version but can result in broken downloads in some cases. This is the default setting.
        
        **OpenVPN TCP** allows more stable connections than the UDP version but is a bit slower. Choose this version, if you have recurrent connection issues such as sudden disconnections.

        Once the desired parameters are chosen, save them with **Save Configuration**

    4. To view the **OpenVPN** credentials that are generated for you on the configuration dashboard, press **View Configuration**.

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. After setting up your connection preferences, please take note of the following:

        * **Server Group** : This is the address of the country (server) you want to be connected with, e.g. '12345-1-ca.cg-dialup.net'. This address changes with every country you have chosen in the step before. The actual single server to be used will be chosen automatically by CyberGhost.
        * **Username** : A solely for this protocol generated user name. This is NOT your regular CyberGhost account user name, it's used only to authenticate with CyberGhost servers via Manual Configurations. You will need this when set up OpenVPN on GL.iNet routers.
        * **Password** : A solely for protocol usage generated password. This is NOT your regular CyberGhost account password, it's used only to authenticate with CyberGhost servers via Manual Configurations. You will need this when set up OpenVPN on GL.iNet routers.

        Once done, please download the configuration file. For that click on *Download Configuration* and download the config file to your computer

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN

    [Official Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    Information quoted from [Expressvpn official instruction](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Go to [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} website, and log in with your ExpressVPN credentials.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Enter the verification code** that is sent to your email.

    2. In the "Set up your devices" section, click on **More**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3.  Click on **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4.  You will see your **username**, **password**, and a list of **OpenVPN configuration files**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Click the location(s) you want in order to download the .ovpn file(s).

        **Keep this browser window open**. You will need this information for the setup later.

    [Refer link](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Download FastestVPN config files zip folder for OpenVPN TCP and UDP from [here](https://support.fastestvpn.com/download/fastestvpn_ovpn/)

    Tips: If the zip file is too large to upload, delete some .ovpn files in the .zip folder, or upload a single .ovpn file.

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. Login your FinchVPN account.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Go to the Download page and click Download under FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Choose Linux

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Choose the protocol based on your preference. Generally, you can choose the first one **Port 8484 over UDP**

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Remember to tick the box to include your username and password before download the file.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. Login your HideIPVPN account.

    2. Go to Package on the left side, click the your package, make sure it is active.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. On the VPN tab, there is VPN Login Details of username and password, this is for login when OpenVPN connection

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Scroll down to download OpenVPN config files.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Login your Hide.me account, find the Server Locations on the left side.

    2. Download the OpenVPN Configuration for Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [Official Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Note: The Hotspot Shield Router configuration files are no longer available or supported. The following steps are here for legacy purposes for those that may still have the files installed.**

    1. Go to [https://www.hotspotshield.com/](https://www.hotspotshield.com/) and click on Account. Sign in if you're asked.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Go to [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router)

        Go to the Select location dropdown and pick the virtual location that the router will use. Now click on "Download file". The configuration file (config.ovpn) will be downloaded to your computer. The username and password will need to be entered when you set up the OpenVPN client on the router.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Refer link](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - You can download all of the config files for all of the servers from [here](https://configs.ipvanish.com/configs/configs.zip), it contain all the server config file(.ovpn) and a certificate file(.crt). The .zip file maybe a little big for some models, please delete the configuration(.ovpn) of the server that you will not use.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - You can also download individual server configuration files [here](https://www.ipvanish.com/software/configs/), but you will need to download **ca.ipvanish.com.crt** as well. Before uploading to the router, you need to compress the **ca.ipvanish.com.crt** and .ovpn configuration files into a .zip archive.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    To set up an OpenVPN client using Ivacy, you will need the following: 

    - Your username for the OpenVPN manual configuration, shown in the "Download Configuration" prompt
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Your password (same as the one you used to sign in to your Ivacy account)
    - An OpenVPN configuration file

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Download the [OpenVPN config files](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Find the Account ID on [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. When drag the config file to Add a New OpenVPN Configuration, you will be asked to enter User Name and Password. The User Name is your Account ID that begins with letters **ivpn**. The password can be anything, like **ivpn**

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad"
    ### Mullvad

    [Official Website](https://mullvad.net/en){target="_blank"}

    1. Go to [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"} website, and log in with your Mullvad credentials.

    2. Choose OpenVPN Configuration

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. Choose **Linux** and select your server location

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}
    
    Just login, then you can easily get the OpenVPN configurations file by click the menu below.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Choose the server and download.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    The username and password are the same you login OVPN.

??? "OysterVPN"
    ### OysterVPN

    [Official Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Access [the OysterVPN server list page](https://support.oystervpn.com/server-list/){target="_blank"}, click **Download .ovpn file** to download the configuration file.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. The username and password for OpenVPN connection are the same as the one you use to login OysterVPN.

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

??? "PIA (Private Internet Access)"
    ### PIA

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Download](https://www.privateinternetaccess.com/openvpn/openvpn.zip) directly.

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Just login, then you can easily find the **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

??? "PrivateVPN"
    ### PrivateVPN

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank} directly.

    [Here](https://privatevpn.com/client/PrivateVPN-TUN.zip) is the official download link. Due to a bug encountered while importing the router, the file name inside contains special characters 'Bogotá'. We have renamed it and provided the download link above. We will fix this bug in future versions.

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

??? "Proton VPN"
    ### Proton VPN

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN has WireGuard service, we recommend to use WireGuard, checkout [here](wireguard_client.md#wireguard-providers)**.

    1. Login your [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} account.

    2. Click **Download** in the left-hand side.

    3. Choose Router platform, protocol etc, find your target country to download configuration file.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. The credential for connect OpenVPN is not the one that login Proton website's dashboard. You can find the crdential at **Account -> OpenVPN/IKEv2 username**

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    To set up an OpenVPN client using PureVPN, you will need your OpenVPN username and password and a configuration file, which you can find in your PureVPN account. 
   
    1. [Sign in to your PureVPN account.](https://my.purevpn.com/)
    2. From the left sidebar, click **Subscriptions**.
    3. Scroll down to find your OpenVPN username and password.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. From the left sidebar, click **Manual Configuration**. 
    5. Select a VPN location and click **Download** to download the configuration file. 

    [Refer link](https://support.purevpn.com/openvpn-files)

    GL.iNet routers don't support the [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"} feature of PureVPN, because it needs PPTP.

??? "SaferVPN"
    ### SaferVPN

    [Official Website](https://safervpn.com/?a_aid=563){target="_blank"}

    [Download](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup) directly.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN has WireGuard service, we recommend to use WireGuard, checkout [here](wireguard_client.md#starvpn).

    1. **Register an account with StarVPN**

        Head on over to their [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} options and choose a VPN plan that suits your needs. You can register on checkout or directly [here](https://www.starvpn.com/dashboard/register.php){target="_blank"}

    2. VPN Login Information

        Log into the StarVPN member area [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. You can find your VPN username and password for each slot in the Manage Slots Section or dashboard area.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_edited-2.jpg){class="glboxshadow"}

        For multiple slots, the VPN configuration settings and credentials can be located in the “Manage Slots” section.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_slots_edited-1024x355.jpeg){class="glboxshadow"}

    3. Download OpenVPN Configuration File

        The next step, you must download the VPN server configuration files necessary so that the OpenVPN Software knows where to connect to.   Download the configuration file in the members area dashboard.

        ![download starvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/download-ovpn_edited.jpg){class="glboxshadow"}

        Some GL.iNet routers do not support IPv6 or DNS Leak Protection, as a result you may experience an IP or connection error. Edit the ovpn configuration file and disable IPv6 by performing these simple tasks.

        ![troubleshooting](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/troubleshooting.jpg){class="glboxshadow"}
        
??? "StreamVPN"
    ### StreamVPN

    [Official Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Login with your [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} account and then you will be able to see your subscription information. Click **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Click **VPN Router**, it will download a .zip archive file called `StreamVPN.zip`.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Note:** Only the configuration file name contains "Primary" work.

??? "StrongVPN"
    ### StrongVPN

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Login with your [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} account and then you will be able to see VPN Accounts Summary. Click **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Find the Manual setup section, follow the steps to get configuration.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Find your login details**

        Surfshark service credentials are different from your Surfshark account credentials, namely your email address and your password. You'll need Surfshark service credentials to connect to the VPN using the manual OpenVPN configuration method in the router.

        Login the [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, go to [this page](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, where you will find all of the details required for a manual connection.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Choose a Surfshark server**

        Select the **Locations** tab, where you will see all of the Surfshark servers.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        It will ask to choose TCP or UDP. Click [here](../faq/openvpn_tcp_udp.md) to see the difference.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    You can download all configs [here](https://api.surfshark.com/v1/server/configurations) directly.

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    The OpenVPN configuration files are listed on the [VPN Gate website](https://www.vpngate.net/en/) according to the server location.

    1. Click OpenVPN Config file under the column **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. You will see the download page.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Information quoted from [VPN unlimited official instruction](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Start out by logging in to your User Office, press Manage for the VPN Unlimited service, and follow a few simple steps:

    1. Select a device

        Pick a device from the list or create a new one. If you are out of free slots, delete an old device or buy extra slots.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Choose the desired server location
    
        VPN Unlimited offers a large variety of servers, namely 400+ in 70+ locations. In this case, let it be Germany.

    3. Select the VPN protocol

        selece OpenVPN protocol.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Create a configuration

        Press Generate and you will get all the data required to set up a VPN connection.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPN offers the OpenVPN files here: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    The provided zip file contains two folders with the .ovpn files. One called OpenVPN160 one OpenVPN256. Just delete the OpenVPN160 folder from the zip file then upload it to GL.iNet router as usual.

??? "Windscribe"
    ### Windscribe

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Log in to your Windscribe membership account [here](https://windscribe.com/login?auth_required){target="_blank"}, then access the [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}. 
    
    2. Select the server location, protocol (UDP/TCP), port (e.g., 1194) you'd like to use, and OpenVPN version (preferably the newer one), then click **Download Config**. You will then get a file with the suffix ".ovpn" downloaded to your local device.

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Click the **Get Credentials** button on the same page. You will then receive the corresponding credentials, which will be used later in the router's web admin panel when uploading the config file to the router for authentication. Copy the credentials or keep this webpage open.

    4. Then follow [this guide](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers) to continue.

??? "ZoogVPN"
    ### ZoogVPN

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Sign in its [official website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}, then access the [OpenVPN configuration files page](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}, you will find all the servers here. Download the configuration file in the TCP column or UDP column.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Then follow the [guide to setup OpenVPN Client on GL.iNet router](#setup-openvpn-client), the username and password are the same as the ones used to log into ZoogVPN website.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
