# Mudi (GL-E750V2) User Guide

**Note:** The device previously named Mudi V2 (GL-E750V2) is now simply called Mudi (GL-E750V2). Both the original Mudi (GL-E750) and the updated Mudi (GL-E750V2) run on the same firmware. If you're using the original Mudi (GL-E750), update your firmware ([link to: GL.iNet download center | GL-E750/GL-E750V2 Mudi]) to access the latest features and functionality.

## How to set up Mudi 

To set up Mudi, you will use one of the four supported internet connection methods: Cellular (SIM cards), Ethernet, Repeater, and Tethering. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k?start=65" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!! note "Before you start, follow these steps (if connecting via the cellular method):"

    To connect to the internet via the cellular method, you will need at least one nano SIM card. Once you have the nano SIM card(s) ready, follow these steps:
    
    1. Activate your SIM card(s), if required by the SIM card carrier.
    2. Make sure you router is powered off.
    3. Insert the SIM card(s) into the SIM card slots. (**Note:** Only one SIM card is active at each time. The other SIM card functions only as a backup.)

### 1. First-time Setup 

=== "Insert SIM card"
     
    1. Turn to the backside of Mudi V2 (GL-E750V2).
    2. Poke your finger into the hole near the edge of the lid.
    3. Slide along the edge.
    4. When the lid slightly goes up (from around 25 degrees to 30 degrees or so), pull it up for the opening.
    5. Insert the card into the card slot as suggested by the symbol near the corner.
    6. Press the lid down to close the cover plate. 

     ![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_power-on.png){class="glboxshadow"}

=== "Battery Status"

    When Mudi V2 (GL-E750V2)'s power is off, you can still check the battery status by pressing the power button. The LED screen will show the battery status when you click the power button.

    ![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_battery.png){class="glboxshadow"}

=== "Standard Adapter"

    Make sure you are using a standard 5V/2A power adapter. Otherwise, it may **cause malfunction**.

    ![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_charge.png){class="glboxshadow"}

=== "Power On" 

    To turn on the device, press the power button for 3 sec.


### 2. Connect your device to the Mudi 

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

    The wireless settings lets users manage network security of the primary Wi-Fi and the Guest Wi-Fi, it is accessible by going to **WIRELESS** on the side menu.

### 3. Connect the Mudi V2 to the internet 

**Note:** The following instructions were written for those using the router web Admin Panel to connect the router to the internet. If you want to use the GL.iNet app instead of the web Admin Panel, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions. 

#### 1. Sign in to the router web Admin Panel 

In a web browser's address bar, enter `192.168.8.1`. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

    There are two ways to connect cellular connectivity to your router:

    **Option 1: Cellular-Enabled USB Modem**  

    * Insert a cellular-enabled USB modem into the router’s USB port to share internet access with all connected devices. This method is ideal for using an external modem to provide internet connectivity. [Click here to learn how to connect via USB modem.](../../interface_guide/internet_cellular.md)  

    **Option 2: Physical SIM Card**  

    * The router supports **Dual SIM, Single Standby**, allowing you to insert two SIM cards for internet access. However, only one SIM card can be active at a time, and you can manually switch between them.  
    * Additionally, this router supports **physical eSIM**. Follow our step-by-step guide to set up your eSIM:  [How to Set Up the eSIM Physical Card with GL.iNet Routers.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_esim/)

    [Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

=== "Ethernet"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a light blue dot appears next to "Ethernet."

    [Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)


=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

    1. On the main screen of the web Admin Panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a light blue dot appears next to the Wi-Fi network name.

    [Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the web Admin Panel, click **Connect** in the "Tethering" section. 
    
    If you are connected to the internet successfully, a light blue dot appears next to "Tethering."

    [Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

---

**Note:** If you want to use the [Multi-WAN](../../interface_guide/multi-wan.md) feature, you will have to set up more than one internet connection methods. 

---
## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Mudi V2 (and other GL.iNet routers) support OpenVPN, WireGuard, and Tailscale. 


=== "OpenVPN" 

    Mudi V2 (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mudi V2 (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, short for The Onion Router, is a privacy-focused network that enables anonymous communication over the internet. It routes internet traffic through a series of volunteer-operated servers (nodes) to obscure the user's location and usage, making it difficult to trace online activities.
    
    * [How to set up Tor](../../interface_guide/tor.md).

---

## More features and settings

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 
    
    To set up multi-WAN, Refer to [Multi-WAN](../../interface_guide/multi-wan.md). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently.
    
    To set up LAN, Refer to [Lan Tutorial](../../interface_guide/lan.md). 

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices.
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPV6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).
  
---

=== "MAC Address"

    A MAC address, or Media Access Control address, is a unique identifier assigned to network interfaces for communications on a physical network. It is typically expressed as a 12-digit hexadecimal number and is used to ensure that data packets are sent to the correct device on a local area network (LAN). 
    
    To set up MAC address, refer to [MAC Address](../../interface_guide/network_mode.md).
  

=== "Plug-ins"

    A plugin is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).


=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. 
    
    To set up dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "GoodCloud"

    Good Cloud refers to a cloud computing service that prioritizes performance, reliability, and security while providing scalable resources for users. 
    
    To set up goodcloud, refer to [GoodCloud](../../interface_guide/cloud.md).

---

=== "eSIM"

    This router supports eSIM functionality. To enable the feature, ensure you are using [firmware version 4.3.19](https://dl.gl-inet.com/release/router/release/xe3000/4.4.13) or later.  
    
    To set up eSIM, refer to [eSIM](https://youtu.be/hyHh8pAxgVw?feature=shared)  

=== "Tailscale"

    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/parental_control.md). 

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

## System settings

#### Power Button

- To turn on the device, press the power button for 3 seconds.
- To turn off the device, press the power button for 5 seconds. (After you press it for 3 seconds, the OLED screen will show “Standby Mode On” first). KEEP PRESSING the power button until you see “Shut Down” under the “Standby Mode On.” It will count down 3 seconds and turn off the device.

#### Standby Mode
In Standby Mode, the Mudi V2 (GL-E750V2) will turn off Wi-Fi and 4G to save power. You can't connect to Mudi V2 (GL-E750V2) in this mode.

To turn on or off the Standby Mode, press the power button for 3 seconds. You will see “Standby Mode On” or “Standby Mode Off” on the OLED screen

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

* To upgrade the router's firmway, please visit the [**Upgrade**](../../interface_guide/firmware_upgrade.md) tutorial.
* To learn more about managing your device clients, please visit the [**Clients**](../../interface_guide/clients.md) tutorial.
* To schedule tasks, please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.
* To set admin password, please visit the [**Admin Password**](../../interface_guide/admin_password.md) tutorial.
* To set timezone, please visit the  [**Time Zone**](../../interface_guide/time_zone.md) tutorial.
* To toggle button settings, please visit the [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md) tutorial.
* To view the logs, please visit the [**Log**](../../interface_guide/log.md) tutorial.
* To view security, please visit the [**Security**](../../interface_guide/security.md) tutorial.
* To reset firmware, please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.
* To adjust advanced settings, please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.
* To Uboot Mudi, please visit [**How to Uboot Mudi / Mudi V2 tutorial video**](https://www.youtube.com/watch?feature=shared&v=pz0DidfIXRk) tutorial.

---

## Product overview

### Product information

Mudi V2 (GL-E750V2) is a portable 4G LTE travel router compatible with global carriers. It runs fully open source on OpenWrt and GL.iNet's SDK 4.0, providing customization capabilities and a suite of features. Mudi V2 (GL-E750V2) supports 300Mbps (2.4GHz) and 433Mbps (5GHz) Wi-Fi speeds and a MicroSD card of up to 1TB. It has a built-in 7000mAh battery. It also supports multi-WAN (failover and load balance) to ensure a smooth connection for all your devices. 

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

---

### Package contents

Your router package includes:

- 1 x Mudi V2 (GL-E750V2) portable 4G LTE router
- 1 x Power adapter 
- 1 x Converters (Based on your shipping countries)
- 1 X User manual
- 1 x Warranty card
- 1 x Ethernet cable
- 1 x USB-C port replicator 
- 1 x USB-C to USB-C cable
- 1 x USB-A to USB-C cable
- 1 x Pouch bag
- 1 x Thank-you card

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

Check out [Mudi's unboxing video](https://www.youtube.com/watch?v=4FzEgmYyy7k&feature=youtu.be).

---

### Specification

[GL-e750 specification](https://www.gl-inet.com/products/gl-e750/#specs){target="_blank"}

---
