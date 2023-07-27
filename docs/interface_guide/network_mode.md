# Network Mode

On the left side of web Admin Panel -> NETWORK -> Network Mode

When you change the router's network mode, you may need to re-connect all your client devices.

When you use Access Point/Extender/WDS mode, you may not connect to the web Admin Panel again. Try to access the web Admin Panel by the IP address that parent router assigned to this router. Or you can Press and hold the reset button for 4 seconds to revert to Router mode.

## For models that have Wi-Fi

Here is an example of GL-AXT1800.

**Note:** some models do not support WDS mode.

![network mode](https://static.gl-inet.com/docs/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**. Create your own private network. The router will act as NAT, firewall and DHCP server. This is the default mode.

- **Access Point**. Connect to a wired network and broadcast a wireless network.

- **Extender**. Extend the Wi-Fi coverage of an existing wireless network.

- **WDS**. Similar to Extender, please choose WDS if your main router supports WDS mode.

## For models that don't have Wi-Fi

Here is an example of GL-MT2500/GL-MT2500A. It doesn't have Access Point, Extender, WDS, modes, but it has Bridge mode.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**. Create your own private network. The router will act as NAT, firewall and DHCP server. This is the default mode.

- **Bridge**. Connect to a wired network. Bridge mode is a networking feature that allows two routers together. When it enabled, it essentially turns the the router into a switch. The bridge-enabled router will still transfer data, but it won't perform traditional Network Access Translation (NAT) processes.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
