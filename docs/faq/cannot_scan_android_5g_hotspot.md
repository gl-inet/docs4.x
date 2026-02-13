# Cannot Scan Android 5G Hotspot

Connecting the GL.iNet router as a repeater to an Android phone's 5G hotspot is one of the common ways to access the Internet.

However, if you cannot scan your Android phone's 5G hotspot, it may be related to the Wi-Fi country code.

Some Android phones set their 5G hotspot to a US channel by default. If your GL.iNet router wasn't originally purchased in the US, you might experience this issue. 

You can change your GL.iNet router's Wi-Fi country code in LuCI page as per the steps below.

## Step 1. Log in to LuCI

Log in to your GL.iNet router, at the left sidebar, choose **SYSTEM -> Advanced Settings -> Go to LuCI**. Login to LuCI with the same admin password.

## Step 2. Edit Wi-Fi settings

Go to **Network -> Wireless**, select 5G Wi-Fi and edit. If you are using GL-MT3000, go to **Network -> MTK Wi-Fi**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

![mtkwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/mtkwifi.jpg){class="glboxshadow"}

## Step 3. Select US as the country code

Under **Device Configuration -> Advanced Settings**, select US (United States) as the country code for your 5GHz Wi-Fi. 

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

Click **Save & Apply** before logging out.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

Then try scanning your Android phone 5G hotspot again.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.