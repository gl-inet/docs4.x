# Beryl AX (GL-MT3000) ユーザーガイド {#beryl-ax-gl-mt3000-user-guide}

## 製品概要 {#product-overview}

Beryl AX（GL-MT3000）は、Wi-Fi 6 に対応した AX3000 クラスのポケットサイズトラベルルーターです。Beryl（GL-MT1300）の後継モデルで、MT7981B 1.3GHz デュアルコアプロセッサを搭載し、Wi-Fi の合計速度は 2 倍以上に向上しています。Wi-Fi を多用する家庭での利用に対応するとともに、旅行での持ち運びにも適したコンパクトな設計です。

![gl-mt3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/hardware_info/mt3000_interface.jpg){class="glboxshadow"}

## パッケージ内容 {#package-contents}

- 1 x Beryl AX (GL-MT3000)
- 1 x ユーザーマニュアル
- 1 x Ethernet ケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター
- 1 x 変換プラグ（配送先の国に応じた仕様）

![gl-MT3000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/first_time_setup/mt3000_unboxing.jpg){class="glboxshadow"}

## Beryl AX のセットアップ方法 {#how-to-set-up-beryl-ax}

以下のセットアップ動画を見るか、下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. 電源を入れる {#1-power-on}

2 ピース式の電源アダプターを組み立てます。ルーターに接続し、コンセントに差し込むと自動的に起動します。

### 2. デバイスを接続する {#2-connect-device}

コンピューター、ノートパソコン、スマートフォンなどのデバイスを Wi-Fi または Ethernet でルーターに接続します。

- Ethernet

    Ethernet ケーブルを使用して、デバイスをルーターの LAN ポートに接続します。

- Wi-Fi

    デバイスで Settings -> WLAN に移動し、利用可能なネットワーク一覧からルーターの Wi-Fi ネットワーク名を探してパスワードを入力します。デフォルトのネットワーク名とパスワードは、ルーターのラベルに印刷されています。

### 3. Web 管理パネルにログインする {#3-log-in-to-web-admin-panel}

Web ブラウザを開き、アドレスバーに `192.168.8.1` と入力してログインします。言語を選択し、管理者パスワードを設定して **Apply** をクリックします。

Wi-Fi 情報を確認する際、Wi-Fi 情報を変更した場合は、更新後の認証情報を使用してデバイスをルーターの Wi-Fi に再接続する必要があります。

### 4. インターネット設定 {#4-internet-setup}

**注：** 以下の手順は、GL.iNet Web 管理パネルでルーターを設定するユーザー向けです。GL.iNet アプリを使用する場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}し、画面の指示に従ってください。

対応しているインターネット接続方式（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用して、Beryl AX を設定します。[Multi-WAN](../../interface_guide/multi-wan.md) 機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_ethernet.png){class="glboxshadow"}

    ルーターの WAN ポートと、モデムなどの上位機器を Ethernet ケーブルで接続します。
    
    インターネットへの接続に成功すると、INTERNET ページの Ethernet セクションに緑のドットが表示されます。

    詳細な手順については、[Ethernet ケーブル経由でインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_repeater.png){class="glboxshadow"}

    1. Web 管理パネルの INTERNET ページで Repeater セクションを探し、**Connect** をクリックします。
    2. 利用可能なネットワークから Wi-Fi ネットワークを選択します。
    3. パスワードを入力し、**Apply** をクリックします。
    
    インターネットへの接続に成功すると、INTERNET ページの Repeater セクションに緑のドットが表示されます。

    詳細な手順については、[既存の Wi-Fi ネットワーク経由でインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_tethering.png){class="glboxshadow"}

    1. スマートフォンや USB ドングルなどのモバイルデバイスを USB ケーブルでルーターの USB ポートに接続します。
    2. モバイルデバイスで Settings に移動し、USB Tethering を有効にします。
    3. Web 管理パネルの INTERNET ページで、Tethering セクションの **Connect** をクリックします。
    
    インターネットへの接続に成功すると、INTERNET ページの Tethering セクションに緑のドットが表示されます。

    詳細な手順については、[USB テザリング経由でインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_cellular.png){class="glboxshadow"}

    セルラー対応の USB モデムをルーターの USB ポートに挿入します。USB モデムのインターネット接続を、接続中のすべてのデバイスで共有する場合に便利です。

    インターネットへの接続に成功すると、INTERNET ページの Cellular セクションに緑のドットが表示されます。

    詳細な手順については、[Cellular 経由でインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

## DNS {#dns}

ルーターのDNS設定は、ドメイン名をIPアドレスに変換する方法を制御します。このページでは、上流デバイスから自動取得したDNSサーバーを使用するか、カスタムDNSサーバーを設定できます。DNSオプションの設定や静的ホストルールの編集もできます。

詳細については、[DNS](../../interface_guide/dns_v4.11.md)を参照してください。

## Wireless {#wireless}

Wireless ページでは、5 GHz と 2.4 GHz の Wi-Fi ネットワークの設定を行えます。Wi-Fi の有効化/無効化、送信出力（TX power）の設定、Wi-Fi 名（SSID）の指定、ランダム化 BSSID の有効化/無効化、Wi-Fi セキュリティモードの選択、Wi-Fi パスワードの設定、SSID の表示設定、Wi-Fi モード、帯域幅、チャンネルの選択が含まれます。

Wireless の設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Mesh {#mesh}

Meshは、Wi-Fi EasyMesh™規格に基づいて家全体のWi-Fiカバレッジを拡張し、シームレスなローミングを実現する機能です。複数のGL.iNetルーターがある場合は、1台をメインルーター、残りをメッシュノードとして設定すると、家の中を移動してもシームレスにWi-Fiを利用できます。

詳細については、[Mesh](../../interface_guide/mesh.md)を参照してください。

## Clients {#clients}

Clients ページには、接続中のデバイス情報が表示されます。各クライアントについて、デバイス名、接続タイプ（Ethernet 経由か Wi-Fi 経由か）、IP アドレス、MAC アドレス、ダウンロード/アップロード速度、総トラフィックが表示され、IP の予約、クライアントのブロック、その他の操作も行えます。

Clients の設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Accountを使用すると、デバイスとクラウドサービスを接続して管理できます。GoodCloudとglinet Appの両方にシームレスにアクセスでき、安全で快適に利用できます。これにより、いつでもどこからでも、より便利にネットワークを管理できます。

    GL.iNet Accountの設定については、[GL.iNet Account](../../interface_guide/glinet_account.md)を参照してください。

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} サービスは、GL.iNet ルーターへリモートアクセスして管理するための簡単な方法を提供します。
    
    GoodCloud の設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "GoodPAS"

    GoodPASは、シームレスなリモートアクセスとデバイス管理を実現する高度なネットワーク機能です。GL.iNetルーターとの統合専用に設計されており、トラフィック難読化機能を備えたAmneziaWGプロトコルを使用して、安全で安定した接続を確保します。GoodPASを使用すると、ホームネットワークにリモートアクセスできます。自宅のルーターがGoodPASの出口ノードとして機能している場合、GoodPAS経由で送信されるインターネットトラフィックには、そのルーターのWANパブリックIPアドレスが使用されます。

    GoodPAS の設定については、[GoodPAS](../../interface_guide/goodpas.md) を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスと VPN サーバーの間に安全で暗号化された通信を作成します。プライバシーとセキュリティを強化し（VPN クライアント）、リモートネットワークへのアクセスも可能にします（VPN サーバー）。Beryl AX（およびその他の GL.iNet ルーター）は、OpenVPN と WireGuard に対応しています。

=== "OpenVPN" 

    Beryl AX（およびその他の GL.iNet ルーター）は、強力なセキュリティを提供する OpenVPN プロトコルに対応しています。OpenVPN の設定については、次のチュートリアルを参照してください。

    * [OpenVPN クライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPN サーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Beryl AX（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルに対応しています。WireGuard の設定については、次のチュートリアルを参照してください。

    * [WireGuard クライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuard サーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク {#network}

=== "Multi-WAN"

    Multi-WAN は、Cellular、Repeater、Ethernet など複数のインターネット接続を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、スムーズで途切れにくいインターネットアクセスを維持できます。

    Multi-WAN の設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LANページでは、メインネットワーク、ゲストネットワーク、IoTネットワーク、カスタムVLANネットワークの設定と管理を一元的に行えます。複数のサブネットを作成・管理して、異なる種類のデバイスやトラフィックを分離できます。

=== "Ethernet Port"

    Ethernet Port ページでは、WAN/LAN ポートの設定、WAN/LAN インターフェースの Ethernet への設定、WAN インターフェースの MAC モードと MAC アドレスの指定、ネットワークポートのネゴシエート速度の確認を行えます。

    Ethernet Portの設定については、[Ethernet Port](../../interface_guide/ethernet_port_v4.10.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。非常に大きなアドレス空間を提供し、インターネットに接続されるデバイス数の増加に対応するために必要な、ほぼ無制限の一意な IP アドレスを利用できます。
    
    IPv6 の設定については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

---

=== "IGMP Snooping"

    IGMP スヌーピングは、Ethernet スイッチでマルチキャストトラフィックを管理・制御するためのネットワーク最適化技術です。
    
    IGMP Snooping の設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "Network Mode"

    Network Modeページでは、さまざまなネットワーク展開要件に合わせてルーターの動作役割を設定できます。家庭のWi-Fiカバレッジから企業向けマルチリンクネットワークまで、用途に応じたモードを選択でき、各モードでは特定のルーター機能を有効または無効にして性能を最適化します。

    設定方法については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in Gateway"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN クライアントなど、メインルーターの機能を拡張します。

    ドロップインゲートウェイの設定については、以下のリンクを参照してください：

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Drop-in Gatewayを設定する](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU 負荷を軽減し、トラフィックパケットの転送を高速化できます。
    
    Network Acceleration の設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御 {#flow-control}

=== "Network Quality"

    Network Qualityダッシュボードは、インターネット接続の品質をリアルタイムで監視します。応答性、遅延、DNSのパフォーマンスを評価し、接続の切断やパケット損失を検出します。これらの指標により、帯域幅のテストだけでは分からないネットワークの不安定さや接続の問題を特定できます。

    詳細については、[Network Quality](../../interface_guide/network_quality.md)を参照してください。

=== "Data Statistics"

    Data Statisticsは、アプリケーション別にネットワーク使用量を分類して可視化するインテリジェントなトラフィック分析ダッシュボードです。リアルタイムと過去のトラフィックを監視し、ネットワークの状態を把握して管理できます。

    詳細は[Data Statistics](../../interface_guide/data_statistics.md)を参照してください。

=== "Content Filter"

    Content Filterは、DPIベースの分類を利用したオンライン保護機能です。有害または悪意のあるWebサイトを自動的にブロックし、ネットワークを安全に保ちます。

    詳細は[Content Filter](../../interface_guide/content_filter.md)を参照してください。

---

=== "QoS"

    QoS（Quality of Service）は、ネットワークの混雑時にビデオ通話やゲームなどの重要な通信を優先し、帯域幅の割り当てを最適化します。これにより、遅延を軽減してネットワーク全体の性能を向上させます。この機能はローカルクライアントのトラフィックとVPNクライアントのトンネルトラフィックに適用されますが、ルーターがVPNサーバーとして受信するトラフィックには適用されません。

    詳細は[QoS](../../interface_guide/qos.md)を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファブロート」を抑え、ゲームや音声通話をより滑らかにします。

    詳細は[SQM](../../interface_guide/sqm.md)を参照してください。

=== "Parental Control"

    Parental Control は、お子様のデバイスを管理・制御するための機能です。画面使用時間の制限や、特定コンテンツへのアクセス制限などが含まれます。

    ペアレンタルコントロールの設定については、[Parental Control](../../interface_guide/parental_control_v4.9.md)を参照してください。

## セキュリティ {#security}

=== "Security Scan"

    Security Scanは、ルーターのセキュリティチェックを実行します。ルーターのセキュリティ設定を評価し、セキュリティスコア、リスクの警告、最適化の提案を表示します。スキャン結果に基づいて設定を調整し、ルーターのセキュリティを向上させることができます。

    詳細については、[Security Scan](../../interface_guide/security_scan.md)を参照してください。

=== "ACL"

    ACL（Access Control List）では、接続プロトコル、デバイスアドレス、ポートに基づくルールを作成し、ネットワークトラフィックを管理できます。ネットワークアクセスを許可するかブロックするかを制御します。複数のACLルールが競合する場合は、優先度の高いルールが適用されます。

    詳細は[ACL](../../interface_guide/acl.md)を参照してください。

=== "Port Forwarding"

    ポートフォワーディングは、インターネット上のリモートサーバーやデバイスからプライベートネットワーク内のデバイスへアクセスできるようにします。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

---

=== "UPnP"

    UPnP（Universal Plug and Play）を使用すると、対応するLANデバイスやアプリケーションがGL.iNetルーターにポートマッピングを自動的に要求できます。これらのマッピングは、受信したWANトラフィックを指定されたLAN IPアドレスとポートに転送します。これにより、ポート転送ルールを手動で設定せずに、外部クライアントがローカルサービスに接続できます。

    詳細については、[UPnP](../../interface_guide/upnp.md)を参照してください。

=== "Admin Access"

    Admin Accessでは、不正なアクセスからネットワークとルーターを保護するための各種セキュリティ設定を行えます。このページには次の項目があります。

    * Local Access Control: ローカルネットワークに接続されたデバイスからルーターインターフェースへのアクセスを管理・制限します。
    * Remote Access Control: インターネット経由のリモートロケーションからルーターインターフェースへのアクセスを設定・制限し、外部脅威に対するセキュリティを強化します。
    * Open Ports on Router: ルーターで開いているポートを制御し、潜在的な脆弱性や不正アクセスを制限します。

    詳細は[Admin Access](../../interface_guide/admin_access.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。
    
    Plug-ins の設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられた IP アドレスをリアルタイムで自動検出し、更新します。ドメイン名をルーターの動的なパブリックIPアドレスに対応付けるため、固定IPアドレスがなくてもネットワークにリモートアクセスできます。
    
    Dynamic DNS の設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージは、複数のユーザーやデバイスがネットワーク経由でファイルへアクセスし共有できる、集中型のデータストレージソリューションです。
    
    Network Storage の設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Home は、ホームネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングする DNS サーバーとして動作する、ネットワーク全体の広告・トラッカーブロックソリューションです。
    
    AdGuard Home の設定については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "Tailscale"

    Tailscale は、どこからでもデバイスやアプリケーションにアクセスできる VPN サービスです。
    
    Tailscale の設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "ZeroTier"

    ZeroTier は、インターネット上に安全な仮想ネットワークを作成し、デバイス同士を同じローカルネットワーク上にあるかのように接続できるソフトウェア定義ネットワーキングソリューションです。
    
    ZeroTier の設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tor"

    Tor は The Onion Router の略で、インターネット上で匿名通信を可能にするプライバシー重視のネットワークです。インターネットトラフィックを複数のボランティア運営サーバー（ノード）経由でルーティングし、ユーザーの場所や利用状況を分かりにくくすることで、オンライン活動の追跡を困難にします。

    Torの設定方法は[Tor](../../interface_guide/tor.md)を参照してください。

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

    詳細な手順については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェース用パスワードを管理し、許可されたユーザーだけが設定を変更できるようにします。

    詳細は[Admin Password](../../interface_guide/admin_password.md)を参照してください。

=== "Upgrade"

    Upgrade ページは、ルーターのファームウェアを最新バージョンへ更新し、性能、セキュリティ、新機能を向上させるために使用します。このページには 2 種類のアップグレード方法があります。

    * Firmware Online Upgrade: メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * Firmware Local Upgrade: コンピューターからファームウェアファイルを手動でアップロードしてルーターを更新し、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、ルーターを最新の改善や修正が含まれた状態に保てます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前に定義したスケジュールに基づいて各種ルーター機能を自動化し、利便性と効率を高められます。このページの主な機能は次のとおりです。

    * LED Display Schedule: 特定の時間帯にルーターの LED ライトを自動的にオンまたはオフにするスケジュールを設定し、光害を減らせます。
    * Schedule Reboot: 指定した間隔でルーターを自動再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fi Status Schedule: 5GHz / 2.4GHz Wi-Fi バンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力を管理しやすくします。
    
    これらのスケジュール機能により、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

=== "Time Zone"

    Time Zone ページでは、ルーターに正しいタイムゾーンを設定し、すべてのスケジュールタスク、ログ、システムイベントが現地時間に基づいて正確に記録されるようにします。この設定は、正確な記録の維持と時間ベース設定の適切な実行に重要です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Toggle Button Settings"

    Toggle Button Settings ページでは、ルーターの物理トグルボタンを設定し、特定の機能を割り当ててすばやく操作できるようにします。この機能は、よく使うタスクや設定への便利なショートカットを提供し、ユーザー体験を向上させ、ルーター管理を簡単にします。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md)を参照してください。

---

=== "Reset Firmware"

    Reset Firmware ページでは、現在のファームウェアバージョンをデフォルト設定へリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定に戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Log ページでは、トラブルシューティングやパフォーマンス監視に役立つ、ルーターの動作やイベントを記録した各種ログへアクセスできます。このページには次の項目があります。

    * System Log: システムレベルのイベントや動作に関する詳細ログ。
    * Kernel Log: カーネルの処理やイベントに関するログ。
    * Crash Log: システムクラッシュやエラーの記録。重大な問題の診断に役立ちます。
    * Cloud Log: ルーターに統合された GoodCloud サービスに関連する操作や通信のログ。
    * Nginx Log: ルーターで Nginx Web サーバーを使用している場合のログ。Web トラフィックやサーバー動作の詳細を記録します。
    
    さらに、このページには Export Log ボタンがあり、収集されたすべてのログをテクニカルサポート分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に役立ちます。

    詳細な手順については、[Log](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションへアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えてルーターの設定や機能を細かく調整できます。詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
