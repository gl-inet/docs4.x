# VPN Dashboard (Firmware v4.9)

**Note**: This guide is based on firmware v4.9. For earlier versions, please refer to [here](vpn_dashboard.md).

---

On the left side of the web Admin Panel, go to **VPN** -> **VPN Dashboard**. 

The VPN dashboard displays VPN connection details, such as routing rules, connected server, traffic statistics, client virtual IP, and connection log, and allows users to configure advanced settings such as the VPN Kill Switch, IP Masquerading, and MTU.

Compared to firmware v4.8, v4.9 includes the following improvements to the VPN Dashboard:

1. **Allow users to select multiple profiles within a tunnel group and set their priority**. The tunnel will attempt to connect using each profile in priority order until a connection is successfully established.

2. **Each tunnel group operates independently and does not perform failover between groups**. If all profiles in a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and the All Other Traffic tunnel.

## Getting Started

When entering this page for the first time, if no tunnels have been created, the page will appear as shown below. Click **Add VPN Tunnel** to get started.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**Select a VPN provider**. The VPN providers listed are integrated into the GL.iNet router web Admin Panel. With an active subscription, users simply enter their credentials to log in instantly and obtain configuration files for VPN connections.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

If you have subscribed to other VPN providers, or if you want to upload your personal VPN configurations, go to **VPN Client Profile** to configure manually.

Here's an example with **Hide.me**. Log in with Hide.me credentials.

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**Select a VPN server**. This is the server you will connect to via this VPN tunnel, and your public IP address will appear to be from the selected server's location. Click **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

It will connect automatically. Click **Done**.

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

You will be directed to the VPN Dashboard, where the VPN Tunnel 1 has been enabled and connected. 

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**In this example, all clients connected to this router will access the Internet through this VPN tunnel.**

If you want to configure VPN policy, please refer to [VPN Policy](#vpn-policy).

The **All Other Traffic** is a pre-enabled tunnel displaying at the bottom of the VPN Dashboard. Click [here](#all-other-traffic) for details.

## Tunnel Details

On the VPN Dashboard, each individual VPN tunnel is displayed as shown below, showing detailed VPN tunnel information such as routing rules, connected server, traffic statistics, server address, listen port, client virtual IP, and connection log. You can enable or disable the VPN tunnel and configure tunnel settings at the top of the tunnel group.

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## VPN Policy

A VPN policy defines how network traffic is routed through VPN tunnels, determining which traffic goes to target destinations via VPN and which accesses the Internet directly through the local WAN.

It allows all clients or specific devices to access designated websites or the entire Internet over a VPN connection, enabling flexible and secure network management.

### Quick Setup

On the VPN Dashboard, click **Add New Tunnel** or click the middle area of an existing VPN tunnel. 

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

Then follow the setup wizard to configure your VPN policy, including selecting VPN profile, traffic source, and traffic destination.

1. **Select the VPN profile.** 

    If you have logged in with any integrated VPN service credentials or uploaded a configuration file, the available profiles will be listed here. Otherwise, go to **VPN Client Profile** to log in with your credentials or upload a configuration file manually.

    Take [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} as an example. Log in with your service credentials, and you will see a list of VPN profiles. Select one or multiple profiles, and adjust their priority on the right as needed.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) tunnel.

2. **Select the client source.** 

    There are four options:

    - **All Clients**: If selected, traffic from all devices will match this rule.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: If selected, traffic from specified connection types (e.g., LAN subnet, Drop-in Gateway, Guest Network) will match this rule.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: If selected, traffic from specified devices (identified by MAC address) will match this rule.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: If selected, traffic from specified devices (identified by MAC address) will not match this rule.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **Select the target destination**. 

    There are three options:

    - **All Targets**: If selected, traffic matching this rule will be routed to all targets.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: If selected, traffic matching this rule will be routed to specified domains or IP addresses. You need to enter them manually.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: If selected, traffic matching this rule will not be routed to specified domains or IP addresses. You need to enter them manually.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Usage Scenarios

Here are two scenarios with step-by-step instructions for your reference.

**Scenario 1** 

**Objectives**:

1. Only specific devices connected to this router access the Internet through the VPN. All other devices access the Internet through the local WAN.

2. The selected devices must use the VPN connection only. If the VPN disconnects unexpectedly, Internet access for these devices will be blocked to prevent DNS leaks and IP tracking.

**Follow the steps below to configure the VPN policy.**

1. Select the VPN profile. 

    If you have logged in with any integrated VPN service credentials or uploaded a configuration file, the available profiles will be listed here. Otherwise, go to **VPN Client Profile** to log in with your credentials or upload a configuration file manually.

    Take [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} as an example. Log in with your service credentials, and you will see a list of VPN profiles.

    ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

    Select one or multiple profiles, and adjust their priority on the right as needed.

    ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) tunnel.

2. Select **Specified Devices** as the client source, then select the devices that will use the VPN and click **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. Select **All Targets** as the target destination, then click **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. You will be redirected to the VPN Dashboard, where a VPN tunnel has been added. 

    ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. Make sure the **Kill Switch** for this tunnel is enabled. If the VPN disconnects unexpectedly, Internet access for traffic matching this tunnel will be blocked to prevent DNS leaks and IP tracking.

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}
    
6. Make sure the **All Other Traffic** is enabled and the mode is set to **Allow Non-VPN Traffic**. This ensures that traffic not matching the above VPN tunnels can still access the Internet through the local WAN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. Toggle the switch to activate this tunnel.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. Once connected, the page will display the VPN connection details, including VPN policy, traffic statistics, server address, listen port, and virtual IP address.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

    Now, only two specified devices access the Internet through VPN. If the VPN disconnects unexpectedly, Internet access for these devices will be blocked to prevent DNS leaks and IP tracking. All other devices will access the Internet through the local WAN instead.

**Scenario 2**

**Objectives:** 

1. All devices use **VPN Tunnel 1** when accessing domains of specific social media and streaming services, and use **VPN Tunnel 2** for all other Internet access.

2. If the VPN tunnels disconnect unexpectedly, Internet access for all devices will be blocked to prevent DNS leaks and IP tracking.

**Follow the steps below to configure the VPN policy.**

1. Select the VPN profile for Tunnel 1. 

    If you have logged in with any integrated VPN service credentials or uploaded a configuration file, the available profiles will be listed here. Otherwise, go to **VPN Client Profile** to log in with your credentials or upload a configuration file manually.

    Take [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} as an example. Log in with your service credentials, and you will see a list of VPN profiles. 

    ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}
    
    Select one or multiple profiles, and adjust their priority on the right as needed.

    ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) tunnel.

2. Select **All Clients** as the client source for Tunnel 1, then click **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Select **Specified Domain / IP List** as the target destination for Tunnel 1. Enter domains of some common social media and streaming services, as shown below, then click **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. You will be redirected to the VPN Dashboard, where the Tunnel 1 has been added. 

    ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Make sure the **Kill Switch** for Tunnel 1 is enabled. If the VPN disconnects unexpectedly, Internet access for traffic matching this tunnel will be blocked to prevent DNS leaks and IP tracking.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}
    
6. Click **Add New Tunnel** to add Tunnel 2.

    ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Select the VPN profile for Tunnel 2. 

    If you have logged in with any integrated VPN service credentials or uploaded a configuration file, the available profiles will be listed here. Otherwise, go to **VPN Client Profile** to log in with your credentials or upload a configuration file manually.

    Take [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} as an example. Log in with your service credentials, and you will see a list of VPN profiles. 
    
    ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}
    
    Select one or multiple profiles, and adjust their priority on the right as needed.

    ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

    **Note**: When multiple profiles are selected, the tunnel will attempt to connect using each profile in priority order until a connection is successfully established. If all profiles within a single tunnel fail to connect, the system will determine whether to switch to the local WAN based on the status of the Tunnel Kill Switch and [All Other Traffic](#all-other-traffic) tunnel.

8. Select **All Clients** as the client source for Tunnel 2, then click **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Select **All Targets** as the target destination for Tunnel 2, then click **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. You will be redirected to the VPN Dashboard, where the Tunnel 2 has been added. 

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Make sure the **Kill Switch** for Tunnel 2 is enabled. If the VPN disconnects unexpectedly, Internet access for traffic matching this tunnel will be blocked to prevent DNS leaks and IP tracking.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. Disable **All Other Traffic**. Ensure the mode is set to **Enhanced Kill Switch**. This ensures that all traffic must access Internet via the VPN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. Toggle the switch to activate Tunnel 1 and Tunnel 2.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. Once connected, the page will display the VPN connection details, including VPN policy, traffic statistics, server address, listen port, and virtual IP address.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    Now, all devices will use **VPN Tunnel 1** when accessing specified domains, and use **VPN Tunnel 2** for all other Internet access. If the VPN tunnels disconnect unexpectedly, Internet access for all devices will be blocked to prevent DNS leaks and IP tracking.

## All Other Traffic

This option controls whether traffic that does not match any of the above VPN tunnel groups can access the Internet. It is enabled by default to ensure normal Internet access for traffic not routed via VPN.

When enabled, unmatched traffic can still access the Internet.

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

When disabled, only traffic routed via VPN is allowed to access the Internet. All non-VPN traffic and traffic that fails over from VPN connections will be blocked. This option does not override the individual Kill Switch for each VPN tunnel.

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## Tunnel Priority

To adjust tunnel priority, click the gear icon in a tunnel group and select **Sort**.

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

5. The **All Other Traffic** tunnel is enabled by default to ensure that traffic not matching the VPN tunnels can still access the Internet.

    - If enabled, it routes unmatched or failover traffic through the local WAN.
    - If disabled, it strengthens the Kill Switch and blocks regular Internet access to prevent IP leaks.

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