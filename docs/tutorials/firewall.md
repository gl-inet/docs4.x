# ファイアウォール

ウェブ管理画面の左側にある -> ファイアウォール

ファイアウォールページでは、次のようなファイアウォールルールを設定することができます。**ポートフォワード**, **ルーターのポート開放** と **DMZ**.

---

## ポートフォワード


ポートフォワーディングは、リモートコンピュータがLANネットワークのファイアウォールの内側のローカルコンピュータまたはサーバー（Webサーバー、FTPサーバーなど）に接続することを可能にします。

ポート転送を設定するには、on the **Port Forwards** タブの **Add**をクリックします。.

![ファイアウォール ページ](https://static.gl-inet.com/docs/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

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

---

## Open Ports on Router

The router's services, such as web and FTP, requires their respective ports to be opened on the router in order to be publicly reachable.

To open a port, click **Add**.

![open Ports on router](https://static.gl-inet.com/docs/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** The name of the rule which can be specified by the user.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**Port:** The port number that you want to open.

**Enable:** Enable of disable of the rule.

---

## DMZ

DMZ lets you to expose one computer to the Internet, so all inbound packets will be redirected to this computer.

Toggle on **Enable DMZ**. Select the internal IP address of your device which is going to receive all the inbound packets.

![Port Forwards](https://static.gl-inet.com/docs/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}
