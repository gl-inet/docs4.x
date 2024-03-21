# ドロップインゲートウェイ

この機能を使用するには、v4.2.x にアップグレードしてください。

Web 管理パネルの左側 -> ネットワーク -> ドロップイン ゲートウェイ

## 使用シナリオ

メインのルーターを交換したくないユーザーは、このモードを使用してメインのルーターの機能を拡張することができます。

* ADGuard Homeを使用して広告をフィルタリングします。
* 暗号化DNSを使用します。
* VPNクライアントを使用します。
* 大容量メモリを搭載したより強力なルーター（GL-MT2500など）を使用し、他のトラフィック転送および制御ツールを自分でインストールすることをお勧めします。

## ネットワークトポロジー

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

上の図には、灰色の線、緑の線があり、緑の線には3つの矢印があり、それぞれの矢印の横には数字が書かれている。

1. 灰色の線は、デバイスがメインルーターに接続され、メインルーターのLANポートがイーサネットケーブルでドロップインゲートウェイ機能付きGL.iNetルーターのWANポートに接続されていることを示しています。

2. 緑色の線は、ドロップイン・ゲートウェイ・モードが有効な場合、メイン・ルーターを経由して送信される前に、デバイスのデータの全部または一部がGL.iNetデバイスで処理されることを示しています。

## セットアップ

すべてのデバイスをDrop-in Gatewayで管理する場合と、一部のデバイスのみを管理する場合の2つの使用シナリオがあります。

以下に言及するGL.iNetルーターは、ドロップインゲートウェイ機能を有効にしたいGL.iNetルーターです。ここでのメインルーターのルーターIPアドレスは192.168.1.1です。

### ドロップインゲートウェイが管理するすべてのデバイス

1. メインルーターのLANポートとGL.iNetルーターのWANポートはイーサネットケーブルで接続します。

2. GL.iNetルーターのウェブ管理パネルにアクセスし、ドロップインゲートウェイ機能を有効にします。設定が自動的に作成されます。

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

     **IP アドレス**は [インターネット ページのイーサネット セクター](internet_ethernet.md)の IP アドレスと同じです。**ゲートウェイ** と **DNS サーバー 1** は、メイン ルーターの IP アドレスです。 これらの項目が正しく設定されていない場合は、自分で手動で変更できます。

    ここに IP アドレスを書き留めます。次の手順で使用します。

    最初の設定方法を選択し、適用をクリックします。

3. メインルーターの管理ページにログインします。

    ??? "GL.iNet"

        メインルーターのブランドがGL.iNetで、バージョンがv4.2以上の場合。

        管理画面-> NETWORK -> LAN -> DHCPサーバー -> 詳細設定にアクセスします。

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        ステップ2のIPアドレスとしてDHCPゲートウェイを記入します。 etc. `192.168.116.23`、そして**Apply**をクリックしてください。

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        メインルーターのブランドがTP-Linkの場合: 以下は TP-LINK Archer C3150 の例です。

        TP-Link の管理ページにアクセスします。 **詳細** -> **ネットワーク** -> **DHCP サーバー** のタブで、**DHCP** を無効にします。

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        そして**保存**をクリックします。

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        メインルーターのブランドがLinksysの場合：Linksys WHW01の例です。

        Linksysの管理ページにアクセスします。

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        **ローカル ネットワーク**タブで、**DHCP サーバー**を無効にして、**OK** をクリックします。

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        警告が表示されます。**OK** をクリックします。

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "その他"

        DHCPを無効にする方法については、該当するブランドを検索するか、カスタマーサービスにご相談ください。

4. GL.iNetルーターに戻り、 [ADGuard Home](adguardhome.md)、[encypted DNS](dns.md)、[WireGaurd Client](wireguard_client.md) 、[OpenVPN Client](openvpn_client.md)などの機能を設定します。

### ドロップイン ゲートウェイによって管理される一部のデバイス

1. メインルーターのLANポートとGL.iNetルーターのWANポートはイーサネットケーブルで接続します。

2. GL.iNetルーターのウェブ管理パネルにアクセスし、ドロップインゲートウェイ機能を有効にします。設定が自動的に作成されます。

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    **IPアドレス**は、 [インターネットページのイーサネットセクター](internet_ethernet.md)のIPアドレスと同じです。 **ゲートウェイ**と**DNSサーバー1**はメインルーターのIPアドレスです。これらの項目が正しく設定されていない場合は、ご自身で手動で変更してください。

    ここに IP アドレスを書き留めます。IPアドレスは次のステップで使用します。

    2番目の設定方法を選択し、適用をクリックします。

3. ドロップインゲートウェイ機能を使用するデバイスのゲートウェイとDNSを、ドロップインゲートウェイページのIPアドレスに設定します。

    ??? "Windows"

        以下はWindows 11の例ですが、Windows 10も同様です。PCがメインルーターに接続されていることを確認してください。ここでは、PCがネットワークケーブルでメインルーターに接続されていることを想定しています。WiFiで接続する場合も、セットアップは同様です。

        1. 設定を開きます。

        2. **Network & Internet**をクリックしてください。

        3. **Ethernet** タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. このPCのIPアドレスが表示されます。IP割り当て "セクションで、**編集**ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. **Manual**オプションを選択します。**IPv4トグル**スイッチをオンにします。

        6. **IPアドレス**をステップdのIPアドレスに設定し、**サブネットマスク**を`255.255.255.0`に設定、**ゲートウェイ**と**優先DNS**の両方をドロップインゲートウェイページのIPアドレスに設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. **保存**ボタンをクリックします。

    ??? "Android"

        以下はSamsung S21の例です。スマートフォンがメインルーターに接続されていることを確認してください。

        1. 設定を開き、接続をクリックします。

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Wi-Fiをクリックします。

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. 現在のSSIDのコグアイコンをクリックします。

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. **もっと見る**をクリックしてください。

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. **IP構成**をクリックし、**スタティック**を選択します。

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. ドロップイン・ゲートウェイのページで**ゲートウェイ**と**DNS 1**をIPアドレスに設定し、**保存**をクリックします。

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        以下はiPhone 8のiOS 16.3の例です。スマートフォンがメインルーターに接続されていることを確認してください。

        1. 設定を開き、Wi-Fiをクリックします。

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. SSIDをクリックします。

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. 下にスクロールすると、**IP構成**が**自動**になっています。**IPアドレス**とサブネットマスク**を書き留めてください。次のステップで必要になります。

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. **IP構成**を**手動**に変更し、**IPアドレス**と**サブネットマスク**を前のステップと同じように設定し、**ルーター**をドロップインゲートウェイページのIPアドレスとして設定し、**保存**をクリックします。

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. **DNS 構成**をクリックし、**手動**に変更します。サーバーを追加**をクリックし、ドロップインゲートウェイページのIPアドレスとしてサーバーIPアドレスを設定し、**保存**をクリックします。

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. GL.iNet ルーターに戻り、 [ADGuard Home](adguardhome.md)、[encypted DNS](dns.md)、 [WireGaurd Client](wireguard_client.md) 、 [OpenVPN Client](openvpn_client.md)などの機能を設定します。

## 注意事項

1. このモードを使用すると、レイテンシーが増加します。
2. このモードを有効にすると、LAN内の選択したデバイス間で転送されるデータもドロップインゲートウェイを経由するため、メインルーターとドロップインゲートウェイ間の帯域幅がLAN全体の帯域幅に影響します。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
