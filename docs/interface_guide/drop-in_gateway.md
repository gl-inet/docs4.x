# Drop-in Gateway

Please upgrade to v4.2.x to use this feature. There are some bugs in v4.1.x.

On the left side of web Admin Panel -> NETWORK -> Drop-in Gateway

## Usage Scenarios

For users who do not want to replace their main router, you can use this mode to extend the functionality of your main router.

* Use ADGuard Home to filter advertisements
* Use encrypted DNS
* Use VPN client
* It is recommended to use a more powerful router with large memory (e.g. GL-MT2500) and install other traffic forwarding and control tools yourself.

## Network Typology

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

The diagram above has two colored lines, gray lines, and green lines with 3 arrows on the green lines, and a number next to each arrow.

1. The gray lines show that the devices are connected to the main router, and the LAN port of the main router is connected to the WAN port of the GL.iNet router with Drop-in Gateway function via an Ethernet cable.

2. The green lines indicate that when the Drop-in Gateway mode is enabled, all or part of the devices' data will be processed by the GL.iNet device before being sent out through the main router.

## Setup

There are two usage scenarios, where all devices can be managed by Drop-in Gateway or only some devices can be managed.

The GL.iNet router referred to below is the GL.iNet router on which you want to enable the Drop-in Gateway function. The router ip address of our main router here is 192.168.1.1.

### All devices managed by the Drop-in Gateway

1. The LAN port of the main router connect to the WAN port of the GL.iNet router via an ethernet cable.

2. Access web Admin Panel of GL.iNet router, enable Drop-in Gateway feature, it will generate the settings automatically.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_enabled.png){class="glboxshadow"}

    The **IP Address** is same of the IP address in [Ethernet sector of Internet page](internet_ethernet.md). The **Gateway** and **DNS Server 1** are the IP address of the main router. If these items are not set correctly, you can change them manually yourself.

    Write down the IP address here, you will use it in the following steps.

3. Log in to the main router's admin page.

    ??? "GL.iNet"

        If the brand of main router is GL.iNet and its version is v4.2 and above.

        Access web Admin Panel -> NETWORK -> LAN -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Fill in the DHCP Gateway as the IP Address in step 2, then click **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        If the brand of main router is TP-Link. Here is an example of TP-LINK Archer C3150.

        Access TP-Link's admin page. At the tab of **Advanced** -> **Network** -> **DHCP Server**, disable the **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Then click **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        If the brand of main router is Linksys. Here is an example of Linksys WHW01.

        Access Linksys's admin page.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        At the tab of **Local Network**, disable the **DHCP Server**, then click **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        It will show a warning, click **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        Please search for the corresponding brand on how to disable DHCP, or consult customer service.

4. Go back to the GL.iNet router and set up features like [ADGuard Home](adguardhome.md), [encypted DNS](dns.md), [WireGaurd Client](wireguard_client.md) and [OpenVPN Client](openvpn_client.md).

### Some devices managed by the Drop-in Gateway

1. The LAN port of the main router connect to the WAN port of the GL.iNet router via an ethernet cable.

2. Access web Admin Panel of GL.iNet router, enable Drop-in Gateway feature, it will generate the settings automatically.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_enabled.png){class="glboxshadow"}

    The **IP Address** is same of the IP address in [Ethernet sector of Internet page](internet_ethernet.md). The **Gateway** and **DNS Server 1** are the IP address of the main router. If these items are not set correctly, you can change them manually yourself.

    Write down the IP address here, you will use it in the following steps.

3. Set the gateway and DNS on the device that you want to use the Drop-in Gateway feature to the IP address in Drop-in Gateway page.

    ??? "Windows"

        Here is an example of Windows 11, Windows 10 is similar. Make sure your PC is connected to the main router, it is assumed here that your computer is connected to the main router via a network cable, and the setup is similar if you connect via WiFi.

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

        Here is an example of Samsung S21. Make sure your smartphone is connected to the main router.

        1. Open Settings, click on Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Click on Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Click the cog icon of current SSID.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Click **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Click **IP settings**, choose **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Set the **Gateway** and **DNS 1** as the IP address in Drop-in Gateway page, then click **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Here is an example of iOS 16.3 of iPhone 8. Make sure your smartphone is connected to the main router.

        1. Open Settings, click Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Click the SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Scroll down, you will find the **Configure IP** is **Automatic**, please write dwon **IP Address** and **Subnet Mask**, you will need it at next step.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Change **Configure IP** to **Manual**, set the **IP Address** and **Subnet Mask** same as you see in previous step, and set the **Router** as the IP address in Drop-in Gateway page, then click **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Click **Configure DNS**, change it to **Manual**. Click **Add Server**, set the server IP address as the IP address in Drop-in Gateway page, then click **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Go back to the GL.iNet router and set up features like [ADGuard Home](adguardhome.md), [encypted DNS](dns.md), [WireGaurd Client](wireguard_client.md) and [OpenVPN Client](openvpn_client.md).

## Cautions

1. It will increase the latency when using this mode.
2. When this mode is enabled, the data transferred between the selected devices in the LAN will also pass through the drop-in gateway, so the bandwidth between the main router and the drop-in gateway will affect the bandwidth of the whole LAN.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
