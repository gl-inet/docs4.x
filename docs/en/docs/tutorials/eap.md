# Connect GL.iNet routers to an EAP network

Some GL.iNet routers support connecting to EAP (Extensible Authentication Protocol) Wi-Fi networks.

EAP is an authentication framework commonly used with **802.1X authentication** for **WPA2‑Enterprise / WPA3‑Enterprise** networks. A typical example is **eduroam**, a global Wi‑Fi roaming service for education and research that relies on 802.1X and EAP.

This guide will introduce two ways to connect GL.iNet routers to an EAP Wi-Fi network: via GL.iNet Web Admin Panel and via LuCI.

## Supported Models

??? "Supported Models"
    - <u>GL-BE10000 (Slate 7 Pro)</u><sup>1</sup>
    - <u>GL-MT3600BE (Beryl 7)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - <u>GL-BE3600 (Slate 7)</u><sup>1</sup>
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>

    ---

    **Footnote:** 
    
    1. When connecting to WPA/WPA2/WPA3-Enterprise networks, GL-BE10000 (Slate 7 Pro), GL-MT3600BE (Beryl 7), and GL-BE3600 (Slate 7) support only PEAP-authenticated networks. Other EAP methods (EAP-TLS, EAP-TTLS, EAP-MD5, etc.) are not supported.
    
    2. GL-MT6000 (Flint 2) and GL-MT3000 (Beryl AX) do not support connecting to EAP networks on the default firmware. However, GL.iNet provides native OpenWrt 24 firmware for these models, which adds EAP support. Please search the model in the [Download Center](https://dl.gl-inet.com/){target="_blank"} and refer to the OPENWRT 24 tab for details.

    3. GL-SFT1200 (Opal) supports connecting to EAP networks starting from firmware v4.8.

??? "Unsupported Models"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Connect via Web Admin Panel

1. Log in to the web Admin Panel, go to **INTERNET** -> **Repeater** section, then click **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    It will scan the available networks. Find and select the EAP SSID to connect.

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Or click **Join Other Network** in the upper right to manually join the EAP network.

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Input the **SSID**.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Select **Security** as WPA/WPA2/WPA3 Enterprise.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Input the **Username** and **Password**, then click **Apply** to connect.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Connect via LuCI

The GL.iNet web Admin Panel supports only a limited number of EAP types.

If your target EAP network cannot be connected via the web Admin Panel, please try connecting via the LuCI interface.

> Note: The following steps are for reference only, please refer to the actual LuCI page of your device.

1. Log in to the web Admin Panel, go to **SYSTEM** -> **Advanced Settings**. Install LuCI and click **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Log in to LuCI interface with the same admin password, and go to Network -> Wireless.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Click **Scan** on 2.4G section or 5G section.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Join the network you want.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Troubleshooting

If the target EAP network requires additional parameters, such as EAP type (e.g., PEAP, TTLS), domain suffix match, identity, anonymous identity, etc., the EAP connection via web Admin Panel may fail.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

Follow the steps below to connect your GL.iNet router to EAP networks that requires advanced settings via LuCI interface.

1. Obtain configurations.

    Obtain the configuration parameters for the target EAP network in advance. For example: 

    - EAP Type (e.g., PEAP, TTLS, TLS)
    - Authentication domain suffix (e.g., @company.com)
    - Identity (usually full username)
    - Anonymous Identity (optional)
    - Inner authentication type (e.g., MSCHAPv2, PAP)
    - CA certificate (if required, prepare .crt format file)

    This is an example of Xfinity Mobile Wi-Fi for your reference.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Log in to LuCI.

    Log in to the router's web admin panel. After login, if you previously attempted to connect to the target EAP network via the WebGUI but failed, please abort the connection.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    Then go to **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Log in to the LuCI with the same admin password.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Configure Repeater in LuCI.

    In the LuCI interface, go to Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    Click the **Scan** button in the 5G or 2.4G section to search for available Wi-Fi networks.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    Find the target EAP network in the scan results and click **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    In the "Joining Network" page, enter the **WPA passphrase** and click **Submit** button.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    You will be directed to the Wireless Client configuration. 

4. Locate the **Interface Configuration** -> **Wireless Security**. 

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    Select/enter the correct configuration parameters according to your target EAP network, as shown below. **Do not click Save yet**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. Switch to **Advanced Settings** tab, specify an interface name, such as **wlan0**. Then click **Save** in the bottom right corner.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. You will return to the Wireless page, which shows pending changes. Click the **Save & Apply** button in the bottom right corner.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    Your router will be connected to the target EAP network successfully.

7. Verify connection.

    ??? "Check connection in the WebGUI"

        Once the router successfully connects to the target EAP network, a repeater icon will light up in the WebGUI, as shown below.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Note**: Since the configuration in LuCI is not synchronized with that in the WebGUI, details of the repeater interface (e.g., connected IP, gateway, etc.) will not appear on the WebGUI.
        
        As shown in the image, the repeater section at the bottom is blank. However, the router has already connected to the target EAP network as a repeater, because the repeater icon at the top is lit up.

    ??? "Check connection via SSH"

        1. [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} log in to your router.

        2. Input **ifconfig** and click Enter.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            You will be able to check the **wlan0** interface status.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.