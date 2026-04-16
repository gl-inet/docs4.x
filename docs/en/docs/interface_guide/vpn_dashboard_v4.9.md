# VPN Dashboard (Firmware v4.9)

On the left side of the web Admin Panel, go to **VPN** -> **VPN Dashboard**. 

The VPN dashboard displays VPN connection details, such as routing rules, connected server, traffic statistics, client virtual IP, and connection log, and allows users to configure advanced settings such as the VPN Kill Switch, IP Masquerading, and MTU.

Compared to firmware v4.8, v4.9 includes the following improvements to the VPN Dashboard:

1. **Allow users to select multiple profiles within a tunnel group and set their priority**. The tunnel will attempt to connect using each profile in priority order until a connection is successfully established.

2. **Each tunnel group operates independently and does not perform failover between groups**. If all profiles in a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and the All Other Traffic tunnel.

## Getting Started

When entering this page for the first time, if no tunnels have been created, the page will appear as shown below. Click **Add VPN Tunnel** to get started.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

You will be directed to the **VPN Client Profile** page. Select a VPN provider and log in. 

The VPN providers listed are integrated into the GL.iNet router web Admin Panel. With an active subscription, users simply enter their credentials to log in instantly and obtain configuration files for VPN connections.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

If you have subscribed to other VPN providers, or if you want to upload your personal VPN configurations, click **Add Manually** and upload your configurations.

Take **PureVPN** as an example. Click PureVPN and log in with valid credentials.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

You will obtain a list of VPN profiles. For some VPN service providers, you may need to select a VPN protocol or preferred servers/cities before the list of profiles appears.

Then click **Go to Dashboard** at the bottom. You will be directed to the VPN Dashboard to add your VPN tunnel and set up VPN policy.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

??? "What is VPN policy?"

    A VPN policy defines how network traffic is routed through VPN tunnels, determining which traffic goes to target destinations via VPN and which accesses the Internet directly through the local WAN.

    It allows all clients or specific devices to access designated websites or the entire Internet over a VPN connection, enabling flexible and secure network management.

On the VPN Dashboard, follow the setup wizard to configure your VPN policy, including selecting VPN profile, traffic source, and traffic destination.

1. **Select the VPN profile.** 

    If you have previously logged in with any integrated VPN service credentials or uploaded a configuration file, the available profiles will be listed here. Otherwise, go to **VPN Client Profile** to log in with your credentials or upload a configuration file manually.

    Take [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} as an example. Select one or multiple profiles, and adjust their priority on the right as needed. 

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) policy.

2. **Select the client source.** 

    There are four options:

    - **All Clients**: If selected, traffic from all devices will match this rule.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: If selected, traffic from specified connection types (e.g., LAN subnet, Drop-in Gateway, Guest Network) will match this rule.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: If selected, traffic from specified devices (identified by MAC address) will match this rule.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: If selected, traffic from specified devices (identified by MAC address) will not match this rule.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

3. **Select the target destination**. 

    There are three options:

    - **All Targets**: If selected, traffic matching this rule will be routed to all targets.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: If selected, traffic matching this rule will be routed to specified domains or IP addresses. You need to enter them manually.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: If selected, traffic matching this rule will not be routed to specified domains or IP addresses. You need to enter them manually.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

## Usage Scenarios

Here are two scenarios with step-by-step setup instructions for your reference.

### Scenario 1

**Objectives**:

1. Only specific devices connected to this router access the Internet through the VPN. All other devices access the Internet through the local WAN.

2. The selected devices must use the VPN connection only. If the VPN disconnects unexpectedly, Internet access for these devices will be blocked to prevent DNS leaks and IP tracking.

**Follow the steps below to configure the VPN policy.**

1. Select the VPN profile. 

    If you have logged in with any integrated VPN service credentials or uploaded a configuration file, the available profiles will be listed here. Otherwise, go to **VPN Client Profile** to log in with your credentials or upload a configuration file manually.

    Take [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} as an example. Select one or multiple profiles, and adjust their priority on the right as needed. 

    ![scenario 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) policy.

2. Select Client Source.

    Click the **Specified Devices** tab, select the devices that will use the VPN, then click **Apply**.

    ![scenario 1 select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

3. Select Target Destination.

    Click the **All Targets** tab, set it as the traffic destination, then click **Apply**.

    ![scenario 1 select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. You will be directed to the VPN Dashboard, where a VPN tunnel has been added. 

    ![scenario 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

5. Make sure the **Kill Switch** for this tunnel is enabled. If the VPN disconnects unexpectedly, Internet access for traffic matching this tunnel will be blocked to prevent DNS leaks and IP tracking.

    ![scenario 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

    ![scenario 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}
    
6. Make sure the **Allow Non-VPN Traffic** is enabled. This is enabled by default to ensure that traffic not matching the VPN tunnel can still access the Internet through the local WAN.

    ![scenario 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

7. Click the middle button to activate this tunnel.

    ![scenario 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

8. Once connected, the page will display the VPN connection details, including VPN policy, traffic statistics, server address, listen port, and virtual IP address.

    ![scenario 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

    Now, only two specified devices access the Internet through VPN. If the VPN disconnects unexpectedly, Internet access for these devices will be blocked to prevent DNS leaks and IP tracking. All other devices will access the Internet through the local WAN instead.

### Scenario 2

**Objectives:** 

1. All devices use **VPN Tunnel 1** when accessing domains of specific social media and streaming services, and use **VPN Tunnel 2** for all other Internet access.

2. If the VPN tunnels disconnect unexpectedly, Internet access for all devices will be blocked to prevent DNS leaks and IP tracking.

**Follow the steps below to configure the VPN policy.**

1. Select the VPN profile for Tunnel 1. 

    Take [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} as an example. Select one or multiple profiles, and adjust their priority on the right as needed.

    ![scenario 2 select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) policy.

2. Select Client Source.

    Click the **All Clients** tab, set it as the client source for Tunnel 1, then click **Apply**.

    ![scenario 2 select source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Select Target Destination.

    Click the **Specified Domain / IP List** tab, enter domains of some common social media and streaming services, as shown below, then click **Apply**.

    ![scenario 2 select target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

4. You will be directed to the VPN Dashboard, where the Tunnel 1 has been added. 

    ![scenario 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

5. Make sure the **Kill Switch** for Tunnel 1 is enabled. If the VPN disconnects unexpectedly, Internet access for traffic matching this tunnel will be blocked to prevent DNS leaks and IP tracking.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}
    
6. Click **Add New Tunnel** to add Tunnel 2.

    ![scenario 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

7. Select the VPN profile for Tunnel 2. 

    Take [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} as an example. Select one or multiple profiles, and adjust their priority on the right as needed.

    ![scenario 2 select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) policy.

8. Select Click Source.

    Click the **All Clients** tab, set it as the client source for Tunnel 2, then click **Apply**.

    ![scenario 2 select source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. Select Target Destination.

    Click the **All Targets** tab, set it as the traffic destination for Tunnel 2, then click **Apply**.

    ![scenario 2 select target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

10. You will be directed to the VPN Dashboard, where the Tunnel 2 has been added. 

    ![scenario 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

11. Make sure the **Kill Switch** for Tunnel 2 is enabled. If the VPN disconnects unexpectedly, Internet access for traffic matching this tunnel will be blocked to prevent DNS leaks and IP tracking.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

12. Click the gear icon at the upper right and enable **Enhanced Kill Switch**. This ensures that all traffic must access Internet via the VPN.

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

13. Click the middle button to activate Tunnel 1 and Tunnel 2.

    ![scenario 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

14. Once connected, the page will display the VPN connection details, including VPN policy, traffic statistics, server address, listen port, and virtual IP address.

    ![scenario 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

    Now, all devices will use **VPN Tunnel 1** when accessing specified domains, and use **VPN Tunnel 2** for all other Internet access. If the VPN tunnels disconnect unexpectedly, Internet access for all devices will be blocked to prevent DNS leaks and IP tracking.

## All Other Traffic

Click the gear icon at the upper right to set up policy for those traffic not matching VPN tunnel.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

This policy controls whether traffic that does not match any of your VPN tunnel groups can access the Internet or not. It has two options: **Allow Non-VPN Traffic** and **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: Enabled by default to ensure normal internet access for non-VPN traffic.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Forces all devices to access the Internet through a VPN. Any traffic that does not match a VPN tunnel will be blocked. This global setting does not override the Kill Switch configured for individual VPN tunnels.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel Priority

To adjust tunnel priority, click the gear icon in a tunnel group and select **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Click and hold the three-line icon on the right to reorder the tunnels, then click **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router routes traffic according to the following rules**:

1. Traffic will first attempt to match the highest-priority tunnel rule. If matched, it will be routed through that tunnel; otherwise, it will try the next priority tunnel, and so on.

2. Each tunnel group operates independently. Once traffic matches a tunnel rule, it will be routed through that tunnel and will not fail over between tunnel groups.

3. Multiple profiles can be selected within each tunnel group to enable intra-tunnel failover. When the highest-priority profile in a tunnel group goes down, the tunnel will automatically connect using the second-highest priority profile, and so on.

4. If a VPN tunnel disconnects unexpectedly, the system will determine whether to fail over the traffic to the All Other Traffic tunnel based on whether this tunnel's **Kill Switch** is enabled. 

    - If the Kill Switch is enabled, traffic will be blocked and will not fail over to the All Other Traffic tunnel.
    - If the Kill Switch is disabled, traffic will fail over to the All Other Traffic tunnel.

5. In the **All Other Traffic** tunnel, different modes determine whether the traffic that does not match the VPN tunnel can access the Internet.

    - **Allow Non-VPN Traffic**: It is enabled by default to ensure that traffic not matching the VPN tunnels can still access the Internet via local WAN.

    - **Enhanced Kill Switch**: It forces all devices to access the Internet through a VPN. Any traffic that does not match a VPN tunnel will be blocked. This global setting does not override the Kill Switch configured for individual VPN tunnels. In short, it strengthens the Kill Switch and blocks regular Internet access to prevent IP leaks. 

## Tunnel Options

You can configure advanced settings for each VPN tunnel, such as the VPN Kill Switch, IP Masquerading, and MTU.

Click the gear icon in a tunnel group, and select **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: If enabled, traffic matching this VPN tunnel will be blocked if the VPN connection fails unexpectedly. If disabled, such traffic will fail over to the **All Other Traffic** tunnel.

- **Services from GL.iNet Use VPN**: If enabled, GoodCloud, DDNS, and rtty services will transmit packets through VPN tunnels. This option is disabled by default, as these services normally require the device's real IP address to work properly.

- **Allow Remote Access to the LAN Subnet**: If enabled, remote access to this router and its LAN devices through the VPN will be allowed. It requires the VPN server to advertise a route back to its LAN subnet.

- **IP Masquerading**: If enabled, the source IP addresses of LAN clients will be rewritten to the router's VPN tunnel IP. Disable this only for Site-to-Site setups where the remote peer knows your LAN subnets.

- **MTU**: The MTU value you set for the tunnel will override the MTU settings in the configuration file.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.