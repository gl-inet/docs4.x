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

* If GL.iNet router is the main router in your network, this is simple, please move to the next step.
* If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a port forwarding on the main router.
* If you already have a main router, the GL.iNet router is several levels below it and you need to set up port forwarding on each level.

## Setup WireGuard Server

1. Click **Generate Configuration**

    ![openvpn server generate configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_generate_config.png){class="glboxshadow"}

2. Apply the configuration

    ![openvpn server configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_configuration.png){class="glboxshadow"}

    **Protocol:** UDP or TCP. To find out what the difference is, check out [this tutorial](../openvpn_tcp_udp/).

    **Authentication Mode:** The router will automatically generate a server and client certificate-key, and write into the configuration file when generating the client configuration file.
    There are three options Only Certificate, Only Username/Password, Username/Password and Certificate. 
    
    For **Username/Password** and **Username/Password and Certificate** option, it need add user(s).

    ![openvpn server users](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_users.png){class="glboxshadow"}

    ![openvpn server add a user](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_add_a_user.png){class="glboxshadow"}

    Then, a OpenVPN client connect to this server, it need to input the usernamd and password.

3. Export Client Configuration

    ![openvpn server configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_export_client_configuration.png){class="glboxshadow"}

4. Start OpenVPN server

    Click the Start button in the upper right corner to start OpenVPN server. Go to VPN Dashboard page to check its status.

    ![openvpn server started](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_started.png){class="glboxshadow"}
