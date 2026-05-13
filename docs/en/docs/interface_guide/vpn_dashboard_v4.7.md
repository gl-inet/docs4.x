# VPN Dashboard (Firmware v4.7 and earlier)

Log in to the web Admin Panel and go to **VPN** -> **VPN Dashboard**.

VPN Dashboard page displays the VPN connection details, such as server address, traffic statistics, client virtual IP, and connection log. It also allows users to configure advanced settings such as the VPN Kill Switch, VPN policy, IP Masquerading, MTU, and VPN Cascading. 

This page is devided into two sections: [VPN Client](#vpn-client) and [VPN Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN Client

When entering this page for the first time, if there is no configuration file available for OpenVPN and WireGuard, the page displays as follows. Click **Set Up Now** and you will be directed to the [OpenVPN Client](openvpn_client.md) or [WireGuard Client](wireguard_client.md) page to upload your VPN configuration file.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_setup.png){class="glboxshadow"}

Once uploaded, your configuration will be shown in the **Configuration File** column. If you have multiple configuration files uploaded, you can switch files by clicking on the box.

![configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_config.png){class="glboxshadow"}

### Client Options

Click the gear icon on the right to access OpenVPN or WireGuard client options.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options.png){class="glboxshadow"}

The OpenVPN Client Options displays as follows. 

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_ovpn.png){class="glboxshadow"}

The WireGuard Client Options displays as follows. 

![wg client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: If enabled, remote access to this router and its LAN devices via VPN will be allowed. The VPN server must advertise a route to the LAN subnet of this router.

    For example, as shown in the diagram below, the GL.iNet router runs as a VPN client and connects to a VPN server over the VPN tunnel. When this option is enabled, both the GL.iNet router and its LAN-side devices can be accessed by devices on the VPN server side (e.g. NAS). This requires you to add a routing rule on the VPN server to reach the LAN subnet of the GL.iNet router.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: If enabled, the source IP addresses of LAN clients will be rewritten to the router's VPN tunnel IP. Disable this only for Site-to-Site setups where the remote peer knows your LAN subnets.

- **MTU**: Short for Maximum Transmission Unit. This optional setting lets you customize the VPN tunnel MTU, which overrides the value defined in the configuration file.

### Proxy Mode

The default proxy mode for VPN connection is **Global Proxy**. You can click the box in the upper right to switch to other proxy modes. 

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_proxy.png){class="glboxshadow"}

Three proxy modes are available: **Global Proxy**, **Policy Mode** and **Route Mode**.

1. Global Proxy

    In this mode, all traffic will be routed through the VPN. Only one VPN client instance can be activated.

2. Policy Mode

    This mode can be further divided into three policies.

    - Based on the Target Domain or IP.
    
        In this mode, only the traffic of certain websites identified by IP address or domain name will be routed through VPN. Only one VPN client instance can be activated.

    - Based on the Client Device.

        In this mode, only the traffic of certain LAN devices identified by MAC addresses will be routed through VPN. Only one VPN client instance can be activated.

    - Based on the VLAN.

        In this mode, only the traffic of certain VLAN will be routed through VPN. Only one VPN client instance can be activated.

3. Route Mode

    - Auto Detect

        The routing rules defined in each VPN client configuration file or issued by the VPN server will be used.
    
    - Customize Routing Rules

        You can manually configure routing rules for each VPN client instance.

### Global Options

Click **Global Options** in the upper right corner to configure advanced settings for your VPN client.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: If enabled, all internet traffic is forced to pass exclusively through the VPN tunnel and cannot be routed via other interfaces such as the local ISP WAN. If the VPN connection drops unexpectedly, all internet traffic is fully blocked to prevent fallback to the regular WAN. This avoids VPN leaks caused by VPN failures, incorrect client DNS settings, and similar issues.

    This feature is also known as [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. It prevents user data from being exposed online. A typical Kill Switch automatically cuts off internet access when the VPN connection fails. The Block Non-VPN Traffic feature on GL.iNet routers provides broader leak protection and covers the following scenarios:

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applications Launched Before VPN Establishment

    6. Per-Application Traffic Leaks

- **Allow Access WAN**: If enabled, local client devices can still access WAN-side services (e.g., printers, NAS and other devices in the upstream subnet) while the VPN is active.

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    As shown in the diagram above, enabling this feature allows your local devices to reach hosts on the upstream subnet, such as printers and NAS.

    This option is primarily designed to let clients access devices within the upstream subnet. However, the router cannot distinguish upstream subnet traffic from regular Internet traffic. If client devices access resources directly via public IPs, there is a potential traffic leakage risk. For this reason, **Allow Access WAN** and **Block Non-VPN Traffic** are mutually exclusive and cannot be enabled simultaneously.

- **Services From GL.iNet Use VPN**: If enabled, GoodCloud, DDNS, and rtty services will transmit packets through VPN tunnels. This option is disabled by default, as these services normally require the device's real IP address to work properly.

## VPN Server

If the router has never been configured as an OpenVPN or WireGuard server, the page will appear as shown below. Click **Set Up Now** and you will be directed to the **OpenVPN Server** or **WireGuard Server** page to initialize your VPN server.

![vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_setup.png){class="glboxshadow"}

After the OpenVPN Server or WireGuard Server is enabled, the page will display the server status as follows.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_connected.png){class="glboxshadow"}

### Server Options

Click the gear icon on the right to access OpenVPN or WireGuard server options.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options.png){class="glboxshadow"}

The OpenVPN Server Options displays as follows. 

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_ovpn.png){class="glboxshadow"}

The WireGuard Server Options displays as follows. 

![wg server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: If enabled, resources inside the server's LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading**: If enabled, the source IP addresses of LAN clients will be rewritten to the router's VPN tunnel IP. Disable this only for Site-to-Site setups where the remote peer knows your LAN subnets.

* **MTU**: Short for Maximum Transmission Unit. The MTU value you set for the tunnel will override the MTU settings in the configuration file.

* **Client to Client**: If enabled, VPN clients connected to this server can access each other via their VPN tunnel IPs. If you want to allow clients to also access one another's LAN subnets, the VPN server must advertise corresponding routes to those remote LAN subnets.

* **Client to Client**: If enabled, VPN clients connected to this server can access each other via their VPN tunnel IPs. If you want to allow clients to also access one another's LAN subnets, you need to add routing rules on the VPN server to advertise routes to those remote LAN subnets.

### Server Route Rule

Click the route icon on the right to customize OpenVPN or WireGuard route rules as needed.

![server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule.png){class="glboxshadow"}

The OpenVPN Server Route Rule displays as follows. Click **Add Route Rule**, enter the **Target Address** and **Gateway**, then click the green check icon to apply.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

The WireGuard Server Route Rule displays as follows. Click **Add Route Rule**, enter the **Target Address** and **Gateway**, then click the green check icon to apply.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Note**: In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the VPN encrypted tunnel when accessing any network segment is determined by the routing rules you manually set.

### Global Options

Click **Global Options** in the upper right corner to configure advanced settings for your VPN server.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: If enabled, when this router acts as a VPN server and a VPN client simultaneously, remote VPN clients connected to this router's VPN server will have their traffic routed through the upstream VPN tunnel that this router is using as a VPN client. [Learn more about VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
