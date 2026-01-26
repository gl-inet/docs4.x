# How to set up OpenVPN client on GL.iNet routers

This tutorial will show you **how to set up an OpenVPN client on GL.iNet routers**. 

Before you start, ensure you have an active subscription with a VPN service provider that supports OpenVPN manual configuration. [See a list of OpenVPN-compatible VPNs that are supported by GL.iNet](https://www.gl-inet.com/solutions/vpn/). 

The following instructions guide you through setting up an OpenVPN client via the router admin panel. (To set up an OpenVPN client via the GL.iNet mobile app, [download the app](https://www.gl-inet.com/app/) and set it up.)

## 1. Log in to your router

In a web browser, enter the URL (e.g.,192.168.8.1) to access the router admin panel. Enter your admin password, then click **Login**. 

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Set up VPN client

Refer to the section appropriate to the VPN service provider you are using. 

??? "NordVPN"

    1. In the left sidebar, click **VPN** > **OpenVPN Client**.

    2. Click **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Enter your service credentials, then click **Save and Continue**. 

        Note: It is NOT the login account email/password, but the service credentials obtained from NordVPN website -> Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. In the prompt, select the VPN locations you want to connect, then click **Apply**. 

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Select the VPN server you want to connect to, click the three-dot icon and **Start**. 

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Other VPN service providers (E.g., Surfshark)"

    1. In the left sidebar, click **VPN** > **OpenVPN Client**.

    2. Click **Add Manually**. 

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Set a name. You can enter the name of your VPN service provider, then click the check icon. 

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Ensure you have downloaded the configuration file provided by your VPN service provider, and the service credentials if any.  
    5. Upload the configuration file you downloaded. 
    
        Enter the service credentials if required, then click **Apply**. 

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Next to the VPN server address, click the three-dot icon and **Start**. 

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Check VPN connection

In a web browser, search your IP address location. If it matches the VPN server location you are connected to, the VPN connection is successful.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
