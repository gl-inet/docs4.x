# Beryl AX (GL-MT3000) User Guide

## How to set up Beryl AX

To set up Beryl AX, you will use one of the four supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Beryl AX and other router models.)</small>


### 1. Power on the Beryl AX

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Connect your device to the Beryl AX

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

    The wireless settings lets users manage network security of the primary Wi-Fi and the Guest Wi-Fi, it is accessible by going to **WIRELESS** on the side menu.

### 3. Connect the Beryl AX to the internet 

**Note:** The following instructions were written for those using the router admin panel to connect the router to the internet. If you want to use the GL.iNet app instead of the admin panel, [download the app](https://www.gl-inet.com/app/) and follow the on-screen instructions. 

#### 1. Sign in to the router admin panel 

In a web browser's address bar, enter 192.168.8.1. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Ethernet"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_repeater.png){class="glboxshadow"}

    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a light blue dot appears next to "Ethernet."

    [Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)


=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_repeater.png){class="glboxshadow"}

    1. On the main screen of the admin panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a light blue dot appears next to the Wi-Fi network name.

    [Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_tethering.png){class="glboxshadow"}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the admin panel, click **Connect** in the "Tethering" section. 
    
    If you are connected to the internet successfully, a light blue dot appears next to "Tethering."

    [Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_cellular.png){class="glboxshadow"}

    Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

    [Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

---

**Note:** If you want to use the [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/) feature, you will have to set up more than one internet connection methods. 

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Beryl AX (and other GL.iNet routers) support OpenVPN, WireGuard, and Tailscale. 


=== "OpenVPN" 

    Beryl AX (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [How to set up an OpenVPN server](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"

    Beryl AX (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [How to set up a WireGuard server](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. To set up Tailscale, refer to [Tailscale](https://docs.gl-inet.com/router/en/4/interface_guide/tailscale/). 

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities. To set up Tor, refer to [Tor](../../interface_guide/tor.md).

---

## More features and settings

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 
    
    To set up multi-WAN, Refer to [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

=== "Priority and Load Balancing"

    Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time.

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently.
    
    To set up LAN, Refer to [Lan Tutorial](../../interface_guide/lan.md). 


=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
    To set up drop-in gateway, refer to [How to set up drop-in gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/). 

---

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices.
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPV6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).
  

=== "MAC Address"

    A MAC address, or Media Access Control address, is a unique identifier assigned to network interfaces for communications on a physical network. It is typically expressed as a 12-digit hexadecimal number and is used to ensure that data packets are sent to the correct device on a local area network (LAN). 
    
    To set up MAC address, refer to [MAC Address](../../interface_guide/network_mode.md).
  

=== "Plug-ins"

    A plugin is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. 
    
    To set up dynamic DNS, refer to [Dynamic DNS](https://docs.gl-inet.com/router/en/4/interface_guide/ddns/). 

=== "GoodCloud"

    Good Cloud refers to a cloud computing service that prioritizes performance, reliability, and security while providing scalable resources for users. 
    
    To set up goodcloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    To set up network storage, refer to [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    To set up adguard home, refer to [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content. Spitz AX offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app. 
    
    To set up parental controls, refer to [Parental controls](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control). 

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up zerotier, refer to [**ZeroTier**](../../interface_guide/zerotier.md).

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

## System settings

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

* To upgrade the router's firmway, please visit the [**Upgrade**](../../interface_guide/firmware_upgrade.md) tutorial.
* To learn more about managing your device clients, please visit the [**Clients**](./../interface_guide/clients.md) tutorial.
* To schedule tasks, please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.
* To set admin password, please visit the [**Admin Password**](../../interface_guide/admin_password.md) tutorial.
* To set timezone, please visit the  [**Time Zone**](../../interface_guide/time_zone.md) tutorial.
* To toggle button settings, please visit the [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md) tutorial.
* To view the logs, please visit the [**Log**](../../interface_guide/log.md) tutorial.
* To view security, please visit the [**Security**](../../interface_guide/security.md) tutorial.
* To reset firmware, please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.
* To adjust advanced settings, please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.

---

## Product overview

### Product information

Beryl AX (GL-MT3000) is an AX3000 pocket-sized travel router that uses the Wi-Fi 6 protocol. It is an upgraded version of Beryl (GL-MT1300). It runs on MT7981B 1.3GHz dual-core processor, offering more than double the total Wi-Fi speed. It is designed to support families with heavy Wi-Fi usage, and it's also compactly designed for travel use.

---

### Package contents

Your router package includes:

- 1 x User manual
- 1 x Beryl AX (GL-MT3000)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Warranty card
- 1 x Power adapter (Selected plug type)

![gl-MT3000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/first_time_setup/mt3000_unboxing.jpg){class="glboxshadow"}

Check out Beryl AX's [unboxing video](../../video_library/unboxing_first_set_up.md#gl-mt3000beryl-ax).

---

### Specification

[GL-MT3000 specification](https://www.gl-inet.com/products/gl-mt3000/#specs){target="_blank"}

[LED Indication](../../faq/led.md#gl-mt3000)


---
