# How to use VPN Cascading on GL.iNet routers?

## Introduction

VPN Cascading is often referred to as "Double VPN" in some contexts, but it may differ slightly on GL.iNet routers . The core concept is illustrated below.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (Router as VPN Server)**: When the router acts as a VPN server, clients connected to this server will access the internet via the router's ISP network by default.

**VPN 2 (Router as VPN Client)**: The router also acts as a VPN client, connecting to a third-party VPN service.

**VPN Cascading**: By configuring the router to forward traffic from the VPN 1 tunnel to the VPN 2 tunnel, end devices (such as laptops, desktops, and smartphones) connected to VPN 1 can access the internet through the third-party VPN service — no additional setup is required on the end devices themselves.

## How to enable VPN cascading

### For firmware v4.7 and earlier

Please follow the steps below.

1. First, set your router as a VPN server. WireGuard protocol is recommended for faster speed. Please refer to [this](../interface_guide/wireguard_server.md){target="_blank"} link.

2. Export a configuration file from your router and upload it to a client device, which will be connecting to the router via VPN.

3. Set your router as a VPN client, connecting to a third-party VPN service. WireGuard protocol is recommended for faster speed. Please refer to [this](../interface_guide/wireguard_client.md){target="_blank"} link.

4. Once connected, the **VPN Dashboard** page will display as below, where the router has been set as a VPN server, and also a VPN client, connecting to a third-party VPN service.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Turn to the VPN Server section and click on **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Enable **VPN Cascading** and click **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

### For firmware v4.8 and higher

The VPN Cascading option has been removed since firmware v4.8. 

As long as you set a router as a VPN server, which is also been set as a VPN client connecting to a third-party VPN service at the same time, in the default VPN global mode, all VPN clients connecting to the router through VPN will eventually access the Internet through the third-party VPN service – no need to enable VPN Cascading.

Take GL-AXT1800 as an example.

1. First, set the GL-AXT1800 as a WireGuard server. Please refer to [this](../interface_guide/wireguard_server.md) link.

2. Export a configuration file from GL-AXT1800 and upload it to a laptop, which will be set as a WireGuard client connecting to GL-AXT1800 via VPN.

3. Set the GL-AXT1800 as a WireGuard client, connecting to a third-party VPN service (e.g., IPVanish). Please refer to [this](../interface_guide/wireguard_client.md) link.

4. Once connected, the **VPN Dashboard** page will display as below, indicating that this router has been set as a WireGuard client connecting to a third-party VPN service.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

    The server status is displayed on the **WireGuard Server** page.

    ![vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-wgserver.jpg){class="glboxshadow"}

    Now the laptop, which has been set as a WireGuard client connecting to the GL-AXT1800 (VPN 1), will access the Internet via the third-party VPN service (VPN 2), rather than the the GL-AXT1800's ISP network.

5. **Connection Test**: On the laptop, open a browser and visit [What Is My IP](https://whatismyipaddress.com/){target="_blank"} to check its public IP. If it shows the laptop's IP address is in the region of the third-party VPN server (which is Buenos Aires in this example), it indicates that VPN cascading has taken effect.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

## Does VPN policy affect VPN Cascading

* Case 1. Policies DO NOT affect VPN Cascading

    VPN policies, including **Global Proxy**, **Based on the Target Domain or IP**, **Based on the Client Device** and **Based on the VLAN**, does not affect VPN cascading. These polices only affect on the devices connected on the router physically, i.e. in the router's own subnet.

    ![gl.inet vpn dashboard, vpn policy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/modify_vpn_policy_mode_1.png){class="glboxshadow"}

* Case 2. Policies DO affect VPN Cascading

    When you use **Auto Detect** or **Customized Routing Rules**, the routing rules comes with the VPN config or you set up will affect how the router route data so VPN cascading may not work.

    ![gl.inet vpn dashboard, vpn policy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/modify_vpn_policy_mode_2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.