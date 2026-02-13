# Drop-in Gateway

On the left side of web Admin Panel -> NETWORK -> Drop-in Gateway

Drop-in Gateway is an extension function that enables capability expansion for an existing primary router without replacing or reconfiguring it. By connecting the GL.iNet router to the primary router via an Ethernet cable, users can add advanced network features onto the existing network infrastructure, for example:

- Filter advertisements via AdGuard Home
- Enable VPN client
- Use encrypted DNS

It is recommended to use a higher-performance router or security gateway with ample memory (e.g., GL-MT2500, GL-MT5000) and install additional traffic forwarding and control tools as required.

## Network Topology

Drop-in Gateway operates as an intermediate network system, routing data traffic from client devices through the GL.iNet router for processing before transmitting it via the primary router. During this process, it not only preserves existing network settings (e.g., SSID and password) to ensure uninterrupted connectivity for all connected devices, but also allows you to manage network traffic for all or specific client devices as needed.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

The diagram above consists of two types of lines: gray lines, and green lines marked with three arrows, each labeled with a corresponding number.

1. **Gray lines** illustrate the physical connection topology: client devices (e.g., computer, laptop) connect to the primary router, and the primary router's LAN port links to the WAN port of the GL.iNet router (with Drop-in Gateway enabled) via an Ethernet cable.

2. **Green lines** depict the sequential data transmission path when Drop-in Gateway is active, with the numbered arrows indicating the traffic flow order:

    1. Traffic from client devices is first routed to the primary router;
    
    2. The primary router forwards the traffic to the GL.iNet router for processing (e.g., ad filtering, VPN encryption);
    
    3. After processing, the traffic is sent back to the primary router, which then either delivers the final data to the original client devices or routes it out to the Internet.

## Setup

There are two deployment modes for different application scenarios: All client devices are networked through Drop-in Gateway, or only specific client devices are networked through Drop-in Gateway.

In the following example, the gateway address of the primary router is `192.168.1.1`.

### All devices are networked through Drop-in Gateway

1. Connect the LAN port of the primary router to the WAN port of the GL.iNet router via an ethernet cable.

2. Log in to the web admin panel of your GL.iNet router, enable Drop-in Gateway, and the system will automatically generate the corresponding configuration parameters.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - The **IP Address** refers to the WAN IP address of your GL.iNet router, which is dynamically assigned by the primary router. This WAN IP can be viewed in the Ethernet section of the [INTERNET](internet_ethernet.md) page. 
    
    - The **Gateway** and **DNS Server 1** fields are automatically filled with the IP address of the primary router by default. If these parameters are incorrectly configured, you can manually adjust them as needed.

    Write down the IP address here, as you will use it in the following steps.

    Select the first configuration method and click **Apply**.

3. Log in to the web admin panel of your primary router.

    ??? "GL.iNet"

        If your primary router is GL.iNet and it runs firmware v4.2 and above, follow the steps below.

        Log in to the web Admin Panel -> NETWORK -> LAN -> DHCP Server -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Fill in the DHCP Gateway as the IP Address in step 2, etc, `192.168.1.23`, then click **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        If your primary router is TP-Link, follow the steps below (Taking TP-LINK Archer C3150 as an example).

        Log in to the TP-Link admin page, navigate to **Advanced** -> **Network** -> **DHCP Server**, then disable the **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Then click **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        If your primary router is Linksys, follow the steps below (Taking Linksys WHW01 as an example)

        Log in to the Linksys admin page, navigate to **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Click the tab **Local Network**, disable the **DHCP Server**, then click **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        It will show a warning. Click **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        Please log in to the primary router's admin panel to disable its DHCP server. You may refer to the corresponding manufacturer's user manual, or consult their support.

4. Go back to the GL.iNet router and set up features like [AdGuard Home](adguardhome.md), [encrypted DNS](dns.md), [WireGuard Client](wireguard_client.md) and [OpenVPN Client](openvpn_client.md).

### Specific devices are networked through Drop-in Gateway

1. Connect the LAN port of the primary router to the WAN port of the GL.iNet router via an ethernet cable.

2. Log in to the web admin panel of GL.iNet router, enable Drop-in Gateway, and the system will automatically generate the corresponding configuration parameters.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - The **IP Address** refers to the WAN IP address of your GL.iNet router, which is dynamically assigned by the primary router. This WAN IP can be viewed in the Ethernet section of the [INTERNET](internet_ethernet.md) page. 
    
    - The **Gateway** and **DNS Server 1** fields are automatically filled with the IP address of the primary router by default. If these parameters are incorrectly configured, you can manually adjust them as needed.

    Write down the IP address here, as you will use it in the following steps.

    Select the second configuration method and click **Apply**.

3. Set the gateway and DNS on the device that you want to use the Drop-in Gateway feature as the IP address in Drop-in Gateway page.

    ??? "Windows"

        Here is an example of Windows 11, Windows 10 is similar. Make sure your PC is connected to the primary router. It is assumed here that your computer is connected to the primary router via a network cable, and the setup is similar if you connect via Wi-Fi.

        1. Open Settings.

        2. Click on **Network & Internet**.

        3. Click the **Ethernet** tab.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. You will find the IP address of this PC. Under the "IP assignment" section, click the **Edit** button.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Select the **Manual** option. Turn on the **IPv4 toggle** switch.

        6. Set the **IP address** as the IP address you see in step d, **Subnet mask** set as `255.255.255.0`, both **Gateway** and **Preferred DNS** set as the IP address in Drop-in Gateway page.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Click the **Save** button.

    ??? "Android"

        Here is an example of Samsung S21. Make sure your smartphone is connected to the primary router.

        1. Open Settings, click on Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Click on Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Click the cog icon of the current SSID.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Click **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Click **IP settings**, choose **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Set the **Gateway** and **DNS 1** as the IP address in Drop-in Gateway page, then click **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Here is an example of iOS 16.3 on iPhone 8. Make sure your smartphone is connected to the primary router.

        1. Open Settings, click Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Click the SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Scroll down and you will find the **Configure IP** is **Automatic**. Write down the **IP Address** and **Subnet Mask** for the next step.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Change **Configure IP** to **Manual**, set the **IP Address** and **Subnet Mask** to the same as you obtained in the previous step, and set the **Router** as the IP address displayed on the Drop-in Gateway page, then click **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Click **Configure DNS** and change it to **Manual**. Click **Add Server**, set the DNS server IP address to the IP address displayed on the Drop-in Gateway page, then click **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Back to the GL.iNet router's web Admin Panel and set up features as needed, such as [AdGuard Home](adguardhome.md), [encrypted DNS](dns.md), [WireGuard Client](wireguard_client.md) and [OpenVPN Client](openvpn_client.md).

## Cautions

1. Enabling Drop-in Gateway increases network latency.

2. When Drop-in Gateway is enabled, data transmission between selected LAN devices is also routed through the drop-in gateway. Bandwidth between the primary router and drop-in gateway therefore impacts overall LAN bandwidth.

---

Related Article:

- [How to set up drop-in gateway on a GL.iNet router](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
