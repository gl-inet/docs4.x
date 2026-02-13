# VPN Obfuscation

## What is VPN Obfuscation

VPN obfuscation is a technique that disguises VPN traffic to look like regular internet traffic. This helps users bypass network restrictions and censorship, especially in regions with strict internet policies.

- It masks VPN characteristics to prevent detection by ISPs, firewalls, or Deep Packet Inspection (DPI).

- It makes your VPN connection appear as standard web traffic, improving connection stability and success rate in restricted networks.

## What is AmneziaWG

AmneziaWG is a VPN protocol built on WireGuard, with built-in traffic obfuscation. It retains the core benefits of WireGuard, such as high speed, lightweight design, and low latency, while adding a dedicated obfuscation module. This module effectively hides VPN traffic patterns, allowing both individual and business users to protect online privacy, bypass regional restrictions, and avoid connection interruptions caused by strict network controls.

AmneziaWG is compatible with a wide range of devices, including Windows, macOS, iOS, Android, Linux, and routers, delivering reliable obfuscated VPN connections across all scenarios.

Currently, several GL.iNet routers (such as **Brume 3** and **Beryl AX**) support the AmneziaWG protocol in specific firmware versions. Full support will be officially available in firmware version 4.9 and gradually extended to more models.

## Set up VPN Obfuscation on GL.iNet routers

Below are two typical scenarios for setting up AmneziaWG VPN obfuscation on GL.iNet routers.

### Scenario 1. Using two GL.iNet routers

This scenario uses two GL.iNet routers to establish a VPN obfuscation connection via the AmneziaWG protocol.

- **Brume 3 (GL-MT5000)**: Acting as a VPN Server for home use.
- **Beryl AX (GL-MT3000)**: Acting as a portable VPN Client for on-the-go use. 

#### Set up VPN Server

1. Log in to the Brume 3's web Admin Panel. 

    Connect a device (e.g., your laptop or PC) to the Brume 3's LAN port via an Ethernet cable. Open a browser and enter the default admin address (usually `192.168.8.1`), then log in with your admin password.

2. Complete the Brume 3 initial setup for internet access.

    If the Brume 3 is used as the primary router, connect its WAN port to the upstream network such as an ISP modem. 
    
    If it is not the primary router (i.e., there is another upstream device, such as an ISP router, acting as the primary router), a **port forwarding** setup is required on your primary router. Please refer to [this link](how_to_set_up_port_forwarding.md).

3. Enable DDNS (Optional).

    Enable the DDNS function if your Public IP is not static but dynamic.
    
    From the left sidebar, navigate to **APPLICATIONS** -> **Dynamic DNS**. Toggle on **Enable DDNS**, agree to the **Terms of Service & Privacy Policy**, then click **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. Enable VPN Obfuscation. 

    From the left sidebar, navigate to **VPN** > **WireGuard Server** -> **Configurations** tab, toggle on **Enable Obfuscation**, then click **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    You can customize the obfuscation parameters as needed. We recommend keeping the default settings.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Export configuration file.

    On the **WireGuard Server** page, switch to **Profiles** tab, click the **Add** button to create a configuration file for Beryl AX to connect.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Set a descriptive name (e.g., Travel Router), then click **Apply**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    In the pop-up window, click **Export** to download the config to your local, which will be used latter.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Start the VPN server. 

    At the top of the **WireGuard Server** page, click the **Start** button to run the server. 

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    Then your VPN server with AmneziaWG obfuscation is enabled. You can now connect to this VPN server Brume 3 via the AmneziaWG app, or a GL.iNet router running firmware that supports AmneziaWG obfuscation. 
    
    **Note: Clients that do not support AmneziaWG obfuscation will be unable to connect.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### Set up VPN Client

1. Log in to the Beryl AX's web Admin Panel. 

    Connect a device (e.g., your laptop or PC) to the Beryl AX's Wi-Fi or LAN port via an Ethernet cable. Open a browser and enter the default admin address (usually `192.168.8.1`), then log in with your admin password.

2. Complete the Beryl AX initial setup for internet access.

    **Tips**: Please connect the Beryl AX to a network different from Brume 3. For example, you can enable mobile hotspot for Beryl AX to connect.

3. Upload configuration file. 

    From the left sidebar, navigate to **VPN** > **WireGuard Client**. Add a new group and set a descriptive name (e.g., Home Router).

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Upload the previously exported configuration file on the right side.

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    After uploading the configuration file and passing verification, click **Apply**.

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    The page will refresh, with one configuration file displayed in the list. 
    
4. Start VPN connection.

    Click the three-dot icon and then select **Start**.

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Wait for about 1 minute. If the status indicator turns green, it means the VPN connection is successful.

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Turn to the **VPN Dashboard**, you will see that the Beryl AX has been connected to the Home router Brume 3.

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Double Check (Optional).

    Log in to the Brume 3's web Admin Panel, navigate to **VPN** -> **WireGuard Server**. You will also see an online client, which is Beryl AX, currently connected to this VPN server Brume 3.

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    The VPN connection is complete. All devices on the Beryl AX now access the internet via the Brume 3's gateway, enabling a VPN obfuscation connection.

### Scenario 2. Using a single GL.iNet router

This scenario uses a single GL.iNet router **Brume 3 (GL-MT5000)** as a VPN client to connect to an AmneziaVPN server. 

There is no need to set up your own server. You can establish a VPN obfuscation connection directly using the official AmneziaVPN servers (Amnezia Premium subscription required).

#### Download Configuration

1. Log in to the [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} with your Subscription Key.

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. On the Amnezia Dashboard, turn to the **Connection Assets** -> **Configuration Files**, select a country and download a configuration file to your local for later use.

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

#### Set up VPN Client

1. Log in to the Brume 3's web Admin Panel. 

    Connect a device (e.g., your laptop or PC) to the Brume 3's LAN port via an Ethernet cable. Open a browser and enter the default admin address (usually `192.168.8.1`), then log in with your admin password.

2. Complete the Brume 3 initial setup for internet access.

3. Upload configuration file. 

    From the left sidebar, navigate to **VPN** > **WireGuard Client**. Add a new group and set a descriptive name (e.g., AmneziaVPN).

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Upload the previously exported AmneziaVPN configuration file on the right side.

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    After uploading the configuration file and passing verification, click **Apply**.

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    The page will refresh, with one configuration file displayed in the list. 
    
4. Start VPN connection.

    Click the three-dot icon and then select **Start**.

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Wait for about 1 minute. If the status indicator turns green, it means the VPN connection is successful.

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Turn to the **VPN Dashboard**, you will see that the Brume 3 has been connected to a AmneziaVPN server.

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}
    
    The VPN connection is complete. All devices on the Brume 3 now access the internet via the AmneziaVPN server, enabling a VPN obfuscation connection.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.