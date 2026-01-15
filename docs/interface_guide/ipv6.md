# IPv6

IPv6 (Internet Protocol version 6) is the latest Internet Protocol designed to replace IPv4. It offers a larger pool of unique IPs, solving the address exhaustion issue of IPv4 and supporting the growing number of connected devices globally.

On the left side of web Admin Panel -> NETWORK -> IPv6. This page allows you to enable and configure IPv6 on your router.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

When IPv6 is enabled, WAN interfaces such as Ethernet will get their IPv6 addresses via DHCPv6. You can also modify the IPv6 address manually in the Ethernet settings page.

**Note**: Some features (e.g., firewall, GoodCloud, OpenVPN DCO) do not yet support IPv6. If you use these features and IPv6 at the same time, it's likely to cause connectivity issues.

Toggle on **Enable IPv6**, select the mode for your main network and DNS acquisition method, then click **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: Four modes are available: **Native**, **Passthrough**, **NAT6** and **Static IPv6**.

- Native: This mode is applicable when the router directly obtains a public IPv6 address, and the router automatically assigns IPv6 addresses to online devices. This mode can meet the IPv6 access needs of most users.

- Passthrough: This mode is applicable when IPv6 packets need to be directly passed through without any processing or conversion. For example, some specific network applications or services may require the complete preservation of the content of IPv6 packets for further processing or analysis, which is used by technical personnel for network debugging or security analysis.

- NAT6: This mode is suitable for scenarios where a router is used as a management gateway to assign dynamic internal IPv6 addresses to each device on the network. In this mode, terminal devices connect through a Optical Network Terminal and obtain a local area network IPv6 address.

- Static IPv6: This mode is suitable for devices or services that require a fixed IPv6 address, such as servers or network printers. This mode ensures that the device always uses the same IPv6 address, facilitating management and access.

**DNS acquisition method**: It determines how the router obtains IPv6 DNS server addresses. There are two options: **Automatic** and **Manual**. 

- Automatic: The router will obtain IPv6 DNS server addresses dynamically (e.g., via DHCPv6).

- Manual: Input custom IPv6 DNS server addresses. However, since DNS is used to resolve domain names to their corresponding IP addresses, manual DNS server configuration may result in DNS lookup failures. Please use it with caution.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
