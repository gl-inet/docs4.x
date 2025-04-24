# Puli AX (GL-XE3000) User Guide

All of GL.iNet's devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup.md/).

## How to set up Puli AX

To set up Puli AX, you will use one of the four supported internet connection methods: Cellular (SIM cards), Ethernet, Repeater, and Tethering. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Puli AX and other router models.)</small>

!!! note "Before you start, follow these steps (if connecting via the cellular method):"

    To connect to the internet via the cellular method, you will need at least one nano SIM card. Once you have the nano SIM card(s) ready, follow these steps:
    
    1. Activate your SIM card(s), if required by the SIM card carrier.
    2. Make sure you router is powered off.
    3. Insert the SIM card(s) into the SIM card slots. (**Note:** Only one SIM card is active at each time. The other SIM card functions only as a backup.)

### 1. Power on the Puli AX

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Connect your device to the Puli AX

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

### 3. Connect the Puli AX to the internet 

**Note:** The following instructions were written for those using the router web Admin Panel to connect the router to the internet. If you want to use the GL.iNet app instead of the web Admin Panel, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

#### 1. Sign in to the router web Admin Panel 

In a web browser's address bar, enter `192.168.8.1` and sign in.  Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Cellular"
    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_cellular.png){class="glboxshadow"}

    There are two ways to connect cellular connectivity to your router:

    **Option 1: Cellular-Enabled USB Modem**  

    * Insert a cellular-enabled USB modem into the router’s USB port to share internet access with all connected devices. This method is ideal for using an external modem to provide internet connectivity. [Click here to learn how to connect via USB modem.](../../interface_guide/internet_cellular.md)  

    **Option 2: Physical SIM Card**  

    * The router supports **Dual SIM, Single Standby**, allowing you to insert two SIM cards for internet access. However, only one SIM card can be active at a time, and you can manually switch between them.  
    * Additionally, this router supports **physical eSIM**. Follow our step-by-step guide to set up your eSIM:  [How to Set Up the eSIM Physical Card with GL.iNet Routers.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_esim/)


=== "Ethernet"
    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_ethernet.png){class="glboxshadow"}
    
    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a green dot appears next to "Ethernet."

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_repeater.png){class="glboxshadow"}

    1. On the main screen of the web Admin Panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a green dot appears next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/internet/xe3000_tethering.png){class="glboxshadow"}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the web Admin Panel, click **Connect** in the "Tethering" section.  
    
    If you are connected to the internet successfully, a green dot appears next to "Tethering".

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

**Note:** If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, you will have to set up more than one internet connection methods. 

---

## How to set up a VPN

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Puli AX (and other GL.iNet routers) support OpenVPN, WireGuard, and Tor. 


=== "OpenVPN" 

    Puli AX (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:
    
    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Puli AX (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities. 
    
    * [How to set up Tor](../../interface_guide/tor.md).

## More features and settings

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 
    
    To set up multi-WAN, Refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "Priority and Load Balancing"

    Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time.

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently. 
    
    To set up LAN, refer to [Lan Tutorial](../../interface_guide/lan.md). 


=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
    To set up drop-in gateway, refer to [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md). 

---

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPV6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).
  

=== "MAC Address"

    A MAC address, or Media Access Control address, is a unique identifier assigned to network interfaces for communications on a physical network. It is typically expressed as a 12-digit hexadecimal number and is used to ensure that data packets are sent to the correct device on a local area network (LAN). 
    
    To set up MAC address, refer to [Mac Address](../../interface_guide/network_mode.md).
    
=== "Network Acceleration"

    Hardware acceleration refers to the use of specialized hardware components to perform specific tasks more efficiently than general-purpose CPUs. 
    
    To set up network acceleration to this [Network Acceleration](../../interface_guide/network_acceleration.md) tutorial.
--- 

=== "Plug-ins"

    A plugin is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. 
    
    To set up dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage GL.iNet routers. 
    
    To set up goodcloud, refer to [GoodCloud](../../interface_guide/cloud.md).

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    To set up network storage, refer to [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home is a network-wide ad and tracker blocking solution that acts as a DNS server to filter unwanted content across all devices connected to a home network. 
    
    To set up adguard home, refer to [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content.
    
    To set up parental controls, refer to [Parental controls](../../interface_guide/parental_control.md). 

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](https://docs.gl-inet.com/router/en/4/interface_guide/tailscale/). 

=== "eSIM"

    This router supports eSIM functionality. To enable the feature, ensure you are using [firmware version 4.4.13](https://dl.gl-inet.com/release/router/release/xe3000/4.4.13) or later.  
    
    To learn how to set up and manage eSIM on your device, please refer to [this tutorial](../../tutorials/how_to_set_up_esim_physical_card_with_glinet_routers.md).
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up zerotier, refer to [ZeroTier](../../interface_guide/zerotier.md).


=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

## System settings

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

* To upgrade the router's firmway, please visit the [**Upgrade**](../../interface_guide/upgrade.md) tutorial.
* To learn more about managing your device clients, please visit the [**Clients**](../../interface_guide/clients.md) tutorial.
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

Puli AX (GL-XE3000) is the ultimate Wi-Fi 6 5G Cellular Router that takes your internet speed to the next level! With a powerful built-in 6400mAh/7.4V/47.4Wh battery, you can now enjoy uninterrupted internet connectivity for even longer periods. Experience lightning-fast Wi-Fi speeds of up to 574Mbps (2.4GHz) and 2402Mbps (5GHz), with a combined maximum Wi-Fi speed of 3000Mbps. It is equipped with a 5G NR cellular connection, ensuring uninterrupted internet connectivity, even in the event of an ethernet failure.

![xe3000_interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/hardware_info/xe3000_interface.jpg){class="glboxshadow"}

---

### Package contents

Please note that the adapter within the package depends on your shipping country.

Your router package includes:

- 1 x User manual
- 1 x Puli AX (GL-XE3000)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Converter (Selected plug type)

![xe3000_unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe3000/first_time_setup/xe3000_unboxing.jpg){class="glboxshadow"}

---

### Specification

[GL-XE3000 specification](https://www.gl-inet.com/products/gl-xe3000/#specs){target="_blank"}

[LED Indication](../../faq/led.md#gl-xe3000)




