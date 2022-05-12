# WireGuard Client

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/), [simpler](https://www.wireguard.com/quickstart/), leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. 

GL.iNet routers have pre-installed WireGuard Client and Server.

If you have already bought WireGuard service from a provider, but you don't know how to get the configuration files, please refer to [get configuration files from WireGuard service providers](#get-configuration-files-from-wireguard-service-providers).

You can setup WireGuard Client via web Admin Panel and [mobile app](../mobile_app). For the mobile app, it has already integrated some WireGuard Service Providers, they are AzireVPN, Mullvad VPN, TorGuard VPN, OVPN, WeVPN, StrongVPN, PIA VPN, SpiderVPN.

For setup via web Admin Panel, please follow the guide below.

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

## Setup WireGuard server on GL.iNet router

You can get a GL.iNet router to set as WireGuard server, and get another GL.iNet router to set as WireGuard client. For setup OpenVPN server, please check out [here](../wireguard_server).

## Get configuration files from WireGuard service providers
