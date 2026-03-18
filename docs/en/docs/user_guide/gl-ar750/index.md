# Creta (GL-AR750) User Guide

## Product overview

Creta (GL-AR750) is a dual-band travel AC router. The simultaneous dual-band supports up to 733Mbps (2.4GHz: 300Mbps + 5GHz: 433Mbps) wireless transmission rate. Creta can convert a public network to a private Wi-Fi for secure surfing. External storage supports MicroSD up to 128GB. OpenWrt/LEDE and OpenVPN are pre-installed. Therefore, Creta gives the privacy-minded users a fast and simple VPN that utilizes state-of-the-art cryptography.

![ar750 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/product_info/ar750_overview.png){class="glboxshadow"}

### Specifications

[GL-AR750 specifications](https://www.gl-inet.com/products/gl-ar750/#specs){target="_blank"}

## How to set up Creta

To set up Creta, you will use one of the four supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Creta and other router models.)</small>

### 1. Power on Creta

Plug the Micro USB power cable into the power port of the router. Make sure you are using a standard 5V/2A power adapter.

!!! Note

    Hot plugging for TF card is not supported. If you want to use TF card, please insert before powering on the router.

### 2. Connect your device to Creta

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable.

### 3. Connect Creta to the internet 

**Note:** The following instructions were written for those connecting the router to Internet via web admin panel. If you want to use the GL.iNet app instead of the web admin panel, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

#### 1. Log in to the router web admin panel

In a web browser's address bar, enter `192.168.8.1`. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/ethernet.png){class="glboxshadow"}
    
    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a green dot appears next to "Ethernet."

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/repeater.png){class="glboxshadow"}

    1. On the main screen of the web admin panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a green dot appears next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/tethering.png){class="glboxshadow"}

    1. Connect your smartphone to the router via USB cable and enable network shareing in Personal hotspot of the setting.
    2. On the main screen of the web admin panel, locate the "Tethering" section, then click **Connect**.
    3. If you are connected to the internet successfully, a green dot appears next to "Tethering".

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/usb_modem.png){class="glboxshadow"}

    1. Insert a cellular-enabled USB modem into the router's USB port.
    2. On the main screen of the web admin panel, locate the "Cellular" section, then click **Connect**.
    3. If you are connected to the internet successfully, a green dot appears next to "Cellular."

    Please refer to [Connect to the Internet via a USB modem](../../interface_guide/internet_cellular.md) for detailed instructions.

**Note:** If you want to use the multi-WAN feature, you will have to set up more than one internet connection methods. 

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Creta (and other GL.iNet routers) support OpenVPN and WireGuard.

=== "OpenVPN" 

    Creta (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Creta (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

---

## More applications

=== "Plug-ins"

    Plug-ins are add-on features that enhance the functionality of your router. To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. To set up dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage GL.iNet routers. To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

---

## Network settings

=== "Firewall"

    The Firewall page provides essential security enhancements for your network. It includes features such as Port Forwarding, Open Ports, and DMZ. These tools allow you to manage and customize your network's traffic flow and enhance its security.

    * Port Forwarding: Redirect specific traffic from the internet to designated devices within your network, enabling access to services like gaming servers or web servers.
    * Open Ports: Monitor and control which ports on your router are open, helping to prevent unauthorized access and potential security threats.
    * DMZ (Demilitarized Zone): Place a device outside the main firewall, allowing it to have unrestricted access to the internet while protecting the rest of your network from potential threats.

    For detailed setup instructions and more information, please refer to [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    The LAN page allows you to manage and configure your router's local area network settings. Key features available on this page include:

    * Router IP Address: Modify the IP address of your router to better fit your network configuration.
    * Netmask: Set the subnet mask for your network, which determines the network's size and range of IP addresses.
    * DHCP: Enable or configure the Dynamic Host Configuration Protocol, which automatically assigns IP addresses to devices on your network.
    * Address Reservation: Reserve specific IP addresses for particular devices, ensuring they always receive the same IP address from the DHCP server.

    For detailed setup instructions and more information, please refer to [LAN](../../interface_guide/lan.md).

---

=== "DNS"

    The DNS page provides options to customize your router's Domain Name System settings, enhancing both security and performance. Key features available on this page include:

    * Encrypted DNS: Configure encrypted DNS to protect your browsing data from being monitored or tampered with, ensuring privacy and security.
    * Manual DNS: Manually set DNS servers of your choice, allowing for customized control over DNS queries and potentially faster resolution times.
    * DNS Proxy: Enable DNS proxy to route DNS requests from your devices through a specified DNS server, providing an additional layer of control over DNS traffic.

    These settings allow you to optimize your network's DNS performance and security according to your specific needs.

    For detailed setup instructions and more information, please refer to [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    The Network Mode page allows you to configure your router to operate in different modes, providing flexibility to meet various networking needs. The available modes include:

    * Router: Operate as a standard router, managing traffic between your local network and the internet, and providing features like NAT, firewall, and DHCP.
    * Access Point: Function as an access point, extending your existing wired network by providing wireless connectivity without routing traffic.
    * Extender: Work as a range extender, boosting the signal of your existing wireless network to cover a larger area and eliminate dead zones.
    * WDS (Wireless Distribution System): Similar to Extender, please choose WDS if your main router supports WDS mode.

    For detailed setup instructions and more information, please refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    The IPv6 page enables you to configure IPv6 settings for your network, providing support for the latest internet protocol. On this page, you can enable IPv6 and select from four different modes to suit your network requirements:

    * Native: Obtain an IPv6 address directly from your ISP, allowing for straightforward and efficient native IPv6 connectivity.
    * Passthrough: Allow IPv6 traffic to pass through the router to the devices on your network, effectively bridging the connection without the router handling IPv6 routing itself.
    * NAT6: Utilize Network Address Translation for IPv6 (NAT6) to translate between internal and external IPv6 addresses, similar to how NAT works for IPv4.
    * Static IPv6: Manually configure a static IPv6 address for your router, providing a fixed address for consistent connectivity and easier management of network services.

    These settings help you leverage the benefits of IPv6, including improved address space, enhanced security features, and better performance.

    For detailed setup instructions and more information, please refer to [IPv6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    The MAC Address page allows you to view and manage the Media Access Control (MAC) addresses associated with your router. Key features available on this page include:

    * Factory Default: Display the default MAC addresses for the router’s Ethernet and Repeater modes, providing a reference for original hardware settings.
    * Clone: Clone the MAC address of a specific client device. This is particularly useful in scenarios where network access is restricted to certain devices.
    * Manual: Manually specify a custom MAC address for your router. Additionally, you can use the Random button to generate a random MAC address, providing flexibility and enhanced privacy.

    These features enable you to manage your router's MAC addresses effectively, ensuring compatibility and flexibility within various network environments.

    For detailed setup instructions and more information, please refer to [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. To set up Drop-in Gateway, refer to [How to set up Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    The IGMP Snooping page allows you to configure settings that optimize multicast traffic management within your network. IGMP Snooping listens to and extracts information from IGMP protocol packets, establishing and maintaining Layer 2 multicast forwarding tables. This ensures that multicast group data is forwarded only to hosts that have joined the multicast group, preventing unwanted multicast traffic from reaching other hosts.

    These settings help optimize network performance and efficiency, particularly in environments with significant multicast traffic, such as streaming video or online gaming.

    For detailed setup instructions and more information, please refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## System settings

=== "Overview"

    The Overview page provides a comprehensive snapshot of your router's current status and performance metrics. On this page, you can view:

    * CPU Average Load: Monitor the average load on your router’s CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * Flash Usage: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    * System Info: Access detailed information about your router's system, including firmware version, uptime, and network status.
    
    These features provide essential insights and controls, helping you to effectively manage and monitor your router's operation.

    For detailed setup instructions and more information, please refer to [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options for upgrading:

    * Online Upgrade: Automatically check for and install the latest firmware version directly from the manufacturer's server, simplifying the update process.
    * Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.

    These options allow you to keep your router up-to-date with the latest improvements and fixes.

    For detailed setup instructions and more information, please refer to [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to automate various router functions based on a predefined schedule, enhancing convenience and efficiency. Key features on this page include:

    * LED Display Schedule: Set a schedule to automatically turn the router's LED lights on or off, reducing light pollution during specific times.
    * Schedule Reboot: Configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.
    * 5GHz Wi-Fi Status Schedule: Create a schedule to enable or disable the 5GHz Wi-Fi band at certain times, optimizing network usage and energy efficiency.
    * 2.4GHz Wi-Fi Status Schedule: Set a schedule to control the 2.4GHz Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    For detailed setup instructions and more information, please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    The Admin Password page allows you to set or change the password for your router's administrative interface, ensuring that only authorized users can access and modify the router's settings. This password is crucial for maintaining the security and integrity of your network, protecting against unauthorized access and configuration changes.

    For detailed setup instructions and more information, please refer to [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    For detailed setup instructions and more information, please refer to [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    The Toggle Button Settings page allows you to configure the physical toggle button on your router, enabling you to assign specific functions to the button for quick access and control. This feature provides convenient shortcuts for common tasks and settings, enhancing the user experience and simplifying router management.

    For detailed setup instructions and more information, please refer to [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    For detailed setup instructions and more information, please refer to [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    For detailed setup instructions and more information, please refer to [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    For detailed setup instructions and more information, please refer to [Advanced Settings](../../interface_guide/advanced_settings.md).
