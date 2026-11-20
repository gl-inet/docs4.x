# Build your own WireGuard home server with two GL.iNet routers {#build-your-own-wireguard-home-server-with-two-glinet-routers}

This article will introduce how to set up your home router as the WireGuard VPN server and your travel router as the WireGuard VPN client to connect together remotely, so that you can use your home IP address with the travel router anywhere.

Watch this video or refer to the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses GL-MT5000 (Brume 3) and GL-MT3600BE (Beryl 7) to demonstrate the VPN setup.)</small>

In the following steps, we take GL-MT6000 (Flint 2) and GL-MT3000 (Beryl AX) as examples:

- GL-MT6000, a home router, will be set up as a WireGuard VPN server. If wireless capacity is not required, our security gateway GL-MT2500 or other models can also be considered.

- GL-MT3000, a travel router, will be set up as a WireGuard VPN client to remotely connect to the VPN server at home.

## Why build your own WireGuard home server {#why-build-your-own-wireguard-home-server}

1. Use your home IP address as your public IP, so your traffic appears to originate from home.
2. Avoid the monthly fees charged by third-party VPN services.
3. Encrypt all internet traffic through the tunnel to your home network to protect your privacy.
4. Reach your home devices and local streaming services from anywhere.

## Preparations {#preparations}

### Check if you have a Public IP {#check-if-you-have-a-public-ip}

First, make sure the GL-MT6000 has a public IP address on its WAN side, so that it can be globally accessed. Otherwise your travel router cannot build up a VPN connection with it while you are traveling.

To check if you have the public IP address, please open a web browser and type in [what is my ip](https://whatismyipaddress.com/){target="_blank"} in the address bar.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

It will show your public IP address. If it matches the WAN IP provided by your ISP for the GL-MT6000, you have a public IP address.

If you don't have a public IP address, here are some methods for your reference.

1. If you have a main router, login to it and check if it gets the public IP from your ISP.
2. Ask your ISP for a public IP address. It may require an extra fee.
3. If the above two methods don't work (e.g., if your network is behind CGNAT), you may try our SD-WAN solution [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}. 

### Check if Port Forwarding is required {#check-if-port-forwarding-is-required}

??? "GL.iNet as Main Router" 

    If your GL.iNet Router is directly connected to a ISP modem via an Ethernet cable, the GL.iNet Router is the Main Router.

    **How to check if your GL.iNet Router connects to the ISP modem directly?**

    Log in to the GL.iNet Admin Panel. Select **INTERNET** from the left sidebar. Check the topology and connection details:

    If directly connected via Ethernet, you will see a section named "Ethernet" with details such as Protocol, IP address, Gateway, etc.

    Taking the following image as an example, the marked IP Address is the WAN IP provided by the ISP for this GL-iNet router. 

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    This WAN IP is a public IP address, thus this GL.iNet router, acting as a Main router, has a public IP and **no need to set a Port Forwarding for it**.

    You just need to set this GL.iNet router as WireGuard server, and a travel router as WireGuard Client connecting to the server. Then a VPN tunnel will be built between them.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}
    
??? "GL.iNet as Sub-Router"

    Set up the **Port Forwarding** on your Main router for the GL.iNet router if the latter is behind NAT.

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Example: A TP-Link Router as your home main router.

    Connect to the Wi-Fi or LAN of your home router. Then login to the web Admin Panel. Check the WAN IP address it obtains from your ISP. In the image below, you can see that your public IP is **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Before setting up port forwarding, we recommend reserving an IP address for the GL.iNet router on your Main router, so that a fixed IP can be assigned to the GL.iNet router.** Otherwise, once the Main router or GL.iNet router restarts, the main router may assign a different IP address to the GL.iNet router, causing the port forwarding rule to fail.

    Then set up the Port Forwarding on your Main router for the GL.iNet router.

    1. Go to “Advanced” and click “virtual Server”, then “Add”.
    
    2. Internal IP (Device IP): It is the IP address assigned to GL.iNet Router, you can find it in the client list of TP-Link
    
    3. External/Internal port:  Please fill both are "51820"
    
    4. Protocol:  You can choose "All or UDP or TCP/UDP"

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **More [Port Forward](how_to_set_up_port_forwarding.md) examples**

## Set up WireGuard server {#set-up-wireguard-server}

1. Log in to the web Admin Panel, and navigate to **VPN** -> **WireGuard Server**. Click **Generate Configuration** (for vpn server initial setup only).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Check the configuration.

    The default configuration works for most cases, as shown below. 

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address**: This is the WireGuard server's Tunnel IP. No need to modify it if it does not conflict with your upstream router's gateway.
    
        If it conflicts with your upstream router's gateway, modify the address to another one, such as **10.1.0.1/24**, then click **Apply**. Ensure the "/24" CIDR notation is included to avoid connectivity issues.
            
        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        For example, if an Xfinity router is in the upstream of a GL.iNet router, the Xfinity router's IP might be 10.0.0.1, which may conflict with this Tunnel IP when some GL.iNet routers are configured as a WireGuard server, thus you may need to make the above changes. Skip this if there's no conflict.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**: IPv6 is disabled by default on GL.iNet routers. To use an IPv6 address, enable [IPv6](../interface_guide/ipv6.md) on your router.
    
    - **Listen Port**: **Listen Port**: The UDP port the WireGuard server listens on. It is set to `51820` by default, which is the conventional WireGuard port. Keep the default unless that port is already in use on your network; if you change it, every client profile must use the same port in its `Endpoint` (`your_ddns:port`).

    - **Enable Obfuscation**: When enabled, this VPN server uses the AmneziaWG obfuscation protocol to disguise VPN traffic. We recommend keeping the default obfuscation settings and changing them only if you are familiar with these parameters. See the following links.

        - [AmneziaWG Obfuscation on GL.iNet routers](../faq/amneziawg_obfuscation.md)  
        - [How to set up VPN Obfuscation on GL.iNet routers](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Add a profile.

    Switch to **Profiles** tab, click the **Add** button to generate a profile for your device.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Set a descriptive name and click **Apply** to continue.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}
    
    If you need to set advanced settings, click **Set More**. Then click **Apply** to continue.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Add route rules if needed"

        It is not necessary to add route rules in most cases.
        
        If you want to access WireGuard client's LAN devices from server, please switch to the **Route Rules** tab on the **WireGuard Server** page to set the route rules. Click [here](../tutorials/wireguard_server_access_to_client_lan_side.md) for more instructions.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Otherwise, turn to Step 4 to download a client configuration.

4. Download configuration.

    After adding a profile and apply, it will generate a configuration file in three formats: QR code, plain text, and .conf file. Choose your preferred method to obtain the configuration file.

    - **QR code**: Suitable for end devices (e.g., smartphone, tablet, laptop) with the WireGuard App installed. If you want to set a certain device as a WireGuard client, simply open the WireGuard App, scan the QR code, and the configuration will be automatically imported.
    
        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: In plain text format, you can review configuration details and conveniently copy-paste them elsewhere for manual configuration, such as the WireGuard App or a GL.iNet router.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: Click the **Download** button to save the .conf file to your local device. It is also convenient and can be directly uploaded to the WireGuard app or a GL.iNet router.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    If required, you can specify the server address from among the public IP, DDNS domain, and current WAN IP. This feature has been available since firmware v4.8. Once changed, the server address in the configuration file will be updated simultaneously.
    
    For example, it is recommended to enable [DDNS](ddns.md) and use DDNS domain as the server address if your network's public IP changes frequently. 
    
    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Click the **Start** button in the upper right corner to start your WireGuard server. The connection status will be displayed on the same page.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Set up WireGuard client {#set-up-wireguard-client}

### Change the LAN IP {#change-the-lan-ip}

Since we use GL-MT6000 and GL-MT3000 as examples in this tutorial, whose default LAN IPs are both **192.168.8.1**, we need to change one of them to a different LAN IP to avoid conflict. 

Below are steps to change the LAN IP of GL-MT3000 (the WireGuard client).

Log in to the web Admin Panel of GL-MT3000, go to **NETWORK** -> **LAN** to change its LAN IP. For example, you can change it from the default 192.168.8.1 to `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Add the configuration {#add-the-configuration}

On the web Admin Panel of GL-MT3000, go to **VPN** -> **WireGuard Client**, and click **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Create a group on the left and set a name, then select the configuration file to upload or drag it to the upload box on the right.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

After the file passes verification, click **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

You can also click **Manually Add Configuration** and paste the configuration text, then click **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

The configuration file will be displayed on the WireGuard Client page once it is uploaded successfully.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Start the connection {#start-the-connection}

Click the three-dot icon and click **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Wait a few minutes. Once it is connected successfully, a green dot will light up.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Turn to **VPN Dashboard**, and you will see that your client is connecting to the server with your home public IP. The page may vary slightly depending on the firmware version.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Log in back to the web Admin Panel of GL-MT6000 (the WireGuard server), go to **VPN** -> **WireGuard Server** (or go to **VPN** -> **VPN Dashboard** if you use firmware v.4.7 and earlier), and you will also see the connection status, indicating that the client is connected.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(WireGuard Server page in FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(VPN Dashboard page in FW v4.7 and earlier)</small>

## Prep for remote VPN fixes ahead {#prep-for-remote-vpn-fixes-ahead}

Pre-bind both routers to your GoodCloud account before traveling. This allows you to perform remote troubleshooting if your VPN connection fails due to configuration or other network issues. Remote access only works when the routers remain powered on and connected to the Internet.

---

Related Articles

- [Set Up WireGuard Server on GL.iNet Routers](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
