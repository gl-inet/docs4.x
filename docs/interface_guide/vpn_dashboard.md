# VPN Dashboard

!!! Note

    This guide is based on firmware v4.8. If you are using an earlier firmware version, please visit [here](vpn_dashboard_v4.7.md).

Access to web Admin Panel, on the left side -> VPN -> VPN Dashboard. 

This page visually displays VPN status and settings through graphics.

![vpn dashboard unmarked](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

### Contents

The VPN dashboard mainly consists of the following parts, marked in the figure below.

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

This guide will introduce to you one by one.

## VPN Setup Wizard

There is no configuration available for VPN Tunnel by default. Please click on VPN Setup Wizard at the upper left, which can help you set up the WireGuard VPN quickly.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/vpn_wizard_1.png){class="glboxshadow"}

The VPN Setup Wizard is only for AzireVPN, Mullvad, PIA, Surfshark, NordVPN, Hide.me and IPVanish. Configuring the VPN may take a few minutes.

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/vpn_wizard_2.png){class="glboxshadow"}

For other vpn providers, skip the wizard and go to [OpenVPN Client](openvpn_client.md){target="_blank"} / [Wireguard Client](wireguard_client.md){target="_blank"} to set up VPN manually. 

## Primary Tunnel

The Primary Tunnel is a preset tunnel where you can customize the traffic rule by setting three factors: 

- Traffic Originating From (i.e. traffic of which device should use this rule)
- Execute (i.e. use VPN or not use VPN)
- Travelling To (i.e. to which target does the traffic travels through this tunnel)

![primary tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/primary_tunnel.png){class="glboxshadow"}

### Traffic Originating From

Click the greyed-out box under Traffic Originating From, select the device that you want to apply this rule to.

![traffic from 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/traffic_from_1.png){class="glboxshadow"}

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

Click the greyed-out box under Execute, select the action you want to perform on this rule.

![execute 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/execute_1.png){class="glboxshadow"}

![execute 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/execute_2.png){class="glboxshadow"}

- **Execute**: Use VPN or Not Use VPN.
- **Auto-select Configuration**: When this option is enabled, the tunnel automatically selects available profiles to connect.
- **Kill Switch**: Enable this feature to block traffic that matches this rule but is not tunneled, with higher priority than other VPN tunnel rules.

### Travelling To

Click the greyed-out box under Travelling To, select the target that the traffic travels to through this tunnel.

![Travel to 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_1.png){class="glboxshadow"}

![Travel to 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_2.png){class="glboxshadow"}

- **All targets**: Traffic through this tunnel will travel to all destinations.

    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_3.png){class="glboxshadow gl-80-desktop"}

- **Specified Domain / IP List**: Traffic through this tunnel will travel to specified Domain / IP. 

    Manually input the specified Domain / IP.

    ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_4.png){class="glboxshadow gl-80-desktop"}

    Or switch the Input Mode from Manual to Subscription URL and input URL Link. 

    ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_5.png){class="glboxshadow gl-80-desktop"}

    !!! Note
        - If you select Subscribe URL, the domain name or IP in the URL is automatically updated every day. 

        - Make sure to enter the correct URL. The URL detection will identify the correctness of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

- **Exclude specified Domain / IP List**: Traffic through this tunnel will **NOT** travel to specified Domain / IP.

    Manually input the specified Domain / IP.

    ![exclude specified domain/IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/travel_to_6.png){class="glboxshadow gl-80-desktop"}

    Or switch the Input Mode from Manual to Subscription URL and input URL Link. 

    !!! Note
        - If you select Subscribe URL, the domain name or IP in the URL is automatically updated every day. 

        - Make sure to enter the correct URL. The URL detection will identify the correctness of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

### Tunnel Settings

Click the cog icon next to the Primary Tunnel, you can rename the tunnel, change tunnel settings or delete the tunnel. 

![tunnel settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/tunnel_settings.png){class="glboxshadow"}

**Options**

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/tunnel_options.png){class="glboxshadow gl-80-desktop"}

- **Services from GL.iNet Use VPN**: If this option is enabled, GoodCloud, DDNS, and rtty services will use VPN tunnels to send packets. Note that these services normally need to use the real IP address of the device, otherwise operations may fail.
- **Remote Access LAN**: If this option is enabled, resources inside the LAN subnet can be accessed through the VPN tunnel.
- **IP Masquerading**: If this option is enabled, when client devices on LAN send their IP packets, the router replaces the source IP address with its own address and then forwards it to the VPN tunnel.
- **MTU**: The MTU you set for the instance here will overwrite the MTU item in the configuration file.

## Add Tunnel

Apart from the preset Primary Tunnel, you can add tunnels to achieve multiple VPN instances.

![add tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/add_tunnel.png){class="glboxshadow"}

After adding a tunnel, the VPN Dashboard page will display the **Priority** option in the upper right corner, which is used to set the priority of tunnels.

![priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/priority_1.png){class="glboxshadow"}

By default, the preset Primary Tunnel will have the highest priority, followed by other manual-added tunnel(s).

The built-in Non VPN Tunnel will be locked as a basic tunnel with lowest priority, to ensure local network connectivity.

![priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/priority_2.png){class="glboxshadow"}

Press and hold the three-line icon on the right to drag the tunnels for sorting.

## Non-VPN Tunnel

The Non-VPN Tunnel is a basic network tunnel with lowest priority. It is unchangeable and cannot be deleted. 

![non-vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/non_vpn_tunnel.png){class="glboxshadow"}

It is actually a local network tunnel that is mutually exclusive with the VPN tunnel.

When there are multiple tunnels, the router transmits traffic in the following order:

- When the tunnel with the highest priority is enabled, the traffic that conforms to the tunnel rule will be transmitted according to the set execute action and targets. 

- For the traffic that does not conform to the tunnel rule of the highest priority, it will automatically be matched to the tunnel rule of the second highest priority. 

- If it still does not match, it will continue to be matched against the next lower priority rule, and so on, until it is matched to the Non-VPN Tunnel with the lowest priority.

You can disable the Non-VPN Tunnel if needed. 

**Note**: Non-VPN tunnelling ensures that traffic not passing through the above tunnels can still connect to the Internet. If disabled, it will drop any remaining traffic.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.