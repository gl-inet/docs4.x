# GoodCloud Site to Site

## 導入

GoodCloud Site to Site は、複数の場所にあるオフィスがインターネットを介してお互いに安全な接続を確立できるようにします。これにより、会社のネットワークが拡張され、ある場所のコンピュータリソースが他の場所の従業員に利用可能になります。

<a href="https://static.gl-inet.com/www/images/solutions/s2s/s2s_main_5.png" target="_blank"><img alt="site to site diagram" src="https://static.gl-inet.com/www/images/solutions/s2s/s2s_main_5.png"></a>

シナリオ 1：会社が複数の支店を持っており、それらを単一のプライベートネットワークに結合してリソースを共有したい場合。

シナリオ 2：会社がパートナー企業と密接な関係を持っており、Site to Site を使用して、企業が安全で共有されたネットワーク環境で一緒に作業できるようにします。

シナリオ 3：家庭にIPカメラがあり、家にいないときにSite to Site を使用してIPカメラにリモートアクセスできるようにします。

## 条件

場所が異なる少なくとも2つのGL.iNetルーターが必要で、そのうちの1つはパブリックIPアドレスを持っている必要があります。 [ISP がパブリック IP アドレスを割り当てているかどうかを確認してください](how_to_check_if_isp_assigns_you_a_public_ip_address.md)。ファームウェアバージョン3.026以上が必要です。

注意：ノードがVPNクライアントも実行している場合、ネットワークが特に複雑になる可能性があるため、Site to Siteの実行は推奨されません。

## サイト間ネットワークを構築する手順

1. ルーターをGoodCloudにバインドします。[方法はこちら](../interface_guide/cloud.md#add-device)

2. 以下の手順に従って、Site to Site ネットワークを作成します。

    ![create a site to site network](https://static.gl-inet.com/goodcloud/docs/create-s2s-01.png){class="glboxshadow"}

    デフォルトのポートは51830です。別のポートを使用したい場合は、左下隅の「Advanced」オプションを見つけてください。

    デバイスの性能により、各Site to Site ネットワークには最大10台のデバイスを接続できます。

    デバイスを選択した後、続行をクリックします。

    ![create a site to site network](https://static.gl-inet.com/goodcloud/docs/create-s2s-02.png){class="glboxshadow"}

    次に、各デバイスがSite to Siteのメインノードとして設定できるかどうかをテストします。

    性能が強力でネットワーク速度が最適なルーターをメインノードにすることをお勧めします。

    ![testing each device](https://static.gl-inet.com/goodcloud/docs/testing-s2s-01.png){class="glboxshadow"}

    どのデバイスもメインノードとして使用できない場合は、次の点を確認してください：

    - ルーターのうちの1つがパブリックIPアドレスを持っていること（静的パブリックIPまたは動的パブリックIP）。
    - ポートが開いていること（デフォルトは51830）。
    - ルーターがNATの背後にある場合、ポートフォワーディングの設定が必要な場合があります。

    ポートを変更して再試行することもできます。
![testing each device](https://static.gl-inet.com/goodcloud/docs/testing-s2s-02.png){class="glboxshadow"}

複数のデバイスがメインノードとして設定できる場合は、続行するデバイスを選択する必要があります。

![testing each device](https://static.gl-inet.com/goodcloud/docs/testing-s2s-03.png){class="glboxshadow"}

メインノードとして設定できるデバイスが1つしかない場合は、直接Site to Site詳細ページに移動します。

ネットワークはデフォルトで停止しています。LAN IPを確認し、問題がなければ「スタート」ボタンをクリックし、問題がある場合は「設定」をクリックしてLAN IPを変更します。

![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

数分待つと、ノードの接続ステータスが表示されます。実線は接続済み、破線は未接続を意味します。

![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## サイト間接続のテスト

これでSite to Siteネットワークが作成され、開始されましたので、接続をテストしましょう。

PCまたは携帯電話を使用して、このSite to Siteのノードの1つに接続し、ブラウザを使用して別のノードのLAN IPにアクセスします。ログインページが表示された場合、これらのノード間の接続が機能していることを意味します。

例えば、私のPCがノード1デバイスに接続している場合、ブラウザを使用してメインノードのLAN IP（192.168.48.1）にアクセスし、ログインページが表示された場合、ノード1とメインノードの間の接続が機能していることを意味します。

## ルートおよびその他のオプション

各デバイスのLAN IPとルートを変更できます。

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s.png){class="glboxshadow"}

デフォルトでは、各ノードは他のノードのLANにアクセスできますが、セキュリティ上の理由から、対応するサービスIPのみを開くことをお勧めします。

例えば、ノード1のサブネットにサーバーA（172.30.97.100）がある場合、他のSite to Siteノードがノード1のサービスAにのみアクセスできるようにするには、以下のように設定できます。

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

ノードの親ルートを追加することもできます。

各サブノードはメインノードに暗号化されたトンネルネットワークを構築します。トンネルサブネットのIPを変更したい場合は、「IPアドレス範囲」をクリックします。

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。