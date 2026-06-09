# How to make AdGuard Home DNS bypass the VPN tunnel

Normally, VPN and AdGuard Home can run simultaneously on GL.iNet routers. No problems arise when AdGuard Home is not set to handle DNS requests.

However, if you configure AdGuard Home to manage all DNS traffic and forward queries to **public upstream DNS servers**, enabling VPN will trigger DNS resolution failures.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home enabled and handles DNS requests)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(AdGuard Home upstream DNS settings)</small>

By default, all outbound traffic is routed through the VPN tunnel. This forces AdGuard Home's upstream DNS traffic onto the VPN, which cannot reach your public upstream DNS servers. As a result, all connected clients will fail to resolve domain names.

To keep AdGuard Home functional while VPN is active, you can add a static route in LuCI to forward upstream DNS traffic to the regular WAN gateway and bypass the VPN tunnel. Follow the steps below.

1. Log in to your router's web Admin Panel and go to **SYSTEM** -> **Advanced Settings** ->** Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Log in with the same admin password.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. In the LuCI, navigate to **Network** -> **Routing**, then click **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Create a new static route for your upstream DNS addresses.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface: Select the physical WAN interface **wan**.
    
    - Route type: Keep the default value.
    
    - Target: `[Your Public Upstream DNS Server]/32`
    
        You can use `nslookup` to verify the actual IP address of your public upstream DNS server.
    
    - Gateway: `[Your WAN Upstream Gateway IP]`
    
        This is usually the IP address of your modem or ISP gateway, such as `192.168.0.1`. Find it in your router's internet status page.

    This route ensures AdGuard Home's upstream DNS queries bypass the VPN tunnel and go directly through your WAN connection.

4. Save and apply the settings. AdGuard Home will then resume normal DNS resolution.

5. Test upstream DNS servers.

    You can verify your upstream DNS servers directly in the AdGuard Home interface.
    
    On your router's web Admin Panel, go to **APPLICATIONS** -> **AdGuard Home**, then click **Settings Page** to open the AdGuard Home dashboard.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    On the AdGuard Home dashboard, go to **Settings** -> **DNS settings** -> **Upstream DNS servers** and click **Test upstreams**. Results will appear on the right.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Tip**: If you have more than one DNS server and they are a mix of IP and domain, you can separate AdGuard DNS from VPN DNS, which might be easier than using a static route. 

SSH log in to your GL.iNet router and run the following commands to force AdGuard Home to send DNS queries through the WAN only.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.