# 静的IPを手動で設定する方法

=== "Windows 11"

    Windows 11では、無線および有線アダプターに対して設定アプリから静的IPアドレスを設定できます。

    **Wi-Fiアダプターに静的IPアドレスを設定する**

    Wi-Fiアダプターに静的IPアドレスを設定するには、以下の手順に従ってください：

    1. Windows 11の設定を開く -> ネットワークとインターネット -> Wi-Fiタブ -> 現在のネットワーク接続を選択します。

    2. 「IP設定」セクションの下にある「編集」ボタンをクリックします。

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. 以下の手順に従って設定を行います：

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - 手動オプションを選択し、IPv4トグルスイッチをオンにします。

        - Windows 11用に静的IPアドレスを設定します - 例：10.1.4.119。

        - サブネットマスクを指定します - 例：255.255.255.0。

        - デフォルトゲートウェイアドレスを指定します。

        - 優先DNSアドレスを指定します（必須）。

        - （オプション）「代替DNS」アドレスを指定します。

        - 「DNS over HTTPS」ドロップダウンメニューを使用して、優先および代替アドレスのオフオプションを選択しますが、以下のオプションでDoHを有効にすることもできます：

            - オフ：すべてのDNSトラフィックを暗号化せずに送信します。

            - オン（自動テンプレート）：すべてのDNSトラフィックを暗号化して送信します。

            - オン（手動テンプレート）：特定のテンプレートを指定できます。DNSサービスが自動的に機能しない場合や、期待通りに機能するテンプレートがある場合にのみ必要です。

        - 「プレーンテキストへのフォールバック」トグルスイッチをオフにします（DoHを有効にする場合）。

            - クイックヒント：この機能を有効にすると、システムはDNSトラフィックを暗号化しますが、暗号化なしでクエリを送信することを許可します。

    4. 「保存」ボタンをクリックします。

        手順を完了すると、コンピューターに静的ネットワーク設定が適用されます。ウェブブラウザを開いてウェブサイトを読み込むことで、新しい設定をテストできます。


    **イーサネットアダプターに静的IPアドレスを設定する**

    Windows 11でイーサネット（有線）アダプターに静的IPアドレスを設定するには、以下の手順に従ってください：

    1. 設定を開く -> ネットワークとインターネット -> イーサネットタブ。

    2. 「IP設定」セクションの下にある「編集」ボタンをクリックします。

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. 以下の手順に従って設定を行います：

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}
        
        - 手動オプションを選択します。

        - IPv4トグルスイッチをオンにします。

        - Windows 11用に静的IPアドレスを設定します - 例：10.1.4.119。

        - サブネットマスクを指定します - 例：255.255.255.0。

        - デフォルトゲートウェイアドレスを指定します。

        - 優先DNSアドレスを指定します（必須）。

        - （オプション）「代替DNS」アドレスを指定します。

        - 「DNS over HTTPS」ドロップダウンメニューを使用して、優先および代替アドレスのオフオプションを選択しますが、以下のオプションでDoHを有効にすることもできます：

            * オフ：すべてのDNSトラフィックを暗号化せずに送信します。

            * オン（自動テンプレート）：すべてのDNSトラフィックを暗号化して送信します。

            * オン（手動テンプレート）：特定のテンプレートを指定できます。DNSサービスが自動的に機能しない場合や、期待通りに機能するテンプレートがある場合にのみ必要です。
            
        - 「プレーンテキストへのフォールバック」トグルスイッチをオフにします（DoHを有効にする場合）。

    4. 「保存」ボタンをクリックします。

        手順を完了すると、ウェブブラウザを使ってウェブサイトを開くことで設定をテストできます。

=== "macOS"

    macOSで静的IPアドレスを設定する方法は以下の通りです：

    MacBookを所有している場合、新しいネットワークロケーションを作成することをお勧めします。これにより、特定のネットワークに対して静的IPアドレスを使用し、他のネットワークに対しては使用しないようにすることができます。
    
     Appleメニューから「システム環境設定」を選択します。

    「ネットワーク」を選択します。以下のウィンドウが表示されます。

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    サイドバーからアクティブなネットワークインターフェイスを選択します。この例では、無線ネットワークに接続しているので、Wi-Fiを選択します。

    Macに割り当てられている現在のIPアドレスをメモしておきます。次に、新しいIPアドレスをプライベートIPアドレス範囲から選択する必要があります。それについては後ほど説明します。

    「詳細」をクリックします。

    「TCP/IP」を選択します。以下のウィンドウが表示されます。
    
    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    「IPv4の設定」メニューから「手動」を選択します。

    「IPv4アドレス」フィールドに静的IPアドレスを入力します。どの番号を入力すればよいでしょうか？一つの方法は、現在のIPアドレスの最後の部分を変更することです。この例では、192.168.7.0から192.168.7.255の範囲内で、他のデバイスに割り当てられていないアドレスを選択します。

    「OK」をクリック -> 「適用」をクリックします。
   
=== "Android"

     手順はAndroidのバージョンによって異なります。このドキュメントはAndroidバージョン11に基づいています。

    1. 設定に移動 -> 「ネットワークとインターネット」を選択し、次に「Wi-Fi」を選択 -> 現在接続されているネットワークをタップして設定メニューを開きます。
    
    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. 静的IPアドレスを設定するには、以下の手順に従います：

    - 右上の鉛筆アイコンを選択してネットワーク設定にアクセスします。
        
        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - 「詳細オプション」を選択します。
        
        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - 「IP設定」を選択します。
        
    - 設定を「DHCP」から「静的」に変更します。
        
        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

  - ホームやその他のプライベートネットワークで静的IPアドレスを使用する場合、以下の標準プライベートIPアドレス範囲内から選択する必要があります：10.0.0.0 から 10.255.255.255、172.16.0.0 から 172.31.255.255、192.168.0.0 から 192.168.255.255

    - IPアドレスを入力します。
        - このステップは各ネットワークに特有です。例：192.168.1.128
        
    - IPアドレスに基づいてゲートウェイが自動的に入力されるはずです。されない場合は、IPアドレスをコピーして最後の数字を1に置き換えます。
        - 例：前述の例に基づく場合：192.168.1.1

    3. 保存をタップし、ネットワークが再接続するのを待ちます。

=== "iOS"

    ホームやその他のプライベートネットワークで静的IPアドレスを使用する場合、以下の標準プライベートIPアドレス範囲内から選択する必要があります：

    10.0.0.0 から 10.255.255.255
    172.16.0.0 から 172.31.255.255
    192.168.0.0 から 192.168.255.255

    静的IPアドレスを設定するには、以下の手順に従います：

    - 設定アイコンをタップします。

    - Wi-Fiに移動します。

    - Wi-Fiネットワーク名の横にある青い情報アイコン (i) をタップします。
         - iOS 7より古いバージョンを使用している場合は青いエラーになるかもしれません。

    - 以下の画像のように、静的タブに移動します。

        
    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials_new/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - IPアドレスフィールドをタップします。

    - iPhone/iPadで使用したい静的IPアドレスを入力します。

    - ルーターフィールドをタップします。

    - ルーターのIPアドレスを入力します。
        
    - サブネットマスクをタップして情報を入力します。

        - 通常は225.225.0.0です。

    - 画面左上のWi-Fiボタンをタップして設定を保存します。

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。