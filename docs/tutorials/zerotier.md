# ZeroTier

ZeroTier feature available since V4.2

ZeroTier is a software-based virtual private network (VPN) that enables secure, encrypted communications between devices over the internet. It creates a private, virtual network that allows devices to communicate as if they were on the same local network, regardless of their physical location or network topology. ZeroTier is designed to be easy to set up and use, and offers features such as end-to-end encryption, network segmentation, and network bridging capabilities.

The ZeroTier feature in GL.iNet router allow the router to join the ZeroTier virtual network, then you can access it remotely, even to its WAN or LAN resources.

**Note**: Because ZeroTier is based on WireGuard, it is not recommended to use the ZeroTier feature with the OpenVPN Client or WireGuard Client at the same time, as there may be bugs.

**Note**: This feature is currently in beta, and may have some bugs.

## Supported models

| Router Model | Support |
| :----------- | :-------: |
| GL-X3000 (Spitz AX) | √ |
| GL-MT3000 (Beryl AX) | √ |
| GL-AXT1800 (Slate AX) | √ |
| GL-A1300 (Slate Plus) | √ |
| GL-MT2500/GL-MT2500A (Brume 2) | √ |
| GL-AX1800 (Flint) | √ |

## Setup

The following is an example of the GL-MT2500.

Refer link: [Getting Started of ZeroTier documentation](https://docs.zerotier.com/getting-started/getting-started/).

1. Create your first ZeroTier network

    Refer to [ZeroTier's official Getting Started documentation](https://docs.zerotier.com/getting-started/getting-started/) to create a ZeroTier account and network. Remember to take note of the Network ID, which is a 16-digit combination of letters and numbers, as it will be needed when connecting other devices later on.

    ![zerotier network id](https://static.gl-inet.com/docs/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Enable ZeroTier on GL.iNet router

    Access router's web Admin Panel, on the left side -> APPLICATIONS -> ZeroTier

    Enable the toggle button, fill in the Network ID in the first step then click **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    After a while the interface will indicate that authorization is required, which we will handle in the next step.

    To facilitate testing, add another device (such as a computer or phone) to the ZeroTier network following the instructions in [this document](https://docs.zerotier.com/getting-started/getting-started/#setup-the-zerotier-app).

3. Authorize your device on your network

    ![zerotier central](https://static.gl-inet.com/docs/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

    To authorize your device on your network, click on the ZeroTier Central icon and navigate to the Members section of the settings for your network on the ZeroTier website. 
    
    ![zerotier members, auth](https://static.gl-inet.com/docs/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Locate the new device and click on the Auth checkbox to authorize it. Customize the name of the device if desired.

    **Note**: The device's Address should be displayed on the ZeroTier page of the router, but this feature may be added in future versions. To confirm the current Address of the ZeroTier on your router, SSH into the router and use the "zerotier-cli info" command.

    ![zerotier managed ip](https://static.gl-inet.com/docs/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

    After a short while, ZeroTier will assign a Managed IP to the device. Take note of this IP address as it will be used in the testing step.

## Test connectivity

On another device that is also on the same ZeroTier network, use a web browser to access the router's web Admin Panel using the Managed IP obtained in the previous step.

Normally, you will be able to access the web Admin Panel of the router. You can also use the `ping` command mentioned in the [official documentation](https://docs.zerotier.com/getting-started/getting-started/#test-connectivity) to test it.

![web admin panel](https://static.gl-inet.com/docs/en/4/tutorials/zerotier/web_admin_panel.png)

## Allow Remote Access WAN

Coming soon.

## Allow Remote Access LAN

Coming soon.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
