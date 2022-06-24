# Using Uboot to Debrick Your Router

You may have bricked your router if you were doing some DIY projects or flashed a wrong firmware. You may not be able to access your router but you can re-install the firmware by using Uboot failsafe.

---

Please follow the procedures below to access the Uboot Web UI and re-install the firmware.

You can also refer to video tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EAaaw8nyrnE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. First you have to download firmware to your computer. You can download the firmware [here](https://dl.gl-inet.com/){target="_blank"}. Some models, such as GL-AR750S-EXT, it is available in two formats of firmware, please use the firmware with the .img extension.

2. Connect your computer to the **Ethernet port (either LAN or WAN)** of the router. You **MUST** leave the other port **unconnected**.

3. Press and hold the Reset button firmly first, and then power on your device. (If your device does not have a power button, plugging it in will power it on automatically.)

    If you can not find the reset button, please refer to our page, [How to Repair and Reset](../../troubleshooting/reset).

    Release your finger when you see the LED has flashed:

    The Power LED will light up. Then, other LEDs will start flashing.

    - **6 times** for GL-MiFi, and then the LTE light will faintly flash twice.

    - **5 times** for GL-AR150, GL-AR300M, GL-USB150, GL-AR750, GL-AR750S-EXT(Slate), GL-X750(Spitz), GL-MT300N-V2, GL-E750(Mudi), microuter-N300.

    - **4 times** for GL-S1300, GL-B1300. 
        
        The left most LED may stay on the whole time while the rightmost LED flashes 4 times, then the middle LED turns on and stays on.
        
        (For some old GL-B1300, the left most LED stays on the whole time, and both the middle LED and the rightmost LED flash 5 times at the same time then they stay on.)

    - **3 times** for GL-MT300N, GL-MT300A.

    - For **GL-SF1200**, the 5G LED flashes 5 times then stays on.

    - For **GL-AX1800(Flint)**, the blue light flashes 5 times then turns white and stay on.

    - For **GL-XE300(Puli)**, the LAN light falshes 5 times then WIFI light stay on.

    - For **GL-X300B(Collie)**, the WAN light flashes 5 times then WIFI light stay on.

    - For **GL-SFT1200(Opal)**, the blue light flashes 5 times then turns white and stay on.

    - For **GL-AP1300(Cirrus)**, the power light falshes 5 times then stay on.

    - For **GL-MT1300(Beryl)**, the LED is blue at first, flash twice slowly, then light 5 times a bit quick and turn to white and stay on.

    - For **GL-B2200(Velica)**, the two LEDs are blue at first, then turn white to flash 5 times, then turn blue and stay on.

    - **No repeat LED flashes signal** for GL-MV1000. (Power and WAN LEDs will stay on the whole time.)

4. Set your computer’s IP address to **192.168.1.2**. Please check the step-by-step guide for different operating systems below:

    ??? "Windows 7 / Windows 10"

        1. Go to Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings.

        2. Right click Local Area Connection -> Properties.

        3. Click Internet Protocol Version 4 (TCP/IPv4) -> Properties.

        4. Set the IP adress to 192.168.1.2 manually.

            ![ipv4 properties](https://static.gl-inet.com/docs/en/2.x/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

    ??? "macOS"

        1. Go to System Preferences -> Network.

        2. Chooose Ethernet -> Advanced -> TCP/IP.

        3. In Configure IPv4, choose Manually.

        4. Set the IPv4 Address to 192.168.1.2 manually.

5. Use Firefox or Chrome to visit **http://192.168.1.1**.

![uboot web ui](https://static.gl-inet.com/docs/en/2.x/troubleshooting/src/debrick/ui.jpg){class="glboxshadow"}

6. Click **Choose File** to find the firmware file. Then click **Update firmware**.

7. Wait for around 3 minutes. Don’t power off your device when updating. The router is ready when both power and  Wi-Fi LED are on or you can find its SSID on your device.

8. Revert the IP setting you did in step 4 and connect your device to the LAN or Wi-Fi of the router. You will be able to access the router via 192.168.8.1 again.
