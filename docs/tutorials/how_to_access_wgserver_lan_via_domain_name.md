# How to access WireGuard Server LAN devices from the client side via domain names?

This tutorial introduces the steps to access your home devices (such as NAS, IP camera, etc.) on the WireGuard server from the client side using their domain names.

## Topology

As shown below, you can access devices such as NAS and IP camera on the WireGuard server's LAN from the PC on the client side via their domain names.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Setup steps

### 1. Edit Hosts on Server (Optional)

This step applies when your VPN server cannot resolve local domain names properly. Skip this step if you are unsure.

Log in to the web admin panel of your VPN server router, navigate to **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Input the IP and domain name of the home devices you want to access, then click **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Allow Remote Access LAN on Server

??? "For server router running firmware v4.8"

    On the server's web admin panel, navigate to **VPN** -> **WireGuard Server**. Click **Options** in the upper right corner.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Enable **Allow Remote Access the LAN Subnet**, and click **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **When enabled, this router and LAN devices can be accessed remotely via the VPN.**
 
??? "For server router running firmware v4.7 and earlier"

    On the server's web admin panel, navigate to **VPN** -> **VPN Dashboard** -> **VPN Server** section. Click the gear icon on the right side of the WireGuard server.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Enable **Remote Access LAN**, and click **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **When enabled, this router and LAN devices can be accessed remotely via the VPN.**

### 3. Export VPN Configuration

On the server's admin panel, navigate to **VPN** -> **WireGuard Server** -> **Profiles** tab, click **Add** to export a configuration profile. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

You will then get a **.conf** file, as shown below.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Open this file. Ensure that the DNS field in the file points to the server's tunnel IP, which is displayed under the **Configuration** tab of the WireGuard Server page, as shown below. Meanwhile, delete "64.6.64.6" from the DNS field if any to avoid DNS resolution failure.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Note**: The WireGuard server's tunnel IP varies from different firmware version. Please check your server's tunnel IP.

### 4. Enable VPN Server

On the **WireGuard Server** page, click the **Start** button in the upper right corner to start the server.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Upload VPN Configuration

Log in to the web admin panel of your VPN client router, navigate to **VPN** -> **WireGuard Client**, then click **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Create a name for this group and upload the configuration file.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Upload successful. Click **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

You will get a configuration file listed here.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Start VPN Client Connection

Click the three-dot icon to initiate the VPN connection. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

When the grey dot turns green, the WireGuard client has connected to the server successfully.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Now you can access your home devices (such as NAS) on the server's LAN from the PC on the client's LAN using their domain names.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
