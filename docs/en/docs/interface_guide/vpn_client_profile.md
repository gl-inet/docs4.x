# VPN Client Profile

> This guide applies to firmware v4.9 and later. 

Since firmware v4.9, the [OpenVPN Client](openvpn_client.md) and [WireGuard Client](wireguard_client.md) have been merged into a single **VPN Client Profile** page for more streamlined management. While the layout has been slightly adjusted, core functionality remains unchanged. You may still refer to the separate guides if needed.

On the left side of the web Admin Panel, go to **VPN** -> **VPN Client Profile**.

This page allows you to log in to some integrated VPN services and download their profiles easily for VPN connection, or manually upload your configuration files exported from other VPN provider's website. You may switch VPN protocols in the upper-right corner if needed.

## WireGuard

WireGuard® is a lightweight, high-performance modern VPN built with cutting-edge cryptography. It delivers superior speed, simplicity and practicality compared to IPsec, and significantly outperforms OpenVPN.

GL.iNet routers offer built-in WireGuard support for the following VPN providers. If you have an active subscription, simply enter your service credentials on the **VPN Client Profile** page to finish setup quickly.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

If you subscribe to other WireGuard service provider, download a configuration file from their website, then click **Add Manually** to upload the file to your router for VPN connection. If you don't know how to download the configuration files, refer to [here](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) or contact their support. 

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

Take [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} as an example. 

1. Click **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Enter your **Username** and **Password**, then click **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    The system will generate configuration files for all available servers.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Refer to the corresponding guidance below based on your actual needs.

    !!! note "Case 1. If you want all connected clients to use VPN for internet access, follow these steps." 
    
        1. Select your preferred server, and click the three-dot icon on the right to start a connection.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Once connected, a green dot will appear next to the configuration file. 

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            Now the VPN connection has been activated, and all clients connected to this router should use VPN for secured internet access.

    !!! note "Case 2. If you prefer to customize VPN policy instead, follow these steps."
    
        1. Click **Go to Dashboard** at the bottom.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. You will then be redirected to the **VPN Dashboard** to configure VPN policy. Click [here](vpn_dashboard_v4.9.md#set-up-vpn-policy) for details.

## OpenVPN

OpenVPN is an open‑source VPN protocol that uses virtual private network techniques to establish secure site‑to‑site or point‑to‑point connections.

GL.iNet routers offer built-in OpenVPN support for [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. If you have an active subscription, simply enter your service credentials on the **VPN Client Profile** page to finish setup quickly.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

If you subscribe to other OpenVPN service provider, download a configuration file from their website, then click **Add Manually** to upload the file to your router for VPN connection. If you don't know how to download the configuration files, refer to [here](openvpn_client.md#get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers) or contact their support. 

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

Related Articles

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard_v4.9.md)
- [Set Up WireGuard Client on GL.iNet Routers](wireguard_client.md)
- [Set Up OpenVPN Client on GL.iNet Routers](openvpn_client.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
