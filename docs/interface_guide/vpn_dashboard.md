# VPN Dashboard

GL.iNet routers include a dedicated VPN Dashboard that provides a centralized interface for managing your VPN connections. You can use it to set up and monitor VPN clients and server configurations. The VPN Dashboard allows you to route your internet traffic through encrypted tunnels, helping protect your online privacy, bypass regional restrictions, and access remote networks. 

This guide walks you through the key features of the VPN Dashboard and shows you how to configure, monitor, and optimize your VPN connections.

<!-- A brief introduction allows the user to understand the contents and purpose of this guide. -->

!!! Note

    This guide is based on firmware v4.8. If you are using an earlier firmware version, please visit [here](vpn_dashboard_v4.7.md).

<!-- Removed "This page visually displays VPN status and settings through graphics.", "[vpn dashboard unmarked.png]" and "This guide will introduce to you one by one." Reason: redundant -->

### Contents

The VPN dashboard consists of the following parts, marked in the figure below.

1. [Navigating to the VPN Dashboard](#navigating-to-the-vpn-dashboard)
1. [VPN Setup Wizard](#vpn-setup-wizard)
2. [Primary Tunnel](#primary-tunnel)
    3. [Traffic Originating From](#traffic-originating-from)
    4. [Execute](#execute)
    5. [Travelling To](#travelling-to)
    6. [Tunnel settings](#tunnel-settings)
7. [Add Tunnel](#add-tunnel)
8. [Non-VPN Tunnel](#non-vpn-tunnel)

</br>
![vpn dashboard marked](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/vpn_dashboard_2.png){class="glboxshadow"}

## Navigating to the VPN Dashboard

Open the web Admin Panel, on the left side bar, select **VPN** -> **VPN Dashboard**. <!-- Use bold to mark items/terms on the UI-->

![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

<!-- This image is a placeholder. For easier navigation, the "VPN" dropdown should be expanded, "VPN Dashboard" is highlighted in a red box. -->

## VPN Setup Wizard

There is no default configuration for VPN tunnels. Click on the VPN Setup Wizard icon at the upper-left corner to quickly set one up. 

<!-- Changed wording to be short, direct and more command-like. -->
<!-- Removed "WireGuard VPN" to avoid confusion between VPN protocols and VPN clients. -->

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/vpn_wizard_1.png){class="glboxshadow"} <!-- To maintain consistency, consider highlighting the icon with a red box. -->

The VPN Setup Wizard allows you to set up the following VPN clients: AzireVPN, Mullvad, PIA, Surfshark, NordVPN, Hide.me and IPVanish. Configuring the VPN may take a few minutes.

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/vpn_wizard_2.png){class="glboxshadow"}

These VPN clients use WireGuard, a VPN protocol. To set up the above clients or other WireGuard clients, go to [WireGuard Client](wireguard_client.md){target="_blank"}. <!-- I intend to direct users to the "WireGuard Client" section, since it has follow-up instructions for setting up clients in the Wizard. I assume a separate section is created to avoid bloat in this guide. --> To set up OpenVPN clients, go to [OpenVPN Client](openvpn_client.md){target="_blank"}. <!-- By only listing the two, I'm assuming other open-source protocols like SoftEther are not supported.-->

## Primary Tunnel

The Primary Tunnel is a preset VPN tunnel where you can customize the tunnel rule <!-- Changed to "tunnel rule" for consistency. Also because it matches with UI label "VPN Tunnel" and "Add Tunnel", which are where rules are created. --> by setting three factors: 

- **Traffic Originating From** (i.e. traffic of which device should use this tunnel rule)
- **Execute** (i.e. to use VPN or not use VPN)
- **Travelling To** (i.e. to which target does the traffic travels through this tunnel)

![primary tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/primary_tunnel.png){class="glboxshadow"}

### Traffic Originating From

1. Click the greyed-out box under **Traffic Originating From**. <!-- Added ordered lists for instructions so that each image has a corresponding caption. -->

    ![traffic from 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_1.png){class="glboxshadow"}
   
2. Select the device that you want to apply this rule to.
   
    ![traffic from 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_2.png){class="glboxshadow"}

- **All Clients**: Traffic from all devices will apply this rule.

    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_3.png){class="glboxshadow gl-80-desktop"}

- **Specified Connection Methods**: Traffic from specified connection methods (LAN subnet/Drop-in Gateway/Guest Network) will apply this rule.

    ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_4.png){class="glboxshadow gl-80-desktop"}

- **Specified Devices**: Traffic from specified devices will apply this rule.

    ![specified device](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_5.png){class="glboxshadow gl-80-desktop"}

- **Exclude Specified Devices**: Traffic from specified devices will **NOT** apply this rule.

    ![exclude specified device](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_6.png){class="glboxshadow gl-80-desktop"}

### Execute

1. Click the greyed-out box under **Execute**. 

    ![execute 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/execute_1.png){class="glboxshadow"}

2. Select the action you want to perform on this rule.
   
    ![execute 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/execute_2.png){class="glboxshadow"}

- **Execute**: Use VPN or Not Use VPN.
- **Auto-select Configuration**: When enabled, the tunnel automatically selects available VPN configurations <!-- Changed to "VPN configurations" to be consistent with this setting name. Understand that "profiles" refers to saved VPN configurations. However, the term "profile" has not been introduced in this guide, thus it's substitutued to avoid confusion. --> to connect.
- **Kill Switch**: When enabled, this feature blocks any matching traffic that isn’t sent through the VPN tunnel. This feature has higher priority over other tunnel rules. <!-- Clarified language. -->

### Travelling To

1. Click the greyed-out box under **Travelling To**. 

    ![Travel to 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_1.png){class="glboxshadow"}

2. Select the target that the traffic travels to through this tunnel.

    ![Travel to 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_2.png){class="glboxshadow"}

- **All targets**: Traffic through this tunnel will travel to all destinations.

    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_3.png){class="glboxshadow gl-80-desktop"}

- **Specified Domain / IP List**: Traffic through this tunnel will travel to a specified Domain / IP. 

    Manually input the specified Domain / IP.

    ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_4.png){class="glboxshadow gl-80-desktop"}

    Or switch the **Input Mode** from **Manual** to **Subscription URL** and input URL Link. 

    ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_5.png){class="glboxshadow gl-80-desktop"}

    !!! Note
        - If you select **Subscribe URL**, the domain name or IP in the URL is automatically updated every day. 

        - Make sure to enter the correct URL. The URL detection will identify the correctness of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

- **Exclude specified Domain / IP List**: Traffic through this tunnel will **NOT** travel to specified Domain / IP.

    Manually input the specified Domain / IP.

    ![exclude specified domain/IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_6.png){class="glboxshadow gl-80-desktop"}

    Or switch the **Input Mode** from **Manual** to **Subscription URL** and input URL Link. 

    !!! Note
        - If you select **Subscribe URL**, the domain name or IP in the URL is automatically updated every day. 

        - Make sure to enter the correct URL. The URL detection will identify the correctness of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

### Tunnel Settings

Click the cog icon next to **Primary Tunnel**, you can rename the tunnel, change tunnel settings or delete the tunnel. 

![tunnel settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/tunnel_settings.png){class="glboxshadow"}

**Options**

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/tunnel_options.png){class="glboxshadow gl-80-desktop"}

- **Services from GL.iNet Use VPN**: When enabled, GoodCloud, DDNS, and rtty services will use VPN tunnels. Note that these services normally need to use the real IP address of the device, enabling this option may affect operation. <!-- Not sure if the original phrasing is intentionally less direct -->
- **Remote Access LAN**: When enabled, devices connected to the VPN tunnel can reach other devices (e.g. computers, printers) on your local network (LAN).
- **IP Masquerading**: When enabled, your LAN devices' outgoing traffic will be sent through the VPN using router's IP address instead of their own.
- **MTU (Maximum Transmission Unit)**: Set your own MTU for this tunnel, it determines the largest size of the data packet travelling through your network. Leave blank to use the system default value. <!-- Consider reccomending values: e.g. "Reccomended 1300-1500 for WireGuard, 1300-1500 for OpenVPN". Also consider adding link to learn more about defining MTU. -->

## Add Tunnel

Apart from the preset **Primary Tunnel**, you can add tunnels to achieve multiple VPN instances.

![add tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/add_tunnel.png){class="glboxshadow"}

After adding a tunnel, the VPN Dashboard page will display the **Priority** option in the upper right corner, which is used to set the priority of tunnels.

![priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/priority_1.png){class="glboxshadow"}

By default, the preset **Primary Tunnel** will have the highest priority, followed by other manual-added tunnel(s).

The built-in **Non-VPN Tunnel** will be locked as a basic tunnel with lowest priority, to ensure local network connectivity.

![priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/priority_2.png){class="glboxshadow"}

Click and hold the three-line icon on the right to drag the tunnels for sorting.

## Non-VPN Tunnel

The **Non-VPN Tunnel** is a basic network tunnel with lowest priority. It is unchangeable and cannot be deleted. 

![non-vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/non_vpn_tunnel.png){class="glboxshadow"}

It is a local network tunnel that is mutually exclusive with the VPN tunnel, traffic will go through one or the other, not both.

When there are multiple tunnels, the router transmits traffic in the following order:

1. When the tunnel with the highest priority is enabled, the traffic that conforms to the tunnel rule will be transmitted according to the set execute action and targets. 

2. For the traffic that does not conform to the tunnel rule of the highest priority, it will automatically be matched to the tunnel rule of the second highest priority. 

3. If it still does not match, it will continue to be matched against the next lower priority rule, and so on, until it is matched to the Non-VPN Tunnel with the lowest priority.

You can disable the **Non-VPN Tunnel** if needed. 

**Note**: Non-VPN tunnelling ensures that traffic not passing through the above tunnels can still connect to the Internet. If disabled, it will drop any remaining traffic.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
