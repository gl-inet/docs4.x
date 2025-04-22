# How to Set Up Urban Shield VPN Client on GL.iNet Router

[Urban Shield VPN](https://urbanshieldvpn.com/) is a VPN provider dedicated to offering high-security and high-performance VPN solutions to global users. It provides pre-configured GL.iNet VPN routers and flexible subscription plans, ensuring secure and private browsing. Simply activate Urban Shield VPN on your router, you’re protected with access to their global servers, allowing you to browse and stream with peace of mind.

## Setup Guide

Follow the steps below to activate Urban Shield VPN on your router by setting it as WireGuard Client to enjoy secure Internet access.

### 1. Sign Up Urban Shield VPN Account

Visit [Urban Shield VPN official website](https://urbanshieldvpn.com/){class="_blank"} or click [here](https://payment.urbanshieldvpn.com/sign-up) to sign up an Urban Shield VPN account.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Power on and Connect

Power on your router. Connect a device to the router via an ethernet cable or via Wi-Fi.

### 3. Access Web Admin Panel

Follow the steps below to access the web Admin Panel. If you have logged in, please turn to the next part.

Open a web browser (we recommend Chrome, Edge, Safari) and visit [192.168.8.1](http://192.168.8.1). You will be directed to the initial setup of the web Admin Panel. If can't access the web Admin Panel, please check [here](cannot_access_web_admin_panel.md).

Choose a language, and click **Next** to continue.

Set up admin password, we recommend using a strong password. Click **Submit** to continue.

**Note**: Wi-Fi may turn off during the initialization, please make sure to reconnect to the router.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password.png){class="glboxshadow"}

### 4. Activate Urban Shield VPN

After login, select **VPN** from the left menu -> **WireGuard Client**. You will see a built-in Urban Shield VPN login page.

Input your **Email** and **Password**, then click **Save And Continue**. It will generate configuration files for each servers.

Select the server you prefer and click **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Then you will get the server(s) available.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Start a server.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.png){class="glboxshadow"}

Once connected, you will see a blue dot indicating successful connection.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.png){class="glboxshadow"}

In the VPN Dashboard, you will also see your user IP address and the number of Bytes send/received.

![vpn dashboard urbanshieldvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Edit credential or logout

Click the cog icon to edit the credential or logout.

![edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_credential_or_logout.png){class="glboxshadow"}

## Go renew

If you click **Go Renew**, it will pop up an edit window which allows you to renew your account.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.png){class="glboxshadow"}

## Delete 

Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.png){class="glboxshadow"}

---