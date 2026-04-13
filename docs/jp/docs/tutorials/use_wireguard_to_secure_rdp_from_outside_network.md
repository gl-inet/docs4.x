# WireGuardを使って外部ネットワークからのRDPを保護する

外部ネットワークからPCへリモートアクセスしたい場合や、その逆を行いたい場合があります。最も安全な方法は、自分専用の WireGuard トンネルを使ってアクセスすることです。ポートフォワーディングを使ってパブリックIPアドレス経由でアクセスするよりも安全性が高くなります。トンネルを設定すれば、Windows の **Remote Desktop App** を使って、どこからでもPCにアクセスできます。

## トポロジー

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## 独自のWireGuardネットワークを設定する

RDP に WireGuard トンネルを使う前に、WireGuard サーバーと WireGuard クライアントを設定する必要があります。2台の GL.iNet ルーターを使ってトンネルを構築できます。[2台のGL.iNetルーターで独自のWireGuardホームサーバーを構築する方法](build_your_own_wireguard_home_server_with_two_glinet_routers.md)をご覧ください。

## サーバーからクライアントLAN側へアクセスできるようにする

サーバーとクライアントの双方から相互アクセスしたい場合は、まずサーバーからクライアントLAN側へアクセスできるようにする必要があります。[サーバー側からクライアントLANへアクセスする方法](wireguard_server_access_to_client_lan_side.md)をご覧ください。

## クライアントからサーバーLAN側へアクセスできるようにする
その後、サーバー側とクライアント側の両方の **VPN Dashboard** で “Allow Remote LAN Access” を有効にしてください。詳細は、クライアント側は[こちら](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options)、サーバー側は[こちら](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options)をご覧ください。

## サーバー側PCをアクセス可能にする

### サーバー側PC

サーバーLAN側に接続されているPC（IPアドレス **192.168.29.123**）へアクセスしたい場合は、そのPCの Windows の設定を開き、**Remote Desktop** をクリックします。

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

オンにします。

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

**Confirm** をクリックします。

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## クライアント側ノートPCでリモートアプリを起動する

### クライアント側ノートPC

**Remote Desktop Connection App** を検索します。

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

起動し、入力欄にサーバー側PCのIPアドレス **192.168.29.123** を入力します。

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

サーバー側PCの認証情報を入力します。

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

すぐにサーバー側PCをリモート操作できるようになります。

逆方向に行いたい場合は、サーバー側PCとクライアント側ノートPCの手順を入れ替えてください。
