# How to access WireGuard client LAN side from Server

This tutorial introduces the steps to access the LAN subnet of WireGuard client (such as IP camera, NAS, etc.) from your WireGuard server side.

## Topology

As shown below, the GL-MT2500 is a WireGuard server and the GL-AXT1800 is a WireGuard client connected to it. You can access the devices on the GL-AXT1800's LAN side (such as IP camera or NAS) from the server side.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Add route rule on server

??? "For firmware v4.7 and earlier"

    Log in to the web admin panel of <u>your WireGuard server</u>, then go to **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Click on the route icon on the right to enter the route rule.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Click **Add Route Rule** in the upper right corner, and input the subnet you want to access.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    For example, the LAN subnet of the WireGuard client GL-AXT1800 is **192.168.8.0/24**, so the Target Address is **192.168.8.0/24**. 
    
    Gateway is the client IP that your WireGuard server generated for this WireGuard client. You can find it under the **Profiles** tab of **WireGuard Server** page. As shown below, the client IP for the WireGuard client GL-AXT1800 is **10.0.0.4**.
    
    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}
    
    So set the Gateway as **10.0.0.4**, and the Scope as **global**, then click **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "For firmware v4.8 and higher"

    Log in to the web admin panel of <u>your WireGuard server</u>, then go to **VPN** -> **WireGuard Server**.

    Click the **Route Rules** tab, and click **Add Route Rule** on the right side.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    In the pop-up window, input the subnet you want to access.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    For example, the LAN subnet of the WireGuard client GL-AXT1800 is **192.168.8.0/24**, so the Target Address is **192.168.8.0/24**. 
    
    Gateway is the client IP that your WireGuard server generated for this WireGuard client. You can find it under the **Profiles** tab on the same page. As shown below, the client IP for the WireGuard client GL-AXT1800 is **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    So set the Gateway as **10.1.0.2**, then click **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Allow remote access to client LAN

??? "For firmware v4.7 and earlier"

    Log in to the web admin panel of <u>your WireGuard client</u>, and go to **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Click on the gear icon on the right side of WireGuard.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    In the pop-up window, enable **Remote Access LAN**, then click **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "For firmware v4.8 and higher"

    Log in to the web admin panel of <u>your WireGuard client</u>, and go to **VPN** -> **VPN Dashboard**.

    On the top-left corner of your VPN tunnel, click the gear icon to enter the tunnel options.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    In the pop-up window, enable **Allow Remote Access the LAN Subnet**, then click **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Test connection

Test if you can access the LAN devices of your WireGuard client from the Server side.

You can test the connection via ping. For example, on a device connected to the WireGuard server (GL-MT2500), ping the IP address of a device within the LAN of your WireGuard client (GL-AXT1800), and check if it can ping successfully.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
