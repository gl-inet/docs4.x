# How to let all data go through VPN?

If you want all data on the router to pass through VPN and block all networks when the VPN connection failed, please follow the steps below to enable **VPN Kill Switch**.

**Note**: Set up VPN client on your GL.iNet router first before enabling VPN Kill Switch.

## For firmware v4.7 and earlier

On the left side of the web Admin Panel -> VPN -> VPN Dashboard.

In the **VPN Client** section, click **Global Options**, toggle on **Block Non-VPN Traffic**, then click **Apply** button.

![vpn client global options](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/global_options.png){class="glboxshadow"}

**Note:** If VPN is disabled, no internet will pass between the router and connected devices

## For firmware v4.8 and higher

On the left side of the web Admin Panel -> VPN -> VPN Dashboard.

In the Primary Tunnel, set all clients use VPN, travelling to all targets.

Then click the greyed-out box under Execute.

![execute 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/execute_1.png){class="glboxshadow"}

In the pop-up window, enable **Kill Switch**.

![execute 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/execute_2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
