# How to access OpenVPN client LAN side from Server

This tutorial introduces the steps to access the LAN subnet of OpenVPN client (such as NAS, IP camera, etc.) from your OpenVPN server side.

## Topology

As shown below, the GL-AXT1800 is an OpenVPN server and the GL-MT2500 is an OpenVPN client connected to it. You can access the devices on the GL-MT2500's LAN side (such as NAS or GL-MT3000, a sub-router) from the server side.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Add route rule on server

Log in to the web admin panel of your OpenVPN server, go to **VPN** -> **VPN Dashboard** -> **VPN server**.

Click on the route icon on the right to enter the route rule.

![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

Click **Add Route Rule** in the upper right corner, and input the subnet you want to access.

![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

For example, the LAN subnet of the OpenVPN client GL-MT2500 is **192.168.48.0/24**, so the Target Address is **192.168.48.0/24**. 
    
Gateway is the client IP that your OpenVPN server generated for this OpenVPN client. Here we set the Gateway as **10.8.0.1**, and set the Scope as **global**.

![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

## 2. Test connection

Here is an example of accessing the sub-router (GL-MT3000) with IP **192.168.48.211**.

On a device connected to your OpenVPN server, open a browser and enter **192.168.48.211**. This is the IP address that OpenVPN client (GL-MT2500) assigns to the sub-router (GL-MT3000) in its LAN.

If you can successfully access it, it means the settings are correct. You will be able to access all other devices within the OpenVPN client LAN subnet through their IP address.

![ovpnlan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlan.jpg){class="glboxshadow"}