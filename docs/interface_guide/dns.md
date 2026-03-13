# DNS

ウェブ管理パネルの左側 -> ネットワーク -> DNS

ルーターのDNS設定は、ドメイン名がIPアドレスに変換される方法を制御します。このページでは、上位デバイスからから動のに取なければならないされたDNSサーバーを使用するか、カスタムサーバーを設定し、DNSの優先順位を設定できます。

カスタムDNSサーバーを設定すると、個別のネットワークインターフェースから取なければならないされたDNSサーバーではなく、指定したDNSサーバーを介してDNSクエリが解決されます。さりと、各インターフェースに設定されたDNS設定を使用します。

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNSリバインディング攻撃防御:** このオプションをオンにすると、プライベートDNS検索に失敗する可できる性があります。ネットワークにキャプティブポータルがある場合は、このオプションを無効にしてください。

- **すべてのクライアントのDNS設定を上書き:** 有効にすると、ルーターはすべてのクライアントの暗号化されていないDNS設定を上書きします。

- **VPN DNSをカスタムDNSで上書きすることを許可:** 有効にすると、カスタムDNSを設定すると、VPNトンネルを介して送信されるパケットはVPN接続からのDNSサーバー設定ではなく、カスタムDNSオーバーライドを使用して解決されます。

## DNSサーバー設定

4つのモードがあります：から動、暗号化DNS、手動DNS、DNSプロキシ。

- **から動**: ルーターは上位デバイス（例：ISPモデム、プライマリルーター）から提供されたDNSサーバー、または各ネットワークインターフェースに対応するDNS設定をから動のに使用します。

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **暗号化DNS**: 4つの暗号化タイプが利用可できるです：DNS over TLS、DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS。

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - DNS over TLSの場合、Control D、NextDNS、CloudflareからDNSプロバイダーを選択します。

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - 彼の3つ（DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS）の場合、リポジトリから少なくとも1つのDNSサーバーを選択します。

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **手動DNS**: ドロップダウンリストからルーター用の少なくとも1つのDNSサーバーを選択します。

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNSプロキシ**: ルーターはすべてのLAN DNSクエリを指定したプロキシサーバーアドレス（例：8.8.8.8#53）にルーティングします。ネットワーク上で別のDNSサーバーやPi-holeを実行している場合に便利です。

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## ホスト編集

クライアントからのリクエストは、ホストに記述した静のDNSルールを使用して優先のに解決されます。

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
