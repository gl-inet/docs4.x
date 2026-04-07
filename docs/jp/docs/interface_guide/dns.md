# DNS

Web Admin Panel の左側で、**NETWORK** -> **DNS** に移動します。

ルーターの DNS 設定では、ドメイン名をどのように IP アドレスへ変換するかを制御します。このページでは、上位デバイスから自動取得した DNS サーバーを使うか、カスタム DNS サーバーを設定するか、また DNS の優先順位を設定できます。

カスタム DNS サーバーを設定すると、DNS クエリは各ネットワークインターフェースから取得した DNS サーバーではなく、指定した DNS サーバーで解決されます。設定しない場合は、各インターフェースごとの DNS 設定が使用されます。

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** このオプションをオンにすると、プライベート DNS の名前解決に失敗する場合があります。ネットワークにキャプティブポータルがある場合は、このオプションを無効にしてください。

- **Override DNS Settings for All Clients:** 有効にすると、ルーターがすべてのクライアントの非暗号化 DNS 設定を上書きします。

- **Allow Custom DNS to Override VPN DNS:** 有効にすると、カスタム DNS を設定したときに、VPN トンネル経由のパケットは VPN 接続側の DNS サーバー設定ではなく、カスタム DNS 設定で名前解決されます。

## DNSサーバー設定

4 つのモードがあります: Automatic、Encrypted DNS、Manual DNS、DNS Proxy。

- **Automatic**: ルーターは上位デバイス（例: ISP モデム、プライマリルーター）から提供された DNS サーバー、または各ネットワークインターフェースに対応する DNS 設定を自動的に使用します。

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS**: 4 種類の暗号化方式を利用できます。DNS over TLS、DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS です。

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - DNS over TLS では、Control D、NextDNS、Cloudflare から DNS プロバイダーを選択します。

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - それ以外の 3 つ（DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS）では、リポジトリから少なくとも 1 つの DNS Server を選択します。

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS**: ドロップダウンリストから、ルーターで使用する DNS Server を少なくとも 1 つ選択します。

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy**: ルーターはすべての LAN DNS クエリを、指定したプロキシサーバーアドレス（例: 8.8.8.8#53）へ転送します。ネットワーク上で別の DNS サーバーや Pi-hole を運用している場合に便利です。

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Hosts の編集

クライアントからのリクエストは、Hosts に記述した静的 DNS ルールを優先して解決されます。

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
