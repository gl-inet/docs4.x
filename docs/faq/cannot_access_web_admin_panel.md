# Can't access web Admin Panel

Sometimes you may be unable to access [http://192.168.8.1](http://192.168.8.1) to login web Admin Panel, there maybe several reasons.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## The possible causes

* You computer or mobile phone doesn't connect to the router.
* 192.168.8.1 is the default IP address of the router, you may have changed this IP.
* The cache or extension of browser may cause inaccessible.
* You are using a VPN client which handle your LAN traffic.
* The router is bricked.

## Check the general steps to access web Admin Panel 

1. Power up the router without connecting to any device.
2. Use your mobile/laptop to scan the SSID GL-XXXX-xxx and input the WiFi key printed on the router label. (If you are using a laptop, don't connect it to the internet by other methods)
3. If step 2 fails, turn off wifi on your computer/laptop, connect it to the router's LAN port via an Ethernet cable instead.
4. Open a browser, type `192.168.8.1` in the address bar. You should be able to visit GL.iNet web Admin Panel.

Or you can use [the app](mobile_app.md) to access the router.

## Other steps to fix this issue

1. [Check the connection](#check-the-connection)
2. [Check router's IP address](#check-routers-ip-address)
3. [Access the router's IP address](#access-the-routers-ip-address)

---

### Check the connection

If connected by ethernet cable, make sure your WAN/LAN port connection is correct. WAN port is connected to an Internet source and LAN port is connected to devices.

If connected by Wi-Fi, make sure the SSID is correct.

### Check router's IP address

Then follow the steps below to check the router's IP address.

=== "Windows 10 / Windows 11"

    Access Control Panel, please make sure the top right corner is a View by Large icons or Small icons.

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    Control Panel -> Network and Share Center -> Click the connection. You may have multiple connections, please choose the corresponding connections of the router you want to check.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    It will pop up a dialog of the status of the connection. Click the detail button.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    It will pop up a dialog of network connection detail, the IP address of router is the **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings

    Right click the network -> Status -> Details
    
    The IP address of router is the **IPv4 Default Gateway**
    
    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. System Preferences -> Network

    2. In the left column, click on the network connection. For an Ethernet connection, the router IP address will be shown.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    For a Wi-Fi connection, click the "Advanced..." button, and then the "TCP/IP" tab on the top of the windows. The router IP address will be shown.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Settings -> Wi-Fi
    2. Tap the information icon(blue i, in a circle) of current connected Wi-Fi. The router IP address will be shown.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    This will vary from different Android device.

    1. Settings -> Network & internet
    2. Tab on Wi-Fi and find the network you are connected to, click on the settings icon to manage its settings
    3. Tap on the Advanced dropdown. If if offers you options for Static or Dynamic IPs, select Static
    4. Either way, you should see your router's IP under Gateway.

### Access the router's IP address

1. Make sure you are using Chrome/Edge/Safari, then try to access your IP address again.
2. In order to avoid problems caused by the browser cache and extension, please open the incognito window. Then try to access the IP address of router again.
3. If you are using a VPN, please turn off then try again.
4. If you are using a mobile phone, please turn off the mobile data. Some phones will use mobile data instead of WiFi if the router can't access Internet.
5. If above steps failed, try [Reset](repair_network_or_reset_firmware.md#reset-to-factory) to back to factory default.
6. If the reset doesn't work, you can try [Debrick via uboot](debrick.md).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com/t/gl-inet-launches-esim-cards-for-routers/47351){target="_blank"}.