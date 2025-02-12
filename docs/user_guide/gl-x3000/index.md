# Spitz AX (GL-X3000) User Guide

## How to set up Spitz AX

To set up Spitz AX, you will use one of the four supported internet connection methods: Cellular (SIM cards), ethernet, repeater, and tethering. Watch this setup video or follow the steps below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup but the steps are the same for Spitz AX and other router models.)</small>

!!! note "Before you start, follow these steps (if connecting via the cellular method):"

    To connect to the internet via the cellular method, you will need at least one nano SIM card. Once you have the nano SIM card(s) ready, follow these steps:
    
    1. Activate your SIM card(s), if required by the SIM card carrier.
    2. Make sure you router is powered off.
    3. Insert the SIM card(s) into the SIM card slots. (**Note:** Only one SIM card is active at each time. The other SIM card functions only as a backup.)

### 1. Power on the Spitz AX

Put the two-piece power adapter together. Connect it to your router and plug it into a outlet. It will start up automatically.

### 2. Connect your device to the Spitz AX

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

=== "Ethernet"

    Connect your device to the router's LAN port using an ethernet cable. 

=== "Wi-Fi"

    On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

### 3. Connect the Spitz AX to the internet 

**Note:** The following instructions were written for those using the router admin panel to connect the router to the internet. If you want to use the GL.iNet app instead of the admin panel, [download the app](https://www.gl-inet.com/app/) and follow the on-screen instructions. 

#### 1. Sign in to the router admin panel 

In a web browser's address bar, enter 192.168.8.1. Choose your language, then click **Next**. Set your admin password, then click **Apply**. 

#### 2. Set up your internet connection method(s)

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_cellular.jpg){class='glboxshadow'}

    There are two ways to connect cellular connectivity to your router:

    **Option 1: Cellular-Enabled USB Modem**  

    * Insert a cellular-enabled USB modem into the router’s USB port to share internet access with all connected devices. This method is ideal for using an external modem to provide internet connectivity. [Click here to learn how to connect via USB modem.](../../interface_guide/internet_cellular.md)  

    **Option 2: Physical SIM Card**  

    * The router supports **Dual SIM, Single Standby**, allowing you to insert two SIM cards for internet access. However, only one SIM card can be active at a time, and you can manually switch between them.  
    * Additionally, this router supports **physical eSIM**. Follow our step-by-step guide to set up your eSIM:  [How to Set Up the eSIM Physical Card with GL.iNet Routers.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_esim/)


    For issues using the cellular method, refer to the [Cellular Network Troubleshooting Guide](https://docs.gl-inet.com/router/en/4/faq/gl-x3000_gl-xe3000_connection_optimization/). 

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_ethernet.jpg){class='glboxshadow'}
    
    Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a light blue dot appears next to "Ethernet."

    Please refer to [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) for detailed instructions.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_repeater.jpg){class='glboxshadow'}

    1. On the main screen of the admin panel, locate the "Repeater" section, then click **Connect**.
    2. Select a Wi-Fi network. 
    3. Enter the network password, then click **Apply**.
    
    If you are connected to the internet successfully, a light blue dot appears next to the Wi-Fi network name.

    Please refer to [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) for detailed instructions.

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/internet/x3000_tethering.jpg){class='glboxshadow'}

    1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
    2. In your mobile device's settings, enable tethering. 
    3. On the main screen of the admin panel, click **Connect** in the "Tethering" section. 
    
    If you are connected to the internet successfully, a light blue dot appears next to "Tethering."

    Please refer to [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) for detailed instructions.

**Note:** If you want to use the multi-WAN feature, you will have to set up more than one internet connection methods. 

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). Spitz AX (and other GL.iNet routers) support OpenVPN, WireGuard, and Tailscale. 


=== "OpenVPN" 
    Spitz AX (and other GL.iNet routers) support the OpenVPN protocol which offers strong security. To set up OpenVPN, follow these tutorials:

    * [How to set up an OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [How to set up an OpenVPN server](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"
    Spitz AX (and other GL.iNet routers) support the WireGuard protocol which offers great speeds and convenience. To set up WireGuard, follow these tutorials:

    * [How to set up a WireGuard client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [How to set up a WireGuard server](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

=== "Tailscale"
    Tailscale is a VPN service that allows you to access your devices and applications anywhere. To set up Tailscale, refer to [Tailscale](https://docs.gl-inet.com/router/en/4/interface_guide/tailscale/). 

---

## More features and settings

=== "Port forwarding"

    Port forwarding allows remote servers and devices on the internet to access devices on a private network. To set up port forwarding, refer to [Port Forwards](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards). 

=== "Multi-WAN"

    Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

    To set up multi-WAN, refer to [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

=== "AdGuard Home"

    AdGuard Home is a third-party tool that blocks ads and tracking to keep you safe. To learn how to enable AdGuard Home, refer to [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/). 


=== "Drop-in gateway"

    Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. To set up drop-in gateway, refer to [How to set up drop-in gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/). 

---

=== "Dynamic DNS"

    Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. To set up dynamic DNS, refer to [Dynamic DNS](https://docs.gl-inet.com/router/en/4/interface_guide/ddns/). 

=== "Parental controls"

    Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content. Spitz AX offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app. 

    To set up parental controls, refer to [Parental controls](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control). 

=== "eSIM"

    This router supports eSIM functionality. To enable the feature, ensure you are using [firmware version 4.4.13](https://dl.gl-inet.com/release/router/release/xe3000/4.4.13) or later.  
    
    To set up eSIM, refer to [eSIM](https://youtu.be/hyHh8pAxgVw?feature=shared)  
    
---

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

Spitz AX (GL-X3000) is a dual-SIM Wi-Fi 6 cellular gateway designed to provide fast, reliable connections especially in remote areas and during road trips. It offers four internet access methods: Cellular (SIM cards), ethernet, repeater, and tethering. It supports multi-WAN (failover and load-balancing), VPN (OpenVPN and Wireguard), parental controls, AdGuard Home, port forwarding, Tailscale, and more. 

### Package contents

Your router package includes:

- 1 x User manual
- 1 x Spitz AX (GL-X3000)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Wall mount kit
- 1 x Power adapter (US+EU+UK+AU plugs)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x3000/first_time_setup/x3000_unboxing.jpg){class="glboxshadow"}

### LED indicators 

| Condition status                                                              | Power                                | Internet                    | 2.4GHz                      | 5GHz                        |Cellular | 
| ----------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | ------- |
| Normal (connected to the internet)                                            | Green                                | Green                       | Green                       | Green                       | Green   |
| Not connected to the internet                                                 | Green                                | Off                         | Green                       | Green                       | Green   |
| Updating firmware                                                             | Green                                | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Green   | 
| Resetting router (hold down "reset" button for > 3s)                          | Blinkng green (every 1s)             | Green                       | Green                       | Green                       | Green   |
| Restoring router to factory settings (hold down "reset" button for 10s)       | Fast blinking green (every 0.25s)    | Green                       | Green                       | Green                       | Green   | 

### Specifications

Refer to [Specifications](https://www.gl-inet.com/products/gl-x3000/#specs){target="_blank"}. 
