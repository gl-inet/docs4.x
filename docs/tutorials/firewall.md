# FIREWALL

On the left side of web Admin Panel -> FIREWALL

In FIREWALL page, you can set up firewall rules like **Port Forwarding**, **Open Ports on Router** and **DMZ**.

## Port Forwards

Port Forwarding lets remote computers to connect to a local computer or server behind the firewall in the LAN network (such as web servers, FTP servers, etc).

To set up port forwarding, on the **Port Forwards** tab click **Add**.

![firewall page](https://static.gl-inet.com/docs/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

It will pop up **Add New Port Forward Rule** dialog.

![add new port forward rule](https://static.gl-inet.com/docs/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** The name of the rule.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**External Zone:** The options for external zone are `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** The numbers of external ports. You can enter a specific port number or a range of service ports (E.g **100-300**).

**Internal Zone:** The options for external zone are `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** The IP address assigned by the router to the device which needs to be accessed remotely.

**Internal Port:** The internal port number of the device. You can enter a specific port number. Leave it blank if it is same as the external port.

**Enable:** Enable of disable of the rule.

## Open Ports on Router

The router's services, such as web and FTP, requires their respective ports to be opened on the router in order to be publicly reachable.

To open a port, click **Add**.

![open Ports on router](https://static.gl-inet.com/docs/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** The name of the rule which can be specified by the user.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**Port:** The port number that you want to open.

**Enable:** Enable of disable of the rule.

## DMZ

DMZ lets you to expose one computer to the Internet, so all inbound packets will be redirected to this computer.

Toggle on **Enable DMZ**. Select the internal IP address of your device which is going to receive all the inbound packets.

![Port Forwards](https://static.gl-inet.com/docs/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}
