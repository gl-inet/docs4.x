# My WireGuard Server is not Working

There are many reasons your own WireGuard server is not working after the first setup. Please follow the below guide and figure out the reason one by one.

## My WireGuard Client is starting and never connect

![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/client.jpg){class='glboxshadow'}

It may be due to your port forward is not done, to ensure your Main router port forward is functioning, you can try to forward a HTTPS port to DDNS function.

1. Go to your Main router and forward the port 443 to our GL-iNet Router, just like what you do when you set up the VPN servers. Here is the example if you are using TP-Link as the Main router.

    ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/DDNS1.jpg){class='glboxshadow'}

2. Enable the DDNS function in your GL-iNet Router

    ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/DDNS2.jpg){class='glboxshadow'}

3. Enable the HTTPS Remote Access

    ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/DDNS3.jpg){class='glboxshadow'}

4. Connect your Laptop or PC to another network or cellular network. Launch a Windows Browser and type the DDNS address **Https://abcd123.glddns.com** and click **Advance**

    ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/DDNS4.jpg){class='glboxshadow'}

5. Click Proceed to abcd123.glddns.com(unsafe)

    ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/DDNS5.jpg){class='glboxshadow'}

6. If you can access our GL-iNet Router admin login, your Main router port forward is functioning.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/My%20client%20is%20waiting/DDNS6.jpg){class='glboxshadow'}

## My WireGuard Server Shows Client connected but My Client cannot access to the internet

1. Your main router gateway IP is conflict with the WireGuard Server Virtual IP.

    Please see point 2 of [set up Wiregaurd Server](../interface_guide/wireguard_server.md/#setup-wireguard-server)

2. If you are using two GL.iNet Routers as the server and client, please change the LAN IP of either one. Change the [LAN IP](../interface_guide/lan.md).

3. You ISP cannot resolve your DNS. Please change the DNS on the configuration to **8.8.8.8** or **8.8.4.4**.

    ![dns8888](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/dns8888.jpg){class='glboxshadow'}

4. You have changed the Server Virtual IP yourself but you didn't put the **/24** and make it become **xx.x.x.x/24**.

    Please see point 2 of [set up Wiregaurd Server](../interface_guide/wireguard_server.md/#setup-wireguard-server)

## My WireGuard Server is connected but My Clients cannot connect to it

1.  Please check again your [port forwarding](my_wireguard_server_is_not_working.md#my-wireguard-client-is-starting-and-never-connect) is working. You can [test the Server](../interface_guide/wireguard_server.md/#to-check-if-wireguard-server-is-working-properly) by official WireGuard mobile App.

2.  Please double confirm you have a Public IP address. For details please click [here](../interface_guide/wireguard_server.md/#make-sure-internet-service-provider-assigns-you-a-public-ip-address).
3.  If you are using two GL.iNet routers as the server and the client, please change the LAN IP of either one. Change the [LAN IP](../interface_guide/lan.md).

4.  You are connecting your client to the server's WiFi or LAN port, please change to another network.

5.  You may missed some lines when you copy your configuration to the client.

6.  You may manually added the **Allowed IPs** into the configuration. Please add the **Allowed IPs** in [Server Profile](../tutorials/wireguard_server_access_to_client_lan_side.md/#2-go-to-the-wireguard-server-you-will-see-the-client-ip-gateway-in-profiles-and-click-the-modify-icon).

## My WireGuard Server is connected but the connection is not stable

1.  Change the [MTU](../interface_guide/vpn_dashboard.md/#vpn-client-options) from **1420** to a smaller value, like **1380**.

2.  Check your Main router if it has to enable the VPN passthrough function or not.

3.  Change the DNS on the [configuration.](my_wireguard_server_is_not_working.md/#my-wireguard-server-shows-client-connected-but-my-client-cannot-access-to-the-internet)

4.  Use [encrypted DNS](../interface_guide/dns.md/#dns-server-settings) on GL-Router.

## My WireGuard Server is suddenly not working

1.  It may due to a power outage, please check if your server is still on line by [Https Remote Access](my_wireguard_server_is_not_working.md/#my-wireguard-client-is-starting-and-never-connect) or [GoodCloud](../interface_guide/cloud.md).

2.  You didn't enable the DDNS before and the public IP address is changed.

3.  The port forwarding is failed for some unknow reasons, forward another port for a trial.
