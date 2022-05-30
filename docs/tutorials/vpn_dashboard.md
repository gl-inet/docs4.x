# VPN Dashboard

Access to web Admin Panel, on the left side -> VPN -> VPN Dashboard

VPN Dashboard page is for the status and setting of VPN.

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

In the beginning, there is no configuration available for OpenVPN and WireGuard, you need to click **Set Up Now** to go to the corresponding page to configure.

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_2.png){class="glboxshadow"}

### Proxy mode

![vpn proxy](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

1. Global proxy

    All traffic will go through VPN. Only one VPN client instance can be activated.

2. Policy mode

    - Based on the target domain or IP.
    
        In this mode, only the traffic of certain websites defined by IP address or domain name will go through VPN. Only one VPN client instance can be activated.

    - Based on the client device.

        In this mode, only the traffic of certain local client devices defined by MAC address will go through VPN. Only one VPN client instance can be activated.

    - Based on the VLAN.

        In this mode, only the traffic of certain VLAN can go through the VPN. Only one VPN client instance can be activated.

3. Route mode

    - Auto detect

        The routing rules defined in each VPN client configuration file or issued by the VPN server will be used.
    
    - Customize routing rules

        You can manually configure routing rules for each VPN client instance.

### Global Options

Click **Global Options** will popup a global options dialog.

![global options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/global_options.png){class="glboxshadow"}

1. Block Non-VPN Traffic

    If this option is enabled, all traffic from client devices trying to be sent out of the VPN tunnel will be blocked, which will effectively prevent VPN leaks due to client DNS settings, dropped VPN connections, client apps requesting by IP, etc.

2. Allow Access WAN

    If this option is enabled, while VPN is connected, client devices will still be able to access WAN, e.g. accessing your printer, NAS etc in upper subnet.

3. Services From GL.iNet Doesn't Use VPN

    If this option is enabled, services on routers that usually require the use of a real IP will not use VPN. Including GoodCloud, DDNS, rtty.

## VPN Server

### OpenVPN Server Options

Click the cog icon of OpenVPN server.

![openvpn server options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN:** If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading:** If this option is enabled, when clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* **MTU:** The MTU you set for the instance will overwrite the MTU item in the configuration file.

### OpenVPN Server Route Rule

In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the encrypted tunnel provided by the VPN when accessing any network segment is determined by the routing rules you manually set.

![openvpn server route rule](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuard Server Options

![wireguard server options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN:** If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.

* **IP Masquerading:** If this option is enabled, when clients devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.

* **MTU:** The MTU you set for the instance will overwrite the MTU item in the configuration file.

### WireGuard Server Route Rule

In customize routes mode, the VPN client will ignore the configuration file and the routing configuration issued by the server. Whether to use the encrypted tunnel provided by the VPN when accessing any network segment is determined by the routing rules you manually set.

![wireguard server route rule](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}
