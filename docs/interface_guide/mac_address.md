# MAC Address

!!! Note

    This guide is applicable to v4.5 and earlier versions.
    
    Since v4.6, the MAC address settings for Ethernet and Repeater interfaces have been migrated to the [Port Management](network_port_management.md) and the [INTERNET](internet_repeater.md) page respectively.

On the left side of web Admin Panel -> NETWORK -> MAC Address

The MAC Address page was previously called MAC Clone and has been changed to MAC Address since v4.2.

On this page, you can find the router's default MAC address, clone a client's MAC address, enter a MAC address manually, or generate a random MAC address.

If the device supports setting multiple Ethernet ports to be used as WAN ports, you can set the MAC address for each port separately. Note that the MAC address setting is only valid when the Ethernet port is used as a WAN port.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* The factory default MAC address.

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Clone a client's MAC address.

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Note:** Many new devices now use a different random MAC address to connect to different Wi-Fi, so the MAC address shown here may not be the actual MAC address of the user's device. The randomized MAC may also be called a Private Wi-Fi Address or a random hardware address on different devices.

* Manual input or generate a random MAC address.

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Usage Scenarios

When you connect to a public hotspot, use a random MAC address if you do not want the hotspot to know your real MAC address or to limit your access to the Internet based on it. Please read this guide [Connect to a Hotspot with a Captive Portal](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
