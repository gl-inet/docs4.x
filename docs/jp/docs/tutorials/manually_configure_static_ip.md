# クライアントデバイスで静的IPを手動設定する方法

=== "Windows 11"

    Windows 11 では、無線アダプターと有線アダプターの両方で、Settings アプリから静的IPアドレスを設定できます。

    **Wi-Fiアダプターで静的IPアドレスを設定する**

    Wi-Fiアダプターに静的IPアドレスを割り当てるには、以下の手順を実行します。

    1. Windows 11 で Settings を開き、**Network & Internet** -> **Wi-Fi** タブ -> 現在接続しているネットワークを選択します。

    2. 「IP settings」セクションで **Edit** ボタンをクリックします。

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. 以下のように設定します。

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - **Manual** を選択し、IPv4 のトグルスイッチをオンにします。
        - Windows 11 用の静的IPアドレスを設定します。例: `10.1.4.119`
        - Subnet mask を指定します。例: `255.255.255.0`
        - Default Gateway address を指定します。
        - Preferred DNS address を指定します。必須です。
        - 必要に応じて Alternate DNS address を指定します。
        - 「DNS over HTTPS」ドロップダウンメニューで、Preferred DNS と Alternate DNS の両方を **Off** に設定します。必要に応じて、次のDoHオプションも利用できます。
            - **Off**: すべてのDNSトラフィックを暗号化せずに送信します。
            - **On (automatic template)**: すべてのDNSトラフィックを暗号化して送信します。
            - **On (manual template)**: 特定のテンプレートを手動指定できます。DNSサービスが自動で動作しない場合や、期待どおりに動くテンプレートがある場合にのみ必要です。
        - DoH を有効にした場合は、「Fallback to plaintext」トグルスイッチをオフにします。

            - Quick tip: この機能をオンにするとDNSトラフィックは暗号化されますが、暗号化なしでクエリを送信できるようにもなります。

    4. **Save** ボタンをクリックします。

        手順が完了すると、静的ネットワーク設定がコンピューターへ適用されます。Webブラウザーでサイトを開き、新しい設定を確認してください。


    ## **Ethernetアダプターで静的IPアドレスを設定する**

    Windows 11 で Ethernet（有線）アダプターに静的IPアドレスを割り当てるには、以下の手順を実行します。

    1. Settings を開き、**Network & Internet** -> **Ethernet** タブへ移動します。

    2. 「IP settings」セクションで **Edit** ボタンをクリックします。

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. 以下のように設定します。

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - **Manual** を選択します。
        - IPv4 のトグルスイッチをオンにします。
        - Windows 11 用の静的IPアドレスを設定します。例: `10.1.4.119`
        - Subnet mask を指定します。例: `255.255.255.0`
        - Default Gateway address を指定します。
        - Preferred DNS address を指定します。必須です。
        - 必要に応じて Alternate DNS address を指定します。
        - 「DNS over HTTPS」ドロップダウンメニューで、Preferred DNS と Alternate DNS の両方を **Off** に設定します。必要に応じて、次のDoHオプションも利用できます。
            * **Off**: すべてのDNSトラフィックを暗号化せずに送信します。
            * **On (automatic template)**: すべてのDNSトラフィックを暗号化して送信します。
            * **On (manual template)**: 特定のテンプレートを手動指定できます。DNSサービスが自動で動作しない場合や、期待どおりに動くテンプレートがある場合にのみ必要です。
        - DoH を有効にした場合は、「Fallback to plaintext」トグルスイッチをオフにします。

    4. **Save** ボタンをクリックします。

        手順が完了したら、Webブラウザーでサイトを開いて設定を確認できます。

=== "macOS"

    macOS で静的IPアドレスを設定する方法は以下のとおりです。

    MacBook を使用している場合は、新しいネットワークロケーションを作成すると便利です。これにより、特定のネットワークだけで静的IPアドレスを使い、他のネットワークでは使わないようにできます。

    Apple メニューから **System Preferences** を選択します。

    **Network** を選択します。以下のウィンドウが表示されます。

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    サイドバーから、現在使用中のネットワークインターフェースを選択します。この例では無線ネットワークへ接続しているため、Wi-Fi を選択します。

    現在 Mac に割り当てられているIPアドレスを控えておきます。このあと、表示されているプライベートIPアドレス帯の中から新しいIPアドレスを選びます。

    **Advanced** をクリックします。

    **TCP/IP** を選択します。以下のウィンドウが表示されます。

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    Configure IPv4 メニューで **Manually** を選択します。

    IPv4 Address フィールドに静的IPアドレスを入力します。たとえば、現在のIPアドレスの最後の数字だけを変更する方法があります。この例では、`192.168.7.0` から `192.168.7.255` の範囲で、他のデバイスに割り当てられていないアドレスを選択できます。

    **OK** をクリックし、続けて **Apply** をクリックします。

=== "Android"

    手順はAndroidのバージョンによって異なります。ここでは Android 11 を例に説明します。

    1. **Settings** を開き、**Network & Internet** -> **Wi-Fi** を選択し、現在接続中のネットワークをタップして設定画面を開きます。

    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. 静的IPアドレスを設定するには、以下の手順を実行します。

    - 右上の鉛筆アイコンをタップしてネットワーク設定を開きます。

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - **Advanced Options** を選択します。

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - **IP Settings** を選択します。

    - 設定を **DHCP** から **Static** に変更します。

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - 自宅やその他のプライベートネットワークで静的IPアドレスを使う場合は、以下の標準的なプライベートIPアドレス範囲内から選択してください。`10.0.0.0` から `10.255.255.255`、`172.16.0.0` から `172.31.255.255`、`192.168.0.0` から `192.168.255.255`

    - IPアドレスを入力します。
        - この値はネットワークごとに異なります。例: `192.168.1.128`

    - Gateway は通常、入力したIPアドレスに基づいて自動入力されます。入力されない場合は、同じIPアドレスの最後の数字だけを `1` に変更してください。
        - 例: 上記の例なら `192.168.1.1`

    3. **Save** をタップし、ネットワークが再接続されるまで待ちます。

=== "iOS"

    自宅やその他のプライベートネットワークで静的IPアドレスを使う場合は、以下の標準的なプライベートIPアドレス範囲内から選択してください。

    `10.0.0.0` から `10.255.255.255`
    `172.16.0.0` から `172.31.255.255`
    `192.168.0.0` から `192.168.255.255`

    静的IPアドレスを設定するには、以下の手順を実行します。

    - Settings アイコンをタップします。

    - **Wi-Fi** に移動します。

    - Wi-Fiネットワーク名の横にある青い情報アイコン `(i)` をタップします。
         - iOS 7 より前の古いバージョンでは、表示が異なる場合があります。

    - 下の画像のように **Static** タブへ移動します。

    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - **IP Address** フィールドをタップします。

    - iPhone / iPad で使用したい静的IPアドレスを入力します。

    - **Router** フィールドをタップします。

    - ルーターのIPアドレスを入力します。

    - **Subnet Mask** をタップして入力します。

        - 通常は `225.225.0.0` です。

    - 画面左上の **Wi-Fi** ボタンをタップして設定を保存します。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
