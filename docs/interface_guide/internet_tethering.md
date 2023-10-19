# Connect to the Internet via usb tethering

Using a USB cable to share network from your smartphone to the router is called Tethering. Host-less modem works in Tethering during the setup of the modem as well.

**Note:** Some mobile carriers limit or charge extra for tethering. We recommend checking with your carrier.

=== "iPhone"

    1. Connect iPhone to the USB port of the router. It will pop up a message asking to trust this computer? Click "Trust" to contine. Because we are connecting the iPhone to the router, so here is to TRUST the router.

        ![trust this computer](https://static.gl-inet.com/docs/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Go to iPhone -> Settings -> Personal Hotspot -> Turn on Allow Others to Join.

        ![turn on allow others to join](https://static.gl-inet.com/docs/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow"}

    3. Use a computer or another phone, connect to the router, then go to web Admin Panel, on the left side bar, choose "INTERNET" and click "Connect" in the middle of the page.

        ![tethering connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_find_device.png){class="glboxshadow"}

    4. It will show connected information on the top of your phone screen and the web Admin Panel once you connect successfully.

        ![tethering](https://static.gl-inet.com/docs/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow"}

        Tethering connected on web Admin Panel.

        ![tethering](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_connected.png){class="glboxshadow"}

    If the connection fails, please turn off and turn on **Allow Others to Join** for a few times.

=== "Android"

    For Android phone tethering, the procedure is similar to iPhone. Connect it to the USB port of the router, it may pop up a dialog ask **Use USB for**, choose **File Transfer/Android Audio**, then check Settings -> Personal hotspot -> Usb network sharing.

    For the Android official documentation for refer [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}


## Warning

When Internet access is not available, the corresponding warning is displayed. To determine whether you can access the Internet or not, please go to [Multi-WAN](multi-wan.md) page.

- Warning: *The interface is connected, but the Internet can't be accessed with IPv4 protocol.*

    Solution: Please check if the smartphone has internet access.

## Troubleshooting

    * Please use the original power supply.

---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
