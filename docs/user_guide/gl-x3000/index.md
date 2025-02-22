# Spitz AX (GL-X3000) User Guide

## How to set up Spitz AX

To set up Spitz AX, you will use one of the four supported internet connection methods: Cellular (SIM cards), Ethernet, Repeater, and Tethering. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Spitz AX and other router models.)</small>

!!! note "Before you start, follow these steps (if connecting via the cellular method):"

    To connect to the internet via the cellular method, you will need at least one nano SIM card. Once you have the nano SIM card(s) ready, follow these steps:
    
    1. Activate your SIM card(s), if required by the SIM card carrier.
    2. Make sure you router is powered off.
    3. Insert the SIM card(s) into the SIM card slots. (**Note:** Only one SIM card is active at each time. The other SIM card functions only as a backup.)

### 1. Power on the Spitz AX

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Connect your device to the Spitz AX

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

### 3. Connect the Spitz AX to the internet 

**Note:** The following instructions were written for those using the router web Admin Panel to connect the router to the internet. If you want to use the GL.iNet app instead of the web Admin Panel, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

#### 1. Sign in to the router web Admin Panel 

In a web browser's address bar, enter `192.168.8.1` and sign in. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_cellular.jpg){class="glboxshadow"}

    If you already inserted the SIM card into your router, you should be connected to the internet automatically. (You should see the name of your SIM carrier and a light blue dot appear next to it.) If not, click the **Auto Setup** option if it appears. 
    
    Learn how to set up the eSIM physical card on your GL.iNet router with our step-by-step instructions here: [How to Set Up the eSIM Physical Card with the GL.iNet Routers?](../../tutorials/how_to_set_up_esim.md)

    For issues using the cellular method, refer to the [Cellular Network Troubleshooting Guide](../../faq/gl-x3000_gl-xe3000_connection_optimization.md). 

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_ethernet.jpg){class="glboxshadow"}
    
    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a light blue dot appears next to "Ethernet."

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_repeater.jpg){class="glboxshadow"}

    1. On the main screen of the web Admin Panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a light blue dot appears next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the web Admin Panel, click **Connect** in the "Tethering" section. 
    
    If you are connected to the internet successfully, a light blue dot appears next to "Tethering."

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

**Note:** If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, you will have to set up more than one internet connection methods. 

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Spitz AX (and other GL.iNet routers) support OpenVPN, WireGuard, and Tailscale. 


=== "OpenVPN" 

    Spitz AX (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Spitz AX (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities. 
    
    * [How to set up Tor](../../interface_guide/tor.md).

---

## Cloud services

=== "GoodCloud"

    Good Cloud refers to a cloud computing service that prioritizes performance, reliability, and security while providing scalable resources for users. 
    
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

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    To set up AdGuard Home, refer to [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content. Spitz AX offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app.

    To set up parental controls, refer to [Parental controls](../../interface_guide/parental_control).

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM Management"

    This router supports eSIM functionality. To learn how to set up and manage eSIM on your device, please refer to [this tutorial](../../tutorials/how_to_set_up_esim.md).

---

## Network settings

=== "Port forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. To set up port forwarding, refer to [Port Forwards](../../interface_guide/port_forwarding.md). 

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently. 
    
    To set up LAN, refer to [Lan Tutorial](../../interface_guide/lan.md). 

=== "Guest Network"

    It allows you to set a subnet within the IPv4 private address ranges 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8, specify the gateway and netmask IP addresses, and configure security settings like AP isolation for the guest network.

    To set up LAN, refer to [Lan Tutorial](../../interface_guide/guest_network.md). 

---

=== "DNS"

    The DNS page allows you to set custom DNS servers, enable DNS rebinding attack protection and override DNS settings of all clients, allow custom DNS to override VPN DNS, and configure the DNS server settings mode to automatic or manually specify DNS servers from the Ethernet connection.

    To set up DNS, refer to [DNS](../../interface_guide/dns.md).

=== "Network Port Management"

    The Network Port Management page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiate the network port rate.

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

---

=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
    To set up drop-in gateway, refer to [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Hardware acceleration refers to the use of specialized hardware components to perform specific tasks more efficiently than general-purpose CPUs. 
    
    To set up network acceleration to this [Network Acceleration](../../interface_guide/network_acceleration.md) tutorial.

=== "NAT Settings"

    The NAT Settings page allows you to enable or disable Full Cone NAT and SIP ALG (Application Layer Gateway) functionality.

    To set up NAT settings, refer to [NAT Settings](../../interface_guide/nat_settings.md).

---

## System settings

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

* To upgrade the router's firmware, please visit the [**Upgrade**](../../interface_guide/firmware_upgrade.md) tutorial.
* To schedule tasks, please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.
* To set timezone, please visit the  [**Time Zone**](../../interface_guide/time_zone.md) tutorial.
* To view the logs, please visit the [**Log**](../../interface_guide/log.md) tutorial.
* To set security, please visit the [**Security**](../../interface_guide/security.md) tutorial.
* To reset firmware, please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.
* To adjust advanced settings, please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.

---

## Product overview

### Product information

Spitz AX (GL-X3000) is a dual-SIM Wi-Fi 6 cellular gateway designed to provide fast, reliable connections especially in remote areas and during road trips. It offers four internet access methods: Cellular (SIM cards), ethernet, repeater, and tethering. It supports multi-WAN (failover and load-balancing), VPN (OpenVPN and Wireguard), parental controls, AdGuard Home, port forwarding, Tailscale, and more. 

### Package contents

Your router package includes:

- 1 x Spitz AX (GL-X3000)
- 1 x Power adapter (US+EU+UK+AU plugs)
- 1 x Ethernet cable
- 1 x User manual
- 1 x Wall mount kit
- 1 x Thank you card

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/first_time_setup/x3000_unboxing.jpg){class="glboxshadow"}

### LED indicators 

| Condition status                                                              | Power                                | Internet                    | 2.4GHz                      | 5GHz                        |Cellular | 
| ----------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | ------- |
| Normal (connected to the internet)                                            | Green                                | Green                       | Green                       | Green                       | Green   |
| Not connected to the internet                                                 | Green                                | Off                         | Green                       | Green                       | Green   |
| Updating firmware                                                             | Green                                | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Green   | 
| Resetting router (hold down "reset" button for > 3s)                          | Blinkng green (every 1s)             | Green                       | Green                       | Green                       | Green   |
| Restoring router to factory settings (hold down "reset" button for 10s)       | Fast blinking green (every 0.25s)    | Green                       | Green                       | Green                       | Green   | 

### Specifications

Refer to [gl-x3000 specifications](https://www.gl-inet.com/products/gl-x3000/#specs){target="_blank"}. 