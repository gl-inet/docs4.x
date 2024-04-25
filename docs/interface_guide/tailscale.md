# Tailscale

Tailscale feature available since V4.2

Tailscale is a VPN service that makes the devices and applications you own accessible anywhere in the world, securely and effortlessly. For more information about Tailscale, please access [their website](https://tailscale.com/).

The Tailscale feature in GL.iNet router allow the router to join the Tailscale virtual network, then you can access it remotely, even to its WAN or LAN resources.

**Note**: Because Tailscale is based on WireGuard, it is not recommended to use the Tailscale feature with the OpenVPN Client or WireGuard Client at the same time, as there may be bugs.

**Note**: This feature is currently in beta, and may have some bugs.

## Supported models

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X3000 (Spitz AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-AXT1800 (Slate AX)          | √         |
| GL-A1300 (Slate Plus)          | √         |
| GL-MT2500/GL-MT2500A (Brume 2) | √         |
| GL-SFT1200 (Opal)              | -         |
| GL-S1300 (Convexa-S)           | -         |
| GL-MT1300 (Beryl)              | -         |
| GL-AX1800 (Flint)              | √         |
| GL-AR750S (Slate)              | -         |
| GL-XE300 (Puli)                | -         |
| GL-X750 (Spitz)                | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-AP1300 (Cirrus)             | -         |
| GL-X300B (Collie)              | -         |
| GL-MV1000/GL-MV1000W (Brume)   | √         |

## Setup

The following is an example of the GL-MT2500.

### Binding

Please register a Tailscale account first. For testing purposes, first bind one or two devices to your Tailscale account. After binding, you will be able to see your devices and their status in the Tailscale Admin console.

![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

On the left side -> APPLICATIONS -> Tailscale

![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

Toggle to enable Tailscale, then click **Apply**.

![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

It will show a **Device Bind Link**. Click the Device Bind Link.

![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

It will pop up and show a tailscale link, click it.

![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

The link will open in your browser and ask you to log in to your Tailscale account.

Once logged in, you will be asked to confirm the device you want to connect to. Click **Connect**.

![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

When the connection is successful, you will automatically be redirected to the admin console. You can see here that the IP of the GL-MT2500 is `100.88.54.21`, and you can use this IP to access the router.

![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

### Test connectivity

Now that the GL-MT2500 is connected to the Tailscale virtual network, you can test it on other devices as fellows three ways.

* Use ping command

    ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

* SSH to the router

    ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

* Access web Admin Panel

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Allow Remote Access WAN

If this option is enabled, the resources on the WAN side of the device will be allowed to be accessed via the Tailscale virtual network.

For example, as shown below, if this function is enabled, you can access `GL-AXT1800` by its IP(`192.168.29.1`) from `leo-phone`, because `GL-AX1800` is connected to the WAN port of `GL-MT2500`, which is the upper layer device of `GL-MT2500`.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

The operation steps are as follows.

1. Enable Allow Remote Access WAN.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Go to admin console of Tailscale, it will display an alert that GL-MT2500 has subnets. Click on the GL-MT2500 menu and select **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Enable the subnet routes.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Now you can access GL-AXT1800 by its IP(`192.168.29.1`) on other machines. You can actually access the devices at `192.168.29.0/24`.

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow"}

## Allow Remote Access LAN

If this option is enabled, the resources inside the device LAN will be allowed to be accessed via the Tailscale virtual network.

For example, as show below, if this function is enabled, you can SSH to `Ubuntu` by its IP(`192.168.8.110`) from `leo-phone`, because `Ubuntu` is connected to the LAN port of `GL-MT2500`, which is the lower layer device of `GL-MT2500`.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

The operation steps are as follows.

1. Enable Allow Remote Access LAN.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Go to admin console of Tailscale, it will display an alert that GL-MT2500 has subnets. Click on the GL-MT2500 menu and select **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Enable the subnet routes.

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Now you can ping or SSH the  by its IP(`192.168.8.110`) on other devices. You can actually access the devices at `192.168.8.0/24`.

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.jpg){class="glboxshadow gl-50-desktop"}

## Custom Exit Nodes

The exit node feature lets you route all non-Tailscale internet traffic through a specific device on your network. The device routing your traffic is called an “exit node”.

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

**Note**: GL.iNet router is not yet available as an exit node, this feature is still under development.

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

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
