# GoodCloud Site to Site

## はじめに

GoodCloud Site to Site を使用すると、複数の拠点にあるオフィス同士をインターネット経由で安全に接続できます。これにより企業ネットワークを拡張し、ある拠点のコンピューターリソースを、ネットワーク上の別拠点にいる従業員も利用できるようになります。

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenario 1**: 同じ会社に属する多数の支店を、1つの統合されたプライベートネットワークにまとめ、全拠点でシームレスにリソース共有したい場合。

**Scenario 2**: 密接に連携する2社が、業務コラボレーションのために、共有された安全なネットワーク環境を必要とする場合。

**Scenario 3**: 自宅に IP カメラがある家庭で、外出中の家族がそのデバイスへリモートアクセスし、どこからでも簡単に監視したい場合。

## 条件

1. Site to Site ネットワークを構築するには、少なくとも 2 台の GL.iNet ルーターが必要です。

2. 少なくとも 1 台のルーターはパブリックIPアドレスを持ち、メインノードとして設定できる必要があります。[ISP がパブリックIPアドレスを割り当てているか確認する](how_to_check_if_isp_assigns_you_a_public_ip_address.md)。

    メインノードには、性能が高く、ネットワーク速度が最も良いルーターを選ぶことを推奨します。

3. サブノードで VPNクライアント / Tailscale / ZeroTier / AstroWarp を同時に実行しながら Site to Site を使用することは **推奨されません**。ネットワーク構成が特に複雑になるためです。

## Site to Site ネットワークを構築する

1. ルーターを GoodCloud アカウントにバインドします。[方法はこちら](../interface_guide/cloud.md/#setup-your-goodcloud-account)。

2. [GoodCloud](https://www.goodcloud.xyz/#/login) にログインし、左側のサイドバーで **Site to Site** に移動します。右上の **Create Network** をクリックします。

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. 左側のチェックボックスをオンにして、少なくとも 2 台のデバイスを選択します。

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

    選択したデバイスはページ下部に表示されます。

    Site to Site のデフォルトポートは **51830** です。別のポートを使用したい場合は、左下の **Advanced** をクリックして変更します。その後 **Next** をクリックします。

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    安定したパフォーマンスを確保するため、1 つの Site to Site ネットワークに追加できるデバイスは最大 10 台です。

4. ネットワーク名を入力し、**Next** をクリックします。

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing が開始され、どのデバイスを Main Node に設定できるかをテストします。

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    どのデバイスも Main Node に使用できない場合は、以下を確認してください。

    - 少なくとも 1 台のルーターが、静的または動的なパブリックIPを持っていること。
    - ポートが開放されていること。Site to Site のデフォルトポートは 51830 です。ポートを変更して再試行することもできます。
    - Main Node に設定したいルーターが NAT 配下にある場合は、Port Forwarding の設定が必要なことがあります。

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    複数のデバイスを Main Node に設定できる場合は、1 台を選択して続行してください。性能が高く、ネットワーク速度が最も良いルーターを Main Node にすることを推奨します。

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Main Node に設定できるデバイスが 1 台しかない場合は、そのまま Site to Site の詳細ページへ進みます。

6. ネットワークはデフォルトで無効になっています。すべてのノードの LAN IP アドレスが互いに競合していないことを確認してください。必要に応じて歯車アイコンをクリックして LAN IP を変更し、**Start** をクリックします。

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. 数分待ちます。破線が実線に変われば、Site to Site ネットワークが正常に構築されています。

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Site to Site 接続をテストする

1. この Site to Site ネットワーク内のいずれかのノードに PC またはスマートフォンを接続します。

2. Webブラウザーを開き、別のノードの LAN IP にアクセスします。ログインページが表示されれば、その 2 つのノード間の接続は正常に動作しています。

## ルートとその他のオプション

デフォルトでは、各ノードは他のノードの LAN にアクセスできます。セキュリティ上の理由から、特定のサービスに必要な IP アドレスのみを開放することを推奨します。

たとえば、Node 1 のサブネット内に Server A (172.30.97.100) があるとします。他のノードから Node 1 の Service A のみへアクセスさせたい場合は、以下のように設定できます。

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

各ノードの親ルートを追加することもできます。

各 Sub Node は Main Node に対して暗号化されたトンネルネットワークを構築します。トンネルサブネットの IP を変更したい場合は、**IP Address Range** をクリックして変更してください。

**IP Address Range** を変更すると、数分間ネットワークが切断されます。

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
