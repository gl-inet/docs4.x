# VPNクライアント有効時に WAN へのアクセスを許可する方法

GL.iNet ルーターで VPN クライアントを有効にすると、デフォルトのグローバルモードでは、LAN 側のデバイスはローカル WAN 側のデバイスやサービスにアクセスできません。これは、DNS リークを防ぐために、LAN からのすべてのトラフィックが上位ネットワーク（WAN）ではなく VPN トンネル経由でルーティングされるためです。

このチュートリアルでは、VPN クライアント配下の LAN デバイスから、ローカル WAN 上のサービス（プリンター、NAS など）へアクセスできるようにする手順を紹介します。

![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## ファームウェア v4.7 以前

VPN クライアントの Web 管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Client** に移動します。右上の **Global Options** をクリックします。

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

**Allow Access WAN** を有効にして、**Apply** をクリックします。

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

このオプションを有効にすると、VPN 接続中でも、クライアントデバイスは上位サブネット上の WAN サービス（プリンター、NAS など）に引き続きアクセスできます。

## ファームウェア v4.8 以降

ファームウェア v4.8 では、**Allow Access WAN** オプションは **VPN Dashboard** から削除されました。ただし、VPN ポリシーを使えばローカル WAN へのアクセスを実現できます。

以下の手順に従って設定してください。

1.  VPN クライアントの Web 管理パネルにログインし、**VPN** -> **VPN Dashboard** に移動します。

    右上のモード表示をクリックします。

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    **Policy Mode** に切り替え、**Apply** をクリックします。

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    ページが更新され、以下のように表示されます。

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2.  中央のボックスをクリックして、トンネルの宛先を設定します。

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    **Exclude Speficied Domain / IP** を選択し、ルーターの WAN サブネットを入力して、**Apply** をクリックします。

    これにより、WAN サブネット宛てのすべてのトラフィックが、VPN トンネルではなくローカル WAN 経由でルーティングされます。

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    ここでは例として 192.168.0.1/24 を使用します。これを入力して適用すると、VPN トンネルは次のように表示されます。

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "GL.iNet ルーターの WAN サブネットを確認するには？"

        GL.iNet ルーターの WAN サブネットは、通常 **INTERNET** ページで確認できます。これは、ルーターの WAN インターフェースが接続している上位側デバイス（ISP モデムや上位ゲートウェイなど）によって決まります。

        たとえば、ルーターが二次ルーターとして動作しており、その WAN ポートが ISP モデムやメインルーターの LAN ポートなど、別のローカルネットワークに接続されているとします。このとき、ルーターの WAN IP が 192.168.1.165、Gateway が 192.168.1.1、Subnet Mask が 255.255.255.0（小規模ネットワークで一般的なマスク）であれば、対応する WAN サブネットは 192.168.1.0/24 です。これは上位側デバイスの LAN サブネットでもあります。

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **注意**: 192.168.1.0/24 のプレフィックス長は 24 で、これはサブネットマスク 255.255.255.0 に対応します。ルーターの WAN Subnet Mask が 255.255.255.0 でない場合、WAN サブネットのプレフィックス長は "/24" にはなりません。実際の WAN 設定に基づいて WAN サブネットを確認してください。

3.  右側のボックスをクリックして、トンネル動作を設定します。

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    **Use VPN** を選択し、VPN 設定ファイルを選んで **Apply** をクリックします。

    利用可能な設定がまだない場合は、まずルーターを VPN クライアントとして動作させるための設定ファイルをアップロードしてください。その後この画面に戻り、**Use VPN** を選択して設定ファイルを指定し、**Apply** をクリックします。

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4.  右上のスイッチを切り替えて、この VPN トンネルを有効にします。接続が開始されます。

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    数分待つと、正常に接続された場合は緑色で表示されます。

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    パブリック IP を確認して VPN 接続をテストします。たとえば、ブラウザで [whatismyip](https://whatismyipaddress.com/){target="\_blank"} にアクセスすると、以下のようにパブリック IP アドレスと位置情報が表示されます。

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5.  WAN サブネット上のデバイスやサービスにアクセスし、正常にアクセスできるか確認します。

    接続確認には `ping` コマンドも利用できます。

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
