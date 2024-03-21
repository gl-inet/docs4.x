# DNS

Web 管理パネルの左側 -> ネットワーク -> DNS

カスタムDNSサーバーを設定すると、すべてのDNS名は、WAN、リピータ、セルラー、ホットスポット共有、またはVPN設定のDNSサーバーから取得したものではなく、ここで設定したDNSサーバーを経由して解決されます。

![dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_page.png){class="glboxshadow"}

**DNSリバインディング攻撃防御：** このオプションをオンにすると、プライベートDNS検索に失敗する可能性があります。ネットワークにキャプティブポータルがある場合は、このオプションを無効にしてください。

**すべてのクライアントの DNS 設定を上書きします：** 有効にすると、ルーターはすべてのクライアントの暗号化されていないDNS設定を上書きします。

## DNSサーバー設定

4つのモードがあります。

- 自動では、親ルーターのゲートウェイを使用し ます。

    ![automatic](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_automatic.png){class="glboxshadow"}

- 暗号化DNS

    ![encrypted dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_encrypted_dns.png){class="glboxshadow"}

    **暗号化タイプ**には、DNS over TLS、DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS の 4 つのタイプがあります。

    - DNS over TLS の場合、DNS プロバイダーには NextDNS と Cloudflare の 2 つのオプションがあります。

    - DNSCrypt-Proxy、DNS over HTTPS、および Oblivious DNS over HTTPS の場合は、DNS サーバーを選択できます。

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dnscrypt-proxy.png){class="glboxshadow"}

- 手動DNS

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_manual_dns.png){class="glboxshadow"}

- DNS Proxy

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_dns_proxy.png){class="glboxshadow"}

## ホスト編集

クライアントからのリクエストは、ホストに記述した静的 DNS ルールを使用して優先的に解決されます。

![hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/edit_hosts.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
