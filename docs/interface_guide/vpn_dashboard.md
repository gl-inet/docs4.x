# VPN Dashboard

**Note**: This guide is based on firmware v4.8. For earlier versions, please refer to [here](vpn_dashboard_v4.7.md).

---

On the left side of the web Admin Panel, go to **VPN** -> **VPN Dashboard**. 

The VPN dashboard displays VPN connection details, such as tunnel rules, server address, traffic statistics, client virtual IP, and connection log, and allows users to configure advanced settings such as the VPN Kill Switch, IP Masquerading, and MTU. 

You can also activate multiple VPN connections for multi-tunnel scenarios.

## Setup Wizard

Click the book icon in the upper left and follow the VPN Setup Wizard to complete the VPN configuration quickly.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Note**: The VPN Setup Wizard is only for the integrated VPN services, including AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA and Surfshark. For other VPN services, skip the wizard and go to [OpenVPN Client](openvpn_client.md){target="_blank"} or [WireGuard Client](wireguard_client.md){target="_blank"} to set up VPN manually. 

Here's an example with **Hide.me**. Log in with Hide.me credentials.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Select a VPN server and click **Apply**. This is the server you will connect to via this VPN tunnel, and your public IP address will appear to be from the selected server's location.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

It will connect automatically. Once connected successfully, go to the VPN Dashboard and you will see a VPN Tunnel has been enabled. 

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

It displays the currently used VPN protocol (e.g., WireGuard), the configuration file, server address, server listen port, traffic statistics, and client virtual IP. Users can view the connection log in the bottom right.

All connected clients will access the Internet via this VPN tunnel.

If you want to configure VPN policy, please refer to [Policy Mode](#policy-mode).

## VPN Mode

On the VPN Dashboard, click the button in the upper right corner to switch VPN modes.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Two modes are available: **Global Mode** and **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Global Mode

In this mode, all traffic is routed through the VPN tunnel, and only one VPN client instance can be activated.

It is ideal for scenarios where all client traffic is routed through a single VPN server, such as unified network security or region‑specific content access.

In the following example, the router connects to an Australian server using the WireGuard protocol. All traffic from connected clients will be routed through this VPN tunnel.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### Policy Mode

In this mode, the router can connect to multiple VPN servers, and you can customize routing rules for different clients or traffic destinations.

It is suitable for use cases requiring flexible traffic management, such as routing different traffic to different destinations through multiple VPN servers.

Switch the VPN Mode to Policy Mode, and click **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

After switching, if the VPN is not enabled, the page displays as below, including three sections: Primary Tunnel, Add Tunnel, and All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Click the corresponding section to learn more.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Primary Tunnel

The primary tunnel is a <u>preset</u> tunnel in Policy Mode. It has the top priority, and you can modify [tunnel priority](#tunnel-priority) if there is more than one tunnel.

In this tunnel, you can customize the tunnel rule by setting three factors: 

1. **From**: It refers to the traffic source, i.e., the traffic that should be routed via this tunnel.

    Click the greyed-out box to select the traffic source.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}
        
    - **All Clients**: If selected, traffic from all devices will match this rule.
        
        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: If selected, traffic from specified connection types (e.g., LAN subnet, Drop-in Gateway, Guest Network) will match this rule.
        
        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        If you have enabled the OpenVPN server or WireGuard server on this router, there will be more options under the Specified Connection Types. This is useful for [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: If selected, traffic from specified devices (identified by MAC address) will match this rule.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: If selected, traffic from specified devices (identified by MAC address) will **NOT** match this rule.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: It refers to the traffic destinations.

    Click the greyed-out box to select the traffic destinations. 

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}
    
    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: If selected, traffic matching this rule will be routed to all targets.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}
    
    - **Specified Domain / IP List**: If selected, traffic matching this rule will be routed to specified domains or IP addresses. You need to enter them manually.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Or switch the **Input Mode** from Manual to Subscription URL, and input URL Link. 

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note
        
            - If you select Subscribe URL, the domain name or IP in the URL is automatically updated every day. 

            - Make sure to enter the correct URL. The URL detection will verify the validity of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: If selected, traffic matching this rule will **NOT** be routed to specified domains or IP addresses. You need to enter them manually.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Or switch the **Input Mode** from Manual to Subscription URL and input URL Link.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"} 

        !!! Note
        
            - If you select Subscribe URL, the domain name or IP in the URL is automatically updated every day. 

            - Make sure to enter the correct URL. The URL detection will verify the validity of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: It refers to the traffic routing method, i.e., whether to use VPN.

    Click the greyed-out box to select the routing method. 

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: If selected, traffic matching this rule will be routed to the selected destinations through VPN.
        
        To begin with, you need to configure your router as a VPN client. Use the [VPN Setup Wizard](#vpn-setup-wizard) to quickly complete the configuration, or navigate to OpenVPN Client / WireGuard Client in the left sidebar to configure manually.

        Once you set the router as a VPN client, select a VPN configuration file for this tunnel, and click **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: If selected, traffic matching this rule will be routed to the selected destinations via local WAN instead of the VPN.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. After selecting the traffic source, destination, and routing method, the primary tunnel rule setup is complete. 

In the following example, the Primary Tunnel rule is: All clients use the VPN to access specified domains. Their traffic is routed through the Australian server and exits to the selected Internet domains via this tunnel.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Note**: For security, please go to [All Other Traffic](#all-other-traffic) and [Tunnel Options](#tunnel-options) to check other settings before enabling the tunnels.

#### Add Tunnel

To create additional tunnels for multiple VPN instances, click **Add Tunnel** below the Primary Tunnel and configure custom rules.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Name the tunnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

You will get one more tunnel on the VPN Dashboard. 

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

You can add more tunnels if needed. Up to 5 tunnels can be created (including the preset primary tunnel).

Customize the tunnel rules by setting the traffic source, destinations and routing method. Please refer to the [Primary Tunnel](#primary-tunnel).

**Note**: For security, please go to [All Other Traffic](#all-other-traffic) and [Tunnel Options](#tunnel-options) to check other settings before enabling the tunnels.

#### All Other Traffic

In Policy Mode, a <u>pre-enabled</u> tunnel is displayed at the bottom of the VPN Dashboard.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

This tunnel controls whether traffic that does not match any of the above VPN tunnel groups can access the Internet. It is enabled by default to ensure normal Internet access for traffic not routed via VPN.

- When enabled, unmatched traffic can still access the Internet.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- When disabled, only traffic routed via VPN is allowed to access the Internet. All non-VPN traffic and traffic that fails over from VPN connections will be blocked. This option does not override the individual Kill Switch for each VPN tunnel.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Tunnel Priority

By default, the preset Primary Tunnel has the top priority, followed by other manual-added tunnel (if any), then the All Other Traffic tunnel to ensure local network connectivity (via local WAN).

To modify tunnel priority, click **Modify Priority** in the top info bar, or click the **priority label** in the top left of any tunnel (e.g., Priority 1/Priority 2).

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Click and hold the three-line icon on the right to reorder the tunnels, and click **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router will route traffic in the following order**:

1. Traffic will first attempt to match the highest-priority tunnel rule. If matched, it will be routed through that tunnel; otherwise, it will try the next priority tunnel, and so on, until it matches the "All Other Traffic" tunnel.

2. If a VPN tunnel disconnects unexpectedly, the system will determine whether to fail over the traffic to the next priority tunnel based on whether this tunnel's **Kill Switch** is enabled.

    - If the Kill Switch is enabled, traffic will be blocked and will not fail over to the next priority tunnel.
    - If the Kill Switch is disabled, traffic will fail over to the next priority tunnel and attempt to match its tunnel rules.

3. The **All Other Traffic** tunnel is enabled by default to ensure that traffic not matching the VPN tunnels can still access the Internet.

    - If enabled, it routes unmatched or failover traffic through the local WAN.
    - If disabled, it strengthens the Kill Switch and blocks regular Internet access to prevent IP leaks.

#### Tunnel Options

You can configure advanced settings for each VPN tunnel, such as the VPN Kill Switch, IP Masquerading, and MTU.

Click the gear icon next to a tunnel name and select **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: If enabled, traffic matching this VPN tunnel will be blocked if the VPN connection fails unexpectedly. If disabled, such traffic will fail over to the next priority tunnel or local WAN.

- **Services from GL.iNet Use VPN**: If enabled, GoodCloud, DDNS, and rtty services will transmit packets through VPN tunnels. This option is disabled by default, as these services normally require the device's real IP address to work properly.

- **Allow Remote Access the LAN Subnet**: If enabled, remote access to this router and its LAN devices through the VPN will be allowed. It requires the VPN server to advertise a route back to its LAN subnet.

- **IP Masquerading**: If enabled, the source IP addresses of LAN clients will be rewritten to the router's VPN tunnel IP. Disable this only for Site-to-Site setups where the remote peer knows your LAN subnets.

- **MTU**: The MTU value you set for the tunnel will override the MTU settings in the configuration file.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.