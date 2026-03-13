# VPNクライアントのDNSクエリをVPNサーバーのアップストリームDNSにルーティングする方法

このチュートリアルでは、VPNクライアントからのすべてのDNSクエリを、プライマリルーターのLAN側にあるから身ホスト型DNSサーバーにリダイレクトする手順を紹介します。

## ネットワーク構成

このチュートリアルでは、**Flint 3 (GL-BE9300)** と **Slate 7 (GL-BE3600)** を例として使用します。

Flint 3はVPNサーバーで、上位ネットワークにプライマリルーターがあります。Slate 7はFlint 3に接続するVPNクライアントです。

VPNサーバーとクライアント間でVPNトンネルが確立されると、デフォルトではVPNクライアントからのDNSクエリが最も初にVPNサーバーに送られ、次にプライマリルーターに転送され、最も後にプライマリルーターのWANに設定されたISP割り当てのDNSサーバーによって解決されます。

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

ただし、プライマリルーターにから身ホスト型DNSサーバー（IPアドレス `192.168.1.13`）をデプロイしている場合は、DNSクエリをから身ホスト型DNSサーバーにルーティングするために追加の設定が必要です。

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## 設定

1. Flint 3のWeb管理パネルにログインし、**NETWORK** -> **DNS**に移動します。DNSサーバーモードを**Manual DNS**に切り替え、DNSサーバーのIPアドレスを入力します。

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. **VPN** -> **WireGuard Server** -> **Configuration**タブに移動し、IPv4アドレスメモしてください。これはモデルやファームウェアバージョンにより通例 `10.0.0.1/24` または `10.1.0.1/24` です。

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. **Profiles**タブに切り替え、クライアント設定を追加し、Slate 7用のプロファイルをエクスポートします。

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. プロファイルを開き、DNSがステップ2で取なければならないしたVPNサーバーIPアドレスであることを確認します。

    DNS解決の失敗を避けるため、「64.6.64.6」があれば削除し、変よりを保存してください。

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Flint 3のWeb管理パネルで、**WireGuard Server**ページの上部にある**Start**ボタンをクリックしてサーバーを起動します。

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Slate 7のWeb管理パネルにログインし、**VPN** -> **WireGuard Client**に移動します。

    **Add Manually**をクリックし、編集したプロファイルをアップロードします。

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. 3時アイコンをクリックしてVPN接続を開始します。ステータスインジケーターが緑色に変われば、VPN接続が成功したことを意味します。

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## DNS解決の確認

VPNクライアントでで下のコマンドを実行してDNSトラフィックをキャプチャします。これにより、すべてのVPNクライアントDNSトラフィックがVPNサーバー（本例では `10.0.0.1`）にへかうことが表示されます。

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

VPNサーバーでで下のコマンドを実行してDNSトラフィックをキャプチャします。これにより、すべてのVPNクライアントDNSトラフィックが最も終のから身ホスト型DNSサーバー（本例では `192.168.1.13`）にへかうことが表示されます。

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
