# Use WireGuard to Secure RDP from Outside Network

You may need to remote access your PC from outside network or vice versa. The most secure way is access it with your own WireGuard tunnel. It gives you more security than use the port forwarding and access through your public IP address. After you setup the tunnel, you can use the **Remote Desktop App** of Window to access your PC anywhere.

## Topology

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Setup your own Wireguard Network

You need to setup your own WireGuard Server and WireGuard Clinet before you can use the WireGuard Tunnel for RDP. You can setup the tunnel with two GL.iNet Routers. [Build your Own Home Wireguard Server two GL.iNet Routers](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Allow your Server access to the Client LAN side

If you want to mutual access from both server and client, you need to allow your server access to the client LAN side first. [Accessing Client LAN from Server](wireguard_server_access_to_client_lan_side.md).

## Allow your Client access to the Server LAN side
After that please enable “Allow Remote LAN Access” on both the VPN Dashboards of the server and the client. For details, Client-side please click [here](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options); Server-side please click [here](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Setup the Server side PC Become Accessable

### Server Side PC

If you want to access the PC attaches to your Server LAN side with the IP **192.168.29.123**, please go to the Window Settings of that PC and click on **Remote Desktop**.

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Turn on it

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Click **Confirm**

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Start up Remote App at Client Laptop

### Client side Laptop

Search the **Remote Desktop Connection App**

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Launch it and type the Server side PC IP **192.168.29.123** into the box.

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Input the credentials of your Server side PC.

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

You will immediately remotely controlling your Server side PC.

If you want to do vice versa, just reverse the steps of Server PC and Client Laptop.
