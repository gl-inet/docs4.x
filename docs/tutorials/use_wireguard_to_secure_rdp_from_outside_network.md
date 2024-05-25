# 外部ネットワークからRDPを保護するためにWireGuardを使用

外部ネットワークからPCにリモートアクセスする必要がある場合やその逆の場合、最も安全な方法は自分のWireGuardトンネルを使用することです。これにより、ポートフォワーディングを使用してパブリックIPアドレス経由でアクセスするよりも高いセキュリティが提供されます。トンネルを設定した後、Windowsの**リモートデスクトップアプリ**を使用して、どこからでもPCにアクセスできます。

## トポロジー

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## 自分のWireGuardネットワークを設定

WireGuardトンネルをRDPに使用する前に、WireGuardサーバーとWireGuardクライアントを設定する必要があります。2台のGL.iNetルーターを使用してトンネルを設定できます。 [2台のGL.iNetルーターを使用してホームWireGuardサーバーを構築](build_your_own_wireguard_home_server_with_two_glinet_routers.md)。

## サーバーがクライアントのLAN側にアクセスできるようにする

サーバーとクライアントの両方から相互アクセスを行う場合、まずサーバーがクライアントのLAN側にアクセスできるようにする必要があります。[クライアントLANへのアクセス](wireguard_server_access_to_client_lan_side.md)。

## クライアントがサーバーのLAN側にアクセスできるようにする

その後、サーバーとクライアントの両方のVPNダッシュボードで「リモートLANアクセスを許可」を有効にしてください。詳細については、クライアント側は[こちら](../interface_guide/vpn_dashboard.md/#vpn-clinet-options)、サーバー側は[こちら](../interface_guide/vpn_dashboard.md/#wireguard-server-options)をクリックしてください。

## サーバー側PCをアクセス可能にする

### サーバー側PC

サーバーLAN側のIP **192.168.29.123**に接続されているPCにアクセスする場合、そのPCのWindows設定に移動し、**リモートデスクトップ**をクリックしてください。

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

これをオンにします

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

**確認**をクリック

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## クライアント側PCでリモートアプリを起動

### クライアント側PC

**リモートデスクトップ接続アプリ**を検索

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

起動して、サーバー側PCのIP **192.168.29.123**をボックスに入力します。

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

サーバー側PCの資格情報を入力します。

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

これで、サーバー側PCをリモートで制御できます。

逆の操作を行いたい場合は、サーバーPCとクライアントラップトップの手順を逆にしてください。
