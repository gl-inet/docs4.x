# How to get configuration files from WireGuard service providers

??? "AzireVPN"
    ### AzireVPN

    [Official Website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Access [AzireVPN official website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} and login, then access the [WireGuard Configuration generator](https://www.azirevpn.com/cfg/wireguard){target="_blank"}

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. At the IP option, please select **IPv4**. Then click **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-azirevpn) to continue.

    4. You can also use [mobile app](../faq/mobile_app.md) to setup AzireVPN.

??? "Hide.me VPN"
    ### Hide.me VPN

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN provides a simple way to use their WireGuard service in GL.iNet router.

    1. [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"} to router.

    2. Copy the install url below, then paste it to the terminal, hit the Enter key. (Right click the mouse will paste it.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. It will start installing, then ask for the username and password. When typing or pasting the password, no change is visible on the terminal, just hit the Enter key after typing.

    4. Once you're done, go to the web Admin Panel and you'll see that a hide.me VPN group has been created with configuration files already in it. Just connect as you would any other configuration file.

    **Note:** The key in the Hide.me VPN configuration file is regenerated before each connection and becomes invalid after disconnection, so copying this configuration file to other devices will not connect successfully.

    [Refer link](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [Official Website](https://mullvad.net/){target="_blank"}

    1. Access [Mullvad Official Website](https://mullvad.net/){target="_blank"} and login, then access the [WireGuard configuration file generator](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}

    2. Then follow [this guide](../interface_guide/wireguard_client.md/#set-up-mullvad) to continue.

    3. You can also use [mobile app](../faq/mobile_app.md) to setup Mullvad.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    It can't downlaod the WireGuard configs from its website, please use [mobile app](../faq/mobile_app.md) to setup PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. If you are using [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, log in then go to [this](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"} page, click on **Router**, and select **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. In the next window, select **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Select **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Once the key has been generatd, select **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Lastly, choose a location you would like to set up, and hit the **download** button next to the location. You will be able to download the configuration files.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-surfshark) to continue.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. If you are using [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, sign in to their website, go to the [Client Area](https://airvpn.org/client/){target="_blank"}, click the [Config Generator](https://airvpn.org/generator/){target="_blank"}

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. At the Config Generator page, select WireGuard at the Protocols sector.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Select a server, then scroll down to the end, click **Generate** button. It will download the configuration file.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "Astrill"
    ### Astrill

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    If you are using [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, please log in then access [this page](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} to generate WireGuard configurations.

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "IVPN"
    ### IVPN

    [Official Website](https://www.ivpn.net/){target="_blank"}

    If you are using [IVPN](https://www.ivpn.net/){target="_blank"}, you need to generate the WireGuard config manually. Follow the guide base on your OS.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "NVPN"
    ### NVPN

    [Official Website](https://www.nvpn.net/){target="_blank"}

    Fellow the guide [here](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} to create the config.

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "OVPN"
    ### OVPN

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Login [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"}, find the menu below to get WireGuard configuration files.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Click **Generate WireGuard keys**, choose the server you wanted, then download the config.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Open the config by text edit software, copy the content.

        The config may contain IPv6 content, as GL.iNet routers is not support IPv6 good enough, so please delete the IPv6 content. I have a example show below, the highlight content is the IPv6 content.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}
    
    4. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

    5. You can also use [mobile app](../faq/mobile_app.md) to setup OVPN.

??? "PrivateVPN"
    ### PrivateVPN

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Login then access the [Control panel](https://privatevpn.com/control-panel){target="_blank"}
    
        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. Select a server
    
        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. Click **GENERATE CONFIG**, then copy the config.
    
        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Access PrivadoVPN website, then login.

    At the dashboard, find the Manual Configuration section, click WireGuard. Select the server you want to connect to, then click Download Configration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "Proton VPN"
    ### Proton VPN

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    If you are using [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, please follow the guide [here](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} to generate the WireGuard configuration file.

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "PureVPN"
    ### PureVPN

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Please refer to [this guide](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} or the following steps to get the WireGuard configuration file manually.

    1. Log in to your [Member Area](https://my.puremember.com/){target="_blank"} and click **Manual Configuration**.

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn1.png){class="glboxshadow"}

    2. Go to your Member Area and download the WireGuard configuration file from there.

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn2.png){class="glboxshadow"}

    **Note**: Please make sure to copy the file and activate the connection within 30 minutes once the profile is downloaded, otherwise the configuration will expire and you will have to redownload a fresh configuration file.

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

    [Refer link](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [Official Website](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Login [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff), find the section to get your VPN configuration. Follow the steps to get the configuration.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Download the vpn configuration

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "StarVPN"
    ### StarVPN

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Register an account with StarVPN**

        Head on over to their [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} options and choose a VPN plan that suits your needs. You can register on checkout or directly [here](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Download Wireguard Configuration**

        Log into the StarVPN member area [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. Click on Wireguard Config to download the configuration file. Each slot will contain a unique wireguard configuration file.

        ![starvpn download wireguard config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/download-config_edited.jpg){class="glboxshadow"}

    3. The config may contain IPv6 content, as GL.iNet routers is not support IPv6 good enough, so please delete the IPv6 content.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/starvpn_wireguard_configuration_remove_ipv6.jpg){class="glboxshadow"}

    4. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

    [Refer link](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. If you are using [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, sign in at [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}
    
    2. Select a location from the drop down menu, click **GENERATE**, open the downloaded text file.
    
        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

    4. You can also use [mobile app](../faq/mobile_app.md) to setup StrongVPN.

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [Official Website](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Access [https://trust.zone/setup](https://trust.zone/setup) and login.
    
    2. Scroll down to the WireGuard section, choose the port you want, then download a config of specific server or a zip file of all configs.

    3. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "VPN.AC"
    ### VPN.AC

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. If you are using [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, you need to login the control panel and find WireGuard Manager from the "Services" menu.
    
        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. Create the config and download.
    
        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. If you are using [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, sign in to your [User Office](https://my.keepsolid.com/){target="_blank"} > select the VPN Unlimited® application > click **Manage**.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}
    
    2. Press the field under **Device** and click **Manually create a new device…** > set it's custom name, for example WireGuard > choose appropriate location of the **Server** > select the **WireGuard**® protocol from the dropdown menu > click **Generate**.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}
    
    3. The configuration parameters will then appear below in the text format.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        Combine the configuration as below.

        <p>
        [Interface]</br>
        PrivateKey = <i>paste the PrivateKey from your User Office</i></br>
        ListenPort = <i>paste the ListenPort details</i></br>
        Address = <i>paste Address information</i></br>
        DNS = <i>paste DNS details from the User Office</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>paste PublicKey from the User Office</i></br>
        PresharedKey = <i>paste PresharedKey details</i></br>
        AllowedIPs = <i>paste AllowedIPs details</i></br>
        Endpoint = <i>paste Endpoint information</i></br>
        </p>

    4. Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.
 
    [Refer link 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Refer link 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Log in to your Windscribe membership account [here](https://windscribe.com/login?auth_required){target="_blank"}, then access the [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}. 
    
    2. Select the server location and port you'd like to use, then click **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

??? "12VPX"
    ### 12VPX

    [Official Website](https://12vpx.com/?aff=1174){target="_blank"}

    If you are using [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, login then access [this page](https://12vpx.com/setup/wireguard){target="_blank"}, you will see the configs of all servers.

    Then follow [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) to continue.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.