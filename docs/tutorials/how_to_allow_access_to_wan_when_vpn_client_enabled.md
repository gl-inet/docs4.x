# VPNクライアントが有効なときにWANへのアクセスを許可する方法

GL.iNetルー器でVPNクライアントが有効な場合、デフォルトのGlobal Modeでは、LAN機器はローカルWAN機器やサービスにアクセスできません。これは、DNSリークを避けるため、すべてのLANからのトラフィックが上位ネットワーク（WAN）ではなくVPNトンネルを経よりしてルーされるためです。

このチュートリアルでは、VPNクライアントのLAN機器がローカルWANサービス（プリンター、NASなど）にアクセスできるようにする手順を紹介します。

![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## ファームウェアv4.7で前

VPNクライアントのWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Client**に移動します。右上隅の**Global Options**をクリックします。

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

**Allow Access WAN**を有効にし、**Apply**をクリックします。

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

このオプションが有効になっていると、VPNが接続されている間、クライアント機器はまだ上位サブネットのWANサービス（プリンター、NASなど）にアクセスできます。

## ファームウェアv4.8で降

オプション**Allow Access WAN**はファームウェアv4.8のVPN Dashboardから削除されました。しかし、VPNポリシーを通じてローカルWANアクセスを達成できます。

以下の手順に従ってください。

1. VPNクライアントのWeb管理パネルにログインし、**VPN** -> **VPN Dashboard**に移動します。

    右上隅のモードをクリックします。

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    **Policy Mode**に切り替え、**Apply**をクリックします。

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    ページがアップデートされ、下図のようにのように表示されます。

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. 真ん中のボックスをクリックしてトンネルターゲットを設定します。

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    **Exclude Speficied Domain / IP**を選択し、ルー器のWANサブネットを入力し、**Apply**をクリックします。

    これにより、WANサブネットへのすべてのトラフィックがVPNトンネルではなくローカルWAN経由でルーされます。

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    ここではサブネット192.168.0.1/24を例にとって説明します。このサブネットを入力して適用すると、VPNトンネルが下図のようにのように表示されます。

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "私のGL.iNetルー器のWANサブネットを知る方法は？"
    
        GL.iNetルー器のWANサブネットは通例INTERNETページで確認できます。ルー器のWANインターフェースが接続する上位機器（ISPモデムや上位ゲートウェイなど）によって決まります。

         例えば、ルー器が二次ルー器として機能している場合（WANポートがISPモデムやメインルー器のLANポートなど別のローカルネットワークに接続されている場合）、ルー器のWAN IPが192.168.1.165、ゲートウェイが192.168.1.1、サブネットマスクが255.255.255.0（小规模ネットワークの一般的なマスク）の場合、対応するWANサブネットは192.168.1.0/24です。これは上位機器のLANサブネットでもあります。

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **注意**：192.168.1.0/24のプレフィックス長は24で、これはサブネットマスク255.255.255.0に対応しています。ルー器のWANサブネットマスクが255.255.255.0でない場合、WANサブネットのプレフィックス長は「/24」ではありません。実際のWAN設定に基づいてWANサブネットを確認してください。

3. 右側のボックスをクリックしてトンネルアクション（VPNを使用するかVPNを使用しないか）を設定します。

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    **Use VPN**を選択し、VPN設定ファイルを選択して**Apply**をクリックします。
    
    利用可能な設定がない場合は、まずルー器をVPNクライアントとして設定する設定をアップロードしてください。次にこのページに移動し、Use VPNを選択してVPN設定ファイルを選択してApplyをクリックします。

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. 右上隅のスイッチをトグルしてこのVPNトンネルを有効にします。接続が開始されます。

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    しばらくお待ちください。正常に 接続すると緑に変更されます。

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    パブリックIPを検索してVPN接続をテストします。例えば、ブラウザを開いて[whatismyip](https://whatismyipaddress.com/){target="_blank"}にアクセスします。下図のようにのようにパブリックIPアドレスと位置情報が表示されます。

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. WANサブネット上の機器やサービスにアクセスし、成功のにアクセスできるか確認します。

    pingコマンドを使用して接続をテストできます。

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
