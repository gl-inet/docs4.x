# VPN Dashboard

ウェブ管理パネルにアクセスし、左側の「VPN」→「VPN Dashboard」を選択します。

VPNダッシュボードは、VPNの状態や設定を行うためのページです。

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

OpenVPNとWireGuardについては、初期状態では設定項目がありませんので、**Set Up Now**をクリックして、該当するページに移動し、設定を行う必要があります。

![glinet vpn dashboard](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_2.png){class="glboxshadow"}

### プロキシモード

![vpn proxy](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

1. グローバルプロクシ

    すべてのトラフィックはVPNを経由します。VPNクライアントインスタンスは1台のみ起動可能です。

2. ポリシーモード

    - 対象ドメインまたはIPに基づいています。
    
        このモードでは、IPアドレスまたはドメイン名で定義された特定のWebサイトのトラフィックのみがVPNを通過します。VPNクライアントインスタンスは1つだけ有効です。

    - クライアントデバイスに基づています

        このモードでは、MACアドレスで定義された特定のローカルクライアントデバイスのトラフィックのみがVPNを通過する。VPNクライアントインスタンスは1つだけアクティブにすることができます。

    - VLANに基づています。

        このモードでは、特定のVLANのトラフィックのみがVPNを通過することができます。VPNクライアントインスタンスは1つだけ起動することができます。
3.ルートモード

    -自動検出

       各VPNクライアントの設定ファイルに定義されている、またはVPNサーバーから発行されたルーティングルールが使用されます。
    
    - ルーティングルールのカスタマイズ

        VPNクライアントインスタンスごとに、ルーティングルールを手動で設定することができます。
### グローバルオプション

Click **グローバルオプション** will popup a global options dialog.

![global options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/global_options.png){class="glboxshadow"}

1. 非VP.Nトラフィックのブロック

    このオプションを有効にすると、VPNトンネルから送信しようとするクライアントデバイスからのすべてのトラフィックがブロックされ、クライアントのDNS設定、VPN接続の切断、IPによるクライアントアプリの要求などによるVPNリークを効果的に防止することができます。

2. WANへのアクセスを許可する

    このオプションを有効にすると、VPN接続中も、クライアント端末はWANにアクセスすることができます。

3. GL.iNetのサービスではVPNを使用しない

    このオプションを有効にすると、通常、実IPの使用を必要とするルーター上のサービスは、VPNを使用しません。GoodCloud、DDNS、rttyを含んでいます。

##VPNサーバー

![vpn dashboard vpn server](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

### OpenVPN Server Options

OpenVPNサーバーのcog iconをクリックします。

![openvpn server options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **リモートアクセスLANを許可する：** このオプションを有効にすると、LANサブネット内のリソースは、VPNトンネルを介してアクセスすることができます。

* **IP　マスカレード。:** このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信するとき、ルーターはソースIPアドレスを自分のアドレスに置き換えてから、VPNトンネルに転送します。

* **MTU:** インスタンスに設定したMTUは、設定ファイルのMTUの項目を上書きします。

### OpenVPNサーバーのルートルール

OpenVPNサーバーのネットワークアイコンをクリックします。

カスタマイズルーツモードでは、VPNクライアントは、サーバーから発行された設定ファイルやルーティングの設定を無視します。任意のネットワーク・セグメントにアクセスする際に、VPNが提供する暗号化トンネルを使用するかどうかは、手動で設定したルーティング・ルールによって決定されます。

![openvpn server route rule](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuardサーバーのオプション

![wireguard server options](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **リモートアクセスLANを許可する:** このオプションを有効にすると、LANサブネット内のリソースは、VPNトンネルを介してアクセスすることができます。

* **IP　マスカレード:** このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信するとき、ルーターはソースIPアドレスを自分のアドレスに置き換えてから、VPNトンネルに転送します。

* **MTU:** インスタンスに設定したMTUは、設定ファイルのMTUの項目を上書きします。

### WireGuardサーバーのルートルール

WireGuardサーバーのネットワークアイコンをクリックします。

カスタマイズルーツモードでは、VPNクライアントは、サーバーから発行された設定ファイルやルーティングの設定を無視します。任意のネットワーク・セグメントにアクセスする際に、VPNが提供する暗号化トンネルを使用するかどうかは、手動で設定したルーティング・ルールによって決定されます。

![wireguard server route rule](https://static.gl-inet.com/docs/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}
