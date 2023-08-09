# GL-MT2500/GL-MT2500A(Brume 2) User Guide

## Hardware info

GL-MT2500/GL-MT2500A(Brume 2) is a lightweight and powerful VPN Gateway that runs on OpenWrt v21.02 operating system. It is compactly designed to host a VPN server at home, or run SD-WAN (Site-to-Site) for small and medium-sized enterprises.

![gl-mt2500 interface](https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

[GL-MT2500/GL-MT2500A specification](https://www.gl-inet.com/products/gl-mt2500/#specs){target="_blank"}

### PCB Pinout

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/hardware_info/gl-mt2500a_pinout.jpg" itemprop="contentUrl" data-size="1500x1313">
      <img src="https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/hardware_info/gl-mt2500a_pinout.jpg" itemprop="thumbnail" alt="gl-mt2500 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## First time setup

All of GL.iNet's devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup/).

Please note that the adapter within the package depends on your shipping country.

What’s inside the package? (The following figure shows the GL-MT2500A as an example.)

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

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

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet)

![Ethernet Connection](https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}

### Tethering

Establish internet access with connected devices by sharing a smartphone’s mobile data to the router via cable. This method is most useful when users wants to use the phone's data to access the internet.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering)

![Tethering Connection](https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

### Cellular

Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular)

![Cellular Connection](https://static.gl-inet.com/docs/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

### Priority and load balance

Go to [Multi-WAN](../../interface_guide/multi-wan/) to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time.

---

## CLIENTS

Clients are devices connected to the router, you can block clients or limit its network speed. The interface is accessible by clicking **CLIENTS** in the side menu of the router’s Admin Panel.

[Click here to learn more about managing your device clients.](../../interface_guide/clients/)

---

## VPN

GL.iNet routers are pre-installed with OpenVPN and WireGuard® supporting 30+ VPN services. It automatically encrypts all network traffic within the connected network, including guest devices and client devices that are not capable of running VPN encryption. Our routers can also act as VPN servers, redirecting traffic from client devices in remote locations to the VPN server via a VPN tunnel before accessing the public internet.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard/)

### OpenVPN

Please refer to the following links for a step to step setup guide:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client/)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server/)

### WireGuard

Please refer to the following links for a step to step setup guide:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client/)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server/)

---

## APPLICATIONS

GL.iNet routers include a wide range of add-on features that simplifies device management, improves user's internet experience, automates firmware update, and more.

### Plug-ins

Please visit the [**Plug-ins**](../../interface_guide/plugins/) tutorial.

### Dynamic DNS

Please visit the [**Dynamic DNS**](../../interface_guide/ddns/) tutorial.

### GoodCloud

Please visit the  [**GoodCloud**](../../interface_guide/cloud/) tutorial.

### Network Storage

Please visit the [**Network Storage**](../../interface_guide/network_storage/) tutorial.

### AdGuard Home

Please visit the [**AdGuard Home**](../../interface_guide/adguardhome/) tutorial.

### Parental Control

Please visit the [**Parental Control**](../../interface_guide/parental_control/) tutorial.

### ZeroTier

Please visit the [**ZeroTier**](../../interface_guide/zerotier/) tutorial.

### Tailscale

Please visit the [**Tailscale**](../../interface_guide/tailscale/) tutorial.

---

## NETWORK

### Firewall

GL.iNet's routers include multiple firewall features to ensure a secure connection and complete oversight by users. It lets users configure firewall rules including Port Forwarding, Open Ports, and DMZ.

[Click here to learn more about GL.iNet routers’ firewall](../../interface_guide/firewall/)

### Multi-WAN

Please visit the [**Multi-WAN**](../../interface_guide/multi-wan/) tutorial.

### LAN

Please visit the [**LAN**](../../interface_guide/lan/) tutorial.

### DNS

Please visit the [**DNS**](../../interface_guide/dns/) tutorial.

### Network Mode

Please visit the [**Network Mode**](../../interface_guide/network_mode/) tutorial.

### IPv6

Please visit the [**IPv6**](../../interface_guide/ipv6/) tutorial.

### MAC Address

The Mac Address page was previously called Mac Clone and has been changed to Mac Address since v4.2.

Please visit the [**MAC Address**](../../interface_guide/mac_address/) tutorial.

### Drop-in Gateway

Please visit the [**Drop-in Gateway**](../../interface_guide/drop-in_gateway/) tutorial.

### IGMP Snooping

Please visit the [**IGMP Snooping**](../../interface_guide/igmp_snooping/) tutorial.

### Network Acceleration

Formerly known as [Hardware Acceleration](../../interface_guide/hardware_acceleration/).

Please visit the [**Hardware Acceleration**](../../interface_guide/hardware_acceleration/) tutorial.

---

## SYSTEM

### Overview

Please visit the [**System Overview**](../../interface_guide/system_overview/) tutorial.

### Upgrade

GL.iNet provides regular updates on our routers' firmware to improve performance, resolving bugs and fix vulnerabilities.

Please visit the [**Upgrade**](../../interface_guide/firmware_upgrade/) tutorial.

### Scheduled Tasks

Please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks/) tutorial.

### Admin Password

Please visit the [**Admin Password**](../../interface_guide/admin_password/) tutorial.

### Time Zone

Please visit the  [**Time Zone**](../../interface_guide/time_zone/) tutorial.

### Log

Please visit the [**Log**](../../interface_guide/log/) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware/) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings/) tutorial.

