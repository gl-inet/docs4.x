# ファイアウォール

ウェブ管理パネルの左側 ->ファイアーウォール

ファイアーウォールのページでは、**ポートフォワーディング**、**ルーターのオープンポート**、**DMZ**などのファイアーウォールルールを設定することができます。

---

## ポート転送

ポートフォワーディングは、リモートコンピュータがLANネットワーク内のファイアウォールの内側にあるローカルコンピュータやサーバー（ウェブサーバーやFTPサーバーなど）に接続できるようにします。

ポートフォワーディングを設定するには、**ポート転送**タブで**追加**をクリックします。

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

**新しいポート転送ルールを追加する**ダイアログがポップアップ表示されます。

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**名称:** ルールの名前。

**プロトコル:** 使用するプロトコルは、TCP、UDP、またはTCPとUDPの両方を選択できます。

**外部ゾーン:** 外部ゾーンのオプションは `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` です。

**外部ポート:** 外部ポートの番号。ここに特定のポート番号を入力できます。

**内部ゾーン:** 内部ゾーンのオプションは `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` です。

**内部IP:** リモートアクセスが必要なデバイスにルーターから割り当てられたIPアドレス。

**内部ポート:** デバイスの内部ポート番号。特定のポート番号を入力できます。外部ポートと同じ場合は空欄にしてください。

**有効にする:** ルールの有効/無効を設定する。

---

## ルーターのオープンポート

Web や FTP などのルーターのサービスでは、パブリックにアクセスできるようにするために、ルーター上でそれぞれのポートが開かれている必要があります。

ポートを開くには、**追加**をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**名称:** ユーザーが指定できるルール名。

**プロトコル:** 使用するプロトコルは、TCP、UDP、またはTCPとUDPの両方を選択できます。

**ポート:** 開きたいポート番号。

**有効にする:** ルールを有効または無効にします。

---

## DMZ

DMZでは、1台のコンピュータをインターネットに公開することができ、すべての受信パケットはこのコンピュータにリダイレクトされます。

**DMZを有効にする**をトグルする。すべてのインバウンドパケットを受信するデバイスの内部IPアドレスを選択します。

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
