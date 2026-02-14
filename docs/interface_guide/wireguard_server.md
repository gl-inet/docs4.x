# Set Up WireGuard Server on GL.iNet Routers

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, [simpler](https://www.wireguard.com/quickstart/){target="_blank"}, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. 

---

## Make sure you have a public IP address

Please click [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) to check if your Internet Service Provider assigns you a public IP address.

**If not, your router cannot be set up as a WireGuard Server.**

Alternative methods:

1. If you have a main router, log in to it and check if it gets a public IP from your ISP.
2. Ask your ISP for a public IP address. This may incur an extra fee.
3. If the above two methods don't work (e.g., if your network is behind CGNAT), you can use a reverse proxy solution such as [Astrorelay](../tutorials/how_to_set_up_wireguard_server_via_astrorelay.md). Alternatively, you may try our SD-WAN solution: [AstroWarp](https://www.astrowarp.net/){target="_blank"}. 

## Confirm if Port Forwarding is required

**Network Topology**

??? "GL.iNet is the Main Router"
    
    * If GL.iNet router is the main router in your network, this is simple, please move to the [next step](#setup-wireguard-server).

??? " GL.iNet is the Sub-Router"

    * If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) on the main router.
    
    * If you already have a main router, the GL.iNet router is several levels below it and you need to set up [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) on each level.

## Setup WireGuard Server

Log in to the web Admin Panel, and navigate to VPN -> WireGuard Server.

1. Click **Generate Configuration** (for vpn server initial setup only).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Check the configuration.

    The default configuration works for most cases, as shown below. No need to modify the IPv4 address if it does not conflict with your upstream router's gateway.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    (The IPv6 on GL.iNet is disabled by default. If you want to use IPv6 address, please enable IPv6 on your router.)
    
    If you notice that the IPv4 address conflicts with your upstream router's gateway, modify the address to another one such as **10.1.0.1/24** and click **Apply**. Ensure the "/24" CIDR notation is included to avoid connectivity issues.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    For example, if there's an Xfinity router in the upstream of a GL.iNet router, the Xfinity router's IP might be 10.0.0.1, which will conflict with the WireGuard Server's Tunnel IP when the GL.iNet router is set up as a WireGuard server, so you need to make the above changes.
    
    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Add a profile.

    Switch to **Profiles** tab, click the **Add** button to generate a profile for your device.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    Set a descriptive name and click **Apply** to continue.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}
    
    If you need to set advanced settings, click **Set More**. Then click **Apply** to continue.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Add route rules if needed"

        It is not necessary to add route rules in most cases.
        
        If you want to access WireGuard client's LAN devices from server, please switch to the **Route Rules** tab on the **WireGuard Server** page to set the route rules. Click [here](../tutorials/wireguard_server_access_to_client_lan_side.md) for more instructions.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        Otherwise, turn to Step 4 to download a client configuration.

4. Download configuration.

    After adding a profile and apply, it will generate a configuration file in three formats: QR code, plain text, and .conf file. Choose your preferred method to obtain the configuration file.

    - **QR code**: Suitable for end devices (e.g., smartphone, tablet, laptop) with the WireGuard App installed. If you want to set a certain device as a WireGuard client, simply open the WireGuard App, scan the QR code, and the configuration will be automatically imported.
    
        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: In plain text format, you can review configuration details and conveniently copy-paste them elsewhere for manual configuration, such as the WireGuard App or a GL.iNet router.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: Click the **Download** button to save the .conf file to your local device. It is also convenient and can be directly uploaded to the WireGuard app or a GL.iNet router.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    If required, you can specify the server address from among the public IP, DDNS domain, and current WAN IP. This feature has been available since firmware v4.8. Once changed, the server address in the configuration file will be updated simultaneously.
    
    For example, it is recommended to enable [DDNS](ddns.md) and use DDNS domain as the server address if your network's public IP changes frequently. 
    
    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Start WireGuard server.

    Click the **Start** button in the upper right corner to start WireGuard server.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    The connection status will be displayed on the same page.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Check if WireGuard Server is working properly

You can check the server connection status on the **WireGuard Server** page. 

If it shows upload/download traffic statistics and online connected devices, it means the WireGuard server is running and there are WireGuard clients connected to it.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

If it shows 0 traffic and 0 client, it means that there's no WireGuard client connected.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

To verify if the WireGuard Server is functioning properly, please import the previously exported WireGuard configuration to a device on a different network (not the same local network as the server). Test the VPN connectivity and the device's public IP address.

The simplest method is to use a smartphone with the official [WireGuard App](https://www.wireguard.com/install){target="_blank"} installed. First, disable the smartphone's Wi-Fi and connect exclusively to the internet via cellular data (4G/5G). Then open the WireGuard App, import the configuration file, and initiate the connection. Check if the smartphone can access the internet and if its IP address matches the WireGuard Server's IP.

If the connection fails, there are several common reasons:

* The Internet Service Provider doesn't assign you a public IP address. Please check [here](#make-sure-you-have-a-public-ip-address).
* You may need to set up port forwarding. Please check [here](#confirm-if-port-forwarding-is-required).
* The port used for the WireGuard Server is blocked by your Internet Service Provider. Change to another port, or contact the Internet Service Provider for further assistance.
* Some countries/regions may block the VPN connection.

## WireGuard Client App

Please refer to WireGuard Official Website: [https://www.wireguard.com/install](https://www.wireguard.com/install){target="_blank"}

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.