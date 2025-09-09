# How to access WireGuard client LAN side from Server

This tutorial introduces the steps to access the LAN subnet of WireGuard client (such as IP camera, NAS, etc.) from your WireGuard server side.

## Topology

As shown below, the GL-MT2500 is a WireGuard server and the GL-AXT1800 is a WireGuard client connected to it. You can access the devices on the GL-AXT1800's LAN side (such as IP camera or NAS) from the server side.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Add route rule on server

Log in to the web admin panel of your WireGuard server, then go to **VPN** -> **VPN Dashboard** -> **VPN server**.

Click on the route icon on the right to enter the route rule.

![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

Click **Add Route Rule** in the upper right corner, and input the subnet you want to access.

![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

For example, the LAN subnet of the WireGuard client GL-AXT1800 is **192.168.8.0/24**, so the Target Address is **192.168.8.0/24**. 
    
Gateway is the client IP that your WireGuard server generated for this WireGuard client. You can find it under the Profiles tab of **WireGuard Server** page. Here we set the Gateway as **10.0.0.4**. Set the Scope as **global**.
    
![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

## 2. Add allowed IP and get a new configuration

In the web admin panel of your WireGuard server, go to **WireGuard Server** -> **Profiles**, and you will find the client IP (Gateway) of GL-AXT1800. 

Click the gear icon on the right to modify configuration.

![gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/gateway.jpg){class="glboxshadow"}

Click **Set More**

![client config set more](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/client-config-set-more.jpg){class="glboxshadow"}

Click **+ Add New** under the Allowed IPs list.

![add new allowed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/add-new-allowed-ip.png){class="glboxshadow"}

Input the subnet of your WireGuard client, which is **192.168.8.0/24** in this case, then click **Apply** to get a new configuration

![get new config](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/get-new-config-file.png){class="glboxshadow"}

### 3. Upload the configuration and test connection

Upload the new configuration to your client router, which is the GL-AXT1800 in this case. Start the VPN connection and test if you can access the LAN devices of your WireGuard client from the Server side.

You can test the connection via ping. For example, on a device connected to the WireGuard server (GL-MT2500), ping the IP of a device in the LAN side of the WireGuard client (GL-AXT1800), and check if it can ping successfully.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}