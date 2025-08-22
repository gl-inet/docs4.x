# Configure dual wired Ethernet WAN via an Ethernet to USB-A adapter

You can configure dual wired Ethernet WAN access on a single-WAN-port router via an Ethernet to USB-A adapter. 

GL-iNet routers support most common Ethernet to USB-A adapters. Simply plug the Ethernet to USB-A adapter into the USB port on the router, and connect the other end to your ISP router.

## Topology

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Setup steps

1. Install the USB driver. Plug the Ethernet to USB-A adapter into the USB port of your GL-iNet router, and connect the other end to your ISP router.

2. Log in to the router's web admin panel. Navigate to **Application** -> **Plug-ins**, install the USB network driver for your adapter. 

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

     instance, if you're using a Realtek adapter, please select the **kmod-usb-net-rtl8152** driver. 

3. Connect by Tethering.

    Once the installation is complete, the USB connection will be detected, allowing you to connect to your ISP router.

    ![suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
