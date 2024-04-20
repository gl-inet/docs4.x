# Connect to the Internet via an existing Wi-Fi by Repeater

Using Repeater means connecting the router to another existing wireless network, e.g. when you are using free Wi-Fi in a hotel or cafe.

It works in WISP (Wireless Internet Service Provider) mode by default, which means that the router will create its own subnet and act as a firewall to protect you from the public network.

On the left side of web Admin Panel -> INTERNET, Repeater sector.

## Basic steps

![repeater](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

Click **Connect** in the image above.

![repeater join wlan](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_join_wlan.png){class="glboxshadow"}

Choose a SSID from the drop-down list and enter its password. If the SSID you want to connect to is not in the list, click [Join Other Network](#join-other-network) in the image above.

![repeater join network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_join_network.png){class="glboxshadow"}

If you want to connect to a public hotspot, such as those provided by hotels/airports/malls, please refer to  [For Public Hotspot](#for-public-hotspot).

For other settings, please refer to [Advanced Settings](#join-network-advanced-setting).

Wait a moment, if the password is correct, the connection will be successful.

![repeater connected](/internet_repeater/repeater_connected.png){class="glboxshadow"}

## For Public Hotspot

* **Auto-Enable Authentication Mode For Public Hotspot**

  If this option is enabled, this router will automatically enter authentication mode when it successfully connected to a hotspot but not the Internet. This mode will pause VPNs, which may cause data leaks to the provider of the hotspot (e.g., hotel/mall).

  Even if you do not turn on this option, the device prompts you to enter this mode when it detects the captive portal existing in the hotspot and does not authenticate successfully.

  ![authentication mode](/internet_repeater/authentication_mode.png){class="glboxshadow"}

* **Enable Camouflage**

  If this option is enabled, this router camouflage itself as the same device as the client device you are now using.

  If you enable camouflage mode, the device automatically emulates the MAC address based on the client device you are using.

* **MAC Mode**

  You can choose which MAC to use to connect to this hotspot.

  **Real**: The factory-written MAC address of the device.
  **Clone**: Clone a client's MAC address. Note that many new devices now use a different random MAC address to connect to different WiFi, so the MAC address shown here may not be the actual MAC address of the user's device. The randomized MAC may also be called a Private Wi-Fi Address or a random hardware address on different devices. You can also manually enter the device's MAC you want to clone if it is not in the options.
  **Random**: Generate a random MAC address.

  The mode and cloned/randomized MAC address used when saving the network follows each SSID save, and you can change it manually.

## Join network advanced setting

When joining the network, there are two additional options.

![repeater join network advanced setting](/internet_repeater/repeater_join_network_advanced_setting.png){class="glboxshadow"}

* **Lock BSSID**. If this option is enabled, the router will only connect to the AP corresponding to the BSSID you selected when switching to a network using this SSID.

* **Manually set static IP**.

* **TTL**: TTL (Time To Live) sets the maximum time for packets to survive in the network, and is filled in according to the requirements of the operator. By default, the router forwards the TTL of the incoming client device minus one. If you need to camouflage, you can set a fixed value here. the TTL is valid only for IPv4.

* **HL**: In IPv6, the HL (Hop Limit) field is used to limit the number of transmission hops of data packets in the network, which is equivalent to the TTL in IPv4.

* **MTU**: The default value is 1500.

## Repeater options

Click the cog icon for Repeater options.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

![repeater options](/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Network**. If the option is enabled, the router will automatically connect to other saved networks when it is unable to connect to the current Wi-Fi network.

* **Band Selection**. If you manually select a band, the router will not scan or connect to any Wi-Fi with another band.

* **Force 20MHz Bandwith For 2.4G**. If the option is enabled, The device will prompting the stability of the connection in exchange of reducing the connection speed. It only works when repeating 2.4G Wi-Fi.

## Manage known network

To delete known network, click **Switch Network**.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

Or click **Connect**.

![repeater](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

On the **Known Network** sector, click trash icon to delete a known network, click cog icon to config the network.

![repeater known network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_known_networks.png){class="glboxshadow"}

## Join Other Network

If the SSID is not in the Available Networks list, or if the SSID is hidden, you can click **Join Other Network**.

![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/join_other_network.png){class="glboxshadow gl-90-desktop"}

![join other network](/internet_repeater/repeater_join_other_network.png){class="glboxshadow"}

Input the SSID, for **Security**, It has the following three options.

* None, it doesn't need password.
* WPA/WPA2/WPA3
* WPA/WPA2/WPA3 Enterprise, for Extensible Authentication Protocol (EAP), it requires a username and password for authentication.

    ![join other network, eap](/internet_repeater/join_other_network_eap.png){class="glboxshadow gl-90-desktop"}

## Reconnection

In the following cases, the router's Repeater will try to connect to WiFi every once in a while. You can turn off the reconnection manually, and for ssid/password errors, please delete it in Known Network.

1. The wrong SSID/password was entered during the process of Repeater, after the first failed connection.

2. After connecting to the WiFi of the upstream router, the router moves out of the signal range of the upstream router.

3. After connecting to the WiFi of the upstream router, the upstream router changed the SSID/password, or restricted the connection.

It can be divided into three phases, the waiting phase, the scanning phase, and the connecting phase.

**Note**: There are some problems during the scanning phase and the connection phase.

1. In the waiting phase, everything is OK.

2. In the scanning phase, data packet may loss in the scanned band, possible connection problems for new devices. For GL-AXT1800 and GL-AX1800, the Guest Wi-Fi will be temporarily turned off.

3. In the connecting phase, the Main Wi-Fi on the corresponding band may be disconnected for a few seconds.

## Warning

When Internet access is not available, the corresponding warning is displayed. To determine whether you can access the Internet or not, please go to [Multi-WAN](multi-wan.md) page.

- Warning: *The interface is connected, but the Internet can't be accessed with IPv4 protocol.*

    ![repeater wrning](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_warning.png){class="glboxshadow gl-90-desktop"}

    Solution: Please check if the upstream device of Repeater has internet access.

## DFS

When Repeater to a upstream 5G WiFi, the router WiFi will fellow the upstream WiFi to use or not use the DFS channel.

* If the upstream WiFi uses a DFS channel and is scannable, the router's 5G WiFi will use the same channel.

* The router's 5G WiFi will switch to the non-DFS channel if the upstream WiFi is not scannable or if the connection fails.

### Supported models

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X3000 (Spitz AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-AXT1800 (Slate AX)          | √         |
| GL-A1300 (Slate Plus)          | -         |
| GL-MT2500/GL-MT2500A (Brume 2) | -         |
| GL-SFT1200 (Opal)              | -         |
| GL-S1300 (Convexa-S)           | -         |
| GL-MT1300 (Beryl)              | -         |
| GL-AX1800 (Flint)              | -         |
| GL-MT6000 (Flint 2)            | √         |
| GL-AR750S (Slate)              | -         |
| GL-AR750 (Creta)               | -         |
| GL-AR300M Series（Shadow）     | -         |
| GL-MT300N-V2（Mango）          | -         |
| GL-XE300 (Puli)                | -         |
| GL-XE3000 (Puli AX)            | √         |
| GL-X750 (Spitz)                | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-AP1300 (Cirrus)             | -         |
| GL-X300B (Collie)              | -         |
| GL-MV1000/GL-MV1000W (Brume)   | -         |

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)
- [How can I know the LAN and WiFi Mac Addresses](../faq/how_can_I_know_the_lan_wifi_mac.md)
---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
