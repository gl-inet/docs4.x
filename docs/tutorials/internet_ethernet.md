# Connect to the Internet via an ethernet cable

To access the Internet, it can connect the WAN port of router to the modem or the LAN port of other router via an ethernet cable.

On the left side of web Admin Panel -> INTERNET, Ethernet sector.

![ethernet dhcp](https://static.gl-inet.com/docs/en/4/tutorials/internet_ethernet/ethernet_dhcp.png){class="glboxshadow"}

**Note**: Before plugging the Ethernet cable into the WAN port of the router, you can click **Change to LAN** to [set the WAN port as a LAN port](../change_wan_to_lan/). That is useful when you are using the router as a [repeater](../internet_repeater). As a result, you can have one more LAN port.

## Protocol

There are 3 types of protocols, DHCP, Static, PPPoE. Click **Modify** to change.

* DHCP 

    DHCP is the default and most common protocol. It is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.

* Static

    Static is required if your Internet Service Provider (ISP) has provided a fixed IP address for you or you want to configure the network information such as IP address, Gateway, Netmask manually.

    ![ethernet static](https://static.gl-inet.com/docs/en/4/tutorials/internet_ethernet/ethernet_static.png){class="glboxshadow"}

* PPPoE

    PPPoE is required by many Internet Service Providers (ISP). Generally, your ISP will give you a modem and provide you a username & password that you needed when you are creating the Internet connection.

    ![ethernet pppoe](https://static.gl-inet.com/docs/en/4/tutorials/internet_ethernet/ethernet_pppoe.png){class="glboxshadow"}
