# VPN Dashboard

VPN Dashboard page is for the status and setting of VPN.

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

At first, there is no configuration available for OpenVPN and WireGuard, you need to click **Set Up Now** to go to the corresponding page to configure.

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

1. Block Non-VPN Traffic

2. Allow Access WAN

3. Services From GL.iNet Doesn't Use VPN

## VPN Server
