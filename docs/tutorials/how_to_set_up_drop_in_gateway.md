# How to set up drop-in gateway on a GL.iNet router

GL.iNet offers the drop-in gateway feature, which enhances the functionality of your primary router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. By using this feature, you can keep using your primary router as usual while enjoying additional features. 

You can enable drop-in gateway for [all your devices](#enable-drop-in-gateway-for-all-devices) or [specific devices](#enable-drop-in-gateway-for-specific-devices) connected to your primary router. Follow the appropriate section for your setup.

**Note**: Models with firmware versions below v4.5.0 only supports enabling drop-in gateway for all devices. When drop-in gateway is enabled, all client devices will be networked through drop-in gateway, which means all traffic from connected clients is first handled by this router.

---

## Enable drop-in gateway for all devices

### 1. Connect GL.iNet router to the main router

Connect the WAN port of the GL.iNet router to the LAN port of the main router with an ethernet cable.

### 2. Enable drop-in gateway 

There are two methods to enable drop-in gateway: through the router admin panel or the GL.iNet mobile app. 

??? "Using web admin panel"

    1. In a web browser, enter `192.168.8.1`.  

    2. Enter your password, then click **Login**. 

    3. In the left sidebar, click **Network** > **Drop-in Gateway**. 

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Next to **Enable Drop-in Gateway Mode**, toggle the switch to on. 

    5. Select **All devices are networked through drop-in gateway**. 

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Click **Apply**. 

??? "Using GL.iNet mobile app"

    **Note:** Before you start, install the GL.iNet mobile app on your device. 

    1. On the main app screen, tap the **System** tab > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tap **Enable**. 

    3. For **Devices are networked via drop-in gateway**, tap **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Tap **Done**. 

### 3. Disable DHCP server on the main router

Please log in to your primary router to disable the DHCP server. You may refer to the instructions provided by your router manufacturer or contact their support. 

### 4. Set up AdGuard, DNS, VPN, and other features

Follow these guides to enable the features you want on your GL.iNet router.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

## Enable drop-in gateway for specific devices

### 1. Connect GL.iNet router to the main router

Connect the WAN port of the GL.iNet router to the LAN port of the main router with an ethernet cable.

### 2. Enable drop-in gateway

There are two methods to enable drop-in gateway: through the [router admin panel](#using-web-admin-panel) or the [GL.iNet mobile app](#using-glinet-mobile-app). 

??? "Using web admin panel"

    1. In a web browser, enter `192.168.8.1`. 

    2. Enter your password, then click **Login**. 

    3. In the left sidebar, click **Network** > **Drop-in Gateway**. 

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Next to **Enable Drop-in Gateway Mode**, toggle the switch to on. 
    
    5. Select **Some devices select their own networking gateway**. 

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Click **Apply**. 

    **Note:** Please Do NOT close this tab. You will need to enter the IP address (shown on the screen) in the next step.

??? "Using GL.iNet mobile app"

    **Note:** Before you start, install the GL.iNet mobile app on your device. 

    1. On the main app screen, tap the **System** tab > **Drop-in Gateway**.
    
        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}
    
    2. Tap **Enable**. 
    
    3. For **Devices are networked via drop-in gateway**, tap **part**.
    
        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Tap **Done**. 

    **Note:** Please Do NOT close this tab. You will need to enter the IP address (shown on the screen) in the next step. 

### 3. Set gateway and DNS on specific device

??? "Windows"
    
    1. Connect your device to the main router. 
    2. On your Windows, open **Settings** > **Network & Internet**.
    3. Based on your connection method, follow these steps: 
        * Ethernet: Click **Ethernet**. 
        * Wi-Fi: Click **Wi-Fi**, then click the Wi-Fi network name. 
    4. Copy the IPv4 address. Next to **IP assignment**, click **Edit**. 
    5. Click **Manual**. 
    6. Toggle **IPv4** to on.
    7. Enter the following information: 
        * **IP address:** Paste the IP address you copied in step 4. 
        * **Subnet mask:** Enter **255.255.255.0**. 
        * **Gateway:** Enter the IP address shown on the **Drop-in Gateway** page. 
        * **Preferred DNS:**  Enter the IP address shown on the **Drop-in Gateway** page. 
    8. Click **Save**. 

??? "Android"
    1. Connect your device to the main router. 
    2. On your Android, open **Settings**. 
    3. Tap **Connections** > **Wi-Fi**.
    4. Tap the **Settings** icon next to the network you are connected to. 
    5. Tap **View more**. 
    6. Tap **IP settings** > **Static**. 
    7. For **Gateway** and **DNS 1**, enter the IP address shown on the **Drop-in Gateway** screen. 
    8. Tap **Save**. 

??? "iOS"
    1. Connect your device to the main router. 
    2. On your iOS, open **Settings**.
    3. Tap **Wi-Fi**.
    4. Tap the Wi-Fi network you are connected to. 
    5. Under **IPv4 Address**, keep a record of **IP Address** and **Subnet Mask**.
    6. Tap **Configure IP** > **Manual**. 
    7. Enter the following information: 
        * **IP Address:** Enter the IP Address you obtained in step 5. 
        * **Subnet Mask:** Enter the Subnet Mask you obtained in step 5. 
        * **Router:** Enter the IP address shown on the **Drop-in Gateway** screen. 
    8. Tap **Save**.
    9. Tap **Configure DNS**, then tap **Manual**. 
    10. Tap **Add Server**, then enter the IP address shown on the **Drop-in Gateway** screen.
    11. Tap **Save**.

??? "Mac"
    1. Connect your device to the main router.
    2. On your Mac, click the Apple icon > **System Settings**, 
    3. In the left sidebar, click **Network**.
    4. Next to the network you are connected to, click **Details**.
    5. Click **TCP/IP**.
    6. Keep a record of **IP Address** and **Subnet Mask**.
    7. Next to **Configure IPv4**, click **Manually**.
    8. Enter the following information: 
        * **IP address:** Enter the IP Address you obtained in step 6. 
        * **Subnet mask:** Enter the IP Address you obtained in step 6. 
        * **Router:** Enter the IP address shown on the **Drop-in Gateway** page. 
    9. Click **OK** > **OK**. 

### 4. Set up AdGuard, DNS, VPN, and other features

Follow these guides to enable the features you want on your GL.iNet router.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

Related Article:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.