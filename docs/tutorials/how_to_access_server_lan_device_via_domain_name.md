# How to access WireGuard Server LAN device via domain name from the client side?

This tutorial introduces the steps to access your home devices (such as NAS, IP camera, etc.) on your WireGuard server side by their domain names from the client side.

## Topology

As shown below, you can access the devices such as NAS and IP camera on the WireGuard server’s LAN via their domain names from the client side.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_mt6000_axt1800.png){class="glboxshadow"}

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

### 3. Export VPN Configuration Profile

In the server's admin panel, go to **VPN** -> **WireGuard Server** -> **Profiles** tab, export a configuration profile. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

You will obtain a file with the **.conf** extension, as shown below.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Open this **.conf** file. Verify that the DNS field in the file points to the server’s tunnel IP, which is displayed under the Configuration tab of the WireGuard Server page. 

Delete the “64.6.64.6” at the end of DNS field if any.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.jpg){class="glboxshadow"}

### 4. Upload Configuration File  

Log in to the web admin panel of your VPN client router, navigate to **VPN** -> **WireGuard Client**, click on **Add Manually**, then upload the configuration file.

### 5. Start VPN Connection

In the client’s VPN Dashboard, start the VPN connection. 

When your client connects to the VPN server successfully, you will be able to access your home devices on the server’s LAN by their domain names from the VPN client.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}
