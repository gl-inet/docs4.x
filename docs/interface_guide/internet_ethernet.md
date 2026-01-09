# Connect to the Internet via an Ethernet cable

Connect the router to a broadband network via an Ethernet cable plugged into the WAN port. It usually automatically acquires an IP address (DHCP). Users can also configure static IP or PPPoE manually. This method offers high stability and fast speed, making it ideal for home and office environments with fixed broadband access.

Follow the steps below to connect your router to the Internet via an Ethernet cable.

1. Connect the WAN port of your router to the upstream device (e.g., an ISP modem, router, network switch or an Ethernet jack) via an Ethernet cable. 

2. Log in to the router's web admin panel, navigate to **INTERNET** -> **Ethernet** section. 

    If the connection is successful, the Ethernet section will display network details, including Protocol, IP Address, Gateway and DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Tips**: Before plugging the Ethernet cable into the WAN port of the router, you can click **Change to LAN** to [set the WAN port as a LAN port](../faq/change_wan_to_lan.md). That is useful when you are using the router as a [repeater](internet_repeater.md) since the physical WAN port is idle. Therefore, you can repurpose the unused WAN port as a LAN port and then you will have one more LAN port.

## Protocol

There are 3 types of protocols, DHCP, Static, PPPoE. Click **Modify** to change.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP is the default and most common protocol, automatically assigning IP addresses and other communication parameters to network devices via a client-server architecture on IP networks.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static is needed if your ISP (Internet Service Provider) provides a fixed IP address, or you want to manually configure network information, such as IP address, Gateway, Netmask.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE is a protocol used by most ISPs. Typically, they provide a modem and a username & password, which are needed for Internet setup.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Advanced

In addition to the essential settings, there are also some optional advanced settings for the above three protocols

* **VLAN ID**: This setting entry is required only if the provider's server requires the interface to use a specific tagged VLAN ID.

* **TTL**: TTL (Time To Live) defines the maximum time packets can survive in the network. By default, the router decrements the TTL of incoming packets from client devices by 1 before forwarding them. If you need to override it, you can set a fixed value here. The TTL setting is valid only for IPv4.

* **HL**: In IPv6, the HL (Hop Limit) field limits the number of transmission hops for data packets in the network, serving as the equivalent of TTL in IPv4.

* **MTU**: The default MTU value is 1500 bytes.

## Ethernet Ports

Click the gear icon in the upper right corner of the Ethernet section to enter [Port Management](network_port_management.md).

![port management 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

Click on **WAN**: It displays the network port status (i.e. using as WAN/LAN), MAC mode & MAC address, as well as the negotiated network port rate of the WAN port.

![port management 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_7.jpg){class="glboxshadow"}

Click on **LAN**: It displays the negotiated network port rate of the LAN port.

![port management 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_8.png){class="glboxshadow"}

Please refer to this [link](network_port_management.md) for more details. 

## Caution

When Internet access is not available, a yellow caution message will be displayed as shown below, reminding you to check network settings or connections. 

**The interface is connected, but the Internet can't be accessed.**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Please check if the upstream device of Ethernet has internet access, or navigate to [Multi-WAN](multi-wan.md) page to check the Ethernet interface status.

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
