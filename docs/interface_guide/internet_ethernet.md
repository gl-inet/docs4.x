# Connect to the Internet via an ethernet cable

Connect the WAN port of your GL.iNet router to the modem or the LAN port of your host router via an ethernet cable to access the Internet.

On the left side of web Admin Panel -> INTERNET -> Ethernet section.

![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Note**: Before plugging the Ethernet cable into the WAN port of the router, you can click **Change to LAN** to [set the WAN port as a LAN port](../faq/change_wan_to_lan.md). That is useful when you are using the router as a [repeater](internet_repeater.md) since the physical WAN port is idle. Therefore, you can repurpose the unused WAN port as a LAN port and then you will have one more LAN port.

## Protocol

There are 3 types of protocols, DHCP, Static, PPPoE. Click **Modify** to change.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP is the default and most common protocol. It is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static is required if your Internet Service Provider (ISP) has provided a fixed IP address for you or you want to configure the network information such as IP address, Gateway, Netmask manually.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE is a protocol used by many Internet Service Providers (ISPs). Generally, your ISP will provide a modem and give you a username & password that you need when setting up the Internet connection.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Advanced

* **VLAN ID**: This setting entry is only required if the provider's server requires the interface to use a specific tagged VLAN ID.

* **TTL**: TTL (Time To Live) defines the maximum time for packets to survive in the network, and should be configured according to the operator's requirements. By default, the router forwards the TTL of the incoming client device minus one. If you need to camouflage it, you can set a fixed value here. The TTL is valid only for IPv4. 

* **HL**: In IPv6, the HL (Hop Limit) field limits the number of transmission hops for data packets in the network, serving as the equivalent of TTL in IPv4.

* **MTU**: The default MTU value is 1500 bytes.

## Ethernet Ports

Click the cog icon in the upper right corner of the Ethernet section to enter [Network Port Management](network_port_management.md).

![network port management 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

![network port management 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_7.png){class="glboxshadow"}

Click on **WAN**, it displays the network port status (i.e. using as WAN/LAN), MAC mode & MAC address, as well as the negotiated network port rate of the WAN port.

Click on **LAN** it displays the negotiated network port rate of the LAN port.

Please refer to this [link](network_port_management.md) for more details. 

## Warning

When Internet access is not available, the corresponding warning will be displayed as shown below. To determine whether you can access the Internet or not, please go to [Multi-WAN](multi-wan.md) page.

- Warning: *The interface is connected, but the Internet can't be accessed.*

    ![ethernet wrning](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_8.jpg){class="glboxshadow gl-90-desktop"}

    Solution: Please check if the upstream device of Ethernet has internet access.

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
