# クライアントデバイスで固定IPを手動設定する方法

=== "Windows 11"

    Windows 11では、無線および有線アダプターに固定IPアドレスを設定できます。

    **Wi-Fiアダプターで固定IPアドレスを設定する**

    1. Windows 11のPCで、**Settings** -> **Network & internet** -> **Wi-Fi**と進み、現在接続中のWi-Fi接続を選択します。

    2. **IP assignment**を見つけ、**Edit**ボタンをクリックします。

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. ポップアップウィンドウで**Manual**を選択し、**IPv4**を有効にします。

        ![IPの手動設定](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. 以下の手順でIP設定を編集します。

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: 固定IPアドレスを設定します。例: `10.1.4.119`。

        - Subnet mask: サブネットマスクを指定します。例: `255.255.255.0`。

        - Gateway: ゲートウェイアドレスを入力します。通常は同じサブネットにあるルーターのLAN IPアドレスです。たとえば、IPアドレスが`10.1.4.119`の場合、ゲートウェイは通常`10.1.4.1`です。

        - Preferred DNS: 優先DNSアドレスを指定します（必須）。GoogleのDNSサーバー`8.8.8.8`などのパブリックDNSサーバーを指定できます。

        - Alternate DNS: 代替DNSアドレスを指定します（任意）。

        - DNS over HTTPS: "Off"を選択します。次の3つのオプションがあります。

            - Off: すべてのDNSトラフィックを暗号化せず送信します。

            - On (automatic template): すべてのDNSトラフィックを暗号化して送信します。

            - On (manual template): 特定のテンプレートを指定できます。DNSサービスが自動で動作しない場合や、想定どおりに動作するテンプレートがある場合にのみ必要です。

        - DNS over HTTPSを有効にする場合は、"Fallback to plaintext"トグルスイッチをオフにします。

            **ヒント**: この機能を有効にすると、システムはDNSトラフィックを暗号化しますが、暗号化なしのクエリ送信も許可します。

    5. **Save**をクリックして設定を適用します。

        手順が完了すると、固定ネットワーク設定がコンピューターに適用されます。Webブラウザを開いてWebサイトを表示し、新しい設定をテストできます。

    ---

    **Ethernetアダプターで固定IPアドレスを設定する**

    1. Windows 11のPCで、**Settings** -> **Network & internet** -> **Ethernet**と進みます。

    2. **IP assignment**を見つけ、**Edit**ボタンをクリックします。

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. ポップアップウィンドウで**Manual**を選択し、**IPv4**を有効にします。

        ![IPの手動設定](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. 以下の手順でIP設定を編集します。

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: 固定IPアドレスを設定します。例: `10.1.4.119`。

        - Subnet mask: サブネットマスクを指定します。例: `255.255.255.0`。

        - Gateway: ゲートウェイアドレスを入力します。通常は同じサブネットにあるルーターのLAN IPアドレスです。たとえば、IPアドレスが`10.1.4.119`の場合、ゲートウェイは通常`10.1.4.1`です。

        - Preferred DNS: 優先DNSアドレスを指定します（必須）。GoogleのDNSサーバー`8.8.8.8`などのパブリックDNSサーバーを指定できます。

        - Alternate DNS: 代替DNSアドレスを指定します（任意）。

        - DNS over HTTPS: "Off"を選択します。次の3つのオプションがあります。

            - Off: すべてのDNSトラフィックを暗号化せず送信します。

            - On (automatic template): すべてのDNSトラフィックを暗号化して送信します。

            - On (manual template): 特定のテンプレートを指定できます。DNSサービスが自動で動作しない場合や、想定どおりに動作するテンプレートがある場合にのみ必要です。

        - DNS over HTTPSを有効にする場合は、"Fallback to plaintext"トグルスイッチをオフにします。

            **ヒント**: この機能を有効にすると、システムはDNSトラフィックを暗号化しますが、暗号化なしのクエリ送信も許可します。

    5. **Save**をクリックして設定を適用します。

        手順が完了すると、固定ネットワーク設定がコンピューターに適用されます。Webブラウザを開いてWebサイトを表示し、新しい設定をテストできます。

=== "macOS"

    macOSで固定IPアドレスを設定する方法は次のとおりです。

    Appleメニューから**System Preferences**を選択します。

    **Network**を選択すると、以下のページが表示されます。サイドバーから、**Wi-Fi**などの有効なネットワークインターフェースを選択します。

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Macに現在割り当てられているIPアドレスを控えておきます。表示されているプライベートIPアドレス範囲内から、新しいIPアドレスを選ぶ必要があります。

    右下の**Advanced**をクリックします。

    次に**TCP/IP**を選択すると、以下のページが表示されます。

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: "Manually"を選択します。

    - IPv4 Address: 固定IPアドレスを入力します。現在のIPアドレスの最初の3オクテットをそのままにし、最後のオクテットを未使用の値に変更します。たとえば、`192.168.7.0/24`ネットワークでは、`192.168.7.2`から`192.168.7.254`までの未使用のアドレスを選択します（ルーターのアドレスである`.1`は避けてください）。`192.168.7.0`と`192.168.7.255`は使用しないでください。

    - Subnet Mask: `255.255.255.0`（またはネットワーク管理者が指定したサブネットマスク）を入力します。

    - Router: ルーターのLAN IPアドレスを入力します。例: `192.168.7.1`。

    **OK**をクリックし、次に**Apply**をクリックします。

=== "iOS"

    手順はiOSのバージョンによって異なる場合があります。以下の手順はiOS 26.2.2を基準にしています。

    1. **Settings** -> **WLAN**と進みます。現在接続しているWi-Fiネットワークの横にある青い情報アイコン（i）をタップします。

        ![iOSの固定IP設定](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. 下にスクロールして**IPv4 Address**を見つけ、**Configure IP**を**Manual**に設定します。

        ![iOSの固定IP設定](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. iPhone/iPadで使用する**IP Address**、**Subnet Mask**、**Router IP**を指定し、右上の**Save**をタップします。

        ![iOSの固定IP設定](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    手順はAndroidのバージョンによって異なる場合があります。以下の手順はAndroid 11を基準にしています。

    1. **Settings** -> **Network & Internet** -> **Wi-Fi**と進みます。現在接続しているネットワークをタップして設定メニューを開きます。

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. 右上の鉛筆アイコンをタップしてネットワーク設定にアクセスします。

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. **Advanced options**をタップします。

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. **IP Settings**をタップし、**Static**を選択します。

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. **IP address**を入力します。**Gateway**はIPアドレスに基づいて自動的に入力されます。入力されない場合は、ネットワークのゲートウェイを入力してください。ゲートウェイは通常、同じサブネットにあるルーターのLAN IPアドレスです。

        **ヒント**: 自宅やその他のプライベートネットワークで固定IPアドレスを使う場合は、現在のサブネット内で未使用のホストアドレスを選択してください。標準的なプライベートIPアドレスの範囲は次のとおりです。

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. **Save**をタップし、ネットワークが再接続されるのを待ちます。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
