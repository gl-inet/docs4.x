# Set Up OpenVPN Server on GL.iNet Router

OpenVPN is an open-source VPN protocol that makes use of virtual private network (VPN) techniques to establish safe site-to-site or point-to-point connections. 

We recommend WireGuard over OpenVPN because it is much faster. For setup a WireGuard Server, please check out [here](wireguard_server.md).

---

## Make sure Internet Service Provider assigns you a public IP address

Please check if you Internet Service Provider assigns you a public IP address [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

**If not, you can't connect to the OpenVPN Server.**

An alternative method is to use a reverse proxy solution, we suggest [AstroRelay](https://www.astrorelay.com/){target="_blank"}.

## Network Topology

* If GL.iNet router is the main router in your network, this is simple, please move to the [next step](#setup-openvpn-server).
* If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a port forwarding on the main router.
* If you already have a main router, the GL.iNet router is several levels below it and you need to set up port forwarding on each level.

## Setup OpenVPN Server

1. Click **Generate Configuration** (Only the first time).

    ![openvpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_generate_config.png){class="glboxshadow"}

2. Apply the configuration.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_configuration.png){class="glboxshadow"}

    If you do not need to modify the configuration, please click directly the **Export Client Configuration** at the bottom of page. If you have modified the configuration, please click the **Apply** button to continue.

    * **Device Mode:** TAP-S2S or Tun. To find out what the difference is, check out [tap s2s vs tun](../tutorials/tap_s2s_vs_tun.md).

    * **Protocol:** UDP or TCP. To find out what the difference is, check out [tcp vs udp](../faq/openvpn_tcp_udp.md).

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

    Click the **Start** button in the upper right corner on OpenVPN Server page to start the server. Then go to [VPN Dashboard page](vpn_dashboard.md#vpn-server) to check its status and other settings.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_openvpn_server.png){class="glboxshadow"}

## To check if OpenVPN Server is working properly

Many people mis-understandstool once they saw the server is up and think it is connected. The server can be up even you forward a wrong port or wrong address.

![openserverup](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

To check if OpenVPN Server is working properly, we can use another device connected to another network and use the OpenVPN configuration we exported earlier, to connect and see whether it connects properly and whether the IP address is the IP of OpenVPN Server.

The simpliest way is to use a cell phone with [OpenVPN official client app](https://openvpn.net/vpn-client/){target="_blank"} installed, turn off its Wi-Fi connection, and only connect to Internet via 3G/4G/5G. Then open the OpenVPN app, import the OpenVPN configuration we previously exported. Enable the connection, check if the phone has Internet access and whether its IP address is the IP of your OpenVPN Server.

When importing the configuration file to the OpenVPN app, it may has a reminder as below, please click **CONTINUE** as the certificate is already included in the configuration file.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow"}

There are several common reasons cause failed:

* The Internet Service Provider doesn't assign you a public IP address, please check [here](#make-sure-internet-service-provider-assigns-you-a-public-ip-address).
* You may need setup port forwarding, please check [here](#network-topology).
* The port you are using for OpenVPN Server is blocked by the Internet Service Provider, change to another port, or contact the Internet Service Provider.
* Some countries/regions may block the VPN connection.

## Advanced Configuration

You can modify your own configuration at this tab.

![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_advanced_configuration.png){class="glboxshadow"}

## Client to client access

### Network Topology

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Enable the client to client toggle and export a new configuration to clinets, your clients can be access to each others now.

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## OpenVPN Client App

We can use another GL.iNet router as OpenVPN Client, or use their official app on other devices with various OS.

- Please refer to OpenVPN Official Website: [https://openvpn.net/vpn-client/](https://openvpn.net/vpn-client/){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
