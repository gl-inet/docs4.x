# Tailscale

Tailscale feature available since V4.2

Tailscale is a VPN service that makes the devices and applications you own accessible anywhere in the world, securely and effortlessly. For more information about Tailscale, please access [their website](https://tailscale.com/).

The Tailscale feature in GL.iNet router allow the router to join the Tailscale and you can remote access it.

**Note**: This feature is currently in beta, and may have some bugs.

## Supported models

| Router Model | Support Tailscale |
| :----------- | :-------: |
| GL-MT3000 (Beryl AX) | √ |
| GL-AXT1800 (Slate AX) | √ |
| GL-A1300 (Slate Plus) | √ |
| GL-MT2500/GL-MT2500A (Brume 2) | √ |
| GL-MT1300 (Beryl) | √ |
| GL-AX1800 (Flint) | √ |

## Setup

## Binding

Please register a Tailscale account first. For testing purposes, first bind one or two devices to your Tailscale account. After binding, you will be able to see your devices and their status in the Tailscale Admin console.

![tailscale admin console](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

On the left side -> APPLICATIONS -> Tailscale

The following is an example of the GL-MT2500.

![glinet tailscale disabled](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

Toggle to enable Tailscale, then click **Apply**.

![glinet enable tailscale](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

It will show a **Device Bind Link**. Click the Device Bind Link.

![glinet bind link](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

It will pop up and show a tailscale link, click it.

![glinet bind link](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

The link will open in your browser and ask you to log in to your Tailscale account.

Once logged in, you will be asked to confirm the device you want to connect to. Click **Connect**.

![tailscale confirm connect device](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow"}

When the connection is successful, you will automatically be redirected to the admin console. You can see here that the IP of the GL-MT2500 is 100.69.203.111, and you can use this IP to access the router.

![tailscale admin console](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

### Testing

Now that the GL-MT2500 is connected to the Tailscale virtual network, you can test it in the following way.

* Use ping command

    ![ping](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

* SSH to the router

    ![ssh](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

* Access web Admin Panel

    ![web admin panel](https://static.gl-inet.com/docs/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow"}

## Allow Remote Access WAN

Coming soon.

## Allow Remote Access LAN

Coming soon.

## Custom Exit Nodes

Coming soon.
