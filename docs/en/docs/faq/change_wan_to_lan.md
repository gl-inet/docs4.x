# Change WAN to LAN

You can change the WAN port of your router to be a LAN port. This is particularly useful when using the router in repeater mode, where the WAN port is unnecessary. By changing the WAN port to a LAN port, you will have an additional LAN port for expanded connectivity.

Follow the steps below to change WAN to LAN.

## For Firmware 4.7 and above

1. Leave the WAN port unconnected.

2. Connect a device to the router and access the router's web admin panel.

3. In the web admin panel, navigate to **INTERNET** -> **Ethernet** section, and click on the gear icon at the upper right corner.

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

	You will be directed to the **Port Management** page, where the WAN port status is displayed as being used for WAN.

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Click on **LAN** to change the Ethernet port properties, and click **Apply**.

	![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

	In the pop-up caution window, click **Apply** to confirm.
	
	![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

	**Note**: Wi-Fi may disconnect temporarily during this process. Please re-connect to the router once completed.

5. Back in the Ethernet section, it will show that the WAN port is now used as a LAN port.

	![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

	You can switch it back to WAN in **Port Management** page, or press the RESET button for 4 seconds to restart the WAN interface.

## For Firmware 4.6 and earlier

1. Leave the WAN port unconnected.

2. Connect a device to the router and access the web admin panel.

3. In the web admin panel, navigate to **INTERNET** -> **Ethernet** section, where it displays the WAN port status is **Using as WAN**. Click **Change to LAN**.

	![internet page](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Click **Apply** to confirm.

	![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

	**Note**: Wi-Fi may disconnect temporarily during this process. Please re-connect to the router once completed.

5. Back in the Ethernet section, it displays `Using as LAN`.

	![using as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

	You can simply revert the setting by repeating the above procedures.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
