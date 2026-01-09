# Configure dual wired Ethernet WAN via an Ethernet to USB-A adapter

You can configure dual wired Ethernet WAN access on a single-WAN-port router via an Ethernet-to-USB-A adapter. 

GL.iNet routers support common Ethernet-to-USB-A adapters, allowing you to convert the wired Ethernet access from your ISP router to a USB connection via the router's USB port, providing the router with an additional wired Ethernet access alongside the WAN port.

## Topology

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Setup steps

1. Plug the Ethernet to USB-A adapter into the USB port of your GL.iNet router, and connect the other end to your ISP router.

2. Install the USB driver. 

    Log in to the router's web admin panel, navigate to **Application** -> **Plug-ins**, and install the USB network driver for your adapter. 

    For instance, if you're using a Realtek adapter, please install the **kmod-usb-net-rtl8152** driver. 

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Wait for installation to complete.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Connect by USB Tethering.

    Once the driver installation is complete, navigate to **INTERNET** -> **Tethering** section. 
    
    The USB connection will be detected, allowing you to connect to your ISP router.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Click on **Connect** and wait a minute. When a green dot lights up and the page displays information such as IP address, it indicates that USB Tethering connection is successful.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
