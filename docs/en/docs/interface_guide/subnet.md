# Subnet  

**Note**: This page is currently available on Flint 4 (GL-BE14000), and will be rolled out to other models with firmware v4.10.

---

On the left side of the web Admin Panel, go to **NETWORK** -> **Subnet**. 

The page consolidates the configuration of **LAN**, **Guest Network**, **IoT Network**, and custom **VLAN Networks** into a single unified view. It provides a centralized management interface for all subnet-related settings, allowing you to create and manage multiple subnets to isolate different types of devices or traffic.

## Main Network

**Main Network** is the network that your device is connected to via the main Wi-Fi or via an Ethernet cable.

In the Main Network, you can directly view all interface statuses, VLAN ID, router IP address, and DHCP Range.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1 .png){class="glboxshadow"}

Click **Edit** in the lower-right corner to configure the Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

The configuration page includes Basic settings, DHCP server settings and Address Reservation.

### Basic Settings

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow"}

- **Router IP Address**

    This is the address that you would enter into your browser's address bar to access the router's admin page. 
    
    It is **192.168.8.1** by default. You can change it if it conflicts with your network.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    The Main Network's default VLAN ID is **1**, which cannot be modified.

- **AP Isolation**

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

### DHCP Server

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client devices.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow"}

Click **Advanced** for further configuration if needed.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow"}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow"}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server**: Two DNS server fields are available for configuring the primary and secondary resolvers. 
    
    **Note**: The primary DNS is entered in the upper field, and the secondary in the lower field. In the event of primary server unavailability, client devices will automatically failover to the secondary resolver, ensuring domain name resolution continuity.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

### Address Reservation

When you specify a reserved IP address for a client within the LAN, the client always receives the same IP address each time it accesses the router's DHCP server. You can assign reserved IP addresses to computers or servers that require permanent IP settings.

**Note:** Configured clients have to reconnect the router to activate.

Click **Add** to reserve an IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow"}

You will see a pop-up window.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow"}

Select **MAC** from the dropdown list. The corresponding available **IP** will be auto-filled. You can optionally enter a **hostname** and a custom **name** for easy identification. Then click **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow"}

After adding a new IP address reservation, you will get the page as shown below, which means you have set it up successfully.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow"}

## Guest Network

The **Guest Network** provides a dedicated Wi-Fi network for visitors. Isolated from the primary network, it enhances security while providing convenient internet access.

**Note**: Some models (e.g., GL-MT5000, GL-MT2500/GL-MT2500A) do not have Wi-Fi functionality, thus the Guest Network settings are not available on their web Admin Panel.

In the Guest Network, you can directly view the interface status, VLAN ID, Gateway, and DHCP Range.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Click **Edit** in the lower-right corner, and the Guest Network configuration panel will open on the right side of the page.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

The configuration page includes Basic settings and DHCP server settings.

### Basic Settings

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/gest-network-basic.png){class="glboxshadow"}

- **Gateway**

    The **default gateway** of the Guest Network is **192.168.9.1**. If it conflicts with your local network, change it to a different one.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    The Guest Network's default VLAN ID is **9**, which can be modified as required.

- **AP Isolation**

    This feature has been available since firmware v4.5

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

- **WAN Access Control**
  
    WAN Access Control manages local subnet access to WAN-side networks, including the internet and other WAN subnets.
    
    Three WAN access control modes are available:

    - **Unrestricted**: Allows this subnet to access the internet and other WAN-side subnets without restrictions.
  
    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.
  
    - **Block Internet Access**: Blocks all outbound access, including the internet and WAN-side subnets.

### DHCP Server

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client devices.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow"}

Click **Advanced** for further configuration if needed.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow"}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow"}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server**: Two DNS server fields are available for configuring the primary and secondary resolvers. 
    
    **Note**: The primary DNS is entered in the upper field, and the secondary in the lower field. In the event of primary server unavailability, client devices will automatically failover to the secondary resolver, ensuring domain name resolution continuity.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured. 

## IoT Network

The IoT Network creates a dedicated Wi-Fi network for IoT devices. Isolated from the primary network, it delivers better compatibility and improved security.

**Note**: Some models (e.g., GL-MT5000, GL-MT2500/GL-MT2500A) do not have Wi-Fi functionality, thus the IoT Network settings are not available on their web Admin Panel.

In the IoT Network, you can directly view the interface status, VLAN ID, Gateway, and DHCP Range.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Click **Edit** in the lower-right corner, and the IoT Network configuration panel will open on the right side of the page. You can configure Basic Settings and DHCP Server Settings in this panel.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Basic Settings

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow"}

- **Gateway**

    The **default gateway** of the Guest Network is **192.168.9.1**. If it conflicts with your local network, change it to a different one.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    The Guest Network's default VLAN ID is **10**, which can be modified as required.

- **AP Isolation**

    This feature has been available since firmware v4.5

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

- **WAN Access Control**
  
    WAN Access Control manages local subnet access to WAN-side networks, including the internet and other WAN subnets.
    
    Three WAN access control modes are available:

    - **Unrestricted**: Allows this subnet to access the internet and other WAN-side subnets without restrictions.
  
    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.
  
    - **Block Internet Access**: Blocks all outbound access, including the internet and WAN-side subnets.

### DHCP Server

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client devices.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow"}

Click **Advanced** for further configuration if needed.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow"}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow"}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server**: Two DNS server fields are available for configuring the primary and secondary resolvers. 
    
    **Note**: The primary DNS is entered in the upper field, and the secondary in the lower field. In the event of primary server unavailability, client devices will automatically failover to the secondary resolver, ensuring domain name resolution continuity.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

## VLAN Networks
 
At the top of the main page, you can create additional **VLAN networks** as needed to isolate different types of devices or visitor traffic.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Click the **+ Add** button on the right side of the page to configure a new network.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Basic Settings

You can configure the basic **VLAN Networks** information on this page.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow"}

- **Name**
    
    Customize a name for your newly created subnet for identification.
  
- **Gateway**

    Manually configure the gateway for the new subnet. Replace this gateway if it conflicts with your existing LAN segment.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    When creating a subnet, you must assign a VLAN ID between **9** and **4000**. Avoid using an already occupied VLAN ID to prevent network conflicts.

- **AP Isolation**

    This feature has been available since firmware v4.5

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

- **WAN Access Control**
  
    WAN Access Control manages local subnet access to WAN-side networks, including the internet and other WAN subnets.
    
    Three WAN access control modes are available:

    - **Unrestricted**: Allows this subnet to access the internet and other WAN-side subnets without restrictions.
  
    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.
  
    - **Block Internet Access**: Blocks all outbound access, including the internet and WAN-side subnets.

### DHCP Server

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client devices.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow"}

Click **Advanced** for further configuration if needed.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow"}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow"}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server**: Two DNS server fields are available for configuring the primary and secondary resolvers. 
    
    **Note**: The primary DNS is entered in the upper field, and the secondary in the lower field. In the event of primary server unavailability, client devices will automatically failover to the secondary resolver, ensuring domain name resolution continuity.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

Once configured, you can see the new VLAN network appear on the current page, showing the subnet information.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
