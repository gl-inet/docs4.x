# LAN

On the left side of web Admin Panel -> NETWORK -> LAN

## LAN

LAN is the network that your device is connected to when it is connected via the main WiFi or via an Ethernet cable.

The **Router IP Address** is **192.168.8.1** by default. You can change it if it conflicts with your network.

![lan simple set](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/lan_simple_set.png){class="glboxshadow"}


## DHCP Server

The **DHCP Server** is enabled by default.The DHCP server automatically assigning IP addresses and other communication parameters to each client devices.If the DHCP server is disabled, you will have to configure them manually for each client. [How to manually configure static ip?](../tutorials/manually_configure_static_ip.md)

You can change the starting and ending IP addresses to suit your needs, for example, if the size of the network expands or shrinks, if there are IP address conflicts in the network, or if the subnet mask or IP address range has changed.

![dhcp_simple_set](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_simple_set.jpg){class="glboxshadow"}

- Advanced

    You can click **Advanced** for more manually settings.

    ![lan page, private network advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_set.jpg){class="glboxshadow"}

## Address Reservation

When you specify a reserved IP address for a client within the LAN, the client always receives the same IP address each time it accesses the router's DHCP server. You can assign reserved IP addresses to computers or servers that require permanent IP settings.

**Note:** Configured clients have to reconnect the router to activate.

Click **Add** to reserve an IP.

![lan page, Address Reservation](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/reserve_ip.png){class="glboxshadow"}

Select the **MAC**, the **IP** corresponding to the selected MAC will be auto-filled. Give it a descriptive name. Then click **Submit**.

![lan page, Address Reservation, add a new reservation entry](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/add_a_new_reservation_entry.png){class="glboxshadow"}

After adding a new IP address reservation, you will get the page as shown below, which means you have set it up successfully.

![lan page, added reserve ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/reserve_ip_added.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.