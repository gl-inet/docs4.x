# Multi-WAN

On the left side of web Admin Panel -> NETWORK -> Multi-WAN

GL.iNet router can be connected to the Internet in multiple ways, such as [Ethernet](../internet_ethernet), [Repeater](../internet_repeater), [Tethering](../internet_tethering), [Cellular](../internet_cellular). You can configure the router with multiple Internet access methods, so that when one type of Internet access is not available, it can automatically switch to another type of Internet access in a short time. Or use multiple Internet access methods at the same time, assigning the network connection to different connection methods in a certain ratio.

## Interface Status Tracking Method

GL.iNet routers have up to 4 interfaces, but this varies depending on the model. They are **Ethernet**, **Repeater**, **Tethering** and **Cellular**. Here is the GL-AXT1800 as an example.

The router will use the ping or httping command to track the status of the connection to the destination IP to determine if the interface is available. If the interface is available, it will show as a green dot at the begining, otherwise it is gray.

![multi-wan interface status tracking method](https://static.gl-inet.com/docs/en/4/tutorials/multi-wan/interface_status_tracking_method.png){class="glboxshadow" width="80%" height="80%"}

The setting of Interface Status Tracking Method

![multi-wan interface status tracking method setting](https://static.gl-inet.com/docs/en/4/tutorials/multi-wan/interface_status_tracking_method_setting.png){class="glboxshadow" width="60%" height="60%"}

You can disable the interface status tracking, the router will use the physical status of the interface (such as whether the network cable is plugged in or not).

## Multi-WAN methods

There are two methods, **Failover** and **Load Balance**.

### Failover

![multi-wan failover](https://static.gl-inet.com/docs/en/4/tutorials/multi-wan/multi-wan_mode_failover.png){class="glboxshadow" width="60%" height="60%"}

You can set the priority of each interface, when the interface being used fails, the router will automatically switch to another available highest priority interface.

For example, if the router has been set up with two types of Internet access, **Ethernet** and **Repeater**, and the priority of of Ethernet is 1, the priority of Repeater is 2, the priority of Ethernet is higher than Repeater, so the router will use the Ethernet to access Internet. If you unpluged the ethernet cable, the Ethernet interface will become unavailable, then the router will automatically switch to Repeater interface to access Internet. After a while, if the Ethernet interface becomes available again, the router will continue to use Repeater if the **Forced Refresh Streams** is off, and vice versa, the router will switch back to the higher priority Ethernet.

### Load Balance

Use multiple interfaces at the same time to increase the total bandwidth of the router.

The system will assign interfaces to new connections based on the load ratio. 

Note: Alive connections or traffic are not ensured to match the load ratio. It is closer to this ratio if it has been used for a longer time.

![multi-wan load balance](https://static.gl-inet.com/docs/en/4/tutorials/multi-wan/multi-wan_mode_load_balance.png){class="glboxshadow" width="60%" height="60%"}

## Usage Scenarios

The store's cashier system uses a wired connection to the Internet, while Repeater to Wi-Fi in neighboring stores (or inserting a SIM card to enable cellular network) as a backup Internet access method to prevent mobile payments from being made when the network cable is unavailable.

