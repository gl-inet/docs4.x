# IPv6

On the left side of web Admin Panel -> NETWORK -> IPv6

The IPv6 function allows you to enable and configure IPv6 on router.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_page.png){class="glboxshadow"}

The current version of the firewall, VPN, terminal list, cloud service, etc., may not support IPv6 for the time being. Therefore, the IPv6 function can only be used for configuration within this interface.

**Note:** If you use functions of both VPN and IPv6 at the same time, it's likely to cause IPv6 data leakage.

After enabled.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: There are four modes, **NAT6**, **Native**, **Passthrough** and **Static IPv6**.

- NAT6 mode is suitable for scenarios where a router is used as a management gateway to assign dynamic internal IPv6 addresses to each device on the network. In this mode, terminal devices connect through a Optical Network Terminal and obtain a local area network IPv6 address.

- Native mode is applicable when the router directly obtains a public IPv6 address, and the router automatically assigns IPv6 addresses to online devices. This mode can meet the IPv6 access needs of most users.

- Static IPv6 mode is suitable for devices or services that require a fixed IPv6 address, such as servers or network printers. This mode ensures that the device always uses the same IPv6 address, facilitating management and access.

- Passthrough mode is applicable when IPv6 packets need to be directly passed through without any processing or conversion. For example, some specific network applications or services may require the complete preservation of the content of IPv6 packets for further processing or analysis, which is used by technical personnel for network debugging or security analysis.


**DNS acquisition method**. It has two options. **Automic** and **Manual**.


---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
