# ファイアウォール

このガイドはファームウェア v4.5 以前に適用されます。

v4.6 以降、Firewall ページは分割されました。Port Forwarding と DMZ の機能は [Port Forwarding](port_forwarding.md) に移動し、Open Ports 機能は [Security](security.md) に移動しました。

---

Web Admin Panel の左側で、**NETWORK** -> **Firewall** に移動します。

このページでは、**Port Forwarding**、**Open Ports on Router**、**DMZ** などのファイアウォールルールを設定できます。

## ポートフォワーディング

Port Forwarding を使うと、リモートコンピューターから LAN 内のルーターのファイアウォール背後にあるローカルコンピューターやサーバー（Web サーバー、FTP サーバーなど）へ接続できます。

Port Forwarding を設定するには、**Port Forwards** タブをクリックし、**Add** をクリックします。

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

ポップアップウィンドウで新しいポート転送ルールを追加し、**Apply** をクリックします。

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** ルール名です。

**Protocol:** 使用するプロトコルです。TCP、UDP、または TCP と UDP の両方を選択できます。

**External Zone:** 外部ゾーンの選択肢は `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` です。

**External Port:** 外部ポート番号です。特定のポート番号を入力できます。

**Internal Zone:** 内部ゾーンの選択肢は `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` です。

**Internal IP:** リモートアクセスする対象デバイスにルーターが割り当てた IP アドレスです。

**Internal Port:** デバイスの内部ポート番号です。特定のポート番号を入力できます。External Port と同じ場合は空欄のままにしてください。

**Enable:** ルールを有効または無効にします。

## ルーターで開いているポート

Web や FTP などのルーターサービスを外部から利用できるようにするには、それぞれのポートをルーター上で開放する必要があります。

ポートを開放するには、**Open Ports on Router** タブに切り替えて **Add** をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

ポップアップウィンドウで新しいポートを開放し、**Apply** をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** ユーザーが指定できるルール名です。

**Protocol:** 使用するプロトコルです。TCP、UDP、または TCP と UDP の両方を選択できます。

**Port:** 開放するポート番号です。

**Enable:** ルールを有効または無効にします。

## DMZ

DMZ を使うと、1 台のコンピューターをインターネットに公開でき、すべての受信パケットがそのコンピューターにリダイレクトされます。

**Enable DMZ** をオンにし、すべての受信パケットを受け取るホストデバイスの内部 IP アドレスを選択します。

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
