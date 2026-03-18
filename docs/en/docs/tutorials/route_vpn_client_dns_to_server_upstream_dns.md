# How to route VPN Client DNS queries to the VPN Server's Upstream DNS?

This tutorial introduces the steps to redirect all DNS queries from VPN clients to your self-hosted DNS Server on the LAN side of your primary router, upstream of the VPN server.

## Topology

In this tutorial, we use **Flint 3 (GL-BE9300)** and **Slate 7 (GL-BE3600)** as examples. 

Flint 3 is the VPN server, which has a primary router on its upstream network, and Slate 7 is the VPN client connecting to Flint 3.

When a VPN tunnel is established between the VPN server and client, by default, the DNS queries from the VPN client are first sent to the VPN server, then forwarded to the primary router, and finally resolved by the ISP-assigned DNS servers configured on the primary router's WAN.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

However, if you have deployed a self-hosted DNS Server (IP address `192.168.1.13`) on the primary router, additional configurations are required to route DNS queries to your self-hosted DNS Server.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Setup

1. Log in to the Flint 3's web Admin Panel, navigate to **NETWORK** -> **DNS**. Switch the DNS Server Mode to **Manual DNS**, and enter the IP address of your DNS Server.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Navigate to **VPN** -> **WireGuard Server** -> **Configuration** tab, note the IPv4 Address, which is usually `10.0.0.1/24` or `10.1.0.1/24`, depending on models and firmware versions.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Switch to the **Profiles** tab, add a client configuration and export a profile for Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Open the profile, make sure the DNS is the VPN Server IP address you obtained in step 2. 

    To avoid DNS resolution failure, please delete "64.6.64.6" if any, and save the changes.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. On the Flint 3's web Admin Panel, click the **Start** button on the top of the **WireGuard Server** page to run the server.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Log in to the Slate 7's web Admin Panel, navigate to **VPN** -> **WireGuard Client**. 

    Click **Add Manually** and upload the edited profile. 

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Click the three-dot icon to start the VPN connection. If the status indicator turns green, it means the VPN connection is successful.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Verify DNS resolution

Run the following command to capture DNS traffic on the VPN client. It will show that all VPN client DNS traffic goes to the VPN server (i.e., `10.0.0.1` in this example).

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Run the following command to capture DNS traffic on the VPN server. It will show that all VPN client DNS traffic finally goes to the self-hosted DNS server (i.e., `192.168.1.13` in this example).

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.











