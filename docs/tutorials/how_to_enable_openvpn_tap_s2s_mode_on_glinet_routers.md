# How to enable OpenVPN TAP-S2S mode on GL.iNet routers?

## Usage Scenarios

After enabling TAP-S2S mode, the OpenVPN client device can remotely access the OpenVPN server device, and the OpenVPN server device can also remotely access the OpenVPN client device. However, the downside is that the VPN rules set by the OpenVPN client themselves will not take effect after enabling TAP-S2S mode.

## TAP-S2S vs TUN mode

Network Topology

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2S and TUN modes have the same physical connection method, but their logical connection methods are different. Here are the differences:

1. When devices on the GL-X3000 LAN side access the management backend of the GL-MT6000, TAP-S2S mode does not use a virtual IP, but TUN mode does.
2. When devices on the GL-X3000 LAN side access the management backend of the GL-X3000, TAP-S2S mode uses a virtual IP, but TUN mode does not.
3. When the GL-X3000 LAN-side device knows the IP address of a device on the GL-MT6000 LAN side, TAP-S2S mode allows direct remote access, but TUN mode cannot access directly without enabling additional settings.
4. In TAP-S2S mode, the GL-X3000 needs to go through the GL-MT6000 to access the internet, while in TUN mode, the Gl-X3000 can directly access the internet. Therefore, in TAP-S2S mode, the VPN rules set by the GL-X3000 do not take effect and the VPN rules set by the GL-MT6000 must be followed.

## Tutorials

Firstly, use a router (assumed to be GL-MT6000) with a public IP to open the OpenVPN Server, set the device mode to **TAP-S2S**, click Apply, and then click **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

In addition, use a router (assuming it is GL-X3000) with a public IP to open the OpenVPN client, import the configuration file downloaded in the above steps, click **Apply**, and then enable the function.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

At this time, the IP address of the GL-X3000 router will change. You can log in to the GL-MT6000 management dashboard, open **Clients**, and find the new IP address of the GL-X3000.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

If the GL-MT6000 loses network connection or turns off the OpenVPN server, or the GL-X3000 turns off the OpenVPN client , the  IP address of the GL-X3000 will be restored.

Points to Note:

- Both devices must be upgraded to version v4.5, otherwise they will not be able to connect;
- TAP-S2S only works with Global Proxy Mode, it will adjust automatically with OpenVPN on.
- After enabling this feature, the following functions cannot be used: VPN server, Adguard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping, etc.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.