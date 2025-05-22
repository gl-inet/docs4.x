# USB modem is not working properly on GL.iNet router

Some GL.iNet routers have USB ports, users can plug a USB modem into the USB port to configure Internet access, even to realize Multi-WAN scenarios if combined with other Internet access. 

However, you may encounter the problem that some USB modem (such as ZTE F50 Mobile WiFi Hotspot) cannot be used normally on the router, causing frequent network dropouts. 

This may be due to the compatibility problem between the router's USB port (usually USB3.0) and the 2.4G WiFi, which leads to the USB modem dropping out constantly and cannot access the Internet normally.

To solve this issue, you can switch the USB port specification from USB 3.0 to USB 2.0.

Access your GL.iNet router's admin panel, go to **SYSTEM -> Overview -> External Storage**. 

You will see an option for USB Protocol Switch.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Switch it to USB 2.0, a prompt will be displayed as below. Click Switch to continue.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

When it shows the USB protocol as USB 2.0, it means you have switched it successfully.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

After that, please check if there's improvement with the Internet connection.

---

Related Articles

- [Compatible Modems](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.