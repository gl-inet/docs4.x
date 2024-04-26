# Connect to the Internet via an ethernet cable

To access the Internet, it can connect the WAN port of router to the modem or the LAN port of other router via an ethernet cable.

On the left side of web Admin Panel -> INTERNET, Ethernet sector.

![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_ethernet/ethernet_dhcp.png){class="glboxshadow"}

**Note**: Before plugging the Ethernet cable into the WAN port of the router, you can click **Change to LAN** to [set the WAN port as a LAN port](../faq/change_wan_to_lan.md). That is useful when you are using the router as a [repeater](internet_repeater.md). As a result, you can have one more LAN port.

## Protocol

There are 3 types of protocols, DHCP, Static, PPPoE. Click **Modify** to change.

* DHCP

    DHCP is the default and most common protocol. It is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.

* Static

    Static is required if your Internet Service Provider (ISP) has provided a fixed IP address for you or you want to configure the network information such as IP address, Gateway, Netmask manually.

    ![ethernet static](images/internet_ethernet/ethernet_static.png){class="glboxshadow"}

* PPPoE

    PPPoE is required by many Internet Service Providers (ISP). Generally, your ISP will give you a modem and provide you a username & password that you needed when you are creating the Internet connection.

    ![ethernet pppoe](images/internet_ethernet/ethernet_pppoe.png){class="glboxshadow gl-90-desktop"}

## Advanced

* **VLAN ID**: This settings entry is only required if the provider's server requires the interface to use a tagged specific VLAN ID.

* **TTL**: TTL (Time To Live) sets the maximum time for packets to survive in the network, and is filled in according to the requirements of the operator. By default, the router forwards the TTL of the incoming client device minus one. If you need to camouflage, you can set a fixed value here. the TTL is valid only for IPv4.

* **HL**: In IPv6, the HL (Hop Limit) field is used to limit the number of transmission hops of data packets in the network, which is equivalent to the TTL in IPv4.

* **MTU**: The default value is 1500.

## Warning

When Internet access is not available, the corresponding warning is displayed. To determine whether you can access the Internet or not, please go to [Multi-WAN](multi-wan.md) page.

- Warning: *The interface is connected, but the Internet can't be accessed with IPv4 protocol.*

    ![ethernet wrning](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_ethernet/ethernet_warning.png){class="glboxshadow gl-90-desktop"}

    Solution: Please check if the upstream device of Ethernet has internet access.

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
