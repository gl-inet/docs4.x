# How to let all data go through VPN?

If you want all data on the router to pass through VPN and block all networks when the VPN connection failed, please follow the steps below to enable **VPN Kill Switch**.

**Note**: Set up VPN client on your GL.iNet router first before enabling VPN Kill Switch.

## For firmware v4.7 and earlier

Log in to your router's web Admin Panel, navigate to **VPN** -> **VPN Dashboard** -> **VPN Client** section, and click **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Toggle on **Block Non-VPN Traffic** (also called Kill Switch in some firmware version), then click **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Note:** When Block Non-VPN Traffic / Kill Switch is enabled, if your VPN is disabled or disconnected, all devices connected to the router will be restricted from accessing the Internet to prevent DNS leaks.

## For firmware v4.8 and higher

In firmware v4.8, the VPN Kill Switch has been divided into two parts.

- **Tunnel Kill Switch**: It is enabled by default when the corresponding VPN tunnel is activated.

- **Global Kill Switch**: It is disabled by default to ensure Internet access for traffic that doesn't go through any VPN tunnel or traffic that fails over from VPN connections.

### Tunnel Kill Switch

If you have set your router as a VPN client, once the VPN is activated, on the router's web Admin Panel, navigate to **VPN** -> **VPN Dashboard**, and you will see the Kill Switch for this VPN tunnel is enabled by default. 

![tunnel kill switch on](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-tunnel-kill-switch.png){class="glboxshadow"}

Click on the three-dot icon next to the tunnel name and select **Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-tunnel-options-1.png){class="glboxshadow"}

You will enter the Tunnel Options settings, where the Kill Switch for this tunnel is enabled by default.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-tunnel-options-2.png){class="glboxshadow"}

### Global Kill Switch

The Global Kill Switch is usually displayed at the botton of the VPN Dashboard. 

On the router's web Admin Panel, navigate to **VPN** -> **VPN Dashboard**, swipe down to the bottom, and you will see a tunnel named **All Other Traffic**. The page may vary slightly depending on the firmware version.

![global kill switch off](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-kill-switch.png){class="glboxshadow"}

**All Other Traffic** is a basic tunnel to ensure Internet access for traffic that doesn't go through any VPN tunnel or traffic that fails over from VPN connections. This tunnel is enabled by default and is mutually exclusive with the Global Kill Switch, meaning that the Global Kill Switch is disabled by default.

Turning this off will enable Global Kill Switch and block regular Internet access for all devices.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
