# VPN Cascading

## How VPN Cascading works

VPN Cascading is also called double VPN in various scenarios. But GL.iNet VPN Cascading may be a little different. Please refer to the following figure for the idea.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/en/4/tutorials/vpn_cascading/vpn_cascading.png){class="glboxshadow"}

**VPN 1**: The router is used as VPN server. Clients connected to this server will go to Internet using the router's ISP Network by default.

**VPN 2**: The router is used as VPN client to 3rd party VPN services.

**VPN Cascading**: You can forward data of VPN1 tunnel to VPN2 tunnel. So when the Laptop, Desktop and Smartphones (end devices) connected on VPN1 will go to 3rd party VPN services, without any other setup in these end devices.

## How to enable VPN cascading

The following figure has OpenVPN and Wireguard servers enabled on the router. And also connect to NordVPN via OpenVPN protocol.

![gl.inet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_cascading/vpn_dashboard.png){class="glboxshadow"}

You can enable VPN cascading in **Global Options** in VPN server section.

![gl.inet enable vpn cascading](https://static.gl-inet.com/docs/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

## Does VPN policy affect VPN Cascading

* Policies DO NOT affect VPN Cascading

    VPN policies, including **Global Proxy**, **Based on the Target Domain or IP**, **Based on the Client Device** and **Based on the VLAN**, does not affect VPN cascading. These polices only affect on the devices connected on the router physically, i.e. in the router's own subnet.

    ![gl.inet vpn dashboard, vpn policy](https://static.gl-inet.com/docs/en/4/tutorials/vpn_cascading/modify_vpn_policy_mode_1.png){class="glboxshadow"}

* Policies DO affect VPN Cascading

    When you use **Auto Detect** or **Customized Routing Rules**, the routing rules comes with the VPN config or you set up will affect how the router route data so VPN cascading may not work.

    ![gl.inet vpn dashboard, vpn policy](https://static.gl-inet.com/docs/en/4/tutorials/vpn_cascading/modify_vpn_policy_mode_2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.