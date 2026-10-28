# キャプティブポータルでパブリックホットスポットにGL.iNetルーターを接続する {#connect-a-glinet-router-to-public-hotspots-with-a-captive-portal}

## キャプティブポータルとは？ {#what-is-a-captive-portal}

キャプティブポータルとは、パブリックホットスポットにおいて、インターネットへのアクセスが許可される前にユーザーが閲覧・操作する必要があるWebページです。

## パブリックホットスポットでルーターを使用する理由 {#why-use-a-router-for-public-hotspots}

* パブリックWi-Fiは安全ではない

    パブリックWi-Fiのリスクは、いくら強調してもしすぎることはありません。GL.iNetルーターをパブリックWi-Fiに接続すると、ルーターの管理パネルから直接VPNアカウントにログインできます。ルーターがすべてのローカルトラフィックをVPN経由で送信するように設定されている場合、接続されたデバイスの通信がVPN経由で暗号化されるため、デバイスごとにVPNを設定する手間が省けます。

* リピーターとして使用し、複数のデバイスを接続できる

    また、一部のパブリックWi-Fi（ホテルのWi-Fiなど）では、接続できるデバイスが2台までなどに制限されています。グループで旅行する場合、これでは不便です。代わりに、トラベルルーターをホテルのWi-Fiに接続してリピーターとして使用すれば、ノートパソコン、スマートフォン、タブレットなど、すべてのデバイスにWi-Fiを提供できます。ホテルのWi-Fiはトラベルルーターを1台のデバイスとして認識します。トラベルルーターには、最大クライアント数の範囲内で複数のデバイスを接続できます。

## キャプティブポータルのあるパブリックホットスポットにルーターを接続するには？ {#how-to-connect-router-to-public-hotspots-with-captive-portal}

このビデオを見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. スマートフォンまたはコンピュータをルーターに接続します。

    ルーターの電源を入れます。スマートフォンまたはコンピュータで、ルーターのSSIDを検索し、Wi-Fiパスワードを入力します。デフォルトのSSIDとパスワードはルーターの底面に印刷されています。

2. ルーターのWeb管理パネルにログインします。

    スマートフォンまたはコンピュータで、Webブラウザを開き、アドレスバーにルーターのIPアドレス（デフォルトIP: `192.168.8.1`）を入力します。ルーターのWeb管理パネルにアクセスできます。
    
    初めてログインする場合は、言語を選択し、ルーターのWeb管理パネルのログインパスワードを設定します。

3. ルーターをパブリックホットスポットに接続します。[リピーター](../interface_guide/internet_repeater.md/)チュートリアルを参照してください。

## トラブルシューティング {#troubleshooting}

キャプティブポータルに入れない場合、ルーターがインターネットにアクセスできない可能性があります。以下のトラブルシューティング方法を試してください。

### 方法1: パブリックホットスポットログインモードとカムフラージュを有効にする {#method-1-enable-public-hotspot-login-mode-camouflage}

**注意**: この2つの機能は、ファームウェアv4.6以降でのみ利用できます。

ルーターをパブリックホットスポットに接続する際に、**Join Network** ページで以下の機能を有効にすると、接続の成功率を高めることができます。

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    このオプションを有効にすると、ルーターがホットスポットには接続できたもののインターネットに接続できない場合に、自動的にパブリックホットスポットのログインモードに入ります。このモードでは一部のサービスが一時停止され、DNSモードが自動に切り替わるため、ネットワーク上のアクティビティがホットスポットの提供者（ホテルやショッピングモールなど）に漏れる可能性があります。

- Enable Camouflage

    有効にすると、ルーターは管理パネルへのアクセスに使用しているクライアントデバイスのMACアドレスをエミュレートし、そのデバイスになりすまします。

---

### 方法2: ルーター設定を変更する {#method-2-change-router-settings}

1. Web管理パネルにログインし、NETWORK -> DNSに移動します。**DNS Rebinding Attack Protection** が無効になっていること、および **Mode** が **Automatic** に設定されていることを確認してください。

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. Web管理パネルで、VPN -> VPN Dashboardに移動します。すべてのVPN接続が無効になっていることを確認してください。

    **ファームウェアv4.7以前**の場合、ページは以下のように表示されます。
    
    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}
    
    **ファームウェアv4.8以上**の場合、ページは以下のように表示されます。

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. Web管理パネルで、APPLICATIONS -> AdGuard Homeに移動します。AdGuard Homeが無効になっていることを確認してください。

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Webブラウザを開き、キャプティブポータルのWebページを再度開くか再読み込みします。1分ほど待ち、キャプティブポータルの認証ページに自動的にリダイレクトされるかどうかを確認します。

    スマートフォンを使用しており、Webブラウザがキャプティブポータルにリダイレクトされない場合は、スマートフォンのWi-Fiをオフにし、再びオンにしてルーターのWi-Fiに再接続してください。Wi-Fiパスワードを入力すると、キャプティブポータルが直接ポップアップ表示されます。

    ![connected](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### 方法3：MACクローン {#method-3mac-clone}

一部のホテルでは、MACアドレスを識別することで、宿泊客1人あたりがホテルのWi-Fiに接続できるデバイス数を制限しており、デバイスが初めて接続したときにそのMACアドレスを記録します。この場合、スマートフォンがホテルのWi-Fiへの接続に使用しているMACアドレスをルーターにクローンすると、ルーターはそのMACアドレスを使用してホテルのWi-Fiにアクセスできます。

1. スマートフォンをホテルのWi-Fiに接続します。スマートフォンがホテルのWi-Fiに接続するために使用するMACアドレスを見つけます。

    以下はiPhone（iOS 16.1.2）の例です：設定 -> Wi-Fi -> ホテルのWi-Fiを選択すると、「Wi-Fiアドレス」が表示されます。このアドレスをメモしてください。

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    一部の古い機種では、Wi-Fi設定にMACアドレスが表示されない場合があります。その場合、デバイスはパブリックWi-Fiへの接続時に実際のMACアドレスを使用している可能性があります。実際のMACアドレスは、スマートフォンの 設定 > 情報（または「端末情報」）で確認できます。

2. スマートフォンまたはコンピュータをルーターに接続します。ルーターのWeb管理パネルにログインし、このMACアドレスをクローンするか手動で入力します。

    **ファームウェアv4.5以前**の場合は、左側のメニューから NETWORK -> MAC Address を選択します。

    Manual Mode を選択し、手順1で取得したMACアドレスを入力して Apply をクリックします。

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **ファームウェアv4.6以降**の場合は、左側のメニューから INTERNET を選択し、Repeater セクションで Modify をクリックします。

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    ポップアップウィンドウで MAC Mode を Clone に切り替え、MACアドレスを手動で入力して Apply をクリックします。

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. 設定を反映するには、ルーターの再起動が必要な場合があります。

---

### 方法4：ホテルのスタッフに助けを求める {#method-4seek-help-from-hotel-staff}

一部のホテルでは、ネットワークに非常に厳格な認証ポリシーを設けています。上記のいずれの方法でも解決しない場合は、ルーターのMACアドレス（ランダムなMACアドレスではなく、工場出荷時のデフォルトMACアドレス）をホテルのネットワークのホワイトリストに直接追加してもらえるよう、ホテルのスタッフに依頼してみてください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
