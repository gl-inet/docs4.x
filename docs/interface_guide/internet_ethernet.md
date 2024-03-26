# イーサネットケーブルでインターネットに接続する

インターネットにアクセスするには、ルーターのWANポートをモデムまたは他のルーターのLANポートにイーサネットケーブルで接続します。

管理画面の左側にある「インターネット」→「イーサネットセクター」をクリックします。

![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_ethernet/ethernet_dhcp.png){class="glboxshadow"}

**注意**: イーサネットケーブルをルーターのWANポートに接続する前に、**LANに変更**をクリックして [WAN ポートを LAN ポートとして設定](../faq/change_wan_to_lan.md)できます。これは、ルーターを [リピーター](internet_repeater.md)として使用する場合に便利です。 その結果、LANポートを1つ増やすことができます。

## プロトコル

DHCP、Static、PPPoEの3種類のプロトコルがあります。変更するには**修正**をクリックします。

* DHCP 

    DHCPはデフォルトで最も一般的なプロトコルです。これは、インターネットプロトコル（IP）ネットワークで使用されるネットワーク管理プロトコルで、クライアントサーバーアーキテクチャを使用して、ネットワークに接続されたデバイスにIPアドレスやその他の通信パラメータを自動的に割り当てます。

* Static

    インターネットサービスプロバイダ（ISP）が固定IPアドレスを提供している場合、またはIPアドレス、ゲートウェイ、ネットマスクなどのネットワーク情報を手動で設定したい場合は、スタティックが必要です。

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_ethernet/ethernet_static.png){class="glboxshadow"}

* PPPoE

    PPPoEは、多くのインターネットサービスプロバイダ（ISP）で必要とされています。一般的に、ISPはあなたにモデムを提供し、インターネット接続を作成するときに必要なユーザー名とパスワードを提供します。

    **VLAN ID**： この設定項目は、プロバイダーのPPPoEサーバーがインターフェイスにタグ付けされた特定のVLAN IDを使用するよう要求する場合にのみ必要です。

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_ethernet/ethernet_pppoe.png){class="glboxshadow gl-90-desktop"}

## 警告

インターネットにアクセスできない場合は、対応する警告が表示されます。インターネットにアクセスできるかどうかは、 [マルチWAN](multi-wan.md) ページをご覧ください。

- 警告 : *インターフェースは接続されていますが、IPv4プロトコルでインターネットにアクセスできません。*

    ![ethernet wrning](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_ethernet/ethernet_warning.png){class="glboxshadow gl-90-desktop"}

    解決方法 :イーサネットのアップストリームデバイスがインターネットにアクセスできるかどうか確認してください。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット・アクセス方式を同時に使用する場合のロードバランスの設定方法は？](multi-wan.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
