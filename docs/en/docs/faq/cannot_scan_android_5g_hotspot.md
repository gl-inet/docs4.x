# Cannot Scan Android 5G Hotspot

Connecting the GL.iNet router as a repeater to an Android phone's 5G hotspot is one of the common ways to access the Internet.

However, if you cannot scan your Android phone's 5G hotspot, it may be related to the Wi-Fi channel.

Some Android phones set their 5G hotspot to a US channel by default. If your GL.iNet router wasn't originally purchased in the US, you might experience this issue. 

You can choose the appropriate method based on your GL.iNet router's LuCI interface to modify the Wi-Fi country code.

## Method 1 Modify the Wi-Fi Country Code on the Network page

1. Log in to your GL.iNet router and go to **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Log in to LuCI with the same admin password.

2. Edit Wi-Fi settings.

    Go to **Network** -> **Wireless**, locate the 5G Wi-Fi and click **Edit** on the right.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. Select US as the country code.

    On the Wireless page, click the **Advanced Settings** tab under **Device Configuration**. Select US (United States) as the country code for your 5GHz Wi-Fi. 

    ![5gus](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. Click **Save & Apply** before logging out.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    Then try scanning your Android phone 5G hotspot again.

## Method 2 Modify the Wi-Fi Country Code on the MTK page

1. Log in to your GL.iNet router and go to **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Log in to LuCI with the same admin password.

2. Edit Wi-Fi configuration.

    Go to **MTK** -> **Wi-Fi configuration**.

    ![wifi config](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/wifi_config.png){class="glboxshadow"}

    Locate the 5 GHz radio module and click **Config** to open its wireless configuration page.

    ![5g wifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5g_wifi.png){class="glboxshadow"}

3. Select US as the country code.

    On the 5G Wireless configuration page, click the **Advanced** tab to set the Country Code. Select US (United States) as the country code for your 5GHz Wi-Fi. 

    ![5g us](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5g_us.png){class="glboxshadow"}

    Click **Save and Apply** before logging out, then try scanning your Android phone 5G hotspot again.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.