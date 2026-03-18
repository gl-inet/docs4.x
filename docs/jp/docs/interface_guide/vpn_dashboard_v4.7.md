# VPNダッシュボード（firmware v4.7で前）

Web管理パネルにアクセスし、左側 -> VPN -> VPNダッシュボード

VPNダッシュボードページはVPNの状態と設定用です。2つのセクションがあり、VPNクライアントとVPNサーバーがあります。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPNクライアント

最も初はOpenVPNとWireGuardの設定がありません。「今すぐ設定」をクリックすると、それぞれOpenVPNクライアントとWireGuardクライアントページに移動します。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

設定が完たすると、設定ファイル列で設定ファイルを選択できます。

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### VPNクライアントオプション

OpenVPNまたはWireGuardの歯車アイコンをクリックします。

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

OpenVPNクライアントオプション。

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

WireGuardクライアントオプション。

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* リモートアクセスLANを許可

    このオプションを有効にすると、ルーターに接続されたデバイスがVPNサーバー側のLANにアクセスできるようになります。これにはVPNサーバー側で適切な設定も必要です。

    例えば、下の画像では、このオプションを有効にすると、「あなたのデバイス」が「NAS」にアクセスすることが許可されますが、「VPNサーバー」がそのサブネット内でNASへのアクセスを許可する必要があります。

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* IPマスカレーディング

    このオプションを有効にすると、LAN上のクライアントデバイスがIPパケットを送信するとき、ルーターはソースIPアドレスをから分のアドレスに置き換えてVPNトンネエルに転送します。

* MTU

    最大転送単位を表します。インスタンスに設定したMTUは設定ファイルのMTUアイテムをオーバーライドします。

### プロキシモード
