# イーサネットケーブルでインターネットに接続する

WANポートに接続したイーサネットケーブルで、ルーターをブロードバンドネットワークに接続します。通常は自動的にIPアドレス（DHCP）を取得しますが、Static IP や PPPoE を手動で設定することもできます。この方法は安定性が高く速度も速いため、固定ブロードバンド回線を利用する家庭やオフィスに適しています。

以下の手順に従って、イーサネットケーブルでルーターをインターネットに接続してください。

1. ルーターの WAN ポートを、イーサネットケーブルで上流機器（ISPモデム、ルーター、ネットワークスイッチ、またはイーサネットジャックなど）に接続します。

2. ルーターの Web 管理パネルにログインし、**INTERNET** -> **Ethernet** に移動します。

    接続に成功すると、Ethernet セクションに Protocol、IP Address、Gateway、DNS Server などのネットワーク情報が表示されます。

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**ヒント**: ルーターの WAN ポートにイーサネットケーブルを挿す前に、**Change to LAN** をクリックして [WANポートをLANポートとして設定](../faq/change_wan_to_lan.md)できます。これはルーターを[リピーター](internet_repeater.md)として使用する場合に便利です。物理 WAN ポートが未使用になるため、LAN ポートとして再利用して LAN ポートを1つ増やせます。

## プロトコル

利用できるプロトコルは DHCP、Static、PPPoE の3種類です。変更するには **Modify** をクリックします。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP はデフォルトかつ最も一般的なプロトコルで、IPネットワーク上のクライアントサーバー方式により、ネットワーク機器へ IP アドレスやその他の通信パラメーターを自動的に割り当てます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    ISP（インターネットサービスプロバイダー）から固定 IP アドレスが提供される場合や、IP Address、Gateway、Netmask などのネットワーク情報を手動で設定したい場合に必要です。

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE は多くの ISP で使われているプロトコルです。通常、インターネット設定に必要なモデムとユーザー名・パスワードが提供されます。

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Advanced

基本設定に加えて、上記3つのプロトコルには次のようなオプションの詳細設定があります。

* **VLAN ID**: プロバイダー側のサーバーで、特定のタグ付き VLAN ID の使用が必要な場合にのみ設定します。

* **TTL**: TTL（Time To Live）は、パケットがネットワーク内で生存できる最大時間を定義します。デフォルトでは、ルーターはクライアントデバイスから受信したパケットを転送する前に TTL を 1 減算します。上書きが必要な場合は、ここで固定値を設定できます。TTL 設定は IPv4 でのみ有効です。

* **HL**: IPv6 では、HL（Hop Limit）フィールドがネットワーク内でのデータパケットの転送ホップ数を制限し、IPv4 の TTL に相当します。

* **MTU**: デフォルトの MTU 値は 1500 バイトです。

## Ethernet Port

右上の歯車アイコンをクリックすると、[Ethernet Port](ethernet_port.md) に移動できます。

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

**WAN** ページには、ポートの役割（WAN または LAN として使用）、MAC mode と MAC address、そしてネゴシエートされたポート速度が表示されます。

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

**LAN** ページには、ポートの役割とネゴシエートされたポート速度が表示されます。

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

詳細はこの[リンク](ethernet_port.md)を参照してください。

## トラブルシューティング

WAN ポートにイーサネットケーブルが接続されていてもインターネットに接続できない場合は、次の黄色いメッセージが表示されます。

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

この問題を解決するには、次を確認してください。

1. 上流機器がインターネットに接続できているか確認します。

2. [Multi-WAN](multi-wan.md) ページで Ethernet インターフェースの状態を確認します。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネット接続方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット接続方法を同時に使用する場合、ロードバランスをどのように設定しますか？](multi-wan.md)

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
