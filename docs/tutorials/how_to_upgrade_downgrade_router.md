# How to manually upgrade or downgrade your router firmware (from v4.x to v4.x)?

This tutorial will show you **how to manually upgrade or downgrade your router firmware (from v4.x to v4.x)**. The steps for manually upgrading and downgrading your router's firmware are the same.

!!! Note "About upgrading and downgrading your router firmware"

    **Upgrade:** GL.iNet routers running firmware version 4.x do not offer the auto-update feature. 
    
    When a new firmware version is available, you will see the "Upgrade Reminder" prompt after you sign in to the router admin panel. You can click the **Upgrade** button to install the latest firmware version listed there. If you have a specific firmware version you want to upgrade to, follow the steps below to upgrade your router manually. 

    **Downgrade:** You can downgrade your router's firmware to resolve certain issues.

## 1. Check if your router is running the latest firmware version (Only for upgrade)

1. In a web browser, enter the URL to your router's admin panel (e.g., 192.168.8.1) and sign in.
2. From the left sidebar, select **SYSTEM** > **Upgrade**.  

## 2. Download the firmware file

1. In the search bar of the [firmware download center](https://dl.gl-inet.com/), search for and select your router model.
2. In the **Stable** tab or other tabs, select **Download for common upgrade and uboot** next to the firmware version you want to download. 

## 3. Upload the firmware

The following instructions were written for uploading your firmware through the router admin panel.  (To upload your firmware via the GL.iNet mobile app, [download the app](https://www.gl-inet.com/app/) and set it up.)

1. In a web browser, enter the URL to your router's admin panel (e.g., 192.168.8.1) and sign in. 
2. (Optional) If you want to back up your current settings, follow the steps below.

    ??? "Back up your current settings"

        a. From the left sidebar, click **SYSTEM** > **Advanced Settings**. 

        b. Click the link or **Go To LuCI** button to access LuCI login page. 

        c. Enter the admin password, then click **Log in**. 

        d. Click **System** > **Backup / Flash Firmware**. 

        e. Under **Backup**, click **Generate archive**. A file containing your current settings will be downloaded to your device. 
        
        **Please note that this file is only applicable to the firmware version at the time of backup and not to other firmware versions.**

3. From the left sidebar, click **SYSTEM** > **Upgrade**. 
4. Click **Local Upgrade** and select the file you downloaded earlier. 
5. To retain your current settings (e.g., your router admin password), toggle **Keep Settings** to on. 
6. Click **Install**.

**Note:** During the upgrade process, do not power off the router. After the upgrade is complete, you will see the router login screen. 

If you lost the router settings during the firmware update process, restore your router settings. 

If the above method doesn't work, try upgrading the firmware via [U-boot](../faq/debrick.md).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.