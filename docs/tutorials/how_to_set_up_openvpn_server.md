# How to set up OpenVPN server on GL.iNet routers

This tutorial will show you **how to set up an OpenVPN server on GL.iNet routers**. A VPN server allows you to establish a secure connection to your home or office network remotely. With a GL.iNet router, you can set up your OpenVPN server in minutes. 

!!! note "Before you start, make sure to check the following requirements:"
    **A public IP address**

    Setting up an OpenVPN server requires a public IP address. To check if you have one, follow [these steps](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Port forwarding**

    If your GL.iNet router is connected to a primary router, you will have to [set up port forwarding on the primary router](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/).

## 1. Log in to your router

In a web browser, enter the URL (e.g., 192.168.8.1) to access the router admin panel. Enter your admin password, then click **Login**.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Set up Dynamic DNS (Optional)

Setting up an OpenVPN server typically requires a **static public IP address**, which provides a fixed endpoint for other devices to access your VPN server. However, most users do not have a static public IP address. In such cases, you can configure **Dynamic DNS (DDNS)** on your GL.iNet router. This allows persistent connectivity to the OpenVPN server even when your public IP address changes dynamically.

To set up Dynamic DNS, follow these steps: 

1. In the left sidebar, click **Applications** > **Dynamic DNS**. 
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Next to **Enable DDNS**, toggle the switch to on. 
3. Check the box for **I have read and agree to the Terms of Service & Privacy Policy**.
4. Click **Apply**. 
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Download configuration file

1. In the left sidebar, click **VPN** > **OpenVPN Server**.
2. Click **Generate Configuration**. 
3. Keep the default settings as-is, then click **Export Client Configuration**. 
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. In the pop-up page, if you set up **Dynamic DNS** previously, toggle the switch to on for **Use DDNS Domain**. 
5. Click **Download**, then save the file. 
6. At the top of OpenVPN Server page, click **Start**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Optional) To access the local network of the VPN server, enable these settings:"
    
    For firmware v4.7 and earlier:

    1. In the left sidebar, click **VPN** > **VPN Dashboard**. 
    2. Click the Options icon.
    3. Toggle the switch to on for **Remote Access LAN**.
    4. Click **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    For firmware v4.8 and higher:

    1. In the left sidebar, click **VPN** > **OpenVPN Server**.
    2. Click **Options** in the upper right.
    3. Toggle the switch to on for **Allow Remote Access the LAN Subnet**.
    4. Click **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. Connect to OpenVPN server

To connect to the OpenVPN server, you will need an OpenVPN client. You can set it up by using one of these methods below: 

??? "Method 1: A third-party OpenVPN client app (Use this method if you don't have an additional router that supports setting up an OpenVPN client)" 

    In this tutorial, we will use the OpenVPN Connect app, the official app developed by OpenVPN Inc, as an example. 

    1. On another device, connect to a different Wi-Fi network (or connect to cellular if you are using a mobile device.)
    2. Send the configuration file you downloaded earlier (e.g., by email) to the device, then download the file to it. 
    3. Download OpenVPN Connect for your device operating system:
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. In the app, read the terms and conditions, then select **Agree**. 
    5. Select **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Select **Browse**, then select the configuration file you downloaded previously. 
    7. Select **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"} 
    8. Select **Connect** > **OK** > **Allow**. 

    You will see the word "Connected" at the top of the VPN profile. 
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"} 

??? "Method 2: A router that supports setting up an OpenVPN client"

    You can use any routers that support setting up the OpenVPN client manual configuration. In this tutorial, we will use GL.iNet's travel router [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) as an example. 

    1. On another device, connect to a different Wi-Fi network (or connect to cellular if you are using a mobile device.). 
    2. In a web browser's address, enter the URL to your router admin panel (e.g., 192.168.8.1).
    3. Enter your password, then click **Login**. 
    4. In the left sidebar, click **VPN** > **OpenVPN Client**. 
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"} 
    5. Click **Add Manually**. 
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"} 
    6. Enter a name in the field, then click the check icon. 
    7. Upload the configuration file you downloaded earlier. 
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"} 
    8. Click **Apply**. 
    9. Click the three-dot icon, then click **Start**. 
    10. Connect a device to the router running the OpenVPN client. 

## 5. Check VPN connection

To check if you are successfully connected to the OpenVPN server, look up your public IP address. If it matches the one provided by the VPN server (not your Internet service provider), you are connected to the OpenVPN server successfully.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
