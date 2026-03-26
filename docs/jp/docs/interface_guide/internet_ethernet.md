# イーサネットケーブルでインターネットに接続する

WANポートにイーサネットケーブルを接続してルーターをブロードバンドネットワークに接続します。通常、IPアドレスを自動的に取得します（DHCP）。ユーザーは、静的IPまたはPPPoEを手動で設定することも可能です。この方法は高い安定性と高速性を兼ね備えており、固定ブロードバンド回線が利用可能な家庭やオフィス環境に最適です。

以下の手順に従って、イーサネットケーブルを使用してルーターをインターネットに接続してください。

1. ルーターのWANポートを、イーサネットケーブルを使用して上流の機器（例：ISPモデム、ルーター、ネットワークスイッチ、またはイーサネットジャック）に接続してください。

2. ルーターのウェブ管理画面にログインし、**インターネット** -> **イーサネット**セクションへ移動してください。

    接続が成功すると、イーサネットセクションにプロトコル、IPアドレス、ゲートウェイ、DNSサーバーを含むネットワークの詳細が表示されます。

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**ヒント**: イーサネットケーブルをルーターのWANポートに接続する前に、**LANに変更**をクリックして[WANポートをLANポートとして設定](../faq/change_wan_to_lan.md)することができます。ルーターを[リピーター](internet_repeater.md)として使用する場合、物理なWANポートはアイドル状態となります。そのため、未使用のWANポートをLANポートとして転用することで、LANポートを1つ増やすことができます。

## プロトコル

プロトコルには、DHCP、Static、PPPoEの3種類があります。変更するには**変更**をクリックしてください。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCPは、IPネットワーク上においてクライアントサーバーアーキテクチャを通じて、ネットワークデバイスにIPアドレスやその他の通信パラメータを自動的に割り当てる、デフォルトかつ最も一般的なプロトコルです。

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    ISP（インターネットサービスプロバイダー）から固定IPアドレスが提供されている場合、あるいはIPアドレス、ゲートウェイ、ネットマスクなどのネットワーク情報を手動で設定したい場合には、「Static（固定）」の設定が必要です。

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoEは、ほとんどのISPで使用されているプロトコルです。通常、ISPからはモデム、およびインターネット接続の設定に必要なユーザー名とパスワードが提供されます。

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## 詳細設定

必須の設定に加え、上記3つのプロトコルには、いくつかのオプションの詳細設定も用意されています。

* **VLAN ID**: この設定項目は、プロバイダーのサーバーが、インターフェースに特定のタグ付きVLAN IDの使用を要求する場合にのみ必要となります。

* **TTL**: TTL（Time To Live）は、パケットがネットワーク内で存続できる最大時間を定義しするものです。デフォルトでは、ルーターはクライアントデバイスから受信したパケットを転送する前に、そのTTL値を1だけ減らします。この設定を上書きする必要がある場合は、ここで固定値を指定することができます。なお、TTLの設定はIPv4のみ有効です。

* **HL**: IPv6では、HL（Hop Limit）フィールドはネットワーク内におけるデータパケット内の送信ホップ数を制限する役割を果たし、IPv4におけるTTLに相当します。

* **MTU**: デフォルトのMTU値は1500バイトです。

## イーサネットポート

右上の歯車アイコンをクリックして、[イーサネットポート](ethernet_port.md)に進んでください。

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

**WAN**ページには、ポートの役割（例：WANまたはLANとしての使用）、MACモードおよび、 MACアドレス、ならびにネゴシエーションされたネットワークポート速度が表示されます。 

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

**LAN**ページには、ポートの役割およびネゴシエートされたネットワークサポート速度が表示されます。

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

詳細については、こちらの[linkリンク](ethernet_port.md)をご参照ください。

## トラブルシューティング

WANポートにイーサネットケーブルが接続されているにもかかわらず、インターネットに接続できない場合、以下に示すような黄色のメッセージが表示されます。

**「インターフェースは接続されていますが、インターネットにアクセスできません。」**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

この問題を解決するには：

1. 上流のデバイスがインターネットに接続できているか確認してください。

2. [マルチWAN](multi-wan.md) ページに移動し、イーサネットインターフェースのステータスを確認してください。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネット接続方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット接続方法を同時に使用する場合のロードバランスの設定方法は？](multi-wan.md)

---

ご不明な点がございましたら、 [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
