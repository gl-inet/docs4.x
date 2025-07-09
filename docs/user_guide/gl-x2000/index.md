# Spitz Plus (GL-X2000) User Guide

All GL.iNet routers have a simple and almost identical setup process. [Click here to learn about the first-time setup](../../faq/first_time_setup.md/).

## How to set up Spitz Plus

To set up Spitz Plus, you will use one of the four supported internet connection methods: Cellular (SIM cards), ethernet, repeater, and tethering. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Spitz Plus and other router models.)</small>

!!! note "Before you start, follow these steps (if connecting via the cellular method):"

    At least one nano SIM card is required to connect to the internet via the cellular method. Once you have the nano SIM card(s) ready, follow these steps:
    
    1. Activate your SIM card(s) if required by the SIM card carrier.
    2. Power off your router.
    3. Insert the SIM card(s) into the SIM card slots. (**Note:** Only one SIM card is active at one time. The other SIM card functions only as a backup.)

### 1. Power on the Spitz Plus

Put the two-piece power adapter together. Connect it to your router and plug it into an outlet. It will start up automatically.

### 2. Connect your device to the Spitz Plus

Connect your computer or mobile device to the router using Wi-Fi or ethernet cable.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, go to Settings -> WLAN, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

### 3. Connect the Spitz Plus to the internet 

**Note:** The following instructions apply to users configuring the router via the GL.iNet Web Admin Panel. If you prefer using the GL.iNet app, [download the app](https://www.gl-inet.com/app/){target="_blank"} and follow the on-screen instructions.

#### 1. Log in to the router admin panel 

Launch a web browser, enter `192.168.8.1` in the address bar, and you will enter the GL.iNet Web Admin Panel. Choose a language and set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    If you have already inserted the SIM card into your router, the internet should be connected automatically. (You should see the name of your SIM carrier and a green dot appear in the Cellular section.) 
    
    If not, click the **Auto Setup** option if it appears. 
    
    Please refer to [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models) for detailed instructions.

    Note: The eSIM functionality of GL-X2000 is available on firmware v4.7 and above.

    Learn how to use the eSIM physical card on GL.iNet router [here](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

    For issues using the cellular, refer to the [Cellular Network Troubleshooting Guide](../../faq/cellular_network_troubleshooting_guide.md). 

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}
    
    Connect an ethernet cable between your router's WAN port and an upstream device, such as a modem. 
    
    Once the router is successfully connected to the internet, a green dot will appear next to "Ethernet" on the INTERNET page of the Web Admin Panel.

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. On the INTERNET page of the admin panel, locate the "Repeater" section and click **Connect**.
    2. Select a Wi-Fi network from the available networks. 
    3. Enter the network password, then click **Apply**.
    
    Once the router is successfully connected to the internet, a green dot will appear next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Connect your mobile device to the router's USB port using a USB 3.0 data transfer cable. 
    2. In your mobile device's settings, enable USB tethering. 
    3. On the INTERNET page of the admin panel, click **Connect** in the "Tethering" section. 
    
    Once the router is successfully connected to the internet, a green dot will appear next to "Tethering".

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

**Note:** If you want to use the multi-WAN feature, please set up more than one internet connection methods. 

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an additional layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Spitz Plus (and other GL.iNet routers) support OpenVPN and WireGuard. 

=== "OpenVPN" 
    Spitz Plus (and other GL.iNet routers) supports the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [How to set up an OpenVPN server](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"
    Spitz Plus (and other GL.iNet routers) supports the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [How to set up a WireGuard server](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

---

## Wireless and clients

=== "Wireless"

    The Wireless page allows you to configure settings for both 5 GHz and 2.4 GHz Wi-Fi networks, including enabling/disabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling/disabling randomized BSSID, selecting Wi-Fi security mode, setting Wi-Fi password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel.

    To set up Wireless, refer to [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    The Clients page displays information about connected devices. For each client, it shows the device name, connection type (i.e., via ethernet or Wi-Fi), IP and MAC addresses, download and upload speeds, total traffic, and provides the ability to reserve IP, block the client or perform other actions.

    To set up Clients, refer to [Clients](../../interface_guide/clients.md).

---

## GoodCloud service

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} service provides an easy and simple way to remotely access and manage GL.iNet routers. 
    
To set up GoodCloud, refer to [GoodCloud](../../interface_guide/cloud.md).

## Applications

=== "Plug-ins"

    A plugin is a software component that adds specific features or functionalities to an existing computer program, allowing for customization and enhancement of its capabilities. 
    
    To set up plug-ins, refer to [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is useful for users who need a static IP address for accessing a remote network. 
    
    To set up dynamic DNS, refer to [Dynamic DNS](../../interface_guide/ddns.md). 

=== "Network Storage"

    Network storage refers to a centralized data storage solution that allows multiple users and devices to access and share files over a network. 
    
    To set up network storage, refer to [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home is a third-party tool that blocks ads and tracking to keep you safe. To learn how to enable AdGuard Home, refer to [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/). 

=== "Parental Control"

    Parental control is a group of settings designed to help you manage and control your children's devices. It includes limiting their screen time and restricting their access to certain content. Spitz Plus offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app. 

    To set up parental control, refer to [Parental controls](../../interface_guide/parental_control.md). 

=== "Tailscale"

    Spitz Plus supports Tailscale on firmware v4.7 and above.
    
    Tailscale is a VPN service that allows you to access your devices and applications anywhere. 
    
    To set up Tailscale, refer to [Tailscale](../../interface_guide/parental_control.md). 

=== "eSIM"

    Spitz Plus supports eSIM functionality only on firmware v4.7 and above. 
    
    To learn how to set up and manage eSIM on your device, please refer to [this tutorial](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
## Network settings

=== "Port forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. To set up port forwarding, refer to [Port Forwards](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards). 

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

=== "LAN"

    LAN, or Local Area Network, is a network that connects computers and devices within a limited geographical area, such as a home or office. It enables high-speed data transfer and resource sharing, allowing devices to communicate with each other efficiently. 
    
    To set up LAN, refer to [Lan Tutorial](../../interface_guide/lan.md). 

---

=== "Guest Network"

    It allows you to set a subnet within the IPv4 private address ranges 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8, specify the gateway and netmask IP addresses, and configure security settings like AP isolation for the guest network.

    To set up LAN, refer to [Lan Tutorial](../../interface_guide/guest_network.md). 

=== "DNS"

    The DNS page allows you to set custom DNS servers, enable DNS rebinding attack protection and override DNS settings of all clients, allow custom DNS to override VPN DNS, and configure the DNS server settings mode to automatic or manually specify DNS servers from the Ethernet connection.

    To set up DNS, refer to [DNS](../../interface_guide/dns.md).

=== "Network Port Management"

    The Network Port Management page allows you to configure the WAN and LAN ports, set the WAN/LAN interface to Ethernet, specify the MAC mode and MAC address for the WAN interface, and show the negotiate the network port rate.

---

=== "Network Mode"

    Network mode refers to the configuration settings that determine how a device connects to a network and communicates with other devices. 
    
    To set up network mode, refer to [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, or Internet Protocol version 6, is the most recent version of the Internet Protocol designed to replace IPv4. It provides a vastly larger address space, allowing for a virtually unlimited number of unique IP addresses, which is essential for accommodating the growing number of devices connected to the internet. 
    
    To set up IPV6, refer to [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. To set up drop-in gateway, refer to [How to set up drop-in gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/). 

---

=== "IGMP Snooping"

    IGMP snooping is a network optimization technique used in Ethernet switches to manage and control multicast traffic. 
    
    To set up IGMP snooping, refer to [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Hardware acceleration refers to the use of specialized hardware components to perform specific tasks more efficiently than general-purpose CPUs. 
    
    To set up network acceleration to this [Network Acceleration](../../interface_guide/network_acceleration.md) tutorial.

=== "NAT Settings"

    The NAT Settings page allows you to enable or disable Full Cone NAT and SIP ALG (Application Layer Gateway) functionality.

    To set up NAT settings, refer to [NAT Settings](../../interface_guide/nat_settings.md).

## System settings

* To reset the router's admin password, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/admin_password/). 
* To reset the router's firmware, follow [these instructions](https://docs.gl-inet.com/router/en/4/faq/repair_network_or_reset_firmware/). 
* To reset the router's time zone, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/time_zone/). 
* To set scheduled tasks, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/scheduled_tasks/). 
* To set up custom DNS servers, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/dns/). 
* To view system logs, follow [these instructions](https://docs.gl-inet.com/router/en/4/interface_guide/log/). 

--- 

## Product overview

### Product information

Spitz Plus (GL-X2000) is a dual-SIM 4G LTE Wi-Fi 6 cellular gateway designed to provide fast, reliable connections especially in remote areas and during road trips. Featuring 3-Carrier Aggregation, the router streams data on three carrier bands simultaneously, providing 3x available bandwidth to avoid congestion. It offers four internet access methods: Cellular (SIM cards), ethernet, repeater, and tethering. It supports multi-WAN (failover and load-balancing), VPN (OpenVPN and Wireguard), parental controls, AdGuard Home, port forwarding, Tailscale, and more. 

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}


### Package contents

Please note that the adapter within the package depends on your shipping country.

Your router package includes:

- 1 x User manual
- 1 x Spitz Plus (GL-X2000)
- 4 x External antennas
- 1 x Thank you card
- 1 x Ethernet cable
- 1 x Wall mount kit
- 1 x Adhesive pad
- 4 x Screws
- 1 x Power adapter
- 1 x Converters (Base on your shipping countries, US/EU/UK/AU plugs)


![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_unboxing.jpg){class="glboxshadow"}

### LED indicators 

| Condition status                                                              | Power                                | Internet                    | 2.4GHz                      | 5GHz                        |Cellular | 
| ----------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | ------- |
| Normal (connected to the internet)                                            | Green                                | Green                       | Green                       | Green                       | Green   |
| Not connected to the internet                                                 | Green                                | Off                         | Green                       | Green                       | Green   |
| Updating firmware                                                             | Green                                | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Green   | 
| Resetting router (hold down "reset" button for > 3s)                          | Blinkng green (every 1s)             | Green                       | Green                       | Green                       | Green   |
| Restoring router to factory settings (hold down "reset" button for 10s)       | Fast blinking green (every 0.25s)    | Green                       | Green                       | Green                       | Green   | 

### Specifications

Refer to [Specifications](https://www.gl-inet.com/products/gl-x2000/#specs){target="_blank"}. 

