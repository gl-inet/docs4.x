# Slate 7 (GL-BE3600) User Guide

## How to set up Slate 7

To set up Slate 7, you will use one of the four supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Spitz Plus and other router models.)</small>

### 1. Power on the Slate 7

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Connect your device to the Slate 7

Connect your computer or mobile device to the router using Wi-Fi or Ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

    The wireless settings lets users manage network security of the primary Wi-Fi and the Guest Wi-Fi, it is accessible by going to **WIRELESS** on the side menu.

### 3. Connect the Slate 7 to the internet 

**Note:** The following instructions were written for those using the router admin panel to connect the router to the internet. If you want to use the GL.iNet app instead of the admin panel, [download the app](https://www.gl-inet.com/app/) and follow the on-screen instructions. 

#### 1. Sign in to the router admin panel 

In a web browser's address bar, enter 192.168.8.1. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class='glboxshadow'}
    
    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, the "Ethernet" icon on the touchscreen will change from white to green.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class='glboxshadow'}

    1. On the main screen of the admin panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, the "Wi-Fi" icon on the touch screen will change from white to green.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class='glboxshadow'}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the admin panel, click **Connect** in the "Tethering" section. 
    
    If you are connected to the internet successfully, the "Tethering" icon on the touch screen will change from white to green.

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class='glboxshadow'}

    Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

    Click here to learn how to connect to the internet via USB modem.
    For issues using the cellular method, refer to the [Cellular Network Troubleshooting Guide](https://docs.gl-inet.com/router/en/4/faq/gl-x3000_gl-xe3000_connection_optimization/). 

**Note:** If you want to use the multi-WAN feature, you will have to set up more than one internet connection methods. 

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Slate 7 (and other GL.iNet routers) support OpenVPN, WireGuard, and Tailscale. 


=== "OpenVPN" 
    Slate 7 (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [How to set up an OpenVPN server](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"
    Slate 7 (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [How to set up a WireGuard server](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

=== "Tailscale"
    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 

    * [How to set up Tailscale](https://docs.gl-inet.com/router/en/4/interface_guide/tailscale/)

---

## More features and settings

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

=== "Priority and Load Balancing"

    Go to Multi-WAN to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time. 

    To set up multi-WAN, refer to [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently.
    
    To set up LAN, Refer to [LAN Tutorial](https://docs.gl-inet.com/router/en/4/interface_guide/lan/)

=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. 
    
    To set up drop-in gateway, refer to [How to set up drop-in gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/). 

---

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices.
    
    To set up Network mode, refer to [Network Mode](https://docs.gl-inet.com/router/en/4/interface_guide/network_mode/). 

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet.
    
    To set up IPv6, refer to [IPv6](https://docs.gl-inet.com/router/en/4/interface_guide/network_mode/)

=== "MAC Address"

    A MAC address, or Media Access Control address, is a unique identifier assigned to network interfaces for communications on a physical network. It is typically expressed as a 12-digit hexadecimal number and is used to ensure that data packets are sent to the correct device on a local area network (LAN).
    
    To set up MAC address, refer to[MAC address](https://docs.gl-inet.com/router/en/4/interface_guide/network_mode/). 

=== "Plug-ins"

    A plugin is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities.
    
    To set up Plug-ins, refer to[Plug-ins](https://docs.gl-inet.com/router/en/4/interface_guide/plugins/).

---
=== "Tor"
    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities.

    To set up Tor, refer to[Tor](https://docs.gl-inet.com/router/en/4/interface_guide/tor/)

=== "Port forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. 
    
    To set up port forwarding, refer to [Port Forwards](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards). 

=== "AdGuard Home"

    AdGuard Home is a third-party tool that blocks ads and tracking to keep you safe. 
    
    To learn how to enable AdGuard Home, refer to [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/). 

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content. Spitz Plus offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app. 

    To set up parental controls, refer to [Parental controls](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control). 
    
---

## System settings

* To reset the router's admin password, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/admin_password/). 
* To reset the router's firmware, follow [these instructions](https://docs.gl-inet.com/router/en/4/faq/repair_network_or_reset_firmware/). 
* To reset the router's time zone, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/time_zone/). 
* To set scheduled tasks, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/scheduled_tasks/). 
* To set up custom DNS servers, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/dns/). 
* To view system logs, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/log/). 
* To learn more about managing your device clients, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/clients/).

--- 

## Product overview

### Product information

Slate 7 (GL-BE3600) is a dual-band Wi-Fi 7 portable travel router, with a maximum Wi-Fi speed of 3600 Mbps. Supporting both OpenVPN and WireGuard, Slate 7 ensures robust performance. Its compact and lightweight design ensures unparalleled portability, making it the perfect companion for travel, while its durable construction provides long-lasting performance wherever you go.

### Package contents

Your router package includes:

- 1 x User manual
- 1 x Slate 7 (GL-BE3600)
- 1 x Thank you card
- 1 x Warrenty card
- 1 x Ethernet cable
- 1 x Power adapter
- 1 x Converters (Base on your shipping countries, US/EU/UK/AU plugs)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

### Specifications

Refer to [Specifications](https://www.gl-inet.com/products/gl-be3600/#specs){target="_blank"}. 
