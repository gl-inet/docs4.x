# LAN

On the left side of web Admin Panel -> NETWORK -> LAN

LAN is the network that your device is connected to when it is connected via the main WiFi or via an Ethernet cable.

It includes Basic settings, DHCP server settings and Address Reservation.

## Basic Settings

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    The router IP Address is the address that you would enter into your browser 's address bar to access the router's admin page. 
    
    It is **192.168.8.1** by default. You can change it if it conflicts with your network.

- **Netmask**
    
    Two options are provided: **255.255.255.0** and **255.255.0.0**

- **AP Isolation**

    You can isolate your network's client devices into a separate network area. These devices cannot communicate with other devices on the network.

## DHCP Server

The **DHCP Server** is enabled by default.The DHCP server automatically assigning IP addresses and other communication parameters to each client devices.If the DHCP server is disabled, you will have to configure them manually for each client. [How to manually configure static ip?](../tutorials/manually_configure_static_ip.md)

You can change the starting and ending IP addresses to suit your needs, for example, if the size of the network expands or shrinks, if there are IP address conflicts in the network, or if the subnet mask or IP address range has changed.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Click **Advanced** for further setup if needed.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: The duration for which a device can use an IP address assigned via DHCP.

- **Gateway**: The device that routes traffic between the local network and external networks (e.g., the internet).

- **DNS Server 1**: The primary server responsible for translating domain names into IP addresses.

- **DNS Server 2**: A backup server used to resolve domain names if the primary DNS server fails.

- **LPR Server**: (Line Printer Remote Server) A service that manages print jobs and enables networked devices to send print requests to remote printers. Multiple printer LPR ports can be filled.

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