# CLIENTS

On the left side of web Admin Panel -> CLIENTS

The Clients page displays information about connected devices, including device name, connection type, IP address, MAC address, speed, and traffic.

## Modify Client Name and Type

If you want to modify name and type of a device, please click the three docs icon, in the menu that pops up, click **Modify** item.

![clients page, three dots](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients_three_dots.png){class="glboxshadow gl-60-desktop"}

![clients page, three dots](https://static.gl-inet.com/docs/en/4/tutorials/clients/edit_client_device.png){class="glboxshadow gl-60-desktop"}

## MAC Address

Many devices will use randomized MAC address, if the randomized MAC address is used, there will be a prompt.

![clients page, three dots](https://static.gl-inet.com/docs/en/4/tutorials/clients/randomized_mac_address.png){class="glboxshadow gl-60-desktop"}

**Note**: The rule here is that if the second character of the MAC address is 2, 6, A or E(Ignore case), then it is considered a randomized MAC address. However, some devices may use a different rule to generate a randomized MAC address, so it may not be accurate.

## Blocking Client

Enable **Block WAN** so that it cannot access the WAN, only LAN. To put it simple, it will cannot access the Internet.

![clients page](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients.png){class="glboxshadow gl-80-desktop"}

**Note**: Blocking client is based on the MAC address of the device, so if the blocked device use a different MAC address next time, it can still connect to router.

## Speed

![clients page](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients_speed.png){class="glboxshadow gl-60-desktop"}

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

![clients page](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients_sort.png){class="glboxshadow gl-60-desktop"}

## Limiting Speed

If you want to limit the speed of a device, please click the three docs icon, in the menu that pops up, click **Limit Speed** item.

![clients page, three dots](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients_three_dots.png){class="glboxshadow gl-60-desktop"}

![clients page](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients_limit_speed_settings.png){class="glboxshadow"}

If a client has applied speed limitation, its up arrow and down arrow of speed will turn yellow.

![clients page](https://static.gl-inet.com/docs/en/4/tutorials/clients/clients_limit_speed.png){class="glboxshadow"}

Click **Action** to disable limiting.

## Remove Offline Clients

In the offline clients sector, you can **Delete All** offline clients. If you want to remove specific client, please click the three dots icon, in the menu that pops up, click **Remove Client** item.

![remove clients](https://static.gl-inet.com/docs/en/4/tutorials/clients/remove_client.png){class="glboxshadow gl-80-desktop"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
