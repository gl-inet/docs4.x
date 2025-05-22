# Why is my VPN speed slow

## Router's CPU Speed

VPNs encrypt your data to protect privacy, which adds extra data processing. This encryption and decryption can slow down your connection. Please choose a router with faster CPU to enhance your VPN speed. We listed all the VPN speeds in our [product page](https://www.gl-inet.com/products/).

## Server Distance

If the VPN server is far from your physical location, the data has to travel a longer distance, resulting in higher latency and slower speeds. You can see the example below. It shows the client speeds when connecting to different server locations at the same time of the day.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Server Load

If many users are connected to the same VPN server, it can become congested, leading to slower speeds for everyone.

## Server Upload Speed

If you are using a private VPN tunnel, the Internet Service Provider (ISP) upload speed on the server side will be the bottleneck of the download speed on the client side, since the VPN client is downloading data through the server.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Protocol Differences

Different VPN protocols like OpenVPN or WireGuard have varying levels of security and speed. Some may be slower due to their encryption methods.

## ISP Throttling
 
 Some Internet Service Providers (ISPs) may throttle speeds for users who are using VPNs, especially if they suspect heavy data usage. Especially in some developing countries or small towns where many users share limited Internet infrastructures.

## DNS

 Some Internet Service Providers (ISPs) may not resolve the VPN domains, please try to use [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) in our router's Network settings.

## MTU

 Some Internet Service Providers (ISPs), especially mobile carries may limited the size of the data packet, please try to change the default MTU from 1420 to 1380 or 1280 in [VPN Client Option](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.