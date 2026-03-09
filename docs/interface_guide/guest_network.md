# Guest Network

The guest network settings have been separated from [LAN](lan.md) since firmware v4.5.

On the left side of the web Admin Panel, go to **NETWORK** -> **Guest Network**. 

It includes Guest Network basic settings and DHCP server settings.

## Basic Settings

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

You can set a separate, isolated network designed for temporary users, providing limited access and enhanced security by being segregated from the primary network.

**Note**: Some models (e.g., GL-MT5000, GL-MT2500/GL-MT2500A) do not support Wi-Fi, thus the Guest Network settings are not available on their web Admin Panel.

- **Gateway**

    The **default gateway** of the Guest Network is **192.168.9.1**. If it conflicts with your local network, change it to a different one.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **AP Isolation**

    This feature has been available since firmware v4.5

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

- **Block WAN Subnets**

    This feature has been available since firmware v4.8

    When enabled, the guest network cannot access the upstream network and its subnet.

## DHCP Server

If the Guest Network is enabled, the DHCP Server will be enabled by default.

The DHCP server automatically assigns IP addresses and other communication parameters to each client devices connected to Guest Network. If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Click **Advanced** for further configuration if needed.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the guest network and external networks such as the Internet.

- **DNS Server 1**: The primary server that translates domain names into IP addresses.

- **DNS Server 2**: The secondary server used for domain name resolution if the primary DNS server is unavailable.

- **LPR Server**: (Line Printer Remote Server) A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

---

Related Articles:

- [How to set up a guest Wi-Fi network on GL.iNet routers](../tutorials/how_to_set_up_a_guest_network.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
