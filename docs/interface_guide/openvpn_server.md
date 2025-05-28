# Set Up OpenVPN Server on GL.iNet Routers

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

OpenVPN is an open-source VPN protocol that makes use of virtual private network (VPN) techniques to establish safe site-to-site or point-to-point connections. 

We recommend WireGuard over OpenVPN because it is much faster. For setup a WireGuard Server, please check out [here](wireguard_server.md).

---

## Make sure you have a public IP address

Please check if your Internet Service Provider assigns you a public IP address [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

**If not, your router cannot be set as the OpenVPN Server.**

Alternative methods:

1. If you have a main router, you shall login to it and check if it gets the Public IP from your ISP.
2. Ask your ISP for a Public IP address. It may require an extra fee.
3. If the above two ways don't work, for example, if you are in a CGNAT, you can take the reverse proxy method such as [Astrorelay](../tutorials/how_to_set_up_wireguard_server_via_astrorelay.md). Alternatively, you may try an SDWAN solution - [AstroWarp](https://www.astrowarp.net/){target="_blank"}. 

## Confirm if Port Forwarding is required

**Network Topology**

??? "GL.iNet is the Main Router"
    
    * If GL.iNet router is the main router in your network, this is simple, please move to the [next step](#setup-openvpn-server).

??? " GL.iNet is the Sub-Router"

    * If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) on the main router.
    
    * If you already have a main router, the GL.iNet router is several levels below it and you need to set up [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) on each level.

## Setup OpenVPN Server

1. Click **Generate Configuration** (Only the first time).

    ![openvpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_generate_config.png){class="glboxshadow"}

2. Apply the configuration.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_configuration.png){class="glboxshadow"}

    If you do not need to modify the configuration, please click directly the **Export Client Configuration** at the bottom of page. If you have modified the configuration, please click the **Apply** button to continue.

    * **Device Mode:** TAP-S2S or Tun. To find out what the difference is, check out [TAP-S2S vs Tun](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md).

    * **Protocol:** UDP or TCP. To find out what the difference is, check out [TCP vs UDP](../faq/openvpn_tcp_udp.md).

    * **Authentication Mode:** There are three options **Only Certificate**, **Only Username/Password**, **Username/Password and Certificate**. 
    
        For **Username/Password** and **Username/Password and Certificate** options, they need add user(s). Then, if a OpenVPN client connect to this server, it need to input the username and password.

        ![openvpn server users](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_users.png){class="glboxshadow"}

        Created a user.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_add_a_user.png){class="glboxshadow"}

        For **Only Certificate** and **Username/Password and Certificate**, the router will automatically generate a server and client certificate-key, and write into the configuration file when generating the client configuration file.

        Please check [here](#advanced-configuration) for **Advanced Configuration**.

3. Export Client Configuration

    Clicking the **Export Client Configuration** button at the bottom or applying the modified configuration will pop up this dialog.

    If your network's public IP changes from time to time, you can enable [DDNS](ddns.md) by using DDNS domain in the configuration. Click **Download** to export the configuration for further setup.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_export_client_configuration.png){class="glboxshadow"}

4. Start OpenVPN server

    Click the **Start** button in the upper right corner on OpenVPN Server page to start the server. Then go to [VPN Dashboard page](vpn_dashboard.md) to check its status and other settings.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_openvpn_server.png){class="glboxshadow"}

## Check if OpenVPN Server is working properly

Many people assume that the server has been successfully established as soon as they see it started, but in fact, it is not. 

Even if you forward the wrong port or address, the server can still run.

![openserverup](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

To verify if the OpenVPN Server is functioning properly, use another device on a separate network and import the previously exported OpenVPN configuration to test connectivity and check the assigned IP address.

The simplest method is to use a smartphone with the official [OpenVPN App](https://openvpn.net/vpn-client/){target="_blank"} installed. First, disable the phone’s Wi-Fi and connect exclusively to the internet via cellular data (3G/4G/5G). Then launch the OpenVPN app, import the pre-exported configuration file, and initiate the connection. Confirm whether the phone gains internet access and whether its IP address matches the OpenVPN Server’s IP.

When importing the configuration file into the OpenVPN app, a reminder may appear as shown below. Click **CONTINUE** to proceed, as the certificate is already embedded in the configuration file.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow"}

If the connection fails, there are several common reasons:

* The Internet Service Provider doesn't assign you a public IP address. Please check [here](#make-sure-you-have-a-public-ip-address).
* You may need to set up port forwarding. Please check [here](#confirm-if-port-forwarding-is-required).
* The port you are using for OpenVPN Server is blocked by the Internet Service Provider. Change to another port, or contact the Internet Service Provider for further assistance.
* Some countries/regions may block the VPN connection.

## Advanced Configuration

In the Configuration tab of the OpenVPN server page, you can modify the configuration of your own Server. 

![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_advanced_configuration.png){class="glboxshadow"}

## Client to client access

**Network Topology**

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Enable the client to client toggle and export a new configuration to clients, your clients can access to each other now.

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## OpenVPN Client App

Please refer to OpenVPN Official Website: [https://openvpn.net/vpn-client/](https://openvpn.net/vpn-client/){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
