# ファイアウォール

このガイドはファームウェアv4.5で前に当てはまります。

v4.6で降、ファイアウォールページは分割されました。ポートフォワーディングとDMZ機できるは[ポートフォワーディング](port_forwarding.md)に移動しました。オープンポート機できるは[セキュリティ](security.md)に移動しました。

---

ウェブ管理パネルの左側 -> ネットワーク -> ファイアウォール

ファイアウォールページでは、**ポートフォワーディング**、**ルーターのオープンポート**、**DMZ**などのファイアウォールルールを設定できます。

## ポート転送

ポートフォワーディングを使用すると、リモートコンピュータがLAN内のルーターファイアウォールの内側にあるローカルコンピュータやサーバー（ウェブサーバーやFTPサーバーなど）に接続できます。

ポートフォワーディングを設定するには、**ポート転送**タブをクリックし、**追加**をクリックします。

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

ポップアップウィンドウで新しいポート転送ルールを追加し、**適用**をクリックします。

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**名称:** ルールの名前。

**プロトコル:** 使用するプロトコル。TCP、UDP、またはTCPとUDPの両方を選択できます。

**外部ゾーン:** 外部ゾーンのオプションは `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` です。

**外部ポート:** 外部ポートの番号。特定のポート番号を入力できます。

**内部ゾーン:** 内部ゾーンのオプションは `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` です。

**内部IP:** リモートアクセスが必要なデバイスにルーターから割り当てられたIPアドレス。

**内部ポート:** デバイスの内部ポート番号。特定のポート番号を入力できます。外部ポートと same じ場合は空欄にしてください。

**有効にする:** ルールの有効/無効を設定します。

## ルーターのオープンポート

ウェブやFTPなどのルーターのサービスでは、公にアクセスできるようにするために、ルーター上で respective ポートが開かれている必要があります。

ポートを開くには、**ルーターのオープンポート**タブに切り替えて、**追加**をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

ポップアップウィンドウで新しいポートを開き、**適用**をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**名称:** ユーザーが指定できるルールの名前。

**プロトコル:** 使用するプロトコル。TCP、UDP、またはTCPとUDPの両方を選択できます。

**ポート:** 開きたいポート番号。

**有効にする:** ルールの有効または無効を設定します。

## DMZ

DMZを使用すると、1台のコンピュータをインターネットに公開でき、すべての受信パケットはこのコンピュータにリダイレクトされます。

**DMZを有効にする**をオンにします。すべての受信パケットを受け取るホストデバイスの内部IPアドレスを選択します。

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
