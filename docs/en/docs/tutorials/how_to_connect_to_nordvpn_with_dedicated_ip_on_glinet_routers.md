# How to connect to NordVPN with a dedicated IP on GL.iNet routers?

This article introduces the steps to set up a NordVPN connection with a dedicated IP on GL.iNet routers.

We use the GL-AXT1800 as an example.

1. Log in to your Nord Account and check the dedicated IP details. As shown below, the assigned IP is **193.32.211.142**, and the server is **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Go to [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) and find the configuration file for **United Kingdom #1625**. Download the UDP or TCP configuration file.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Return to your Nord Account page, go to **Manual Setup** and click **Set up NordVPN Manually** to get your service credentials.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Log in to your router's web Admin Panel and go to **VPN** > **OpenVPN Client**. Create a new group to upload the configuration file you downloaded in Step 2. Then enter the service credentials you obtained in Step 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    1 valid configuration file has been detected. Please enter your username and password. If these configurations use different passwords, you will need to enter the corresponding password for each configuration file.

5. Click the three-dot icon on the right to connect. You may also go to **VPN Dashboard**, select the configuration file and click **Apply** to establish a connection.

6. Once connected, check your public IP [here](https://whatismyipaddress.com/) and confirm if it matches your dedicated IP from NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
