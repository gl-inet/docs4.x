# Network Mode

On the left side of web Admin Panel -> NETWORK -> Network Mode

Network mode refers to the different operational roles and functionalities a router can assume to meet various network deployment needs.

When you change the router's network mode, you may need to reconnect all client devices.

When you use Access Point / WDS, you will not be able to connect to the web admin panel again. You can press and hold the reset button for 4 seconds to revert to router mode.

## For models with Wi-Fi

Except for specific models, most GL.iNet wireless routers have Wi-Fi functionality.

Models with Wi-Fi functionality usually support four modes: Router, Access Point, Extender, and WDS modes. Note that some models do not support WDS mode.

Here is an example of GL-AXT1800.

![network mode](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: Allows the router to create a private network. This is the default mode. In this mode, the router functions as a NAT device, a firewall, and a DHCP server, managing IP address allocation and providing network security for connected devices.

- **Access Point**: Allows the router to connect to a wired network and then broadcast a wireless network signal, expanding wireless network access in a wired network environment.

- **Extender**: It is used to extend the Wi-Fi coverage of an existing wireless network, helping to eliminate Wi-Fi dead zones in areas with poor original signal.

- **WDS**: Wireless Distribution System mode. It is similar to Extender mode. It is recommended when the main router supports WDS, facilitating wireless network expansion through a compatible wireless bridging mechanism.

## For models without Wi-Fi

GL-MT2500/GL-MT2500A does not support Access Point, Extender, or WDS modes as it lacks Wi-Fi functionality, but does support Bridge mode.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: Allows the router to create a private network. This is the default mode. In this mode, the router functions as a NAT device, a firewall, and a DHCP server, managing IP address allocation and providing network security for connected devices.

- **Bridge**: Allows the router to connect to a wired network and function as a bridge between network devices. In this mode, the router essentially operates as a switch, forwarding data between connected devices without performing NAT, firewall, or DHCP services. This enables seamless communication between devices on the same network by acting as a simple connection point rather than a network gateway.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
