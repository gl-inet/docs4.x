# LAN

On the left side of the web Admin Panel, go to **NETWORK** -> **LAN**.

LAN is the network that your device is connected to when it is connected via the main Wi-Fi or via an Ethernet cable.

It includes Basic settings, DHCP server settings and Address Reservation.

## Basic Settings

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    This is the address that you would enter into your browser's address bar to access the router's admin page. 
    
    It is **192.168.8.1** by default. You can change it if it conflicts with your network.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **AP Isolation**

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

## DHCP Server

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client devices.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Click **Advanced** for further configuration if needed.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server 1**: The primary server that translates domain names into IP addresses.

- **DNS Server 2**: The secondary server used for domain name resolution if the primary DNS server is unavailable.

- **LPR Server**: (Line Printer Remote Server) A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

## Address Reservation

When you specify a reserved IP address for a client within the LAN, the client always receives the same IP address each time it accesses the router's DHCP server. You can assign reserved IP addresses to computers or servers that require permanent IP settings.

**Note:** Configured clients have to reconnect the router to activate.

Click **Add** to reserve an IP.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

You will see a pop-up window.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Select the **MAC** from the dropdown list, and the **IP** corresponding to the selected MAC will be auto-filled. Give it a descriptive name. Then click **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

After adding a new IP address reservation, you will get the page as shown below, which means you have set it up successfully.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.