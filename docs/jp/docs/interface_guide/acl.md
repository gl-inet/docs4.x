# ACL

> ACL 機能は firmware v4.9 で追加されました。

ACL は Access Control List の略で、接続プロトコル、デバイスアドレス、ポートに基づいてネットワークトラフィックを管理するルールを作成できます。ネットワークアクセスを許可するかブロックするかを制御し、複数の ACL ルールが競合した場合は、優先度の高いルールが適用されます。

ACL は Port Forwarding とは役割が異なります。ACL は主にセキュリティ目的でネットワークアクセスの許可や遮断を行い、Port Forwarding は外部トラフィックをローカルネットワーク内の特定デバイスへ転送して、ローカルサービスへのリモートアクセスを可能にします。

---

Web Admin Panel の左側で、**SECURITY** -> **ACL** に移動します。

右側の **Add Rule** ボタンをクリックします。

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

ポップアップウィンドウで ACL ルールを作成し、**Apply** をクリックします。

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: ルールのカスタム名を入力します。

- **Protocol**: このルールを適用するネットワークトラフィックの種類を指定します。`Any`、`TCP`、`UDP`、`TCP+UDP`、`ICMP` から接続プロトコルを選択します。

- **IP Type**: ネットワークトラフィックの IP アドレス形式を定義します。`IPv4 & IPv6`、`IPv4`、`IPv6` から選択します。

- **Source Zone**: トラフィックの送信元となるネットワークゾーンを選択します。利用できるオプションは `LAN`、`Guest`、`IoT`、`WAN` です。

- **Source Address**: （任意）特定の送信元デバイスまたは IP アドレスにルールを制限します。ドロップダウンリストから送信元アドレスを選択できます。

- **Destination Zone**: トラフィックの宛先となるネットワークゾーンを選択します。利用できるオプションは `LAN`、`Guest`、`IoT`、`WAN` です。

- **Destination Address**: （任意）特定の宛先デバイスまたは IP アドレスにルールを制限します。ドロップダウンリストから宛先アドレスを選択できます。

- **Action**: このルールに一致するトラフィックを `Accept` するか `Block` するかを選択します。

- **Enable**: このルールを有効または無効にします。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。