# Guest Network

The guest network settings have been separated from the [LAN](lan.md) since v4.5.

On the left side of web Admin Panel -> NETWORK -> Guest Network. 

It includes Guest Network basic settings and DHCP server settings.

## Basic Settings

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

You can set a separate, isolated network designed for temporary users, providing limited access and enhanced security by segregating it from the primary network.

**Note**: Some models do not have Wi-Fi (e.g. GL-MT2500/GL-MT2500A), so there is no Guest Network tab.

The **Default Gateway** is **192.168.9.1**, If you have enable the Guest Wi-Fi and it conflicts with your network, you can change it.

Security settings: 

- AP Isolation.

    You can isolate your network's client devices into a separate network area. These devices cannot communicate with other devices on the network.

- Block WAN Subnets.

    This feature is available in v4.8

    If this function is enabled, the guest network will not be able to access the upper network and the network segment where the upper network is located.

Other basic settings and the DHCP server settings are the same as [LAN](lan.md).

## DHCP Server settings

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

---

Related Articles:

- [How to set up a guest Wi-Fi network on GL.iNet routers](../tutorials/how_to_set_up_a_guest_network.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
