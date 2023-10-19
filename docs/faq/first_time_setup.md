# First time setup

The first time setup of the GL.iNet router is very similar. Most of the models have Wi-Fi module, some models do not have Wi-Fi module, the following is divided into two cases according to the availability of Wi-Fi module.

* [For models that have Wi-Fi](#for-models-that-have-wi-fi)
* [For models that don't have Wi-Fi](#for-models-that-dont-have-wi-fi)

## For models that have Wi-Fi

Here is an example of GL-AXT1800 (Slate AX).

Please prepare the following items that included in the package.

GL-AXT1800, power adapter, ethernet cable.

There is a video guide.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f7DYULL6ZSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Power on

    If you want to use TF card, please insert before powering on the router. Hot plugging for TF card is not supported.

    Plug one end of the power adapter into the router and the other end into an outlet. It will automatically power on.

2. Connect to the router

    You can connect to router via an ethernet cable or via Wi-Fi.

    * Connect via cable

        Connect your computer to the LAN port of the router via Ethernet cable.

    * Connect via Wi-Fi

        The SSID was printed on the bottom label of the router with the following formats:

        **GL-AXT1800-XXX** or **GL-AXT1800-XXX-5G**

        Search for the SSID of the router in your computer/phone/tablet and input the WiFi password. Please find the WiFi password on the label on the back of the router. Some models if you can't find the WiFi password on the label, please try the default password **goodlife**.

        **Tip:** The QR code on the label on the back of the GL-AXT1800 is with wifi connection information and can be quickly connected using your phone's QR code scanning tool.

        **Note:** At this time, you cannot access the Internet after connecting to the WiFi, you need to set up the admin password in the next step before you can access the Internet.

3. Access the web Admin Panel

    Open a web browser (we recommend Chrome, Edge, Safari) and visit [http://192.168.8.1](http://192.168.8.1). You will be directed to the initial setup of the web Admin Panel. If can't access the web Admin Panel, please check [here](cannot_access_web_admin_panel.md).

    Choose a language, and click **Next** to continue.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    Set up admin password, we recommend using a strong password. Click **Submit** to continue.

    **Note**: Wi-Fi may turn off during the initialization, please make sure to reconnect to the router.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password.png){class="glboxshadow"}

    After the initial setup, you will enter the web Admin Panel of the router.

    ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. Connect to the Internet

    * [Connect to the Internet via an ethernet cable](../interface_guide/internet_ethernet.md)
    * [Connect to the Internet via an existing Wi-Fi](../interface_guide/internet_repeater.md)
    * [Connect to the Internet via usb tethering](../interface_guide/internet_tethering.md)
    * [Connect to the Internet via usb modem](../interface_guide/internet_cellular.md)

## For models that don't have Wi-Fi

Here is an example of GL-MT2500A (Brume 2).

1. Power on

    Plug one end of the power adapter into the router and the other end into an outlet. It will automatically power on.

2. Connect to the router

    You can connect to router via an ethernet cable or via Wi-Fi.

    * Connect via cable

        Connect your computer to the LAN port of the router via Ethernet cable.

    * Connect via Wi-Fi by another router

        As GL-MT2500A doesn't have a build-in Wi-Fi module, we can use another router to initialize the GL-MT2500.

        * Method 1, the second router is set to AP(Access Point) mode, then connect the LAN port of GL-MT2500A to the WAN port of the second router.

        * Method 2, the second router is default router mode, but with a different router IP address that is not conflict with 192.168.8.1/24, e.g., 192.168.10.1, then connect the LAN port of GL-MT2500A to the WAN port of the second router.

        Use your computer or smartphone to connect to the Wi-Fi of the second router.

3. Access the web Admin Panel

    Open a web browser (we recommend Chrome, Edge, Safari) and visit [http://192.168.8.1](http://192.168.8.1). You will be directed to the initial setup of the web Admin Panel. If can't access the web Admin Panel, please check [here](cannot_access_web_admin_panel.md).

    Choose a language, and click **Next** to continue.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Set up admin password, we recommend using a strong password. Click **Submit** to continue.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    After the initial setup, you will enter the web Admin Panel of the router.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. Connect to the Internet

    * [Connect to the Internet via an ethernet cable](../interface_guide/internet_ethernet.md)
    * [Connect to the Internet via usb tethering](../interface_guide/internet_tethering.md)
    * [Connect to the Internet via usb modem](../interface_guide/internet_cellular.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
