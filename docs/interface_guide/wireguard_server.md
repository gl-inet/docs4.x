# Set Up WireGuard Server on GL.iNet Routers

<iframe width="560" height="315" src="https://www.youtube.com/embed/qLEj9zoiYRs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, [simpler](https://www.wireguard.com/quickstart/){target="_blank"}, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. 

---

## Make sure you have a public IP address

Please check if your Internet Service Provider assigns you a public IP address [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

**If not, your router cannot be set as the WireGuard Server.**

Alternative methods:

1. If you have a main router, you shall login to it and check if it gets the Public IP from your ISP.
2. Ask your ISP for a Public IP address. It may require an extra fee.
3. If the above two ways don't work, for example, if you are in a CGNAT, you can take the reverse proxy method such as [Astrorelay](../tutorials/how_to_set_up_wireguard_server_via_astrorelay.md). Alternatively, you may try an SDWAN solution - [AstroWarp](https://www.astrowarp.net/){target="_blank"}. 

## Confirm if Port Forwarding is required

**Network Topology**

??? "GL.iNet is the Main Router"
    
    * If GL.iNet router is the main router in your network, this is simple, please move to the [next step](#setup-wireguard-server).

??? " GL.iNet is the Sub-Router"

    * If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) on the main router.
    
    * If you already have a main router, the GL.iNet router is several levels below it and you need to set up [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) on each level.

## Setup WireGuard Server

Access to web Admin Panel, on the left side -> VPN -> WireGuard Server.

1. Click **Generate Configuration** (for vpn server initial setup only).

    ![wireguard server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_generate_configuration.png){class="glboxshadow"}

2. Apply the configuration.

    The default configuration works for most cases. 
    
    If you find that the IPv4 address conflicts with your upstream router's gateway, modify the address to others such as **10.1.0.1/24** and click **Apply**. Ensure the "/24" subnet mask is included to avoid connectivity issues.

    ![wireguard server apply configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_apply_configuration.png){class="glboxshadow"}

    For example, if you use an Xfinity router in the upstream of GL.iNet router, the Xfinity router's IP might be 10.0.0.1, which will be same as our WireGuard Server IP, then you will need to do the above changes.
    
    ![xfinitygateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Add a profile.

    Switch to **Profiles** tab, generate a profile for your device by clicking the **Add** button.

    ![wireguard server profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profiles.png){class="glboxshadow"}

    Enter a descriptive name.

    ![wireguard server profile setting](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profile_setting.png){class="glboxshadow"}
    
    If you need to set advanced settings, click **Set More**.

    ![wireguard server profile advanced setting](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profile_setting_more.png){class="glboxshadow"}

    Click **Apply** to continue. It will generate a profile.
    
    ![download wireguard client configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_wireguard_client_configuration.png){class="glboxshadow"}

    If your network's public IP changes from time to time, you can enable [DDNS](ddns.md) by using DDNS domain in the configuration.

    Click **Download** to save the profile.

4. Start WireGuard server.

    Click the **Start** button in the upper right corner to start WireGuard server. Go to VPN Dashboard page to check its status and other settings.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wireguard_server.png){class="glboxshadow"}

## Check if WireGuard Server is working properly

Many people assume that the server has been successfully established as soon as they see it started, but in fact, it is not. 

Even if you forward the wrong port or address, the server can still run.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgconnected.jpg){class="glboxshadow"}

To verify if the WireGuard Server is functioning properly, use another device on a separate network and import the previously exported WireGuard configuration to test connectivity and check the assigned IP address.

The simplest method is to use a smartphone with the official [WireGuard App](https://www.wireguard.com/install){target="_blank"} installed. First, disable the phone’s Wi-Fi and connect exclusively to the internet via cellular data (3G/4G/5G). Then launch the WireGuard app, import the pre-exported configuration file, and initiate the connection. Confirm whether the phone gains internet access and whether its IP address matches the WireGuard Server’s IP.

If the connection fails, there are several common reasons:

* The Internet Service Provider doesn't assign you a public IP address. Please check [here](#make-sure-you-have-a-public-ip-address).
* You may need to set up port forwarding. Please check [here](#confirm-if-port-forwarding-is-required).
* The port you are using for WireGuard Server is blocked by the Internet Service Provider.Change to another port, or contact the Internet Service Provider for further assistance.
* Some countries/regions may block the VPN connection.

## WireGuard Client App

Please refer to WireGuard Official Website: [https://www.wireguard.com/install](https://www.wireguard.com/install){target="_blank"}

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.