# DNS

**注**：このページの内容は、ファームウェアv4.11で初めて導入されました。

デバイスで別のファームウェアバージョンを使用している場合は、次のセレクターで対応するガイドに切り替えてください。

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [ファームウェアv4.10以前](dns.md)

</div>

---

Web管理画面の左側で、**DNS**に移動します。

ルーターのDNS設定は、ドメイン名をIPアドレスへ変換する方法を制御します。このページでは、上流デバイスから自動取得したDNSサーバーを使用するか、カスタムサーバーを設定できます。また、DNSオプションの設定や静的ホストルールの編集も行えます。

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

デフォルトでは、VPNポリシーに一致するトラフィックのDNSクエリは、VPNトンネルから提供されたDNSサーバーを使用します。VPN以外のDNSクエリは、アクティブなWANインターフェースから取得したDNSサーバーを使用します。カスタムDNSサーバーを設定すると、VPNトンネル、ルーター自体、またはその両方に適用できます。これらのオプションを有効にすると、選択した範囲のDNSクエリは、関連するネットワークインターフェースから取得したサーバーではなく、指定したサーバーで解決されます。カスタムDNSサーバーが設定されていない場合、ルーターは関連するネットワークインターフェースから取得したDNSサーバーを使用します。

## WAN DNS

WAN DNSには、Ethernet、Repeater、Tethering、Cellularを含む各WANアップリンクから取得したDNSサーバーが表示されます。

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

WANアップリンクがアクティブな場合は、次のようにDNSサーバーアドレスが右側に表示されます。

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## VPN DNS

VPN DNSには、各アクティブVPNトンネルから取得したDNSサーバーが表示されます。

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

VPNトンネルが動作している場合、VPNトラフィックのDNSクエリは、次のようにVPN DNS設定に従います。

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## 手動DNS

手動DNSでは、**Static DNS**と**Encrypted DNS**の2種類を設定できます。

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**：有効にすると、VPNトンネルを通過するパケットには、VPNのDNS設定ではなく、カスタムの手動DNSが使用されます。

- **Apply Manual DNS to Router Itself**：デフォルトで有効です。有効にすると、GoodCloudなどのルーター内蔵サービスにカスタムの手動DNS設定が適用されます。

### 静的DNS

静的DNSでは、IPv4またはIPv6のDNSサーバーアドレスを手動で入力できます。アドレスを直接入力するか、ドロップダウンリストからプリセットの公開DNSサーバーを選択して、ルーターのDNSサーバーを設定できます。

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

DNSサーバーアドレスは最大4つ入力できます。**Apply**をクリックして変更を保存します。

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### 暗号化DNS

暗号化DNSモードは、Control D、NextDNS、Quad9、CleanBrowsing、Cloudflare、AdGuard DNS、Google DNS、OpenDNSなど複数のDNSプロバイダーに対応しています。必要に応じて、暗号化DNSサーバーを手動で指定することもできます。

最初にDNSプロバイダーを選択します。残りのオプションは、選択内容に応じて変わります。

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- 特定のDNSプロバイダー（NextDNSなど）を選択した場合は、DNS over TLS（DoT）、DNS over HTTPS（DoH）、DNS over QUIC（DoQ）から暗号化方式を選択してください。DNS over QUIC（DoQ）はファームウェアv4.9で導入され、DNSプロバイダーとしてControl D、NextDNS、AdGuard DNSのいずれかを使用する場合にのみ利用できます。

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- DNSプロバイダーとしてManualを選択した場合は、DNS over TLS（DoT）、DNS over HTTPS（DoH）、DNS over QUIC（DoQ）、Oblivious DNS over HTTPS、DNSCryptから暗号化方式を選択してください。

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    次に、**Add a Server**をクリックして少なくとも1つのDNSサーバーを追加します。暗号化DNSのURLまたはstamp形式を直接入力できます。公開サーバーの一覧は、[https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}を参照してください。

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "暗号化方式の比較"

    1. **DNS over TLS (DoT)**

        専用TLSポートを介してDNSクエリを暗号化します。DNSトラフィックを通常のWebトラフィックから分離するため、ネットワーク事業者が識別しやすい方式です。

    2. **DNS over HTTPS (DoH)**

        標準のHTTPSトラフィック内でDNSデータを送信します。DNS要求が通常のWebトラフィックに混在するため、高いプライバシーを確保し、単純なトラフィックフィルタリングを回避できます。

    3. **DNS over QUIC (DoQ)**

        DNSをQUICプロトコルでカプセル化します。低遅延、高速な再接続、不安定なネットワークでの安定したパフォーマンスが特徴です。

    4. **Oblivious DNS over HTTPS (ODoH)**

        DoHの拡張版です。ユーザーのIPアドレスとDNSクエリを分離し、サーバーとネットワークプロバイダーの両方による閲覧活動の追跡を防ぎます。

    5. **DNSCrypt**

        実績のあるDNS暗号化プロトコルです。DNSトラフィックを認証・暗号化し、改ざん防止と従来のネットワーク環境との互換性を重視します。

## DNSオプション

右上の**Options**をクリックして、高度なDNS設定を構成します。

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

必要に応じて、次のオプションをオンまたはオフにできます。

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**：有効にすると、プライベートDNSの検索に失敗する場合があります。ネットワークにキャプティブポータルがある場合は、このオプションを無効にしてください。

- **Override DNS Settings of All Clients**：有効にすると、すべてのクライアントの暗号化されていないDNS設定をルーターが上書きします。

## ホストの編集

右上の**Edit Hosts**ボタンをクリックして、静的ホストルールをカスタマイズできます。

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

ルーターは、接続済みクライアントからの要求を解決する際に、これらのホストルールを優先します。

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
