# Wireless

The wireless interface may vary a bit from model to model, here is an example of GL-AXT1800.

On the left side of web Admin Panel -> WIRELESS

**Note**: Some models do not have 5G Wi-Fi, e.g. GL-S200, GL-X300B(Collie).

**Note**: Some models do not have Wi-Fi, e.g. GL-MT2500/GL-MT2500A(Brume 2), GL-MV1000(Brume)

## Wi-Fi Status

When Wi-Fi is enabled, the corresponding Wi-Fi icon will light up below the device model image on the Internet page.

![wifi status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_status.png){class="glboxshadow"}

The Wi-Fi QR code will be displayed if the cursor hovers over the enabled Wi-Fi icon. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_qr_code.png){class="glboxshadow"}

## Main Wi-Fi

* 5G Wi-Fi

    ![main wifi 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.png){class="glboxshadow"}

    **Note**:

    * The Wi-Fi QR code will be displayed if the cursor hovers over the QR code icon beside the SSID Label. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

        ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_qr_code.png){class="glboxshadow"}

    * The **Bandwidth** and **Channel** can't be modified when [repeater](internet_repeater.md) is enabled.
    * When **Channel** set as **Auto**, Wi-Fi will not automatically switch to the DFS channel.
    * When switch to DFS channel from non-DFS channel, it will pop up a caution.

        ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/tutorials/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

    * When the **Bandwidth** is set to 160 MHz (Only some models can be set to 160MHz), Wi-Fi will always use the DFS channel, even if you choose a non-DFS channel of the **Auto** option.

* 2.4G Wi-Fi

    ![main wifi 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

### Randomized BSSID

* **Using randomized BSSID can protect your privacy.** Clients vendor collect the geolocation of Wi-Fi access points based on their unique BSSID to locate the device. When client device scan or connect your router, merely being within Wi-Fi range of a client device can lead to a device’s location and movements being made widely and publicly available. When a client device uses GPS to determine its location, it periodically reports nearby Wi-Fi BSSIDs and their GPS coordinates to clients vendor servers. This allows other clients devices to query visible BSSIDs to estimate their location, even without GPS connectivity. An attacker can exploit client’s crowdsourced location tracking system to amass a worldwide database of Wi-Fi access point locations and track devices’ movements over time.
![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid.jpg){class="glboxshadow"}

* BSSID Option enabled by default. If this option is enabled, the device uses a randomly generated BSSID and renews it at each booting. When the random BSSID is disabled, you can use the real MAC.

## Guest Wi-Fi

* 5G Guest Wi-Fi

    ![guest wifi 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

* 2.4G Guest Wi-Fi

    ![guest wifi 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

* Note:

    * Guest Wi-Fi BSSID is consistent with the primary Wi-Fi BSSID in the same band.


---


Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
