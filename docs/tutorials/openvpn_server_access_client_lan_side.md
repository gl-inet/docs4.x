# How to visit OpenVPN client LAN side from Server

## The Topology of OpenVPN site to site tunnel

Visit the subnet of OpenVPN client (GL-MT2500), like NAS, printer, IP Cam......For example, Sub-router (GL-MT3000) with IP **192.168.48.211**

![ovpnlantop](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

### 1. Go to the VPN Dashboard of OpenVPN server

Click the icon and enter the custom rule page

![ovpnoption](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnoption.jpg){class="glboxshadow"}


### 2. Set up the custom rule

Input the subnet you wanted to visit, in this example the Target Address is **192.168.48.0/24**, Gateway **10.8.0.1** and input the Scope **global**

![ovpnrule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnrule.jpg){class="glboxshadow"}

### 3. Check the IP can be visited or not

![ovpnlan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlan.jpg){class="glboxshadow"}