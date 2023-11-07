# DNS

Web管理パネルの左側 -> MORE SETTINGS -> DNS

カスタムDNSサーバーを設定すると、あらゆるdns名は、wan、リピータ、セルラー、ホットスポット共有、VPN設定のDNSサーバーから取得するのではなく、ここで設定したDNSサーバーを経由して解決されるようになります。

![dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_page.png){class="glboxshadow"}

**DNS Rebinding Attack Protection:** このオプションをオンにすると、プライベートDNSルックアップに失敗することがあります。ネットワークにキャプティブポータルがある場合は、このオプションを無効にしてください。

**すべてのクライアントのDNS設定を上書きする。** 有効にすると、ルーターはすべてのクライアントの非暗号化DNS設定を上書きします。

## DNSサーバーの設定

4つのモードがあります。

- 自動、親ルーターのゲートウェイを使用します。

    ![automatic](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_automatic.png){class="glboxshadow"}

- 暗号化DNS

    ![encrypted dns](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_encrypted_dns.png){class="glboxshadow"}

    **暗号化タイプ**は、DNS over TLS、DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPSの4種類です。

    - DNS over TLSの場合、DNSプロバイダーはNextDNSとCloudflareの2つの選択肢があります。

    - DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPSについては、DNSサーバーを選択することができます。

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dnscrypt-proxy.png){class="glboxshadow"}

- マニュアルDNS

    ![マニュアルDNS](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_manual_dns.png){class="glboxshadow"}

- DNS Proxy

    ![マニュアルDNS](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/dns_server_settings_dns_proxy.png){class="glboxshadow"}

## ホストの編集

クライアントからのリクエストは、Hostsに記述した静的DNSルールで優先的に解決されます。

![ホスト](https://static.gl-inet.com/docs/router/en/4/tutorials/dns/edit_hosts.png){class="glboxshadow"}
