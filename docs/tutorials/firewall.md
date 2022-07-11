# ファイアウォール

ウェブ管理画面の左側にある -> ファイアウォール

ファイアウォールページでは、次のようなファイアウォールルールを設定することができます。**ポートフォワード**, **ルーターのポート開放** と **DMZ**.

---

## ポートフォワード


ポートフォワーディングは、リモートコンピュータがLANネットワークのファイアウォールの内側のローカルコンピュータまたはサーバー（Webサーバー、FTPサーバーなど）に接続することを可能にします。

ポート転送を設定するには、on the **Port Forwards** タブの **Add**をクリックします。.

![ファイアウォール ページ](https://static.gl-inet.com/docs/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

**新しいポートフォワードルールの追加**」ダイアログが表示されます。

![add new port forward rule](https://static.gl-inet.com/docs/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**名前:** 規則の名前です。

**Protocol:** 使用するプロトコルは、TCP、UDP、またはTCPとUDPの両方が選択できます。

**外部ゾーン:** 外部ゾーンのオプションは `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` である。

**外部ポート:** 外部ポートの番号です。特定のポート番号またはサービスポートの範囲（例：100-300**）を入力することができます。

**内部ゾーン:** 外部ゾーンのオプションは `WAN`、`wgclient`、`wgserver`、`ovpnclient`、`ovpnserver` である。

**内部IP：**  リモートアクセスが必要な機器にルーターから割り当てられたIPアドレスです。 

**Internal Port:** 機器の内部ポート番号です。特定のポート番号を入力することができます。外部ポートと同じ場合は空欄にしてください。

 **有効** ルールの有効/無効を設定します。

---

## ルーターのポート開放

WebやFTPなどのルーターのサービスは、一般に到達できるようにするために、それぞれのポートがルーター上で開いている必要があります。

ポートを開くには、**Add**をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**名前:** ユーザーが指定可能なルールの名前。

**プロトコル**：使用するプロトコルを、TCP、UDP、またはTCPとUDPの両方から選択できます。

**ポート:** 開放したいポート番号。

**有効:** ルールの有効・無効を設定します。

---

## DMZ

DMZは、1台のコンピュータをインターネットに公開し、すべての受信パケットをこのコンピュータにリダイレクトさせることができます。

DMZを有効にする**をトグルします。すべての受信パケットを受信するデバイスの内部IPアドレスを選択します。

![Port Forwards](https://static.gl-inet.com/docs/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}
