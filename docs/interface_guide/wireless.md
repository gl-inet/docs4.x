# Wireless

The wireless interface may vary a bit from model to model. Here is an example of Beryl AX GL-MT3000.

!!! Note

    1. Some models do not have 5G Wi-Fi, e.g. GL-S200, GL-X300B(Collie).
    2. Some models do not have Wi-Fi, e.g. GL-MT2500/GL-MT2500A(Brume 2).

## Wi-Fi Status Display

The router’s Wi-Fi networks are enabled by default, and the corresponding Wi-Fi icon will light up below the device model image on the INTERNET page.

![wifi status display](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_status_display.png){class="glboxshadow"}

The Wi-Fi QR code will be displayed if the cursor hovers over the enabled Wi-Fi icon. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_qr_code.jpg){class="glboxshadow"}

## Wireless Settings

On the left side of web Admin Panel, go to WIRELESS page.

The Wireless page allows configuration for both Main Wi-Fi networks (5 GHz and 2.4 GHz) and Guest Wi-Fi networks (5 GHz and 2.4 GHz).

### Main Wi-Fi

The Main Wi-Fi network includes 5 GHz and 2.4 GHz bands.

It allows you to configure settings for both 5 GHz and 2.4 GHz Wi-Fi networks, including enabling/disabling Wi-Fi, setting TX power, specifying the Wi-Fi name (SSID), enabling/disabling randomized BSSID, selecting Wi-Fi security mode, setting Wi-Fi password, configuring SSID visibility, choosing the Wi-Fi mode, bandwidth, and channel.

**5G Wi-Fi**

![main wifi 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

**2.4G Wi-Fi**

![main wifi 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

**Note**:

* The Wi-Fi QR code will be displayed beside the SSID if the cursor hovers over the QR code icon. You can scan the Wi-Fi QR code using your Phone/Pad to quickly connect to the corresponding Wi-Fi.

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: This feature is enabled by default. It aims to prevent the client vendors from collecting nearby Wi-Fi BSSIDs and client devices' GPS coordinates to their servers. Click [here](#randomized-bssid) for more details.

* The **Bandwidth** and **Channel** cannot be modified when the router acts as a [repeater](internet_repeater.md), as they follow that of the repeated network.

* When **Channel** is set to **Auto**, the router's Wi-Fi will not automatically switch to the DFS channel.

* When switching the Channel to a DFS one from non-DFS channel, a caution will appear as shown below.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/tutorials/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* When the **Bandwidth** is set to **160 MHz** (Only some models can be set to 160MHz), the Wi-Fi will always use the DFS channel, even if you choose a non-DFS channel or Auto for Channel settings.

### Guest Wi-Fi

he Guest Wi-Fi network includes 5 GHz and 2.4 GHz bands.

It supports settings including enabling/disabling Wi-Fi, setting the Wi-Fi Name (SSID), configuring Wi-Fi Security and Password, and adjusting SSID Visibility.

**5G Guest Wi-Fi**

![guest wifi 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

**2.4G Guest Wi-Fi**

![guest wifi 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Randomized BSSID

Randomized BSSID feature is available as of firmware v4.6. It aims to prevent the client vendors from collecting nearby Wi-Fi BSSIDs and client devices' GPS coordinates to their servers.

**How Client Vendors Collect Location Data**

Client vendors usually collect the geographical location data of Wi-Fi access points by leveraging their unique BSSIDs to locate devices. When client devices (e.g., mobile phones, computers) scan or connect to a router:

- If other devices are within the router’s Wi-Fi signal coverage, their location and movement trajectories may be exposed.

- If a device uses GPS for positioning, it periodically uploads nearby Wi-Fi BSSIDs and corresponding GPS coordinates to the vendor’s server.

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

**Security Risks of Crowdsourced Tracking**

Even devices without GPS (or with GPS disabled) can estimate their location by querying visible BSSID info. However, this crowd-sourced location tracking system has security vulnerabilities. Attackers can use it to accumulate a global database of Wi-Fi access point locations and continuously track the movement trajectories of devices, posing a threat to user privacy and security.

**How Randomized BSSID Protects Your Privacy**

To address these vulnerabilities, GL-iNet routers implement the Randomized BSSID feature as a privacy safeguard.

In the router’s web admin panel, go to WIRELESS -> 5GHz Wi-Fi or 2.4GHz Wi-Fi, the BSSID option is enabled by default. 

With this setting, the device uses a randomly generated BSSID and renews it each time it boots. If you disable the random BSSID, the router reverts to using the real MAC address.

**Note**: For Guest Wi-Fi, the BSSID remains consistent with the Main Wi-Fi BSSID within the same frequency band.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
