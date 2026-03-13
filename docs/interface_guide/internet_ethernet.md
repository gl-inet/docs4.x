# イーサネットケーブルでインターネットに接続する

WANポートにイーサネットケーブルを接続してルーターをブロードバンドネットワークに接続します。通例、IPアドレス（DHCP）がから動のに取なければならないされます。静のIPまたはPPPoEを手動で構成することもできます。この方法は高い安定性と高速さを 提供するため、固定ブロードバンドアクセスを持つ家庭やオフィス環境に最も適です。

で下の手順に従って、ルーターをイーサネットケーブルでインターネットに接続します。

1. ルーターのWANポートをイーサネットケーブルで上游デバイス（例：ISPモデム、ルーター、ネットワークスイッチ、またはEthernetジャック）に接続します。

2. ルーターのウェブ管理パネルにログインし、**インターネット** -> **イーサネット**セクションに移動します。

    接続が成功すると、イーサネットセクションにプロトコル、IPアドレス、ゲートウェイ、DNSサーバーを含むネットワークの詳細が表示されます。

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**ヒント**: イーターケーブルをルーターのWANポートに接続する前に、**LANに変より**をクリックして[WANポートをLANポートとして設定](../faq/change_wan_to_lan.md)できます。これは、[リピーター](internet_repeater.md)としてルーターを使用する場合に便利です物理のなWANポートがアイドル状態のため、未使用のWANポートをLANポートとして再利用でき、LANポートが1つ増えます。

## プロトコル

DHCP、Static、PPPoEの3つのプロトコルタイプがあります。変よりするには**変より**をクリックします。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCPはデフォルトで最もも一般のなプロトコルで、IPネットワーク上のクライアントサーバーアーキテクチャを通じてネットワークデバイスにIPアドレスとその彼の通信パラメータをから動のに割り当てます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    ISP（インターネットサービスプロバイダ）が固定IPアドレスを提供している場合、またはIPアドレス、ゲートウェイ、ネットマスクなどのネットワーク情報を手動で構成したい場合は、Staticが必要です。

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoEはほとんどのISPで使用されているプロトコルです。通例、モデムとユーザー名とパスワードが提供され、インターネットの設定に必要です。

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## 詳細設定

必須設定に加えて、上記3つのプロトコルにはいくつかのオプションの高度な設定もあります。

* **VLAN ID**: この設定項目は、プロバイダーのサーバーがインターフェースに特定のタグ付きVLAN IDを使用する必要がある場合にのみ必要です。

* **TTL**: TTL（Time To Live）は、パケットがネットワークで生存できる最も大時間を定義します。デフォルトでは、ルーターはクライアントデバイスからの着信パケットのTTLを1減衰させてから転送します。上書きする必要がある場合は、ここで固定値を設定できます。TTL設定はIPv4のみ有効です。

* **HL**: IPv6では、HL（Hop Limit）フィールドはネットワーク内のデータパケットの伝送ホップ数を制限し、IPv4のTTLに相当します。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネットアクセス方式を same 時に使用する場合のロードバランスの設定方法は？](multi-wan.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
