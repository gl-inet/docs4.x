# Set Up WireGuard Server on GL.iNet Routers

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, [simpler](https://www.wireguard.com/quickstart/){target="_blank"}, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. 

---

## Make sure Internet Service Provider assigns you a public IP address

Please check if you Internet Service Provider assigns you a public IP address [here](../how_to_check_if_isp_assigns_you_a_public_ip_address).

**If not, you can't connect to the WireGaurd Server.**

An alternative method is to use a reverse proxy solution, we suggest [AstroRelay](https://www.astrorelay.com/){target="_blank"}.

## Network Topology

* If GL.iNet router is the main router in your network, this is simple, please move to the next step.
* If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a port forwarding on the main router.
* If you already have a main router, the GL.iNet router is several levels below it and you need to set up port forward on each level.

## Setup WireGuard Server

Access to web Admin Panel, on the left side -> VPN -> WireGuard Server.

1. Click **Generate Configuration** (Only the first time).

    ![wireguard server generate configuration](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_generate_configuration.png){class="glboxshadow"}

2. Apply the configuration

    The default configuration works for most cases. If you found the IPv4 address conflict with your upper router's gateway, click the **Apply** button after modification. You can modify it as **10.1.0.1/24** 

    ![wireguard server apply configuration](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_apply_configuration.png){class="glboxshadow"}

    ![xfinitygateway](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    For **Set Key Manually**.

    ![wireguard server set key manually](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_set_key_manually.png){class="glboxshadow"}

3. Add a profile

    Switch to **Profiles** tab, generate a profile for your device by click the **Add** button.

    ![wireguard server profiles](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_profiles.png){class="glboxshadow"}

    Enter a descriptive name.

    ![wireguard server profile setting](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_profile_setting.png){class="glboxshadow"}
    
    **Set More** is for advanced settings.

    ![wireguard server profile advanced setting](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_profile_setting_more.png){class="glboxshadow"}

    Click **Apply** to continue. It will generate a profile.
    
    ![download wireguard client configuration](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/download_wireguard_client_configuration.png){class="glboxshadow"}

    If your network's public IP changes from time to time, you can enable [DDNS](../ddns/), then using DDNS domain in the configuration.

    Click **Download** to save the profile.

4. Start WireGuard server

    Click the **Start** button in the upper right corner to start WireGuard server. Go to VPN Dashboard page to check its status and other settings.

    ![start wireguard server](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/start_wireguard_server.png){class="glboxshadow"}

### To check if WireGuard Server is working properly

Many people mis-understandstool once they saw the server is up and think it is connected. The server can be up even you forward a wrong port or wrong address.

![wgconnected](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wgconnected.jpg){class="glboxshadow"}

To check if WireGaurd Server is working properly, we can use another device connected to another network and use the WireGuard configuration we exported earlier to connect and see whether it connects properly and whether the IP address is the IP of WireGuard Server.

The simpliest way is to use a cell phone with [WireGuard official client app](https://www.wireguard.com/install){target="_blank"} installed, turn off its Wi-Fi connection, and only connect to Internet via 3G/4G/5G. Then open the WireGaurd app, import the WireGaurd configuration from QR code. Enable the connection, check if the phone has Internet access and whether its IP address is the IP of your WireGuard Server.

There are several common reasons cause failure:

* The Internet Service Provider doesn't assign you a public IP address, please check [here](#make-sure-internet-service-provider-assigns-you-a-public-ip-address).
* You may need setup port forwarding, please check [here](#network-topology).
* The port you are using for WireGuard Server is blocked by the Internet Service Provider, change to another port, or contact the Internet Service Provider.
* Some countries/regions may block the VPN connection.

## WireGuard Client App

We can use another GL.iNet router as WireGuard Client, or use their official app on other devices with various OS.

- Please refer to WireGuard Official Website: [https://www.wireguard.com/install](https://www.wireguard.com/install){target="_blank"}

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
