# ポートフォワーディング

このページはファームウェア v4.6 以降で利用できます。古いバージョンについては、[Firewall](firewall.md) を参照してください。

---

Web Admin Panel の左側で、**NETWORK** -> **Port Forwarding** に移動します。

このページでは、**DMZ** や **Port Forwarding** などのファイアウォールルールを設定できます。

**Open Ports on Router** の設定については、**SYSTEM** -> **Security** に移動してください。

## DMZ

DMZ を使うと、1 台のコンピューターをインターネットに公開でき、すべての受信パケットがそのコンピューターにリダイレクトされます。

**Enable DMZ** をオンにし、すべての受信パケットを受け取るホストデバイスの内部 IP アドレスを選択します。

DMZ の優先度を設定できます。DMZ の優先度が Port Forwarding ルールより高い場合、すべての Port Forwarding ルールは無効になります。それ以外の場合は、アクセスされたポートに対応する Port Forwarding ルールがないときのみ、リクエストが DMZ Host デバイスへ転送されます。

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## ポートフォワーディング

Port Forwarding を使うと、リモートコンピューターから LAN 内のルーターのファイアウォール背後にあるローカルコンピューターやサーバー（Web サーバー、FTP サーバーなど）へ接続できます。

Port Forwarding を設定するには、Port Forwarding セクションで **Add** をクリックします。

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

ポップアップウィンドウで新しい Port Forwarding ルールを追加し、**Apply** をクリックします。

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

**Protocol:** 使用するプロトコルです。TCP、UDP、または TCP と UDP の両方を選択できます。

**External Zone:** 外部ゾーンの選択肢は `WAN`、`WireGuard Client`、`WireGuard Server`、`OpenVPN Client`、`OpenVPN Server`、`LAN`、`Guest` です。

**External Port:** 外部ポート番号です。特定のポート番号を入力できます。ポート範囲は 1 から 65535 です。単一ポートを指定することも、先頭と末尾のポート番号を `-` でつないでポート範囲を指定することもできます（例: `501-510`）。

**Internal Zone:** 内部ゾーンの選択肢は `LAN`、`Guest`、`WireGuard Client`、`WireGuard Server`、`OpenVPN Client`、`OpenVPN Server`、`WAN` です。

**Internal IP:** リモートアクセスする対象デバイスにルーターが割り当てた IP アドレスです。**External Port** で単一ポートを設定した場合は、ここでも単一ポートを設定してください。**External Port** でポート範囲を設定した場合は、ここでも対応するポート範囲を設定してください。

**Internal Port:** デバイスの内部ポート番号です。特定のポート番号を入力できます。External Port と同じ場合は空欄のままにしてください。

**Description:** Port Forwarding ルールの名前または説明を設定します（任意）。

**Enable:** ルールを有効または無効にします。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
