# DNS

On the left side of web Admin Panel -> NETWORK -> DNS

If you set custom DNS servers, any dns name will be resolved through the DNS servers set here instead of the one obtained from wan, repeater, cellular, hotspot sharing or VPN configuration DNS server.

![dns](images/dns/dns_page.png){class="glboxshadow"}

**DNS Rebinding Attack Protection:** Turning on this option may cause private DNS lookup failure. If your network has a captive portal please disable this option.

**Override DNS Settings for All Clients:** If enabled, your router will override unencrypted DNS settings for all clients.

**Allow VPN tunnels to prefer their own DNS:** If this option is enabled, when a VPN connection is available, data packets transmitted over the VPN tunnel will be resolved using the VPN's own DNS servers. If your VPN uses DNS servers on the intranet. Or if you are using policy-based VPN proxy mode and want to use the VPN's DNS server while using encrypted DNS for non-VPN packets. please enable it.

## DNS Server Settings

There are four modes.

- Automatic, use the gateway of the parent router.

    ![automatic](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_automatic.png){class="glboxshadow"}

- Encrypted DNS

    ![encrypted dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_encrypted_dns.png){class="glboxshadow"}

    **Encrypted Type** has four type, DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS, Oblivious DNS over HTTPS.

    - For DNS over TLS, the DNS Provider has two options, NextDNS and Cloudflare.

    - For DNSCrypt-Proxy, DNS over HTTPS and Oblivious DNS over HTTPS, they can select DNS Server.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dnscrypt-proxy.png){class="glboxshadow"}

- Manual DNS

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_manual_dns.png){class="glboxshadow"}

- DNS Proxy

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_dns_proxy.png){class="glboxshadow"}

## Edit Hosts

Requests from clients will be resolved preferentially using the static DNS rules you write in Hosts.

![hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/edit_hosts.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
