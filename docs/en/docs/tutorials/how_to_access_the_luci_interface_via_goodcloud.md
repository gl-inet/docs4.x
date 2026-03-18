# How to access the LuCI interface via GoodCloud

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} breaks through geographical limitations and provides a convenient way for remote router management. Through GoodCloud, you can access the LuCI interface of the router anytime and anywhere, perform various settings on the router and easily manage the network.

## Preparation

- Hardware Equipment: A GL.iNet router that has been configured with Internet and is operating normally.
- Network Environment: The network to which the router is connected is stable and can access the Internet normally.
- Device Binding: You need to [bind your GL.iNet router to your GoodCloud account](../interface_guide/cloud.md/#setup-your-goodcloud-account). If you don't have a GoodCloud account, please [register](https://www.goodcloud.xyz/){target="_blank"} one.

## Steps to Access the LuCI Interface via GoodCloud

### For Firmware Version 4.7 or Above

Starting from v4.7, users can directly access the LuCI page from the GoodCloud platform without going through the router's web Admin Panel.

1. Log in to your GoodCloud account [here](https://www.goodcloud.xyz/){target="_blank"}.

2. On the left side -> **Devices** -> **Bound Devices**, Click the name of the device you want to access, then you will see the icons of Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    The pop-up window displays the port 80. Change the port to **8080**, click Apply.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. You will be re-directed to the LuCI login page. Enter your admin password to log in.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. You have successfully logged in to LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}    

### For Firmware Version 4.6 or Below

1. Log in to your GoodCloud account [here](https://www.goodcloud.xyz/){target="_blank"}.

2. On the left side -> **Devices** -> **Bound Devices**, Click the name of the device you want to access, then you will see the icons of Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    The pop-up window displays the port 80, click Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. You will then be re-directed to the GL.iNet Admin Panel login page. Enter your admin password to log in.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. After login, on the left side -> SYSTEM -> Advanced Settings, click the hyperlink to go to LuCI interface.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    You will be re-directed to the LuCI login page. Enter the same admin password to log in.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. You have successfully logged in to LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.