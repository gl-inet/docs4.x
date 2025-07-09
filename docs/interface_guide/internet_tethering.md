# Connect to the Internet via usb tethering

Using a USB cable to share network from your smartphone to the router is called Tethering. Host-less modem works in Tethering during the setup of the modem as well.

**Note:** Some mobile carriers limit or charge extra for tethering. We recommend checking with your carrier.

## Setup

=== "iPhone"

    1. Connect an iPhone to the router’s USB port using a USB cable. A system dialog will appear asking whether to trust the device. Tap **Trust** to proceed. 

        ![trust this computer](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Go to iPhone **Settings** -> **Personal Hotspot** -> **Turn on Allow Others to Join**.

        ![turn on allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow"}

    3. Connect a computer or another phone to the router to access the web Admin Panel, then go to INTERNET -> Tethering section, click **Connect**.

        ![tethering connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_find_device.png){class="glboxshadow"}

    4. Once connected, the personal hotspot status (such as the number of connected devices) appears in the status bar at the top of the phone screen.

        ![tethering](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow"}

        The web admin panel will also display the Tethering connection status.

        ![tethering](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_connected.png){class="glboxshadow"}

=== "Android"

    1. Connect an Android phone to the router’s USB port using a USB cable. A system dialog may appear asking Use USB for what purpose. Select **File Transfer** if prompted. 

    2. Go to **Settings** -> **Network & Internet** -> **Hotspot & tethering**, enable **USB tethering**.
    
        (The steps to enable USB Tethering vary by brand. Check your device’s settings for the exact location, and contact your manufacturer’s support if you need assistance.)

    3. Access the router’s web admin panel, go to INTERNET -> Tethering section, click **Connect**.

    4. Once connected, the personal hotspot status (such as the number of connected devices) appears in the status bar at the top of the phone screen. 
    
        The web admin panel will also display the Tethering connection status.

    For the Android official documentation, refer to [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Warning

When Internet access is not available, the corresponding warning will be displayed: 

**"The interface is connected, but the Internet can't be accessed."**

Solutions: 

1. Check if the smartphone has internet access.

2. Go to [Multi-WAN](multi-wan.md) page to determine whether you can access the Internet or not.

## Troubleshooting

If the connection fails, try these troubleshooting steps:
    
- Use the original power supply for the router.
- Unplug and re-plug the USB cable.
- Use another USB cable. Ensure it supports data transfer (not just charging).
- Turn off and turn on "USB Tethering" for a few times (for Android Phone).
- Turn off and turn on "Allow Others to Join" for a few times (for iPhone).
- Restart your smartphone and try again.

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.