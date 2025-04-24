# Mudi V2 (GL-E750V2) User Guide

**Note:** Mudi V2 (GL-E750V2) and Mudi (GL-E750) run on the same firmware. If you are using Mudi (GL-E750), [upgrade your firmware](https://dl.gl-inet.com/?model=e750) to use the latest features and functionality, and refer to this user guide. 

## Product Information

Mudi V2 (GL-E750V2) is a portable 4G LTE travel router compatible with global carriers. It runs fully open source on OpenWrt and GL.iNet's SDK 4.0, providing customization capabilities and a suite of features. Mudi V2 (GL-E750V2) supports 300Mbps (2.4GHz) and 433Mbps (5GHz) Wi-Fi speeds and a MicroSD card of up to 1TB. It has a built-in 7000mAh battery. It also supports multi-WAN (failover and load balance) to ensure a smooth connection for all your devices. 

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

---

## Functionality

### Power Button

- To turn on the device, press the power button for 3 seconds.
- To turn off the device, press the power button for 5 seconds. (After you press it for 3 seconds, the OLED screen will show “Standby Mode On” first. KEEP PRESSING the power button until you see “Shut Down” under the “Standby Mode On.” It will count down 3 seconds and turn off the device.

### Standby Mode
In Standby Mode, the Mudi V2 (GL-E750V2) will turn off Wi-Fi and 4G to save power. You can't connect to Mudi V2 (GL-E750V2) in this mode.

To turn on or off the Standby Mode, press the power button for 3 seconds. You will see “Standby Mode On” or “Standby Mode Off” on the OLED screen.


## Package Contents

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Mudi V2 (GL-E750V2) portable 4G LTE router
- 1 x Power adapter 
- 4 x Converters (US, EU, UK & AU plugs)
- 1 X User manual
- 1 x Warranty card
- 1 x Ethernet cable
- 1 x USB-C port replicator 
- 1 x USB-C to USB-C cable
- 1 x USB-A to USB-C cable
- 1 x Pouch bag
- 1 x Thank-you card

---

## First-time Setup

### 1. Insert a SIM Card and an optional MicroSD card into Mudi V2 (GL-E750V2)

Note: If you are using a SIM card, you must insert it into your device before powering it on. 

1. Turn to the backside of Mudi V2 (GL-E750V2).
2. Poke your finger into the hole near the edge of the lid.
3. Slide along the edge.
4. When the lid slightly goes up (from around 25 degrees to 30 degrees or so), pull it up for the opening.
5. Insert the card into the card slot as suggested by the symbol near the corner.
6. Press the lid down to close the cover plate.

### 2. Power on
Press the power button to turn on the device.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_power-on.png){class="glboxshadow"}

When Mudi V2 (GL-E750V2)'s power is off, you can still check the battery status by pressing the power button. The LED screen will show the battery status when you click the power button.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_battery.png){class="glboxshadow"}

Make sure you are using a standard 5V/2A power adapter. Otherwise, it may cause malfunction.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET

The internet configuration interface lets users choose to establish the type of internet connection supported by the router.

Configure the internet network by selecting **INTERNET** in the side menu within the router's web Admin Panel. 

It supports four ways to connect to the internet as listed below:

### Ethernet

Transmit data over an Ethernet cable using an Ethernet cable to connect the router to an active modem or an active network device. This method usually provides the fastest and most reliable Internet connection. 

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

Extend the Wi-Fi coverage area of an existing Wi-Fi network by using a router to receive wireless signals within range and forwarding the signals to a further distance. This method is most useful when a single router does not have enough range to cover the entire usage area.

[Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

Establish internet access with connected devices by sharing a smartphone's mobile data to the router via cable. This method is most useful when users wants to use the phone's data to access the internet.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular
 
Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via cellular](../../interface_guide/internet_cellular.md)

Learn how to set up the eSIM physical card on your GL.iNet router with our step-by-step instructions here: [How to Set Up the eSIM Physical Card with the GL.iNet Routers?](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_esim/)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

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

### IGMP Snooping

Please visit the [**IGMP Snooping**](../../interface_guide/igmp_snooping.md) tutorial.

---

## SYSTEM

### Overview

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

### Upgrade

GL.iNet provides regular updates on our routers' firmware to improve performance, resolving bugs and fix vulnerabilities.

Please visit the [**Upgrade**](../../interface_guide/upgrade.md) tutorial.

### OLED Screen Settings

On this page, you can adjust what information is displayed on your Mudi V2 (GL-E750V2)'s OLED screen. 


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

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.

