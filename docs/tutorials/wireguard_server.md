# Setup WireGuard Server on GL.iNet router

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, [simpler](https://www.wireguard.com/quickstart/){target="_blank"}, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. 

GL.iNet routers have pre-installed WireGuard Server and Client.

---

## Make sure Internet Service Provider assigns you a public IP address

Please check if you Internet Service Provider assigns you a public IP address [here](../how_to_check_if_isp_assigns_you_a_public_ip_address).

**If no, you can't connect to the WireGaurd Server.**

An alternative method is to use a reverse proxy solution, we suggest [AstroRelay](https://www.astrorelay.com/){target="_blank"}.

## Network Topology

* If GL.iNet router is the main router in your network, this is simple, please move to the next step.
* If you already have a main router, then the GL.iNet router is under the main router, you may need to setup a port forwarding on the main router.
* If you already have a main router, the GL.iNet router is several levels below it and you need to set up port forward on each level.

## Setup WireGuard Server

Access to web Admin Panel, on the left side -> VPN -> WireGuard Server.

1. Click **Generate Configuration**.

    ![wireguard server generate configuration](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_generate_configuration.png){class="glboxshadow"}

2. Apply the configuration

    The default configuration works for most cases. Also modify it according to your network situation, click the **Apply** button after modification.

    ![wireguard server apply configuration](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_apply_configuration.png){class="glboxshadow"}

3. Add a profile

    Switch to **Profiles** tab, generate a profile for your device by click the **Add** button.

    ![wireguard server profiles](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_profiles.png){class="glboxshadow"}

    Enter a descriptive name.

    ![wireguard server profile setting](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_profile_setting.png){class="glboxshadow"}
    
    **Set More** is for advanced settings.

    ![wireguard server profile advanced setting](https://static.gl-inet.com/docs/en/4/tutorials/wireguard_server/wireguard_server_profile_setting_more.png){class="glboxshadow"}

    Click **Apply** to continue. It will generate a profile. If you want to generate the profile with DDNS instead of IP, please enable DDNS first.

    Switch tab and click **Download** the QRCode or profile.

4. Start WireGuard server

    Click **Start** to start WireGuard server.