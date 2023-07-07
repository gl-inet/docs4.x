# How to visit WireGuard client LAN side from Server

## The Topology of WireGuard site to site tunnel

If you want to visit the subnet of **192.168.8.1** **(GL-AXT1800)** at the client side, like NAS, IP Cam...

![Topology](https://static.gl-inet.com/docs/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}


### 1. Go to the VPN Dashboard of the Server

Click the icon and enter the custom rule page
![Custom rule](https://static.gl-inet.com/docs/en/4/tutorials/wiregaurd_server_access_client_lan_side/Custom%20rule.jpg){class="glboxshadow"}

Input the subnet you wanted to visit, in this case is **192.168.28.0/24** and type in the scope **global**.

Gateway is the WireGuard IP of your client router, you can find it at your **WireGuard Server** page.

![addrule](https://static.gl-inet.com/docs/en/4/tutorials/wiregaurd_server_access_client_lan_side/addrule.jpg){class="glboxshadow"}

### 2. Go to the **WireGuard Server** then **Profiles** and click the modify icon

![Gateway](https://static.gl-inet.com/docs/en/4/tutorials/wiregaurd_server_access_client_lan_side/Gateway.jpg){class="glboxshadow"}

Click **Set More**

![Setup](https://static.gl-inet.com/docs/en/4/tutorials/wiregaurd_server_access_client_lan_side/setup.jpg){class="glboxshadow"}

Click **+** to add the allow IP and then click **Apply** to get a new configuration

![allowip](https://static.gl-inet.com/docs/en/4/tutorials/wiregaurd_server_access_client_lan_side/allowip.jpg){class="glboxshadow"}

### 3. Download the configuration 

Load the configuration to your client router **192.168.8.1** in this case is the GL-AXT1800
