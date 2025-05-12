# Clients

On the left side of web Admin Panel -> CLIENTS

The Clients page displays information about connected devices, including device name, connection type, IP address, MAC address, speed, and traffic.

## Device Name

The device name displayed here depends on the hostname of the device operator. You can modify the device name and type.

Click the three-dot icon in the Action column, and in the popped-up menu, click **Modify**.

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/action.jpg){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow gl-80-desktop"}

## MAC Address

Many devices will use randomized MAC address. If the connected devices use randomized MAC addresses, there will be a prompt.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Note**: The rule here is that if the second character of the MAC address is 2, 6, A or E(Ignore case), then it is considered a randomized MAC address. However, some devices may use a different rule to generate a randomized MAC address, so it may not be accurate.

## Speed

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

The speed here is the average speed over 3 minutes.

- Open the current page for 10 seconds, the average speed of the last 10 seconds is displayed.
- Open the current page for 30 seconds, the average speed of the last 30 seconds is displayed.
- Open the current page for 60 seconds, the average speed of the last 60 seconds is displayed.
- Open current page for 3 minutes, the average rate of the last 3 minutes is displayed.
- Open current page for 10 minutes, the average rate of the last 3 minutes is displayed.

## Reserved IP

This feature is available since v4.8

When you specify a reserved IP address for a client within the LAN, the client always receives the same IP address each time it accesses the router's DHCP server. 

You can assign reserved IP addresses to computers or servers that require permanent IP settings.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blocklist

Enable **Block** toggle to block client device. The access control rule is Blocklist by default, you can switch it to Allowlist from the top if needed.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_whitelist.png){class="glboxshadow gl-80-desktop"}

**Blacklist**: Devices with MAC addresses on the prohibited list are not allowed to connect to this router.

**Allowlist**: Only devices with specific MAC addresses are allowed to connect, suitable for IoT devices and enterprise network management.

Starting from firmware 4.4.x, you can upload a block list in excel form or input Mac addresses manually to creat a **Block List**.

You can either import a list from a CSV file at **(1)** or input the Mac Address one by one at **(2)**.

![inputblock](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/inputblock.jpg){class="glboxshadow gl-80-desktop"}

![importcsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

![dragcsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow gl-80-desktop"}

![loadcsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/loadcsv.jpg){class="glboxshadow"}

![applycsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/applycsv.jpg){class="glboxshadow"}

**Note**: Blocking client is based on the MAC address of the device, so if the blocked device use a different MAC address next time, it can still connect to router.

## Sort

The current sort type is displayed in the upper right corner, and you can switch to other sort types.

The default sort type is as follows:

- The self device is always on top.
- In the online client section, the later the device is connected, the higher it appears in the list.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Action

### Client Details

If you need to view the details of the client device, please click the three-dot icon in the Action column and then click the **View Details** in the popped-up menu.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/view_details.png){class="glboxshadow"}

After that, you can see all the information about the client device in the opened subpage, including all IPv6 addresses of the device if any.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modify

Click the three-dot icon in the Action column, and in the popped-up menu, click **Modify**.

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/action.jpg){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow gl-80-desktop"}

### Limit Speed

If you want to limit the speed of a device, please click the three-dot icon in the Action column, and in the popped-up menu, click **Limit Speed**.

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/action.jpg){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

If a client has applied speed limitation, its up arrow and down arrow of speed will turn yellow.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

Click the three-dot icon in the Action column to disable speed limit.

### Use VPN Tunnel

This feature is available since v4.8

Add client to VPN policy based tunnel list. If you want to make more detailed changes to the tunnels, please go to the VPN Dashboard to manage tunnels.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use_vpn_tunnel.png){class="glboxshadow"}

## Remove Offline Clients

In the offline clients section, you can click **Delete All** at the top right to delete all offline clients. 

If you want to remove specific client, click the three-dot icon in the Action column, and in the popped-up menu, click **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remote_offline_device.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
