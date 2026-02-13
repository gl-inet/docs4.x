# Connect to the Internet via an existing Wi-Fi by Repeater

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Using Repeater means connecting the router to another existing wireless network, e.g. when you are using free Wi-Fi in a hotel or cafe.

It works in WISP (Wireless Internet Service Provider) mode by default, which means that the router will create its own subnet and act as a firewall to protect you from the public network.

## Basic Steps

Log in to the router's web admin panel, navigate to **INTERNET** -> **Repeater** section, and click **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Choose the Wi-Fi network you want to connect to from the available network list.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**Note**: The page displays the Wi-Fi channels your router supports. Please ensure that the Wi-Fi network you're connecting to uses one of these channels, otherwise it may not be displayed in the available network list.

Enter the correct Wi-Fi password and click **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

If the Wi-Fi SSID you want to connect to is not in the Available Network list, click **Join Other Network** in the upper-right corner, manually input the Wi-Fi SSID and other information required. Refer to [here](#join-other-network) for detailed steps.

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

For connecting to a public hotspot, such as those provided by hotels/airports/malls, please refer to  [For Public Hotspot](#for-public-hotspot).

For other settings, please refer to [Advanced Settings](#advanced-settings).

After a while, if the password input is correct, the connection will be successful.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## For Public Hotspot

When connecting the router to a public hotspot with a captive portal, enabling the following features can help improve the connection success rate.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    This feature is available since v4.6

    If this option is enabled, this router will automatically enter Login Mode for Public Hotspots when it is successfully connected to a hotspot but not the Internet. **In this mode, some services will be suspended while the DNS mode will be switched to automatic**, which may leak your network activity to the hotspot provider (e.g. hotel or shopping mall).

    Even if this option is not enabled, the router will prompt you to enter this mode when it detects a captive portal in the hotspot and fails to log in successfully.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    If enabled, the router will masquerade as the client device you use to access the admin panel by emulating that device’s MAC address.

- **MAC Mode**

    You can choose which MAC the router uses to connect to the public hotspot.

    - **Factory**: Uses the device's original factory-assigned MAC address.

    - **Clone**: Clones a client device’s MAC address for connection. If the desired MAC isn’t listed, manually enter the address you want to clone. 
    
        Note: Many modern devices use randomized MAC addresses (often called Private Wi-Fi Address or random hardware address) when connecting to Wi-Fi networks. Because of this, the MAC address displayed here may not match the device’s actual physical MAC.
  
    - **Random**: Automatically generates a random MAC address for connection.

    When saving the network configuration, the MAC Mode (including any cloned/randomized MAC address) is tied to the specific SSID you save. You can manually change these settings for each SSID at any time.

- **Auto Update MAC**: If this option is enabled, the MAC can update automatically.

## Advanced Settings

When joining the network, there are some additional options.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: Enable this to remember the current repeated Wi-Fi network. This is available in firmware v4.7 and later.

* **Lock BSSID**: If this option is enabled, the router will only connect to the AP corresponding to the BSSID you selected when switching to a network using this SSID.

* **Manually set static IP**: This is available in firmware v4.7 and later.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL (Time To Live) sets the maximum time for packets to survive in the network, and is filled in according to the requirements of the operator. By default, the router forwards the TTL of the incoming client device minus one. If you need to camouflage, you can set a fixed value here. the TTL is valid only for IPv4.

* **HL**: In IPv6, the HL (Hop Limit) field is used to limit the number of transmission hops of data packets in the network, which is equivalent to the TTL in IPv4.

* **MTU**: The default value is 1500.

## Repeater Options

To view repeater options, click the gear icon in the upper-right corner of the connected Repeater section.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**For firmware v4.8**, the Repeater Options page is displayed as follows.

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**: 

    - No Switching mode: When No Switching mode is enabled, other saved networks will not be automatically connected when the current Wi-Fi is disconnected.
  
    - Auto Switching mode: When Auto Switching mode is enabled, the router will try to connect to other saved networks when the current Wi-Fi is disconnected.
  
    - Auto Switching Without Network: When Auto-switching Without Network mode is enabled, the router will not automatically scan for networks when it is successfully networked in the non-repeater mode, and will only try to automatically switch to other saved networks when the router is without a network, which can avoid communication packet loss. 

- **Band Selection**: you can select from three options: Auto, 5 GHz and 2.4 GHz.

    If you manually select a band, the router will not scan or connect to any Wi-Fi that is using another band.

**For firmware v4.7 and earlier**, the Repeater Options page is displayed as below.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Networks**. If the option is enabled, the router will automatically connect to other saved networks when it is unable to connect to the current Wi-Fi network.

* **Band Selection**. If you manually select a band, the router will not scan or connect to any Wi-Fi with another band.

## Manage Known Network

To delete known network, click **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Or click **Connect** in the Repeater section if there's no any network connected.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

On the **Known Networks** section, click the trash icon to delete a known network, or the gear icon to configure the network.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Join Other Network

If the SSID is not in the Available Networks list, or if the SSID is hidden, you can click **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Input the SSID, select the Security and enter the password (if required).

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

For **Security** settings, there are two or three options, depending on the model.

* None, which means no password is required.
* WPA/WPA2/WPA3, which is common and supported by nearly all Wi-Fi networks.
* WPA/WPA2/WPA3 Enterprise, which requires Extensible Authentication Protocol (EAP) for authentication. A valid username and password are needed to connect (typically used in business or campus networks).

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    For detailed guidance on repeating EAP networks, please click [here](../tutorials/eap.md){target="_blank"}.

## Reconnection

In the following cases, the router will automatically attempts to reconnect to Wi-Fi every once in a while. You can manually disable this if needed. For SSID/password errors, remove the network from Known Networks to resolve.

1. Incorrect SSID/password entered during Repeater setup.

2. Moved out of range of the upstream router after initial connection.

3. Upstream router changes SSID/password or restricts access post-connection.

The reconnection process has three distinct phases: waiting phase, scanning phase and connecting phase.

1. Waiting Phase: No issues - router waits for reconnection conditions.

2. Scanning Phase: Packet loss may occur on the scanned frequency band. New devices might face connection problems. For models GL-AXT1800/GL-AX1800, Guest Wi-Fi will be temporarily disabled.

3. Connecting Phase: Main Wi-Fi on the target band may drop for a few seconds during re-establishment.

**Note**: Problems typically arise in the Scanning and Connecting Phases.

## Warning

When Internet access is not available, the corresponding warning is displayed as below. 

**"The interface is connected, but the Internet can't be accessed."**

![repeater wrning](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Solutions: 

1. Check if the upstream device of Repeater has internet access.

2. Go to [Multi-WAN](multi-wan.md) page to determine whether you can access the Internet or not.

## DFS

When connecting to an upstream 5G Wi-Fi, the router's Wi-Fi will follow the upstream Wi-Fi to use or not use the DFS channel.

* If the upstream Wi-Fi uses a DFS channel and is scannable, the router's 5G Wi-Fi will use the same channel.

* The router's 5G Wi-Fi will switch to the non-DFS channel if the upstream Wi-Fi is not scannable or if the connection fails.

??? "Supported Models"

    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Unsupported Models"

    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)
- [How can I know the LAN and Wi-Fi Mac Addresses](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
