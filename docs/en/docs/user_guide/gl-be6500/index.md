# Flint 3e (GL-BE6500) User Guide {#flint-3e-gl-be6500-user-guide}

## Product overview {#product-overview}

Flint 3e (GL-BE6500) is a dual-band Wi-Fi 7 desktop router built for home users and small offices. It supports Multi-Link Operation (MLO), allowing compatible devices to use links on both the 2.4 GHz and 5 GHz bands to help mitigate the effects of interference and congestion. Its 4K-QAM modulation offers up to 20% higher theoretical data rates than Wi-Fi 6's 1024-QAM under otherwise identical conditions. The router supports a combined theoretical dual-band rate of up to 6452 Mbps, with 4×4 MIMO and a 160 MHz channel width on the 5 GHz band. Actual speeds depend on client capabilities and network conditions.

Packed with 5× 2.5G Ethernet ports and 1× USB 3.0 port, it supports high-speed wired connectivity and storage expansion. Additionally, it is compatible with 30+ VPN services and delivers powerful VPN performance up to 680Mbps on WireGuard® and OpenVPN-DCO, plus it includes free Bark Parental Control, perfectly balancing performance, practicality and security.

![gl-be6500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/hardware_info/be6500_interface.jpg){class="glboxshadow"}

**Note**: The difference in appearance between Flint 3e and Flint 3 lies in the silk-screen printing: the silk-screen on Flint 3e is blue, while that on Flint 3 is white.

## Package contents {#package-contents}

- 1 x Flint 3e (GL-BE6500)
- 1 x Power adapter
- 1 x Ethernet cable
- 1 x User Manual
- 1 x Thank you card
- 1 x Converter (Based on your shipping country)

Check out Flint 3e's unboxing video below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-E0LtWqshk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## How to set up Flint 3e {#how-to-set-up-flint-3e}

Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/R40QsUFYuUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Power on {#1-power-on}

Put the two-piece power adapter together. Connect it to your router and plug it into an outlet. It will start up automatically.

### 2. Connect device {#2-connect-device}

Connect a device (e.g., computer, laptop or smartphone) to the router using Wi-Fi or Ethernet.

- Ethernet

    Connect your device to the router's LAN port using an ethernet cable. 

- Wi-Fi

    On your device, go to Settings -> WLAN, locate your router's Wi-Fi network name in the available networks list, and enter the password to join the network. You can find the default network name and password printed on the router's label.

### 3. Log in to web Admin Panel {#3-log-in-to-web-admin-panel}

Open a web browser, enter `192.168.8.1` in the address bar and log in. Choose your language and set your admin password, then click **Apply**.

### 4. Internet setup {#4-internet-setup}

**Note:** The following instructions apply to users configuring the router via the GL.iNet Web Admin Panel. If you prefer using the GL.iNet app, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

Configure your Flint 3e using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection.

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_ethernet.jpg){class="glboxshadow"}

    Connect the Flint 3e's WAN port to an upstream device (e.g., a modem) via an ethernet cable. 
    
    Once successfully connected to the internet, a green dot will appear in the Ethernet section on the INTERNET page.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_repeater.jpg){class="glboxshadow"}

    1. On the INTERNET page of the web Admin Panel, locate the Repeater section and click **Connect**.
    2. Select a Wi-Fi network from the available networks. 
    3. Enter the password, then click **Apply**.
    
    Once successfully connected to the internet, a green dot will appear in the Repeater section on the INTERNET page.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device (e.g., smartphone or USB dongle) to the router's USB port using a USB cable. 
    2. On your mobile device, go to Settings and enable USB Tethering. 
    3. On the INTERNET page of the web Admin Panel, click **Connect** in the Tethering section. 
    
    Once the router is successfully connected to the internet, a green dot will appear in the Tethering section on the INTERNET page.

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_cellular.jpg){class="glboxshadow"}

    Plug a cellular USB modem into the Flint 3e's USB port. This is useful for sharing internet from a USB modem to all connected devices.

    Once successfully connected to the internet, a green dot will appear in the Cellular section on the INTERNET page.

    Please refer to [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) for detailed instructions.

---

Below is an overview of the features in the Flint 3e web Admin Panel.

## Wireless {#wireless}

The Wireless page allows you to configure settings for the 5 GHz and 2.4 GHz Wi-Fi networks, including enabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling randomized BSSID, selecting Wi-Fi security mode and password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel. 
    
In addition, Flint 3e supports MLO Wi-Fi, i.e. Multi-Link Operation, combining multiple wireless networks simultaneously to achieve higher bandwidth and more reliable connections.

To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

The Clients page displays information about connected devices. For each client, it shows the name, IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud Services {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} provides an easy and simple way to remotely access and manage GL.iNet routers. 
    
    To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp is an advanced networking platform designed to provide seamless remote networking and remote device management. Built specifically for GL.iNet router integration, AstroWarp supports comprehensive device management across entire networks, enabling both upper and lower device control. With a focus on network-wide management and future support for hardware-level control, AstroWarp offers a more robust and dependable solution for managing devices and maintaining secure, stable networks. 
    
    To set up AstroWarp, refer to [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Flint 3e supports OpenVPN and WireGuard. 

=== "OpenVPN" 
    
    Flint 3e (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Flint 3e (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., ethernet, tethering, and cellular) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently. 
    
    To set up LAN, refer to [LAN](../../interface_guide/lan.md). 

=== "Guest Network"

    It allows you to set a subnet within the IPv4 private address ranges 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8, specify the gateway and netmask IP addresses, and configure security settings like AP isolation for the guest network.

    To set up guest network, refer to [Guest Network](../../interface_guide/guest_network.md). 

---

=== "IoT Network"

    It allows you to create a dedicated Wi-Fi network for IoT devices. Isolated from the primary network, it delivers better compatibility and improved security.

    To set up IoT network, refer to [IoT Network](../../interface_guide/iot_network.md). 

=== "DNS"

    The DNS page allows you to set custom DNS servers, enable DNS rebinding attack protection, override the DNS settings of all clients, and allow custom DNS to override VPN DNS. You can use DNS servers automatically obtained from upstream devices or manually specify custom DNS servers.

    To set up DNS, refer to [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    The Ethernet Port page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiated network port rate.

    To manage Ethernet ports, refer to [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

---

=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router, including AdGuard Home, encrypted DNS, and VPN client. 
    
    To set up drop-in gateway, refer to these links:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration can reduce CPU load and speeds up traffic packet forwarding.
    
    To set up network acceleration, refer to [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control {#flow-control}

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

=== "QoS"

    QoS (Quality of Service) optimizes bandwidth allocation by prioritizing critical activities (e.g., video calls, gaming) during network congestion, reducing latency and improving overall network performance. Note that this applies to local client traffic and VPN Client tunnel traffic, but not to traffic received when the router functions as a VPN Server.

    Please refer to [QoS](../../interface_guide/qos.md) for detailed instructions.

=== "SQM"

    SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls.

    Please refer to [SQM](../../interface_guide/sqm.md) for detailed instructions.

=== "Parental Control"

    Parental Control is designed to help you manage and control your children's devices. It includes limiting their screen time and restricting their access to certain content.

    To set up parental control, refer to [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Security {#security}

=== "Port Forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. 
    
    To set up port forwarding, refer to [Port Forwarding](../../interface_guide/port_forwarding.md). 

=== "ACL"

    ACL, short for Access Control List, lets you create rules to manage network traffic based on connection protocols, device addresses and ports. It controls whether to allow or block network access. If multiple ACL rules conflict, the system applies the one with higher priority.

    Please refer to [ACL](../../interface_guide/acl.md) for details.

=== "Admin Access"

    Admin Access allows you to configure various security settings to protect your network and router from unauthorized access. This page includes the following options:

    * Local Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.
    * Open Ports on Router: Control which ports are open on the router, limiting potential vulnerabilities and unauthorized access.

    Please refer to [Admin Access](../../interface_guide/admin_access.md) for details.

=== "NAT Mode"

    NAT Mode page allows you to enable or disable Full Cone NAT and SIP ALG (Application Layer Gateway) functionality.

    To set up NAT settings, refer to [NAT Mode](../../interface_guide/nat_settings.md).

## Applications {#applications}

=== "Plug-ins"

    A plug-in is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It maps a domain name to your router's dynamic public IP address, so you can access your network remotely without a static IP address. 
    
    To set up Dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    To set up network storage, refer to [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    To set up AdGuard Home, refer to [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    Integrated in Flint 3e, the Bark service can help protect your child's digital world and provide comprehensive online protection. It typically requires a paid subscription. However, as part of our partnership with Bark, GL.iNet offers the Bark Home plan for free on select router models including Flint 3e, providing advanced monitoring and alerts at no extra cost.

    Please refer to [Bark](../../interface_guide/bark.md) for details.

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities. 
    
    Please refer to [Tor](../../interface_guide/tor.md) for details.

## System {#system}

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

    The Admin Password page enables you to manage the password for the router's administrative interface to ensure only authorized users can modify settings.

    Please refer to [Admin Password](../../interface_guide/admin_password.md) for details.

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options for upgrading:

    * Firmware Online Upgrade: Automatically check for the latest firmware version from the manufacturer's server. You can install the latest one if available online.
    * Firmware Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.

    These options allow you to keep your router up-to-date with the latest improvements and fixes.

    Please refer to [Upgrade](../../interface_guide/upgrade.md) for detailed instructions.

---

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to automate various router functions based on a predefined schedule, enhancing convenience and efficiency. Key features on this page include:

    * LED Display Schedule: Set a schedule to automatically turn the router's LED lights on or off, reducing light pollution during specific times.
    * Schedule Reboot: Configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.
    * Wi-Fi Status Schedule: Set a schedule to control the 5GHz / 2.4GHz / MLO Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    Please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) for detailed instructions.

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    Please refer to [Time Zone](../../interface_guide/time_zone.md) for detailed instructions.

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    Please refer to [Reset Firmware](../../interface_guide/reset_firmware.md) for detailed instructions.

---

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

## Regulatory Statements {#regulatory-statements}

**FCC ID: 2AFIW-BE6500**  

1. This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions:   
    
    (1) This device may not cause harmful interference, and  
    (2) This device must accept any interference received, including interference that may cause undesired operation.  

2. Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.  

3. Note: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, and the user is encouraged to try to correct the interference by one or more of the following measures:  
    - Reorient or relocate the receiving antenna.  
    - Increase the separation between the equipment and receiver.  
    - Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.  
    - Consult the dealer or an experienced radio/TV technician for help important announcement.

**FCC Radiation Exposure Statement**  
This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with minimum distance 20cm between the radiator and your body. This transmitter must not be co-located oroperating in conjunction with any other antenna or transmitter.

---

**Canadian Compliance Statement**

This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation, Science and Economic Development Canada's licence-exempt RSS(s).  
Operation is subject to the following two conditions:  
(1) This device may not cause interference.  
(2) This device must accept any interference, including interference that may cause undesired operation of the device.  

L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. 
L'exploitation est autorisée aux deux conditions suivantes:  
(1) L'appareil ne doit pas produire de brouillage;  
(2) L'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.  

This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with minimum distance 20cm between the radiator and your body.  

Cet équipement est conforme aux limites d'exposition aux radiations IC CNR-102 établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec une distance minimale de 20 cm entre le radiateur et votre corps.

---

The user manual for LE-LAN devices shall contain instructions related to the restrictions mentioned in the above sections, namely that:  
i. the device for operation in the band 5150-5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems;  
i. le dispositif utilisé dans la bande 5150-5250 MHz est réservé à une utilisation en intérieur afin de réduire le risque de brouillage préjudiciable aux systèmes mobiles par satellite dans le même canal. 

Hereby, GL TECHNOLOGIES (HONG KONG) LIMITED declares that the radio equipment type [BE6500 Wi-Fi 7 Travel Router, GL-BE6500] is in compliance with the essential requirements and other relevant provisions of Directive 2014/53/EU. The full text of the EU declaration of conformity is available at [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.

Maximum output power:
CE: ≤20dBm EIRP (2.412GHz–2.472GHz); ≤23dBm EIRP (5.15GHz–5.35GHz); ≤30dBm EIRP (5.47GHz–5.725GHz); ≤13.98dBm EIRP (5.725GHz–5.85GHz)
