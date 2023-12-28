# キャプティブ・ポータルでホットスポットに接続する

## キャプティブ・ポータルとは？

キャプティブ ポータルは、インターネットアクセスが許可される前に、パブリック ホットスポットがユーザーに閲覧および操作することを義務付けられている Web ページです。

## パブリック ホットスポットに接続するためにルーターを使用する必要があるのはなぜですか?

* パブリックWi-Fiは安全ではありません 

    パブリックWi-Fiがいかに安全でないかは、いくら強調してもしきれません。GL.iNetルーターを公衆無線LANに接続すれば、ルーターの管理パネルから直接VPNアカウントにログインするだけで、ローカルネットワーク内で接続された全てのデバイスが自動的に暗号化され、全てのデバイスにVPNを設定する手間が省けます。

* リピーターとして使用し、複数のデバイスと接続可能

    その上、ホテルの無料Wi-FiなどパブリックWi-Fiの中には、例えば2台のデバイスに制限されている場合もあります。グループで旅行している場合、それではうまくいきません。その代わりに、トラベルルーターをホテルのWi-Fiに接続し、ホットスポットとして使用して、ノートパソコン、スマートフォン、タブレットなど、すべてのデバイスにWi-Fiをブロードキャストすることができます。ホテルのWi-Fiはトラベルルーターを1台のデバイスとしてしか認識しないが、何台でも無料Wi-Fiを楽しむことができます。

## ルーターをキャプティブポータル経由でパブリックホットスポットに接続するには？

1. スマートフォンまたはコンピューターをルーターに接続します。

    ルーターの電源を入れます。 スマートフォンまたはコンピュータで、SSID を検索して WiFi をトラベル ルーターに接続し、WiFi パスワードを入力します。 デフォルトのパスワードは、ルーターの底部に「WIFI キー」として表示されます。

2. トラベル ルーターの Web 管理パネルにアクセスします。

    ルーターへの接続に成功したら、インターネットブラウザでルーターのIPアドレス（デフォルトは`192.168.8.1`）にアクセスして、ルーターのウェブ管理パネルにアクセスします。初めてログインする場合は、言語を選択し、ルータのWeb管理パネルの新しいパスワードを作成します。

3. [リピーター](../interface_guide/internet_repeater.md/) 機能を使用して、ルーターをパブリックホットスポットのSSIDに接続します。

4. ホテルのキャプティブ・ポータルに必要事項を記入する。

## トラブルシューティング

ただし、キャプティブ ポータルに入ることができないため、ホットスポットに接続したり、インターネットにアクセスしたりできない場合があります。 この場合は、次の解決策を 1 つずつ試してください。

---

### 解決策 1: DNS 設定を変更する

1. Web 管理パネル -> ネットワーク -> DNS に移動します。 次に、**DNS 再バインディング攻撃保護** が無効になっていて、**モード** が **自動** であることを確認します。

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="580"}

2. Web 管理パネル -> VPN -> VPN ダッシュボードに移動します。 OpenVPN と WireGuard クライアントの接続が無効になっていることを確認してください。

    ![vpn client is disable](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="572"}

3. Web 管理パネル -> アプリケーション -> AdGuard Homeに移動します。 AdGuard Homeが停止していることを確認してください。

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Web ブラウザを使用して Web ページにアクセスすると、ホットスポットのキャプティブ ポータルに自動的にリダイレクトされます。

    スマートフォンを使用しているが、Web ブラウザがキャプティブ ポータルにリダイレクトされない場合、スマートフォンのWi-Fiを一度OFFにし、再度ONにしてルーターのWi-Fiに接続し直してください。 Wi-Fi パスワードを入力すると、キャプティブ ポータルが直接ポップアップ表示されます。

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### 解決策 2：MAC クローン

[解決策 1](#solution-1-change-dns-settings)だけではこの問題を解決できない場合があります。 一部のホテルでは、各顧客がアクセスできるデバイスの数を MAC アドレスによって制限しており、初めてホテルの WiFi にアクセスしたときに携帯電話 (またはその他のデバイス) の MAC アドレスを記録します。 この場合、携帯電話がホテルの WiFi に接続するために使用する MAC アドレスをルーターにクローンする必要があります。

1. スマートフォンをネットワークに登録します。

2. お使いのスマートフォンがホテルのWiFiに接続されていることを確認します。あなたのスマホがホテルのWiFiに接続するために使用しているMACアドレスを確認します。以下はiPhone（iOS 16.1.2）の例です。設定→Wi-Fi→ホテルのWiFiを選択してください。Wi-Fiアドレスが表示されるので、このアドレスをメモします。

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    一部の古い携帯電話では、WiFiでMACアドレスが見つからない場合、携帯電話の本当のMACアドレスを使用します。これは携帯電話の**設定** -> **About**にあり、そこで携帯電話のMACアドレスを見つけることができます。

3. 携帯電話またはパソコンを使ってルーターに接続し、ウェブ管理パネルにアクセスします。ウェブ管理パネルの左側にある「ネットワーク」→「MACアドレス」を選択します。

    手動モードを選択し、ステップ2でメモしたMACアドレスを入力ボックスに記入し、[適用]をクリックします。

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

4. 有効にするには、ルーターを再起動する必要があるかもしれません。

---

### 解決策3：ホテルのスタッフに助けを求める

ホテルのネットワークによっては、非常に厳格な認証ポリシーを持っている場合があります。解決策1でも2でもうまくいかない場合は、ルーターのMACアドレス（工場出荷時のデフォルトのもの）を直接「ホワイトリスト」に追加できるかどうか、ホテルのスタッフに相談してみてください。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
