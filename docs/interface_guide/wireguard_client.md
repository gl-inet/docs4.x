# How to Set Up WireGuard Client on GL.iNet Router

!!! note

    This guide is based on firmware v4.7.x. If you are using an earlier firmware version, please visit [here](wireguard_client_v4.6.md).

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN.

If you have already bought WireGuard service from a provider, but you don't know how to get the configuration files, please refer to [get configuration files from WireGuard service providers](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) or ask its support.

You can set up WireGuard Client via web Admin Panel or [mobile app](../faq/mobile_app.md). For the mobile app, it has already integrated some WireGuard Service Providers, they are AzireVPN, Mullvad VPN, OVPN, StrongVPN, PIA VPN.

For set up via web Admin Panel, several providers are already integrated, and connection can also be established using a configuration file.

* [Set Up AzireVPN](#set-up-azirevpn)
* [Set Up Hide.me](#set-up-hideme)
* [Set Up IPVanish](#set-up-ipvanish)
* [Set Up Mullvad](#set-up-mullvad)
* [Set Up NordVPN](#set-up-nordvpn)
* [Set Up PIA(Private Internet Access)](#set-up-piaprivate-internet-access)
* [Set Up Surfshark](#set-up-surfshark)
* [Set up WireGuard Client via configurations](#set-up-wireguard-client)

## Set Up AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

1. Input **Username** and **Password**, then click **Save And Continue**. It will generate configuration files for each servers.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Start server

    ![azirevpn start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

3. Update servers

    AzireVPN may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

4. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![azirevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

5. Go renew

    If you click **Go Renew**, it will jump to the official website to renew your subscription.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

6. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

## Set Up Hide.me

[Official Website](https://www.hideipvpn.com/){target="_blank"}

1. Input **Username** and **Password**, then click **Save And Continue**. 

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Start the server

    ![hideme select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}
    
    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard hideme connectedia](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

3. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

4. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![hideme edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

5. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

## Set Up IPVanish

[Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

1. Input **Username** and **Password**, then click **Save And Continue**. 

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Select servers

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Start server

    ![ipvanish start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard ipvanish connectedia](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

4. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

5. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![ipvanish edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

6. Refresh

    You can click **Refresh** to update the public key when the VPN server cannot be connected.

    ![ipvanish refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

7. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Set Up Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} is a VPN service that helps keep your online activity, identity, and location private.

1. Input **Account**, then click **Save And Continue**. It will generate configuration files for each servers.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Select servers

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Start server

    ![mullvad start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}
    
    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard mullvad connectedia](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

4. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

5. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![mullvad edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

6. Go renew

    If you click **Go Renew**, it will jump to the official website to renew your subscription.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

7. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

## Set Up NordVPN

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is the top online VPN service for speed and security.

1. Login your NordVPN web account and get your service credentials

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}
    
    After login to Nord dashboard, click NordVPN on the left side, then click Set up NordVPN manually.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_dashboard.png){class="glboxshadow"}

    Then you will find the service credentials.

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/manual_setup.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/generate_new_token.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/copy_access_token.png){class="glboxshadow"}

2. Input **Token**, then click **Save And Continue**. It will generate configuration files for each servers.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Select servers

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Start server

    ![nordvpn start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}
    
    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard nordvpn connectedia](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

5. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

6. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![nordvpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

7. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

## Set Up PIA(Private Internet Access)

[Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

1. Input **Username** and **Password**, then click **Save And Continue**. It will generate configuration files for each servers.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Select servers

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Start server

    ![pia start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}
    
    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard pia connectedia](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

4. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

5. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

6. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

## Set Up Surfshark

[[Official Website]](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}

1. Input **Username** and **Password**, then click **Save And Continue**.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Select servers

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Start server

    ![surfshark start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}
    
    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard surfshark connectedia](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

4. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

5. Edit credential or logout

    Click the cog icon to edit the credential or logout.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

6. Refresh

    You can click **Refresh** to update the public key when the VPN server cannot be connected.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

7. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

## Set up WireGuard Client

1. Click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient1.png){class="glboxshadow"}

2. It will create a group.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient2.png){class="glboxshadow"}

3. Give the group a descriptive name, e.g. azirevpn. Then you can choose to upload configuration files or manually add configuration.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient3.png){class="glboxshadow"}

    1. **Upload configuration files**

        Upload your WireGuard configuration file, click **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient4.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient5.png){class="glboxshadow"}

    2. **Manually Add Configuration**, it is for if you want to paste the WireGuard configuration or fill in each item.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient7.png){class="glboxshadow"}

        Give a descriptive name and paste the configuration, click **Item Mode** to continue.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient8.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient9.png){class="glboxshadow"}

4. Click the three dots icon to start / edit /delete the profile.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/WireGuardClient6.png){class="glboxshadow"}

5. Check the connection status by go to [VPN Dashboard](vpn_dashboard.md) page.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Set Up WireGuard Server on GL.iNet Router

You can get a GL.iNet router to set as WireGuard server, and get another GL.iNet router to set as WireGuard client. For setup WireGuurd server, please check out [here](wireguard_server.md).

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
