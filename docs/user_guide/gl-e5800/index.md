# Mudi 7 (GL-E5800) User Guide

## Product overview

Mudi 7 is a portable 5G NR Wi-Fi 7 travel router built for road warriors and business travelers, delivering reliable, private networks to secure data against cyber threats. It features 5G hyper-speed, dual SIM auto-switching (failover), and Wi-Fi 7 (320MHz channels and 4K QAM) for stable, fast connectivity, supporting fast downloads, 4K streaming, lag-free video conferencing even in crowded areas.

Equipped with a touchscreen, Mudi 7 lets you monitor real-time data usage, signal strength and connected devices, or adjust settings via simple swipes. The interface features one-tap network optimization and dynamic cues (e.g., speed, battery) for hassle-free intuitive control.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Package contents

Please note that the adapter within the package depends on your shipping country.

The package includes:

- 1 x Mudi 7 (GL-E5800)
- 1 x Battery Pack
- 1 x 10Gbps USB-C Cable
- 1 x Travel Case
- 1 x User Manual
- 1 x Warranty Card

## How to set up Mudi 7

### 1. Install Nano-SIM card

First, remove the battery cover, then take out Mudi 7's battery.

Second, insert the Nano-SIM card(s). If using only one card, prioritize SIM 1.

Finally, put the battery and the cover back.

![install nano-sim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/install_nano-sim.png){class="glboxshadow"}

### 2. Power on

Press and hold the Power Button for **3 seconds**, or plug in a power adapter.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power_on.png){class="glboxshadow"}

Then follow the on-screen instructions to complete the device initialization, or follow the steps below to proceed.

### 3. Connect to Mudi 7

Connect a device (e.g., computer, laptop or smartphone) to the Mudi 7 via Wi-Fi, an Ethernet cable, or even via a USB cable.

- **Wi-Fi**

    <u>QR code</u>: Use a device to scan the QR code on the screen of Mudi 7. Then click "Join" on your device to connect.

    <u>Manual Connect</u>: On your device, go to Settings -> WLAN, locate the Wi-Fi network name of Mudi 7 in the available networks list, and enter the password to join the network. (You can find the default network name and password printed on the label.)

- **Ethernet**

    Connect your device to the Ethernet port (default LAN) of Mudi 7 via an Ethernet cable. 

- **USB**

    Connect your device to the USB-C port of Mudi 7 via a USB cable. The OTG-enabled USB-C port allows you to access the Mudi 7's WebGUI in the next step.

### 4. Log in to the WebGUI

Open a web browser, enter `192.168.8.1` in the address bar, then access the login page of Mudi 7. Choose your language, set your admin password, then click **Apply**.

### 5. Connect Mudi 7 to the Internet

Configure your Mudi 7 using one of the supported internet connection methods: Cellular, Ethernet, Repeater, Tethering, and USB Ethernet. If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}
    
    Mudi 7 comes with a **built-in eSIM** and **dual Nano‑SIM** slots. You can connect to the Internet by purchasing an eSIM package (no physical SIM card required), or insert your Nano‑SIM cards to access the 5G mobile network.
    
    - eSIM: On the touchscreen, go to **Cellular** -> **Active SIM Card**, enable eSIM, then upload your eSIM profile or purchase it in the eSIM Profile Store. 

    - Nano‑SIM: Remove the back cover of Mudi 7, take out the battery, insert your Nano-SIM card into the slot, then install the battery. 

    Once successfully connected to the internet, the signal bars and cellular status will appear in the top right corner of the touchscreen. You can also check the connection details on the web admin panel.

    Please refer to [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) for detailed instructions.

    !!! note

        1. The built-in eSIM and SIM 2 are mutually exclusive and cannot be activated at the same time. The eSIM is disabled by default. If you enable the eSIM, SIM 2 will not work even if a SIM card is inserted.
        2. Since Mudi 7 comes with a built-in eSIM, a SIMPoYo eSIM physical card will be recognized as a regular SIM card without eSIM functionality on Mudi 7. 

=== "Ethernet"
    
    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Connect Mudi 7's Ethernet port to an upstream network source (e.g., ISP modem, network switch, or Ethernet jack on the wall) via an Ethernet cable. 
    2. On the touchscreen or web admin panel, go to **Network** -> **Ethernet Ports**, set the port role to **WAN**, and click **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Once successfully connected to the internet, an Ethernet port icon will appear in the top right corner of the touchscreen. You can also check the connection details on the web admin panel.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"
    
    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. On the touchscreen or web admin panel, go to **Internet** -> **Repeater** and click **Connect**. Mudi 7 will start scanning for available Wi-Fi networks.
    2. Select the Wi-Fi network you want Mudi 7 to extend. 
    3. Enter the password and click **Apply**.
    4. Once successfully connected to the internet, a Wi-Fi icon will appear in the top right corner of the touchscreen. You can also check the connection details on the web admin panel.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device (e.g., smartphone or USB dongle) to Mudi 7's USB-C port via a USB cable. 
    2. On your mobile device, go to Settings and enable **USB Tethering**. If you use iPhone, tap **Trust This Device** if prompted. 
    3. Mudi 7 will then automatically connect to your device. If it does not connect, repeat the above steps, or log in to the web admin panel and check the Tethering connection on the INTERNET page.
    4. Once successfully connected to the internet, a chain link icon will appear in the top right corner of the touchscreen. You can also check the connection details on the web admin panel.

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 is equipped with an **OTG-enabled** USB-C port. If you want to convert the USB-C port to an Ethernet port for additional network input, simply plug a **separately purchased USB-C-to-Ethernet adapter** into the USB-C port, then you will have one more Ethernet port.

    <small>*USB OTG (On-The-Go) is a USB standard that enables compatible devices like routers to switch between host and peripheral roles, allowing direct data transmission and power interaction without a separate host device.</small>

    1. Connect an upstream network source (e.g., ISP modem, network switch, or Ethernet jack on the wall) to Mudi 7's USB-C port via a USB C-to-Ethernet adapter. 
    2. On the touchscreen or web admin panel, go to **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, set the port role to **WAN**, and click **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 will then automatically connect to your device. If it does not connect, repeat the above steps, or log in to the web admin panel and check the USB Ethernet connection on the INTERNET page.
    3. Once successfully connected to the internet, a USB icon and an Ethernet port icon will appear in the top right corner of the touchscreen. You can also check the connection details on the web admin panel.

## Repair & Reset

You can restore network connectivity or reset Mudi 7 to factory defaults by a physical reset button.

**Note**: Before performing a reset, ensure Mudi 7 has fully booted up. Do NOT press the reset button immediately after power-up, as this may trigger U-Boot failsafe mode.

Remove the back cover, and you will find the reset button as shown below. 

![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

!!! note "Network Repair"

    Press and hold the reset button for **4 seconds**, then release to repair your network. When holding the button, pay attention to the on-screen prompts and operate as instructed.

    This will restart the network interface, while preserving Wi-Fi settings, VPN configurations (disabled), system settings, etc.

    **Note**:

    1. If Wi-Fi has been disabled, a soft reset will restore Wi-Fi to its default enabled state.

    2. A soft reset can also be used to quickly switch the device from non-router mode to router mode.

!!! note "Device Reset"

    Press and hold the reset button for **10 seconds**, then release to perform a hard reset. When holding the button, pay attention to the on-screen prompts and operate as instructed.
    
    This will clear all your settings. Please proceed with caution.

---

Below is an overview of the Mudi 7 WebGUI features.

## Wireless

The Wireless page allows you to configure settings for the 6 GHz, 5 GHz, and 2.4 GHz Wi-Fi networks, including enabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling randomized BSSID, selecting Wi-Fi security mode and password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel. 

To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

**Note**: There are some differences in the wireless settings of the Mudi 7 compared with those of other GL.iNet Wi-Fi 7 routers.

1. Due to chipset hardware constraints, the 5 GHz and 6 GHz Wi-Fi cannot be enabled simultaneously.
2. When Repeater is enabled, the Guest Network will be automatically disabled.
3. As required by regulations, switch Wi-Fi to Outdoor mode when using it outdoors. This may reduce the coverage range. You can switch the Usage Environment (Indoor or Outdoor) at the top of the Wireless page. 

## Clients

The Clients page displays information about connected devices. For each client, it shows the name, IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provides an easy and simple way to remotely access and manage GL.iNet routers. 
    
    To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp is an advanced networking platform designed to provide seamless remote networking and remote device management. Built specifically for GL.iNet router integration, AstroWarp supports comprehensive device management across entire networks, enabling both upper and lower device control. With a focus on network-wide management and future support for hardware-level control, AstroWarp offers a more robust and dependable solution for managing devices and maintaining secure, stable networks. 
    
    To set up AstroWarp, refer to [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Mudi 7 supports OpenVPN and WireGuard. 

=== "OpenVPN" 
    
    Mudi 7 (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Mudi 7 (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., ethernet, repeater, tethering, cellular, and USB ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

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

    The Ethernet Port page allows you to set the Ethernet port role (i.e., using it as WAN/LAN), switch the MAC mode and MAC address for the WAN interface, and display the negotiated port rate.

    Mudi 7 comes with a single Ethernet port, default to LAN. You can switch it to WAN port on the touchscreen or the web admin panel if required.

    To manage Ethernet ports, refer to [Port Management](../../interface_guide/network_port_management.md).

=== "IPv6"

    IPv6, short for Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network mode refers to the configuration that determines how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

    **Note**: Mudi 7 supports Router, Access Point, and Extender mode. It does not support WDS mode.

=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router, including AdGuard Home, encrypted DNS, and VPN client. 
    
    To set up drop-in gateway, refer to these links:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

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

=== "Management Control"

    The Management Control allows you to configure various security settings to protect your network and router from unauthorized access. This page includes the following options:

    * Local Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.
    * Open Ports on Router: Control which ports are open on the router, limiting potential vulnerabilities and unauthorized access.

    These settings help you maintain a secure network environment, safeguarding both your router and connected devices.

    Please refer to [Security](../../interface_guide/security.md) for detailed instructions.

=== "NAT Mode"

    The NAT Mode page allows you to enable or disable Full Cone NAT and SIP ALG functionality.

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

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

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

    For detailed setup instructions and more information, please refer to [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    The Admin Password page enables you to set or change the password for the router's administrative interface to ensure only authorized users can modify settings.

    For security reasons, we recommend that you turn on **Prevent Weak Password**.

    When **Prevent Weak Password** is turned on, the requirements for new passwords are as follows.

    * 5 characters and maximum 63 characters.
    * Letters (case senstive), numbers and symbols `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` are allowed.
    * At least two of uppercase letters, lowercase letters, numbers, and symbols are required.

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options for upgrading:

    * Firmware Online Upgrade: Automatically check for and install the latest firmware version directly from the manufacturer's server, simplifying the update process.
    * Firmware Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.

    These options allow you to keep your router up-to-date with the latest improvements and fixes.

    For detailed setup instructions and more information, please refer to [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.

    For detailed setup instructions and more information, please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

    **Note**: Mudi 7 does not support LED display schedule and Wi-Fi status schedule.

=== "Display Management"

    The Display Management page lets you manage the touchscreen display and its related settings.
    
    - Wallpaper: Customize the wallpaper and wake display style.
    - Brightness: Adjust the touchscreen brightness. Use the slider or enter a specific level (range from 1 to 10) to fit different lighting conditions.
    - Personalised Signature: Add a custom text to the touchscreen to show your unique style or for quick identification.
    - Auto Lock: Set the time delay for the screen to auto-lock when there is no activity. The range is 15 seconds to 5 minutes.
    - Passcode: Set a passcode for the touchscreen for an extra layer of security.

    For detailed setup instructions and more information, please refer to [Display Management](../../interface_guide/display_management.md).

=== "USB & Power"

    The USB & Power page provides comprehensive settings for managing the router's USB functions and power-related configurations.
    
    **USB**

    - USB Protocol Switch: Switch between USB 2.0 and USB 3.1 protocols for the USB port.
    - Dual Role USB Mode: Select the USB working mode from the dropdown menu. You can set it as Device or Host.
    - Power Direction: Choose the power priority for the USB port from the dropdown menu. You can set it as Input Priority or Output Priority.
    - Power Threshold: Set a specific power threshold percentage for the USB port. 
    
    **Power**
    
    - Wi-Fi Idle Timeout: Set the idle duration (range from 10 minutes to 2 hours, or never) after which Wi-Fi will enter standby. 
    - Ethernet Idle Timeout: Set the idle duration (range from 10 minutes to 2 hours, or never) for Ethernet to switch to standby.
    - Power Off Timeout: Set the time delay (range from 1 hour to 12 hours, or never) until the router automatically powers off when idle.
    - Power On with Charger: Toggle this switch to enable/disable the router powering on automatically when connected to a charger.
    - Auto Standby: Toggle this switch to activate/deactivate automatic system standby for power saving.

---

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    For detailed setup instructions and more information, please refer to [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    For detailed setup instructions and more information, please refer to [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    For detailed setup instructions and more information, please refer to [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    For detailed setup instructions and more information, please refer to [Advanced Settings](../../interface_guide/advanced_settings.md).