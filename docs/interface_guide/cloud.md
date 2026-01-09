# GL.iNet GoodCloud

## Contents

- [Introduction](#introduction)
- [Bind Devices to GoodCloud](#bind-devices-to-goodcloud)
    - [For firmware v4.6 or earlier](#for-firmware-v46-or-earlier)
        - [Enable GoodCloud](#enable-goodcloud)
        - [Sign up an account](#sign-up-an-account)
        - [Add devices](#add-devices)
        - [Binding details](#binding-details)
        - [Unbind device](#unbind-device)
    - [For firmware v4.7 or later](#for-firmware-v47-or-later)
        - [Enable Cloud Service](#enable-cloud-service)
        - [Binding details](#binding-details_1)
        - [Unbind device](#unbind-device_1) 
- [Manage Devices](#manage-devices)
    - [System info and actions](#system-info-and-actions)
    - [Device details](#device-details)  
        - [Basic info](#basic-info)
        - [Statistics](#statistics)
        - [Network settings](#network-settings)
        - [Clients list](#clients-list)
- [Remote Access](#remote-access)
    - [Remote GUI](#remote-gui)
    - [Remote SSH](#remote-ssh)
- [Modify Settings](#modify-settings)
- [Email Alarm](#email-alarm)
- [Site to Site](#site-to-site)
- [GoodCloud and VPN](#goodcloud-and-vpn)
- [View Logs](#view-logs)
- [Disable Cloud](#disable-cloud)
- [Delete Account](#delete-account)

## Introduction

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} is a platform designed to simplify the remote deployment and management of connected devices. It provides an easy way to remotely access and manage GL.iNet routers. By centralizing network devices on the cloud, users can efficiently perform batch management tasks, such as deploying network configurations and performing software upgrades. They can also remotely access the router's web admin panel or connect to the router's terminal via SSH, achieving cross-regional and end-to-end network device management.

Features:

- Check the router's real-time status
    - Monitor online-offline status
    - View real-time RAM usage and load average
    - Receive email alerts for online-offline status changes

- Set up routers remotely
    - configure router settings (e.g. SSID and password)
    - Remote SSH access
    - Remote access to the WebUI
    - Share router access with others

- Monitor connected clients remotely
    - View devices connected to your network
    - Monitor real-time traffic and block clients
    - Receive email alerts for new connections and block events

- Batch router operations
    - Batch reboot
    - Batch firmware upgrade

- Site-to-Site Connectivity
    - Virtual Office: Extend your office network to other branch offices
    - Business Travel: Remotely access office systems (e.g., OA, CRM, MySQL)
    - Smart Home: Remotely access home devices (e.g., IP cameras, NAS)

If you need to manage multiple devices and unlock advanced features like bulk operations, multi-account management, and customized solutions, choose our value-added plans. Click [here](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} for details, and feel free to reach out to [support@glinet.biz](mailto:support@glinet.biz).

## Bind Devices to GoodCloud

To connect devices to the cloud platform successfully, please follow the binding procedures corresponding to your firmware version.

### For firmware v4.6 or earlier

#### Enable GoodCloud

Log in to your router's web admin panel, and navigate to **APPLICATIONS** -> **GoodCloud**. Toggle the switch to enable GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

Enable **Remote SSH** and **Remote Web Access** as needed, select the nearest server, read and agree the **Terms of Service & Privacy Policy**, then click **Apply**.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH**: For remotely accessing the router's terminal via GoodCloud.

- **Remote Web Access**: For remotely accessing the router's web admin panel via GoodCloud.

- **Data Server**: Please choose the server nearest to your device's location. There are three options: Asia Pacific (Japan), America (Oregon), and Europe (Ireland).

#### Sign up an account

Visit the [GoodCloud website](https://www.goodcloud.xyz){target="_blank"} to sign up for an account and log in.

If you don't receive the verification email, check your spam folder or wait a few minutes and try again. For any signup difficulties, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance.

#### Add devices

On the Cloud platform, navigate to **Devices** -> **Bound Devices** -> **Add Devices**. 

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

There are three methods to bind device to your GoodCloud account: Auto Discover, Manually Add, and Bulk Import.

??? "Auto Discover"

    You may try **Auto discover** if your router and the device used to access GoodCloud website are on the same network.
    
    Select your device from the drop-down list, and input the **DDNS / Device ID**, which can be found at the bottom of your router, or on the GoodCloud page in the web admin panel. 

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Please refer to [this link](../faq/where_to_find_the_device_id_mac_sn.md) to find the Device ID.

??? "Manually Add"

    If your device is not in the list, click **Manually add** and input the details of your router. All information requested can be found at the bottom of the router, or on the GoodCloud page in the web admin panel.

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** is designed for users managing a large number of devices. You can import multiple devices via a Microsoft Excel file.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### Binding details

After successfully binding, log in back to the router's web admin panel, and navigate to **APPLICATIONS** -> **GoodCloud**. Refresh this page, and it will display the bound GoodCloud username and date.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Unbind device

If you want to unbind your router, log in to the router's web admin panel, navigate to **APPLICATION** -> **GoodCloud** and click **Unbind**. 

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

Alternatively, you can remove the corresponding device from the Bound Devices List on the GoodCloud platform. The router's web admin panel will then synchronize to reflect the latest device binding status.

For any difficulties, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance.

### For firmware v4.7 or later

#### Enable Cloud service

Log in to your router's web admin panel, and navigate to **CLOUD SERVICE** -> **GoodCloud**. 

Click the **Get Started** button, and a Cloud Service pop-up window will appear in the upper right corner. Click **Enable** to use Cloud Service.

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

Log in to your GoodCloud account. 

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

If you don't have an account, sign up for one and log in. Once registration is complete, the router will automatically bind to this account. 

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

If you don't receive the verification email, check your spam folder or wait a few minutes and try again. For any signup difficulties, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance.

#### Binding details

After successfully binding, log in back to the router's web admin panel, click on the Cloud icon in the upper right corner, and you will see the binding details, including the bound GoodCloud username and date, Device ID, Device MAC and Device S/N.

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

In the web admin panel, navigate to **CLOUD SERVICES** -> **GoodCloud**, and you can enable or disable the remote access for your router.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH**: For remotely accessing the router's terminal via GoodCloud.

- **Remote Web Access**: For remotely accessing the router's web admin panel via GoodCloud.

- **View Logs**: It will show API call logs by GoodCloud.

#### Unbind device

If you want to unbind your router, log in to the router's web admin panel. Click the cloud icon in the upper right corner, and click **Unbind**. 

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

Alternatively, you can remove the corresponding device from the Bound Devices List on the GoodCloud platform. The router's web admin panel will then synchronize to reflect the latest device binding status.

For any difficulties, please email [support@glinet.biz](mailto:support@glinet.biz) for assistance.

## Manage Devices

### System info and actions

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, you can view the system information (e.g., model, version, MAC address, IP address) and status (e.g., online, offline) of all devices bound to your account.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Select a device, then you can perform actions in the upper right corner, such as modifying settings, updating firmware, remote accessing the device, rebooting, or resetting.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Click the gear icon on the far right of the list header, and you can customize the display of columns and their order to focus on the device information that matters most.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Device details

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, click a device name, and you will be re-directed to the device details page, where it displays the router's basic info, statistical data, network settings, clients list, etc. 

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Basic info

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistics

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Network settings

This page displays your router's network configurations and Wi-Fi settings.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Clients list

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Remote Access

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, click the name of the device you want to access to enter the details page, then you will see remote actions in the upper right corner.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI

Click **Remote GUI** to remotely access your router's web admin panel.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

If this option is grayed out or unavailable, it is likely that this feature is disabled. Please enable it in the router's web admin panel first before accessing it via GoodCloud.

If this option is clickable but unresponsive, try using your browser's incognito/inPrivate mode.

### Remote SSH

Click **Remote SSH** to remotely access your router's terminal over SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

If this option is grayed out or unavailable, it is likely that this feature is disabled. Please enable it in the router's web admin panel first before accessing it via GoodCloud.

If this option is clickable but unresponsive, try using your browser's incognito/inPrivate mode.

## Modify Settings

You can configure multiple parameters for a single device or multiple devices.

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, select the device you want to configure, and in the upper right corner, click **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Here you can check and modify the router's network settings, including wireless, Ethernet, security, port forwarding, LAN and system settings.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Email Alarm

You can set up an email alarm when the device status changes (online/offline) or new clients connect.

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications**, click the **Add Rule** button in the upeer right corner.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Select the device you want to monitor, and click **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Select the trigger event, such as device online/offline status, and click **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Check the rule settings, and click **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

In the Notifications list, you can view the alert rules you've created. Individual users are limited to creating one alert rule. If you require bulk device management, feel free to contact us to upgrade your plan.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site

Please refer to [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud and VPN

If you enable **GoodCloud** and **VPN client** at the same time on your router, the connection between the router and the GoodCloud server will not go through the VPN by default. This ensures a more stable connection to GoodCloud services.

However, if you want the GoodCloud connection to go through the VPN, you can change this settings in the router's web admin panel. Navigate to VPN -> VPN Dashboard -> VPN Client -> Options, and enable the option "Services from GL.iNet Use VPN".

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Note that routing GoodCloud through VPN may affect the stability of the cloud connection, especially if:

* The VPN connection is unstable
* The VPN provider filters or blocks GoodCloud traffic
* The VPN adds significant latency to the connection

It is generally recommended to keep the default settings where GoodCloud bypasses the VPN for optimal performance and reliability.

## View Logs

You can view GoodCloud logs as needed, including Activity Logs, Device Logs, Upgrade Logs, Alert Logs, and Device Settings Logs. 

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs**, and select the logs you want to view from the drop-down list.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Disable Cloud

If you no longer wish to have your device connected to the cloud platform, you can disable cloud service in the router's web admin panel.

??? "For firmware v4.6 or earlier"

    Log in to your router's web admin panel, navigate to **APPLICATIONS** -> **GoodCloud**, toggle the switch to disable GoodCloud, and click **Apply**

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Once disabled, the interface will display as follows.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "For firmware v4.7 or later"

    Log in to your router's web admin panel, and click the cloud icon in the top right corner.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Once disabled, the interface will display as follows.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Delete Account

For security reasons, you may delete your account if it is no longer in use. 

On the [GoodCloud](https://www.goodcloud.xyz){target="_blank"} platform, click the user name in the top right corner and select **Personal Center**. Scroll down to the bottom of the page and click **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Deletion will permanently erase all related services, data, and personal information with no option for recovery. 
    
    If your account belongs to any organization, please leave all organizations first before deleting your account.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
