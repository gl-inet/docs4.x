# Fortify (GL-MT6000) User Guide

## Product overview

Fortify (GL-MT6000) is a co-branded Wi-Fi 6 router jointly released by GL.iNet and ExpressVPN. Every unit comes with a complimentary one-year ExpressVPN subscription. Users can redeem the subscription and bind their accounts directly on the router's web Admin Panel. Once activated, all traffic passing through the router will leverage ExpressVPN's high-speed network and robust encryption to protect your entire network connection and online privacy.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## How to set up Fortify

### 1. Power on

Put the two-piece power adapter together. Connect it to your Fortify router and plug it into an outlet. It will start up automatically.

### 2. Connect device

Connect a device (e.g., computer, laptop or smartphone) to the router via Wi-Fi or Ethernet.

- Ethernet

    Connect your device to the router's LAN port using an Ethernet cable. 

- Wi-Fi

    On your device, go to Settings -> WLAN, locate your router's Wi-Fi network name in the available networks list, and enter the password to join the network. You can find the default network name and password printed on the router's label.

### 3. Log in to web Admin Panel

Open a web browser, enter `192.168.8.1` in the address bar and log in. Choose your language in the upper right corner, set your admin password, then click **Next**. The password must be 10–63 characters long and contain at least two of the following: uppercase letters, lowercase letters, numbers and special symbols.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Set up your Wi-Fi. Please note that if you change the Wi‑Fi information, you will need to reconnect your device to the router's Wi‑Fi using the updated credentials.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Internet setup

**Note:** The following instructions apply to users configuring the router via the GL.iNet web Admin Panel. If you prefer the [GL.iNet app](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, download it and follow the on-screen prompts.

Configure your Fortify using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Connect an Ethernet cable between your Fortify router's WAN port and an upstream device such as a modem. 
    
    Once successfully connected to the internet, the router LED turns solid white.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. On the web admin panel, go to INTERNET -> Repeater section and click **Connect**.
    2. Select a Wi-Fi from the available networks. 
    3. Enter the password, then click **Apply**.
    
    Once successfully connected to the internet, the router LED turns solid white.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Connect your smartphone to the router's USB port using a USB cable. 
    2. On your smartphone, go to Settings and enable USB Tethering. For iPhone, trust this device and enable Personal Hotspot.
    3. On the web admin panel, go to INTERNET -> Tethering section and click **Connect**. 
    
    Once successfully connected to the internet, the router LED turns solid white.

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Plug a cellular USB modem into the router's USB port. This is useful for sharing internet from a USB modem to all connected devices.

    Once successfully connected to the internet, the router LED turns solid white.

    Please refer to [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) for detailed instructions. 

---

Below is an overview of the features in the Fortify web Admin Panel.

## Wireless

The Wireless page lets you configure Fortify’s Wi-Fi networks, including Main Network, Guest Network and IoT Network. Each network supports both the 2.4 GHz and 5 GHz bands.

To set up Wireless, refer to [Wireless](../../interface_guide/wireless_v4.9.md).

## Clients

The Clients page displays information about connected devices, including device name, connection type, IP and MAC addresses, download and upload speeds, traffic, and provides the ability to block specific client with one click or perform other actions.

Please refer to [Clients](../../interface_guide/clients.md) for details.

## Cloud services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} provides an easy and simple way to remotely access and manage your GL.iNet routers. 
    
    Please refer to [GoodCloud](../../interface_guide/cloud.md) for details.

=== "AstroWarp"

    AstroWarp is a feature built for seamless remote networking on GL.iNet routers. It adopts the AmneziaWG protocol with built-in traffic obfuscation, delivering stable and secure remote access anytime, anywhere.
    
    Please refer to [AstroWarp](../../interface_guide/astrowarp.md) for details.

## VPN 

A VPN (virtual private network) establishes secure, encrypted traffic tunnels between your local device and the VPN server. It adds an extra layer of privacy and security to the VPN client, and enables access to the remote VPN server network.

Fortify integrates with [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, allowing you to activate an ExpressVPN connection in minutes. Every Fortify device comes with a complimentary one-year ExpressVPN subscription. You may redeem the subscription and bind your ExpressVPN account directly on the router’s web admin panel. Once the VPN connection is enabled, all traffic routed through the router will utilize ExpressVPN's high-speed servers and robust encryption to secure your entire network and online privacy.

To redeem free subscription and set up VPN tunnel, refer to [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md).

To set up an OpenVPN server, refer to [OpenVPN Server](../../interface_guide/openvpn_server.md).

To set up a WireGuard server, refer to [WireGuard Server](../../interface_guide/wireguard_server.md).

## Network

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    Please refer to [Multi-WAN](../../interface_guide/multi-wan.md) for details.

=== "LAN"

    A LAN, or Local Area Network, is a network that connects computers and devices within a limited geographic area, such as a home or office. This is the local network your device joins when connected to the main Wi-Fi or via an Ethernet cable. The LAN page covers Basic Settings, DHCP Server Settings, and Address Reservation.
    
    Please refer to [LAN](../../interface_guide/lan.md) for details.

=== "Guest Network"

    The Guest Network page lets you create a dedicated Wi-Fi network for visitors. Isolated from the primary network, it enhances security while providing convenient internet access. You can set a guest subnet within the IPv4 private address ranges `192.168.0.0/16`, `172.16.0.0/12`, or `10.0.0.0/8`, specify the gateway and netmask IP addresses.

    Please refer to [Guest Network](../../interface_guide/guest_network.md) for details.

=== "IoT Network"

    The IoT Network page allows you to create a dedicated Wi-Fi network for IoT devices. Isolated from the primary network, it delivers better compatibility and improved security.
    
    Please refer to [IoT Network](../../interface_guide/iot_network.md) for details.

<br>

=== "DNS"

    The DNS settings on your router control how domain names are translated into IP addresses. This page lets you use the DNS server(s) automatically obtained from upstream devices, or set custom ones, and configure DNS priorities.

    Please refer to [DNS](../../interface_guide/dns.md) for details.

=== "Ethernet Port"

    The Ethernet Port page allows you to manage Ethernet port roles (WAN/LAN) and view port details such as MAC address and negotiated speed.

    Please refer to [Ethernet Port](../../interface_guide/ethernet_port.md) for details.

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    Please refer to [IPV6](../../interface_guide/network_mode.md) for details.

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    Please refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md) for details.

<br>

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
    To set up drop-in gateway, refer to [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

=== "Network Acceleration"

    Network acceleration can reduce CPU load and speeds up traffic packet forwarding.
    
    To set up network acceleration, refer to [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) is a core capability of intelligent network management. It can overcome the limitation of traditional routers (which only identify source or destination addresses), analyze data packet payloads in depth, and accurately identify user-accessed applications and websites through feature library comparison, enabling refined traffic classification and control. 
    
    Integrated with [Netify](https://www.netify.ai/){target="_blank"}, GL.iNet DPI feature adopts a lightweight embedded plug-in for efficient deployment. With Netify online-updated signature database, it enables reliable management, making network control more accurate and efficient.

    Please refer to [DPI Engine](../../interface_guide/dpi_engine.md) for details.

=== "Data Statistics"

    Data Statistics offers an intelligent traffic insight dashboard that categorizes and visualizes network usage by applications, helping you monitor real-time and historical traffic for better network awareness and control.

    Please refer to [Data Statistics](../../interface_guide/data_statistics.md) for details.

=== "Content Filter"

    Content Filter provides smart online safety powered by DPI-based classification, automatically blocking harmful or malicious websites to keep your network clean and secure.

    Please refer to [Content Filter](../../interface_guide/content_filter.md) for details.

<br>

=== "QoS"

    QoS (Quality of Service) optimizes bandwidth allocation by prioritizing critical activities (e.g., video calls, gaming) during network congestion, reducing latency and improving overall network performance. Note that this applies to local client traffic and VPN Client tunnel traffic, but not to traffic received when the router functions as a VPN Server.

    Please refer to [QoS](../../interface_guide/qos.md) for details.

=== "SQM"

    SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls.

    Please refer to [SQM](../../interface_guide/sqm.md) for details.

=== "Parental Control"

    Parental Control is designed to help you manage and control your children's devices. It includes limiting their screen time and restricting their access to certain content.

    Please refer to [Parental Control](../../interface_guide/parental_control_v4.9.md) for details.

## Security

=== "Port forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. 
    
    Please refer to [Port Forwarding](../../interface_guide/port_forwarding.md) for details.

=== "ACL"

    ACL, short for Access Control List, lets you create rules to manage network traffic based on connection protocols, device addresses and ports. It controls whether to allow or block network access. If multiple ACL rules conflict, the system applies the one with higher priority.

    Please refer to [ACL](../../interface_guide/acl.md) for details.

=== "Admin Access"

    Admin Access allows you to configure various security settings to protect your network and router from unauthorized access. This page includes the following options:

    * Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.
    * Open Ports on Router: Control which ports are open on the router, limiting potential vulnerabilities and unauthorized access.

    Please refer to [Admin Access](../../interface_guide/admin_access.md) for details.

=== "NAT Mode"

    NAT Mode page allows you to enable or disable Full Cone NAT and SIP ALG (Application Layer Gateway) functionality.

    Please refer to [NAT Mode](../../interface_guide/nat_settings.md) for details.

## Applications

=== "Plug-ins"

    A plug-in is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    Please refer to [Plug-ins](../../interface_guide/plugins.md) for details.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is useful for users who need a static IP address for accessing a remote network. 
    
    Please refer to [Dynamic DNS](../../interface_guide/ddns.md) for details.

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    Please refer to [Network Storage](../../interface_guide/network_storage.md) for details.

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    Please refer to [AdGuard Home](../../interface_guide/adguardhome.md) for details.

<br>

=== "Bark"

    The [Bark](https://www.bark.us/){target="_blank"} service can help protect your child's digital world and provide comprehensive online protection. It typically requires a paid subscription. However, as part of GL.iNet partnership with Bark, we offers the Bark Home plan for free on Fortify (GL-MT6000), providing advanced monitoring and alerts at no extra cost.

    Please refer to [Bark](../../interface_guide/bark.md) for details.

=== "Tailscale"

    Tailscale is a VPN service that makes the devices and applications you own accessible anywhere in the world, securely and effortlessly. 

    Fortify (GL-MT6000) integrates with Tailscale, allowing you to join the router into a Tailscale virtual network. Once connected, you can access it remotely, including its WAN and LAN resources.
    
    Please refer to [Tailscale](../../interface_guide/tailscale.md) for details.

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    Please refer to [ZeroTier](../../interface_guide/zerotier.md) for details.

=== "Tor"

    Tor (derived from The Onion Router) is a free and open-source software for enabling anonymous communication. It helps users to explore the internet with privacy.

    Please refer to [Tor](../../interface_guide/tor.md) for details.

## System

=== "Overview"

    The Overview page provides a comprehensive snapshot of your router's current status and performance metrics. On this page, you can view:

    * CPU Average Load: Monitor the average load on your router’s CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    * Flash Usage: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * Device Info: Access detailed information about your router's system, including uptime, hostname, model, architecture, OpenWrt version, kernel version, device ID, device MAC and device S/N.
    * External Storage: Check the status of any external storage devices connected to the router, such as USB drives or TF cards.
    
    These features provide essential insights and controls, helping you to effectively manage and monitor your router's operation.

    Please refer to [Overview](../../interface_guide/system_overview.md) for details.

=== "Admin Password"

    The Admin Password page allows you to set or change the password for the router's administrative interface.

    Please refer to [Admin Password](../../interface_guide/admin_password.md) for details.

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options:

    * Firmware Online Upgrade: Automatically check for and install the latest firmware version directly from the manufacturer's server, simplifying the update process.
    * Firmware Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.

    Please refer to [Upgrade](../../interface_guide/upgrade.md) for details.

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to automate various router functions based on a predefined schedule, enhancing convenience and efficiency. Key features on this page include:

    * LED Display Schedule: Set a schedule to automatically turn the router's LED lights on or off, reducing light pollution during specific times.
    * Schedule Reboot: Configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.
    * 5GHz / 2.4GHz Wi-Fi Status Schedule: Set a schedule to control the 5GHz / 2.4GHz Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    Please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) for details.

<br>

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    Please refer to [Time Zone](../../interface_guide/time_zone.md) for details.

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    Please refer to [Reset Firmware](../../interface_guide/reset_firmware.md) for details.

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    Please refer to [Log](../../interface_guide/log.md) for details.

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    Please refer to [Advanced Settings](../../interface_guide/advanced_settings.md) for details.
