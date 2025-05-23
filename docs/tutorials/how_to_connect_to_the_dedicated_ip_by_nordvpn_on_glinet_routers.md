# How to connect to the dedicated IP by NordVPN on GL.iNet routers?

This article introduces the steps to set up the dedicated IP by NordVPN. 

Here we take GL-AXT1800 as an example. 

1. Log in to your Nord Account and check the dedicated IP info. As the following picture shows, the assigned IP is **193.32.211.142** and the server info is **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Go to this link: [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) and find the config file of **United Kingdom #1625**. Download the UDP or TCP config file as you want.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Back to the Nord Account page, go to Manual setup and click on **Set up NordVPN Manually** to get the service credentials.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Log in to the web Admin Panel of your router, go to **VPN** > **OpenVPN Client**, create a new group to upload the config file you downloaded in step 2. Then type in the service credentials you got in step 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

5. Go to **VPN Dashboard**, select the config file and click on **Apply** to connect to it.

    ![connect nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/connect_nordvpn_on_glinet_router.png){class="glboxshadow"}

6. When it is connected, you can check your public IP here: [https://whatismyipaddress.com/](https://whatismyipaddress.com/) and confirm if it matches with the dedicated IP by NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
