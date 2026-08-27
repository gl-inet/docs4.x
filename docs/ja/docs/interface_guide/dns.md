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

### Automatic

このモードでは、ルーターは上位デバイス（例: ISP モデム、プライマリルーター）から提供された DNS サーバー、または各ネットワークインターフェースに対応する DNS 設定を自動的に使用します。

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS

ファームウェアのバージョンに応じて、以下の説明を参照してください。

!!! note "ファームウェア v4.8 以前"

    4 種類の暗号化方式を利用できます。DNS over TLS、DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS です。

    まず **Encryption Type** を選択してください。選択に応じて残りのオプションが変わります。

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - **DNS over TLS (DoT)** では、**Control D**、**NextDNS**、**Cloudflare** から DNS プロバイダーを選択します。

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - **それ以外の 3 種類（DNSCrypt-Proxy、DNS over HTTPS、Oblivious DNS over HTTPS）** では、リポジトリから少なくとも 1 つの DNS Server を選択します。

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

!!! note "ファームウェア v4.9 以降"

    Encrypted DNS モードでは、Control D、NextDNS、Cloudflare に加えて、**Quad9**、**CleanBrowsing**、**AdGuard DNS**、**Google DNS**、**OpenDNS** も利用できます。必要に応じて暗号化 DNS サーバーを手動で指定することも可能です。

    まず **DNS Provider** を選択してください。選択に応じて残りのオプションが変わります。

    ![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

    - 特定の DNS プロバイダー（例: NextDNS）を選択した場合は、**DNS over TLS (DoT)**、**DNS over HTTPS (DoH)**、**DNS over QUIC (DoQ)** から暗号化方式を選択します。なお、**DNS over QUIC (DoQ)** はファームウェア v4.9 で導入された機能で、DNS プロバイダーに **Control D**、**NextDNS**、**AdGuard DNS** を選択した場合のみ利用できます。

        ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

    - DNS プロバイダーに **Manual** を選択した場合は、**DNS over TLS (DoT)**、**DNS over HTTPS (DoH)**、**DNS over QUIC (DoQ)**、**Oblivious DNS over HTTPS**、**DNSCrypt** から暗号化方式を選択します。

        ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

        次に **Add a Server** をクリックして、少なくとも 1 つの DNS サーバーを追加します。暗号化 DNS の URL または stamp 形式を直接入力できます。公開サーバーの一覧は [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"} を参照してください。

        ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### 暗号化方式の比較

1. **DNS over TLS (DoT)**

    専用の TLS ポートを使って DNS クエリを暗号化します。通常の Web トラフィックと DNS トラフィックを分離するため、ネットワーク管理者が識別しやすい方式です。

2. **DNS over HTTPS (DoH)**

    標準的な HTTPS トラフィックの中で DNS データを送信します。DNS リクエストを通常の Web トラフィックに紛れ込ませることで高いプライバシー性を確保し、単純なトラフィックフィルタリングを回避できます。

3. **DNS over QUIC (DoQ)**

    DNS を QUIC プロトコル上でカプセル化します。低遅延、高速な再接続、不安定なネットワークでも安定した動作が特長です。

4. **Oblivious DNS over HTTPS (ODoH)**

    DoH を強化した方式です。ユーザー IP と DNS クエリを分離することで、サーバー側とネットワーク提供者の双方から閲覧行動を追跡されにくくします。

5. **DNSCrypt**

    DNS 向けの成熟した暗号化プロトコルです。DNS トラフィックの認証と暗号化を行い、改ざん防止や従来型ネットワーク環境との互換性に重点を置いています。

### Manual DNS

このモードでは、ルーターで使用する DNS サーバーをカスタマイズできます。ドロップダウンリストから、ルーターで使用する DNS Server を少なくとも 1 つ選択してください。

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy

このモードでは、ルーターはすべての LAN DNS クエリを、指定したプロキシサーバーアドレス（例: 8.8.8.8#53）へ転送します。ネットワーク上で別の DNS サーバーや Pi-hole を運用している場合に便利です。

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Hosts の編集

右上の **Edit Hosts** ボタンをクリックすると、静的なホストルールをカスタマイズできます。

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

ルーターは、接続中クライアントからのリクエストを名前解決する際に、これらのホストルールを優先します。

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
