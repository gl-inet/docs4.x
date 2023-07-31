# GL.iNet GoodCloud

## Contents

- [Introduction](#introduction)
- [Setup](#setup)
    - [Enable GoodCloud on router](#enable-goodcloud-on-router)
    - [Sign up GoodCloud account](#sign-up-goodcloud-account)
    - [Select server region](#select-server-region)
    - [Add a new group](#add-a-new-group)
    - [Add device](#add-device)
    - [Bound info on router web Admin Panel](#bound-info-on-router-web-admin-panel)
    - [Unbind router](#unbind-router)
- [Manage your devices](#manage-your-devices)
    - [Devices info and status](#devices-info-and-status)
    - [LTE Signal](#lte-signal)
    - [Device detail info](#device-detail-info)
    - [Remote access web Admin Panel](#remote-access-web-admin-panel)
    - [Remote access router's terminal](#remote-access-routers-terminal)
    - [Set email alarm](#set-email-alarm)
- [Site to Site](../../tutorials/goodcloud_site_to_site)
- [Batch Setting](#batch-setting)
    - [Batch Setting of Single Device](#batch-setting-of-single-device)
    - [Batch Setting of Mutiple Devices](#batch-setting-of-mutiple-devices)
    - [Other Batch Operations](#other-batch-operations)
- [Template Management](#template-management)
    - [Add a Template](#add-a-template)
    - [Upgrade](#upgrade)
    - [Apply a template to a router](#apply-a-template-to-a-router)
    - [Apply a template to multiple routers](#apply-a-template-to-multiple-routers)
- [Task List](#task-list)
- [GoodCloud and VPN](#goodcloud-and-vpn)
- [Turn off cloud](#turn-off-cloud)

## Introduction

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud management service provide an easy and simple way to remotely access and manage routers. There is a video introduction below.

Introducing GoodCloud, Your Remote Device Management Solution.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JkV2PAy-_Og" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Easy Guide to Setting Up your GoodCloud Wi-Fi Management System for SMEs.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7U1CwpKOKDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Features:

* Check live router status
    - Live online offline status check
    - Live RAM and Load Average check
    - LTE Signal
    - Email alarm about online offline status update

* Set up routers remotely
    - Set up routers (e.g. SSID and Key) remotely
    - Remote SSH
    - Remote access web Admin Panel

* Monitoring clients on routers remotely
    - Check who is on your network
    - Realtime traffic monitoring and block clients
    - Email alarm about new client and block

* Operate routers in batch
    - Set up config templates and configure routers in batch
    - Reboot or upgrade routers in batch

* Manage routers in groups
    - Divide devices in different groups
    - Manage devices in one page

* Site to Site
    - Virtual Office: extend your office network to other offices
    - Business Travel: remote access office's OA, CRM, MySQL systems
    - Smart Home: remote access IP camera, NAS and other devices at home

## Setup

There is a video tutorial below about how to enable cloud function and bind it to GoodCloud.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mvJQZphSO1A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Enable GoodCloud on router

On the left side of web Admin Panel -> APPLICATIONS -> GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/en/4/tutorials/cloud/enable_goodcloud.png){class="glboxshadow"}

Follow the steps above, to enable the cloud function, which will allow the router to connect to the GoodCloud server.

* **Remote SSH** is for remote access router's terminal via GoodCloud. Check out [here](#remote-access-routers-terminal).

* **Remote Web Access** is for remote access router's web Admin Panel via GoodCloud. Check out [here](#remote-access-web-admin-panel).

* **Data Server**, please choose the server which is nearest your devices located. There are three Data Server, **Asia Pacific**(Japan), **America**(Oregon) and **Europe**(Ireland).

### Sign up GoodCloud account

 Visit [https://www.goodcloud.xyz](https://www.goodcloud.xyz){target="_blank"}, sign up then sign in. If you don't find the verify email, look in spam or check email later. If you have any difficulty with sign up, please send email to [support@glinet.biz](mailto:support@glinet.biz) for help.

### Select server region

At the first time when you sign in, it will pop up a dialog to let you select the region, please select the region same as your device selected Data Server on the web Admin Panel ([Step of enable GoodCloud on router](#enable-goodcloud-on-router)).

You can change the region on the top right corner at anytime.

![select region button](https://static.gl-inet.com/docs/en/4/tutorials/cloud/select_region_button.png){class="glboxshadow"}

### Add a new group 

On the left side -> Groups List -> Add group.

Follow the steps below to add a new group.

![add group](https://static.gl-inet.com/goodcloud/docs/add-group.png){class="glboxshadow"}

Set the group name, company, description and location.

Each device must belong to a group.

### Add device

On the left side -> Devices List -> Add Device. There are three methods to bind device to your GoodCloud account, **Auto discover**, **Manually add** and **Bulk import**.

=== "Auto discover"

    If your router and PC(which opened GoodCloud website) are in the same network, please try the **Auto discover**.
    
    Follow the steps below to add your device.

    ![add device](https://static.gl-inet.com/goodcloud/docs/add-device.png){class="glboxshadow"}

    Check out [here](../where_to_find_the_device_id_mac_sn) to find the Device ID.

        Note: Input "DDNS/Device ID" here just to verify that the router is really 
        original/valid.

        If you haven't added a group before, it will automatically create a default 
        group.

    Click `Refresh` to force auto discover devices again.

    ![auto discover](https://static.gl-inet.com/goodcloud/docs/auto-discover.png){class="glboxshadow"}

=== "Manually add"

    If it can't discover automatically, try `Manually add`. All information that need to input can be found on the back of the router.

        Note: Input "MAC", "SN" and "DDNS" / "Device ID" here just to verify that the 
        router is really original and valid.

    For new models, it has **Device ID** on the back of router.

    ![manually add device](https://static.gl-inet.com/goodcloud/docs/manually-add-device-device-id.png){class="glboxshadow"}

    For old models, it has **DDNS** on the back of the router. Only the first 7 characters of **DDNS** are needed.

    ![manually add device](https://static.gl-inet.com/goodcloud/docs/manually-add-device.png){class="glboxshadow"}

=== "Bulk import"

    `Bulk import` is for user who have a great number of devices to add. By `Bulk import` you can import many devices by a Microsoft excel file.

### Bound info on router web Admin Panel

After you seccessfully add router to GoodCloud, go back to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, 

refresh this page, It will display the bound GoodCloud username and date.

![goodcloud bound](https://static.gl-inet.com/docs/en/4/tutorials/cloud/goodcloud_bound_info.png){class="glboxshadow"}

### Unbind router

If you want to unbind the router, go to router web Admin Panel, on the left side, APPLICATION -> GoodCloud, click **Unbind** button.

![goodcloud unbind](https://static.gl-inet.com/docs/en/4/tutorials/cloud/goodcloud_unbind.png){class="glboxshadow"}

## Manage your devices

### Devices info and status

Sign in [Goodcloud](https://www.goodcloud.xyz), check at left side -> Device List

![device list table](https://static.gl-inet.com/goodcloud/docs/device_list_table.png){class="glboxshadow"}

there is icon at the first column of this table, 

![online icon](https://static.gl-inet.com/goodcloud/docs/online_icon.png) means this device is online.

![offline icon](https://static.gl-inet.com/goodcloud/docs/offline_icon.png) means this device is offline.

![deactovate icon](https://static.gl-inet.com/goodcloud/docs/deactivate_icon.png) means this device is deactivated, it has never connected to GoodCloud before.

![column selector](https://static.gl-inet.com/goodcloud/docs/column_selector.png){class="glboxshadow"}

Select the column you want to display.

`Online time` is the latest time when device connected GoodCloud.

`Offline time` is the latest time when device disconnected GoodCloud.

`Update time` is the latest time when device connected or disconnected GoodCloud.

`IP`, if your router run VPN client, this IP will be your VPN IP by default. <a href="#goodcloud-and-vpn">Learn More</a>

### LTE Signal

Only available for 4G devices, e.g. GL-MiFi, GL-X750

Toggle the column on Device List page.

![device LTE signal](https://static.gl-inet.com/goodcloud/docs/lte_signal.png){class="glboxshadow"}

It will show Signal strength, Type, and relavant parameters.

![device LTE signal](https://static.gl-inet.com/goodcloud/docs/lte_signal_2.png){class="glboxshadow"}

### Device detail info

At left side -> Device List, click the name of an online device, it will open a page to manage this device of WiFi, Clients and view router info, memory usage, up time, load average and log.

![to device detail page](https://static.gl-inet.com/goodcloud/docs/to_device_detail.png){class="glboxshadow"}

#### Device info

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-device-info.png){class="glboxshadow"}

#### WiFi

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-wifi.png){class="glboxshadow"}

Modify all WiFi settings.

#### Router status

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-router-status.png){class="glboxshadow"}

#### Client list

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-client-list.png){class="glboxshadow"}

#### Timeline

Timeline tab display the activities of router, and messages uploaded by the router's associated IoT device.

![device timeline](https://static.gl-inet.com/goodcloud/docs/timeline.png){class="glboxshadow"}

#### Tools

There are two tools, `Ping` and `Traceroute`.

![tools ping traceroute](https://static.gl-inet.com/goodcloud/docs/tools_ping_traceroute.png){class="glboxshadow"}

### Remote access web Admin Panel

Note: Please upgrade to 3.211 to use this feature.

If you can't find these icons, please make sure you have enable it, check out [here](#enable-goodcloud-on-router).

If this feature not work, please try the incognito mode of browser.

![remote access web admin panel](https://static.gl-inet.com/goodcloud/docs/remote_access_web_admin_panel.png){class="glboxshadow"}

### Remote access router's terminal

Note: Please upgrade to 3.211 to use this feature.

If you can't find these icons, please make sure you have enable it, check out [here](#enable-goodcloud-on-router).

If this feature not work, please try the incognito mode of browser.

![remote access web admin panel](https://static.gl-inet.com/goodcloud/docs/remote_access_terminal.png){class="glboxshadow"}

### Set email alarm

You can set email alarm when a device is online, offline, and new client connected.

At left side -> Setting -> Alarm Setting, create alarm rules

![create alarm rules](https://static.gl-inet.com/goodcloud/docs/create-alarm-rules.png){class="glboxshadow"}

Then set the email you want to receive notification. To ensure you get email successful, please add admin@goodcloud.xyz to your email address book.

![alarm rules](https://static.gl-inet.com/goodcloud/docs/alarm-rules.png){class="glboxshadow"}

## Site to Site

Please refer to [GoodCloud Site to Site](../../tutorials/goodcloud_site_to_site).

## Batch Setting

You can use this feature to configure multiple parameters for a single device, or you can configure multiple parameters for multiple devices.

    Note: This feature is only available to business users.

### Batch Setting of Single Device

To configure single device, as show below.

  <a href="https://static.gl-inet.com/goodcloud/docs/modify_configuration.png" target="_blank"><img alt="Modify Configuration" src="https://static.gl-inet.com/goodcloud/docs/modify_configuration.png"></a>

The left side of image below is correct. If your interface is like the right side of image below, please upgrade to latest testing firmware.

  <a href="https://static.gl-inet.com/goodcloud/docs/single_configuration.png" target="_blank"><img alt="Single Configuration" src="https://static.gl-inet.com/goodcloud/docs/single_configuration.png"></a>

Check the configuration that needs to be modified and input value.
  
![Add Configuration](https://static.gl-inet.com/goodcloud/docs/add_configuration.png){class="glboxshadow"}

The checked configuration is required, and only the configuration that conforms to the rule can be filled out. After the configuration is delivered, it does not take effect immediately. The configuration takes effect and the device needs to be restarted. You can check the Restart now option in the lower right corner of the above figure. After the configuration is completed, the device will restart immediately.

Preview the configuration and confirm the delivery.

![Preview Configuration](https://static.gl-inet.com/goodcloud/docs/preview_configuration.png){class="glboxshadow"}

Unchecked **Restart now** option will prompt.

<a href="https://static.gl-inet.com/goodcloud/docs/config_not_take_effect.png" target="_blank"><img alt="config not take effect" src="https://static.gl-inet.com/goodcloud/docs/config_not_take_effect.png"></a>

### Batch Setting of Mutiple Devices

Select the devices you want to configure.

![mutiple configuration](https://static.gl-inet.com/goodcloud/docs/mutiple_configuration.png){class="glboxshadow" width="800"}

Other operations are the same as when operating a single device.

### Other Batch Operations

Other Batch Operations: Move to other group, upgrade, restart, delete.

![Task](https://static.gl-inet.com/goodcloud/docs/task.png){class="glboxshadow"}

## Template Management

Save frequently used configurations as templates and quickly apply them when you modify configurations in batches.

    Note: This feature is only available to business users.

### Add a Template

Check the configuration that needs to be modified and input value. Most of the options are the same as those on web Admin Panel.

![Add Template](https://static.gl-inet.com/goodcloud/docs/add_template.png){class="glboxshadow"}

#### Upgrade

**Upgrade Path** is for upgrading custom firmware. Put the firmware and a text file on a web server, then put the url path on the **Upgrade Path**. For example, [https://fw.gl-inet.com/firmware/ar750/v1/](https://fw.gl-inet.com/firmware/ar750/v1/) is a Upgrade Path, it has a **list-sha256.txt** file [https://fw.gl-inet.com/firmware/ar750/v1/list-sha256.txt](https://fw.gl-inet.com/firmware/ar750/v1/list-sha256.txt) and a corresponding firmware file [https://fw.gl-inet.com/firmware/ar750/v1/openwrt-ar750-3.203-0701.bin](https://fw.gl-inet.com/firmware/ar750/v1/openwrt-ar750-3.203-0701.bin).

    Note: GL-AX1800, GL-S1300, GL-B1300, GL-AP1300 only support http path for now.

![Template info](https://static.gl-inet.com/goodcloud/docs/template_upgrade_path.png){class="glboxshadow"}

The content of the text file is like [this](https://fw.gl-inet.com/firmware/ar750/v1/list-sha256.txt), its name should be **list-sha256.txt**. It has 4 columns, the first column is firmware version, the second column is the name of firmware file, the thrid column is the sha256 of firmware file, the forth column is the size of firmware file.

![gl-ar750 sha256](https://static.gl-inet.com/goodcloud/docs/ar750-sha256.png){class="glboxshadow"}

Give the template a name and description.

![Template info](https://static.gl-inet.com/goodcloud/docs/template_info.png){class="glboxshadow"}

### Apply a template to a router

If you have created a template, then want to apply this template to a router. On the **Device List** page, find the router that you want to apply the template, make sure it is online, on the Actions column, click the cog icon, click **Modify Configuration** item. It will pop up a dialog **Configure batch modification**.

On the top right corner of the dialog, you can choose a template that has already created. Then click **Apply** button on the bottom right corner.

It will pop up another dialog to review the configuration of the template, scroll down to the bottom to click the **Confirm** button, it will load the configuration of template overwrite to this time modification.

Click **Apply** button, please note that the router will restart to take effect after click the **Apply** button.

### Apply a template to multiple routers

If you have created a template, then want to apply this template to multiple routers. This procedure is similar to that applied to a single router. On the **Device List** page, multiple select routers, then click **Bulk Action**, click **Modify Configuration** item. It will pop up a dialog **Configure batch modification**.

On the top right corner of the dialog, you can choose a template that has already created. Then click **Apply** button on the bottom right corner.

It will pop up another dialog to review the configuration of the template, scroll down to the bottom to click the **Confirm** button, it will load the configuration of template overwrite to this time modification.

Click **Apply** button, please note that the router will restart to take effect after click the **Apply** button.

## Task List

At task list page, it shows the execution result of the configuration template.

    Note: This feature is only available to business users.

![Task list](https://static.gl-inet.com/goodcloud/docs/task_list.png){class="glboxshadow"}

You can view the execution result of each device and configuration.

![Task list detail info](https://static.gl-inet.com/goodcloud/docs/task_list_detail_info.png){class="glboxshadow"}

## GoodCloud and VPN

If you enable GoodCloud function and running VPN client at the same time on router, by default, the connection between the router and the GoodCloud server will also go through the VPN, but sometimes the VPN connection is unstable, or the VPN provider mistakenly filters the GoodCloud connection, you can make the GoodCloud connection not go through the VPN by using the following settings.

Go to web Admin Panel, on the left side, VPN -> VPN Dashboard -> VPN Client -> Global Options.

![Services from GL.iNet doesn't Use VPN](https://static.gl-inet.com/docs/en/4/tutorials/cloud/goodcloud_donot_use_vpn.png){class="glboxshadow"}

It is not recommended to run Site to Site while its nodes are also running VPN client, which can make the network particularly complex.

## Turn off cloud

To stop GoodCloud service, turn it off on router web Admin Panel. Please follow the steps below. No action needed on the GoodCloud website.

![disable cloud](https://static.gl-inet.com/docs/en/4/tutorials/cloud/turn_off_cloud.png){class="glboxshadow"}

After disable Cloud, the interface is like below.

![after disable cloud](https://static.gl-inet.com/docs/en/4/tutorials/cloud/after_turn_off_cloud.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
