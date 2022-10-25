# Connect to the Internet via an existing Wi-Fi by Repeater

Using Repeater means connecting the router to another existing wireless network, e.g. when you are using free Wi-Fi in a hotel or cafe.

It works in WISP (Wireless Internet Service Provider) mode by default, which means that the router will create its own subnet and act as a firewall to protect you from the public network.

On the left side of web Admin Panel -> INTERNET, Repeater sector.

## Basic steps

![repeater](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

Click **Connect** in the image above.

![repeater join wlan](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_wlan.png){class="glboxshadow"}

Choose a SSID from the drop-down list and enter its password. If the SSID you want to connect to is not in the list, click [Join Other Network](#join-other-network) in the image above.

![repeater join network](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_network.png){class="glboxshadow"}

For [Advanced Settings](#join-network-advanced-setting).

Wait a moment, if the password is correct, the connection will be successful.

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Join network advanced setting

When joining the network, there are two additional options.

![repeater join network advanced setting](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_network_advanced_setting.png){class="glboxshadow"}

* **Lock BSSID**. If this option is enabled, the router will only connect to the AP corresponding to the BSSID you selected when switching to a network using this SSID.

* **Manually set static IP**.

## Repeater options

Click the cog icon for Repeater options.

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

![repeater options](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Network**. If the option is enabled, the router will automatically connect to other saved networks when it is unable to connect to the current Wi-Fi network.

* **Band Selection**. If you manually select a band, the router will not scan or connect to any Wi-Fi with another band.

* **Allow Repeat DFS Channels**. If the option is enabled, 5GHz Wi-Fi will be temporarily unavailable when a radar is using the channel which is currently router using; Otherwise, the router will not connect to any Wi-Fi using DFS channels.

* **Force 20MHz Bandwith For 2.4G**. If the option is enabled, The device will prompting the stability of the connection in exchange of reducing the connection speed. It only works when repeating 2.4G Wi-Fi.

## Manage known network

To delete known network, click **Switch Network**.

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

Or click **Connect**.

![repeater](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

On the **Known Network** sector, click trash icon to delete a known network, click cog icon to config the network.

![repeater known network](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_known_networks.png){class="glboxshadow"}

## Join other network

![join other network](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_other_network.png){class="glboxshadow"}

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

When Internet access is not available, the corresponding warning is displayed. To determine whether you can access the Internet or not, please go to [Multi-WAN](../multi-wan) page.

- Warning: *The interface is connected, but the Internet can't be accessed with IPv4 protocol.*

    ![repeater wrning](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_warning.png){class="glboxshadow" width="60%"}

    Solution: Please check if the upstream device of Repeater has internet access.

---

Related Articles

- [Internet page](../internet)
- [How to set the priority of each Internet access method?](../multi-wan/)
- [How to set the load balance when multiple Internet access methods are used at the same time?](../multi-wan/)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
