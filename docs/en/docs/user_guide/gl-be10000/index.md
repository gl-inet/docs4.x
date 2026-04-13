# Slate 7 Pro (GL-BE10000) User Guide

## Product overview

Slate 7 Pro (GL-BE10000) is a tri‑band Wi‑Fi 7 portable travel router. As an upgraded version of Slate 7 (GL-BE3600), it features a larger touchscreen on the top, and is equipped with 1GB DDR4 RAM and 8GB eMMC flash storage for stable performance and plugin compatibility. It delivers high VPN speeds of up to 1,100 Mbps for WireGuard® and 1,000 Mbps for OpenVPN-DCO. With 2× 2.5G Ethernet ports (1 WAN + 1 LAN), 1× USB-C 3.0 port and PD power support, it provides strong connectivity and convenience for travel and mobile use.

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## Package contents

The package includes:

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x User manual
- 1 x Thank you card
- 1 x Ethernet cable
- 1 x Power cable
- 1 x Power Adapter
- 4 x Converters (US, EU, UK, and AU Plugs)

## How to set up Slate 7 Pro

To set up Slate 7 Pro, you will use one of the four supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. Follow the steps below.

### 1. Power on

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Touchscreen

When the router is powered on, the GL.iNet logo will be displayed on the screen, followed by the startup progress bar.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){class="glboxshadow" width="360"}

Once the progress bar is fully loaded, the device completes startup and enters the welcome screen. Follow the prompts to set your admin password and Wi-Fi network.

![set admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){class="glboxshadow" width="360"}

![set WiFi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){class="glboxshadow" width="360"}

You will then enter the home screen. The left side shows real-time system info, including system time and network speed, and provides shortcut tiles for Wi-Fi, Clients, VPN, and other functions. The right side provides shortcut tiles for the four connection modes: Ethernet, Repeater, Tethering, and Cellular.

![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){class="glboxshadow" width="360"}

Different colors on the four shortcut tiles indicate different network status.

![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){class="glboxshadow" width="360"}

- **Blue**: Active / Connected to Internet
- **Yellow**: Connecting / Network Failure
- **White**: Inactive connection

### 3. Connect device

Connect a device (e.g., computer, laptop or smartphone) to the router using Wi-Fi or Ethernet.

- Ethernet

    Connect your device to the router's LAN port using an ethernet cable. 

- Wi-Fi

    On your device, locate your router's Wi-Fi network name in the available networks list, and enter the password to join the network. You can find the default network name (SSID) and password printed on the router's label.

### 4. Log in to web Admin Panel

Open a web browser, enter `192.168.8.1` in the address bar and log in. Choose a language and set your admin password, then click **Apply**. 

### 5. Internet setup

Configure your Slate 7 Pro using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}
    
    1. Connect the Slate 7 Pro's WAN port to an upstream device (e.g., ISP modem, network switch, or wall Ethernet jack) using an Ethernet cable. 
    2. Slate 7 Pro will automatically attempt to obtain network parameters, such as IP address, gateway, and DNS server, to establish an Ethernet connection.
    3. Once successfully connected to the internet, the Ethernet section on the touchscreen homepage will turn blue (active). You can either tap Ethernet on the touchscreen homepage or log in to the web admin panel to check the connection details.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. Tap **Repeater** on the touchscreen. It will start scanning for available Wi-Fi networks.
    2. Select the Wi-Fi network you want Slate 7 Pro to extend. 
    3. Enter the password and tap **Apply**.
    4. Once successfully connected to the internet, the Repeater section on the touchscreen homepage will turn blue (active). You can either tap Repeater on the touchscreen homepage or log in to the web admin panel to check the connection details.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device (e.g., smartphone or USB dongle) to the router's USB port using a USB cable. 
    2. On your mobile device, go to Settings and enable **USB Tethering** or **Personal Hotspot**. For iPhone, tap **Trust This Device** if prompted. 
    3. On the touchscreen, select **Tethering** and tap **Connect**. The router will connect to your device.
    4. Once successfully connected to the internet, the Tethering section on the touchscreen homepage will turn blue (active). You can either tap Tethering on the touchscreen homepage or log in to the web admin panel to check the connection details.

    **Note**: If the connection fails, make sure the power supply voltage is above 9V 3A, as low power supply may prevent the USB port from powering up. Repeat the steps above, or log in to the web admin panel to check the Tethering connection status.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. Plug a cellular USB modem into the Slate 7 Pro's USB port. This is useful for sharing internet from a USB modem to all connected devices.
    2. Once successfully connected to the internet, the Cellular section on the touchscreen homepage will turn blue (active). You can either tap Cellular on the touchscreen homepage or log in to the web admin panel to check the connection details.

---

Below is an overview of the features in the Slate 7 Pro web Admin Panel.

## Wireless 

The Wireless page allows you to configure settings for the 6GHz, 5 GHz and 2.4 GHz Wi-Fi networks, including enabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling randomized BSSID, selecting Wi-Fi security mode and password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel. 
    
In addition, Slate 7 Pro supports MLO Wi-Fi, i.e. Multi-Link Operation, combining multiple wireless networks simultaneously to achieve higher bandwidth and more reliable connections.

To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

## Clients

The Clients page displays information about connected devices. For each client, it shows the name, IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud Services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} provides an easy and simple way to remotely access and manage GL.iNet routers. 
    
    To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp is an advanced networking feature integrated into GL.iNet routers. It enables seamless remote access to your home network without registration or login. Using the AmneziaWG protocol with built-in traffic obfuscation, it keeps your connection stable and secure, making it ideal for reliable remote access wherever you go. Users can set up an AstroWarp network directly through the GL.iNet router admin panel. Simply pair your routers using an access code and you can securely connect your travel router to your home network in seconds.
    
    To set up AstroWarp, refer to [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Slate 7 Pro supports OpenVPN and WireGuard protocols. 

=== "OpenVPN" 
    
    Slate 7 Pro (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 Pro (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently. 
    
    To set up LAN, refer to [Lan](../../interface_guide/lan.md). 

=== "Guest Network"

    It allows you to set a subnet within the IPv4 private address ranges 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8, specify the gateway and netmask IP addresses, and configure security settings like AP isolation for the guest network.

    To set up guest network, refer to [Guest Network](../../interface_guide/guest_network.md). 

---

=== "DNS"

    The DNS page allows you to set custom DNS servers, enable DNS rebinding attack protection and override DNS settings of all clients, allow custom DNS to override VPN DNS, and configure the DNS server settings mode to automatic or manually specify DNS servers from the Ethernet connection.

    To set up DNS, refer to [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    The Ethernet Port page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiate the network port rate.

    To manage Ethernet ports, refer to [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway extends the functionality of your main router, including AdGuard Home, encrypted DNS, and VPN client. 
    
    To set up drop-in gateway, refer to these links:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration can reduce CPU load and speeds up traffic packet forwarding.
    
    To set up network acceleration, refer to [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) is a core capability of intelligent network management. It can overcome the limitation of traditional routers (which only identify source or destination addresses), analyze data packet payloads in depth, and accurately identify user-accessed applications and websites through feature library comparison, enabling refined traffic classification and control. 
    
    Integrated with [Netify](https://www.netify.ai/){target="_blank"}, GL.iNet DPI feature adopts a lightweight embedded plug-in for efficient deployment. With Netify online-updated signature database, it enables reliable management, making network control more accurate and efficient.

    Please refer to [DPI Engine](../../interface_guide/dpi_engine.md) for detailed instructions.

=== "Data Statistics"

    Data Statistics offers an intelligent traffic insight dashboard that categorizes and visualizes network usage by applications, helping you monitor real-time and historical traffic for better network awareness and control.

    Please refer to [Data Statistics](../../interface_guide/data_statistics.md) for detailed instructions.

=== "Content Filter"

    Content Filter provides smart online safety powered by DPI-based classification, automatically blocking harmful or malicious websites to keep your network clean and secure.

    Please refer to [Content Filter](../../interface_guide/content_filter.md) for detailed instructions.

---

=== "Parental Control"

    Parental Control is designed to help you manage and control your children's devices. It includes limiting their screen time and restricting their access to certain content.

    To set up parental control, refer to [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) optimizes bandwidth allocation by prioritizing critical activities (e.g., video calls, gaming) during network congestion, reducing latency and improving overall network performance. Note that this applies to local client traffic and VPN Client tunnel traffic, but not to traffic received when the router functions as a VPN Server.

    Please refer to [QoS](../../interface_guide/qos.md) for detailed instructions.

=== "SQM"

    SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls.

    Please refer to [SQM](../../interface_guide/sqm.md) for detailed instructions.

## Security

=== "Port Forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. 
    
    To set up port forwarding, refer to [Port Forwarding](../../interface_guide/port_forwarding.md). 

=== "Management Control"

    Management Control allows you to configure various security settings to protect your network and router from unauthorized access. This page includes the following options:

    * Local Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.
    * Open Ports on Router: Control which ports are open on the router, limiting potential vulnerabilities and unauthorized access.

    These settings help you maintain a secure network environment, safeguarding both your router and connected devices.

    Please refer to [Security](../../interface_guide/security.md) for detailed instructions.

=== "NAT Mode"

    NAT Mode page allows you to enable or disable Full Cone NAT and SIP ALG (Application Layer Gateway) functionality.

    To set up NAT settings, refer to [NAT Mode](../../interface_guide/nat_settings.md).

## Applications


=== "Plug-ins"

    A plug-in is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. 
    
    To set up Dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    To set up network storage, refer to [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    To set up AdGuard Home, refer to [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities. 
    
    * [How to set up Tor](../../interface_guide/tor.md)

## System

=== "Overview"

    The Overview page provides a comprehensive snapshot of your router's current status and performance metrics. On this page, you can view:

    * CPU Average Load: Monitor the average load on your router's CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    * Flash Usage: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * Device Info: Access detailed information about your router's system, including uptime, hostname, model, architecture, OpenWrt version, kernel version, device ID, device MAC and device S/N.
    * External Storage: Check the status of any external storage devices connected to the router, such as USB drives or TF cards.
    
    These features provide essential insights and controls, helping you to effectively manage and monitor your router's operation.

    Please refer to [Overview](../../interface_guide/system_overview.md) for detailed instructions.

=== "Admin Password"

    The Admin Password page enables you to set or change the password for the router's administrative interface to ensure only authorized users can modify settings.

    For security reasons, we recommend that you turn on **Prevent Weak Password**.

    When **Prevent Weak Password** is turned on, the requirements for new passwords are as follows.

    * 5 characters and maximum 63 characters.
    * Letters (case senstive), numbers and symbols `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` are allowed.
    * At least two of uppercase letters, lowercase letters, numbers, and symbols are required.

    Please refer to [Admin Password](../../interface_guide/admin_password.md) for detailed instructions.

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options for upgrading:

    * Firmware Online Upgrade: Automatically check for and install the latest firmware version directly from the manufacturer's server, simplifying the update process.
    * Firmware Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.

    These options allow you to keep your router up-to-date with the latest improvements and fixes.

    Please refer to [Upgrade](../../interface_guide/upgrade.md) for detailed instructions.

---

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to automate various router functions based on a predefined schedule, enhancing convenience and efficiency. Key features on this page include:

    * LCD Display Schedule: Set a schedule to automatically turn the router's LCD display on or off, reducing light pollution during specific times.
    * Schedule Reboot: Configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.
    * Wi-Fi Status Schedule: Set a schedule to control the 6GHz / 5GHz / 2.4GHz / MLO Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    Please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) for detailed instructions.
    
=== "Display Management"

    The Display Management page offers you a full-range of functions to manage the touchscreen display and related settings.

    ‒ Wallpaper: Customize the wallpaper and wake display style.
    ‒ Brightness: Adjust the touchscreen brightness. Use the slider or enter a specific percentage to fit different lighting conditions.
    ‒ Auto Lock: Set the time delay for the screen to auto-lock when there is no activity. The range is 1 minute to 30 minutes.
    ‒ Screen Always On: Toggle this option to decide if the touchscreen stays on continuously or turns off after inactivity.
    ‒ Enable Screen Passcode: Set a passcode for the touchscreen for an extra layer of security.

    Please refer to [Display Management](../../interface_guide/display_management.md) for detailed instructions.

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    Please refer to [Time Zone](../../interface_guide/time_zone.md) for detailed instructions.

---

=== "Toggle Button Settings"

    The Toggle Button Settings page allows you to configure the physical toggle button on your router, enabling you to assign specific functions to the button for quick access and control. This feature provides convenient shortcuts for common tasks and settings, enhancing the user experience and simplifying router management.

    Please refer to [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) for detailed instructions.

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    Please refer to [Reset Firmware](../../interface_guide/reset_firmware.md) for detailed instructions.

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    Please refer to [Log](../../interface_guide/log.md) for detailed instructions.

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    Please refer to [Advanced Settings](../../interface_guide/advanced_settings.md) for detailed instructions.
