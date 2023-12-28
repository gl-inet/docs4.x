# ウェブ管理パネルにアクセスできない

[http://192.168.8.1](http://192.168.8.1)にアクセスして Web 管理パネルにログインできない場合があります。いくつかの理由が考えられます。

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

* パソコンや携帯電話がルーターに接続していません。
* 192.168.8.1 はルーターのデフォルトの IP アドレスですが、この IP は変更されている可能性があります。
* ブラウザのキャッシュや拡張機能によりアクセスできない場合があります。
* LAN トラフィックを処理する VPN クライアントを使用しています。
* ルーターがレンガ化しました。

この問題を解決するには、手順に従ってください。

1. [接続をチェックする](#check_the_connection)
2. [ルーターのIPアドレスを確認する](#check-routers-ip-address)
3. [ルーターのIPアドレスにアクセスする](#access-the-routers-ip-address)

または、[アプリ]を使ってルーターにアクセスすることもできます。

---

## 接続をチェックする

イーサネットケーブルで接続している場合は、WAN/LANポートの接続が正しいことを確認してください。WANポートはインターネットソースに接続され、LANポートはデバイスに接続されています。

Wi-Fiで接続している場合は、SSIDが正しいことを確認してください。

## ルーターのIPアドレスを確認する

次に、以下の手順に従ってルーターのIPアドレスを確認します。

=== "Windows 10 / Windows 11"

    コントロールパネルにアクセスし、右上隅が大きなアイコンまたは小さなアイコンで表示されていることを確認してください。

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    コントロールパネル ->ネットワークと共有センター -> 接続をクリックします。 複数の接続がある場合は、確認したいルーターの対応する接続を選択してください。

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    接続のステータスを示すダイアログがポップアップ表示されます。 詳細ボタンをクリックします。

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    ネットワーク接続の詳細を示すダイアログが表示されます。ルーターの IP アドレスは **IPv4 デフォルト ゲートウェイ**です。

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    コントロールパネル -> ネットワークとインターネット -> ネットワークと共有センター-> アダプター設定を変更する

    ネットワークを右クリック -> ステータス-> 詳細
    
    ルーターのIPアドレスは、**IPv4デフォルトゲートウェイ**です。
    
    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. システム環境設定 -> ネットワーク

    2. 左側の列で、ネットワーク接続をクリックします。 イーサネット接続の場合、ルーターの IP アドレスが表示されます。

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Wi-Fi 接続の場合は、[詳細...] ボタンをクリックし、ウィンドウの上部にある [TCP/IP] タブをクリックします。 ルーターのIPアドレスが表示されます。

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. 設定 -> Wi-Fi
    2. 現在接続しているWi-Fiの情報アイコン（丸の中に青いi）をタップします。ルーターのIPアドレスが表示されます。

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    これはアンドロイドデバイスによって異なります。

    1. 設定 -> ネットワークとインターネット
    2. Wi-Fiをタブし、接続しているネットワークを見つけ、設定アイコンをクリックして設定を管理します。
    3. 詳細設定のドロップダウンをタップします。静的IPまたは動的IPのオプションが表示されたら、静的IPを選択します。
    4. いずれの場合でも、ゲートウェイの下にルーターの IP が表示されるはずです。

## ルーターのIPアドレスにアクセスする

1. Chrome/Edge/Safariを使用していることを確認し、再度IPアドレスにアクセスしてみてください。
2. ブラウザのキャッシュや拡張機能による問題を避けるため、シークレットウィンドウを開いてください。その後、再度ルーターのIPアドレスにアクセスしてみてください。
3. VPN を使用している場合は、VPN をオフにしてからもう一度お試しください。
4. 携帯電話をご利用の場合は、モバイルデータ通信をオフにしてください。 一部の携帯電話では、ルーターがインターネットにアクセスできない場合、WiFi の代わりにモバイル データを使用します。
5. 上記の手順が失敗した場合は、 [リセット](repair_network_or_reset_firmware.md#reset-to-factory)を試して工場出荷時の状態に戻してください。
6. リセットが機能しない場合は、 [uboot経由でデブリック](debrick.md)を試してください。
