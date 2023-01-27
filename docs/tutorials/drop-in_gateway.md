# Drop-in Gateway

Please upgrade to v4.2.x to use this feature. There are some bugs in v4.1.x.

On the left side of web Admin Panel -> NETWORK -> Drop-in Gateway

## Usage Scenarios

For users who do not want to replace their main router, you can use this mode to extend the functionality of your main router.

* Use ADGuard Home to filter advertisements
* Use encrypted DNS
* Use VPN client
* It is recommended to use a more powerful router with large memory (e.g. GL-MT2500) and install other traffic forwarding and control tools yourself.

## Network Typology

![drop-in gateway mode typology](https://static.gl-inet.com/docs/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

The diagram above has two colored lines, gray lines, and green lines with 3 arrows on the green lines, and a number next to each arrow.

1. The gray lines show that the devices are connected to the main router, and the LAN port of the main router is connected to the WAN port of the GL.iNet router with Drop-in Gateway function via an Ethernet cable.

2. The green lines indicate that when the Drop-in Gateway mode is enabled, all or part of the devices' data will be processed by the GL.iNet device before being sent out through the main router.

## Setup

The GL.iNet router referred to below is the GL.iNet router on which you want to enable the Drop-in Gateway function.

* All clients use the Drop-in Gateway feature.

    1. The LAN port of the main router connect to the WAN port of the GL.iNet router via an ethernet cable.

    2. Enable Drop-in Gateway feature, it will generate the settings automatically.

    3. Log in to the main router's admin panel to disable the DHCP feature or set the DHCP gateway to GL.iNet router's IP.

    4. Go back to the GL.iNet router and set up features like ADGuard Home, encypted DNS and VPN Client.

* Some clients use the Drop-in Gateway feature.

    1. The LAN port of the main router connect to the WAN port of the GL.iNet router via an ethernet cable.

    2. Enable Drop-in Gateway feature, it will generate the settings automatically.

    3. Set the gateway on the device that you want to use the Drop-in Gateway feature to the IP of the GL.iNet router.

    4. Go back to the GL.iNet router and set up features like ADGuard Home, encypted DNS and VPN Client.

## Cautions

1. It will increase the latency when using this mode.
2. When this mode is enabled, the data transferred between the selected devices in the LAN will also pass through the drop-in gateway, so the bandwidth between the main router and the drop-in gateway will affect the bandwidth of the whole LAN.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
