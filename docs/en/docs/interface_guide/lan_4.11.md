# LAN {#lan}

**Note**: The content on this page is based on firmware version v4.11 and above. If your device is running a different firmware version, use the selector below to switch to the corresponding guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11 and above" markdown="1">

- [Firmware v4.9 and earlier](lan.md)

</div>

---

On the left side of the web Admin Panel, go to **NETWORK** -> **LAN**. 

This page provides centralized configuration and management of the **Main Network**, **Guest Network**, **IoT Network**, and custom **VLAN Networks**. You can create and manage multiple subnets to isolate different types of devices or traffic.

## Main Network {#main-network}

**Main Network** is the network that your device is connected to via the main Wi-Fi or via an Ethernet cable.

In the Main Network, you can directly view all interface statuses, VLAN ID, router IP address, and DHCP Range.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Click **Edit** in the lower-right corner to configure the Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

The configuration page includes Basic settings, DHCP server settings and Address Reservation.

### Basic Settings {#basic-settings}

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    This is the address that you would enter into your browser's address bar to access the router's admin page. 
    
    It is **192.168.8.1** by default. You can change it if it conflicts with your network.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    The Main Network's default VLAN ID is **1**, which cannot be modified.

- **AP Isolation**

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

    **Note:** AP Isolation applies only to Wi-Fi clients, not wired devices.

### DHCP Server {#dhcp-server}

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client device.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![main network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Click **Advanced** for further configuration if needed.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server 1**: The primary server that translates domain names into IP addresses.

- **DNS Server 2**: The secondary server used for domain name resolution if the primary DNS server is unavailable.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

### Address Reservation {#address-reservation}

When you specify a reserved IP address for a client within the LAN, the client always receives the same IP address each time it accesses the router's DHCP server. You can assign reserved IP addresses to computers or servers that require permanent IP settings.

**Note:** Configured clients have to reconnect the router to activate.

Click **Add** to reserve an IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=650}

You will see a pop-up window.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=650}

Select **MAC** from the dropdown list. The corresponding available **IP** will be auto-filled. You can optionally enter a **hostname** and a custom **name** for easy identification. Then click **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=650}

After adding a new IP address reservation, you will get the page as shown below, which means you have set it up successfully.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=650}

## Guest Network {#guest-network}

The **Guest Network** provides a dedicated Wi-Fi network for visitors. Isolated from the primary network, it enhances security while providing convenient internet access.

**Note**: Some models (e.g., GL-MT5000, GL-MT2500/GL-MT2500A) do not have Wi-Fi functionality, thus the Guest Network settings are not available on their web Admin Panel.

In the Guest Network, you can directly view the interface status, VLAN ID, Gateway, and DHCP Range.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Click **Edit** in the lower-right corner, and the Guest Network configuration panel will open on the right side of the page.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

The configuration page includes Basic settings and DHCP server settings.

### Basic Settings {#basic-settings_1}

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    The **default gateway** of the Guest Network is **192.168.9.1**. If it conflicts with your local network, change it to a different one.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    The Guest Network's default VLAN ID is **9**, which can be modified as required.

- **Associated LAN Ports**

    Select the LAN ports to assign to this subnet. Wired devices connected to these ports will join this network.

- **AP Isolation**

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

    **Note:** AP Isolation applies only to Wi-Fi clients, not wired devices.

- **WAN Access Control**
  
    WAN Access Control manages local subnet access to WAN-side networks, including the internet and other WAN subnets.
    
    Three WAN access control modes are available:

    - **Unrestricted**: Allows this subnet to access the internet and other WAN-side subnets without restrictions.
  
    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.
  
    - **Block Internet Access**: Blocks all outbound access, including the internet and WAN-side subnets.

### DHCP Server {#dhcp-server_1}

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client device.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![guest network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Click **Advanced** for further configuration if needed.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server 1**: The primary server that translates domain names into IP addresses.

- **DNS Server 2**: The secondary server used for domain name resolution if the primary DNS server is unavailable.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured. 

## IoT Network {#iot-network}

The IoT Network creates a dedicated Wi-Fi network for IoT devices. Isolated from the primary network, it delivers better compatibility and improved security.

**Note**: Some models (e.g., GL-MT5000, GL-MT2500/GL-MT2500A) do not have Wi-Fi functionality, thus the IoT Network settings are not available on their web Admin Panel.

In the IoT Network, you can directly view the interface status, VLAN ID, Gateway, and DHCP Range.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Click **Edit** in the lower-right corner, and the IoT Network configuration panel will open on the right side of the page. You can configure Basic Settings and DHCP Server Settings in this panel.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Basic Settings {#basic-settings_2}

You can set the subnet within the IPv4 private address ranges: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    The **default gateway** of the IoT Network is **192.168.10.1**. If it conflicts with your local network, change it to a different one.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    The IoT Network's default VLAN ID is **10**, which can be modified as required.

- **Associated LAN Ports**

    Select the LAN ports to assign to this subnet. Wired devices connected to these ports will join this network.

- **AP Isolation**

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

    **Note:** AP Isolation applies only to Wi-Fi clients, not wired devices.

- **WAN Access Control**
  
    WAN Access Control manages local subnet access to WAN-side networks, including the internet and other WAN subnets.
    
    Three WAN access control modes are available:

    - **Unrestricted**: Allows this subnet to access the internet and other WAN-side subnets without restrictions.
  
    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.
  
    - **Block Internet Access**: Blocks all outbound access, including the internet and WAN-side subnets.

### DHCP Server {#dhcp-server_2}

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client device.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![iot network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Click **Advanced** for further configuration if needed.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server 1**: The primary server that translates domain names into IP addresses.

- **DNS Server 2**: The secondary server used for domain name resolution if the primary DNS server is unavailable.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

## VLAN Networks {#vlan-networks}
 
At the top of the main page, you can create additional **VLAN networks** as needed to isolate different types of devices or visitor traffic.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Click the **+ Add** button on the right side of the page to configure a new network.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Basic Settings {#basic-settings_3}

You can configure the basic **VLAN Networks** information on this page.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**
    
    Customize a name for your newly created subnet for identification.
  
- **Gateway**

    Manually configure the gateway for the new subnet. Replace this gateway if it conflicts with your existing LAN segment.

- **Netmask**
    
    Defaults to **255.255.255.0**. You can also select **255.255.0.0** if you need a larger subnet with more IP addresses.

- **VLAN ID**
  
    When creating a subnet, you must assign a VLAN ID between **9** and **4000**. Avoid using an already occupied VLAN ID to prevent network conflicts.

- **Associated LAN Ports**

    Select the LAN ports to assign to this subnet. Wired devices connected to these ports will join this network.

- **AP Isolation**

    You can isolate client devices into a separate network segment. These devices will not be able to communicate with other devices on the same network.

    **Note:** AP Isolation applies only to Wi-Fi clients, not wired devices.

- **WAN Access Control**
  
    WAN Access Control manages local subnet access to WAN-side networks, including the internet and other WAN subnets.
    
    Three WAN access control modes are available:

    - **Unrestricted**: Allows this subnet to access the internet and other WAN-side subnets without restrictions.
  
    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.
  
    - **Block Internet Access**: Blocks all outbound access, including the internet and WAN-side subnets.

### DHCP Server {#dhcp-server_3}

The **DHCP Server** is enabled by default. The DHCP server automatically assigns IP addresses and other communication parameters to each client device.

If the DHCP server is disabled, you will need to configure network settings for client devices manually. Click [here](../tutorials/manually_configure_static_ip.md) to learn how to manually configure a static IP.

You can change the starting and ending IP addresses to suit your needs — for example, if your network expands or shrinks, if IP address conflicts occur, or if the subnet mask range is modified.

![vlan networks dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Click **Advanced** for further configuration if needed.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: The period for which a DHCP-assigned IP address is valid for a device.

- **Gateway**: The device that routes traffic between the local network and external networks such as the Internet.

- **DNS Server 1**: The primary server that translates domain names into IP addresses.

- **DNS Server 2**: The secondary server used for domain name resolution if the primary DNS server is unavailable.

- **LPR Server** (Line Printer Remote Server): A service that manages print jobs and allows network devices to send print requests to remote printers. Multiple LPR printer ports can be configured.

Once configured, you can see the new VLAN network appear on the current page, showing the subnet information.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
