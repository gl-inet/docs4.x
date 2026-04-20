# VPN Dashboard (Firmware v4.7 and earlier)

Web管理パネルにログインし、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboard ページでは、VPNの状態確認と設定を行います。セクションは [VPNクライアント](#vpn-client) と [VPNサーバー](#vpn-server) の2つです。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPNクライアント {#vpn-client}

初期状態では OpenVPN と WireGuard の設定はありません。**Set Up Now** をクリックすると、それぞれ [OpenVPN Client](openvpn_client.md) と [WireGuard Client](wireguard_client.md) のページへ移動します。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

設定が完了すると、Configuration file 列で設定ファイルを選択できます。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### VPNクライアントオプション {#vpn-client-options}

OpenVPN または WireGuard の歯車アイコンをクリックします。

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

OpenVPN client のオプション。

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

WireGuard client のオプション。

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* Allow Remote Access LAN

    このオプションを有効にすると、ルーター配下に接続されたデバイスが VPN Server 側のLANへアクセスできるようになります。VPN Server 側でも適切な設定が必要です。

    たとえば下の図では、このオプションを有効にすると *Your Device* から *NAS* へアクセスできるようになります。ただし、VPN Server 側でも、そのサブネット内の NAS へのアクセスを許可している必要があります。

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* IP Masquerading

    このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信する際、ルーターが送信元IPアドレスを自分自身のアドレスに書き換えてからVPNトンネルへ転送します。

* MTU

    Maximum Transmission Unit の略です。ここで設定したMTUは、インスタンスの設定ファイル内にある MTU 項目を上書きします。

### プロキシモード

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

上図では現在のプロキシモードは Global Proxy です。Global Proxy をクリックすると、別のプロキシモードへ切り替えられます。種類は **Global Proxy**、**Policy Mode**、**Route Mode** の3つです。

1. Global Proxy

    すべてのトラフィックがVPN経由になります。有効にできるVPNクライアントインスタンスは1つだけです。

2. Policy Mode

    1. Based on the target domain or IP.

        このモードでは、IPアドレスまたはドメイン名で定義した特定のWebサイト向けのトラフィックだけがVPNを通ります。有効にできるVPNクライアントインスタンスは1つだけです。

    2. Based on the client device.

        このモードでは、MACアドレスで定義した特定のローカルクライアントデバイスのトラフィックだけがVPNを通ります。有効にできるVPNクライアントインスタンスは1つだけです。

    3. Based on the VLAN.

        このモードでは、特定のVLANのトラフィックだけがVPNを通ります。有効にできるVPNクライアントインスタンスは1つだけです。

3. Route Mode

    1. Auto detect

        各VPNクライアント設定ファイルで定義されたルーティングルール、またはVPNサーバーから配布されたルーティング設定が使用されます。

    2. Customize routing rules

        各VPNクライアントインスタンスごとに、ルーティングルールを手動で設定できます。

### VPNクライアントのグローバルオプション

**Global Options** をクリックすると、グローバルオプションのダイアログが表示されます。

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Block Non-VPN Traffic

    このオプションを有効にすると、VPNトンネルをバイパスしようとするすべてのクライアントデバイスのトラフィックがブロックされます。これにより、クライアントのDNS設定、VPN接続の切断、IP直接指定のアプリ通信などによるVPNリークを効果的に防げます。

    この機能は [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"} とも呼ばれます。データがインターネットへ漏れるのを防ぐための機能です。多くのVPNプロバイダーは、VPN接続が切断された場合にコンピューター、スマートフォン、タブレットを自動的にインターネットから切断する Kill Switch 機能を提供しています。GL.iNet ルーターの Block Non-VPN Traffic 機能は、さらに多くの漏えい経路に対応しており、以下の6つのシナリオを防ぎます。

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. Dropped VPN Connection

    5. Programs Started Before VPN

    6. Application Specific Leaks

2. Allow Access WAN

    このオプションを有効にすると、VPN接続中でもクライアントデバイスは WAN にアクセスできます。たとえば上位サブネット内のプリンターや NAS にアクセスできます。

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    上図のように、この機能をオンにすると、デバイスは上流サブネット内のプリンターや NAS などの機器にアクセスできます。

    主な用途は、クライアントが上流サブネット内の機器へアクセスできるようにすることです。ただし、ルーターは上流サブネットとインターネットを区別できないため、クライアントデバイスのトラフィックがIPで直接アクセスされた場合はリークのリスクがあります。そのため、このオプションと Block Non-VPN Traffic は相互排他的です。

3. Services From GL.iNet Use VPN

    このオプションを有効にすると、通常は実IPアドレスが必要なルーター上のサービスもVPNを使用します。対象は GoodCloud、DDNS、rtty です。rtty には [GoodCloud ページ](cloud.md#enable-goodcloud) の **Remote SSH** と **Remote Web Access** が含まれます。

    主な目的は、VPN Client と [GoodCloud](cloud.md) / [DDNS](ddns.md) を同時に使えるようにすることです。GoodCloud を使う場合は、このオプションをオフにすることを推奨します。オンのままだと GoodCloud の安定性がVPNの状態に影響されます。DDNS を使う場合は、このオプションを必ずオフにしてください。オンのままだと DDNS は VPN Server のIPアドレスを指すようになります。

## VPNサーバー {#vpn-server}

初期状態では、どちらの VPN Server もまだ初期化されていません。**Set Up Now** をクリックすると、それぞれ [OpenVPN Server](openvpn_server.md) と [WireGuard Server](wireguard_server.md) のページへ移動します。

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

OpenVPN Server と WireGuard Server を起動した後の状態です。

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### OpenVPNサーバーオプション

OpenVPN server の歯車アイコンをクリックします。

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    このオプションを有効にすると、LANサブネット内のリソースへVPNトンネル経由でアクセスできるようになります。

* **IP Masquerading**

    このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信する際、ルーターが送信元IPアドレスを自分自身のアドレスに書き換えてからVPNトンネルへ転送します。

* **MTU**

    ここで設定したMTUは、インスタンスの設定ファイル内にある MTU 項目を上書きします。

### OpenVPNサーバーのルートルール

OpenVPN server のネットワークアイコンをクリックします。

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

Customize routes mode では、VPNクライアントは設定ファイルおよびサーバーから配布されたルーティング設定を無視します。任意のネットワークセグメントにアクセスする際に、VPNが提供する暗号化トンネルを使うかどうかは、手動で設定したルーティングルールによって決まります。

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuardサーバーオプション

WireGuard server の歯車アイコンをクリックします。

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    このオプションを有効にすると、LANサブネット内のリソースへVPNトンネル経由でアクセスできるようになります。

* **IP Masquerading**

    このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信する際、ルーターが送信元IPアドレスを自分自身のアドレスに書き換えてからVPNトンネルへ転送します。

* **MTU**

    ここで設定したMTUは、インスタンスの設定ファイル内にある MTU 項目を上書きします。

* **Client to Client**

    WireGuard クライアント同士が相互に通信できるようになります。拠点間接続ではなく、外出先から自宅やオフィスの内部ネットワーク機器にアクセスしたい場合に便利です。また、暗号化処理により、ポートフォワーディングより安全で、接続後の動作もより安定して高速になります。

### WireGuardサーバーのルートルール

WireGuard server のネットワークアイコンをクリックします。

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

Customize routes mode では、VPNクライアントは設定ファイルおよびサーバーから配布されたルーティング設定を無視します。任意のネットワークセグメントにアクセスする際に、VPNが提供する暗号化トンネルを使うかどうかは、手動で設定したルーティングルールによって決まります。

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### VPNサーバーのグローバルオプション

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPN Cascading**: このオプションを有効にすると、このルーター上で VPN server と VPN Client の両方を実行している場合に、VPN server へ接続したクライアントのトラフィックはさらに VPN client トンネルへルーティングされます。[VPN Cascading の詳細はこちら](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md)。

---

まだご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
