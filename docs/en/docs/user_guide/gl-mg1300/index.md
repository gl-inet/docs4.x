# Mango 2 (GL-MG1300) User Guide

## Product overview

Mango 2 (GL-MG1300) is GL.iNet's first dual-band Wi‑Fi 5 mini travel router, featuring an ultra‑thin and portable design. It delivers theoretical dual-band speeds of 400 Mbps (2.4 GHz) and 866 Mbps (5 GHz), with a 2×2 MIMO configuration. Additionally, it comes pre-installed with OpenVPN and WireGuard, supports  30+ VPN services and automatically encrypts all network traffic, and enables remote management via GoodCloud — perfectly balancing performance, practicality, and security.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.png){class="glboxshadow"}

## Package contents

- 1 x Mango 2 (GL-MG1300)
- 1 x User manual
- 1 x Power cable
- 1 x Thank you card

## How to set up Mango 2

To set up Mango 2, you will use one of the four supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. Follow the steps below. 

### 1. Power on

Plug the USB Type-C power cable into the router's power port, then connect the other end to a 5V/2A power adapter (not included) and plug it into a power outlet. 

### 2. Connect device

Connect a device (e.g., computer, laptop or smartphone) to the router using Wi-Fi or Ethernet.

- Ethernet

    Connect your device to the router's LAN port using an Ethernet cable. 

- Wi-Fi

    On your device, go to Settings -> WLAN, locate your router's Wi-Fi network name in the available networks list and enter the password. You can find the default network name and password printed on the router's bottom label.

### 3. Log in to web Admin Panel

Open a web browser, enter `192.168.8.1` in the address bar and log in. Choose your language and set your admin password, then click **Apply**. 

Please note that if you change the Wi‑Fi information, you will need to reconnect your device to the router's Wi‑Fi using the updated credentials.

### 4. Internet setup

**Note:** The following instructions apply to users configuring the router via the GL.iNet Web Admin Panel. If you prefer using the GL.iNet app, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions.

Configure your Mango 2 using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Connect the Mango 2's WAN port to an upstream device (e.g., a modem) via an ethernet cable. 
    
    Once successfully connected to the internet, a green dot will appear in the Ethernet section on the INTERNET page.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. On the INTERNET page of the web Admin Panel, locate the Repeater section and click **Connect**.
    2. Select a Wi-Fi network from the available networks. 
    3. Enter the password, then click **Apply**.
    
    Once successfully connected to the internet, a green dot will appear in the Repeater section on the INTERNET page.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Connect your mobile device (e.g., smartphone or USB dongle) to the router's USB port using a USB cable. 
    2. On your mobile device, go to Settings and enable **USB Tethering** or **Personal Hotspot**. For iPhone, tap **Trust This Device** if prompted. 
    3. On the INTERNET page of the web Admin Panel, click **Connect** in the Tethering section. 

    Once successfully connected to the internet, a green dot will appear in the Tethering section on the INTERNET page.

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "Cellular"

    Plug a cellular USB modem into the Mango 2's USB port. This is useful for sharing internet from a USB modem to all connected devices.

    Once successfully connected to the internet, a green dot will appear in the Cellular section on the INTERNET page.
   
    Please refer to [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) for detailed instructions.

---

Below is an overview of the features in the Mango 2 web Admin Panel.

## Wireless

The Wireless page allows you to configure settings for both the 5 GHz and 2.4 GHz Wi-Fi networks, including enabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling randomized BSSID, selecting Wi-Fi security mode and password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel.

To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

## AstroNode

AstroNode allows connection to your home network, with the Main Router designated as the exit node for all traffic. You can join an existing AstroMesh network to securely access your home network and its resources from any remote location.

## Clients

The Clients page displays information about connected devices. For each client, it shows the name, IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud services

=== "GL.iNet Account"

    The GL.iNet Account allows you to connect and manage your devices and cloud services. You can access both GoodCloud and the glinet App seamlessly, ensuring a secure and improved experience. This provides you a more convenient way to manage your network from anywhere, at any time.

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} provides an easy and simple way to remotely access and manage GL.iNet routers. 

=== "AstroLink"

    AstroLink is an advanced networking platform designed to provide seamless remote networking and remote device management. Built specifically for GL.iNet router integration, AstroLink supports comprehensive device management across entire networks, enabling both upper and lower device control. With a focus on network-wide management and future support for hardware-level control, AstroLink offers a more robust and dependable solution for managing devices and maintaining secure, stable networks. 

## VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Mango 2 supports OpenVPN and WireGuard.

=== "OpenVPN" 
    
    Mango 2 (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Mango 2 (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](../../interface_guide/multi-wan.md). 


=== "Subnet"
    
    Subnet centralizes management of LAN, Guest Network, IoT Network, and custom VLAN Networks, allowing you to create and manage multiple subnets to isolate different types of devices or traffic.

    To set up subnet, refer to [Subnet](../../interface_guide/subnet.md). 

=== "Ethernet Port"

    The Ethernet Port page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiate the network port rate.

---

=== "DNS"

    The DNS page allows you to set custom DNS servers, enable DNS rebinding attack protection and override DNS settings of all clients, allow custom DNS to override VPN DNS, and configure the DNS server settings mode to automatic or manually specify DNS servers from the Ethernet connection.

    To set up DNS, refer to [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Network Mode page allows you to configure the operational role of the router to meet different network deployment needs. You can select from various modes tailored to scenarios ranging from home Wi-Fi coverage to enterprise-level multi-link networking, with each mode enabling or disabling specific router features to optimize performance.

    To set up Network Mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "Network Acceleration"

    Network acceleration can reduce CPU load and speeds up traffic packet forwarding.
    
    To set up network acceleration, refer to [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "Parental Control"

    Parental Control is designed to help you manage and control your children's devices. It includes limiting their screen time and restricting their access to certain content.

    To set up parental control, refer to [Parental Control](../../interface_guide/parental_control.md).

## Security

=== "Port Forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. 
    
    To set up port forwarding, refer to [Port Forwarding](../../interface_guide/port_forwarding.md). 

=== "Admin Access"
    
    Admin Access enables you to configure a range of security settings designed to protect your network and router from unauthorized access.

    To set up admin access, refer to [Admin Access](../../interface_guide/admin_access.md). 

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

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

## System

=== "Overview"

    The Overview page provides a comprehensive snapshot of your router's current status and performance metrics. On this page, you can view:

    * CPU Average Load: Monitor the average load on your router's CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    * Flash: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * Device Info: Access detailed information about your router's system, including uptime, hostname, model, architecture, OpenWrt version, kernel version, device ID, device MAC and device S/N.
    * External Storage: Check the status of any external storage devices connected to the router, such as USB drives or TF cards.
    
    These features provide essential insights and controls, helping you to effectively manage and monitor your router's operation.

    Please refer to [Overview](../../interface_guide/system_overview.md) for detailed instructions.

=== "Admin Password"

    The Admin Password page allows you to set or change the password for the router's administrative interface.

    The admin password must meet the following requirements:

    * Minimum 10 characters and maximum 63 characters.
    * Letters (case senstive), numbers and symbols `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` are allowed.
    * At least two of uppercase letters, lowercase letters, numbers, and symbols are required.

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
    * Wi-Fi Status Schedule: Set a schedule to control the 5GHz / 2.4GHz / MLO Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    Please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) for detailed instructions.

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    Please refer to [Time Zone](../../interface_guide/time_zone.md) for detailed instructions.

=== "Toggle Button Settings"

    The Toggle Button Settings page allows you to configure the physical toggle button on your router, enabling you to assign specific functions to the button for quick access and control. This feature provides convenient shortcuts for common tasks and settings, enhancing the user experience and simplifying router management.

    Please refer to [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) for detailed instructions.

---

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

## Regulatory Statements

This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation,Science and Economic Development Canada's licence-exempt RSS(s). Operation is subject to the following two conditions:  
(1) This device may not cause interference.  
(2) This device must accept any interference, including interference that may cause undesired operation of the device.

L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence.  
L'exploitation est autorisée aux deux conditions suivantes:  
(1) L'appareil ne doit pas produire de brouillage;  
(2) L'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement. 

This equipment complies with IC Rss-102 radiation exposure limits set forth for an uncontrolled environment.  
This equipment should be installed and operated with minimum  distance 20cm between the radiator and your body.

Cet équipement est conforme aux limites d'exposition aux radiations IC CNR-102 établies pour un environnement non contrôlé.  
Cet équipement doit être installé et utilisé avec une distance minimale de 20 cm entre le radiateur et votre corps.

---

The user manual for LE-LAN devices shall contain instructions related to the restrictions mentioned in the above sections, namely that:  
i. the device for operation in the band 5150-5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems;  
i. le dispositif utilisé dans la bande 5150-5250 MHz est réservé à une utilisation en intérieur afin de réduire le risque de brouillage préjudiciable aux systèmes mobiles par satellite dans le même canal;  

The functions of Wireless Access Systems including Radio Local Area Networks(WAS/R-LANs) within the band 5150-5350 MHz for this device are restricted to indoor use only within all European Union countries.

---

**Declaration of conformity**

Hereby, GL TECHNOLOGIES (HONG KONG) LIMITED declares that the radio equipment type [Dual-band Mini Travel Router, GL-MG1300] is in compliance with the essential requirements and other relevant provisions of Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.

FOR EU:  
Maximum output power  
CE: ≤20dBm EIRP(2.412GHz-2.472GHz); ≤23dBm EIRP(5.15GHz~5.35GHz); s30dBm EIRP(5.47GHz~5.725GHz); ≤13.98dBm(5.725GHz~5.85GHz)
