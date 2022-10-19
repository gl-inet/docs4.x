# Drop-in Gateway

Drop-in Gateway mode is available since firmware version 4.1.

On the left side of web Admin Panel -> NETWORK -> Network Mode

## Usage Scenarios

Users who do not want to replace their main router, you can use this mode to extend the functionality of your main router.

* Use ADGuard Home to filter ads
* Use encrypted DNS
* Use VPN client
* It is recommended to use a router with more powerful and big storage (e.g. GL-MT2500) and install other traffic forwarding and control tools on your own.

## Network Typology

![drop-in gateway mode typology](https://static.gl-inet.com/docs/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_typology.png){class="glboxshadow" width="60%" height="60%"}

The diagram above has two color lines, gray lines, and green lines with 3 arrows on the green lines, and a number next to each arrow.

1. The gray lines show the devices are connected to the main router, the LAN port of the main router connect to the WAN port of the GL.iNet router which has Drop-in Gateway function via an ethernet cable.

2. The green lines indicate that when Drop-in Gateway mode is enabled, all or part of the devices' data will be processed by the GL.iNet device before being sent out through the main router.

## Setup

1. The LAN port of the main router connect to the WAN port of the GL.iNet router which has Drop-in Gateway function via an ethernet cable.

2. On the left side of web Admin Panel -> Network -> Drop-in Gateway

    ![drop-in gateway](https://static.gl-inet.com/docs/en/4/tutorials/drop-in_gateway/drop-in_gateway_options.png){class="glboxshadow" width="70%"}

    * **Force the use of Drop-In Gateway Mode DNS**, if this option is enable, it will force to use the Drop-In Gateway router's DNS. Please enable it if you want to use AdGuard Home, DNS settings(encrypted DNS, Manual DNS, DNS Proxy etc).
    * **Device Cover Mode**
        * **Overall Cover**, all devices connected to the main router will be controled by drop-in gateway mode.
        * **Partial Cover**, you can choose which devices connected to the main router will be controled by drop-in gateway mode.

    Click **Apply** to enable it.

3. When it is enabld, it will show a device list of MAC, IP and active status.

    ![drop-in gateway enabled](https://static.gl-inet.com/docs/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_enabled.png){class="glboxshadow" width="76%"}

4. Then you can continue to set up with the other functions.

## Cautions

1. It will increase the latency when using this mode.
2. When this mode is enabled, the data transferred between the selected devices in the LAN will also pass through the drop-in gateway, so the bandwidth between the main router and the drop-in gateway will affect the bandwidth of the whole LAN.
3. The implementation mechanism of drop-in gateway is through APR spoofing, so it will be affected by various security settings of firewalls and client devices in the LAN, and it is likely that clients with APR firewall enabled will not be covered.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
