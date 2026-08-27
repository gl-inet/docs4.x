# ウェブ管理パネルにアクセスできない

[http://192.168.8.1](http://192.168.8.1) にアクセスして Web 管理パネルにログインできない場合があります。いくつかの理由が考えられます。

![can't access admin](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## 考えられる原因

* パソコンや携帯電話がルーターに接続していません。
* `192.168.8.1` はルーターのデフォルトの IP アドレスですが、変更されている可能性があります。
* ブラウザのキャッシュや拡張機能により管理パネルにアクセスできない場合があります。
* VPN またはプロキシソフトウェアがトラフィックを処理しているため、管理パネルにアクセスできない場合があります。
* ルーターがレンガ化（ブリック）しています。

## ウェブ管理パネルにアクセスする一般的な手順

1. デバイスを何も接続せずにルーターの電源を入れます。
2. モバイル/ノートパソコンをルーターの Wi-Fi に接続し、ルーターのラベルに印刷されている Wi-Fi キーを入力します。
3. 手順 2 が失敗した場合は、コンピューター/ノートパソコンの Wi-Fi をオフにします。代わりにイーサネットケーブルでルーターの LAN ポートに接続します。
4. ブラウザを開き、アドレスバーに `192.168.8.1` と入力して Enter キーを押します。GL.iNet のウェブ管理パネルが表示されるはずです。

または、[アプリ](mobile_app.md)を使ってルーターにアクセスすることもできます。

## その他の解決手順

1. [接続をチェックする](#check-the-connection)
2. [ルーターのIPアドレスを確認する](#check-routers-ip-address)
3. [ルーターのIPアドレスにアクセスする](#access-the-routers-ip-address)

---

### 接続をチェックする {#check-the-connection}

イーサネットケーブルで接続している場合は、ルーターの WAN/LAN ポートの接続が正しいことを確認してください。

- WAN ポートは、モデムやプライマリルーターなどのインターネットソースに接続されています。
- LAN ポートは、ノートパソコンなどの端末デバイスに接続されています。

Wi-Fi で接続している場合は、使用しているデバイスで正しい SSID を選択し、正しいパスワードを入力していることを確認してください。

### ルーターのIPアドレスを確認する {#check-routers-ip-address}

=== "Windows 10 / Windows 11"

    コントロールパネルにアクセスし、右上隅が大きなアイコンまたは小さなアイコンで表示されていることを確認してください。

    ![control panel](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/control_panel_view_by.png){class="glboxshadow"}

    コントロールパネル ->ネットワークと共有センター -> 接続をクリックします。 複数の接続がある場合は、確認したいルーターの対応する接続を選択してください。

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    接続のステータスを示すダイアログがポップアップ表示されます。 詳細ボタンをクリックします。

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    ネットワーク接続の詳細を示すダイアログが表示されます。ルーターの IP アドレスは **IPv4 デフォルト ゲートウェイ**です。

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    コントロールパネル -> ネットワークとインターネット -> ネットワークと共有センター-> アダプター設定を変更する

    ネットワークを右クリック -> ステータス-> 詳細
    
    ルーターのIPアドレスは、**IPv4デフォルトゲートウェイ**です
    
    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. システム環境設定 -> ネットワーク

    2. 左側の列で、ネットワーク接続をクリックします。 イーサネット接続の場合、ルーターの IP アドレスが表示されます。

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Wi-Fi 接続の場合は、[詳細...] ボタンをクリックし、ウィンドウの上部にある [TCP/IP] タブをクリックします。 ルーターのIPアドレスが表示されます。

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. 設定 -> Wi-Fi
    2. 現に接続しているWi-Fiの情報アイコン（丸の中に青いi）をタップします。ルーターのIPアドレスが表示されます。

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    これはアンドロイドデバイスによって異なります。

    1. 設定 -> ネットワークとインターネット
    2. Wi-Fiをタブし、接続しているネットワークを見つけ、設定アイコンをクリックして設定を管理します。
    3. 詳細設定のドロップダウンをタップします。静的IPまたは動的IPのオプションが表示されたら、静的IPを選択します。
    4. いずれの場合でも、ゲートウェイの下にルーターの IP が表示されるはずです。

### ルーターのIPアドレスにアクセスする {#access-the-routers-ip-address}

1. 互換性を高めるために、ルーターの管理パネルには Chrome / Edge / Safari を使用してください。

2. ブラウザのキャッシュや拡張機能による問題を避けるため、シークレットウィンドウを開いてから、再度ルーターのIPアドレスにアクセスしてください。

3. TailscaleやZeroTierを含むすべてのVPNまたはプロキシソフトウェアを無効にしてください。

4. 携帯電話を使用している場合は、モバイルデータをオフにしてください。

    一部のスマートフォンは、ルーターがインターネットに接続されていないことを検出すると、ルーターのWi-Fiを切断し、代わりにモバイルデータを使用します。ルーターから切断されると、ウェブ管理パネルにアクセスできなくなります。

5. 上記の手順で解決しない場合は、ルーターを[リセット](repair_network_or_reset_firmware.md#reset-to-factory)して工場出荷時の状態に戻してください。

6. リセットが機能しない場合は、[U-Boot経由でデブリック](debrick.md)を試してください。

---

それでも質問がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} にアクセスするか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} ください。
