# How to Set Up WireGaurd Client on GL.iNet Router

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN.

If you have already bought WireGuard service from a provider, but you don't know how to get the configuration files, please refer to [get configuration files from WireGuard service providers](#get-configuration-files-from-wireguard-service-providers) or ask its support.

You can set up WireGuard Client via web Admin Panel or [mobile app](../mobile_app). For the mobile app, it has already integrated some WireGuard Service Providers, they are AzireVPN, Mullvad VPN, TorGuard VPN, OVPN, WeVPN, StrongVPN, PIA VPN.

For set up via web Admin Panel, please follow the guide below.

You can log in by clicking the **AzireVPN** or **Mullvad** button if you have a their membership, or by clicking **Add Manually** to upload the WireGuard profiles.

![wireguard client no initialized](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/wireguard_client_no_initialized.png){class="glboxshadow gl-80-desktop"}

## Set Up AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

![azirevpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/azirevpn.png){class="glboxshadow"}

1. Input **Username** and **Password**, then click **Save Credentials & Get Servers**. It will generate configuration files for each servers.

    ![azirevpn profiles](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Update servers

    AzireVPN may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![azirevpn update servers](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/azirevpn_update_servers.png){class="glboxshadow"}

4. Edit credential

    Click the cog icon to edit the credential.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/azirevpn_edit_credential.png){class="glboxshadow"}

## Set Up Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} is a VPN service that helps keep your online activity, identity, and location private.

Firmware 4.x has integrated Mullvad WireGaurd service.

![mullvad vpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/mullvad.png){class="glboxshadow"}

1. Input **Account**, then click **Save Credentials & Get Servers**.

    Mullvad account number is a 16-digit decimal in the "1000 0000 0000 0000" to "9999 9999 9999 9999" range.

    It will pop up a dialog to select a location.

    ![mullvad vpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/mullvad_select_servers.png){class="glboxshadow"}

    Then it will generate the configuration files of the selected location server.
    
    The **Public Key** is the WireGuard public key to send to Mullvad server, you can have up to five keys at the same time, you can manage WireGuard keys on [Mullvad's page](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/mullvad_generated_profiles.png){class="glboxshadow"}

2. Go to VPN Dashboard to enable the connection.

    ![mullvad vpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![mullvad vpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/mullvad_update_servers.png){class="glboxshadow"}

4. Edit credential

    ![mullvad vpn](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/mullvad_edit_credential.png){class="glboxshadow"}

## Set Up WireGuard Client

As of firmware 4.0, it brings grouping to manage WireGuard profiles.

1. Click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/wireguard_client_add_manually.png){class="glboxshadow gl-80-desktop"}

2. It will create a group.

    ![add a new group](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/add_a_new_group.png){class="glboxshadow"}

3. Give the group a descriptive name, e.g. azirevpn. Then you can choose to upload configuration files or manually add configuration.

    ![set the new group name](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Upload configuration files**

        Upload your WireGuard configuration file, click **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration**, it is for if you want to paste the WireGuard configuration or fill in each item.

        ![add wireguard by text](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Give a descriptive name and paste the configuration, click **Apply** to continue.

        ![add wireguard by text](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Or you can add configuration by fill in each item, click **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Click the three dots icon to start / edit /delete the profile.

    ![start the profile](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Check the connection status by go to [VPN Dashboard](../vpn_dashboard) page.

    ![vpn dashboard page](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Set Up WireGuard Server on GL.iNet Router

You can get a GL.iNet router to set as WireGuard server, and get another GL.iNet router to set as WireGuard client. For setup WireGaurd server, please check out [here](../wireguard_server).

## Get Configuration Files from WireGuard Service Providers

<div id="azirevpn"></div>

??? "AzireVPN"

    [Official Website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Access [AzireVPN official website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} and login, then access the [WireGuard Configuration generator](https://www.azirevpn.com/cfg/wireguard){target="_blank"}

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. At the IP option, please select **IPv4**. Then click **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Then follow the [guide](#setup-wireguard-client) to continue.

    4. You can also use [mobile app](../mobile_app) to setup AzireVPN.

<div id="mullvad"></div>

??? "Mullvad"

    [Official Website](https://mullvad.net/){target="_blank"}

    1. Access [Mullvad Official Website](https://mullvad.net/){target="_blank"} and login, then access the [WireGaurd configuration file generator](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}

    2. Then follow the [guide](#setup-wireguard-client) to continue.

    3. You can also use [mobile app](../mobile_app) to setup Mullvad.

<div id="ovpn"></div>

??? "OVPN"

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Login [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"}, find the menu below to get WireGuard configuration files.

        ![ovpn dashboard](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Click **Generate WireGuard keys**, choose the server you wanted, then download the config.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Open the config by text edit software, copy the content.

        The config may contain IPv6 content, as GL.iNet routers is not support IPv6 good enough, so please delete the IPv6 content. I have a example show below, the highlight content is the IPv6 content.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}
    
    4. Then follow the [guide](#setup-wireguard-client) to continue.

    5. You can also use <a href="../mobile_app">mobile app</a> to setup OVPN.

<div id="torguard"></div>

??? "TorGuard"

    [Official Website](https://torguard.net/aff.php?aff=3040){target="_blank"}

    1. If you are using [TorGuard](https://torguard.net/aff.php?aff=3040){target="_blank"}, you need to login the control panel and find **Config Generator** from the **Tools** menu. 

        ![torguard enable wireguard access](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/torguard/torguard_menu.jpg){class="glboxshadow"}

    2. On the Config Generator page, choose **VPN Tunnel type** to WireGuard, select **VPN Server**, input **VPN Username** and **VPN Password**, click **Generate Config** button, wait a second, you will find the config on **Config Output** section.

        ![torguard generate wireguard config](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/torguard/torguard_generate_wireguard_config.png){class="glboxshadow"}

        You can find the **VPN Username** and **VPN Password** below

        ![torguard vpn username vpn password](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/torguard/torguard_vpnusername_vpnpassword.png){class="glboxshadow"}

    3. Then follow the [guide](#setup-wireguard-client) to continue.

    4. You can also use <a href="../mobile_app">mobile app</a> to setup TorGuard.

<div id="surfshark"></div>

??? "Surfshark"

    [Official Website](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}

    1. If you are using [Surfshark](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}, login then go to [this](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"} page, click on **Router**, and select **WireGaurd**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. In the next window, select **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Select **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Once the key has been generatd, select **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Lastly, choose a location you would like to set up, and hit the **download** button next to the location.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    [Refer link](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}


<div id="vpnac"></div>

??? "VPN.AC"

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. If you are using [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, you need to login the control panel and find WireGuard Manager from the "Services" menu.
    
        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. Create the config and download.
    
        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Then follow the [guide](#setup-wireguard-client) to continue.

<div id="strongvpn"></div>

??? "StrongVPN"

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. If you are using [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, sign in at [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}
    
    2. Select a location from the drop down menu, click **GENERATE**, open the downloaded text file.
    
        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. Then follow the [guide](#setup-wireguard-client) to continue.

    4. You can also use <a href="../mobile_app">mobile app</a> to setup StrongVPN.

<div id="wevpn"></div>

??? "WeVPN"

    [Official Website](https://www.wevpn.com/aff/glinet){target="_blank"}

    1. Access the Members Area to make a custom config using the Config Generator.
    
        ![wevpn manual configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/wevpn/wevpn_1.jpg){class="glboxshadow"}
    
    2. When you select the WireGuard protocol, you will need to select **Add device** for the region selected.
    
        ![wevpn manual configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/wevpn/wevpn_2.jpg){class="glboxshadow"}

    3. Then follow the [guide](#setup-wireguard-client) to continue.

    4. You can also use <a href="../mobile_app">mobile app</a> to setup WeVPN.

    [Refer link](https://wevpn.com/support/hc/en-us/search/click?data=BAh7CjoHaWRsKwgmhcHUUwA6CXR5cGVJIgxhcnRpY2xlBjoGRVQ6CHVybEkiTWh0dHBzOi8vd2V2cG4uemVuZGVzay5jb20vaGMvZW4tdXMvYXJ0aWNsZXMvMzYwMDUxNzM3ODk0LVdpcmVndWFyZC1TZXR1cAY7B1Q6DnNlYXJjaF9pZEkiKTg1MzYyYTliLTFiNjQtNDgxZi1hOTZiLTIzMTE3NzQ4ZGMwMwY7B0Y6CXJhbmtpBg%3D%3D--708754fd43f05b5496036ebe0747c5a6dac84bf3){target="_blank"}

<div id="windscribe"></div>

??? "Windscribe"

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    Login then access the [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}. Select location and port you'd like to use, then click Download Config.

    ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="privatevpn"></div>

??? "PrivateVPN"

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Login then access the [Control panel](https://privatevpn.com/control-panel){target="_blank"}
    
        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. Select a server
    
        ![select a server](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. Click **GENERATE CONFIG**, then copy the config.
    
        ![generate config](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Then follow the [guide](#setup-wireguard-client) to continue.

<div id="pia"></div>

??? "PIA (Private Internet Access)"

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    It can't downlaod the WireGaurd configs from its website, please use [mobile app](../mobile_app) to setup PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div id="airvpn"></div>

??? "AirVPN"

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. If you are using [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, sign in to their website, go to the [Client Area](https://airvpn.org/client/){target="_blank"}, click the [Config Generator](https://airvpn.org/generator/){target="_blank"}

        ![airvpn configuration generator](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. At the Config Generator page, select WireGuard at the Protocols sector.

        ![airvpn protocols](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Select a server, then scroll down to the end, click **Generate** button. It will download the configuration file.

        ![airvpn select server](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Then follow the [guide](#setup-wireguard-client) to continue.

<div id="proton"></div>

??? "Proton VPN"

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    If you are using [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, please follow the guide [here](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} to generate the WireGuard configuration file.

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="astrill"></div>

??? "Astrill"

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    If you are using [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, please log in then access [this page](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} to generate WireGuard configurations.

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="vpnunlimited"></div>

??? "VPN Unlimited(KeepSolid)"

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. If you are using [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, sign in to your [User Office](https://my.keepsolid.com/){target="_blank"} > select the VPN Unlimited® application > click **Manage**.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}
    
    2. Press the field under **Device** and click **Manually create a new device…** > set it’s custom name, for example WireGuard > choose appropriate location of the **Server** > select the **WireGuard**® protocol from the dropdown menu > click **Generate**.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}
    
    3. The configuration parameters will then appear below in the text format.
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

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

    4. Then follow the [guide](#setup-wireguard-client) to continue.
 
    [Refer link 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Refer link 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

<div id="12vpx"></div>

??? "12VPX"

    [Official Website](https://12vpx.com/?aff=1174){target="_blank"}

    If you are using [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, login then access [this page](https://12vpx.com/setup/wireguard){target="_blank"}, you will see the configs of all servers.

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="ivpn"></div>

??? "IVPN"

    [Official Website](https://www.ivpn.net/){target="_blank"}

    If you are using [IVPN](https://www.ivpn.net/){target="_blank"}, you need to generate the WireGuard config manually. Follow the guide base on your OS.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="trustzone"></div>

??? "TRUST.ZONE"

    [Official Website](https://trust.zone/){target="_blank"}

    1. Access [https://trust.zone/setup](https://trust.zone/setup) and login.
    
    2. Scroll down to the WireGuard section, choose the port you want, then download a config of specific server or a zip file of all configs.

    3. Then follow the [guide](#setup-wireguard-client) to continue.

<div id="anonine"></div>

??? "ANONINE"

    [Official Website](https://anonine.com/){target="_blank"}

    Fellow the guide below to generate WireGuard configs.

    [Windows](https://help.anonine.com/support/solutions/articles/5000817193-anonine-wireguard-installation-guide-for-windows-10){target="_blank"}, [macOS](https://help.anonine.com/support/solutions/articles/5000817206-anonine-wireguard-installation-guide-for-macos){target="_blank"}, [Ubuntu](https://help.anonine.com/support/solutions/articles/5000817191--anonine-wireguard-installation-guide-for-ubuntu-18-04){target="_blank"}, [Android](https://help.anonine.com/support/solutions/articles/5000817310--anonine-wireguard-installation-for-android){target="_blank"}, [iOS](https://help.anonine.com/support/solutions/articles/5000823286--anonine-wireguard-installation-for-ios){target="_blank"}

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="nvpn"></div>

??? "NVPN"

    [Official Website](https://www.nvpn.net/){target="_blank"}

    Fellow the guide [here](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} to create the config.

    Then follow the [guide](#setup-wireguard-client) to continue.

<div id="starvpn"></div>

??? "StarVPN"

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Register an account with StarVPN**

        Head on over to their [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} options and choose a VPN plan that suits your needs. You can register on checkout or directly [here](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Download Wireguard Configuration**

        Log into the StarVPN member area [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. Click on Wireguard Config to download the configuration file. Each slot will contain a unique wireguard configuration file.

        ![starvpn download wireguard config](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/starvpn/download-config_edited.jpg){class="glboxshadow"}

    3. The config may contain IPv6 content, as GL.iNet routers is not support IPv6 good enough, so please delete the IPv6 content.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/starvpn/starvpn_wireguard_configuration_remove_ipv6.jpg){class="glboxshadow"}

    4. Then follow the [guide](#setup-wireguard-client) to continue.

    [Refer link](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}

<div id="purevpn"></div>

??? "PureVPN"

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Please follow the guide [here](https://support.purevpn.com/setup-wireguard-on-linux){target="_blank"} to get the WireGuard configuration file.

    **Note**: Please make sure to copy the file and activate the connection within 30 minutes once the profile is downloaded, otherwise the configuration will expire and you will have to redownload a fresh configuration file.

<div id="hidemevpn"></div>

??? "Hide.me VPN"

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN providers a simple way to use their WireGuard service in GL.iNet router.

    1. [SSH](https://docs.gl-inet.com/en/3/tutorials/ssh/){target="_blank"} to router.

    2. Copy the install url below, then paste it to the terminal, hit the Enter key. (Right click the mouse will paste it.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. It will start installing, then ask for the username and password. When typing or pasting the password, no change is visible on the terminal, just hit the Enter key after typing.

    4. Once you're done, go to the web Admin Panel and you'll see that a hide.me VPN group has been created with configuration files already in it. Just connect as you would any other configuration file.

    **Note:** The key in the Hide.me VPN configuration file is regenerated before each connection and becomes invalid after disconnection, so copying this configuration file to other devices will not connect successfully.

    [Refer link](https://github.com/eventure/hide.client.routers){target="_blank"}

<div id="spidervpn"></div>

??? "SpiderVPN"

    [Official Website](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Login [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff), find the section to get your VPN configuration. Follow the steps to get the configuration.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Download the vpn configuration

        ![download spider vpn configuration](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Then follow the [guide](#setup-wireguard-client) to continue.

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
