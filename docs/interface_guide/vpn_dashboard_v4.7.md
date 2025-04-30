# VPN Dashboard (Firmware v4.7 and earlier)

Access to web Admin Panel, on the left side -> VPN -> VPN Dashboard

VPN Dashboard page is for the status and setting of VPN. There are two sectors, [VPN Client](#vpn-client) and [VPN Server](#vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

In the beginning, there is no configuration available for OpenVPN and WireGuard, please click **Set Up Now**, it will go to the [OpenVPN Client](openvpn_client.md) and [WireGuard Client](wireguard_client.md) pages respectively.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

Once the configuration is complete, you can select the configuration file in the Configuration file column.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### VPN Client Options

Click the cog icon of OpenVPN or WireGuard.

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

OpenVPN client options.

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

WireGuard client options.

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* Allow Remote Access LAN

    If this option is enabled, the devices connected under the router is allowed to access the LAN on the VPN Server side, which also requires the appropriate settings on the VPN Server side.

    For example, in the image below, if this option is enabled, if means *Your Device* is allowed to access the *NAS*, but still needs the *VPN Server* to allow you to access the NAS within its subnet.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* IP Masquerading

    If this option is enabled, When clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* MTU

    Stands for maximum transmission unit. The MTU you set for the instance will overwrite the MTU item in the configuration file.

### Proxy mode

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

As the above figure, the current proxy mode is Global Proxy, click Global Proxy to switch to other proxy modes. There are 3 types, **Global Proxy**, **Policy Mode** and **Route Mode**.

1. Global Proxy

    All traffic will go through VPN. Only one VPN client instance can be activated.

2. Policy Mode

    1. Based on the target domain or IP.
    
        In this mode, only the traffic of certain websites defined by IP address or domain name will go through VPN. Only one VPN client instance can be activated.

    2. Based on the client device.

        In this mode, only the traffic of certain local client devices defined by MAC address will go through VPN. Only one VPN client instance can be activated.

    3. Based on the VLAN.

        In this mode, only the traffic of certain VLAN can go through the VPN. Only one VPN client instance can be activated.

3. Route Mode

    1. Auto detect

        The routing rules defined in each VPN client configuration file or issued by the VPN server will be used.
    
    2. Customize routing rules

        You can manually configure routing rules for each VPN client instance.

### Global Options of VPN Client

Click **Global Options** will popup a global options dialog.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Block Non-VPN Traffic

    If this option is enabled, all traffic from client devices trying to be sent out of the VPN tunnel will be blocked, which will effectively prevent VPN leaks due to client DNS settings, dropped VPN connections, client apps requesting by IP, etc.

    This feature is also know as [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. It is designed to prevent your data from leaking to the web. Most VPN providers offer a Kill Switch feature that automatically disconnects your computer, phone, or tablet from the internet if your VPN connection drops. The Block Non-VPN Traffic feature on GL.iNet rotuers can handle more ways to compromise, including the following six scenarios:

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. Dropped VPN Connection

    5. Programs Started Before VPN

    6. Application Specific Leaks

2. Allow Access WAN

    If this option is enabled, while VPN is connected, client devices will still be able to access WAN, e.g. accessing your printer, NAS etc in upper subnet.

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    As shown above, if this feature is turned on, your device will have access to devices in the upstream subnet, such as printer and NAS.

    The main scenario is to give clients access to devices in the upstream subnet, but there is no way for the router to distinguish between the upstream subnet and the Internet, so if the traffic in the client device is accessed directly through IP, there may be a risk of leakage, so this option and Block Non-VPN Traffic are mutually exclusive.

3. Services From GL.iNet Use VPN

    If this option is enabled, services on routers that usually require the use of a real IP will use VPN. Including GoodCloud, DDNS, rtty. Rtty include the **Remote SSH** and **Remote Web Access** in [GoodCloud page](cloud.md#enable-goodcloud-on-router).

    The main purpose of this is to use VPN Client and [GoodCloud](cloud.md) / [DDNS](ddns.md) at the same time. It is recommended to turn off this option if you want to use GoodCloud, otherwise the stability of GoodCloud will be affected by the VPN status. If you want to use DDNS, you must turn off this option, otherwise DDNS will point to the IP address of the VPN Server.

## VPN Server

In the beginning, both VPN Server are not initialized yet, please click **Set Up Now**, it will go to the [OpenVPN Server](openvpn_server.md) and [WireGuard Server](wireguard_server.md) pages respectively.

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

After the OpenVPN Server and WireGuard Server are started.

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### OpenVPN Server Options

Click the cog icon of OpenVPN server.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading**

    If this option is enabled, when clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* **MTU**

    The MTU you set for the instance will overwrite the MTU item in the configuration file.

### OpenVPN Server Route Rule

Click the network icon of OpenVPN server.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the encrypted tunnel provided by the VPN when accessing any network segment is determined by the routing rules you manually set.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuard Server Options

Click the cog icon of WireGuard server.

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading**

    If this option is enabled, when clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* **MTU**

    The MTU you set for the instance will overwrite the MTU item in the configuration file.

* **Client to Client**

    Wireguard clients can access data from each other, not side to side, users can access internal network devices at home or in the office while remote, and the data access of the wireguard server is safer than port forwarding due to encrypted processes, and once connected, the process is more stable and faster.

### WireGuard Server Route Rule

Click the network icon of WireGuard server.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the encrypted tunnel provided by the VPN when accessing any network segment is determined by the routing rules you manually set.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### Global Options of VPN Server

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPN Cascading**, If this option is enabled, when you have both VPN server and VPN Client running on this router, clients connected to the VPN server will further be routed to the VPN client tunnel. [Learn more about VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
