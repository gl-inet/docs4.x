# How to set up OpenVPN server via AstroRelay?

This tutorial introduces the steps to set up an OpenVPN server via AstroRelay on a GL.iNet router, which is ideal for users who need remote access to their home or office local services but do not have a public IP address from their ISP.

[AstroRelay](https://www.astrorelay.com){target="_blank"} provides a secure reverse proxy tunnel, through which you can securely access resources behind NAT and firewalls.

1. Follow [this guide](../interface_guide/openvpn_server.md) to set up an OpenVPN server on your GL.iNet router, even if you don't have a public IP address. 

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Then export the OpenVPN configuration. Here is an example config file.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. (Optional) If you need to access the VPN server's LAN remotely, enable **Allow Remote Access LAN**. Otherwise, skip this step.

    ??? "For firmware v4.7 and earlier"

        1. In the left sidebar, click **VPN** > **VPN Dashboard**. 
        2. Click the Options icon.
        3. Toggle the switch to on for **Remote Access LAN**.
        4. Click **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "For firmware v4.8 and later"

        1. In the left sidebar, click **VPN** > **OpenVPN Server**.
        2. Click **Options** in the upper right.
        3. Toggle the switch to on for **Allow Remote Access the LAN Subnet**.
        4. Click **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3. Sign up an AstroRelay account and follow this [tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"} to complete first-time setup.

    When adding a new domain, choose the server closest to your router.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    When adding a new link, enter your router's **LAN IP address** into the **Destination Host IP** field, and enter **1194** in the **Destination Port** field.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    You will then get a link, such as **testforx3000.arlab1.cc:37202**. Click it to copy the link.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4. Open the OpenVPN configuration file, and replace the value after **Remote** with the link you got in the previous step. In the example below, "42.200.00.00 1194" is replaced with the link "testforx3000.arlab1.cc:37202". Then replace the colon ":" with a space and apply the changes.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5. Install the [OpenVPN Connect app](https://openvpn.net/client/){target="_blank"} on the device you want to use as an OpenVPN client. Then upload the modified configuration file to the app and start the conneciton. Alternatively, upload it to another GL.iNet router so as to set it up as an OpenVPN client.

    Once connected, you will be able to access your home or office local services remotely.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.