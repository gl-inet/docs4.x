# Wireless

The wireless interface may vary a bit from model to model, here is an example of GL-AXT1800.

On the left side of web Admin Panel -> WIRELESS

**Note**: Some models do not have 5G Wi-Fi, e.g. GL-S200, GL-X300B(Collie).

**Note**: Some models do not have Wi-Fi, e.g. GL-MT2500/GL-MT2500A(Brume 2), GL-MV1000(Brume)

## Wi-Fi Status

When Wi-Fi is enabled, the corresponding Wi-Fi icon will light up below the device model image on the Internet page.

![wifi status](images/internet/wifi_status.png){class="glboxshadow"}

The Wi-Fi QR code will be displayed if the cursor hovers over the enabled Wi-Fi icon. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

![wifi qr code](images/internet/wifi_qr_code.png){class="glboxshadow"}

## Main Wi-Fi

* 5G Wi-Fi

    ![main wifi 5g](images/wireless/main_wifi_5g.png){class="glboxshadow"}

    **Note**:

    * The Wi-Fi QR code will be displayed if the cursor hovers over the QR code icon beside the SSID Label. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

        ![wifi qr code](images/wireless/wifi_qr_code.png){class="glboxshadow"}

    * The **Bandwidth** and **Channel** can't be modified when [repeater](internet_repeater.md) is enabled.
    * When **Channel** set as **Auto**, Wi-Fi will not automatically switch to the DFS channel.
    * When switch to DFS channel from non-DFS channel, it will pop up a caution.

        ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/tutorials/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

    * When the **Bandwidth** is set to 160 MHz (Only some models can be set to 160MHz), Wi-Fi will always use the DFS channel, even if you choose a non-DFS channel of the **Auto** option.




* 2.4G Wi-Fi

    ![main wifi 2.4g](images/wireless/main_wifi_2.4g.png){class="glboxshadow"}



## Guest Wi-Fi

* 5G Guest Wi-Fi

    ![guest wifi 5g](images/wireless/guest_wifi_5g.png){class="glboxshadow"}

* 2.4G Guest Wi-Fi

    ![guest wifi 2.4g](images/wireless/guest_wifi_2.4g.png){class="glboxshadow"}


## Randomized BSSID
* The randomized BSSID solves the problem that router devices are tracked and located, effectively prevents the BSSID of your router from leaking, and prevents attackers from launching attacks on your router based on the vendor information obtained by the router BSSID, protecting your privacy.
* When you use router Wi-Fi for the first time, a BSSID is generated for you by default, and each time the router restarts, a new BSSID is automatically generated for each Wi-Fi, that is, a randomly generated MAC. 
* Using a random BSSID can hide your router's real MAC, helping to protect your privacy. 
* The BSSID of the guest Wi-Fi is consistent with the BSSID of the primary Wi-Fi in the same band.

    ![main wifi 5g](images/wireless/main_wifi_2.4g_bssid.png){class="glboxshadow"}

    ![main wifi 5g](images/wireless/main_wifi_5g_bssid.png){class="glboxshadow"}

* In both 2.4GHz and 5GHz bands, you can configure whether to enable the randomized BSSID independently. When the random BSSID is disabled, you can set the real MAC, and the BSSID will be generated using the real MAC.

    ![main wifi 5g](images/wireless/main_wifi_2.4g_bssid_disable.png){class="glboxshadow"}

    ![main wifi 5g](images/wireless/main_wifi_5g_bssid_disable.png){class="glboxshadow"}
---


Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
