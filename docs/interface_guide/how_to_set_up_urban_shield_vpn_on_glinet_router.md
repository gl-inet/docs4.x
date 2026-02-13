# How to Set Up Urban Shield VPN on GL.iNet Router

[Urban Shield VPN](https://urbanshieldvpn.com/) is a VPN provider dedicated to offering high-security and high-performance VPN solutions to global users. It provides pre-configured GL.iNet VPN routers and flexible subscription plans, ensuring secure and private browsing. Simply activate Urban Shield VPN on your router, you’re protected with access to their global servers, allowing you to browse and stream with peace of mind.

## Setup Guide

Here's an example of GL-B3000 to activate Urban Shield VPN by setting it as WireGuard Client. 

### 1. Sign Up Urban Shield VPN

Visit [Urban Shield VPN official website](https://urbanshieldvpn.com/){class="_blank"} or click [here](https://payment.urbanshieldvpn.com/sign-up) to sign up an Urban Shield VPN account.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Power on and Connect

Power on your router. Connect a device to the router via an ethernet cable or via Wi-Fi.

### 3. Access Web Admin Panel

Follow the steps below to access the web Admin Panel. If you have logged in, please turn to the [next part](#4-network-setup).

Open a web browser (Chrome, Edge, or Safari are recommended) and visit [192.168.8.1](http://192.168.8.1){target="_blank"}. You will be directed to the initial setup of the web Admin Panel, as shown below. Set up your admin password and click **Next** to continue.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Set up your Wi-Fi network. The page displays factory Wi-Fi details, including the Wi-Fi name (SSID) and password, which you can change or keep. If you change any Wi-Fi details, please reconnect your device to the updated Wi-Fi.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Then click **Next** to log in with your admin password.

### 4. Network Setup

There's a **Network Setup Wizard** in the top-right corner (available in firmware v4.7 and above). Please follow the wizard to configure your router for Internet access before setting up VPN.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Activate Urban Shield VPN

Select **VPN** from the left menu -> **WireGuard Client**. You will see a built-in Urban Shield VPN login page.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Input your **Email** and **Password**, then click **Save And Continue**. It will generate configuration files for each servers.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Select your preferred server and click **Apply**. 

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

The available server(s) will then appear in the list.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Click the three-dot icon to initiate the connection.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Once connected, a blue dot will appear to indicate a successful connection.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

You may also check the connection status on the VPN Dashboard.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Edit Account Info or Logout

Click the gear icon to edit the account information or logout.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Go renew

If you click **Go Renew**, it will jump to the official website to renew your subscription.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Delete 

You can delete all configuration files with one click, as well as the private key and public key.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---