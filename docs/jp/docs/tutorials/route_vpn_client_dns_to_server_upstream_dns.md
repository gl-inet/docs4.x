# VPNクライアントのDNSクエリをVPNサーバー上流のDNSへルーティングする方法

このチュートリアルでは、VPNクライアントから送信されるすべてのDNSクエリを、VPNサーバーの上流側にあるプライマリルーターのLAN内で動作している自前のDNSサーバーへリダイレクトする手順を紹介します。

## トポロジー

このチュートリアルでは、**Flint 3 (GL-BE9300)** と **Slate 7 (GL-BE3600)** を例に説明します。

Flint 3 はVPNサーバーで、その上流ネットワークにはプライマリルーターがあります。Slate 7 は Flint 3 に接続するVPNクライアントです。

VPNサーバーとクライアントの間にVPNトンネルが確立されると、デフォルトではVPNクライアントからのDNSクエリはいったんVPNサーバーへ送られ、その後プライマリルーターへ転送され、最終的にプライマリルーターのWAN側で設定されているISP割り当てのDNSサーバーによって名前解決されます。

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

ただし、プライマリルーター上に自前のDNSサーバー（IPアドレス `192.168.1.13`）を構築している場合は、DNSクエリをその自前のDNSサーバーへルーティングするために追加設定が必要です。

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## 設定

1. Flint 3 のWeb管理画面にログインし、**NETWORK** -> **DNS** に移動します。DNS Server Mode を **Manual DNS** に切り替え、自前のDNSサーバーのIPアドレスを入力します。

   ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. **VPN** -> **WireGuard Server** -> **Configuration** タブに移動し、IPv4 Address を確認します。モデルやファームウェアバージョンによって異なりますが、通常は `10.0.0.1/24` または `10.1.0.1/24` です。

   ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. **Profiles** タブへ切り替え、クライアント設定を追加して、Slate 7 用のプロファイルをエクスポートします。

   ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. プロファイルを開き、DNS が手順2で確認したVPNサーバーのIPアドレスになっていることを確認します。

   DNS名前解決の失敗を防ぐため、`64.6.64.6` が含まれている場合は削除し、変更を保存してください。

   ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Flint 3 のWeb管理画面で、**WireGuard Server** ページ上部にある **Start** ボタンをクリックしてサーバーを起動します。

   ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Slate 7 のWeb管理画面にログインし、**VPN** -> **WireGuard Client** に移動します。

   **Add Manually** をクリックし、編集済みのプロファイルをアップロードします。

   ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. 三点アイコンをクリックしてVPN接続を開始します。ステータスインジケーターが緑色になれば、VPN接続は成功しています。

   ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## DNS名前解決を確認する

VPNクライアントで次のコマンドを実行してDNSトラフィックをキャプチャします。これにより、VPNクライアントからのすべてのDNSトラフィックがVPNサーバー（この例では `10.0.0.1`）へ送られていることを確認できます。

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

VPNサーバーで次のコマンドを実行してDNSトラフィックをキャプチャします。これにより、VPNクライアントからのすべてのDNSトラフィックが最終的に自前のDNSサーバー（この例では `192.168.1.13`）へ送られていることを確認できます。

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
