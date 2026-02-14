# How to access OpenVPN Server LAN devices from the client side via domain names?

This tutorial introduces the steps to access your home devices (such as NAS, IP camera, etc.) on the OpenVPN server from the client side using their domain names.

## Topology

As shown below, you can access devices such as NAS and IP camera on the OpenVPN server's LAN from the PC on the client side via their domain names.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Setup steps

### 1. Edit Hosts on Server (Optional)

This step applies when your VPN server cannot resolve local domain names properly. Skip this step if you are unsure.

Log in to the web admin panel of your VPN server router, navigate to **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Input the IP and domain name of the home devices you want to access, then click **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Allow Remote Access LAN on Server

On the server's web admin panel, navigate to **VPN** -> **OpenVPN Server**. Click **Options** at the upper right corner.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Enable **Allow Remote Access the LAN Subnet**, and click **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

When enabled, the router and LAN devices can be accessed remotely via the VPN.

### 3. Export VPN Configuration

On the server's admin panel, navigate to **VPN** -> **OpenVPN Server** -> **Configuration** tab, click **Export Client Configuration** at the bottom. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

In the pop-up window, click **Export**. 

**Note**: If the public IP address on your server is dynamic and changes from time to time, please go to **APPLICATIONS** -> **Dynamic DNS** to enable **DDNS** before exporting the client configuration.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

You will then get a **.ovpn** file, as shown below.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

If your server router runs firmware v4.8 or later, no need to edit the configuration file; proceed to the next step.

If your server router runs firmware v4.7 or earlier, open this file, add the following line to set the DNS server to your OpenVPN server's tunnel IP, then save your changes.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Tip: The OpenVPN server's tunnel IPv4 subnet can be found under the **Configuration** tab of the OpenVPN Server page, as shown below. It varies by firmware version. Please check your OpenVPN server's tunnel IP.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Enable VPN Server

On the **OpenVPN Server** page, click the **Start** button in the upper right corner to start the server.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Upload VPN Configuration

Log in to the web admin panel of your VPN client router, navigate to **VPN** -> **OpenVPN Client**, then click **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Create a name for this group and upload the configuration file.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Upload successful. Click **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

You will get a configuration file listed here.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Start VPN Client Connection

Click the three-dot icon to initiate the VPN connection. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

When the grey dot turns green, the OpenVPN client has connected to the server successfully.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Now you can access your home devices (such as NAS) on the server's LAN from the PC on the client's LAN using their domain names.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
