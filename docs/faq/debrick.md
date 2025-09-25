# Using U-Boot to unbrick your router

If you bricked your router due to some DIY projects or flashing a wrong firmware, you may fail to access it. In this case, you can re-install the firmware by using U-Boot failsafe.

**Note:** The U-Boot operation will remove your router's settings and installed plugins.

---

## Preparation

Please prepare a computer with an ethernet port. If your computer does not have ethernet port, please prepare an additional USB Ethernet Adapter.

## Unbrick Steps

Refer to this video tutorial or follow the procedures below to access the U-Boot Web UI and re-install the firmware.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>The steps for using U-Boot to re-install firmware are roughly the same, and this video takes Mudi/Mudi V2 as an example. For other models, you may follow the procedures below.</small>

1. Download firmware [here](https://dl.gl-inet.com/){target="_blank"} to your computer.

    Some models, such as GL-AR750S-EXT, are available in two formats of firmware. Please use the firmware for U-Boot, whose file name extension is **.img**.

2. Remove the power of router. Connect your computer to the **Ethernet LAN port** of the router. You **MUST** leave all the other ports **unconnected**.

    !!! note

        For some models, certain individual LAN ports and the WAN port are interchangeable. Please do not use this LAN port. For example, on the GL-MT6000 (Flint 2), do not use LAN 1. Please use LAN 2, LAN 3, or LAN 4 instead.

3. Press and hold the Reset button firmly, **at the same time power up the router**. If your router doesn't have a power button, plugging the power in will power it on automatically.

    Then you will see the LED flashing in a regular sequence a few times, please release your finger **after** the sequence changes.

    The following will give the description of sequence of each model of LED flashing.

    **Note:** Same router models with different manufacturing dates may have different LED colours or flashing sequences, it won't affect the U-Boot process. Please pay more attention to the change of the flashing LED.

    - For **GL-BE9300(Flint 3)**, the blue LED flashes 6 times, then turns solid white.
    
    - For **GL-BE3600(Slate 7)**, after holding down the reset button for about 5 seconds, a 5-second countdown will appear on the LED display. Keep pressing the reset button until the next step is displayed on the screen:

        1. Manually set the IP address of your computer to 192.168.1.2
        2. Use browser to visit  http://192.168.1.1

        Turn to Step 4 for further instruction.

    - For **GL-B3000(Marble)**, the blue LED light flashes 7 times, then turns solid white.

    - For **GL-MT6000(Flint 2)**, the blue LED flashes 6 times, then turns solid white.

    - For **GL-MT3000(Beryl AX)**, the blue LED flashes 6 times, then turns solid white.

    - For **GL-MT2500/GL-MT2500A(Brume 2)**, the blue LED flashes 5 times, then turns solid white.

    - For **GL-S200**, the cyan LED flashes 5 times, then briefly turns purple, then turns solid cyan.

    - For **GL-A1300(Slate Plus)**, the LED flashes slowly 5 times, then stays on for a short while, then flashes quickly all the time.

    - For **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)** and **microuter-N300**, the LED flashes 5 times.

    - For **GL-E750(Mudi)**, its screen will first display "Booting", followed by "Reset Counting 1 to 4", and finally "Please Open Web 192.168.1.1".

    - For **GL-S1300(Convexa-S)** and **GL-B1300(Convexa-B)**, the LED flashes 4 times.
        
        The leftmost Power LED may stay on the whole time while the rightmost Wi-Fi LED flashes 4 times, then the middle Mesh LED turns solid on.
        
        (For some old GL-B1300, the leftmost Power LED stays on the whole time, and both the middle LED and the rightmost LED flash 5 times simutaneously, then stay on.)

    - For **GL-SF1200**, the 5G LED flashes 5 times, then turns solid on.

    - For **GL-AX1800(Flint)**, the blue LED flashes 5 times, then turns solid white.

    - For **GL-AXT1800(Slate AX)**, the blue LED flashes 5 times, then turns solid on.

    - For **GL-XE300(Puli)**, the LAN LED flashes 5 times, then the Wi-Fi LED stays on.

    - For **GL-X300B(Collie)**, the WAN LED flashes 5 times, then the Wi-Fi LED stays on.

    - For **GL-X3000(Spitz AX)**, the WAN LED flashes 5 times, then the Wi-Fi LED stays on.

    - For **GL-XE3000(Puli AX)**, the WAN LED flashes 5 times, then the Wi-Fi LED stays on.

    - For **GL-SFT1200(Opal)**, the blue LED flashes 5 times, then turns solid white.

    - For **GL-AP1300(Cirrus)**, the power LED flashes slowly 5 times, then stays on for a short while, then flashes quickly all the time.

    - For **GL-MT1300(Beryl)**, the LED starts blue, flashes twice slowly, then flashes 5 times faster and turns solid white.

    - For **GL-B2200(Velica)**, the two LEDs start blue, then turn white and flash 5 times, then turn solid blue.

    - For **GL-MV1000/GL-MV1000W(Brume)**, no repeat LED flashes signal. (Power and WAN LEDs will stay on the whole time.)

    - For **GL-MiFi**, the LED flashes 6 times.

    - For **GL-MT300N**, **GL-MT300A**, the LED flashes 3 times.

4. Manually set the IP address of your computer to **192.168.1.2**. Please check the step-by-step guide for different operating systems below:

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

5. Use browser to visit **http://192.168.1.1**. This is the U-Boot Web UI.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note 
    
        - If you fail to access U-Boot Web UI, check if you have any VPN or proxy software running. Disable any VPN or proxy software, including Tailscale and ZeroTier.
    
        - The U-Boot Web UI above may not be exactly the same as what you see, because the U-Boot version is different for different production dates. In some extreme cases, we recommend upgrading the U-Boot version. Please refer to the tutorial [here](upgrade_uboot_version.md).

6. Click **Choose file** button to find the firmware file. Then click **Update firmware** button.

7. Wait for around 3 minutes. Don't power off your device when updating. The router is ready when both power and  Wi-Fi LED are on or you can find its SSID on your device.

8. Revert the IP setting you did in step 4 and connect your device to the LAN or Wi-Fi of the router. You will be able to access the router via **192.168.8.1** again.

    **Note:** It might be required to use the incognito mode or to delete the browser cache and cookies to access the router.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
