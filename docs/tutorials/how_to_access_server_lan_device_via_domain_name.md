# How to access WireGuard Server LAN device via domain name from the client side?

This tutorial introduces the steps to access your home devices (such as NAS, IP camera, etc.) on your WireGuard server side by their domain names from the client side.

## Topology

As shown below, you can access the devices such as NAS and IP camera on the WireGuard server’s LAN via their domain names from the PC on the client side.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Setup Steps

### 1. Edit Hosts on Server

Log in to the web admin panel of your VPN server router, navigate to **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Input the IP and domain name of the home devices you want to access, then click **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Allow Remote Access LAN on Server

??? "For server router running firmware v4.8"

    In your server's admin panel, go to **VPN** -> **WireGuard Server**, click **Options** at the upper right corner.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Enable **Allow Remote Access the LAN Subnet**, and click **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Once enabled, it means allowing remote access to this router (tunnel IP) and LAN devices through the VPN.**
 
??? "For server router running firmware v4.7 and earlier"

    In your server's admin panel, go to **VPN** -> **VPN Dashboard** -> **VPN Server** section. Click the cog icon at the right side of the WireGuard server.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Enable **Remote Access LAN**, and click **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Once enabled, resources inside the LAN subnet of the WireGuard Server can be accessed through the VPN tunnel.**

### 3. Export VPN Configuration

In the server's admin panel, go to **VPN** -> **WireGuard Server** -> **Profiles** tab, export a configuration profile. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

You will obtain a file with the **.conf** extension, as shown below.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Open this **.conf** file. Ensure that the DNS field in the file points to the server’s tunnel IP, which is displayed under the Configuration tab of the WireGuard Server page, as shown below.

Delete "64.6.64.6" from the DNS field if any to avoid DNS resolution failure.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Note**: The WireGuard server's tunnel IP varies from different firmware version. Please check your server’s tunnel IP.

### 4. Enable VPN Server

In the **WireGuard Server** page, start the server.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Upload VPN Configuration

Log in to the web admin panel of your VPN client router, navigate to **VPN** -> **WireGuard Client**, click on **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Create a name for this new group and upload the configuration file.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Upload successful. Click **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

You will get a configuration file listed here.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 5. Start VPN Client Connection

Click the three-dot icon to start the VPN connection. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

When the grey dot turns to green, it means the WireGuard client is connected to your WireGuard Server successfully.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Now you can access your home devices (such as NAS) on the server’s LAN via their domain names from the PC on the client's LAN.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}
