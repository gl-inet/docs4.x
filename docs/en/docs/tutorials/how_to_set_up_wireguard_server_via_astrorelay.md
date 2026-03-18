# How to set up WireGuard server via AstroRelay?

Scenario: If you want to set up WireGuard server in GL.iNet router at home/office to remote access your local service, but your ISP doesn't provide a public IP address.

[AstroRelay](https://www.astrorelay.com){target="_blank"} provides a secure reverse proxy tunnel, through which you can securely access resources behind NAT and firewalls.

1. Follow the guide [here](../interface_guide/wireguard_server.md) to set up WireGuard server even if you don't have a public IP address. Please enable **Allow Access Local Network**.

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Then export a WireGuard configuration. The image below is an example.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. Sign up an AstroRelay account and follow this [tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"} to complete first-time setup.

    When adding a new domain, please choose the server closest to your router.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    When adding a new link, input your router's **LAN IP address** into the **Destination Host IP** box. Input **51820** into the **Destination Port** box.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    Then you will get a link, such as **wg_server_test.arlab1.cc:33331**. Click on it to copy the link.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

3. Open the WireGuard configuration, replace the data after **Endpoint** with the link you got in previous step. Then you will be able to use the modified config in WireGuard client app.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

4. When you are not at home/office, you can upload the modified config file into the WireGuard client app to access your home/office local service as you are at home/office.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.

