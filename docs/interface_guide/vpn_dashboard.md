# VPN ダッシュボード

Web 管理パネルにアクセスし、左側のメニューから -> VPN -> VPN ダッシュボード を選択します。

VPN ダッシュボードページは、VPN のステータスと設定のためのページです。ここには [VPN クライアント](#vpn-client) と [VPN サーバー](#vpn-server) の二つのセクションがあります。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN クライアント

最初のページは、OpenVPN および WireGuard の設定がありません。**Set Up Now** をクリックしてください。それぞれ [OpenVPN クライアント](openvpn_client.md) と [WireGuard クライアント](wireguard_client.md) のページに移動します。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

設定が完了すると、設定ファイル欄で設定ファイルを選択できます。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### VPN クライアントオプション

OpenVPN または WireGuard の歯車アイコンをクリックします。

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

OpenVPN クライアントオプション。

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

WireGuard クライアントオプション。

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* リモートアクセス LAN を許可

    このオプションを有効にすると、ルーターに接続されたデバイスが VPN サーバー側の LAN にアクセスできるようになります。これには VPN サーバー側での適切な設定も必要です。

    例えば、以下の画像のように、このオプションを有効にすると、*あなたのデバイス* が *NAS* にアクセスできるようになりますが、NAS にアクセスするためには *VPN サーバー* 側でもそのような設定が必要です。

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* IP マスカレード

    このオプションを有効にすると、LAN 上のクライアントデバイスが IP パケットを送信する際に、ルーターが送信元の IP アドレスを自身のアドレスに置き換えてから VPN トンネルに転送します。

* MTU

    MTU は最大転送単位のことです。設定した MTU は、設定ファイルの MTU 項目を上書きします。

### プロキシモード

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

上の図のように、現在のプロキシモードはグローバルプロキシです。グローバルプロキシをクリックして他のプロキシモードに切り替えます。**グローバルプロキシ**、**ポリシーモード**、**ルートモード**の3種類があります。

1. グローバルプロキシ

    すべてのトラフィックがVPNを通過します。アクティブ化できるVPNクライアントインスタンスは1つだけです。

2. ポリシーモード

    1. 対象ドメインまたはIPベース。
    
        このモードでは、IPアドレスまたはドメイン名で定義された特定のウェブサイトのトラフィックのみがVPNを通過します。アクティブ化できるVPNクライアントインスタンスは1つだけです。

    2. クライアントデバイスベース。

        このモードでは、MACアドレスで定義された特定のローカルクライアントデバイスのトラフィックのみがVPNを通過します。アクティブ化できるVPNクライアントインスタンスは1つだけです。

    3. VLANベース。

        このモードでは、特定のVLANのトラフィックのみがVPNを通過します。アクティブ化できるVPNクライアントインスタンスは1つだけです。

3. ルートモード

    1. 自動検出

        各VPNクライアント設定ファイルに定義されたルーティングルールやVPNサーバから発行されたルールが使用されます。
    
    2. ルーティングルールをカスタマイズする

        各VPNクライアントインスタンスのルーティングルールを手動で設定できます。

### VPNクライアントのグローバルオプション

**グローバルオプション**をクリックすると、グローバルオプションダイアログが表示されます。

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. 非VPNトラフィックをブロック

    このオプションを有効にすると、VPNトンネル外に送信しようとするクライアントデバイスからのすべてのトラフィックがブロックされ、クライアントDNS設定やVPN接続の中断、クライアントアプリのIP要求などによるVPNリークを効果的に防止します。

    この機能は[VPNキルスイッチ](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}とも呼ばれます。これは、データがウェブに漏れるのを防ぐために設計されています。ほとんどのVPNプロバイダは、VPN接続が切断された場合にコンピュータ、電話、またはタブレットをインターネットから自動的に切断するキルスイッチ機能を提供しています。GL.iNetルーターの非VPNトラフィックブロック機能は、次の6つのシナリオを含む、より多くの侵害方法に対処することができます：

    1. DNSリーク

    2. IPv6リーク
    
    3. WebRTCリーク　
    
    4. VPN接続の切断
    
    5. VPN開始前に起動したプログラム
    
    6. アプリケーション固有のリーク

### 2. WANアクセスを許可

このオプションを有効にすると、VPN接続中でもクライアントデバイスはWANにアクセスできます。例えば、上位サブネットのプリンターやNASなどにアクセスすることができます。

![vpn dashboard allow access wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

上の図のように、この機能を有効にすると、デバイスは上位サブネットのデバイス（例えばプリンターやNAS）にアクセスできます。

主なシナリオは、クライアントが上位サブネットのデバイスにアクセスできるようにすることですが、ルーターは上位サブネットとインターネットを区別できないため、クライアントデバイスが直接IPを通じてアクセスする場合、漏洩のリスクがあります。このため、このオプションと「非VPNトラフィックをブロック」は互いに排他的です。

### 3. GL.iNetのサービスがVPNを使用

このオプションを有効にすると、通常はリアルIPを使用する必要があるルーターのサービスはVPNを使用します。これには、GoodCloud、DDNS、rttyが含まれます。rttyには[GoodCloudページ](cloud.md#enable-goodcloud-on-router)の**リモートSSH**と**リモートWebアクセス**が含まれます。

主な目的は、VPNクライアントと[GoodCloud](cloud.md) / [DDNS](ddns.md)を同時に使用することです。GoodCloudを使用する場合は、このオプションをオフにすることをお勧めします。そうしないと、GoodCloudの安定性がVPNの状態に影響されます。DDNSを使用したい場合は、このオプションをオフにする必要があります。そうしないと、DDNSはVPNサーバーのIPアドレスを指します。

## VPNサーバー

最初は、両方のVPNサーバーが初期化されていません。「**今すぐセットアップ**」をクリックすると、それぞれ[OpenVPNサーバー](openvpn_server.md)と[WireGuardサーバー](wireguard_server.md)のページに移動します。

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

OpenVPNサーバーとWireGuardサーバーを起動した後。

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### OpenVPNサーバーのオプション

OpenVPNサーバーの歯車アイコンをクリックします。

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **リモートアクセスLANを許可**

    このオプションを有効にすると、VPNトンネルを通じてLANサブネット内のリソースにアクセスできます。

* **IPマスカレード**

    このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信する際に、ルーターが送信元IPアドレスを自分のアドレスに置き換えてからVPNトンネルに転送します。

    * **MTU**

    インスタンスに設定したMTUは、設定ファイル内のMTU項目を上書きします。

### OpenVPNサーバールート規則

OpenVPNサーバーのネットワークアイコンをクリックします。

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

カスタマイズされたルートモードでは、VPNクライアントは設定ファイルとサーバーから発行されたルーティング構成を無視します。任意のネットワークセグメントにアクセスする際にVPNが提供する暗号化トンネルを使用するかどうかは、手動で設定したルーティングルールによって決定されます。

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuardサーバーオプション

WireGuardサーバーの歯車アイコンをクリックします。

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **リモートアクセスLANを許可**

    このオプションを有効にすると、VPNトンネルを通じてLANサブネット内のリソースにアクセスできます。

* **IPマスカレード**

    このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信する際に、ルーターが送信元IPアドレスを自分のアドレスに置き換えてからVPNトンネルに転送します。

* **MTU**

    インスタンスに設定したMTUは、設定ファイル内のMTU項目を上書きします。

* **クライアント間通信**

    WireGuardクライアントは互いにデータにアクセスできます。これにより、リモートで自宅やオフィスの内部ネットワークデバイスにアクセスすることができます。WireGuardサーバーのデータアクセスは暗号化プロセスによりポート転送よりも安全で、一度接続されるとプロセスがより安定し迅速になります。

### WireGuardサーバールート規則

WireGuardサーバーのネットワークアイコンをクリックします。

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

カスタマイズされたルートモードでは、VPNクライアントは設定ファイルとサーバーから発行されたルーティング構成を無視します。任意のネットワークセグメントにアクセスする際にVPNが提供する暗号化トンネルを使用するかどうかは、手動で設定したルーティングルールによって決定されます。

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### VPNサーバーのグローバルオプション

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPNカスケード**: このオプションを有効にすると、このルーターでVPNサーバーとVPNクライアントの両方が動作している場合、VPNサーバーに接続されているクライアントはさらにVPNクライアントトンネルにルーティングされます。[VPNカスケードについての詳細はこちら](../tutorials/vpn_cascading.md)。

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。