# VPN Dashboard (Firmware v4.7 and earlier)

Web管理パネルにログインし、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboard ページでは、サーバーアドレス、トラフィック統計、クライアント仮想IP、接続ログなどのVPN接続情報を確認できるほか、VPNキルスイッチ、VPNポリシー、IPマスカレーディング、MTU、VPN Cascading などの詳細設定も行えます。

このページは、[VPNクライアント](#vpn-client) と [VPNサーバー](#vpn-server) の2つのセクションに分かれています。

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_initial.png){class="glboxshadow"}

## VPNクライアント {#vpn-client}

このページを初めて開いたときに OpenVPN と WireGuard の設定ファイルがまだない場合は、以下のように表示されます。**Set Up Now** をクリックすると、[OpenVPN Client](openvpn_client.md) または [WireGuard Client](wireguard_client.md) のページに移動し、VPN設定ファイルをアップロードできます。

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_setup.png){class="glboxshadow"}

アップロード後、設定は **Configuration File** 列に表示されます。複数の設定ファイルをアップロードしている場合は、ボックスをクリックして切り替えられます。

![configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_config.png){class="glboxshadow"}

### クライアントオプション

右側の歯車アイコンをクリックすると、OpenVPN または WireGuard のクライアントオプションを開けます。

![vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options.png){class="glboxshadow"}

OpenVPN Client Options は次のように表示されます。

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_ovpn.png){class="glboxshadow"}

WireGuard Client Options は次のように表示されます。

![wg client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: 有効にすると、VPN経由でこのルーターおよびそのLAN側デバイスへリモートアクセスできるようになります。VPNサーバー側では、このルーターのLANサブネットへのルートを通知している必要があります。

    たとえば下図のように、GL.iNet ルーターが VPN クライアントとして動作し、VPN トンネル経由で VPN サーバーに接続している場合、このオプションを有効にすると VPN サーバー側のデバイス（例: NAS）から GL.iNet ルーター本体とそのLAN側デバイスへアクセスできるようになります。そのためには、VPNサーバー側に GL.iNet ルーターのLANサブネットへ到達するためのルーティングルールを追加する必要があります。

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: 有効にすると、LAN クライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモートピアがLANサブネットを認識しているサイトツーサイト構成の場合にのみ無効にしてください。

- **MTU**: Maximum Transmission Unit の略です。このオプション設定ではVPNトンネルの MTU をカスタマイズでき、設定ファイル内で定義された値を上書きします。

### プロキシモード

VPN接続の既定のプロキシモードは **Global Proxy** です。右上のボックスをクリックすると、別のプロキシモードへ切り替えられます。

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_proxy.png){class="glboxshadow"}

利用できるプロキシモードは **Global Proxy**、**Policy Mode**、**Route Mode** の3種類です。

1. Global Proxy

    このモードでは、すべてのトラフィックがVPN経由でルーティングされます。有効にできるVPNクライアントインスタンスは1つだけです。

2. Policy Mode

    このモードは、さらに3つのポリシーに分かれます。

    - Based on the Target Domain or IP.

        このモードでは、IPアドレスまたはドメイン名で識別される特定のWebサイト向けトラフィックだけがVPN経由でルーティングされます。有効にできるVPNクライアントインスタンスは1つだけです。

    - Based on the Client Device.

        このモードでは、MACアドレスで識別される特定のLANデバイスのトラフィックだけがVPN経由でルーティングされます。有効にできるVPNクライアントインスタンスは1つだけです。

    - Based on the VLAN.

        このモードでは、特定の VLAN のトラフィックだけがVPN経由でルーティングされます。有効にできるVPNクライアントインスタンスは1つだけです。

3. Route Mode

    - Auto Detect

        各VPNクライアント設定ファイルで定義されたルーティングルール、またはVPNサーバーから配布されたルーティングルールが使用されます。

    - Customize Routing Rules

        各VPNクライアントインスタンスごとに、ルーティングルールを手動で設定できます。

### グローバルオプション

右上の **Global Options** をクリックすると、VPNクライアントの詳細設定を行えます。

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: 有効にすると、すべてのインターネットトラフィックはVPNトンネルのみを通過するよう強制され、ローカルISPのWANなど他のインターフェース経由ではルーティングされません。VPN接続が予期せず切断された場合も、通常のWANへのフォールバックを防ぐため、すべてのインターネットトラフィックが完全にブロックされます。これにより、VPN障害やクライアントのDNS設定ミスなどに起因するVPNリークを防げます。

    この機能は [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"} とも呼ばれます。ユーザーデータがオンライン上に漏れるのを防ぐ機能です。一般的な Kill Switch は、VPN接続が失敗した際にインターネット接続を自動的に遮断します。GL.iNet ルーターの Block Non-VPN Traffic 機能は、より広範なリーク保護を提供し、次のシナリオに対応します。

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applications Launched Before VPN Establishment

    6. Per-Application Traffic Leaks

- **Allow Access WAN**: 有効にすると、VPN接続中でもローカルクライアントデバイスは WAN 側のサービス（上位サブネット内のプリンター、NAS など）へアクセスできます。

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    上図のように、この機能を有効にすると、ローカルデバイスから上位サブネット内のプリンターやNASなどへアクセスできます。

    このオプションは主に、クライアントが上位サブネット内の機器へアクセスできるようにするためのものです。ただし、ルーターは上位サブネット向けトラフィックと通常のインターネットトラフィックを区別できません。クライアントデバイスがパブリックIPへ直接アクセスした場合は、トラフィックリークの可能性があります。そのため、**Allow Access WAN** と **Block Non-VPN Traffic** は相互排他的で、同時に有効化できません。

- **Services From GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスはVPNトンネル経由でパケットを送信します。これらのサービスは通常デバイスの実IPアドレスを必要とするため、このオプションはデフォルトで無効です。

## VPNサーバー {#vpn-server}

ルーターが OpenVPN サーバーまたは WireGuard サーバーとしてまだ設定されたことがない場合、ページは以下のように表示されます。**Set Up Now** をクリックすると、**OpenVPN Server** または **WireGuard Server** ページに移動し、VPNサーバーを初期設定できます。

![vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_setup.png){class="glboxshadow"}

OpenVPN Server または WireGuard Server を有効にすると、ページには次のようにサーバー状態が表示されます。

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_connected.png){class="glboxshadow"}

### サーバーオプション

右側の歯車アイコンをクリックすると、OpenVPN または WireGuard のサーバーオプションを開けます。

![vpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options.png){class="glboxshadow"}

OpenVPN Server Options は次のように表示されます。

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_ovpn.png){class="glboxshadow"}

WireGuard Server Options は次のように表示されます。

![wg server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: 有効にすると、サーバー側LANサブネット内のリソースへVPNトンネル経由でアクセスできるようになります。

* **IP Masquerading**: 有効にすると、LAN クライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモートピアがLANサブネットを認識しているサイトツーサイト構成の場合にのみ無効にしてください。

* **MTU**: Maximum Transmission Unit の略です。ここで設定したトンネルの MTU 値は、設定ファイル内の MTU 設定を上書きします。

* **Client to Client**: 有効にすると、このサーバーに接続した VPN クライアント同士がVPNトンネルIP経由で相互にアクセスできます。さらに互いのLANサブネットにもアクセスさせたい場合は、VPNサーバー側でそれらのリモートLANサブネットへのルートを通知する必要があります。

### サーバールートルール

右側のルートアイコンをクリックすると、必要に応じて OpenVPN または WireGuard のルートルールをカスタマイズできます。

![server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule.png){class="glboxshadow"}

OpenVPN Server Route Rule は次のように表示されます。**Add Route Rule** をクリックし、**Target Address** と **Gateway** を入力して、緑色のチェックアイコンをクリックして適用します。

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

WireGuard Server Route Rule は次のように表示されます。**Add Route Rule** をクリックし、**Target Address** と **Gateway** を入力して、緑色のチェックアイコンをクリックして適用します。

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Note**: カスタムルートモードでは、VPNクライアントは設定ファイルおよびサーバーから配布されたルーティング設定を無視します。任意のネットワークセグメントへアクセスする際にVPN暗号化トンネルを使用するかどうかは、手動で設定したルートルールによって決まります。

### グローバルオプション

右上の **Global Options** をクリックすると、VPNサーバーの詳細設定を行えます。

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: 有効にすると、このルーターが VPN サーバーと VPN クライアントを同時に実行している場合、このルーターのVPNサーバーに接続したリモートVPNクライアントのトラフィックは、このルーターがVPNクライアントとして使用している上流VPNトンネル経由でルーティングされます。[VPN Cascading の詳細はこちら](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md)。

---

まだご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
