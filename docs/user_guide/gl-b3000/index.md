# Marble (GL-B3000) User Guide

## Product overview

The Marble (GL-B3000) router is an art of its own, cleverly displayed as a photo frame to house your favorite art piece and elevate your living space. Not just a visual delight to the eye, the Marble (GL-B3000) router delivers top-notch performance by featuring Wi-Fi 6 and supporting VPN capabilities.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Package contents

Please note that the adapter within the package depends on your shipping country.

The package includes:

- 1 x User manual
- 1 x Marble (GL-B3000)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Wall mount kit
- 1 x Power adapter (Selected plug type)
- 1 x Adhesive pad
- 1 x Router stand
- 1 x Photo frame (Optional)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Specifications

Refer to [Specifications](https://www.gl-inet.com/products/gl-b3000/#specs){target="_blank"}. 

## How to set up Marble

All GL.iNet routers have a simple and almost identical setup process. [Click here to learn about the first-time setup](../../faq/first_time_setup.md/).

To set up Marble, you will use one of the two supported internet connection methods: Ethernet and repeater. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Power on the Marble

Put the two-piece power adapter together. Connect it to your router and plug it into an outlet. It will start up automatically.

### 2. Connect your device to the Marble

Connect your computer or mobile device to the router using Wi-Fi or ethernet cable.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, go to Settings -> WLAN, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

### 3. Connect the Marble to the internet 

**Note:** The following instructions apply to users configuring the router via the GL.iNet Web Admin Panel. If you prefer using the GL.iNet app, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions.

#### 1. Log in to the router web admin panel

Launch a web browser, enter `192.168.8.1` in the address bar, and you will enter the GL.iNet Web Admin Panel. Choose a language and set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}
    
    Connect an ethernet cable between your router's WAN port and an upstream device, such as a modem. 
    
    Once the router is successfully connected to the internet, a green dot will appear next to "Ethernet" on the INTERNET page of the Web Admin Panel.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. On the INTERNET page of the web admin panel, locate the "Repeater" section and click **Connect**.
    2. Select a Wi-Fi network from the available networks. 
    3. Enter the network password, then click **Apply**.
    
    Once the router is successfully connected to the internet, a green dot will appear next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

**Note:** If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection methods. 

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an additional layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Marble (and other GL.iNet routers) support OpenVPN and WireGuard. Additionally, it also supports Tor.

=== "OpenVPN" 

    Marble (and other GL.iNet routers) supports the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble (and other GL.iNet routers) supports the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor is a privacy-focused service that allows you to access the internet anonymously. To set up Tor, follow these tutorials:

    * [How to set up Tor](../../interface_guide/tor.md)

---

## Wireless and clients

=== "Wireless"

    The Wireless page allows you to configure settings for both 5 GHz and 2.4 GHz Wi-Fi networks, including enabling/disabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling/disabling randomized BSSID, selecting Wi-Fi security mode, setting Wi-Fi password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel.

    To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    The Clients page displays information about connected devices. For each client, it shows the device name, connection type (i.e., via ethernet or Wi-Fi), IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

    To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} service provides an easy and simple way to remotely access and manage GL.iNet routers. 
    
    To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    This feature is available from firmware v4.7.

    AstroWarp is an advanced networking platform designed to provide seamless remote networking and remote device management. Built specifically for GL.iNet router integration, AstroWarp supports comprehensive device management across entire networks, enabling both upper and lower device control. With a focus on network-wide management and future support for hardware-level control, AstroWarp offers a more robust and dependable solution for managing devices and maintaining secure, stable networks.

## Applications

=== "Plug-ins"

    Plug-ins are add-on features that enhance the functionality of your router. To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. To set up dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

---

=== "AdGuard Home"

    AdGuard Home is a third-party tool that blocks ads and tracking to keep you safe. 
    
    To learn how to enable AdGuard Home, refer to [AdGuard Home](../../interface_guide/adguardhome.md). 

=== "Parental Control"

    Parental control is a group of settings designed to help you manage and control your children's devices. It includes limiting their screen time and restricting their access to certain content. Marble offers two options for parental control: the local version developed by GL.iNet and the integrated version from Bark, a parental control app. 

    To set up parental control, refer to [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"
   
    Tailscale is a VPN service that allows you to access your devices and applications anywhere. To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md). 

=== "ZeroTier"

    ZeroTier is a VPN service that allows you to connect your devices to a virtual network. To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

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

=== "Guest Network"

    The Guest Network page allows you to create and manage a separate network for your guests, providing them with internet access while keeping your main network secure. Key functionalities on this page include:

    * Gateway: Set a specific IP address range for the guest network to distinguish it from your main network.
    * DHCP: Configure the Dynamic Host Configuration Protocol for the guest network, automatically assigning IP addresses to devices that connect to it.

    These features ensure that your guests can enjoy internet access without compromising the security and performance of your primary network.
    
    For detailed setup instructions and more information, please refer to [Guest Network](../../interface_guide/guest_network.md).

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

---

=== "IPv6"

    The IPv6 page enables you to configure IPv6 settings for your network, providing support for the latest internet protocol. On this page, you can enable IPv6 and select from four different modes to suit your network requirements:

    * Native: Obtain an IPv6 address directly from your ISP, allowing for straightforward and efficient native IPv6 connectivity.
    * Passthrough: Allow IPv6 traffic to pass through the router to the devices on your network, effectively bridging the connection without the router handling IPv6 routing itself.
    * NAT6: Utilize Network Address Translation for IPv6 (NAT6) to translate between internal and external IPv6 addresses, similar to how NAT works for IPv4.
    * Static IPv6: Manually configure a static IPv6 address for your router, providing a fixed address for consistent connectivity and easier management of network services.

    These settings help you leverage the benefits of IPv6, including improved address space, enhanced security features, and better performance.

    For detailed setup instructions and more information, please refer to [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    The MAC Address page allows you to view and manage the Media Access Control (MAC) addresses associated with your router. Key features available on this page include:

    * Factory Default: Display the default MAC addresses for the router’s Ethernet and Repeater modes, providing a reference for original hardware settings.
    * Clone: Clone the MAC address of a specific client device. This is particularly useful in scenarios where network access is restricted to certain devices.
    * Manual: Manually specify a custom MAC address for your router. Additionally, you can use the Random button to generate a random MAC address, providing flexibility and enhanced privacy.

    These features enable you to manage your router's MAC addresses effectively, ensuring compatibility and flexibility within various network environments.

    For detailed setup instructions and more information, please refer to [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. To set up Drop-in Gateway, refer to [How to set up Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    The IGMP Snooping page allows you to configure settings that optimize multicast traffic management within your network. IGMP Snooping listens to and extracts information from IGMP protocol packets, establishing and maintaining Layer 2 multicast forwarding tables. This ensures that multicast group data is forwarded only to hosts that have joined the multicast group, preventing unwanted multicast traffic from reaching other hosts.

    These settings help optimize network performance and efficiency, particularly in environments with significant multicast traffic, such as streaming video or online gaming.

    For detailed setup instructions and more information, please refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    The Network Acceleration page allows you to enable features that reduce CPU load and speed up traffic packet forwarding, enhancing overall network performance. However, enabling network acceleration can conflict with certain features.

    For detailed setup instructions and more information, please refer to [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    The NAT Settings page allows you to configure Network Address Translation (NAT) options to optimize specific applications and improve network performance. Key settings available on this page include:

    * Enable Full Cone NAT: Full Cone NAT can be used to reduce game latency, offering a more direct and less restrictive path for network traffic. However, enabling Full Cone NAT may be less secure as it allows external hosts to initiate connections to internal devices more easily.
    * Enable SIP ALG: The Session Initiation Protocol Application Layer Gateway (SIP ALG) can help mitigate issues caused by multiple NATs, which can affect VoIP services. However, in most cases, SIP ALG may not be beneficial and can cause issues such as one-way audio (only one party can hear the other), phones not ringing during a call, phones dropping while connected, and calls going directly to voicemail.

    These settings allow you to tailor your router's NAT behavior to better suit your network's needs, balancing performance improvements with potential security and functionality considerations.

    For detailed setup instructions and more information, please refer to [NAT Settins](../../interface_guide/nat_settings.md).

---

## System settings

=== "Overview"

    The Overview page provides a comprehensive snapshot of your router's current status and performance metrics. On this page, you can view:

    * CPU Average Load: Monitor the average load on your router’s CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * Flash Usage: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * System Info: Access detailed information about your router's system, including firmware version, uptime, and network status.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    
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

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    For detailed setup instructions and more information, please refer to [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    For detailed setup instructions and more information, please refer to [Log](../../interface_guide/log.md).

=== "Security"

    The Security page allows you to configure various security settings to protect your network and router from unauthorized access. This page includes options for:

    * Admin Password: Set or change the password for the router's administrative interface to ensure only authorized users can modify settings.
    * Local Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.

    These settings help you maintain a secure network environment, safeguarding both your router and connected devices.

    For detailed setup instructions and more information, please refer to [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    For detailed setup instructions and more information, please refer to [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    For detailed setup instructions and more information, please refer to [Advanced Settings](../../interface_guide/advanced_settings.md).
