# Mudi V2 (GL-E750V2) User Guide

**Note:** Mudi V2 (GL-E750V2) and Mudi (GL-E750) run on the same firmware. If you are using Mudi (GL-E750), [upgrade your firmware](https://dl.gl-inet.com/?model=e750) to use the latest features and functionality.

## Product Overview

Mudi V2 (GL-E750V2) is a portable 4G LTE travel router compatible with global carriers. It runs fully open source on OpenWrt and GL.iNet's SDK 4.0, providing customization capabilities and a suite of features. Mudi V2 (GL-E750V2) supports 300Mbps (2.4GHz) and 433Mbps (5GHz) Wi-Fi speeds and a MicroSD card of up to 1TB. It has a built-in 7000mAh battery. It also supports multi-WAN (failover and load balance) to ensure a smooth connection for all your devices. 

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Button

- Press the power button for **3 seconds**: Turn on the device.

- Press the power button for **3-5 seconds**: Enter Standby Mode.

- Press the power button for **more than 5 seconds**: Turn off the device. 

    (When pressing for 3 seconds, the OLED screen will show “Standby Mode On” first. KEEP PRESSING the power button until you see "Shut Down" under the "Standby Mode On". It will count down 3 seconds and turn off the device.)

## Standby Mode

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

Watch this video or follow the steps to set up Mudi V2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Insert a SIM Card

Insert a SIM Card and an optional MicroSD card into Mudi V2 (GL-E750V2).

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

Log in to the router's web Admin Panel, and navigate to **INTERNET** from the left-side menu. 

This page allows you to select your internet connection type, such as Ethernet, Repeater, Tethering, and Cellular.

### Ethernet

Connect your router to an active modem or an active network device via an Ethernet cable to access the Internet. This method usually provides the fastest and most reliable Internet connection.

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

Set up your router as a repeater to extend the Wi-Fi coverage of an existing Wi-Fi network. As a repeater, it receives and retransmits wireless signals within its range, thereby extending its coverage. This method is useful when a single router cannot cover the entire usage area.

[Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

Connect the router's USB port to a smartphone with active mobile data via a USB cable to access the Internet. This method enables multiple devices connected to the router to access the internet using the smartphone's mobile data.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular
 
Remove the back cover from Mudi V2, and insert a SIM card into the SIM card slot to connect it to the internet. This method is useful for sharing internet access from a single SIM card to all connected devices.

[Click here to learn how to connect to the internet via cellular](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

To use eSIM physical card on your GL.iNet router, please click here: [How to use the eSIM Physical Card with GL.iNet routers?](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

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

