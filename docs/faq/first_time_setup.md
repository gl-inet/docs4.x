# First time setup

The first-time setup of the GL.iNet router is very similar. Most models have a Wi-Fi module, while some do not. 

Therefore, the following guidance is divided into two cases based on the presence of a Wi-Fi module.

* [For models that have Wi-Fi](#for-models-that-have-wi-fi)
* [For models that don't have Wi-Fi](#for-models-that-dont-have-wi-fi)

## For models that have Wi-Fi

Here is an example of GL-AXT1800 (Slate AX).

Please prepare the following items included in the package.

- GL-AXT1800
- A power adapter
- An Ethernet cable

Watch this video guide or follow the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses a different GL.iNet router to demonstrate the setup, as the steps are the same for most router models.)</small>

1. Power on

    If you want to use TF card, please insert before powering on the router. Hot-swapping TF cards is not supported.

    Plug one end of the power adapter into the router and the other end into an outlet. It will automatically power on.

2. Connect to the router

    You can connect to router via an ethernet cable or via Wi-Fi.

    * Connect via cable

        Connect your computer to the LAN port of the router via Ethernet cable.

    * Connect via Wi-Fi

        The Wi-Fi SSID is printed on the router's bottom label in the following formats:

        **GL-AXT1800-XXX** or **GL-AXT1800-XXX-5G**

        The default Wi-Fi Key is located below the SSID. 

        Search for the router's SSID on your computer, phone, or tablet, then enter the Wi-Fi Key. For some models, if the Wi-Fi password is not found on the label, please try "**goodlife**".

        **Tip:** The QR code on the bottom label contains the default Wi-Fi information. You can connect quickly by scanning it with your phone's QR code scanner.

        **Note:** After connecting to the Wi-Fi, you may not have immediate Internet access. Please follow the next step to configure your network first before accessing the Internet.

3. Log in to the web Admin Panel

    Open a web browser (we recommend Chrome, Edge, or Safari) and visit [http://192.168.8.1](http://192.168.8.1). You will be directed to the initial setup of the web Admin Panel. 
    
    If you cannot access the web Admin Panel, please check [here](cannot_access_web_admin_panel.md).

    Choose a language, and click **Next** to continue.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    Set up admin password. We recommend using a strong password. Click **Apply** to continue.

    **Note**: Wi-Fi may turn off during the initialization, please make sure to reconnect to the router.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

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

    Plug one end of the power adapter into the router and the other end into an outlet. The router will power on automatically.

2. Connect to the router

    We can connect to router via an Ethernet cable or via Wi-Fi.

    * Direct connection via Ethernet cable

        Connect your computer to the LAN port of the router using an Ethernet cable. This is the recommended configuration method as it's simple and straightforward.

    * Connect via Wi-Fi of another router

        As GL-MT2500A doesn't have a built-in Wi-Fi module, we can use another router with Wi-Fi capability to initialize the GL-MT2500A.

        * Method 1: Set the second router in AP (Access Point) mode, then connect the LAN port of GL-MT2500A to the WAN port of the second router.

        * Method 2: Keep the second router in default router mode, but with a different router IP address that is not conflict with 192.168.8.1/24, e.g., 192.168.10.1. Then connect the LAN port of GL-MT2500A to the WAN port of the second router.

        Use your computer or smartphone to connect to the Wi-Fi of the second router.

        !!! Note
        
            The second router mentioned here is a regular router, like GL.iNet GL-AXT1800, TP-LINK, or Netgear routers. Modems, Optical Network Terminals, or devices provided by ISPs may not work in this scenario.

3. Access the web Admin Panel

    Open a web browser (we recommend Chrome, Edge, Safari) and visit [http://192.168.8.1](http://192.168.8.1). You will be directed to the initial setup of the web Admin Panel. If can't access the web Admin Panel, please check [here](cannot_access_web_admin_panel.md).

    Choose a language, and click **Next** to continue.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Set up admin password. We recommend using a strong password. Click **Submit** to continue.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    After the initial setup, you will enter the web Admin Panel of the router.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. Connect to the Internet

    * [Connect to the Internet via an ethernet cable](../interface_guide/internet_ethernet.md)
    * [Connect to the Internet via usb tethering](../interface_guide/internet_tethering.md)
    * [Connect to the Internet via usb modem](../interface_guide/internet_cellular.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
