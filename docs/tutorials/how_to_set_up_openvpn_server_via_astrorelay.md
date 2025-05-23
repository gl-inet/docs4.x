# How to set up OpenVPN server via AstroRelay?

Scenario: If you want to set up OpenVPN server in GL.iNet router at home/office to remote access your local service, but your ISP doesn't provide a public IP address.

[AstroRelay](https://www.astrorelay.com){target="_blank"} provides a secure reverse proxy tunnel, through which you can securely access resources behind NAT and firewalls.

1. Follow the guide [here](../interface_guide/openvpn_server.md) to set up OpenVPN server even if you don't have a public IP address. Please enable **Allow Access Local Network**.

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Then export an OpenVPN configuration. The image below is an example.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. Sign up an AstroRelay account and follow this [tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"} to complete first-time setup.

    When adding a new domain, please choose the server closest to your router.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    When adding a new link, input your router's **LAN IP address** into the **Destination Host IP** box. Input **1194** into the **Destination Port** box.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    Then you will get a link, such as **testforx3000.arlab1.cc:37202**. Click on it to copy the link.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

3. Open the OpenVPN configuration, replace the data after **Remote** with the link you got in previous step. In the example below, we replace the "42.200.00.00 1194" with the link "testforx3000.arlab1.cc:37202".

    Then replace the colon ":" with a space, e.g. "testforx3000.arlab1.cc 37202". 

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

    Then you will be able to use the modified config file in OpenVPN client app.

4. When you are not at home/office, you can upload the modified config file into the OpenVPN client app to access your home/office local service as you are at home/office.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.