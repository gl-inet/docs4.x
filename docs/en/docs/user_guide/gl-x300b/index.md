# Collie (GL-X300B) User Guide

## Product overview

Collie (GL-X300B) is an industrial cellular gateway designed to operate under high temperatures and scenarios with potential physical hazards. There are three versions of Collie, designed to operate in indoor stationary facilities (GL-X300B-RS485 / GL-X300B-BLE), or in transportation vehicles (GL-X300B-GPS). Collie is perfect for machine-to-machine communications between electrical devices in high electrical noise environments.

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

**What's the difference?**

![gl-x300b series](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b_series.png){class="glboxshadow"}

![gl-x300b comparison](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/model_comparison.png){class="glboxshadow"}

- **GL-X300B-GPS** is equipped with five external antennas, including two 2.4GHz Wi-Fi, two 4G LTE, and one GPS Antenna. The extendable wired antennas are perfect for having multiple reception placements within a vehicle, minimizing reception black spots when traveling through high network density cities.

- **GL-X300B-BLE** is equipped with three external omnidirectional antennas for 2.4GHz Wi-Fi, 4G LTE, and BLE communication, receiving signals from all directions, and providing high flexibility in installation placement within an industrial environment.

- **GL-X300B-RS485** includes an RS485 chip with RS485 interface. The module supports bi-directional data transmission of various devices in the field of industrial automation and IoT, thus realizing the functions of data acquisition, control and monitoring.

!!! Note

    The BLE and GPS versions are available with a minimum order quantity.

## Package contents

Please note that the adapter within the package depends on your shipping country.

The package includes:

- 1 x User manual
- 1 x Collie (GL-X300B)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Warranty card
- 1 x Power adapter (Selected plug type)

**Note**: The image below is an example of GL-X300B-GPS, with some models slightly different.

![gl-x300b unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/first_time_setup/x300b-gps_unboxing.jpg){class="glboxshadow"}

## Specifications

[GL-X300B specifications](https://www.gl-inet.com/products/gl-x300b/#specs){target="_blank"}

## First-time setup

All GL.iNet routers have a similar setup process. [Click here to learn about the first-time setup](../../faq/first_time_setup.md/).

## INTERNET

Log in to the router's web Admin Panel, and navigate to **INTERNET** from the left-side menu. 

This page allows you to select your internet connection type, such as Ethernet, Repeater, Tethering, and Cellular, depending on your model. 

For Collie (GL-X300B), it supports three types of connection type: Ethernet, Repeater, and Cellular.

### Ethernet

Connect your router to an active modem or an active network device via an Ethernet cable to access the Internet. This method usually provides the fastest and most reliable Internet connection.

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### Repeater

Set up your router as a repeater to extend the Wi-Fi coverage of an existing Wi-Fi network. As a repeater, it receives and retransmits wireless signals within its range, thereby extending its coverage. This method is useful when a single router cannot cover the entire usage area.

[Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### Cellular
 
Insert a SIM card into the router's SIM card slot to connect it to the internet. This method is useful for sharing internet access from a single SIM card to all connected devices.

[Click here to learn how to connect to the internet via cellular](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., Ethernet, Repeater, and Cellular) at the same time. If the top-priority internet connection fails, the router will automatically switch to another internet connection. This is also called Failover, ensuring smooth and uninterrupted internet access.

Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet connection. 

Alternatively, you can switch the Multi-WAN mode from Failover to Load Balance, which enables you to use multiple network interfaces at the same time to increase the total bandwidth of the router.

---

## WIRELESS

The wireless settings lets users manage network security of the primary Wi-Fi and the Guest Wi-Fi, it is accessible by going to **WIRELESS** on the side menu.

[Click here to learn more about the wireless configuration](../../interface_guide/wireless.md)

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

---

## APPLICATIONS

GL.iNet routers include a wide range of add-on features that simplifies device management, improves user's internet experience, automates firmware update, and more.

### Plug-ins

Please visit the [**Plug-ins**](../../interface_guide/plugins.md) tutorial.

### Dynamic DNS

Please visit the [**Dynamic DNS**](../../interface_guide/ddns.md) tutorial.

### GoodCloud

Please visit the  [**GoodCloud**](../../interface_guide/cloud.md) tutorial.

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

### Log

Please visit the [**Log**](../../interface_guide/log.md) tutorial.

### Security

This feature is available since v4.5.

Please visit the [**Security**](../../interface_guide/security.md) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.
