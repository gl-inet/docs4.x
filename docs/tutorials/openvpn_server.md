# Setup OpenVPN Server on GL.iNet router

OpenVPN is an open-source VPN protocol that makes use of virtual private network (VPN) techniques to establish safe site-to-site or point-to-point connections. 

GL.iNet routers have pre-installed OpenVPN Client and Server.

We recommend WireGuard over OpenVPN because it is much faster. For setup a WireGuard Server, please check out [here](../wireguard_server).

---

## Make sure Internet Service Provider assigns you a public IP address

Please check if you Internet Service Provider assigns you a public IP address [here](../how_to_check_if_isp_assigns_you_a_public_ip_address).

**If no, you can't connect to the OpenVPN Server.**

An alternative method is to use a reverse proxy solution, we suggest [AstroRelay](https://www.astrorelay.com/){target="_blank"}.

## Network Topology

* If GL.iNet router is the main router in your network, this is simple, please move to the [next step](#setup-openvpn-server).
* If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a port forwarding on the main router.
* If you already have a main router, the GL.iNet router is several levels below it and you need to set up port forwarding on each level.

## Setup OpenVPN Server

1. Click **Generate Configuration**

    ![openvpn server generate configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_generate_config.png){class="glboxshadow"}

2. Apply the configuration

    ![openvpn server configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_configuration.png){class="glboxshadow"}

    If you do not need to modify the configuration, please click directly the **Export Client Configuration** at the bottom of page. If you have modified the configuration, please click the **Apply** button to continue.

    * **Protocol:** UDP or TCP. To find out what the difference is, check out [this tutorial](../openvpn_tcp_udp/).

    * **Authentication Mode:** There are three options **Only Certificate**, **Only Username/Password**, **Username/Password and Certificate**. 
    
        For **Username/Password** and **Username/Password and Certificate** options, they need add user(s). Then, if a OpenVPN client connect to this server, it need to input the username and password.

        ![openvpn server users](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_users.png){class="glboxshadow"}

        Created a user.

        ![openvpn server add a user](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_add_a_user.png){class="glboxshadow"}

        For **Only Certificate** and **Username/Password and Certificate**, the router will automatically generate a server and client certificate-key, and write into the configuration file when generating the client configuration file.

3. Export Client Configuration

    If your network's public IP changes from time to time, you can enable [DDNS](../ddns/) by using DDNS domain in the configuration. Click **Download** to export the configuration for further setup.

    ![openvpn server configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_export_client_configuration.png){class="glboxshadow"}

4. Start OpenVPN server

    Click the **Start** button in the upper right corner on OpenVPN Server page to start the server. Then go to [VPN Dashboard page](../vpn_dashboard#vpn-server) to check its status and other settings.

    ![start openvpn server](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/start_openvpn_server.png){class="glboxshadow"}
