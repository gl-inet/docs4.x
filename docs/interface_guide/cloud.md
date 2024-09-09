# GL.iNet GoodCloud

## Contents

- [Introduction](#introduction)
- [Setup your GoodCloud account](#setup-your-goodcloud-account)
    - [For devices running firmware version 4.6 or earlier](#for-devices-running-firmware-version-46-or-earlier)
        - [Enable GoodCloud on router](#enable-goodcloud-on-router)
        - [Sign up GoodCloud account](#sign-up-goodcloud-account)
        - [Add device in your account](#add-device-in-your-account)
        - [Bound info on router web Admin Panel](#bound-info-on-router-web-admin-panel)
        - [Unbind router](#unbind-router)
    - [For devices running firmware version 4.7 or later](#for-devices-running-firmware-version-47-or-later)
        - [Enable Cloud Service on router](#enable-cloud-service-on-router)
        - [Complete GoodCloud account registration and login](#complete-goodcloud-account-registration-and-login)
        - [Bound info on router web Admin Panel](#bound-info-on-router-web-admin-panel_1)
        - [Unbind router](#unbind-router_1) 
- [Manage your devices](#manage-your-devices)
    - [Devices info and status](#devices-info-and-status)
    - [Device detail info](#device-detail-info)  
        - [Device info](#device-info)
        - [Router status](#router-status)
        - [Configuration Details](#configuration-details)
        - [Client list](#client-list)
- [Remote access](#remote-access)
    - [Remote access web Admin Panel](#remote-access-web-admin-panel)
    - [Remote access router's terminal](#remote-access-routers-terminal)
- [Modify Device Settings](#modify-device-settings)
- [Set email alarm](#set-email-alarm)
- [Site to Site](#site-to-site)
- [GoodCloud and VPN](#goodcloud-and-vpn)
- [View Logs](#view-logs)
- [Turn off cloud](#turn-off-cloud)
    - [For devices running firmware version 4.6 or earlier](#for-devices-running-firmware-version-46-or-earlier_1)
    - [For devices running firmware version 4.7 or later](#for-devices-running-firmware-version-47-or-later_1)

## Introduction

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage GL.iNet routers.

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

## Setup your GoodCloud account

Users are required to follow the binding procedures specific to their firmware versions to successfully connect devices to the cloud platform.

Users need to first access the router's web interface (default address: 192.168.8.1) to enable cloud services. After that, they can complete the GoodCloud account registration and device binding on the cloud platform.

### For devices running firmware version 4.6 or earlier

#### Enable GoodCloud on router

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

On the left side of web Admin Panel -> APPLICATIONS -> GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

Follow the steps above, to enable the GoodCloud function, which will allow the router to connect to the GoodCloud server.

* **Remote SSH** is for remote access router's terminal via GoodCloud. Check out [here](#remote-access-routers-terminal).

* **Remote Web Access** is for remote access router's web Admin Panel via GoodCloud. Check out [here](#remote-access-web-admin-panel).

* **Data Server**, please choose the server which is nearest your devices located. There are three Data Server, **Asia Pacific**(Japan), **America**(Oregon) and **Europe**(Ireland).

#### Sign up GoodCloud account

Visit [GoodCloud website](https://www.goodcloud.xyz){target="_blank"}, sign up then sign in.

If you don't find the verify email, look in spam or check email later. If you have any difficulty with sign up, please send email to [support@glinet.biz](mailto:support@glinet.biz) for help.

For the data server region, please select the region closest to you or the region where you wish the device to connect.

#### Add device in your account

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

On the left side -> Devices -> Bound Devices -> Add Device. There are three methods to bind device to your GoodCloud account, **Auto discover**, **Manually add** and **Bulk import**.

=== "Auto discover"

    If your router and computer(which opened GoodCloud website) are in the same network, please try the **Auto discover**.
    
    Follow the steps below to add your device.

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.png){class="glboxshadow"}

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

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.png){class="glboxshadow"}

#### Bound info on router web Admin Panel

After you seccessfully add router to GoodCloud, go back to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, refresh this page, it will display the bound GoodCloud username and date.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Unbind router

If you want to unbind the router, go to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, click **Unbind** button. 

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

Alternatively, you can remove the corresponding device from the Bound Devices List on the GoodCloud platform. The router's web interface will then synchronize to reflect the latest device binding status.

If you encounter any difficulties, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance.

### For devices running firmware version 4.7 or later

#### Enable Cloud Service on router

On the left side of web Admin Panel -> CLOUD SERVICE -> GoodCloud. 点击 Get start，右上角会有Cloud Service弹窗，点击 Enable 按钮来开启Cloud Service。

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

Follow the steps above, to enable the GoodCloud function, which will allow the router to connect to the GoodCloud server.

#### Complete GoodCloud account registration and login

![register goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/register_1.png){class="glboxshadow"}

After enabling cloud services, click the "Sign Up" button to register a Cloud account. If you already have an account, simply log in.

![register goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/register_2.png){class="glboxshadow"}

Follow the steps above to register a GoodCloud account. Once registration is complete, the router will automatically bind to this account. 

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

If you don’t see the verification email, check your spam folder or try again later. For any difficulties with sign-up, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance. 

#### Bound info on router web Admin Panel

After you seccessfully add router to GoodCloud, go back to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, refresh this page, it will display the bound GoodCloud username and date.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

In this interface, you can enable or disable the router's remote access feature.

* **Remote SSH** is for remote access router's terminal via GoodCloud. Check out [here](#remote-access-routers-terminal).

* **Remote Web Access** is for remote access router's web Admin Panel via GoodCloud. Check out [here](#remote-access-web-admin-panel).

Click View Logs will show API call logs by GoodCloud.

#### Unbind router

If you want to unbind the router, go to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, click **Unbind** button. 

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

Alternatively, you can remove the corresponding device from the Bound Devices List on the GoodCloud platform. The router's web interface will then synchronize to reflect the latest device binding status.

If you encounter any difficulties, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance.

## Manage your devices

### Devices info and status

Sign in [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, check at left side -> Bound Devices. Users can view all devices bound to their account and perform actions such as configuration deployment, reboot, and reset on the devices.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

By clicking the icon on the far right of the list header, users can customize the display and order of the columns to focus on the device information that matters most to them.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Device detail info

At left side -> Bound Devices, click the name of an device, it will open a page to manage this device of WiFi, Clients and view router info, memory usage, up time, and load average.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_detail_info.png){class="glboxshadow"}

#### Device info

![Device info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_info.png){class="glboxshadow"}

#### Router status

![Router status](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/router_status.png){class="glboxshadow"}

#### Configuration Details

The page will display configuration information for WiFi, Repeater, Ethernet, and Tethering settings of the device. Below is an example of the details page layout.

![Configuration Details](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/configuration_details.png){class="glboxshadow"}

#### Client list

![Client list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/client_list.png){class="glboxshadow"}

## Remote access

### Remote access web Admin Panel

Note: Please upgrade to 3.211 to use this feature.

On the left side -> Devices -> Bound Devices

Click the name of the device you want to access, then you will see the icons of **Remote Web Access**.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/access_web_admin_panel.png){class="glboxshadow"}

If you can't find the icon, please make sure you have enable it, check out [here](#enable-goodcloud-on-router).

If this feature not work, please try the incognito mode of browser.

### Remote access router's terminal

Note: Please upgrade to 3.211 or above to use this feature.

On the left side -> Devices -> Bound Devices

Click the name of the device you want to access, then you will see the icons of **Remote SSH**.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/access_device_terminal.png){class="glboxshadow"}

If you can't find the icon, please make sure you have enable it, check out [here](#enable-goodcloud-on-router).

If this feature not work, please try the incognito/inPrivate mode of browser.

## Modify Device Settings

You can use this feature to configure multiple parameters for a single device, or you can configure multiple parameters for multiple devices.

Select the devices you want to configure. And click on the 'Settings' operation button to modify the configuration.

![device settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_device_settings.png){class="glboxshadow"}

## Set email alarm

You can set email alarm when a device is online, offline, and new client connected.

At left side -> Notifications, create alarm rules.

First, you need to select the device you want to monitor.

![set alarm](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/set_alarm_1.png){class="glboxshadow"}

Next, select the monitoring items for the device, such as device online/offline status, new client connections, and more.

![set alarm](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/set_alarm_2.png){class="glboxshadow"}

Finally, choose the notification method for alerts.

![set alarm](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/set_alarm_3.png){class="glboxshadow"}

In the Notification List, you can view the alert rule you’ve created. Individual users are limited to creating one alert rule. If you require bulk device management, please feel free to contact us.

![rules list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/rules_list.png){class="glboxshadow"}

## Site to Site

Please refer to [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud and VPN

If you enable GoodCloud function and running VPN client at the same time on router, by default, the connection between the router and the GoodCloud server will also go through the VPN, but sometimes the VPN connection is unstable, or the VPN provider mistakenly filters the GoodCloud connection, you can make the GoodCloud connection not go through the VPN by using the following settings.

Go to web Admin Panel, on the left side, VPN -> VPN Dashboard -> VPN Client -> Global Options.

![Services from GL.iNet doesn't Use VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_donot_use_vpn.png){class="glboxshadow"}

It is not recommended to run Site to Site while its nodes are also running VPN client, which can make the network particularly complex.

## View Logs

You can see your activities in GoodCloud Platform.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Turn off cloud

To stop GoodCloud service, turn it off on router web Admin Panel. Please follow the steps below. No action needed on the GoodCloud website.

### For devices running firmware version 4.6 or earlier

If you no longer wish to have your device connected to the cloud platform, please follow these steps to disable cloud services.

![disable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/turn_off_cloud_1.png){class="glboxshadow"}

After disable Cloud, the interface is like below.

![after disable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/turn_off_cloud_display.png){class="glboxshadow"}

### For devices running firmware version 4.7 or later

If you no longer want your device to be connected to the cloud platform, please follow these steps to disable cloud services.

![disable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/turn_off_cloud_2.png){class="glboxshadow"}

After disable Cloud, the interface is like below.

![after disable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/turn_off_cloud_display_2.png){class="glboxshadow"}


---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
