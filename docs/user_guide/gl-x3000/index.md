# Spitz AX (GL-X3000) User Guide

## Product overview

Spitz AX (GL-X3000) is a dual-SIM Wi-Fi 6 cellular gateway designed to provide fast, reliable connections especially in remote areas and during road trips. It offers four internet access methods: Cellular (SIM cards), ethernet, repeater, and tethering. It supports multi-WAN (failover and load-balancing), VPN (OpenVPN and Wireguard), parental controls, AdGuard Home, port forwarding, Tailscale, and more. 

![x3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/hardware_info/gl-x3000_interface.jpg){class="glboxshadow"}

## Package contents

Please note that the adapter within the package depends on your shipping country.

The package includes:

- 1 x Spitz AX (GL-X3000)
- 1 x Power adapter (US+EU+UK+AU plugs)
- 1 x Ethernet cable
- 1 x User manual
- 1 x Wall mount kit
- 1 x Thank you card

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/first_time_setup/x3000_unboxing.jpg){class="glboxshadow"}

## LED indicators 

| Device Status                          | Power                  | Internet               | 2.4GHz                 | 5GHz                   | Cellular               | 
| -------------------------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| Internet connected (Cellular active)   | Green On               | Green On               | Green On               | Green On               | Green On               |
| Internet connected (Cellular inactive) | Green On               | Green On               | Green On               | Green On               | Off                    |
| No Internet connection                 | Green On               | Off                    | Green On               | Green On               | Off                    |
| Firmware updating                      | Green On               | Flashing every 0.5s    | Flashing every 0.5s    | Flashing every 0.5s    | Green On               | 
| Network reset (press reset < 3s)       | Flashing every 1s      | Green On               | Green On               | Green On               | Green On               |
| Factory reset (press reset for 10s)    | Flashing every 0.25s   | Green On               | Green On               | Green On               | Green On               | 

**Tips**: When connected to the Internet, a flashing 2.4GHz or 5GHz LED means that Wi-Fi devices are connected and actively transmitting data.

## Specifications

Refer to [GL-X3000 specifications](https://www.gl-inet.com/products/gl-x3000/#specs){target="_blank"}.

## How to set up Spitz AX

To set up Spitz AX, you will use one of the four supported internet connection methods: Cellular, Ethernet, Repeater, and Tethering. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/64C7dqHG2EI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!! note "Before you start, follow these steps (if connecting via cellular)"

    At least one nano SIM card is required to connect to the internet via the cellular method. Once you have the nano SIM card(s) ready, follow these steps:
    
    1. Activate your SIM card(s) if required by the SIM card carrier.
    2. Power off your router.
    3. Insert the SIM card(s) into the SIM card slots. (**Note:** Only one SIM card is active at one time. The other SIM card functions only as a backup.)

### 1. Power on Spitz AX

Put the two-piece power adapter together. Connect it to your router and plug it into an outlet. It will start up automatically.

### 2. Connect to Spitz AX

Connect a device (e.g., computer, laptop or smartphone) to the router via Wi-Fi or Ethernet.

- Ethernet

    Connect your device to the router's LAN port using an Ethernet cable. 

- Wi-Fi

    On your device, go to Settings -> WLAN, locate your router's Wi-Fi network name in the available networks list and enter the password. You can find the default network name and password printed on your router's label.

### 3. Log in to the WebGUI

Open a web browser, enter `192.168.8.1` in the address bar and log in. Choose your language and set your admin password, then click **Apply**. 

When confirming the Wi‑Fi details, please note that if you change the Wi‑Fi information, you will need to reconnect your device to the router's Wi‑Fi using the updated credentials.

### 4. Connect Spitz AX to the Internet 

**Note:** The following instructions apply to users configuring the router via the GL.iNet Web Admin Panel. If you prefer using the GL.iNet app, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

Configure your Spitz AX using one of the supported internet connection methods: Cellular, Ethernet, Repeater, and Tethering. If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, please set up more than one internet connection.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_cellular.jpg){class="glboxshadow"}

    If you have already inserted the SIM card into your router, the internet should be connected automatically. (You should see the name of your SIM carrier and a green dot appear in the Cellular section.) 
    
    If not, click the **Auto Setup** option if it appears. 
    
    Please refer to [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models) for detailed instructions.

    Learn how to use the eSIM physical card on GL.iNet router [here](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

    If you encounter any issues, refer to the [Cellular Network Troubleshooting Guide](../../faq/cellular_network_troubleshooting_guide.md). 

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_ethernet.jpg){class="glboxshadow"}
    
    Connect an ethernet cable between your router's WAN port and an upstream device such as a modem. 
    
    Once successfully connected to the internet, a green dot will appear in the Ethernet section on the INTERNET page.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_repeater.jpg){class="glboxshadow"}

    1. On the INTERNET page of the web Admin Panel, locate the Repeater section and click **Connect**.
    2. Select a Wi-Fi network from the available networks. 
    3. Enter the password, then click **Apply**.
    
    Once successfully connected to the internet, a green dot will appear in the Repeater section on the INTERNET page.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device (e.g., smartphone or USB dongle) to the router's USB port using a USB cable. 
    2. On your mobile device, go to Settings and enable USB Tethering. 
    3. On the INTERNET page of the web Admin Panel, click **Connect** in the Tethering section. 
    
    Once successfully connected to the internet, a green dot will appear in the Tethering section on the INTERNET page.

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an additional layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Spitz AX (and other GL.iNet routers) supports OpenVPN and WireGuard. Additionally, it supports Tor.

=== "OpenVPN" 

    Spitz AX (and other GL.iNet routers) supports the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Spitz AX (and other GL.iNet routers) supports the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

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

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} service provides an easy and simple way to remotely access and manage GL.iNet routers. 
    
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

=== "Parental Control"

    Parental control is a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content.

    To set up parental control, refer to [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM Management"

    To learn how to set up and manage eSIM on your device, please refer to [this tutorial](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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

=== "Port Management"

    The Port Management page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiate the network port rate.

---

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
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

    * CPU Average Load: Monitor the average load on your router's CPU, helping to assess performance and identify potential bottlenecks.
    * Memory Usage: Check how much of your router's memory is in use, aiding in the management of resources.
    * LED Control: Toggle the router's LED lights on or off, allowing for customization of the device's visual indicators.
    * Flash Usage: View the utilization of the router's flash storage, ensuring there's sufficient space for firmware and configuration data.
    * Device Info: Access detailed information about your router's system, including uptime, hostname, model, architecture, OpenWrt version, kernel version, device ID, device MAC and device S/N.
    * External Storage: Check the status of any external storage devices connected to the router, such as USB drives or TF cards.
    
    These features provide essential insights and controls, helping you to effectively manage and monitor your router's operation.

    Please refer to [Overview](../../interface_guide/system_overview.md) for detailed instructions.

=== "Upgrade"

    The Upgrade page is used to update your router's firmware to the latest version, ensuring enhanced performance, security, and new features. This page offers two options for upgrading:

    * Firmware Online Upgrade: Automatically check for and install the latest firmware version directly from the manufacturer's server, simplifying the update process.
    * Firmware Local Upgrade: Manually upload a firmware file from your computer to update the router, providing control over the upgrade version and timing.
    * Module Online Upgrade: Automatically check for and install the latest 4G/5G module version directly from the manufacturer's server, simplifying the update process.
    * Module Local Upgrade: Manually upload a module file from your computer to update the 4G/5G module.

    These options allow you to keep your router up-to-date with the latest improvements and fixes.

    Please refer to [Upgrade](../../interface_guide/upgrade.md) for detailed instructions.

=== "Scheduled Tasks"

    The Scheduled Tasks page allows you to automate various router functions based on a predefined schedule, enhancing convenience and efficiency. Key features on this page include:

    * LED Display Schedule: Set a schedule to automatically turn the router's LED lights on or off, reducing light pollution during specific times.
    * Schedule Reboot: Configure your router to reboot automatically at specified intervals, helping to maintain optimal performance and stability.
    * 5GHz Wi-Fi Status Schedule: Set a schedule to control the 5GHz Wi-Fi band, allowing for better management of network availability and power consumption.
    * 2.4GHz Wi-Fi Status Schedule: Set a schedule to control the 2.4GHz Wi-Fi band, allowing for better management of network availability and power consumption.
    
    These scheduling options provide you with greater control over your router's operations, ensuring it meets your specific needs and preferences.

    Please refer to [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) for detailed instructions.

---

=== "Time Zone"

    The Time Zone page allows you to set the correct time zone for your router, ensuring that all scheduled tasks, logs, and system events are accurately timestamped according to your local time. This setting is crucial for maintaining precise records and for the proper execution of time-based configurations.

    Please refer to [Time Zone](../../interface_guide/time_zone.md) for detailed instructions.

=== "Log"

    The Log page provides access to various logs that record the router's activities and events, aiding in troubleshooting and performance monitoring. This page includes:

    * System Log: Detailed logs of system-level events and activities.
    * Kernel Log: Logs related to the kernel's operations and events.
    * Crash Log: Records of system crashes and errors, useful for diagnosing critical issues.
    * Cloud Log: Logs of interactions and activities related to GoodCloud services integrated with the router.
    * Nginx Log: Logs from the Nginx web server, if used by the router, detailing web traffic and server operations.
    
    Additionally, the page features an Export Log button, allowing you to export all collected logs for technical support analysis. This function is invaluable for diagnosing complex issues and obtaining professional assistance.

    Please refer to [Log](../../interface_guide/log.md) for detailed instructions.

=== "Security"

    The Security page allows you to configure various security settings to protect your network and router from unauthorized access. This page includes options for:

    * Admin Password: Set or change the password for the router's administrative interface to ensure only authorized users can modify settings.
    * Local Access Control: Manage and restrict access to the router's interface from devices connected to your local network.
    * Remote Access Control: Configure and restrict access to the router's interface from remote locations over the internet, enhancing security against external threats.
    * Open Ports on Router: Control which ports are open on the router, limiting potential vulnerabilities and unauthorized access.

    These settings help you maintain a secure network environment, safeguarding both your router and connected devices.

    Please refer to [Security](../../interface_guide/security.md) for detailed instructions.

---

=== "Reset Firmware"

    The Reset Firmware page allows you to reset your router's current firmware version to its default settings, erasing all custom configurations. This process will restore the router to the default settings of the currently installed firmware version. This can be useful for troubleshooting persistent issues or starting fresh with the current firmware's default configuration.

    Please refer to [Reset Firmware](../../interface_guide/reset_firmware.md) for detailed instructions.

=== "Advanced Settings"

    The Advanced Settings page provides access to advanced configuration options through the OpenWrt LuCI interface, allowing experienced users to fine-tune their router's settings and functionalities beyond the basic interface options. This includes detailed network configurations, firewall settings, and other advanced system customizations.

    Please refer to [Advanced Settings](../../interface_guide/advanced_settings.md) for detailed instructions.
