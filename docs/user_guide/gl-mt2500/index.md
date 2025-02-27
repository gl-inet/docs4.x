# GL-MT2500/GL-MT2500A(Brume 2) User Guide

## Hardware info

GL-MT2500/GL-MT2500A(Brume 2) is a lightweight and powerful VPN Gateway that runs on OpenWrt v21.02 operating system. It is compactly designed to host a VPN server at home, or run SD-WAN (Site-to-Site) for small and medium-sized enterprises.

![gl-mt2500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

[GL-MT2500/GL-MT2500A specification](https://www.gl-inet.com/products/gl-mt2500/#specs){target="_blank"}

[LED Indication](../../faq/led.md#gl-mt2500)

### PCB Pinout

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/gl-mt2500a_pinout.jpg" itemprop="contentUrl" data-size="1500x1313">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/gl-mt2500a_pinout.jpg" itemprop="thumbnail" alt="gl-mt2500 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## First time setup

All of GL.iNet's devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup.md/).

Please note that the adapter within the package depends on your shipping country.

What's inside the package? (The following figure shows the GL-MT2500A as an example.)

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

Package Contents:

- 1 x User manual
- 1 x Brume 2 (GL-MT2500 or GL-MT2500A)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Warranty card
- 1 x Power adapter (Selected plug type)

---

## INTERNET

The internet configuration interface lets users choose to establish the type of internet connection supported by the router.

Configure the internet network by selecting **INTERNET** in the side menu within the router's web Admin Panel. 

It supports three ways to connect to the internet as listed below:

### Ethernet

Ethernet 
Transmit data over an Ethernet cable using an Ethernet cable to connect the router to an active modem or an active network device. This method usually provides the fastest and most reliable Internet connection. 

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}

### Tethering

Establish internet access with connected devices by sharing a smartphone's mobile data to the router via cable. This method is most useful when users wants to use the phone's data to access the internet.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

### Cellular

Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

### Priority and load balance

Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time.

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

## CLIENTS

The Clients page displays information about connected devices. For each client, it shows the name, IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to block the client or perform other actions.

To set up Clients, refer to [Clients](../../interface_guide/clients.md).

## Cloud services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage GL.iNet routers. 
    
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

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content. Spitz AX offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app.

    To set up parental controls, refer to [Parental controls](../../interface_guide/parental_control).

=== "ZeroTier"

    ZeroTier is a software-defined networking solution that enables users to create secure, virtual networks over the internet, connecting devices as if they were on the same local network. 
    
    To set up ZeroTier, refer to [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/tailscale.md).

## NETWORK

### Firewall

GL.iNet's routers include multiple firewall features to ensure a secure connection and complete oversight by users. It lets users configure firewall rules including Port Forwarding, Open Ports, and DMZ.

[Click here to learn more about GL.iNet routers' firewall](../../interface_guide/firewall.md)

### Multi-WAN

Please visit the [**Multi-WAN**](../../interface_guide/multi-wan.md) tutorial.

### LAN

Please visit the [**LAN**](../../interface_guide/lan.md) tutorial.

### DNS

Please visit the [**DNS**](../../interface_guide/dns.md) tutorial.

### Network Mode

Please visit the [**Network Mode**](../../interface_guide/network_mode.md) tutorial.

### IPv6

Please visit the [**IPv6**](../../interface_guide/ipv6.md) tutorial.

### MAC Address

The Mac Address page was previously called Mac Clone and has been changed to Mac Address since v4.2.

Please visit the [**MAC Address**](../../interface_guide/mac_address.md) tutorial.

### Drop-in Gateway

Please visit the [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md) tutorial.

### IGMP Snooping

Please visit the [**IGMP Snooping**](../../interface_guide/igmp_snooping.md) tutorial.

### Network Acceleration

Formerly known as [Hardware Acceleration](../../interface_guide/hardware_acceleration.md).

Please visit the [**Network Acceleration**](../../interface_guide/network_acceleration.md) tutorial.

---

## SYSTEM

### Overview

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

### Upgrade

GL.iNet provides regular updates on our routers' firmware to improve performance, resolving bugs and fix vulnerabilities.

Please visit the [**Upgrade**](../../interface_guide/firmware_upgrade.md) tutorial.

### Scheduled Tasks

Please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.

### Admin Password

This feature has been moved to [**Security**](../../interface_guide/security.md) since v4.5.

Please visit the [**Admin Password**](../../interface_guide/admin_password.md) tutorial.

### Time Zone

Please visit the  [**Time Zone**](../../interface_guide/time_zone.md) tutorial.

### Log

Please visit the [**Log**](../../interface_guide/log.md) tutorial.

### Security

This feature is available since v4.5.

Please visit the [**Security**](../../interface_guide/security.md) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.

