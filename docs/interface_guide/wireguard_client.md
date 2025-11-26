# How to Set Up WireGuard Client on GL.iNet Router

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!! note

    This guide is for firmware v4.7 and above. If you are using an earlier firmware version, please visit [here](wireguard_client_v4.6.md).

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be faster, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN.

If you have subscribed to the WireGuard service from a provider but don't know how to get the configuration files, please refer to [Get Configuration Files from WireGuard Service Providers](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) or contact their support.

You can set up WireGuard Client via the web Admin Panel or [mobile app](../faq/mobile_app.md). 

**The mobile app** integrates some WireGuard service providers, such as AzireVPN, Mullvad VPN, OVPN, StrongVPN, PIA VPN, etc., which means you can easily set it up by simply entering the login credentials of the WireGuard service you subscribed to. Open the app and follow the on-screen instructions to set up.

**The web Admin Panel** not only integrates some WireGuard service providers, but also provides an entry for manual configuration. You can either enter the credentials of your subscribed WireGuard service for quick setup, or manually upload a configuration file to complete the setup.

Select the corresponding WireGuard service provider below to quickly locate the step-by-step instructions.

* [Set Up AzireVPN](#set-up-azirevpn)
* [Set Up Hide.me](#set-up-hideme)
* [Set Up IPVanish](#set-up-ipvanish)
* [Set Up Mullvad](#set-up-mullvad)
* [Set Up NordVPN](#set-up-nordvpn)
* [Set Up PIA (Private Internet Access)](#set-up-pia-private-internet-access)
* [Set up PureVPN](#set-up-purevpn)
* [Set Up Surfshark](#set-up-surfshark)
* [Set Up WireGuard Client Manually (for other providers)](#set-up-wireguard-client-manually-for-other-providers)

## Set Up AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

Watch this video to set up AzireVPN on GL.iNet routers via web Admin Panel or mobile app.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Or follow the steps below to set up AzireVPN on GL.iNet routers via web Admin Panel.

In the web Admin Panel -> VPN -> WireGuard Client -> AzireVPN.

1. Input **Username** and **Password**, then click **Save and Continue**. It will generate configuration files for each server.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}
    
    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Go renew.

    If you click **Go Renew**, you will be re-directed to the official website to renew your subscription.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Set Up Hide.me

[Official Website](https://www.hideipvpn.com/){target="_blank"}

In the web Admin Panel -> VPN -> WireGuard Client -> Hide.me.

1. Input **Username** and **Password**, then click **Save and Continue**. It will generate configuration files for each server.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Set Up IPVanish

[Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

In the web Admin Panel -> VPN -> WireGuard Client -> IPVanish.

1. Input **Username** and **Password**, then click **Save and Continue**. It will generate configuration files for each server.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Select servers.

    Select the server(s) you want to connect to, and click **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Set Up Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} is a VPN service that helps keep your online activity, identity, and location private.

In the web Admin Panel -> VPN -> WireGuard Client -> Mullvad.

1. Input **Account**, then click **Save and Continue**. It will generate configuration files for each server.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Select servers.

    Select the server(s) you want to connect to, and click **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}
    
    Once connected, a green dot will appear next to the configuration file.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Go renew.

    If you click **Go Renew**, you will be re-directed to the official website to renew your subscription.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Set Up NordVPN

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is an online VPN service that combines speed and security.

1. Click [here](https://my.nordaccount.com/){target="_blank"} to log in with your NordVPN web account.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}
    
    After logging in to the Nord dashboard, click NordVPN on the left side, then click **Set up NordVPN manually**.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_dashboard.png){class="glboxshadow"}

    Then you will find the **Access token**.

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/manual_setup.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/generate_new_token.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/copy_access_token.png){class="glboxshadow"}

2. Log in to the router's web Admin Panel -> VPN -> WireGuard Client -> NordVPN. 

    Input **Token**, then click **Save and Continue**. It will generate configuration files for each server.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Select servers.

    Select the server(s) you want to connect to, and click **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Set Up PIA (Private Internet Access)

[Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

In the web Admin Panel -> VPN -> WireGuard Client -> PIA.

1. Input **Username** and **Password**, then click **Save and Continue**. It will generate configuration files for each server.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Select servers.

    Select the server(s) you want to connect to, and click **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Set Up PureVPN

[Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

In the web Admin Panel -> VPN -> WireGuard Client -> PureVPN.

1. Input **Username** and **Password**, then click **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    It will generate all available configuration files.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

4. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Set Up Surfshark

[Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

In the web Admin Panel -> VPN -> WireGuard Client -> Surfshark.

1. Input **Username** and **Password**, then click **Save and Continue**. It will generate configuration files for each server.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Select servers.

    Select the server(s) you want to connect to, and click **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Refresh.

    You can click **Refresh** to update the public key when the VPN server cannot be connected.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Set Up Windscribe

[Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

In the web Admin Panel -> VPN -> WireGuard Client -> Windscribe.

1. Input **Username** and **Password**, then click **Save and Continue**. It will generate configuration files for each server.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Select servers.

    Select the server(s) you want to connect to, and click **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Then you will get a list of configuration files corresponding to the selected server.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Start a connection.

    Select your preferred server, and click the three-dot icon on the right to start a connection.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    And the VPN connection details will be displayed on the **VPN Dashboard**.

    ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. Update servers.

    You can click **Update Servers** to obtain the latest available server list, avoiding connection failures caused by server maintenance or shutdown.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Edit credentials or logout.

    Click the gear icon to edit your login credentials or log out.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Refresh.

    You can click **Refresh** to update the public key when the VPN server cannot be connected.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Delete All.

    You can click **Delete All** to delete all configuration files with one click, and choose whether to delete the private and public keys simultaneously.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Set Up WireGuard Client Manually (for other providers)

If you are using another WireGuard service provider, you can download the WireGuard configuration files and follow the steps below to set up the WireGuard Client. If you don't know how to download the configuration files, please refer to [this guide](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) or contact their support.

In the web Admin Panel -> VPN -> WireGuard Client -> Add Manually.

1. Click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. It will create a group on the left sidebar.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Set a descriptive name for the group (e.g., azirevpn). Then upload a configuration file (supported formats: zip, tar, gz, conf, txt) or manually add configuration details (in text form).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Upload a configuration file**.

        Click on the upload area to upload your WireGuard configuration file, then click **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Manually add configuration**.
    
        Click on **Manually Add Configuration** at the bottom of the upload area.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Set a descriptive name, and paste the configuration into the text box. Then click **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        If you want to verify each item, you can switch to the Item mode and check the config details. Then click **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Click the three-dot icon on the right side to start the connection.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. Once connected, you can check the connection status on the **VPN Dashboard** page.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Set Up WireGuard Server on GL.iNet Router

Do not want to subscribe to third-party VPN services? You may purchase two GL.iNet routers – set one as WireGuard server and the other as WireGuard server.

This is especially suitable for scenarios where your home network's ISP provides a Public IP, and you want to connect to your home network via VPN when away from home to ensure security and access to internal network resources. This eliminates the cost and hassle of continuously subscribing to commercial VPN services.

For WireGuard server setup, please check [here](wireguard_server.md).

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
