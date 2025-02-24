# Port Forwarding

This page was added since v4.6. For older versions, please view [Firewall](firewall.md).

---

On the left side of web Admin Panel -> NETWORK -> Port Forwarding

In this page, you can set up firewall rules like **DMZ** and **Port Forwarding**.

For **Open Ports on Router**, please go to SYSTEM -> Security.

---

## DMZ

DMZ lets you to expose one computer to the Internet, so all inbound packets will be redirected to this computer.

Toggle on **Enable DMZ**. Select the internal IP address of your device which is going to receive all the inbound packets.

You can select the priority of the DMZ. If the priority of the DMZ is higher than the port forwarding rules, all the port forwarding rules will be invalidated. Otherwise, only if the accessed port does not have a corresponding port forwarding rule, the request will be forwarded to the client device set by the DMZ.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

---

## Port Forwarding

Port Forwarding lets remote computers to connect to a local computer or server behind the firewall in the LAN network (such as web servers, FTP servers, etc).

To set up port forwarding, on the **Port Forwarding** tab click **Add**.

![port forwarding](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding.png){class="glboxshadow"}

It will pop up **Add New Port Forward Rule** dialog.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** The name of the rule.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**External Zone:** The options for external zone are `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN`, `Guest`.

**External Port:** The numbers of external ports. You can enter a specific port number here. The port range is from 1 to 65535. You can set a single port or set the port range by concatenating the first and last port numbers with the - symbol (Such as 501-510).

**Internal Zone:** The options for internal zone are `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `WAN`.

**Internal IP:** The IP address assigned by the router to the device which needs to be accessed remotely. If you set a single port in **External Port**, you should set the single port here. If you set a port range in **External Port**, you should set the corresponding port range here.

**Internal Port:** The internal port number of the device. You can enter a specific port number. Leave it blank if it is same as the external port.

**Enable:** Enable or disable of the rule.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
