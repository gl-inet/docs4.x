# ZeroTier

ZeroTier feature available since V4.2

ZeroTier is a software-based virtual private network (VPN) that enables secure, encrypted communications between devices over the internet. It creates a private, virtual network that allows devices to communicate as if they were on the same local network, regardless of their physical location or network topology. ZeroTier is designed to be easy to set up and use, and offers features such as end-to-end encryption, network segmentation, and network bridging capabilities.

The ZeroTier feature in GL.iNet router allow the router to join the ZeroTier virtual network, then you can access it remotely, even to its WAN or LAN resources.

**Note**: Because ZeroTier is based on WireGuard, it is not recommended to use the ZeroTier feature with the OpenVPN Client or WireGuard Client at the same time, as there may be bugs.

**Note**: This feature is currently in beta, and may have some bugs.

## Supported models

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-BE9300 (Flint 3)            | √         |
| GL-BE3600 (Slate 7)            | √         |
| GL-X2000 (Spitz Plus)          | -         |
| GL-B3000 (Marble)              | √         |
| GL-MT6000 (Flint2)             | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-AXT1800 (Slate AX)          | √         |
| GL-A1300 (Slate Plus)          | √         |
| GL-MT2500/GL-MT2500A (Brume 2) | √         |
| GL-SFT1200 (Opal)              | -         |
| GL-S1300 (Convexa-S)           | -         |
| GL-MT1300 (Beryl)              | -         |
| GL-AX1800 (Flint)              | √         |
| GL-AR750S (Slate)              | -         |
| GL-AR300M Series (Shadow)      | -         |
| GL-MT300N-V2 (Mango)           | -         |
| GL-XE300 (Puli)                | -         |
| GL-E750/GL-E750V2 (Mudi V2)    | -         |
| GL-X750/GL-X750V2 (Spitz)      | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-AP1300 (Cirrus)             | -         |
| GL-X300B (Collie)              | -         |

## Setup

The following is an example of the GL-MT2500.

1. Create your first ZeroTier network

    Refer to [ZeroTier's official Getting Started documentation](https://docs.zerotier.com/getting-started/getting-started/) to create a ZeroTier account and network. Remember to take note of the Network ID, which is a 16-digit combination of letters and numbers, as it will be needed when connecting other devices later on.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Enable ZeroTier on GL.iNet router

    Access router's web Admin Panel, on the left side -> APPLICATIONS -> ZeroTier

    Enable the toggle button, fill in the Network ID in the first step then click **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    After a while the interface will indicate that authorization is required, which we will handle in the next step.

    To facilitate testing, add another device (such as a computer or phone) to the ZeroTier network following the instructions in [this document](https://docs.zerotier.com/getting-started/getting-started/#setup-the-zerotier-app).

3. Authorize your device on your network

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

    To authorize your device on your network, click on the ZeroTier Central icon and navigate to the Members section of the settings for your network on the ZeroTier website. 
    
    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Locate the new device and click on the Auth checkbox to authorize it. Customize the name of the device if desired.

    **Note**: The device's Address should be displayed on the ZeroTier page of the router, but this feature may be added in future versions. To confirm the current Address of the ZeroTier on your router, SSH into the router and use the "zerotier-cli info" command.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

    After a short while, ZeroTier will assign a Managed IP to the device. Take note of this IP address as it will be used in the testing step.

## Test connectivity

On another device that is also on the same ZeroTier network, use a web browser to access the router's web Admin Panel using the Managed IP obtained in the previous step.

Normally, you will be able to access the web Admin Panel of the router. You can also use the `ping` command mentioned in the [official documentation](https://docs.zerotier.com/getting-started/getting-started/#test-connectivity) to test it.

![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

## Allow Remote Access WAN

If this option is enabled, the resources on the WAN side of the device will be allowed to be accessed via the ZeroTier virtual network.

For example, as shown below, if this function is enabled, you can access `GL-AXT1800` by its IP(`192.168.29.1`) from `leo-phone`, because `GL-AX1800` is connected to the WAN port of `GL-MT2500`, which is the upper layer device of `GL-MT2500`.

![zerotier, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

The operation steps are as follows.

1. Enable Allow Remote Access WAN.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    It will prompt you to set up routing rules.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Go to the [my.zerotier.com](https://my.zerotier.com) or click on **ZeroTier Central** in the image above, find the **Advanced** sector of settings panel. Fill in the route (Destination and Via) requested in the previous step. Click **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

    After adding.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. Now you can access GL-AXT1800 by its IP(`192.168.29.1`) on other machines. You can actually access the devices at `192.168.29.0/24`.

    ![zerotier, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow"}

## Allow Remote Access LAN

If this option is enabled, the resources inside the device LAN will be allowed to be accessed via the ZeroTier virtual network.

For example, as show below, if this function is enabled, you can SSH to `Ubuntu` by its IP(`192.168.8.110`) from `leo-phone`, because `Ubuntu` is connected to the LAN port of `GL-MT2500`, which is the lower layer device of `GL-MT2500`.

![ZeroTier, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

The operation steps are as follows.

1. Enable Allow Remote Access LAN.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    It will prompt you to set up routing rules.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Go to the [my.zerotier.com](https://my.zerotier.com) or click on **ZeroTier Central** in the image above, find the **Advanced** sector of settings panel. Fill in the route (Destination and Via) requested in the previous step. Click **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    After adding.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. Now you can ping or SSH the  by its IP(`192.168.8.110`) on other devices. You can actually access the devices at `192.168.8.0/24`.

    ![zerotier, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-50-desktop"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
