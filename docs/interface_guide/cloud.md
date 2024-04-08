# GL.iNet GoodCloud

## Contents

- [Introduction](#introduction)
- [Setup](#setup)
    - [Enable GoodCloud on router](#enable-goodcloud-on-router)
    - [Sign up GoodCloud account](#sign-up-goodcloud-account)
    - [Add device](#add-device)
    - [Bound info on router web Admin Panel](#bound-info-on-router-web-admin-panel)
    - [Unbind router](#unbind-router)
- [Remote access](#remote-access)
    - [Remote access web Admin Panel](#remote-access-web-admin-panel)
    - [Remote access router's terminal](#remote-access-routers-terminal)
- [Site to Site](../tutorials/goodcloud_site_to_site.md)
- [GoodCloud and VPN](#goodcloud-and-vpn)
- [Turn off cloud](#turn-off-cloud)

## Introduction

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage routers.

Features:

- Check live router status
    - Live online offline status check
    - Live RAM and Load Average check
    - Email alarm about online offline status update

- Set up routers remotely
    - Set up routers (e.g. SSID and Key) remotely
    - Remote SSH
    - Remote access web Admin Panel
    - Share router to others

- Monitoring clients on routers remotely
    - Check who is on your network
    - Realtime traffic monitoring and block clients
    - Email alarm about new client and block

- Operate routers in batch
    - Reboot or upgrade routers in batch

- Site to Site
    - Virtual Office: extend your office network to other offices
    - Business Travel: remote access office's OA, CRM, MySQL systems
    - Smart Home: remote access IP camera, NAS and other devices at home

If you want to bind multiple devices, we have additional features specifically designed for multiple devices. Please feel free to contact [support@glinet.biz](mailto:support@glinet.biz).

## Setup

### Enable GoodCloud on router

On the left side of web Admin Panel -> APPLICATIONS -> GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/enable_goodcloud.png){class="glboxshadow"}

Follow the steps above, to enable the GoodCloud function, which will allow the router to connect to the GoodCloud server.

* **Remote SSH** is for remote access router's terminal via GoodCloud. Check out [here](#remote-access-routers-terminal).

* **Remote Web Access** is for remote access router's web Admin Panel via GoodCloud. Check out [here](#remote-access-web-admin-panel).

* **Data Server**, please choose the server which is nearest your devices located. There are three Data Server, **Asia Pacific**(Japan), **America**(Oregon) and **Europe**(Ireland).

### Sign up GoodCloud account

Visit [GoodCloud website](https://www.goodcloud.xyz){target="_blank"}, sign up then sign in.

If you don't find the verify email, look in spam or check email later. If you have any difficulty with sign up, please send email to [support@glinet.biz](mailto:support@glinet.biz) for help.

For the data server region, please select the region closest to you or the region where you wish the device to connect.

### Add device

On the left side -> Devices -> Bound Devices -> Add Device. There are three methods to bind device to your GoodCloud account, **Auto discover**, **Manually add** and **Bulk import**.

=== "Auto discover"

    If your router and computer(which opened GoodCloud website) are in the same network, please try the **Auto discover**.
    
    Follow the steps below to add your device.

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_device_auto_discover.png){class="glboxshadow"}

    Check out [here](../faq/where_to_find_the_device_id_mac_sn.md) to find the Device ID.

    !!! note

        Input "DDNS/Device ID" here just to verify that the router is really original/valid.

    Click **Refresh** to force auto discover devices again.

=== "Manually add"

    If it can't discover automatically, try **Manually add**. All information that need to input can be found on the back of the router.

    !!! note

        Input "MAC", "SN" and "DDNS" / "Device ID" here just to verify that the router is really original and valid.

    For new models, it has **Device ID** on the back of router.

    ![manually add device](https://static.gl-inet.com/goodcloud/docs/manually-add-device-device-id.png){class="glboxshadow"}

    For old models, it has **DDNS** on the back of the router. Only the first 7 characters of **DDNS** are needed.

    ![manually add device](https://static.gl-inet.com/goodcloud/docs/manually-add-device.png){class="glboxshadow"}

=== "Bulk import"

    **Bulk import** is for user who have a great number of devices to add. By **Bulk import** you can import many devices by a Microsoft excel file.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_device_bulk_import.png){class="glboxshadow"}

### Bound info on router web Admin Panel

After you seccessfully add router to GoodCloud, go back to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, refresh this page, it will display the bound GoodCloud username and date.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_bound_info.png){class="glboxshadow"}

### Unbind router

If you want to unbind the router, go to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, click **Unbind** button.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_unbind.png){class="glboxshadow"}

## Remote access

### Remote access web Admin Panel

Note: Please upgrade to 3.211 to use this feature.

On the left side -> Devices -> Bound Devices

Click the name of the device you want to access, then you will see the icons of **Remote Web Access**.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access_web_admin_panel.png){class="glboxshadow"}

If you can't find the icon, please make sure you have enable it, check out [here](#enable-goodcloud-on-router).

If this feature not work, please try the incognito mode of browser.

### Remote access router's terminal

Note: Please upgrade to 3.211 or above to use this feature.

On the left side -> Devices -> Bound Devices

Click the name of the device you want to access, then you will see the icons of **Remote SSH**.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access_terminal.png){class="glboxshadow"}

If you can't find the icon, please make sure you have enable it, check out [here](#enable-goodcloud-on-router).

If this feature not work, please try the incognito/inPrivate mode of browser.

## Site to Site

Please refer to [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud and VPN

If you enable GoodCloud function and running VPN client at the same time on router, by default, the connection between the router and the GoodCloud server will also go through the VPN, but sometimes the VPN connection is unstable, or the VPN provider mistakenly filters the GoodCloud connection, you can make the GoodCloud connection not go through the VPN by using the following settings.

Go to web Admin Panel, on the left side, VPN -> VPN Dashboard -> VPN Client -> Global Options.

![Services from GL.iNet doesn't Use VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_donot_use_vpn.png){class="glboxshadow"}

It is not recommended to run Site to Site while its nodes are also running VPN client, which can make the network particularly complex.

## Turn off cloud

To stop GoodCloud service, turn it off on router web Admin Panel. Please follow the steps below. No action needed on the GoodCloud website.

![disable cloud](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/turn_off_cloud.png){class="glboxshadow"}

After disable Cloud, the interface is like below.

![after disable cloud](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/after_turn_off_cloud.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
