# How to visit WireGuard client LAN side from Server

## The Topology of WireGuard site to site tunnel

Visit the subnet of WireGuard client(GL-AXT1800) like NAS, IP Cam... For Example IP Cam **192.168.8.160** 

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}


### 1. Go to the VPN Dashboard of the Server

Click the icon and enter the custom rule page
![Custom rule](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Custom%20rule.jpg){class="glboxshadow"}

Input the subnet you wanted to visit, in this case is **192.168.8.0/24** and type in the scope **global**.

Gateway is the WireGuard IP of your client router, you can find it at your **WireGuard Server** page.

![addrule](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/addrule.jpg){class="glboxshadow"}

### 2. Go to the **WireGuard Server** you will see the client IP (Gateway) in **Profiles** and click the modify icon

![gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/gateway.jpg){class="glboxshadow"}

Click **Set More**

![Setup](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/setup.jpg){class="glboxshadow"}

Click **+** to add the allow IP and then click **Apply** to get a new configuration

![allowip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/allowip.jpg){class="glboxshadow"}

### 3. Download the configuration 

Load the configuration to your client router, in this case is the GL-AXT1800

You can test the settings by ping from **GL-MT2500**(Server) to **192.168.8.160** (IP Cam under Client GL-AXT1800)

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}