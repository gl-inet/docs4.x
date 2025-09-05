# Why is my VPN speed slower than expected?

If you've noticed that your VPN connection speed is lower than the theoretical maximum speed (tested in an ideal local area network), this is actually normal in real-world usage. 

VPNs are designed to prioritize security and privacy, which inherently affects speed. It's normal for VPN speeds to range between 30-50% of the advertised maximum under typical network conditions. This discrepancy arises due to multiple factors that impact performance, which will be explained below, along with some tips to optimize your experience.

**Note**: The methods below may help improve VPN speed but cannot guarantee matching advertised speeds, as real-world performance depends on multiple factors.

## Router CPU Speed

VPN encrypts your data to protect privacy, which adds extra data processing. This encryption and decryption can slow down your connection. Please choose a router with faster CPU to enhance your VPN speed. 

We have listed the VPN test speeds for all models on our [product page](https://www.gl-inet.com/products/). However, please note:

* Tests are conducted on a local network. Real-world speeds may differ depending on your network configuration.
* OpenVPN and WireGuard speeds will be slower when the router is used as a server. Results above are in client mode.

## Server Distance

If the VPN server is far from your physical location, data has to travel a longer distance, resulting in higher latency and slower speeds. 

You can see the example below, which shows client speeds when connecting to different server locations at the same time of day.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Server Load

If many users are connected to the same VPN server, it can become congested, leading to slower speeds for everyone.

## Server Upload Speed

If you are using a private VPN tunnel, the upload speed of the Internet Service Provider (ISP) on the server side will be the bottleneck for the download speed on the client side, since the VPN client downloads data through the server.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Protocol Differences

Different VPN protocols like OpenVPN or WireGuard vary in security and speed. Some may be slower due to their encryption methods.

## ISP Throttling

Some Internet Service Providers (ISPs) may throttle speeds for users using VPNs, especially if they suspect heavy data usage. This is particularly common in some developing countries or small towns where many users share limited internet infrastructure.

## DNS

Some Internet Service Providers (ISPs) may fail to resolve VPN domains. Try using [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) in your router's Network settings.

## MTU

Some Internet Service Providers (ISPs), especially mobile carriers, may limit the size of data packets. Try changing the default MTU from 1420 to 1380 or 1280 in the VPN Client Options. 

For firmware v4.8 and above, please refer to [here](../interface_guide/vpn_dashboard.md/#tunnel-options). 

For firmware v4.7 and earlier, please refer to [here](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.