# AdGuard Home DNSがVPNトンネルをバイパスするようにする方法

通常、GL.iNetルーターではVPNとAdGuard Homeを同時に使用できます。AdGuard HomeがDNSリクエストを処理するように設定されていない場合は問題は発生しません。

しかし、AdGuard HomeですべてのDNSトラフィックを管理し、クエリを**パブリック上流DNSサーバー**に転送するように設定している場合、VPNを有効にするとDNS解決が失敗します。

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Homeが有効でDNSリクエストを処理している)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(AdGuard Homeの上流DNS設定)</small>

デフォルトでは、すべての外向きトラフィックはVPNトンネルを通ります。このため、AdGuard Homeの上流DNSトラフィックがVPNに乗り、パブリック上流DNSサーバーに到達できなくなります。その結果、接続されているすべてのクライアントでドメイン名解決が失敗します。

VPNがアクティブな間もAdGuard Homeを機能させるには、LuCIでスタティックルートを追加し、上流DNSトラフィックを通常のWANゲートウェイに転送してVPNトンネルをバイパスします。以下の手順に従ってください。

1. ルーターのWeb管理パネルにログインし、**SYSTEM** -> **Advanced Settings** ->** Go to LuCI**の順に進みます。

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    同じ管理者パスワードでログインします。

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. LuCIで**Network** -> **Routing**に移動し、**Add**をクリックします。

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. 上流DNSアドレス用に新しいスタティックルートを作成します。

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface: 物理WANインターフェース**wan**を選択します。

    - Route type: デフォルト値のままにします。

    - Target: `[Your Public Upstream DNS Server]/32`

        パブリック上流DNSサーバーの実際のIPアドレスを確認するには`nslookup`を使用できます。

    - Gateway: `[Your WAN Upstream Gateway IP]`

        通常はモデムやISPゲートウェイのIPアドレスで、例: `192.168.0.1`です。ルーターのインターネットステータスページで確認してください。

    このルートにより、AdGuard Homeの上流DNSクエリがVPNトンネルをバイパスし、WAN接続を直接経由するようになります。

4. 設定を保存して適用します。AdGuard Homeは通常のDNS解決を再開します。

5. 上流DNSサーバーをテストします。

    AdGuard Homeインターフェースで直接、上流DNSサーバーを確認できます。

    ルーターのWeb管理パネルで、**APPLICATIONS** -> **AdGuard Home**に移動し、**Settings Page**をクリックしてAdGuard Homeダッシュボードを開きます。

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    AdGuard Homeダッシュボードで、**Settings** -> **DNS settings** -> **Upstream DNS servers**に移動し、**Test upstreams**をクリックします。結果は右側に表示されます。

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**ヒント**: 複数のDNSサーバーがあり、IPとドメインが混在している場合は、スタティックルートを使用するよりも、AdGuard DNSをVPN DNSから分離するほうが簡単な場合があります。

SSHでGL.iNetルーターにログインし、以下のコマンドを実行して、AdGuard HomeがWANのみを使用してDNSクエリを送信するように強制します。

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# 元に戻す場合:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

ご不明な点がございますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
