<<<<<<< HEAD
# WireGuardクライアント

WireGuard®は、**最先端の暗号技術**を利用した、非常にシンプルかつ高速な最新のVPNです。[faster](https://www.wireguard.com/performance/), [simpler](https://www.wireguard.com/quickstart/)を目指します。IPSecよりも無駄がなく、便利でありながら、膨大な頭痛の種を回避することができます。OpenVPNよりもかなり高性能になる予定です。
=======
# GL.iNetルーターでWireGaurdクライアントをセットアップする方法

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN.

GL.iNetのルーターには、WireGuard ClientとServerがプリインストールされています。

プロバイダーからWireGuardサービスを購入済みで、設定ファイルの入手方法が分からない場合は、以下のページを参照してください。 [get configuration files from WireGuard service providers](#get-configuration-files-from-wireguard-service-providers)　また、サポートにお聞きください。


WireGuardクライアントの設定は、Web管理パネルと[モバイルアプリ](../mobile_app)で行えます。モバイルアプリでは、AzireVPN、Mullvad VPN、TorGuard VPN、OVPN、WeVPN、StrongVPN、PIA VPN、SpiderVPNのいくつかのWireGuardサービスプロバイダが既に統合されています。

Web管理画面からの設定は、以下の手順で行ってください。

## Setup AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

Firmware 4.x has integrated AzireVPN WireGaurd service.

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

## Setup Mullvad

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

## Setup WireGuard client

As of frimware 4.0, it brings grouping to manage WireGuard profiles.

1. Add a new group

    ![add a new group](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_a_new_group.png){class="glboxshadow"}

2. Give the group a descriptive name, e.g. azirevpn.

    ![set the new group name](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/set_new_group_name.png){class="glboxshadow"}

3. Upload your WireGuard configuration file, then input the credential, click **Apply**.

    ![upload profile](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/upload_profile.png){class="glboxshadow"}

    ![after upload profile](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/after_upload_profile.png){class="glboxshadow"}

    **Manually Add Configuration** is for if you want to paste the WireGuard configuration or fill in each item.

    ![add wireguard by text](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/manually_add_configuration.png){class="glboxshadow"}

    Give a descriptive name and paste the configuration, click **Apply** to continue.

    ![add wireguard by text](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_wg_by_text.png){class="glboxshadow"}

    Or you can add configuration by fill in each item, click **Item Mode**.

    ![add wireguard by item mode](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}
    
    ![add wireguard by item mode](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard page](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_client/vpn_dashboard_to_connect_azirevpn.png){class="glboxshadow"}

## Setup WireGuard server on GL.iNet router

You can get a GL.iNet router to set as WireGuard server, and get another GL.iNet router to set as WireGuard client. For setup WireGaurd server, please check out [here](../wireguard_server).

## Get configuration files from WireGuard service providers

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
    
    4. Then fllow the [guide](#setup-wireguard-client) to continue.

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

    3. Then fllow the [guide](#setup-wireguard-client) to continue.

    4. You can also use <a href="../mobile_app">mobile app</a> to setup TorGuard.

<div id="vpnac"></div>

??? "VPN.AC"

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. If you are using [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, you need to login the control panel and find WireGuard Manager from the "Services" menu.
    
        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. Create the config and download.
    
        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="strongvpn"></div>

??? "StrongVPN"

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. If you are using [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, sign in at [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}
    
    2. Select a location from the drop down menu, click **GENERATE**, open the downloaded text file.
    
        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. Then fllow the [guide](#setup-wireguard-client) to continue.

    4. You can also use <a href="../mobile_app">mobile app</a> to setup StrongVPN.

<div id="wevpn"></div>

??? "WeVPN"

    [Official Website](https://www.wevpn.com/aff/glinet){target="_blank"}

    1. Access the Members Area to make a custom config using the Config Generator.
    
        ![wevpn manual configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/wevpn/wevpn_1.jpg){class="glboxshadow"}
    
    2. When you select the WireGuard protocol, you will need to select **Add device** for the region selected.
    
        ![wevpn manual configuration generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/wevpn/wevpn_2.jpg){class="glboxshadow"}

    3. Then fllow the [guide](#setup-wireguard-client) to continue.

    4. You can also use <a href="../mobile_app">mobile app</a> to setup WeVPN.

    [Refer link](https://wevpn.com/support/hc/en-us/search/click?data=BAh7CjoHaWRsKwgmhcHUUwA6CXR5cGVJIgxhcnRpY2xlBjoGRVQ6CHVybEkiTWh0dHBzOi8vd2V2cG4uemVuZGVzay5jb20vaGMvZW4tdXMvYXJ0aWNsZXMvMzYwMDUxNzM3ODk0LVdpcmVndWFyZC1TZXR1cAY7B1Q6DnNlYXJjaF9pZEkiKTg1MzYyYTliLTFiNjQtNDgxZi1hOTZiLTIzMTE3NzQ4ZGMwMwY7B0Y6CXJhbmtpBg%3D%3D--708754fd43f05b5496036ebe0747c5a6dac84bf3){target="_blank"}

<div id="windscribe"></div>

??? "Windscribe"

    [Official Website](https://windscribe.com/){target="_blank"}

    Login then access the [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}. Select location and port you'd like to use, then click Download Config.

    ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="privatevpn"></div>

??? "PrivateVPN"

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Login then access the [Control panel](https://privatevpn.com/control-panel){target="_blank"}
    
        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. Select a server
    
        ![select a server](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. Click **GENERATE CONFIG**, then copy the config.
    
        ![generate config](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="pia"></div>

??? "PIA (Private Internet Access)"

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    It can't downlaod the WireGaurd configs from its website, please use [mobile app](../mobile_app) to setup PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div id="proton"></div>

??? "Proton VPN"

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    If you are using [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, please follow the guide [here](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} to generate the WireGuard configuration file.

    Then fllow the [guide](#setup-wireguard-client) to continue.

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

    4. Then fllow the [guide](#setup-wireguard-client) to continue.
 
    [Refer link 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Refer link 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

<div id="12vpx"></div>

??? "12VPX"

    [Official Website](https://12vpx.com/?aff=1174){target="_blank"}

    If you are using [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, login then access [this page](https://12vpx.com/setup/wireguard){target="_blank"}, you will see the configs of all servers.

    Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="ivpn"></div>

??? "IVPN"

    [Official Website](https://www.ivpn.net/){target="_blank"}

    If you are using [IVPN](https://www.ivpn.net/){target="_blank"}, you need to generate the WireGuard config manually. Follow the guide base on your OS.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="trustzone"></div>

??? "TRUST.ZONE"

    [Official Website](https://trust.zone/){target="_blank"}

    1. Access [https://trust.zone/setup](https://trust.zone/setup) and login.
    
    2. Scroll down to the WireGuard section, choose the port you want, then download a config of specific server or a zip file of all configs.

    3. Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="anonine"></div>

??? "ANONINE"

    [Official Website](https://anonine.com/){target="_blank"}

    Fellow the guide below to generate WireGuard configs.

    [Windows](https://help.anonine.com/support/solutions/articles/5000817193-anonine-wireguard-installation-guide-for-windows-10){target="_blank"}, [macOS](https://help.anonine.com/support/solutions/articles/5000817206-anonine-wireguard-installation-guide-for-macos){target="_blank"}, [Ubuntu](https://help.anonine.com/support/solutions/articles/5000817191--anonine-wireguard-installation-guide-for-ubuntu-18-04){target="_blank"}, [Android](https://help.anonine.com/support/solutions/articles/5000817310--anonine-wireguard-installation-for-android){target="_blank"}, [iOS](https://help.anonine.com/support/solutions/articles/5000823286--anonine-wireguard-installation-for-ios){target="_blank"}

    Then fllow the [guide](#setup-wireguard-client) to continue.

<div id="nvpn"></div>

??? "NVPN"

    [Official Website](https://www.nvpn.net/){target="_blank"}

    Fellow the guide [here](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} to create the config.

    Then fllow the [guide](#setup-wireguard-client) to continue.

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

    4. Then fllow the [guide](#setup-wireguard-client) to continue.

    [Refer link](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}

<div id="spidervpn"></div>

??? "SpiderVPN"

    [Official Website](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Login [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff), find the section to get your VPN configuration. Follow the steps to get the configuration.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Download the vpn configuration

        ![download spider vpn configuration](https://static.gl-inet.com/docs/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Then fllow the [guide](#setup-wireguard-client) to continue.
