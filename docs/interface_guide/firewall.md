# Firewall

**Note**: Since v4.6, the Firewall page has been split. The Port Forwarding and DMZ features have been moved to the [Port Forwarding](port_forwarding.md). The Open Ports feature has been moved to the [Security](security.md).

This document applies to the firmware versions prior to v4.6.

---

On the left side of web Admin Panel -> NETWORK -> Firewall

The Firewall page allows you to set firewall rules like **Port Forwarding**, **Open Ports on Router** and **DMZ**.

## Port Forwards

Port Forwarding lets remote computers connect to a local computer or server behind the router's firewall in the LAN (such as web servers, FTP servers).

To set up port forwarding, click the **Port Forwards** tab, then click **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

In the pop-up window, add a new port forward rule, and click **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** The name of the rule.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**External Zone:** The options for external zone are `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** The numbers of external ports. You can enter a specific port number here.

**Internal Zone:** The options for internal zone are `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** The IP address assigned by the router to the device which needs to be accessed remotely.

**Internal Port:** The internal port number of the device. You can enter a specific port number. Leave it blank if it is same as the external port.

**Enable:** Enable or disable the rule.

## Open Ports on Router

The router's services, such as web and FTP, requires their respective ports to be opened on the router in order to be publicly reachable.

To open a port, switch to the **Open Ports on Router** tab, then click **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

In the pop-up window, open a new port and click **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** The name of the rule which can be specified by the user.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**Port:** The port number that you want to open.

**Enable:** Enable or disable the rule.

## DMZ

DMZ lets you to expose one computer to the Internet, so all inbound packets will be redirected to this computer.

Toggle on **Enable DMZ**. Select the internal IP address of your host device which is going to receive all the inbound packets.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
