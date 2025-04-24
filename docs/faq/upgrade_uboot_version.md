# Upgrade Uboot Version

## Warning

**Upgrading U-Boot is very dangerous and generally not recommended. Once it fails, your device will be bricked and there will be no way to restore it. Only do this when necessary or instructed by GL.iNet support**.

**Do NOT turn off the power during the upgrade process, otherwise it may cause the upgrade to fail and the device to be bricked**.

## Preparation

- A computer with an ethernet port. If not, please prepare an additional USB Ethernet Adapter.
- An Ethernet cable.
- Download the Uboot file as per the instructions of the GL-iNet support staff. Mark sure you are using the correct uboot file. If you don't know how to download the Uboot file, contact us via email at support@gl-inet.com.

## Upgrade Steps

Please follow the procedures below to access the U-Boot upgrade page.

1. Remove the power of router. Connect your computer to the **Ethernet LAN port** of the router. You **MUST** leave all the other ports **unconnected**.

    !!! note

        For some models, certain individual LAN ports and the WAN port are interchangeable. Please do not use this LAN port. For example, on the GL-MT6000 (Flint 2), do not use LAN 1. Please use LAN 2, LAN 3, or LAN 4 instead.

2. Press and hold the Reset button firmly, at the same time power up the router. If your router doesn't have a power button, plugging the power in will power it on automatically.

    Then you will see a LED flashing in a regular sequence a few times, please release your finger after the sequence changes.
    
3. Manually set the IP address of your computer to **192.168.1.2**. Please check the step-by-step guide for different operating systems below:

    ??? "Windows 7 / Windows 10"

        1. Go to **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Right click **Local Area Connection** -> **Properties**.

        3. Click **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Set the **IP adress** to `192.168.1.2` manually.

        5. Set the **Subnet mask** to `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Click the **OK** button.

    ??? "Windows 11"

        7. Open Settings.

        8. Click on **Network & Internet**.

        9. Click the **Ethernet** tab.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Under the "IP assignment" section, click the **Edit** button.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Select the **Manual** option.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Turn on the **IPv4 toggle** switch.

        13. Set the static **IP address** as **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Specify the **Subnet mask** as **255.255.255.0**.

        15. Click the **Save** button.

    ??? "macOS"

        16. Click the **Apple** icon in the top left corner of the screen, and select **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Click **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Click **Ethernet** on the left and then click the drop-down box next to **Configure IPv4** and select **Manually**. If you are using a USB Ethernet Adapter, Ethernet may not be found and it may show up as the name of the USB Ethernet Adapter.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Enter the **IPv4 Address** to `192.168.1.2`, **Subnet Mask** to `255.255.255.0`, **Router** to `192.168.1.1`, then click the Apply button in the lower right corner.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4. **Use Google Chrome/Microsoft Edge to visit `http://192.168.1.1/uboot.html`**

    **DO NOT use Mozilla/Firefox as it may brick your router.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5. Click the **Choose file** button and choose the Uboot file you downloaded.

6. Click **Update U-Boot** button. Do NOT turn off the power during the upgrade process. It will take several minutes to update. 

7. After a successful update, it will reboot the router. At this time you can change the IP setting back in step 3 and try to access the web Admin Panel via **192.168.8.1**. If you can access the web Admin Panel normally, it means the router has been rebooted.

    **Note:** It might be required to use the incognito mode or to delete the browser cache and cookies to access the router.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
