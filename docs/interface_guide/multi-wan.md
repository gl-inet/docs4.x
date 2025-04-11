# Multi-WAN

On the left side of web Admin Panel -> NETWORK -> Multi-WAN

GL.iNet router can be connected to the Internet in multiple ways, such as [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md), [Cellular](internet_cellular.md). You can configure the router with multiple Internet access methods, so that when one type of Internet access is not available, it can automatically switch to another type of Internet access in a short time. Or use multiple Internet access methods at the same time, assigning the network connection to different connection methods in a certain ratio.

Some models support [Dual-Ethernet WAN](dual-ethernet_wan.md), which will add an additional Ethernet interface on the user interface.

## Interface Status Tracking Method

GL.iNet routers have up to 5 interfaces, but this varies depending on the model. They are **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** and **Cellular**. Here is the GL-MT6000 as an example.

The router will use the ping or httping command to track the status of the connection to the destination IP to determine if the interface is available. If the interface is available, it will show as a green dot at the begining, otherwise it is gray.

![multi-wan interface status tracking method](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track.png){class="glboxshadow"}

**The setting of Interface Status Tracking Method**

![multi-wan interface status tracking method setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_setting.png){class="glboxshadow gl-90-desktop"}

- **Enable Interface Status Track**: You can disable the interface status tracking, the router will use the physical status of the interface (such as whether the network cable is plugged in or not).

- **Low Data Mode**: Enable the switch to track only when there is an interface network error, and recommend users to use Low Data Mode when you are on a limited data plan.However, one drawback is that reconnecting after a network disconnection may be slightly slower compared to the regular mode, and only the cellular interface will be turned on by default.

**Sensitivity Options**

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.png){class="glboxshadow gl-90-desktop"}

This sensitivity determines the time interval for Internet status detection. 

- If the network is stable and in scenarios such as watching videos or live streams, playing games, users are recommended to use high sensitivity for quick switching in case of network disconnection. 
- If the network is unstable and downloading cached files, users are recommended to use low sensitivity to prevent constant network switching and discovering unsuccessful connections.

**Tips**: Switching to high sensitivity may lead to network disconnection, please adjust it with caution.

## Multi-WAN methods

There are two methods, **Failover** and **Load Balance**. **Failover** and **Load Balance** are mutually exclusive functions, and you can only use one of them.

### Failover

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/multi-wan_mode_failover.png){class="glboxshadow gl-90-desktop"}

You can set the priority of each interface, when the interface being used fails, the router will automatically switch to another available highest priority interface.

For example, if the router has been set up with two types of Internet access, **Ethernet** and **Repeater**, and the priority of of Ethernet is 1, the priority of Repeater is 2, the priority of Ethernet is higher than Repeater, so the router will use the Ethernet to access Internet. If you unpluged the ethernet cable, the Ethernet interface will become unavailable, then the router will automatically switch to Repeater interface to access Internet. After a while, if the Ethernet interface becomes available again, the router will continue to use Repeater if the **Forced Refresh Streams** is off, and vice versa, the router will switch back to the higher priority Ethernet.

### Load Balance

Use multiple interfaces at the same time to increase the total bandwidth of the router.

The system will assign interfaces to new connections based on the load ratio. The load ratio here can simply be set according to the bandwidth ratio. For example, if the bandwidth of Ethernet is 200Mbps, the bandwidth of Repeater's WiFi is 100Mbps, and no Tethering is connected, then the load ratio of Ethernet can be set to 2, the load ratio of Repeater to 1, and the load ratio of Tethering to 0.

**Note:** Alive connections or traffic are not ensured to match the load ratio. It is closer to this ratio if it has been used for a longer time.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/multi-wan_mode_load_balance.png){class="glboxshadow gl-90-desktop"}

## Usage Scenarios

* The store's cashier system uses a wired connection to the Internet, while Repeater to Wi-Fi in neighboring stores (or inserting a SIM card to enable cellular network) as a backup Internet access method to prevent mobile payments from being made when the network cable is unavailable.

* Router Repeater to public WiFi, but the network speed is not fast enough, then you can use Mobile Tethering to do load balance at the same time to improve the overall bandwidth.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
