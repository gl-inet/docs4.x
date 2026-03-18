# GoodCloud Site to Site

## はじめに

GoodCloud Site to Site を使うと、異なる拠点にあるオフィス同士をインターネット経由で安全に接続できます。これにより、会社のネットワークを拡張し、ある拠点のコンピューターリソースを別の拠点の従業員も利用できるようになります。

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenario 1**: 同じ会社の複数の支店を 1 つのプライベートネットワークとして統合し、全拠点でシームレスにリソース共有したい場合。

**Scenario 2**: 密接に連携する 2 社が、共同作業のために安全な共有ネットワーク環境を必要とする場合。

**Scenario 3**: 自宅に IP カメラがあり、外出先からそのデバイスへリモートアクセスしたい場合。

## 条件

1. Site to Site ネットワークの構築には、少なくとも 2 台の GL.iNet ルーターが必要です。

2. 少なくとも 1 台のルーターはパブリックIPアドレスを持ち、Main Node として設定できる必要があります。[ISP がパブリックIPアドレスを割り当てているか確認してください](how_to_check_if_isp_assigns_you_a_public_ip_address.md)。

   Main Node には、性能が高く、ネットワーク速度が最も良いルーターを選ぶことを推奨します。

3. Sub Node 側で VPNクライアント / Tailscale / ZeroTier / AstroWarp を同時に動作させた状態で Site to Site を使うことは推奨されません。ネットワーク構成が非常に複雑になるためです。

## Site to Site ネットワークを構築する

1. ルーターを GoodCloud アカウントへバインドします。[手順はこちら](../interface_guide/cloud.md/#setup-your-goodcloud-account)。

2. [GoodCloud](https://www.goodcloud.xyz/#/login){target="\_blank"} にログインし、左側のサイドバーで **Site to Site** を開きます。右上の **Create Network** をクリックします。

   ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. 左側のチェックボックスをオンにして、少なくとも 2 台のデバイスを選択します。

   ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

   選択したデバイスはページ下部に表示されます。

   Site to Site のデフォルトポートは **51830** です。別のポートを使いたい場合は、左下の **Advanced** をクリックして変更してください。その後 **Next** をクリックします。

   ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

   安定した性能を確保するため、1 つの Site to Site ネットワークに追加できるデバイスは最大 10 台です。

4. ネットワーク名を入力し、**Next** をクリックします。

   ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing が始まり、どのデバイスを Main Node に設定できるかを確認します。

   ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

   どのデバイスも Main Node にできない場合は、以下を確認してください。
   - 少なくとも 1 台のルーターが静的または動的なパブリックIPアドレスを持っていること
   - ポートが開放されていること。Site to Site のデフォルトポートは 51830 です
   - Main Node にしたいルーターが NAT 配下にある場合、Port Forwarding の設定が必要なこと

   ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

   複数のデバイスが Main Node にできる場合は、その中から 1 台を選んで続行してください。性能が高く、ネットワーク速度が最も良いルーターを Main Node に選ぶことを推奨します。

   ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

   Main Node にできるデバイスが 1 台だけの場合は、そのまま Site to Site の詳細ページへ移動します。

6. ネットワークはデフォルトで無効です。すべてのノードで LAN IP アドレスが重複していないことを確認してください。必要に応じて歯車アイコンをクリックして LAN IP を変更し、問題がなければ **Start** をクリックします。

   ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. 数分待ってください。破線が実線に変われば、Site to Site ネットワークの構築は成功です。

   ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Site to Site 接続をテストする

1. この Site to Site ネットワーク内のいずれかのノードに、PC またはスマートフォンを接続します。

2. Webブラウザーで別のノードの LAN IP を開きます。ログインページにアクセスできれば、その 2 つのノード間の接続は正常です。

## ルートとその他のオプション

デフォルトでは、各ノードは他のノードの LAN にアクセスできます。セキュリティ上の理由から、必要なサービスの IP アドレスだけを許可する設定を推奨します。

たとえば、Node 1 のサブネット内に Server A (`172.30.97.100`) があり、他のノードから Node 1 の Service A のみへアクセスさせたい場合は、以下のように設定できます。

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

各ノードには parent route を追加することもできます。

各 Sub Node は Main Node に対して暗号化されたトンネルを構築します。トンネルサブネットの IP を変更したい場合は、**IP Address Range** をクリックして変更してください。

IPアドレス範囲を変更すると、数分間ネットワークが切断されます。

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
