# CLIENTS

On the left side of web Admin Panel -> CLIENTS

The Clients page displays information about connected devices, including device name, connection type, IP address, MAC address, speed, and traffic.

## Modify Client Name and Type

If you want to modify name and type of a device, please click the three docs icon, in the menu that pops up, click **Modify** item.

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients_three_dots.png){class="glboxshadow"}

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/edit_client_device.png){class="glboxshadow"}

## MAC Address

Many devices will use randomized MAC address, if the randomized MAC address is used, there will be a prompt.

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/randomized_mac_address.png){class="glboxshadow"}

**Note**: The rule here is that if the second character of the MAC address is 2, 6, A or E(Ignore case), then it is considered a randomized MAC address. However, some devices may use a different rule to generate a randomized MAC address, so it may not be accurate.

## Blocking Client

Enable **Block** toggle to block client device, the blocked device can't access the LAN interface and WAN interface.

![clients page](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients.png){class="glboxshadow"}

If you only want a client device access LAN, please try the [Parental Control](parental_control.md).

Starting from firmware 4.4.x, you can upload a block list in excel form or input Mac addressed manually to creat a **Block List**.

![blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/blocklist.jpg){class="glboxshadow"}

You can either import a list from a CSV file at **(1)** or input the Mac Address one by one at **(2)**.

![inputblock](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/inputblock.jpg){class="glboxshadow gl-80-desktop"}

![importcsv](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

![dragcsv](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/dragcsv.jpg){class="glboxshadow gl-80-desktop"}

![loadcsv](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/loadcsv.jpg){class="glboxshadow"}

![applycsv](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/applycsv.jpg){class="glboxshadow"}

**Note**: Blocking client is based on the MAC address of the device, so if the blocked device use a different MAC address next time, it can still connect to router.

## Speed

![clients page](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients_speed.png){class="glboxshadow"}

The speed here is the average speed over 3 minutes.

- Open the current page for 10 seconds, the average speed of the last 10 seconds is displayed.
- Open the current page for 30 seconds, the average speed of the last 30 seconds is displayed.
- Open the current page for 60 seconds, the average speed of the last 60 seconds is displayed.
- Open current page for 3 minutes, the average rate of the last 3 minutes is displayed.
- Open current page for 10 minutes, the average rate of the last 3 minutes is displayed.

## Sort

The current sort type is displayed in the upper right corner, and you can switch to other sort types.

The default sort type: 

- The self device is alway s on top
- In online client sector, the later the device is connected, the higher it is on top.

![clients page](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients_sort.png){class="glboxshadow"}

## Limiting Speed

If you want to limit the speed of a device, please click the three docs icon, in the menu that pops up, click **Limit Speed** item.

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients_three_dots.png){class="glboxshadow"}

![clients page](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients_limit_speed_settings.png){class="glboxshadow"}

If a client has applied speed limitation, its up arrow and down arrow of speed will turn yellow.

![clients page](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/clients_limit_speed.png){class="glboxshadow"}

Click **Action** to disable limiting.

## Remove Offline Clients

In the offline clients sector, you can **Delete All** offline clients. If you want to remove specific client, please click the three dots icon, in the menu that pops up, click **Remove Client** item.

![remove clients](https://static.gl-inet.com/docs/router/en/4/tutorials/clients/remove_client.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
