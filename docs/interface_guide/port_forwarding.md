# Port Forwarding

This page has been added since firmware v4.6. For older firmware versions, please refer to [Firewall](firewall.md).

---

On the left side of web Admin Panel -> NETWORK -> Port Forwarding

This page allows you to set firewall rules like **DMZ** and **Port Forwarding**.

For **Open Ports on Router** settings, please go to SYSTEM -> Security.

## DMZ

DMZ lets you to expose one computer to the Internet, so all inbound packets will be redirected to this computer.

Toggle on **Enable DMZ**. Select the internal IP address of your host device, which is going to receive all the inbound packets.

You can set the priority for the DMZ. If the DMZ priority is higher than the port forwarding rules, all port forwarding rules will be invalidated. Otherwise, requests will be forwarded to the DMZ Host device only if the accessed port has no corresponding port forwarding rule.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding

Port Forwarding lets remote computers connect to a local computer or server behind the router's firewall in the LAN (such as web servers, FTP servers, etc).

To set up port forwarding, click **Add** in the Port Forwarding section.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

In the pop-up window, add a new port forwarding rule, and click **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**External Zone:** The options for external zone are `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN`, `Guest`.

**External Port:** The numbers of external ports. You can enter a specific port number here. The port range is from 1 to 65535. You can set a single port or set the port range by concatenating the first and last port numbers with the - symbol (Such as 501-510).

**Internal Zone:** The options for internal zone are `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `WAN`.

**Internal IP:** The IP address assigned by the router to the device which needs to be accessed remotely. If you set a single port in **External Port**, you should set the single port here. If you set a port range in **External Port**, you should set the corresponding port range here.

**Internal Port:** The internal port number of the device. You can enter a specific port number. Leave it blank if it is same as the external port.

**Description:** Set a name or add a description for the port forwarding rule (optional).

**Enable:** Enable or disable the rule.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
