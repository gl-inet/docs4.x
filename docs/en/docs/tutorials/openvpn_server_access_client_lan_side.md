# How to access OpenVPN client LAN side from Server

This tutorial introduces the steps to access the LAN subnet of OpenVPN client (such as NAS, IP camera, etc.) from your OpenVPN server side.

## Topology

As shown below, the GL-AXT1800 is an OpenVPN server and the GL-MT2500 is an OpenVPN client connected to it. You can access the devices on the GL-MT2500's LAN side (such as NAS or GL-MT3000, a sub-router) from the server side.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Add route rule on server

??? "For firmware v4.7 and earlier"

    Log in to the web admin panel of <u>your OpenVPN server</u>, and go to **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Click on the route icon on the right to enter the route rule.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    In the pop-up window, click on **Add Route Rule** button on the right side, and input the subnet you want to access.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    For example, the LAN subnet of the OpenVPN client GL-MT2500 is **192.168.48.0/24**, so the Target Address is **192.168.48.0/24**. 
    
    Gateway is the Client IP that your OpenVPN server generated for this OpenVPN client. Here we set the Gateway as **10.8.0.1**, then click **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Note: If you have multiple OpenVPN clients whose LAN subnets need to be accessed, please refer to [this link](reserve_fixed_IP_for_ovpn_client.md) to reserve a Client IP for each OpenVPN client before setting the route rules.

??? "For firmware v4.8 and higher"

    Log in to the web admin panel of <u>your OpenVPN server</u>, and go to **VPN** -> **OpenVPN Server**.

    Click the **Route Rules** tab, then click on **Add Route Rule** button on the right side.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    In the pop-up window, input the subnet you want to access.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    For example, the LAN subnet of the OpenVPN client GL-MT2500 is **192.168.48.0/24**, so the Target Address is **192.168.48.0/24**. 
    
    Gateway is the Client IP that your OpenVPN server generated for this OpenVPN client. Here we set the Gateway as **10.8.0.2**, then click **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Note: If you have multiple OpenVPN clients whose LAN subnets need to be accessed, please refer to [this link](reserve_fixed_IP_for_ovpn_client.md) to reserve a Client IP for each OpenVPN client before setting the route rules.

## 2. Allow remote access to client LAN

??? "For firmware v4.7 and earlier"

    Log in to the web admin panel of <u>your OpenVPN client</u>, and go to **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Click on the gear icon to enter the client options.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    In the pop-up window, enable **Remote Access LAN**, then click **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "For firmware v4.8 and higher"

    Log in to the web admin panel of <u>your OpenVPN client</u>, and go to **VPN** -> **VPN Dashboard**.

    On the top-left corner of your VPN tunnel, click the gear icon to enter the tunnel options.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    In the pop-up window, enable **Allow Remote Access the LAN Subnet**, then click **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Test connection

Here is an example of accessing the GL-MT3000 (a device in OpenVPN client's LAN) with IP **192.168.48.211**.

On a device connected to your OpenVPN server, ping GL-MT3000's IP address **192.168.48.211**. This is the IP address that OpenVPN client (GL-MT2500) assigns to the GL-MT3000 in its LAN.

If you can ping it successfully, it means the settings are correct. You will be able to access all other devices within the OpenVPN client LAN subnet through their IP addresses.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
