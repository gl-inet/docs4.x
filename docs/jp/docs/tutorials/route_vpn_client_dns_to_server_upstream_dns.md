# VPNクライアントのDNSクエリをVPNサーバー上流のDNSへルーティングする方法

このチュートリアルでは、VPNクライアントからのすべてのDNSクエリを、VPNサーバーの上流側であるプライマリルーターのLAN側に設置した自前のDNS Serverへ転送する手順を紹介します。

## トポロジー

このチュートリアルでは、**Flint 3 (GL-BE9300)** と **Slate 7 (GL-BE3600)** を例として使用します。

Flint 3 がVPNサーバーで、その上流ネットワークにプライマリルーターがあります。Slate 7 は Flint 3 に接続するVPNクライアントです。

VPNサーバーとクライアントの間にVPNトンネルが確立されると、デフォルトでは、VPNクライアントからのDNSクエリはまずVPNサーバーに送られ、次にプライマリルーターへ転送され、最後にプライマリルーターのWANに設定されたISP割り当てのDNSサーバーで名前解決されます。

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

しかし、プライマリルーター側に自前のDNS Server（IPアドレス `192.168.1.13`）を構築している場合は、DNSクエリをそのDNS Serverへ送るために追加設定が必要です。

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## 設定

1. Flint 3 のWeb管理パネルにログインし、**NETWORK** -> **DNS** に移動します。DNS Server Mode を **Manual DNS** に切り替え、DNS Server のIPアドレスを入力します。

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. **VPN** -> **WireGuard Server** -> **Configuration** タブへ移動し、IPv4 Address を控えます。通常は `10.0.0.1/24` または `10.1.0.1/24` で、モデルやファームウェアバージョンによって異なります。

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. **Profiles** タブに切り替え、クライアント設定を追加して、Slate 7 用のプロファイルをエクスポートします。

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. プロファイルを開き、DNS が Step 2 で取得した VPN Server IP address になっていることを確認します。

    DNS解決に失敗しないよう、もし "64.6.64.6" が含まれていれば削除し、変更を保存してください。

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Flint 3 のWeb管理パネルで、**WireGuard Server** ページ上部の **Start** ボタンをクリックしてサーバーを起動します。

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Slate 7 のWeb管理パネルにログインし、**VPN** -> **WireGuard Client** に移動します。

    **Add Manually** をクリックし、編集済みプロファイルをアップロードします。

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. 三点アイコンをクリックしてVPN接続を開始します。ステータスインジケーターが緑色になれば、VPN接続は成功です。

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## DNS解決を確認する

VPNクライアントで次のコマンドを実行してDNSトラフィックをキャプチャします。これにより、VPNクライアントのDNSトラフィックがすべてVPNサーバー（この例では `10.0.0.1`）へ送られていることがわかります。

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

VPNサーバーで次のコマンドを実行してDNSトラフィックをキャプチャします。これにより、VPNクライアントのDNSトラフィックが最終的に自前のDNS Server（この例では `192.168.1.13`）へ送られていることがわかります。

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
