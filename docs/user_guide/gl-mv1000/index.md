# Brume (GL-MV1000) User Guide

## Product overview

Brume (GL-MV1000) and Brume-W (GL-MV1000W) are powerful and stable networking products designed to do cutting-edge computing. With the Marvell high-performance chipset, the Brume and Brume-W* can run state-of-the-art cryptography at impressive speeds for an excellent VPN routing experience. Pre-installed OpenWrt and supported Ubuntu, Brume and Brume-W* allows in-depth developments for commercial IoT projects.

Brume-W (GL-MV1000W) is the special edition of Brume (GL-MV1000) that comes with an embedded Wi-Fi module, which delivers high-speed WiFi performance on 2.4GHz Wi-Fi with up to 300Mbps Wi-Fi speed.

## Specifications

[GL-MV1000 specifications](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

---

## First-time setup

All GL.iNet routers have a similar setup process. [Click here to learn about the first time-setup](../../faq/first_time_setup.md/).

---

## INTERNET

Log in to the router's web Admin Panel, and navigate to **INTERNET** from the left-side menu. 

This page allows you to select your internet connection type, such as Ethernet, Repeater, Tethering, and Cellular, depending on your model. 

For Brume (GL-MV1000), it supports three types of connection type: Ethernet, Tethering, and Cellular.

### Ethernet

Connect your router to an active modem or an active network device via an Ethernet cable to access the Internet. This method usually provides the fastest and most reliable Internet connection.

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}

### Tethering

Connect the router's USB port to a smartphone with active mobile data via a USB cable to access the Internet. This method enables multiple devices connected to the router to access the internet using the smartphone's mobile data.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### Cellular
 
Connect the router to the internet by plugging a cellular-enabled USB modem into the router's USB port. This method is useful for sharing internet from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., Ethernet, Repeater) at the same time. If the top-priority internet connection fails, the router will automatically switch to another internet connection. This is also called Failover, ensuring smooth and uninterrupted internet access.

Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet connection. 

Alternatively, you can switch the Multi-WAN mode from Failover to Load Balance, which enables you to use multiple network interfaces at the same time to increase the total bandwidth of the router.

---

## CLIENTS

Clients are devices connected to the router, you can block clients or limit its network speed. The interface is accessible by clicking **CLIENTS** in the side menu of the router's Admin Panel.

[Click here to learn more about managing your device clients.](../../interface_guide/clients.md)

---

## VPN

GL.iNet routers are pre-installed with OpenVPN and WireGuard® supporting 30+ VPN services. It automatically encrypts all network traffic within the connected network, including guest devices and client devices that are not capable of running VPN encryption. Our routers can also act as VPN servers, redirecting traffic from client devices in remote locations to the VPN server via a VPN tunnel before accessing the public internet.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Please refer to the following links for a step to step setup guide:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard

Please refer to the following links for a step to step setup guide:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

GL.iNet routers include a wide range of add-on features that simplifies device management, improves user's internet experience, automates firmware update, and more.

### Plug-ins

Please visit the [**Plug-ins**](../../interface_guide/plugins.md) tutorial.

### Dynamic DNS

Please visit the [**Dynamic DNS**](../../interface_guide/ddns.md) tutorial.

### GoodCloud

Please visit the  [**GoodCloud**](../../interface_guide/cloud.md) tutorial.

### Network Storage

Please visit the [**Network Storage**](../../interface_guide/network_storage.md) tutorial.

### AdGuard Home

Please visit the [**AdGuard Home**](../../interface_guide/adguardhome.md) tutorial.

### Parental Control

Please visit the [**Parental Control**](../../interface_guide/parental_control.md) tutorial.

### ZeroTier

Please visit the [**ZeroTier**](../../interface_guide/zerotier.md) tutorial.

### Tailscale

Please visit the [**Tailscale**](../../interface_guide/tailscale.md) tutorial.

---

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

---

## SYSTEM

### Overview

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

### Upgrade

GL.iNet provides regular updates on our routers' firmware to improve performance, resolving bugs and fix vulnerabilities.

Please visit the [**Upgrade**](../../interface_guide/upgrade.md) tutorial.

### Scheduled Tasks

Please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.

### Admin Password

This feature has been moved to [**Security**](../../interface_guide/security.md) since v4.5.

Please visit the [**Admin Password**](../../interface_guide/admin_password.md) tutorial.

### Time Zone

Please visit the  [**Time Zone**](../../interface_guide/time_zone.md) tutorial.

### Toggle Button Settings

Please visit the [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md) tutorial.

### Log

Please visit the [**Log**](../../interface_guide/log.md) tutorial.

### Security

This feature is available since v4.5.

Please visit the [**Security**](../../interface_guide/security.md) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.
