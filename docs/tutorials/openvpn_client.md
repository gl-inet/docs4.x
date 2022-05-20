# OpenVPN Client

OpenVPN is an open-source VPN protocol that makes use of virtual private network (VPN) techniques to establish safe site-to-site or point-to-point connections. 

GL.iNet routers have pre-installed OpenVPN Client and Server.

We recommend WireGuard over OpenVPN because it is much faster. For setup a WireGuard Client, please check out [here](../wireguard_client).

If you have already bought OpenVPN service from a provider, but you don't know how to get the configuration file, please refer to [get configuration files from OpenVPN service providers](#get-configuration-files-from-openvpn-service-providers).

You can setup OpenVPN Client via web Admin Panel and [mobile app](../mobile_app). For the mobile app, it has already integrated NordVPN.

## Setup NordVPN

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is the top online VPN service for speed and security.

From firmware 4.0.0, it has integrated NordVPN OpenVPN service.

1. Input your credential, then click **Save Credentials & Get Servers**

    ![input nordvpn credential](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/input_nordvpn_credential.png){class="glboxshadow"}

2. Select protocol, max server count of each location, locations, then click **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/select_nordvpn_servers.png){class="glboxshadow"}

    It will download configuration files.

    ![downloaded configuration files](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/downloaded_configs.png){class="glboxshadow"}

3. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard page](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/vpn_dashboard_to_connect.png){class="glboxshadow"}

    Toggle the switch to enable the connection.

    ![openvpn connected](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/openvpn_connected.png){class="glboxshadow"}

4. Update servers

    NordVPN may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![update servers](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/update_servers.png){class="glboxshadow"}

5. Edit credential

    Click the cog icon to edit the credential.

    ![edit credential](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/edit_credential.png){class="glboxshadow"}

## Setup OpenVPN client

As of frimware 4.0, it brings grouping to manage OpenVPN profiles. Please make sure all the profiles in the same group with the same credentials. For example, if you are ExpressVPN user, you can add a group named expressvpn, then upload all the ExpressVPN OpenVPN profiles you wanted to this group. For another OpenVPN service provider, please create another group.

Next steps, we will use ExpressVPN as an example.

1. Add a new group

    ![add a new group](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/add_a_new_group.png){class="glboxshadow"}

2. Give the group a descriptive name, e.g. expressvpn.

    ![set the new group name](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/set_new_group_name.png){class="glboxshadow"}

3. Upload your OpenVPN configuration file, then input the credential, click **Apply**.

    ![upload profile](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/upload_profile.png){class="glboxshadow"}

    ![after upload profile](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/after_upload_profile.png){class="glboxshadow"}

4. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard page](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/vpn_dashboard_to_connect_expressvpn.png){class="glboxshadow"}

## Setup OpenVPN server on GL.iNet router

You can get a GL.iNet router to set as OpenVPN server, and get another GL.iNet router to set as OpenVPN client. For setup OpenVPN server, please check out [here](../openvpn_server).

## Get configuration files from OpenVPN service providers

We have tested different OpenVPN service providers. Therefore, if you don't know how to get the configuration file, you can follow the instruction below. However, you have to contact your service provider for the configuration file if they are not listed below. 

If you have any problem in the setup of OpenVPN, please contact [support@gl-inet.com](mailto:support@gl-inet.com)

Recommended:

??? "NordVPN"

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    Download OpenVPN client configuration files. We recommend going into [NordVPN recommended server utility here](https://nordvpn.com/servers/tools/){target="_blank"}. It will recommend a server base on your network, click <code>Show available protocols</code> to download the UDP or TCP config.

    ![nordvpn server utility](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/nordvpn/nordvpn_server_utility.png){class="glboxshadow"}

    Of course you can download all servers configs [here](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Tips: if the zip file is too big to upload, you can delete some .ovpn in .zip file or upload single .ovpn file.

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    You can also use [mobile app](../mobile_app) to setup NordVPN.

??? "PIA (Private Internet Access)"

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Download](https://www.privateinternetaccess.com/openvpn/openvpn.zip) directly.

??? "Surfshark"

    [Official Website](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}

    Login and [Download](https://api.surfshark.com/v1/server/configurations) directly, or read this [guide](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-).

??? "PureVPN"

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    [Download](https://d32d3g1fvkpl8y.cloudfront.net/heartbleed/router/Recommended-CA2.zip) directly.

    [Refer link](https://support.purevpn.com/openvpn-files)

??? "TorGuard"

    [Official Website](https://torguard.net/aff.php?aff=3040){target="_blank"}

    1. If you are using [TorGuard](https://torguard.net/aff.php?aff=3040){target="_blank"}, you need to login the control panel and find **Config Generator** from the **Tools** menu. Choose the **VPN Server** and some other options. Then click **Generate Config** a config file will be downloaded automatically.

        ![Generate ovpn](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/torguard/torguard_menu.jpg){class="glboxshadow"}

    2. The username and password for OpenVPN connection is different from your control panel login. You can find the VPN username and VPN password below.

        ![torguard vpn username vpn password](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/torguard/torguard_vpnusername_vpnpassword.png){class="glboxshadow"}

??? "PrivateVPN"

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://privatevpn.com/client/PrivateVPN-TUN.zip) directly.

??? "Proton VPN"

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN has WireGuard service, we recommend to use WireGuard, checkout [here](../wireguard_client/#wireguard-providers)**.

    1. Login your [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} account.

    2. Click **Download** in the left-hand side.

    3. Choose Router platform, protocol etc, find your target country to download configuration file.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. The credential for connect OpenVPN is not the one that login Proton website's dashboard. You can find the crdential at **Account -> OpenVPN/IKEv2 username**

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "ExpressVPN"

    [Official Website](https://www.xvbelink.com/?a_fid=glinet){target="_blank"}

    Information quoted from [Expressvpn official instruction](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Go to [ExpressVPN](https://www.xvbelink.com/?a_fid=glinet){rel="sponsored" target="_blank"} website, and log in with your ExpressVPN credentials.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Enter the verification code** that is sent to your email.

    2. On the right, with **OpenVPN** already selected for you, you will see your **username**, **password**, and a list of **OpenVPN configuration files**.

        ![](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-manual-configuation-openvpn.jpg){class="glboxshadow"}

        Click the location(s) you want in order to download the .ovpn file(s).

        **Keep this browser window open**. You will need this information for the setup later.

Others:

??? "AirVPN"

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Login your AirVPN acoount

        ![airvpn client detail](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Choose Config Generator on the left and then choose Linux as your operating system. Next, choose your preferred server.

        ![openvpn config generator](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. You will be able to see the download page of the configuration file.

        ![download config](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Information quoted from [Astrill official instruction](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Generate and Download Astrill Openvpn configuration ZIP

        ![astrill vpn tools](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Type a Description like OPENVPN_GUI.

    3. Click on ADD to my certificates button.

        ![create new certificate](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Once OpenVPN certificate is added, click on Download button.

        ![download certificate](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "bolehvpn"

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

    Login in [Dashboard](https://users.bolehvpn.net/){target="_blank"}, download your configuration files and select the [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"} format. Extract the zip files after completing the download.

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Download](https://www.cactusvpn.com/downloads/){target="_blank"} directly.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [Download](https://cryptostorm.is/configs/ecc/){target="_blank"} directly.

??? "CyberGhost"

    [Official Website](https://support.cyberghostvpn.com/hc/en-us){target="_blank"}

    Information quoted from [CyberGhost official instruction](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers?fbclid=IwAR0_IicBlnNzVqlKh0mAHFyM6uvsGgBQooYfMyJ0bHgb13Eidn8KhXnd6Y0){target="_blank"}

    1. Login your CyberGhost VPN online account.

        ![login](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Click on **My Devices**  > click **Other** > choose **Configure new device**.

        ![config new device](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.png){class="glboxshadow"}

    3. At the new screen, in the **Server configuration** tab, the desired parameters can be configured. For the purpose of setting OpenVPN for your DD-WRT Router, choose 'OpenVPN' from the Protocol drop down menu. Your desired country and server group, as described below, need to be defined too:

        ![](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.png){class="glboxshadow"}

        - Protocol: For Router configurations, please choose OpenVPN

        - Country: Since native protocol connections may only be used with exactly one server you now have to choose the country you want to surf from; the server to be used in this country will be chosen by CyberGhost automatically.

        - Server group: Choose the server group and the OpenVPN protocol (UDP or TCP) you want to use:

            UDP allows higher speed than the TCP version, but can result in broken downloads in some cases. This is the default setting.

            TCP allows more stable connections than the UDP version, but is a bit slower. Choose this version, if you have recurrent connection issues such as sudden disconnections.

        After setting up your preferred settings, save them with **Save and download configuration**.

??? "FastestVPN"

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Download FastestVPN Config Files zip folder for OpenVPN TCP and UDP from [here](https://support.fastestvpn.com/download/openvpn-tcp-udp-config-files/)

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. Login your FinchVPN account.

        ![finchvpn login](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Go to the Download page and click Download under FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Choose Linux

        ![finchvpn](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Choose the protocol based on your preference. Generally, you can choose the first one **Port 8484 over UDP**

        ![finchvpn](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Remember to tick the box to include your username and password before download the file.

        ![finchvpn](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. Login your HideIPVPN account.

    2. Go to Package on the left side, click the your package, make sure it is active.

        ![hideipvpn client area](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. On the VPN tab, there is VPN Login Details of username and password, this is for login when OpenVPN connection

        ![hideipvpn client area](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Scroll down to download OpenVPN config files.

        ![hideipvpn client area](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Login your Hide.me account, find the Server Locations on the left side.

    2. Download the OpenVPN Configuration for Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "HideMyAss"

    [Official Website](https://click.hmavpn.com/aff_c?offer_id=1&aff_id=861){target="_blank"}

    [Download](https://vpn.hidemyass.com/vpn-config/vpn-configs.zip)

??? "IPVANISH"

    [Official Website](https://www.ipvanish.com/){target="_blank"}

    You can download all of the config files for all of the servers from [here](https://www.ipvanish.com/software/configs/configs.zip), then should upload this **config.zip** on the OpenVPN Client of web Admin Panel. Before uploading, please remove the servers in the .zip file that you will not use to reduce the file size.

    You can also download individual server configuration files [here](https://www.ipvanish.com/software/configs/), but you will need to download **ca.ipvanish.com.crt** as well. Before uploading to the router, you need to compress the **ca.ipvanish.com.crt** and .ovpn configuration files into a .zip archive and upload them.

    ![ipvanish](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/ipvanish/ipvanish_download_openvpn_configs.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    [Download OpenVPN UDP Configs](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/ivacy/IVACY_OpenVPN_Configs_UDP.zip)

    [Download OpenVPN TCP Configs](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/ivacy/IVACY_OpenVPN_Configs_TCP.zip)

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Download the [OpenVPN config files](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Find the Account ID on [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. When drag the config file to Add a New OpenVPN Configuration, you will be asked to enter User Name and Password. The User Name is your Account ID that begins with letters **ivpn**. The password can be anything, like **ivpn**

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "OVPN"

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}
    
    Just login, then you can easy get the OpenVPN configurations file by click the menu below.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Choose the server and download.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    The username and password are the same you login OVPN.

