# Spitz AX (GL-X3000 ) User Guide

## How to set up Spitz AX

To set up Spitz AX, you will use one of the four supported internet connection methods: Cellular (SIM cards), ethernet, repeater, and tethering. Follow the steps below. 

<div class="callout">

<b> If you are connecting via the cellular method </b> <br>

<br> To connect to the internet via the cellular method, you will need at least one nano SIM card. Once you have the nano SIM card(s) ready, follow these steps: <br>

<br>

1. Activate your SIM card(s), if required by the SIM card carrier. <br>
2. Make sure you router is powered off. <br>
3. Insert the SIM card(s) into the SIM card slots. (<b>Note:</b> Only one SIM card is active at each time. The other SIM card functions only as a backup.)

</div>

<style type="text/css" rel="stylesheet">
.callout {
  border: 1px solid #ccc;
  background-color: #f5f5f5;
  padding: 10px;
  margin-bottom: 10px;
}
</style>

### 1. Power on the Spitz AX

Put the two-piece power adapter together. Connect it to your router and plug it into a wall outlet. Press the power button.

### 2. Connect your device to the Spitz AX

Connect your computer or mobile device to the router using Wi-Fi or ethernet.

#### Wi-Fi

On your device, locate your router's Wi-Fi network name in the list of available networks and enter the password. (You can find the default network name and password printed on your router's label.)

#### Ethernet
Connect your device to the router's LAN port using an ethernet cable. 

### 3. Connect the Spitz AX to the internet 

**Note:** The following instructions were written for those using the router admin panel to connect the router to the internet. If you want to use the GL.iNet app instead of the admin panel, download the app from your device's app store and follow the on-screen instructions. 

#### I. Sign in to the router admin panel 

1. In a web browser's address bar, enter 192.168.8.1. 
2. Choose your language, then click **Next**.
3. Set your admin password, then click **Apply**. 

#### II. Set up your internet connection method(s)

**Note:** To use the multi-WAN feature, you will have to set up more than one internet connection methods below for failover and load balancing to function.

**The Cellular Method**

If you already inserted the SIM card into your router, you should be connected to the internet automatically. (You should see the name of your SIM carrier and a light blue dot appear next to it.) If not, click the **Auto Setup** option if it appears. 

**Note:** If you are having issues using the cellular method, refer to the [Cellular Network Troubleshooting Guide](https://docs.gl-inet.com/router/en/4/faq/gl-x3000_gl-xe3000_connection_optimization/). 

**The Ethernet Method**

Connect an ethernet cable to your router's WAN port and an upstream device, such as a modem. If you are connected to the internet successfully, a light blue dot appears next to "Ethernet."

**The Repeater Method**

1. On the main screen of the admin panel, locate the "Repeater" section, then click **Connect**.
2. Select a Wi-Fi network. 
3. Enter the network password, then click **Apply**.

If you are connected to the internet successfully, a light blue dot appears next to the Wi-Fi network name. 

**The Tethering Method**

1. Connect your mobile device to the router's USB port using a 3.0 USB data transfer cable. 
2. In your mobile device's settings, enable tethering. 
3. On the main screen of the admin panel, click **Connect** in the "Tethering" section. 
If you are connected to the internet successfully, a light blue dot appears next to "Tethering."

---

## How to set up a VPN 

A VPN (virtual private network) creates a secure, encrypted traffic between your device and the VPN server. It provides an added layer of privacy and security (VPN client) and allows you to access a remote network (VPN server). 

Spitz AX (and other GL.iNet routers) support the OpenVPN and WireGuard protocols. Both protocols offer strong security, but Wireguard offers greater speeds and convenience. If you do not have a preference in which VPN protocol to use, you can use WireGuard. 

### OpenVPN 

To set up OpenVPN, follow these tutorials:

* [How to set up an OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
* [How to set up an OpenVPN server](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

### WireGuard

To set up WireGuard, follow these tutorials:

* [How to set up a WireGuard client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
* [How to set up a WireGuard server](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

---

## How to set up tailscale

Tailscale is a VPN service that allows you to access your devices and applications anywhere. To set up tailscale, refer to [Tailscale](https://docs.gl-inet.com/router/en/4/interface_guide/tailscale/). 

---

## How to set up multi-WAN (failover and load-balancing)

Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., cellular, repeater, and ethernet) at the same time. If your current internet connection fails, the router will automatically switch to another internet connection. This ensures smooth and uninterrupted internet access. 

To set up multi-WAN, refer to [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/). 

---

## How to set up port forwarding

Port forwarding allows remote servers and devices on the internet to access devices on a private network. To set up port forwarding, refer to [Port Forwards](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards). 

---

## Other Spitz AX features and settings

### AdGuard Home

AdGuard Home is a third-party tool that blocks ads and tracking to keep you safe. To learn how to enable AdGuard Home, refer to [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/). 

### Drop-in gateway 

Drop-in gateway extends the functionality of your main router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. To set up drop-in gateway, refer to [How to set up drop-in gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/). 

### Dynamic DNS

Dynamic DNS (DDNS) automatically detects and updates the IP address associated with a domain in real-time. It is most useful for users who need a static IP address for accessing a remote network. To set up dynamic DNS, refer to [Dynamic DNS](https://docs.gl-inet.com/router/en/4/interface_guide/ddns/). 

### Parental controls

Parental controls are a group of settings designed to help you manage and control your children's devices. They include limiting their screen time and restricting their access to certain content. Spitz AX offers two options for parental controls: the local version developed by GL.iNet and the integrated version from Bark, a parental controls app. 

To set up parental controls, refer to [Parental controls](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control). 

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

### Specifications

Refer to [Specifications](https://www.gl-inet.com/products/gl-x3000/#specs){target="_blank"}. 