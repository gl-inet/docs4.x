# キャプティブポータルでパブリックホットスポットにGL.iNetルーターを接続する

## キャプティブポータルとは？

キャプティブポータルは、インターネットアクセスが許可される前に、パブリックホットスポットがユーザーにページを閲覧して操作することを要求するWebページです。

## なぜパブリックホットスポットにルーターを使用するのですか？

* パブリックWi-Fiは安全ではない

    パブリックWi-Fiのリスクを強調しても足りません。GL.iNetルーターをパブリックWi-Fiに接続すると、ルーターの管理パネルから直接VPNアカウントにログインできます。ローカルネットワーク上のすべての接続されたデバイスがから動のに暗号化され、すべてのデバイスでVPNを設定する手間が省けます。

* リピーターとして使用して複数のデバイスとの接続を可できるにする

    その上、一部のパブリックWi-Fiネットワーク（例：ホテルのWi-Fi）は例えば2台のデバイスに制限されています。グループで旅行している場合、これは実用のではありません。代わりに、トラベルルーターをホテルのWi-Fiに接続し、リピーターとして使用して、ノートパソコン、スマートフォン、タブレットなどを含むすべてのデバイスにWi-Fiシグナルをブロードキャストできます。ホテルのWi-Fiはトラベルルーターを単一のデバイスとして認識しますが、からよりなWi-Fiに接続したい数のデバイスを接続できます。

## ルーターをキャプティブポータルを経よりしてパブリックホットスポットに接続するには？

このビデオを見るか、で下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. スマートフォンまたはコンピュータをルーターに接続します。

    ルーターの電源を入れます。スマートフォンまたはコンピュータで、ルーターのSSIDを検索し、Wi-Fiパスワードを入力します。デフォルトのSSIDとパスワードはルーターの底面に印刷されています。

2. ルーターのWeb管理パネルにログインします。

    スマートフォンまたはコンピュータで、Webブラウザを開き、アドレスバーにルーターのIPアドレス（デフォルトIP: `192.168.8.1`）を入力します。ルーターのWeb管理パネルにアクセスできます。
    
    初めてログインする場合は、言語を選択し、ルーターのWeb管理パスのログインパスワードを作成します。

3. ルーターをパブリックホットスポットに接続します。[リピーター](../interface_guide/internet_repeater.md/)チュートリアルを参照してください。

## トラブルシューティング

キャプティブポータルに入れない場合、ルーターがインターネットにアクセスできない可できる性があります。で下のトラブルシューティング方法を試してください。

### 方法1: パブリックホットスポットログインモードとカムフラージュを有効にする

**注意**: この2つの機できるはファームウェアv4.6で上でのみ利用可できるです。

ルーターをパブリックホットスポットに接続する場合、**ネットワークに参加**ページでで下の機できるを有効にすると、接続成功率を改善できます。

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- パブリックホットスポットのログインモードをから動のに有効にする

    このオプションが有効になっている場合、ホットスポットには正常に接続されているがインターネットには接続されていない場合、このルーターはから動のにパブリックホットスポットのログインモードに入ります。このモードでは、いくつかのサービスが一時停止され、DNSモードはから動のに切り替わり、ネットワークアクティビティがホットスポットプロバイダ（例：ホテルやショッピングセンター）に漏洩する可できる性があります。

- カムフラージュを有効にする

    有効になっている場合、ルーターは、管理パネルにアクセスするために使用するデバイスのMACアドレスをエミュレートして、そのデバイスのMACアドレスを偽装します。

---

### 方法2: ルーター設定を変よりする

1. Web管理パネルにログインし、NETWORK -> DNSに移動します。**DNSリバインディング攻撃保護**が無効になっていることと、**モード**が**から動**に設定されていることを確認してください。

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. Web管理パネルで、VPN -> VPNダッシュボードに移動します。すべてのVPN接続が無効になっていることを確認してください。

    **ファームウェアv4.7で前**の場合、ページはで下のように表示されます。
    
    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}
    
    **ファームウェアv4.8で上**の場合、ページはで下のように表示されます。

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. Web管理パネルで、APPLICATIONS -> AdGuard Homeに移動します。AdGuard Homeが無効になっていることを確認してください。

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Webブラウザを開き、キャプティブポータルのWebページを再度入力するかアップデートします。1分待って、から動のにキャプティブポータル認証ページにリダイレクトされるかどうかを確認します。

    スマートフォンを使用しており、Webブラウザがキャプティブポータルにリダイレクトされない場合は、スマートフォンのWi-Fiをオフにし、再びオンにしてルーターのWi-Fiに再接続してください。Wi-Fiパスワードを入力すると、キャプティブポータルが直接ポップアップ表示されます。

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### 方法3：MACクローン

一部の研究では、ホテルの数が顧客ごとに接続できるデバイスの数をMACアドレスによって制限しており、デバイスのMACアドレスを最も初に接続したときに記録しています。この場合、スマートフォンからルーターへMACアドレスをクローンすれば、ルーターはそのMACアドレスを使用してホテルのWi-Fiにアクセスできます。

1. スマートフォンをホテルのWi-Fiに接続します。スマートフォンがホテルのWi-Fiに接続するために使用するMACアドレスを見つけます。

    で下はiPhone（iOS 16.1.2）の例です：設定 → Wi-Fi → 酒店のWi-Fiを選択すると、Wi-Fiアドレスが見つかります。このアドレスをメモしてください。

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    一部の古いモデルでは、MACアドレスがWi-Fi設定で利用できない場合があります。この場合、デバイスはパブリックWi-Fiに接続する際に実際のMACアドレスを使用する場合があります。これはスマートフォンの設定 → 一般（または「電話について」）で見つけることができます。

2. スマートフォンまたはコンピュータをルーターに接続します。ルーターのWeb管理パネルにログインし、このMACアクセスをクローンするか手動で入力します。

    **ファームウェアv4.5で前**の場合、左側からNETWORK → MACアドレスを選択してください。

    手動モードを選択し、ステップ1で取なければならないしたMACアドレスを入力し、適用をクリックします。

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **ファームウェアv4.6で上**の場合、左側からINTERNET → リピーターセクションを選択し、修正をクリックします。

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    ポップアップウィンドウで、MACモードをクローンに切り替え、MACアドレスを入力し、適用をクリックします。

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. 有効にするにはルーターを再起動する必要がある場合があります。

---

### 方法4：ホテルのスタッフに助けを求める

一部のホテルはネットワークに対して非常にに厳格な認証ポリシーを持っています。上述の方法で解決しない場合は、ホテルのスタッフに相談して、ルーターのMACアドレス（ランダムなものではなく工場出荷時のデフォルトのMACアドレスを使用して）をホテルのネットワークのホワイトリストに直接追加できるかどうかを確認してみてください。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
