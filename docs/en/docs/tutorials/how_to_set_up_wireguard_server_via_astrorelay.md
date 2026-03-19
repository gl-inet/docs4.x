# How to set up WireGuard server via AstroRelay?

This tutorial introduces the steps to set up a WireGuard server via AstroRelay on a GL.iNet router, which is ideal for users who need remote access to their home or office local services but do not have a public IP address from their ISP.

[AstroRelay](https://www.astrorelay.com){target="_blank"} provides a secure reverse proxy tunnel, through which you can securely access resources behind NAT and firewalls.

1. Follow [this guide](../interface_guide/wireguard_server.md) to set up a WireGuard server on your GL.iNet router, even if you don't have a public IP address. 

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Then click **Profiles** to export the WireGuard configuration. Here is an example config file.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. (Optional) If you need to access the VPN server's LAN remotely, enable **Allow Remote Access LAN**. Otherwise, skip this step.

    ??? "For firmware v4.7 and earlier"

        On the server's web admin panel, go to **VPN** -> **VPN Dashboard** -> **VPN Server** section. Click the gear icon on the right side of the WireGuard server.

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        Enable **Remote Access LAN**, and click **Apply**.

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **When enabled, this router and LAN devices can be accessed remotely via the VPN.**

    ??? "For firmware v4.8 and later"

        On the server's web admin panel, go to **VPN** -> **WireGuard Server**. Click **Options** in the upper right corner.

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        Enable **Allow Remote Access the LAN Subnet**, and click **Apply**.

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **When enabled, this router and LAN devices can be accessed remotely via the VPN.**

3. Sign up an AstroRelay account and follow this [tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"} to complete first-time setup.

    When adding a new domain, choose the server closest to your router.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    When adding a new link, enter your router's **LAN IP address** into the **Destination Host IP** field, and enter **51820** into the **Destination Port** field.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    You will then get a link, such as **wg_server_test.arlab1.cc:33331**. Click it to copy the link.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4. Open the WireGuard configuration file, replace the value after **Endpoint** with the link you got in the previous step, and apply the changes.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5. Install the [WireGuard app](https://www.wireguard.com/install/){target="_blank"} on the device you want to use as a WireGuard client. Then upload the modified configuration file to the app and start the conneciton. Alternatively, upload it to another GL.iNet router so as to set it up a WireGuard client.

    Once connected, you will be able to access your home or office local services remotely.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.

