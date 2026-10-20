# ファイアウォール

このガイドはファームウェア v4.5 以前に適用されます。

v4.6 以降、Firewall ページは分割されました。Port Forwarding と DMZ の機能は [Port Forwarding](port_forwarding.md) に移動し、Open Ports 機能は [Security](security.md) に移動しました。

---

Web Admin Panel の左側で、**NETWORK** -> **Firewall** に移動します。

このページでは、**Port Forwarding**、**Open Ports on Router**、**DMZ** などのファイアウォールルールを設定できます。

## ポートフォワーディング

Port Forwarding を使うと、リモートコンピューターから LAN 内のルーターのファイアウォール背後にあるローカルコンピューターやサーバー（Web サーバー、FTP サーバーなど）へ接続できます。

Port Forwarding を設定するには、**Port Forwards** タブをクリックし、**Add** をクリックします。

![firewall page](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/firewall.png){class="glboxshadow"}

ポップアップウィンドウでポート転送ルールを追加し、**Apply** をクリックします。

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** ルール名を入力します。

**Protocol:** TCP、UDP、またはその両方を選択します。

**External Zone:** 受信トラフィックが入ってくるインターフェースを選択します。選択肢は `LAN`、`WAN`、`guest`、`ovpnclient`、`ovpnserver`、`wgclient`、`wgserver` です。VPN関連の選択肢は、VPN接続を設定した後にのみ表示されます。

**External Port:** 外部ポート番号を入力します。

**Internal Zone:** トラフィックの転送先インターフェースを選択します。選択肢は `LAN`、`WAN`、`guest`、`ovpnclient`、`ovpnserver`、`wgclient`、`wgserver` です。VPN関連の選択肢は、VPN接続を設定した後にのみ表示されます。

**Internal IP:** リモートアクセスするデバイスのLAN IPアドレスを入力します。

**Internal Port:** デバイスの内部ポート番号を入力します。外部ポートと同じ場合は空欄にします。

**Enable:** スイッチでルールを有効または無効にします。

## ルーターで開いているポート

Web や FTP などのルーターサービスを外部から利用できるようにするには、それぞれのポートをルーター上で開放する必要があります。

ポートを開放するには、**Open Ports on Router** タブに切り替えて **Add** をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/open_ports_on_router.png){class="glboxshadow"}

ポップアップウィンドウで新しいポートを開放し、**Apply** をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** ユーザーが指定できるルール名です。

**Protocol:** 使用するプロトコルです。TCP、UDP、または TCP と UDP の両方を選択できます。

**Port:** 開放するポート番号です。

**Enable:** ルールを有効または無効にします。

## DMZ

DMZ を使うと、1 台のコンピューターをインターネットに公開でき、すべての受信パケットがそのコンピューターにリダイレクトされます。

**Enable DMZ** をオンにし、すべての受信パケットを受け取るホストデバイスの内部 IP アドレスを選択します。

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/dmz.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
