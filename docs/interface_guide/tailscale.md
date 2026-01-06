# Tailscale

Tailscale is a VPN service that makes the devices and applications you own accessible anywhere in the world, securely and effortlessly. For more information about Tailscale, please visit [Tailscale official website](https://tailscale.com/).

The Tailscale feature on GL.iNet routers, available since firmware V4.2, allows the router to join a Tailscale virtual network. Once connected, you can access the router remotely, including its WAN and LAN resources.

**Note**: 

1. Since Tailscale is based on WireGuard, it is not recommended to use Tailscale simultaneously with any of the following features or services, as this may cause routing conflicts: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, AstroWarp.

2. This feature is currently in beta, and may have some bugs.

3. GL.iNet routers are **not yet available as exit nodes**.

## Supported models

??? "Supported Models"
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Unsupported Models"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Set up Tailscale network

The following is an example of the GL-MT2500.

1. Bind your devices.

    Please register a Tailscale account first, then bind one or two devices (e.g., smartphone, laptop) to your Tailscale account for testing purposes. 

    After binding, you will be able to see your devices and their status in the Tailscale Admin console.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Enable Tailscale on GL.iNet router.

    Log in to your router's web Admin Panel, and navigate to **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Toggle to enable Tailscale, then click **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

3. After a short while, the interface will show a **Device Bind Link**. Click the Device Bind Link.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    It will show a Tailscale link in the pop-up window. Click the link to redirect to the Tailscale website and log in.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Once logged in, you will be asked to confirm the device you want to connect to. Click **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    When the connection is successful, you will be automatically redirected to the Tailscale admin console. You can see that the IP address of the GL-MT2500 is `100.88.54.21`. Now you can use this IP to access the router.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Test connectivity.

    On devices connected to the same Tailscale network, you can test the connectivity in the following three ways.

    * Use the ping command

        ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

    * SSH into the router

        ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

    * Access web Admin Panel

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Allow Remote Access WAN

If this option is enabled, resources on the device's WAN side can be accessed through the Tailscale virtual network.

For example, as shown in the topology below, if this function is enabled, you can access the `GL-AXT1800` via its IP address (`192.168.29.1`) from `leo-phone`. This is because the GL-AXT1800 is the upper-layer device of the `GL-MT2500`, and the latter is connected to the same Tailscale network as leo-phone.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

The operation steps are as follows.

1. Log in to your router's web Admin Panel, and navigate to **APPLICATIONS** -> **Tailscale**. 

    Enable **Allow Remote Access WAN**, and click **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Go to Tailscale admin console, and it will display an alert that GL-MT2500 has subnets. 

    Click the three-dot icon on the right of GL-MT2500 and select **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Enable the subnet routes.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Now you can access the GL-AXT1800 via its IP address (`192.168.29.1`) on other devices. In fact, you can access all devices within the `192.168.29.0/24` subnet.

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN

If this option is enabled, resources on the device's LAN side can be accessed through the Tailscale virtual network.

For example, as shown in the topology below, if this function is enabled, you can SSH log in to `Ubuntu` via its IP address (`192.168.8.110`) from `leo-phone`. This is because `Ubuntu` is the lower-layer device of the `GL-MT2500`, and the latter is connected to the same Tailscale network as leo-phone.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

The operation steps are as follows.

1. Log in to your router's web Admin Panel, and navigate to **APPLICATIONS** -> **Tailscale**. 

    Enable **Allow Remote Access LAN**, and click **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Go to Tailscale admin console, and it will display an alert that GL-MT2500 has subnets. 

    Click the three-dot icon on the right of GL-MT2500 and select **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Enable the subnet routes.

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Now you can ping or SSH log in to the Ubuntu by its IP address (`192.168.8.110`) on other devices. In fact, you can access all devices within the `192.168.8.0/24` subnet.

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Custom Exit Nodes

The exit node feature lets you route all non-Tailscale internet traffic through a specific device on your network. The device routing your traffic is called an “exit node”.

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

**Note**: If the router's DNS Server is a private IP address that can be accessed only in the local network, you may lose the Internet access when running the exit nodes. Please go to Network > DNS menu and set a manual public DNS server such as 8.8.8.8 as the solution.

Setup Steps:

1. On the device you wish to use as an exit node, select **Run exit node**. On Windows, follow the steps below.

    ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Click **Yes**.

    ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

2. Set up the device as an exit node in the Admin console.

    ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

3. Enable **Custom Exit Nodes** in your GL-router, click the refresh button, and select the IP of the device that has been set up as an exit node from the drop-down menu, then click **Apply**. That is it.

    ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

4. The devices under that GL-router will use the home IP of the **Exit Node** .

[Refer link: Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
