# Can I use Multi-WAN wired input if my GL router doesn't have two WAN ports?

Yes, you can. Our router supports most common Ethernet to USB-A adapters. Simply plug the Ethernet to USB-A adapter into the USB port on the router and connect the other end to your ISP router.

## Topology

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Install USB Driver

Then, navigate to **Application**, **Plug-ins** to install the USB network driver for your adapter. 

![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

For instance, if you’re using a Realtek adapter, please select the **kmod-usb-net-rtl8152** driver. 

## Connect by Tethering

Once the installation is complete, the USB connection will be detected, allowing you to connect to your ISP router.

![suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}
