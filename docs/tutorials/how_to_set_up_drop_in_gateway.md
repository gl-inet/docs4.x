# How to set up drop-in gateway on a GL.iNet router 

**Please note**: Models with firmware versions below v4.5.0 lack the "Configuration method" option in both the app and the web Admin Panel. Upon enabling the Drop-in Gateway, these models automatically operate in the "All devices are networked through drop-in gateway" mode.

GL.iNet offers the drop-in gateway feature, which enhances the functionality of your primary router with features it may not have, including AdGuard Home, encrypted DNS, and VPN. By using this feature, you can keep using your primary router as usual while enjoying additional features. 

You can enable drop-in gateway for [all your devices](#enable-drop-in-gateway-for-all-devices) or [specific devices](#enable-drop-in-gateway-for-specific-devices) connected to your primary router. Follow the appropriate section for your setup.

---

## Enable drop-in gateway for all devices

### 1. Connect the GL.iNet router to the main router

Connect the WAN port of the GL.iNet router to the LAN port of the main router with an ethernet cable.

### 2. Enable drop-in gateway mode 
There are two methods for enabling drop-in gateway mode: via through the [router admin panel](#via-the-router-admin-panel) or the [GL.iNet mobile app](#via-the-glinet-mobile-app). 

#### Via the router admin panel 

1. In a web browser, enter 192.168.8.1.  
2. Enter your password, then click **Login**. 
3. In the left sidebar, click **Network** > **Drop-in Gateway**. 
![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

4. Next to **Enable Drop-in Gateway Mode**, toggle the switch to on. 
5. Select **All devices are networked through drop-in gateway**. 
![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

6. Click **Apply**. 

#### Via the GL.iNet mobile app

**Note:** Before you start, install and set up the GL.iNet mobile app on your device. 

1. On the main app screen, tap the **System** tab > **Drop-in Gateway**.![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

2. Tap **Enable**. 
3. For **Devices are networked via drop-in gateway**, tap **All**.![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}
4. Tap **Done**. 

### 3. Disable the DHCP server on the main router
To disable the DHCP server on your specific router, refer to the instructions provided by your router manufacturer. 

### 4. Set up AdGuard, DNS, VPN, and other features

Follow these articles to enable the features on your GL.iNet router:

* [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/){target="_blank"}
* [Encrypted DNS](https://docs.gl-inet.com/router/en/4/interface_guide/dns/){target="_blank"}
* [Parental controls](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control/){target="_blank"}
* [WireGaurd client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/){target="_blank"}
* [OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/){target="_blank"}

---

## Enable drop-in gateway for specific devices

### 1. Connect the GL.iNet router to the main router
Connect the WAN port of the GL.iNet router to the LAN port of the main router with an ethernet cable.

### 2. Enable drop-in gateway mode 
There are two methods for enabling drop-in gateway mode: via through the [router admin panel](#specific-devices-admin) or the [GL.iNet mobile app](#specific-devices-mobile). 

#### Via the router admin panel {#specific-devices-admin}

1. In a web browser, enter 192.168.8.1. 
2. Enter your password, then click **Login**. 
3. In the left sidebar, click **Network** > **Drop-in Gateway**. 
![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}
4. Next to **Enable Drop-in Gateway Mode**, toggle the switch to on. 
5. Select **Some devices select their own networking gateway**. 
![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

6. Click **Apply**. 

**Note:** Do not close this tab. You will need to enter the IP address (shown on the screen) in the next step.

#### Via the GL.iNet mobile app {#specific-devices-mobile}

**Note:** Before you start, install and set up the GL.iNet mobile app on your device. 

1. On the main app screen, tap the **System** tab > **Drop-in Gateway**.![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}
2. Tap **Enable**. 
3. For **Devices are networked via drop-in gateway**, tap **part**.![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}
4. Tap **Done**. 

**Note:** Do not close this tab. You will need to enter the IP address (shown on the screen) in the next step. 

### 3. Set the gateway and DNS on the device

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
        * **IP address:** Enter the IP Address you obtained in step 5. 
        * **Subnet mask:** Enter the IP Address you obtained in step 5. 
        * **Router:** Enter the IP address shown on the **Drop-in Gateway** page. 
    9. Click **OK** > **OK**. 

### 4. Set up AdGuard, DNS, VPN, and other features

Follow these articles to enable the features on your GL.iNet router:

* [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/){target="_blank"}
* [Encrypted DNS](https://docs.gl-inet.com/router/en/4/interface_guide/dns/){target="_blank"}
* [Parental controls](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control/){target="_blank"}
* [WireGaurd client](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/){target="_blank"}
* [OpenVPN client](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.