# DNS

On the left side of web Admin Panel -> NETWORK -> DNS

The DNS settings on your router control how domain names are translated into IP addresses. This page lets you use the DNS server(s) automatically obtained from upstream devices, or set custom ones, and configure DNS priorities.

If you set custom DNS server(s), any DNS queries will be resolved through the specified one(s), instead of the DNS servers obtained through individual network interfaces. Otherwise, you will use the DNS settings configured for each interface.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Turning on this option may cause private DNS lookup failure. If your network has a captive portal please disable this option.

- **Override DNS Settings for All Clients:** If enabled, your router will override unencrypted DNS settings for all clients.

- **Allow Custom DNS to Override VPN DNS:** If enabled, once you have set custom DNS, packets transmitted through the VPN tunnel will be resolved using the custom DNS override instead of the DNS server settings from the VPN connections.

## DNS Server Settings

There are four modes: Automatic, Encrypted DNS, Manual DNS, and DNS Proxy.

- **Automatic**: The router will automatically use the DNS server provided by the upstream device (e.g., ISP modem, primary router), or the DNS settings corresponding to each network interface.

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS**: Four Encryption Type are available: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS, Oblivious DNS over HTTPS.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - For DNS over TLS, select a DNS provider among Control D, NextDNS, and Cloudflare.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - For the other three (i.e., DNSCrypt-Proxy, DNS over HTTPS, and Oblivious DNS over HTTPS), select at least one DNS Server from the repository.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS**: Select at least one DNS Server for your router from the drop-down list.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy**: The router will route all LAN DNS queries to the proxy server address you specify (e.g., 8.8.8.8#53). This might be useful if you are running another DNS server or Pi-hole on your network.

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Edit Hosts

Requests from clients will be resolved preferentially using the static DNS rules you write in Hosts.

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
