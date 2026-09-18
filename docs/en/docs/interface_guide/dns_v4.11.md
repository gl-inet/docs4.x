# DNS

**Note**: The content on this page was first introduced in firmware v4.11.

If your device is running a different firmware version, use the selector below to switch to the corresponding guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 and earlier](dns.md)

</div>

---

On the left side of the web Admin Panel, go to **DNS**.

The DNS settings on your router control how domain names are translated into IP addresses. This page allows you to use the DNS server(s) automatically obtained from upstream devices, or set custom ones. You can also configure DNS options and edit static host rules.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

By default, DNS queries for traffic matching the VPN policy use the DNS server(s) provided by the VPN tunnel. Non-VPN DNS queries use the DNS server(s) obtained from the active WAN interface. If you set custom DNS server(s), you can apply them to VPN tunnels, the router itself, or both. When these options are enabled, DNS queries within the selected scope are resolved through the specified one(s), instead of those obtained from the relevant network interfaces. If no custom DNS server(s) are set, the router uses the DNS server(s) obtained from the relevant network interfaces.

## WAN DNS

The WAN DNS displays DNS servers retrieved from each WAN uplink, including Ethernet, Repeater, Tethering and Cellular. 

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

If a WAN uplink is active, its DNS server addresses are displayed on the right, as shown below.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## VPN DNS

The VPN DNS shows DNS servers obtained from each active VPN tunnel. 

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

If a VPN tunnel is running, DNS queries from VPN traffic will follow the VPN DNS configuration, as shown below.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## Manual DNS

Manual DNS supports two configuration types: **Static DNS** and **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: If this option is enabled, custom Manual DNS will be used for packets through the VPN tunnel instead of the VPN's DNS settings.

- **Apply Manual DNS to Router Itself**: This option is enabled by default. When it is turned on, the router's built-in services (such as GoodCloud) will apply the custom manual DNS settings.

### Static DNS

Static DNS allows you to manually enter IPv4 or IPv6 DNS server addresses. You can either input addresses directly or select preset public DNS servers from the drop-down list to set up your router's DNS servers.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

You can enter up to four DNS server addresses. Click **Apply** to save the changes.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### Encrypted DNS

Encrypted DNS mode supports multiple DNS providers, including Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS, and OpenDNS. You can also specify an encrypted DNS server manually as needed. 

Select the DNS Provider first. The remaining options will change according to your selection.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- If you select a specific DNS provider (e.g., NextDNS), please choose an encryption type from DNS over TLS (DoT), DNS over HTTPS (DoH), and DNS over QUIC (DoQ). Note that the DNS over QUIC (DoQ) was introduced in firmware v4.9 and is only available when using Control D, NextDNS, or AdGuard DNS as the DNS provider.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- If you select Manual as the DNS provider, please choose an encryption type from DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS, and DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Next, click **Add a Server** to add at least one DNS server. You can directly enter the URL or stamp format of the encrypted DNS. For a list of public servers, please refer to [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Encryption Type Comparison"

    1. **DNS over TLS (DoT)**

        Encrypts DNS queries via a dedicated TLS port. It isolates DNS traffic from regular web traffic and is easy to identify by network operators.

    2. **DNS over HTTPS (DoH)**

        Transmits DNS data inside standard HTTPS traffic. It blends DNS requests with normal web traffic for strong privacy and bypasses simple traffic filtering.

    3. **DNS over QUIC (DoQ)**
        
        Encapsulates DNS over the QUIC protocol. It features low latency, fast reconnection and stable performance on unstable networks.

    4. **Oblivious DNS over HTTPS (ODoH)**

        An enhanced version of DoH. It separates user IP from DNS queries, preventing both server and network providers from tracking your browsing activity.

    5. **DNSCrypt**

        A mature encryption protocol for DNS. It authenticates and encrypts DNS traffic, focusing on anti-tampering and compatibility with legacy network environments.

## DNS Options

Click **Options** in the upper-right corner to configure advanced DNS settings.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

You can toggle these options on or off as needed.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: Turning this option on may cause private DNS lookup failure. If your network has a captive portal, please disable this option.

- **Override DNS Settings of All Clients**: If this option is enabled, the router overrides unencrypted DNS settings for all clients.

## Edit Hosts

You can click the **Edit Hosts** button at the top right to customize static host rules.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

The router prioritizes these host rules when resolving requests from connected clients.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.