# Slate 7 (GL-BE3600) User Guide

## How to set up Slate 7

To set up Slate 7, you will use one of the four supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In this video we demonstrate the setup by configuring Slate 7 as Repeater. If you need to configure Slate 7 by other Internet connetion methods, please refer to the steps below.)</small>

### 1. Power on the Slate 7

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Touchscreen Explanation

#### Startup

When the router is powered on, the GL.iNet logo will be displayed on the screen, followed by the startup progress bar.

![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){class="glboxshadow"}
    
Once the progress bar is fully loaded, the device startup is completed.

#### Network

The home screen displays four icons representing four network connection types: Ethernet, Repeater, Tethering, and Cellular.

![network connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){class="glboxshadow"}

| Color               | Indication                     |
| :------------------ | :----------------------------- |
| Green               | Network connected.             |
| Yellow              | Network connecting or abnormal connection (e.g., no internet access).  |
| White               | No network connection.         |

Click on any of these icons to view the network status or detailed configuration information.

#### Functions

Access functions by swiping left and right.

| Action                | Indication                     |
| :-------------------- | :----------------------------- |
| Swipe Left to Right   | Move to the previous page      |
| Swipe Right to Left   | Move to the next page          |

When sliding from right to left, the following items are displayed in sequence, some of which require pre-configuration in the admin panel.

- Network connection

    ![network connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){class="glboxshadow"}

- Tri-band WiFi details (including the SSID, password, QR code and the switch button)

    ![wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wifi-details.png){class="glboxshadow"}

- OpenVPN

    ![openvpn](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/nordvpn-4.7.jpg){class="glboxshadow"}

- WireGuard

    ![wireguard](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wireguard.png){class="glboxshadow"}

- AdGuard Home

    ![adguard home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/adguard_home.png){class="glboxshadow"}

- Tor

    ![tor](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/tor.png){class="glboxshadow"}

- Traffic statistics (It refers to the average speed of all traffic passing through the router. The speed is calculated every 3 seconds.)

    ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/traffic_statistics.png){class="glboxshadow"}

- CPU overview

    ![CPU overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/overview.png){class="glboxshadow"}

- Time

    ![time](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/time.png){class="glboxshadow"}
    
When sliding from left to right, the display order is reversed.

#### System

Swipe from top to bottom to access the system settings: Reboot and Lock Screen.

![system settings](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/system_settings.png){class="glboxshadow"}

- Reboot: Clicking the "Reboot" will display the "Slide To Reboot" prompt (two-step verification), then the router will initiate a restart process.

    ![slide to reboot](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-reboot.png){class="glboxshadow"}

- Lock Screen: The screen will turn off when clicking the "Lock Screen" option. Tap the screen to wake it up, and the function page where it last stayed will be displayed. Clicking again will display the "Slide To Unlock" prompt.

    ![slide to unlock](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-unlock.png){class="glboxshadow"}

### 3. Connect your device to the Slate 7

Connect your computer or mobile device to the router using Wi-Fi or Ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

### 4. Connect the Slate 7 to the internet 

**Note:** The following instructions were written for those using the router web Admin Panel to connect the router to the internet. If you want to use the GL.iNet app instead of the web Admin Panel, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

#### 1. Sign in to the router web Admin Panel

In a web browser's address bar, enter `192.168.8.1` and sign in. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class="glboxshadow"}
    
    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a green dot appears next to "Ethernet."

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class="glboxshadow"}

    1. On the main screen of the web Admin Panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a green dot appears next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the web Admin Panel, click **Connect** in the "Tethering" section. 
    
    If you are connected to the internet successfully, a green dot appears next to "Tethering".

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class="glboxshadow"}

    Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

    Click [here](../../interface_guide/internet_cellular.md) to learn how to connect to the internet via USB modem.

**Note:** If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, you will have to set up more than one internet connection methods.

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Slate 7 (and other GL.iNet routers) support OpenVPN, WireGuard, and Tor. 


=== "OpenVPN" 
    Slate 7 (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    Slate 7 (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities. 
    
    * [How to set up Tor](../../interface_guide/tor.md).

## Wireless and clients

=== "Wireless"

    The Wireless page allows you to configure settings for both the 5 GHz and 2.4 GHz Wi-Fi networks, including enabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling randomized BSSID, selecting Wi-Fi security mode and password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel.

    To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    The Clients page displays information about connected devices. For each client, it shows the name, IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

    To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage GL.iNet routers. 
    
    To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp is an advanced networking platform designed to provide seamless remote networking and remote device management. Built specifically for GL.iNet router integration, AstroWarp supports comprehensive device management across entire networks, enabling both upper and lower device control. With a focus on network-wide management and future support for hardware-level control, AstroWarp offers a more robust and dependable solution for managing devices and maintaining secure, stable networks. 
    
    To set up AstroWarp, refer to [AstroWarp](../../interface_guide/astrowarp.md).

## Applications

=== "Plug-ins"

    A plugin is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. 
    
    To set up dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    To set up network storage, refer to [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    To set up AdGuard Home, refer to [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content.

    To set up parental controls, refer to [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

## Network settings

=== "Port forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. To set up port forwarding, refer to [Port Forwards](../../interface_guide/port_forwarding.md). 

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently. 
    
    To set up LAN, refer to [Lan Tutorial](../../interface_guide/lan.md). 

---

=== "Guest Network"

    It allows you to set a subnet within the IPv4 private address ranges 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8, specify the gateway and netmask IP addresses, and configure security settings like AP isolation for the guest network.

    To set up LAN, refer to [Lan Tutorial](../../interface_guide/guest_network.md). 

=== "DNS"

    The DNS page allows you to set custom DNS servers, enable DNS rebinding attack protection and override DNS settings of all clients, allow custom DNS to override VPN DNS, and configure the DNS server settings mode to automatic or manually specify DNS servers from the Ethernet connection.

    To set up DNS, refer to [DNS](../../interface_guide/dns.md).

=== "Network Port Management"

    The Network Port Management page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiate the network port rate.

---

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
    To set up drop-in gateway, refer to [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

---

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Hardware acceleration refers to the use of specialized hardware components to perform specific tasks more efficiently than general-purpose CPUs. 
    
    To set up network acceleration to this [Network Acceleration](../../interface_guide/network_acceleration.md) tutorial.

=== "NAT Settings"

    The NAT Settings page allows you to enable or disable Full Cone NAT and SIP ALG (Application Layer Gateway) functionality.

    To set up NAT settings, refer to [NAT Settings](../../interface_guide/nat_settings.md).

## System settings

=== "Overview"

    The Overview page provides a comprehensive snapshot of your router's current status and performance metrics. On this page, you can view:

    * CPU Average Load: Monitor the average load on your router’s CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    * Flash Usage: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * Device Info: Access detailed information about your router's system, including uptime, hostname, model, architecture, OpenWrt version, kernel version, device ID, device MAC and device S/N.
    * External Storage: Check the status of any external storage devices connected to the router, such as USB drives or TF cards.
    
    These features provide essential insights and controls, helping you to effectively manage and monitor your router's operation.

    For detailed setup instructions and more information, please refer to [Overview](../../interface_guide/system_overview.md){target="_blank"}.

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options for upgrading:

    * Firmware Online Upgrade: Automatically check for and install the latest firmware version directly from the manufacturer's server, simplifying the update process.
    * Firmware Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.

    These options allow you to keep your router up-to-date with the latest improvements and fixes.

    For detailed setup instructions and more information, please refer to [Upgrade](../../interface_guide/upgrade.md){target="_blank"}.

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to automate various router functions based on a predefined schedule, enhancing convenience and efficiency. Key features on this page include:

    * LED Display Schedule: Set a schedule to automatically turn the router's LED lights on or off, reducing light pollution during specific times.
    * Schedule Reboot: Configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.
    * 5GHz Wi-Fi Status Schedule: Set a schedule to control the 5GHz Wi-Fi band, allowing for better management of network availability and power consumption.
    * 2.4GHz Wi-Fi Status Schedule: Set a schedule to control the 2.4GHz Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    For detailed setup instructions and more information, please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

---

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    For detailed setup instructions and more information, please refer to [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Toggle Button Settings"

    The Toggle Button Settings page allows you to configure the physical toggle button on your router, enabling you to assign specific functions to the button for quick access and control. This feature provides convenient shortcuts for common tasks and settings, enhancing the user experience and simplifying router management.

    For detailed setup instructions and more information, please refer to [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    For detailed setup instructions and more information, please refer to [Log](../../interface_guide/log.md){target="_blank"}.

---

=== "Security"

    The Security page allows you to configure various security settings to protect your network and router from unauthorized access. This page includes options for:

    * Admin Password: Set or change the password for the router's administrative interface to ensure only authorized users can modify settings.
    * Local Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.
    * Open Ports on Router: Control which ports are open on the router, limiting potential vulnerabilities and unauthorized access.

    These settings help you maintain a secure network environment, safeguarding both your router and connected devices.

    For detailed setup instructions and more information, please refer to [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    For detailed setup instructions and more information, please refer to [Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"}.

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    For detailed setup instructions and more information, please refer to [Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}.

## Product overview

### Product information

Slate 7 (GL-BE3600) is a dual-band Wi-Fi 7 portable travel router, with a maximum Wi-Fi speed of 3600 Mbps. Supporting both OpenVPN and WireGuard, Slate 7 ensures robust performance. Its compact and lightweight design ensures unparalleled portability, making it the perfect companion for travel, while its durable construction provides long-lasting performance wherever you go.

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

### Package contents

Please note that the adapter within the package depends on your shipping country.

Your router package includes:

- 1 x User manual
- 1 x Slate 7 (GL-BE3600)
- 1 x Thank you card
- 1 x Warrenty card
- 1 x Ethernet cable
- 1 x Power adapter
- 1 x US Power Adapter
- 3 x Converters (EU, UK, and AU Plugs)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

### Specifications

Refer to [GL-BE3600 Specifications](https://www.gl-inet.com/products/gl-be3600/#specs){target="_blank"}.
