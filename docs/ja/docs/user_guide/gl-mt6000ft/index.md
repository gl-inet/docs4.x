# Fortify (GL-MT6000) ユーザーガイド {#fortify-gl-mt6000-user-guide}

## 製品概要 {#product-overview}

Fortify (GL-MT6000) は、GL.iNet と ExpressVPN が共同でリリースしたコラボレーションモデルの Wi-Fi 6 ルーターです。すべての製品に 1 年間の ExpressVPN サブスクリプションが無料で付属しています。サブスクリプションの引き換えとアカウントの接続は、ルーターの Web 管理パネルで直接行えます。ExpressVPN トンネルが接続されている場合、ルーターは VPN ポリシー設定に従ってトラフィックを暗号化し、そのトンネル経由でルーティングします。

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## パッケージ内容 {#package-contents}

- 1 x Fortify (GL-MT6000)
- 1 x ユーザーマニュアル
- 1 x ExpressVPN アクティベーションガイド
- 1 x Ethernet ケーブル
- 1 x 電源アダプター
- 1 x サンキューカード
- 1 x 変換プラグ（配送先の国に応じた仕様）

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/unboxing.png){class="glboxshadow"}

以下の Fortify の開封動画をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/IQEfj7Hff7U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Fortify のセットアップ方法 {#how-to-set-up-fortify}

セットアップ動画を視聴するか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/FymI3LCRMTA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. 電源を入れる {#1-power-on}

2 ピース式の電源アダプターを組み立てます。Fortify ルーターに接続し、コンセントに差し込むと自動的に起動します。

### 2. デバイスを接続する {#2-connect-device}

コンピューター、ノートパソコン、スマートフォンなどのデバイスを Wi-Fi または Ethernet でルーターに接続します。

- Ethernet

    Ethernet ケーブルを使用して、デバイスをルーターの LAN ポートに接続します。

- Wi-Fi

    デバイスで Settings -> WLAN に移動し、利用可能なネットワーク一覧からルーターの Wi-Fi ネットワーク名を探し、パスワードを入力してネットワークに参加します。デフォルトのネットワーク名とパスワードは、ルーターのラベルに印刷されています。

### 3. Web 管理パネルにログインする {#3-log-in-to-web-admin-panel}

Web ブラウザを開き、アドレスバーに `192.168.8.1` と入力してログインします。右上で言語を選択し、管理者パスワードを設定して **Next** をクリックします。パスワードは 10～63 文字で、英大文字、英小文字、数字、特殊記号のうち少なくとも 2 種類を含める必要があります。

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Wi-Fi を設定します。Wi-Fi 情報を変更した場合は、更新後の認証情報を使用してデバイスをルーターの Wi-Fi に再接続する必要があります。

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. インターネット設定 {#4-internet-setup}

**注：** 以下の手順は、GL.iNet Web 管理パネルでルーターを設定するユーザー向けです。[GL.iNet アプリ](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}を使用する場合は、アプリをダウンロードし、画面の指示に従ってください。

対応しているインターネット接続方式（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用して、Fortify を設定します。[Multi-WAN](../../interface_guide/multi-wan.md) 機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Fortify ルーターの WAN ポートと、モデムなどの上位機器を Ethernet ケーブルで接続します。

    インターネットへの接続に成功すると、ルーターの LED が白色に点灯します。

    詳細な手順については、[Ethernet ケーブル経由でインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Web 管理パネルで INTERNET -> Repeater セクションに移動し、**Connect** をクリックします。
    2. 利用可能なネットワークから Wi-Fi を選択します。
    3. パスワードを入力し、**Apply** をクリックします。

    インターネットへの接続に成功すると、ルーターの LED が白色に点灯します。

    詳細な手順については、[既存の Wi-Fi ネットワーク経由でインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. USB ケーブルを使用して、スマートフォンをルーターの USB ポートに接続します。
    2. スマートフォンで Settings に移動し、USB Tethering を有効にします。iPhone の場合は、このデバイスを信頼し、インターネット共有（Personal Hotspot）を有効にします。
    3. Web 管理パネルで INTERNET -> Tethering セクションに移動し、**Connect** をクリックします。

    インターネットへの接続に成功すると、ルーターの LED が白色に点灯します。

    詳細な手順については、[USB テザリング経由でインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    セルラー対応の USB モデムをルーターの USB ポートに挿入します。USB モデムのインターネット接続を、接続中のすべてのデバイスで共有する場合に便利です。

    インターネットへの接続に成功すると、ルーターの LED が白色に点灯します。

    詳細な手順については、[Cellular 経由でインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下は、Fortify の Web 管理パネルで利用できる機能の概要です。

## Wireless {#wireless}

Wireless ページでは、メインネットワーク、ゲストネットワーク、IoT ネットワークなど、Fortify の Wi-Fi ネットワークを設定できます。各ネットワークは 2.4 GHz と 5 GHz の両方の帯域に対応しています。

Wireless の設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients {#clients}

Clients ページには、デバイス名、接続タイプ、IP アドレス、MAC アドレス、ダウンロード/アップロード速度、トラフィックなど、接続中のデバイスの情報が表示されます。また、ワンクリックで特定のクライアントをブロックしたり、その他の操作を行ったりできます。

詳細については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、GL.iNet ルーターへリモートアクセスして管理するための簡単な方法を提供します。

    詳細については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarp は、GL.iNet ルーターでシームレスなリモートネットワーキングを実現するために構築された機能です。トラフィック難読化機能を内蔵した AmneziaWG プロトコルを採用し、いつでもどこからでも安定した安全なリモートアクセスを提供します。

    詳細については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、ローカルデバイスと VPN サーバーの間に、安全で暗号化されたトラフィックトンネルを確立します。VPN クライアントとしてはプライバシーとセキュリティをさらに強化し、リモートの VPN サーバー側ネットワークへのアクセスも可能にします。

Fortify は [ExpressVPN](https://www.expressvpn.com/){target="_blank"} と統合されており、数分で ExpressVPN 接続を有効にできます。すべての Fortify に 1 年間の ExpressVPN サブスクリプションが無料で付属しています。サブスクリプションの引き換えと ExpressVPN アカウントの接続は、ルーターの Web 管理パネルで直接行えます。ExpressVPN トンネルが接続されている場合、ルーターは VPN ポリシー設定に従ってトラフィックを暗号化し、そのトンネル経由でルーティングします。

無料サブスクリプションの引き換えと VPN トンネルの設定については、[ExpressVPN アクティベーションガイド](../../interface_guide/expressvpn_activation_guide.md)を参照してください。

OpenVPN サーバーの設定については、[OpenVPN サーバー](../../interface_guide/openvpn_server.md)を参照してください。

WireGuard サーバーの設定については、[WireGuard サーバー](../../interface_guide/wireguard_server.md)を参照してください。

## ネットワーク {#network}

=== "Multi-WAN"

    Multi-WAN は、Cellular、Repeater、Ethernet など複数のインターネット接続を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、スムーズで途切れにくいインターネットアクセスを維持できます。

    詳細については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなど限られた範囲内でコンピューターやデバイスを接続するネットワークです。メイン Wi-Fi または Ethernet ケーブルで接続したデバイスが参加するローカルネットワークがこれにあたります。LAN ページには、基本設定、DHCP サーバー設定、アドレス予約があります。

    詳細については、[LAN](../../interface_guide/lan.md)を参照してください。

=== "Guest Network"

    Guest Network ページでは、訪問者専用の Wi-Fi ネットワークを作成できます。メインネットワークから分離されているため、セキュリティを強化しつつ、便利なインターネットアクセスを提供できます。IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` 内でゲスト用サブネットを設定し、ゲートウェイとネットマスクの IP アドレスを指定できます。

    詳細については、[ゲストネットワーク](../../interface_guide/guest_network.md)を参照してください。

=== "IoT Network"

    IoT Network ページでは、IoT デバイス専用の Wi-Fi ネットワークを作成できます。メインネットワークから分離されているため、互換性とセキュリティが向上します。

    詳細については、[IoT ネットワーク](../../interface_guide/iot_network.md)を参照してください。

<br>

=== "DNS"

    ルーターの DNS 設定は、ドメイン名を IP アドレスに変換する方法を制御します。このページでは、上位機器から自動的に取得した DNS サーバーを使用するか、カスタム DNS サーバーを設定するかを選択でき、DNS の優先順位も設定できます。

    詳細については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "Ethernet Port"

    Ethernet Port ページでは、Ethernet ポートの役割（WAN/LAN）を管理し、MAC アドレスやネゴシエート速度などのポートの詳細を確認できます。

    詳細については、[Ethernet ポート](../../interface_guide/ethernet_port.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。非常に大きなアドレス空間を提供し、インターネットに接続されるデバイス数の増加に対応するために必要な、ほぼ無制限の一意な IP アドレスを利用できます。

    詳細については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

=== "IGMP Snooping"

    IGMP スヌーピングは、Ethernet スイッチでマルチキャストトラフィックを管理・制御するためのネットワーク最適化技術です。

    詳細については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

<br>

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する設定です。

    ネットワークモードの設定については、[ネットワークモード](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in Gateway"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN など、メインルーターにない機能を追加してメインルーターの機能を拡張します。

    Drop-in Gateway の設定については、[ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)を参照してください。

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU 負荷を軽減し、トラフィックパケットの転送を高速化できます。

    ネットワークアクセラレーションの設定については、[ネットワークアクセラレーション](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御 {#flow-control}

=== "DPI Engine"

    DPI（Deep Packet Inspection）は、インテリジェントなネットワーク管理の中核となる機能です。送信元または宛先アドレスしか識別できない従来のルーターの制約を克服し、データパケットのペイロードを詳細に分析します。特徴ライブラリとの照合により、ユーザーがアクセスしたアプリケーションや Web サイトを正確に識別し、きめ細かなトラフィック分類と制御を可能にします。

    GL.iNet の DPI 機能は [Netify](https://www.netify.ai/){target="_blank"} と統合されており、効率的に導入できる軽量な組み込みプラグインを採用しています。オンラインで更新される Netify のシグネチャデータベースにより、信頼性の高い管理を実現し、ネットワーク制御をより正確かつ効率的にします。

    詳細については、[DPI エンジン](../../interface_guide/dpi_engine.md)を参照してください。

=== "Data Statistics"

    Data Statistics は、ネットワーク使用状況をアプリケーションごとに分類して可視化するインテリジェントなトラフィック分析ダッシュボードを提供します。リアルタイムおよび過去のトラフィックを監視でき、ネットワークの状況把握と制御に役立ちます。

    詳細については、[データ統計](../../interface_guide/data_statistics.md)を参照してください。

=== "Content Filter"

    Content Filter は、DPI ベースの分類を活用したスマートなオンライン保護機能です。有害または悪意のある Web サイトを自動的にブロックし、ネットワークをクリーンで安全な状態に保ちます。

    詳細については、[コンテンツフィルター](../../interface_guide/content_filter.md)を参照してください。

<br>

=== "QoS"

    QoS（Quality of Service）は、ネットワークの混雑時にビデオ通話やゲームなどの重要な通信を優先して帯域幅の割り当てを最適化し、遅延を減らしてネットワーク全体のパフォーマンスを向上させます。この機能はローカルクライアントのトラフィックと VPN クライアントトンネルのトラフィックに適用されますが、ルーターが VPN サーバーとして動作している場合に受信するトラフィックには適用されません。

    詳細については、[QoS](../../interface_guide/qos.md)を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファブロート（bufferbloat）」を最小限に抑え、ゲームや音声通話をよりスムーズにします。

    詳細については、[SQM](../../interface_guide/sqm.md)を参照してください。

=== "Parental Control"

    ペアレンタルコントロールは、お子様のデバイスを管理・制御するための機能です。画面使用時間の制限や、特定コンテンツへのアクセス制限などが含まれます。

    詳細については、[ペアレンタルコントロール](../../interface_guide/parental_control_v4.9.md)を参照してください。

## セキュリティ {#security}

=== "Port forwarding"

    ポートフォワーディングは、インターネット上のリモートサーバーやデバイスからプライベートネットワーク内のデバイスへアクセスできるようにします。

    詳細については、[ポートフォワーディング](../../interface_guide/port_forwarding.md)を参照してください。

=== "ACL"

    ACL（Access Control List）では、接続プロトコル、デバイスのアドレス、ポートに基づいてネットワークトラフィックを管理するルールを作成し、ネットワークアクセスを許可するかブロックするかを制御できます。複数の ACL ルールが競合する場合は、優先度の高いルールが適用されます。

    詳細については、[ACL](../../interface_guide/acl.md)を参照してください。

=== "Admin Access"

    Admin Access では、不正アクセスからネットワークとルーターを保護するための各種セキュリティ設定を構成できます。このページには次のオプションがあります。

    * Access Control: ローカルネットワークに接続されたデバイスからルーターインターフェースへのアクセスを管理・制限します。
    * Remote Access Control: インターネット経由のリモートロケーションからルーターインターフェースへのアクセスを設定・制限し、外部脅威に対するセキュリティを強化します。
    * Open Ports on Router: ルーターで開いているポートを制御し、潜在的な脆弱性や不正アクセスを制限します。

    詳細については、[管理者アクセス](../../interface_guide/admin_access.md)を参照してください。

=== "NAT Mode"

    NAT Mode ページでは、Full Cone NAT と SIP ALG（Application Layer Gateway）機能の有効化または無効化を設定できます。

    詳細については、[NAT モード](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。

    詳細については、[プラグイン](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられた IP アドレスをリアルタイムで自動検出し、更新します。ドメイン名をルーターの動的なパブリック IP アドレスに対応付けるため、固定 IP アドレスがなくてもネットワークにリモートアクセスできます。

    詳細については、[ダイナミック DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージは、複数のユーザーやデバイスがネットワーク経由でファイルへアクセスし共有できる、集中型のデータストレージソリューションです。

    詳細については、[ネットワークストレージ](../../interface_guide/network_storage.md)を参照してください。

=== "AdGuard Home"

    AdGuard Home は、ホームネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングする DNS サーバーとして動作する、ネットワーク全体の広告・トラッカーブロックソリューションです。

    詳細については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} サービスは、お子様のデジタル環境を守り、包括的なオンライン保護を提供します。通常は有料サブスクリプションが必要ですが、GL.iNet と Bark の提携により、Fortify (GL-MT6000) では Bark Home プランを無料で利用でき、追加費用なしで高度な監視とアラート機能を利用できます。

    詳細については、[Bark](../../interface_guide/bark.md)を参照してください。

=== "Tailscale"

    Tailscale は、所有するデバイスやアプリケーションに世界中のどこからでも安全かつ簡単にアクセスできるようにする VPN サービスです。

    Fortify (GL-MT6000) は Tailscale と統合されており、ルーターを Tailscale 仮想ネットワークに参加させることができます。接続後は、ルーターの WAN 側および LAN 側のリソースも含めてリモートからアクセスできます。

    詳細については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "ZeroTier"

    ZeroTier は、インターネット上に安全な仮想ネットワークを作成し、デバイス同士を同じローカルネットワーク上にあるかのように接続できるソフトウェア定義ネットワーキングソリューションです。

    詳細については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tor"

    Tor（The Onion Router に由来）は、匿名通信を可能にする無料のオープンソースソフトウェアです。プライバシーを保ちながらインターネットを利用できます。

    詳細については、[Tor](../../interface_guide/tor.md)を参照してください。

## システム {#system}

=== "Overview"

    Overview ページでは、ルーターの現在の状態とパフォーマンス指標をまとめて確認できます。このページでは次の情報を確認できます。

    * CPU Average Load: ルーター CPU の平均負荷を監視し、パフォーマンス評価や潜在的なボトルネックの把握に役立ちます。
    * Memory Usage: ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LED Control: ルーターの LED ライトをオンまたはオフに切り替え、表示をカスタマイズできます。
    * Flash Usage: ルーターのフラッシュストレージ使用量を確認し、ファームウェアや設定データ用の空き容量を把握できます。
    * Device Info: 稼働時間、ホスト名、モデル、アーキテクチャ、OpenWrt バージョン、カーネルバージョン、デバイス ID、デバイス MAC、デバイス S/N など、ルーターのシステム情報にアクセスできます。
    * External Storage: USB ドライブや TF カードなど、ルーターに接続された外部ストレージデバイスの状態を確認できます。

    これらの機能により、ルーターの動作を効果的に管理・監視するための重要な情報と制御を利用できます。

    詳細については、[概要](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Password ページでは、ルーターの管理インターフェース用パスワードを設定または変更できます。

    詳細については、[管理者パスワード](../../interface_guide/admin_password.md)を参照してください。

=== "Upgrade"

    Upgrade ページは、ルーターのファームウェアを最新バージョンへ更新し、性能、セキュリティ、新機能を向上させるために使用します。このページには 2 種類のオプションがあります。

    * Firmware Online Upgrade: メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * Firmware Local Upgrade: コンピューターからファームウェアファイルを手動でアップロードしてルーターを更新し、アップグレードバージョンとタイミングを制御できます。

    詳細については、[アップグレード](../../interface_guide/upgrade.md)を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前に定義したスケジュールに基づいて各種ルーター機能を自動化し、利便性と効率を高められます。このページの主な機能は次のとおりです。

    * LED Display Schedule: 特定の時間帯にルーターの LED ライトを自動的にオンまたはオフにするスケジュールを設定し、光害を減らせます。
    * Schedule Reboot: 指定した間隔でルーターを自動再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * 5GHz / 2.4GHz Wi-Fi Status Schedule: 5GHz / 2.4GHz Wi-Fi バンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力を管理しやすくします。

    これらのスケジュール機能により、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細については、[スケジュールタスク](../../interface_guide/scheduled_tasks.md)を参照してください。

<br>

=== "Time Zone"

    Time Zone ページでは、ルーターに正しいタイムゾーンを設定し、すべてのスケジュールタスク、ログ、システムイベントが現地時間に基づいて正確に記録されるようにします。この設定は、正確な記録の維持と時間ベース設定の適切な実行に重要です。

    詳細については、[タイムゾーン](../../interface_guide/time_zone.md)を参照してください。

=== "Reset Firmware"

    Reset Firmware ページでは、現在のファームウェアバージョンをデフォルト設定へリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定に戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細については、[ファームウェアのリセット](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Log ページでは、トラブルシューティングやパフォーマンス監視に役立つ、ルーターの動作やイベントを記録した各種ログへアクセスできます。このページには次の項目があります。

    * System Log: システムレベルのイベントや動作に関する詳細ログ。
    * Kernel Log: カーネルの処理やイベントに関するログ。
    * Crash Log: システムクラッシュやエラーの記録。重大な問題の診断に役立ちます。
    * Cloud Log: ルーターに統合された GoodCloud サービスに関連する操作や通信のログ。
    * Nginx Log: ルーターで Nginx Web サーバーを使用している場合のログ。Web トラフィックやサーバー動作の詳細を記録します。

    さらに、このページには Export Log ボタンがあり、収集されたすべてのログをテクニカルサポート分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に役立ちます。

    詳細については、[ログ](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションへアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えてルーターの設定や機能を細かく調整できます。詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細については、[詳細設定](../../interface_guide/advanced_settings.md)を参照してください。
