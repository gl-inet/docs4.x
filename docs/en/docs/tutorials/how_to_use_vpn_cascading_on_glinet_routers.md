# How to use VPN Cascading on GL.iNet routers?

## Introduction

VPN Cascading is often referred to as "Double VPN" in some contexts, but it may differ slightly on GL.iNet routers . The core concept is illustrated below.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (Router as VPN Server)**: When the router acts as a VPN server, clients connected to this server will access the internet via the router's ISP network by default.

**VPN 2 (Router as VPN Client)**: The router also acts as a VPN client, connecting to a third-party VPN service.

**VPN Cascading**: The router will forward traffic from the VPN 1 tunnel to the VPN 2 tunnel, allowing devices connected to the router via VPN 1 to access the internet through the third-party VPN service (VPN 2) instead of the router's ISP network.

## How to enable VPN Cascading

### For firmware v4.7 and earlier

1. First, set your router as a VPN server. WireGuard protocol is recommended for faster speed. Please refer to [this link](../interface_guide/wireguard_server.md){target="_blank"}.

2. Export a configuration file from your router and upload it to a client device, which will be connecting to the router via VPN.

3. Set your router as a VPN client, connecting to a third-party VPN service. WireGuard protocol is recommended for faster speed. Please refer to [this link](../interface_guide/wireguard_client.md){target="_blank"}.

4. Once connected, the **VPN Dashboard** page will display as below, where the router has been set as a VPN server and a VPN client simultaneously.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Turn to the VPN Server section on the same page and click **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Enable **VPN Cascading** and click **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. The VPN Cascading is enabled. Devices connected to your router via VPN will access the Internet through the third-party VPN service, instead of the router's ISP network.

### For firmware v4.8 and higher

1. First, set your router as a VPN server. WireGuard protocol is recommended for faster speed. Please refer to [this link](../interface_guide/wireguard_server.md){target="_blank"}.

2. Export a configuration file from your router and upload it to a client device, which will be connecting to the router via VPN.

3. Set your router as a VPN client, connecting to a third-party VPN service. WireGuard protocol is recommended for faster speed. Please refer to [this link](../interface_guide/wireguard_client.md){target="_blank"}.

4. In the web admin panel, navigate to **VPN Dashboard**. Choose the corresponding instructions below based on your VPN mode.

    ??? "Global Mode"
    
        If your VPN mode is Global Mode, once the VPN client is enabled (as shown below), the VPN Cascading will be enabled automatically. 
        
        Devices connected to your router via VPN will access the Internet through the third-party VPN service, instead of the router's ISP network.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"
    
        If your VPN mode is Policy Mode, you need to set up the VPN tunnel rule.
        
        Click the greyed-out box on the left.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        Select the traffic source to apply to this rule. To enable VPN Cascading, please select **All Clients**, or select **Specified Connection Types** and then **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: It includes all LAN devices, devices from Drop-in Gateway, devices from Guest network, and devices connected to your router via VPN. 
        
            If you want the traffic from all devices to apply the same tunnel rule, select **All Clients** and click **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: It allows you to specify those devices connected to the router through a specific method (e.g., devices connected via VPN) to apply this tunnel rule. 

            If you want to specify the VPN clients of your router to apply different rule from other devices, select **WireGuard/OpenVPN Server** and click **Apply**.
        
            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}
            
            This is an example of VPN tunnel rules in Policy Mode.
            
            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. The VPN Cascading is enabled. Devices connected to your router via VPN will access the Internet through the third-party VPN service, instead of the router's ISP network.

6. **Connection Test**: On a laptop connected to the router via VPN, open a browser and visit [What Is My IP](https://whatismyipaddress.com/){target="_blank"} to check its public IP. 

    If it shows the laptop's IP address is in the region of the third-party VPN server (which is Buenos Aires in this instruction), it indicates that VPN Cascading has taken effect.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.