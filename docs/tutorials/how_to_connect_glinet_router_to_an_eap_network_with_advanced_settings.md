# How to connect GL.iNet router to an EAP network requiring advanced settings?

Some GL.iNet routers support connecting to EAP (Extensible Authentication Protocol) Wi-Fi networks.

If the target EAP network only requires username and password authentication, you can directly connect the router to it as a repeater via the web admin panel (WebGUI). Simply select the EAP network, security and enter your credentials to complete the connection. Click [here](../tutorials/eap.md){target="_blank"} for details.

![join eap in webgui](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/join_eap_in_webgui.jpg){class="glboxshadow gl-85-desktop"}

However, if the target EAP network requires additional parameters, such as EAP method (e.g., PEAP, TTLS), domain suffix match, identity, anonymous identity, etc., the repeater setup via WebGUI may fail.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connection_failed.png){class="glboxshadow"}

This tutorial will introduce the method to connect GL.iNet router to EAP networks requiring advanced settings via LuCI interface.

## 1. Check Router Model

Ensure your router supports connecting to EAP networks as a repeater. Check the supported models [here](../tutorials/eap.md){target="_blank"}.

## 2. Obtain Configurations 

Obtain the configuration parameters for the target EAP network in advance. For example: 

- EAP Type (e.g., PEAP, TTLS, TLS)
- Authentication domain suffix (e.g., @company.com)
- Identity (usually full username)
- Anonymous Identity (optional)
- Inner authentication type (e.g., MSCHAPv2, PAP)
- CA certificate (if required, prepare .crt format file)

This is an example of Xfinity Mobile WiFi for your reference:

![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

## 3. Access LuCI Interface

Log in to the router's web admin panel. After login, if you previously attempted to connect to the target EAP network via the WebGUI but failed, please abort the connection.

![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/abort_connection.png){class="glboxshadow"}

Then go to SYSTEM -> Advanced Settings -> Go to LuCI. Log in to the [LuCI](../faq/what_is_luci.md){target="_blank"} interface with the same admin password.

![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/luci_login.jpg){class="glboxshadow gl-70-desktop"}

## 4. Configure Repeater in LuCI

In the LuCI interface, navigate to Network -> Wireless.

![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless.png){class="glboxshadow"}

Click the **Scan** button in the 5G or 2.4G section to search for available WiFi networks.

![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_scan.png){class="glboxshadow"}

Find the target EAP network in the scan results and click **Join Network**.

![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/scan_results.png){class="glboxshadow"}

In the "Joining Network" page, enter the **WPA passphrase** and click **Submit** button.

![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/joining_network.png){class="glboxshadow"}

You will be directed to the Wireless Client configuration. 

Locate the **Interface Configuration** -> **Wireless Security**. Select/enter the correct configuration parameters based on your target EAP network. Do NOT click Save for now.

![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security.jpg){class="glboxshadow"}

As an example, the configuration obtained in the step 2 above has been entered into the corresponding entry box. 

![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security_example.png){class="glboxshadow"}

Switch to **Advanced Settings** tab, specify an interface name, such as **wlan0**. Then click **Save** in the bottom right corner.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/advanced_settings.png){class="glboxshadow"}

You will return to the Wireless page, where it shows there are pending changes.

Click on the **Save & Apply** button in the bottom right corner.

![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/save_apply.png){class="glboxshadow"}

Your router will be connected to the target EAP network successfully.

## 5. Verify Connection

??? "Check connection status in the WebGUI"

    Once the router successfully connects to the target EAP network, a repeater icon will light up in the WebGUI, as shown below.

    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connected_status.png){class="glboxshadow"}

    **Note**: Since the configuration in LuCI is not synchronized with that in the WebGUI, details of the repeater interface (e.g., connected IP, gateway, etc.) will not appear on the WebGUI.
    
    As shown in the image, the repeater section at the bottom is blank. However, the router has already connected to the target EAP network as a repeater, because the repeater icon at the top is lit up.

??? "Check connection status via SSH"

    1. [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} log in to your router.

    2. Input **ifconfig** and click Enter.

        ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig.png){class="glboxshadow"}

        You will be able to check the **wlan0** interface status.

        ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig_2.png){class="glboxshadow"}

---

Related Article:

- [How to Connect to an Extensible Authentication Protocol (EAP) Network?](eap.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.