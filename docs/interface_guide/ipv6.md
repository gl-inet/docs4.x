# IPv6

On the left side of web Admin Panel -> NETWORK -> IPv6

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

The IPv6 function allows you to enable and configure IPv6 on router.

When IPv6 is enabled, WAN interfaces such as Ethernet will get their IPv6 addresses via DHCPv6. You can also modify the IPv6 address manually in the Ethernet settings page.

**Note**: Some features (e.g., firewall, GoodCloud, OpenVPN DCO) do not yet support IPv6. If you use functions of both VPN and IPv6 at the same time, it's likely to cause IPv6 data leakage.

Toggle the button to enable IPv6, and click **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: There are four modes: **Native**, **Passthrough**, **NAT6** and **Static IPv6**.

- Native: This mode is applicable when the router directly obtains a public IPv6 address, and the router automatically assigns IPv6 addresses to online devices. This mode can meet the IPv6 access needs of most users.

- Passthrough: This mode is applicable when IPv6 packets need to be directly passed through without any processing or conversion. For example, some specific network applications or services may require the complete preservation of the content of IPv6 packets for further processing or analysis, which is used by technical personnel for network debugging or security analysis.

- NAT6: This mode is suitable for scenarios where a router is used as a management gateway to assign dynamic internal IPv6 addresses to each device on the network. In this mode, terminal devices connect through a Optical Network Terminal and obtain a local area network IPv6 address.

- Static IPv6: This mode is suitable for devices or services that require a fixed IPv6 address, such as servers or network printers. This mode ensures that the device always uses the same IPv6 address, facilitating management and access.

**DNS acquisition method**: There are two options: **Automatic** and **Manual**.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
