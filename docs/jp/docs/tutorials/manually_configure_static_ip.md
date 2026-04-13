# クライアントデバイスで固定IPを手動設定する方法

=== "Windows 11"

    Windows 11 では、設定アプリから無線および有線アダプターの固定IPアドレス設定を行えます。

    **Wi-Fiアダプターで固定IPアドレスを設定する**

    Wi-Fiアダプターに固定IPアドレス設定を割り当てるには、以下の手順を実行します。

    1. Windows 11 の Settings を開き、Network & Internet -> Wi-Fi タブ -> 現在接続中のネットワーク接続を選択します。

    2. 「IP settings」セクションで Edit ボタンをクリックします。

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. 以下の手順で設定します。

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Manual を選択し、IPv4 のトグルスイッチをオンにします。

        - Windows 11 に固定IPアドレスを設定します。例: 10.1.4.119。

        - サブネットマスクを指定します。例: 255.255.255.0。

        - Default Gateway アドレスを指定します。

        - Preferred DNS アドレスを指定します（必須）。

        - （任意）「Alternate DNS」アドレスを指定します。

        - 「DNS over HTTPS」ドロップダウンメニューで、Preferred DNS と Alternate DNS の両方に対して Off を選択します。必要に応じて、以下のオプションで DoH を有効にすることもできます。

            - Off: すべてのDNSトラフィックを暗号化せず送信します。

            - On (automatic template): すべてのDNSトラフィックを暗号化して送信します。

            - On (manual template): 特定のテンプレートを指定できます。DNSサービスが自動で動作しない場合や、想定どおりに動作するテンプレートがある場合にのみ必要です。

        - 「Fallback to plaintext」トグルスイッチをオフにします（DoHを有効にした場合）。

            - Quick tip: この機能を有効にすると、システムはDNSトラフィックを暗号化しますが、暗号化なしのクエリ送信も許可します。

    4. Save ボタンをクリックします。

        手順が完了すると、固定ネットワーク設定がコンピューターに適用されます。Webブラウザを開いてWebサイトを表示し、新しい設定をテストできます。


    ## **Ethernetアダプターで固定IPアドレスを設定する**

    Windows 11 の Ethernet（有線）アダプターに固定IPアドレスを割り当てるには、以下の手順を実行します。

    1. Settings -> Network & Internet -> Ethernet タブを開きます。

    2. 「IP settings」セクションで Edit ボタンをクリックします。

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. 以下の手順で設定します。

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Manual を選択します。

        - IPv4 のトグルスイッチをオンにします。

        - Windows 11 に固定IPアドレスを設定します。例: 10.1.4.119。

        - サブネットマスクを指定します。例: 255.255.255.0。

        - Default Gateway アドレスを指定します。

        - Preferred DNS アドレスを指定します（必須）。

        - （任意）「Alternate DNS」アドレスを指定します。

        - 「DNS over HTTPS」ドロップダウンメニューで、Preferred DNS と Alternate DNS の両方に対して Off を選択します。必要に応じて、以下のオプションで DoH を有効にできます。

            * Off: すべてのDNSトラフィックを暗号化せず送信します。

            * On (automatic template): すべてのDNSトラフィックを暗号化して送信します。

            * On (manual template): 特定のテンプレートを指定できます。DNSサービスが自動で動作しない場合や、想定どおりに動作するテンプレートがある場合にのみ必要です。

        - 「Fallback to plaintext」トグルスイッチをオフにします（DoHを有効にした場合）。

    4. Save ボタンをクリックします。

        手順が完了したら、WebブラウザでWebサイトを開いて設定をテストできます。


=== "macOS"

    macOSで固定IPアドレスを設定する方法は次のとおりです。

    MacBookを使用している場合は、新しいネットワークロケーションを作成しておくと便利です。これにより、特定のネットワークでのみ固定IPアドレスを使い、他のネットワークでは使わない設定ができます。

    Appleメニューから System Preferences を選択します。

    Network を選択します。以下のようなウィンドウが表示されます。

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    サイドバーから有効なネットワークインターフェースを選択します。この例では無線ネットワークに接続しているため、Wi-Fi を選択します。

    Mac に現在割り当てられているIPアドレスを控えておきます。このあと、表示されているプライベートIPアドレス範囲内から新しいIPアドレスを選ぶ必要があります。詳細は次の手順で説明します。

    Advanced をクリックします。

    TCP/IP を選択します。以下のようなウィンドウが表示されます。

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    Configure IPv4 メニューから Manually を選択します。

    IPv4 Address フィールドに固定IPアドレスを入力します。どの番号を入力すべきでしょうか。一般的には、現在のIPアドレスの末尾だけを変更する方法が簡単です。この例では、192.168.7.0 から 192.168.7.255 の範囲内で、他のデバイスにまだ割り当てられていないアドレスなら使用できます。

    OK -> Apply をクリックします。


=== "Android"

    手順はAndroidのバージョンによって異なります。このドキュメントは Android 11 を基準にしています。

    1. Settings -> Network & Internet -> Wi-Fi と進み、現在接続しているネットワークをタップして設定メニューを開きます。

    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. 固定IPアドレスを設定するには、以下を実行します。

    - 右上の鉛筆アイコンを選択してネットワーク設定にアクセスします。

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Advanced Options を選択します。

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - IP Settings を選択します。

    - 設定を DHCP から Static に変更します。

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - 自宅やその他のプライベートネットワークで固定IPアドレスを使う場合は、以下の標準的なプライベートIPアドレス範囲内から選択してください: 10.0.0.0 ～ 10.255.255.255、172.16.0.0 ～ 172.31.255.255、192.168.0.0 ～ 192.168.255.255

    - ここでIPアドレスを入力します。
        - この手順はネットワークごとに異なります。例: 192.168.1.128

    - Gateway は通常、IPアドレスに基づいて自動入力されます。入力されない場合は、IPアドレスをコピーして末尾の数字を 1 に変更してください。
        - 例: 前の例では 192.168.1.1

    3. Save をタップし、ネットワークが再接続されるのを待ちます。

=== "iOS"

    自宅やその他のプライベートネットワークで固定IPアドレスを使う場合は、以下の標準的なプライベートIPアドレス範囲内から選択してください。

    10.0.0.0 ～ 10.255.255.255
    172.16.0.0 ～ 172.31.255.255
    192.168.0.0 ～ 192.168.255.255

    固定IPアドレスを設定するには、以下を実行します。

    - Settings アイコンをタップします。

    - Wi-Fi に移動します。

    - Wi-Fiネットワーク名の横にある青い情報アイコン (i) をタップします。
         - iOS 7 より古いバージョンでは、青いエラーアイコンの場合があります。

    - 以下のように Static タブへ移動します。


    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - IP Address フィールドをタップします。

    - iPhone/iPad で使用したい固定IPアドレスを入力します。

    - Router フィールドをタップします。

    - ルーターのIPアドレスを入力します。

    - Subnet Mask をタップして情報を入力します。

        - 通常は 225.225.0.0 です。

    - 画面左上の Wi-Fi ボタンをタップして設定を保存します。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
