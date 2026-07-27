# Fortify (GL-MT6000) ユーザーガイド

## 製品概要

Fortify (GL-MT6000) は、GL.iNet と ExpressVPN が共同でリリースした共同ブランドの Wi-Fi 6 ルーターです。各製品には、1 年間の ExpressVPN 無料サブスクリプションが付属しています。ユーザーはルーターの Web Admin Panel から直接サブスクリプションを引き換え、アカウントを紐付けることができます。有効化後、ルーターを通過するすべてのトラフィックは ExpressVPN の高速ネットワークと強力な暗号化を利用し、ネットワーク接続全体とオンラインプライバシーを保護します。

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Fortify のセットアップ

### 1. 電源を入れる

2 ピース構成の電源アダプターを組み立てます。Fortify ルーターに接続し、コンセントに差し込みます。ルーターは自動的に起動します。

### 2. デバイスを接続する

パソコン、ノートパソコン、スマートフォンなどのデバイスを Wi-Fi または Ethernet でルーターに接続します。

- Ethernet

    Ethernet ケーブルを使用して、デバイスをルーターの LAN ポートに接続します。

- Wi-Fi

    デバイスで Settings -> WLAN を開き、利用可能なネットワーク一覧からルーターの Wi-Fi ネットワーク名を選択して、パスワードを入力します。初期ネットワーク名とパスワードはルーターのラベルに印字されています。

### 3. Web Admin Panel にログインする

Web ブラウザーを開き、アドレスバーに `192.168.8.1` と入力してログインします。右上で言語を選択し、管理者パスワードを設定して **Next** をクリックします。パスワードは 10～63 文字で、大文字、小文字、数字、特殊記号のうち少なくとも 2 種類を含める必要があります。

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Wi-Fi を設定します。Wi-Fi 情報を変更した場合は、更新後の認証情報を使用してデバイスをルーターの Wi-Fi に再接続する必要があります。

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. インターネットを設定する

**Note:** 以下の手順は、GL.iNet Web Admin Panel からルーターを設定する場合に適用されます。[GL.iNet アプリ](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}を使用する場合は、アプリをダウンロードして画面の指示に従ってください。

Fortify は、Ethernet、Repeater、Tethering、Cellular のいずれかの対応接続方式で設定できます。[Multi-WAN](../../interface_guide/multi-wan.md) を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Fortify ルーターの WAN ポートとモデムなどの上位機器を Ethernet ケーブルで接続します。

    インターネットに正常に接続されると、ルーターの LED が白色点灯になります。

    詳細な手順は [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Web Admin Panel で INTERNET -> Repeater セクションに移動し、**Connect** をクリックします。
    2. 利用可能なネットワークから Wi-Fi を選択します。
    3. パスワードを入力し、**Apply** をクリックします。

    インターネットに正常に接続されると、ルーターの LED が白色点灯になります。

    詳細な手順は [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. USB ケーブルでスマートフォンをルーターの USB ポートに接続します。
    2. スマートフォンで Settings を開き、USB Tethering を有効にします。iPhone の場合は、このデバイスを信頼し、Personal Hotspot を有効にします。
    3. Web Admin Panel で INTERNET -> Tethering セクションに移動し、**Connect** をクリックします。

    インターネットに正常に接続されると、ルーターの LED が白色点灯になります。

    詳細な手順は [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    cellular USB モデムをルーターの USB ポートに接続します。USB モデムのインターネット接続を、接続中のすべてのデバイスで共有できます。

    インターネットに正常に接続されると、ルーターの LED が白色点灯になります。

    詳細な手順は [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) を参照してください。

---

以下は Fortify の Web Admin Panel にある機能の概要です。

## Wireless

Wireless ページでは、Main Network、Guest Network、IoT Network など Fortify の Wi-Fi ネットワークを設定できます。各ネットワークは 2.4 GHz と 5 GHz の両方に対応しています。

Wireless の設定については [Wireless](../../interface_guide/wireless_v4.9.md) を参照してください。

## Clients

Clients ページには、接続中デバイスの名前、接続タイプ、IP アドレス、MAC アドレス、ダウンロード/アップロード速度、トラフィックが表示されます。また、特定のクライアントをワンクリックでブロックしたり、その他の操作を実行したりできます。

詳細は [Clients](../../interface_guide/clients.md) を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、GL.iNet ルーターへリモートアクセスし、管理するための簡単な方法を提供します。

    詳細は [GoodCloud](../../interface_guide/cloud.md) を参照してください。

=== "AstroWarp"

    AstroWarp は GL.iNet ルーターでスムーズなリモートネットワークを構築するための機能です。トラフィック難読化を内蔵した AmneziaWG プロトコルを採用し、安定した安全なリモートアクセスを提供します。

    詳細は [AstroWarp](../../interface_guide/astrowarp.md) を参照してください。

## VPN

VPN (virtual private network) は、ローカルデバイスと VPN サーバーの間に安全で暗号化されたトラフィックトンネルを確立します。VPN クライアントのプライバシーとセキュリティを強化し、リモート VPN サーバーネットワークへのアクセスを可能にします。

Fortify は [ExpressVPN](https://www.expressvpn.com/){target="_blank"} と統合されており、ExpressVPN 接続を短時間で有効化できます。各 Fortify デバイスには 1 年間の ExpressVPN 無料サブスクリプションが付属し、Web Admin Panel から引き換えとアカウント紐付けができます。

無料サブスクリプションの引き換えと VPN トンネルの設定については [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md) を参照してください。

OpenVPN サーバーの設定については [OpenVPN Server](../../interface_guide/openvpn_server.md) を参照してください。

WireGuard サーバーの設定については [WireGuard Server](../../interface_guide/wireguard_server.md) を参照してください。

## ネットワーク

=== "Multi-WAN"

    Multi-WAN は、cellular、repeater、ethernet など複数のインターネット接続を同時に使用できる機能です。現在の接続に障害が発生すると、ルーターは自動的に別の接続へ切り替えます。

    詳細は [Multi-WAN](../../interface_guide/multi-wan.md) を参照してください。

=== "LAN"

    LAN は、メイン Wi-Fi または Ethernet ケーブルで接続したときにデバイスが参加するローカルネットワークです。LAN ページでは Basic Settings、DHCP Server Settings、Address Reservation を設定できます。

    詳細は [LAN](../../interface_guide/lan.md) を参照してください。

=== "Guest Network"

    Guest Network は来客用の専用 Wi-Fi ネットワークを作成します。メインネットワークから分離され、`192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` などのプライベート IPv4 範囲でゲストサブネットを設定できます。

    詳細は [Guest Network](../../interface_guide/guest_network.md) を参照してください。

=== "IoT Network"

    IoT Network は IoT デバイス用の専用 Wi-Fi ネットワークを作成します。メインネットワークから分離することで、互換性とセキュリティを向上させます。

    詳細は [IoT Network](../../interface_guide/iot_network.md) を参照してください。

<br>

=== "DNS"

    DNS 設定は、ドメイン名を IP アドレスに変換する方法を制御します。上位機器から自動取得した DNS サーバーを使用したり、カスタム DNS を設定したり、DNS 優先順位を設定したりできます。

    詳細は [DNS](../../interface_guide/dns.md) を参照してください。

=== "Ethernet Port"

    Ethernet Port では、WAN/LAN のポートの役割を管理し、MAC アドレスやネゴシエート速度などのポート詳細を確認できます。

    詳細は [Ethernet Port](../../interface_guide/ethernet_port.md) を参照してください。

=== "IPv6"

    IPv6 は Internet Protocol の最新バージョンで、IPv4 よりはるかに大きなアドレス空間を提供します。

    詳細は [IPV6](../../interface_guide/network_mode.md) を参照してください。

=== "IGMP Snooping"

    IGMP Snooping は、Ethernet スイッチで multicast トラフィックを管理および制御するためのネットワーク最適化技術です。

    詳細は [IGMP Snooping](../../interface_guide/igmp_snooping.md) を参照してください。

<br>

=== "Network Mode"

    Network Mode は、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する設定です。

    設定方法は [Network Mode](../../interface_guide/network_mode.md) を参照してください。

=== "Drop-in Gateway"

    Drop-in Gateway は、メインルーターに AdGuard Home、暗号化 DNS、VPN などの機能を追加します。

    設定方法は [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md) を参照してください。

=== "Network Acceleration"

    Network Acceleration は CPU 負荷を軽減し、パケット転送を高速化できます。

    設定方法は [Network Acceleration](../../interface_guide/network_acceleration.md) を参照してください。

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) はパケットのペイロードを分析し、署名データベースとの照合によりアプリケーションや Web サイトをより正確に識別します。GL.iNet の DPI 機能は [Netify](https://www.netify.ai/){target="_blank"} と統合されています。

    詳細は [DPI Engine](../../interface_guide/dpi_engine.md) を参照してください。

=== "Data Statistics"

    Data Statistics は、アプリケーション別にネットワーク使用状況を分類して可視化し、リアルタイムおよび履歴トラフィックの監視に役立ちます。

    詳細は [Data Statistics](../../interface_guide/data_statistics.md) を参照してください。

=== "Content Filter"

    Content Filter は DPI ベースの分類により、有害または悪意のある Web サイトを自動的にブロックします。

    詳細は [Content Filter](../../interface_guide/content_filter.md) を参照してください。

<br>

=== "QoS"

    QoS は、ネットワーク混雑時にビデオ通話やゲームなど重要な通信を優先します。これはローカルクライアントのトラフィックと VPN Client トンネルトラフィックに適用されますが、ルーターが VPN Server として受信するトラフィックには適用されません。

    詳細は [QoS](../../interface_guide/qos.md) を参照してください。

=== "SQM"

    SQM (Smart Queue Management) はネットワークトラフィックを管理し、遅延と bufferbloat を低減します。

    詳細は [SQM](../../interface_guide/sqm.md) を参照してください。

=== "Parental Control"

    Parental Control は、子どものデバイス管理、利用時間の制限、特定コンテンツへのアクセス制限に使用します。

    詳細は [Parental Control](../../interface_guide/parental_control_v4.9.md) を参照してください。

## セキュリティ

=== "Port forwarding"

    Port forwarding は、インターネット上のリモートサーバーやデバイスがプライベートネットワーク内のデバイスへアクセスできるようにします。

    詳細は [Port Forwarding](../../interface_guide/port_forwarding.md) を参照してください。

=== "ACL"

    ACL (Access Control List) では、接続プロトコル、デバイスアドレス、ポートに基づいてネットワークトラフィックを制御するルールを作成できます。複数の ACL ルールが競合する場合、優先度の高いルールが適用されます。

    詳細は [ACL](../../interface_guide/acl.md) を参照してください。

=== "Admin Access"

    Admin Access では、Access Control、Remote Access Control、Open Ports on Router など、ネットワークとルーターを不正アクセスから保護するための設定を行えます。

    詳細は [Admin Access](../../interface_guide/admin_access.md) を参照してください。

=== "NAT Mode"

    NAT Mode では Full Cone NAT と SIP ALG の有効/無効を切り替えられます。

    詳細は [NAT Mode](../../interface_guide/nat_settings.md) を参照してください。

## アプリケーション

=== "Plug-ins"

    Plug-ins は、既存のシステムに特定の機能を追加するソフトウェアコンポーネントです。

    詳細は [Plug-ins](../../interface_guide/plugins.md) を参照してください。

=== "Dynamic DNS"

    Dynamic DNS (DDNS) は、ドメインに関連付けられた IP アドレスを自動的かつリアルタイムに検出して更新します。

    詳細は [Dynamic DNS](../../interface_guide/ddns.md) を参照してください。

=== "Network Storage"

    Network Storage は、複数のユーザーやデバイスがネットワーク経由でアクセスし、ファイルを共有できる集中型ストレージです。

    詳細は [Network Storage](../../interface_guide/network_storage.md) を参照してください。

=== "AdGuard Home"

    AdGuard Home は DNS サーバーとして動作し、ネットワーク全体で広告やトラッカーなど不要なコンテンツをフィルタリングします。

    詳細は [AdGuard Home](../../interface_guide/adguardhome.md) を参照してください。

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} は、子どものデジタル環境を保護するのに役立ちます。GL.iNet と Bark のパートナーシップの一環として、Fortify (GL-MT6000) では Bark Home プランを無料で利用できます。

    詳細は [Bark](../../interface_guide/bark.md) を参照してください。

=== "Tailscale"

    Tailscale は、自分のデバイスやアプリケーションへどこからでも安全にアクセスできる VPN サービスです。Fortify (GL-MT6000) は Tailscale 仮想ネットワークに参加し、WAN および LAN リソースへリモートアクセスできます。

    詳細は [Tailscale](../../interface_guide/tailscale.md) を参照してください。

=== "ZeroTier"

    ZeroTier は、インターネット経由で安全な仮想ネットワークを作成し、デバイスを同じローカルネットワーク上にあるかのように接続します。

    詳細は [ZeroTier](../../interface_guide/zerotier.md) を参照してください。

=== "Tor"

    Tor は匿名通信を可能にする無料のオープンソースソフトウェアで、よりプライベートなインターネット利用を支援します。

    詳細は [Tor](../../interface_guide/tor.md) を参照してください。

## システム

=== "Overview"

    Overview では、CPU Average Load、Memory Usage、LED Control、Flash Usage、Device Info、External Storage など、ルーターの現在の状態と性能情報を確認できます。

    詳細は [Overview](../../interface_guide/system_overview.md) を参照してください。

=== "Admin Password"

    Admin Password では、ルーターの管理インターフェースのパスワードを設定または変更できます。

    詳細は [Admin Password](../../interface_guide/admin_password.md) を参照してください。

=== "Upgrade"

    Upgrade はルーターのファームウェア更新に使用します。Firmware Online Upgrade と Firmware Local Upgrade を利用できます。

    詳細は [Upgrade](../../interface_guide/upgrade.md) を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasks では、LED Display Schedule、Schedule Reboot、5GHz / 2.4GHz Wi-Fi Status Schedule など、ルーター機能をスケジュールに基づいて自動化できます。

    詳細は [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) を参照してください。

<br>

=== "Time Zone"

    Time Zone は、スケジュールタスク、ログ、システムイベントに正しい時刻を記録するためのタイムゾーンを設定します。

    詳細は [Time Zone](../../interface_guide/time_zone.md) を参照してください。

=== "Reset Firmware"

    Reset Firmware は、現在のファームウェアをデフォルト設定に戻し、カスタム設定を消去します。

    詳細は [Reset Firmware](../../interface_guide/reset_firmware.md) を参照してください。

=== "Log"

    Log では System Log、Kernel Log、Crash Log、Cloud Log、Nginx Log を確認できます。Export Log ボタンで、テクニカルサポート分析用に収集済みログをエクスポートできます。

    詳細は [Log](../../interface_guide/log.md) を参照してください。

=== "Advanced Settings"

    Advanced Settings は、詳細設定用の OpenWrt LuCI インターフェースを開きます。

    詳細は [Advanced Settings](../../interface_guide/advanced_settings.md) を参照してください。
