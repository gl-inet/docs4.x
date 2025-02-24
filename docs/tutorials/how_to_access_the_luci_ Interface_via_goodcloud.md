# How to Access the LuCI Interface via GoodCloud

GL-iNet [GoodCloud](https://www.goodcloud.xyz/) breaks through geographical limitations and provides a convenient way for remote router management. Through GoodCloud, you can access the LuCI interface of the router anytime and anywhere, perform various settings on the router and easily manage the network.

## Preparation
- Hardware Equipment: A GL-iNet router that has been configured with Internet and is operating normally.
- Network Environment: The network to which the router is connected is stable and can access the Internet normally.
- Device Binding: You need to [bind your GL-iNet router to your GoodCloud account](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/#setup-your-goodcloud-account). If you don't have a GoodCloud account, please [register](https://www.goodcloud.xyz/) one.

## Steps to Access the LuCI Interface via GoodCloud

1. Log in to your GoodCloud account [here](https://www.goodcloud.xyz/).

2. On the left side -> **Devices** -> **Bound Devices**, Click the name of the device you want to access, then you will see the icons of Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    The pop-up window displays the port 80, click Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. You will then be re-directed to the GL-iNet Admin Panel login page. Enter your admin password to log in.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. After login, on the left side -> SYSTEM -> Advanced Settings, click the hyperlink to go to LuCI interface.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    You will be re-directed to the LuCI login page. Enter the same admin password to log in.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow"}

5. You have successfully logged in to LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}
