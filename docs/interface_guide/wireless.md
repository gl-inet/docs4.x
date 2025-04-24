# Wireless

The wireless interface may vary a bit from model to model, here is an example of GL-MT3000.

On the left side of web Admin Panel -> WIRELESS

**Note**: 

1. Some models do not have 5G Wi-Fi, e.g. GL-S200, GL-X300B(Collie).

2. Some models do not have Wi-Fi, e.g. GL-MT2500/GL-MT2500A(Brume 2), GL-MV1000(Brume)

## Wi-Fi Status

When Wi-Fi is enabled, the corresponding Wi-Fi icon will light up below the device model image on the Internet page.

![wifi status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_status.png){class="glboxshadow"}

The Wi-Fi QR code will be displayed if the cursor hovers over the enabled Wi-Fi icon. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_qr_code.png){class="glboxshadow"}

## Main Wi-Fi

**5G Wi-Fi**

![main wifi 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

**2.4G Wi-Fi**

![main wifi 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

**Note**:

* The Wi-Fi QR code will be displayed if the cursor hovers over the QR code icon beside the SSID Label. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: This feature is enabled by default. It aims to prevent the client vendors from collecting nearby Wi-Fi BSSIDs and client devices' GPS coordinates to their servers. Click [here](#randomized-bssid) for more details.

* The **Bandwidth** and **Channel** can't be modified when [repeater](internet_repeater.md) is enabled.

* When **Channel** set as **Auto**, Wi-Fi will not automatically switch to the DFS channel.

* When switch to DFS channel from non-DFS channel, it will pop up a caution.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/tutorials/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* When the **Bandwidth** is set to 160 MHz (Only some models can be set to 160MHz), Wi-Fi will always use the DFS channel, even if you choose a non-DFS channel of the **Auto** option.

## Guest Wi-Fi

**5G Guest Wi-Fi**

![guest wifi 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

**2.4G Guest Wi-Fi**

![guest wifi 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Randomized BSSID

**Note**: This feature is available since firmware v4.6

Randomized BSSID aims to prevent the client vendors from collecting nearby Wi-Fi BSSIDs and client devices' GPS coordinates to their servers.

Client vendors collect the geographical location data of Wi-Fi access points by leveraging their unique BSSIDs to locate devices. When client devices such as mobile phones and computers scan or connect to a router, if other devices are within the Wi-Fi signal coverage area of that router, their location and movement trajectory information may be widely disseminated. If a client device uses GPS for positioning, it will periodically upload the BSSIDs of nearby Wi-Fi access points and their corresponding GPS coordinates to the vendor's server. As a result, even if other devices do not have GPS functionality, or do not enable GPS, they can estimate their own location by querying the visible BSSID information. However, this crowdsourced location tracking system has security vulnerabilities. Attackers can use it to accumulate a global database of Wi-Fi access point locations and continuously track the movement trajectories of devices, posing a threat to user privacy and security. 

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

Therefore, GL.iNet routers' Randomized BSSID feature can protect your privacy. 

In the router's web Admin Panel, go to WIRELESS -> 5GHz Wi-Fi or 2.4GHz Wi-Fi, BSSID option is enabled by default. As a result, the device uses a randomly generated BSSID and renews it at each booting. When the random BSSID is disabled, you can use the real MAC.

Guest Wi-Fi BSSID is consistent with the primary Wi-Fi BSSID in the same band.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
