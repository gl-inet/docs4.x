# VPN Dashboard

Access to web Admin Panel, on the left side -> VPN -> VPN Dashboard

VPN Dashboard page is for the status and setting of VPN. There are two sectors, [VPN Client](#vpn-client) and [VPN Server](vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

In the beginning, there is no configuration available for OpenVPN and WireGuard, please click **Set Up Now**, it will go to the [OpenVPN Client](../openvpn_client) and [WireGuard Client](../wireguard_client) pages respectively.

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

### Proxy mode

![vpn proxy](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

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

![global options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/global_options.png){class="glboxshadow"}

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

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.png){class="glboxshadow" width="80%"}

    As shown above, if this feature is turned on, your device will have access to devices in the upstream subnet, such as printer and NAS.

    The main scenario is to give clients access to devices in the upstream subnet, but there is no way for the router to distinguish between the upstream subnet and the Internet, so if the traffic in the client device is accessed directly through IP, there may be a risk of leakage, so this option and Block Non-VPN Traffic are mutually exclusive.

3. Services From GL.iNet Doesn't Use VPN

    If this option is enabled, services on routers that usually require the use of a real IP will not use VPN. Including GoodCloud, DDNS, rtty.

    The main purpose of this is to use VPN Client and [GoodCloud](../cloud) / [DDNS](../ddns) at the same time. It is recommended to turn on this option if you want to use GoodCloud, otherwise the stability of GoodCloud will be affected by the VPN status. If you want to use DDNS, you must turn on this option, otherwise DDNS will point to the IP address of VPN Server.

## VPN Server

![vpn dashboard vpn server](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

### OpenVPN Server Options

Click the cog icon of OpenVPN server.

![openvpn server options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN:** If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading:** If this option is enabled, when clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* **MTU:** The MTU you set for the instance will overwrite the MTU item in the configuration file.

### OpenVPN Server Route Rule

Click the network icon of OpenVPN server.

In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the encrypted tunnel provided by the VPN when accessing any network segment is determined by the routing rules you manually set.

![openvpn server route rule](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuard Server Options

![wireguard server options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN:** If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading:** If this option is enabled, when clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* **MTU:** The MTU you set for the instance will overwrite the MTU item in the configuration file.

### WireGuard Server Route Rule

Click the network icon of WireGuard server.

In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the encrypted tunnel provided by the VPN when accessing any network segment is determined by the routing rules you manually set.

![wireguard server route rule](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
