# Clients

On the left side of web Admin Panel -> CLIENTS

The Clients page displays information about connected devices, including device name, connection type, IP address, MAC address, speed, and traffic, arranged left to right.

## Device Name

The first column displays the device name and device type, which depends on the hostname of the device operator.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

To modify the device name and type, click the three-dot icon in the Action column, and in the drop-down menu, click **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Connection Type

The blue icon on the right side of the device name represents the connection type/method of device.

It indicates how the device is connected to the network - whether via Wi-Fi or an ethernet cable.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IP and MAC Address

The second column lists the IP and MAC addresses of the connected device.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Many devices use randomized MAC addresses. If the connected devices use randomized MAC addresses, the following prompt will appear.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Note**: The rule here is that if the second character of the MAC address is 2, 6, A or E(Ignore case), it is considered a randomized MAC address. However, some devices may use a different rule to generate a randomized MAC address, so this detection method may not be accurate.

## Speed

The third column displays the internet speed of the connected device.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

The speed here is the average speed over 3 minutes.

- Open the current page for 10 seconds, the average speed of the last 10 seconds is displayed.
- Open the current page for 30 seconds, the average speed of the last 30 seconds is displayed.
- Open the current page for 60 seconds, the average speed of the last 60 seconds is displayed.
- Open current page for 3 minutes, the average rate of the last 3 minutes is displayed.
- Open current page for 10 minutes, the average rate of the last 3 minutes is displayed.

## Traffic

The fourth column displays the internet traffic of the connected device.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## Reserved IP

In the fifth column, you can reserve IP address for a certain connected device with just one click. 

This feature is available as of v4.8.

When you specify a reserved IP address for a client within the LAN, the client always receives the same IP address each time it accesses the router's DHCP server. 

You can assign reserved IP addresses to computers or servers that require permanent IP settings.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blocklist

In the sixth column, you can block specific connected devices with just one click. 

The access control rule is Blocklist by default, and you can switch it to Allowlist from the top if needed.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Devices with MAC addresses on the blocklist list are not allowed to connect to this router.

- **Allowlist**: Only devices with specific MAC addresses are allowed to connect, suitable for IoT devices and enterprise network management.

To create a Blocklist, you can upload a block list in excel form at **(1)**, or input MAC addresses manually at **(2)**.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Method 1. Import Clients**

In the Access Control page, click on **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Click on **Download Import Template**, and you will download an XLS worksheet named "mac-template.csv".

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Open the file, import the MAC addresses and save.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Select the saved file or drag it to the upload area.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Once the upload is successful, click **Import** to complete the batch import of MAC addresses.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Method 2. Input Manually**

In the Access Control page, manually input the MAC address of the devices you want to block, and click **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Note**: Blocking client is based on the MAC address of the device. If the blocked device uses different MAC address next time, it can still be able to connect to router.

## Sort

The current sort type is displayed in the upper right corner, and you can switch to other sort types.

The default sort type is as follows:

- The self device is always on top.
- In the online client section, the later the device is connected, the higher it appears in the list.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Action

### Client Details

If you need to view the details of the client device, click the three-dot icon in the rightmost Action column and then click the **View Details** in the drop-down menu.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

You can see all the information about the client device in the opened subpage, including all IPv6 addresses of the device if any.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modify

Click the three-dot icon in the Action column, and in the drop-down menu, click **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Limit Speed

Click the three-dot icon in the Action column, and in the drop-down menu, click **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

If a client has been applied speed limitation, its up arrow and down arrow of speed will turn yellow.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

Click the three-dot icon in the Action column to disable speed limit.

### Use VPN Tunnel

**Note**: This option is available as of firmware v4.8 and will only appear in the Action menu if a MAC-based policy is configured.

Add a client to the VPN tunnel list with MAC-based policy. If you need to make detailed adjustments to the tunnels, go to the VPN Dashboard for management.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Remove Offline Clients

In the offline clients section, you can click **Delete All** at the top right to delete all offline clients. 

If you want to remove specific client, click the three-dot icon in the Action column, and in the drop-down menu, click **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
