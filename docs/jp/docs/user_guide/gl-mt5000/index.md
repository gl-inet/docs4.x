# Brume 3 (GL-MT5000) ユーザーガイド

## 製品概要

Brume 3 (GL-MT5000) は、OpenWrt v21.02を実行する高パフォーマンスセキュリティゲートウェイです。MediaTekクアッドコア Cortex-A53 CPU、1GB RAM、8GB eMMCストレージ（プラグイン拡張用）を備えています。コンパクトなデザインで、スペースが限られた展開に最も適でホームVPNホスティング、site-to-site SD-WAN、30以上のVPNサービスをサポートし、安全でクロスロケーション接続を実現します。さらに、GL.iNetのDPI機能、Parental Control、AdGuard Homeが含まれており、テクユーザーとビジネスユーザーの多様なニーズに対応しています。

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## パッケージコンテンツ

パッケージには以下が含まれます：

- 1 x Brume 3 (GL-MT5000)
- 1 x 電源アダプター
- 1 x Ethernet cable
- 1 x ユーザーガイド
- 1 x サンキューカード
- 1 x コンバーター（発送国により異なります）

Brume 3の開栓動画については、以下を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Brume 3の設定方法

### 1. 電源を入れる

二分割の電源アダプターを組み合わせます。Brume 3に接続し、コンセントに挿すと自動的に起動します。

### 2. Brume 3に接続する

Ethernet cableを使用して有線デバイス（コンピュータやラップトップなど）をBrume 3のLANポートに接続します。

### 3. WebGUIにログインする

**注意:** 以下の説明は、GL.iNet Web管理パネルでルーターを設定するユーザーに適用されます。

Webブラウザーでアドレスバーに`192.168.8.1`を入力してログインします。言語を選択し、管理者パスワードを設定して、**Apply**をクリックします。

### 4. Brume 3をインターネットに接続する

サポートされているインターネット接続方法（Ethernet、Tethering、Cellular（オプション））を使用してBrume 3を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Brume 3 の WAN ポートを Ethernet ケーブルで上位機器（モデムなど）に接続します。
    
    Brume 3 がインターネットに正常に接続されると、Web 管理パネルの INTERNET ページの「Ethernet」の横に緑色のドットが表示され、Brume 3 本体の LED が白色で点灯します。

    詳細な手順については、[Ethernet ケーブルでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. モバイルデバイスをUSB 3.0データケーブルでBrume 3のUSB Type-Cポートに接続します。
    2. モバイルデバイスの設定で、USBテザリングを有効にします。
    3. Web管理パネルのINTERNETページで、「Tethering」セクションの**Connect**をクリックします。
    
    Brume 3 がインターネットに正常に接続されると、Web 管理パネルの INTERNET ページの「Tethering」の横に緑色のドットが表示され、Brume 3 本体の LED が白色で点灯します。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    この接続方法には、追加のUSB-C to USB-Aアダプターケーブルが必要です。
    
    追加の USB-C to USB-A アダプターケーブルを使って、Cellular USB モデムを Brume 3 の USB Type-C ポートに接続します。USB モデムの回線を接続中のすべてのクライアントデバイスで共有したい場合に便利です。

    Brume 3 がインターネットに正常に接続されると、Web 管理パネルの INTERNET ページの「Cellular」の横に緑色のドットが表示され、Brume 3 本体の LED が白色で点灯します。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

## Clients

Clients ページには、接続中のデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレス、MACアドレス、ダウンロード速度、アップロード速度、合計トラフィックを確認でき、クライアントをブロックしたり、その他の操作を実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}クラウド管理サービスは、GL.iNetルーターに簡単かつシンプルにリモートアクセスと管理を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarp は、シームレスなリモートネットワーク接続とリモートデバイス管理を実現する高度なネットワーキングプラットフォームです。GL.iNet ルーターとの連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位・下位デバイスの制御も可能にします。将来的なハードウェアレベル制御にも対応できる設計で、安全かつ安定したネットワークを維持するための堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Brume 3はOpenVPNとWireGuardをサポートしています。

=== "OpenVPN"
    
    Brume 3（およびその他の GL.iNet ルーター）は、高いセキュリティを提供する OpenVPN プロトコルをサポートしています。OpenVPN を設定するには、以下のチュートリアルを参照してください。

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Brume 3（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルをサポートしています。WireGuard を設定するには、以下のチュートリアルを参照してください。

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク

=== "Multi-WAN"

    Multi-WANは、ルーターに複数のインターネット接続（cellular、repeater、ethernetなど）を同時に設定できるネットワーキング機能です。現在のインターネット接続が失敗すると、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れないインターネットアクセスが確保されます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなどの限られた物理的な範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。
    
    LANの設定については、[Lan](../../interface_guide/lan.md)を参照してください。

=== "DNS"

    DNSページでは、カスタムDNSサーバーを設定し、DNSリバインディング攻撃保護を有効にしてすべてのクライアントのDNS設定を上書きし、カスタムDNSがVPN DNSを上書きできるようにし、Ethernet接続からDNSサーバーを自動的に指定するか手動で指定するモードを構成できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

---

=== "Ethernet Port"

    Ethernet Portページでは、WANとLANポートの設定、WAN/LANインターフェースをEthernetに設定、WANインターフェースのMACモードとMACアドレスの指定、ネゴシエーション済みネットワークポート速度の表示を行うことができます。

    Ethernetポートの管理については、[Port Management](../../interface_guide/ethernet_port.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。ほぼ無制限の固有IPアドレスを提供する広大なアドレス空間を備え、インターネット接続デバイスの増加に対応するうえで不可欠です。
    
    IPV6の設定については、[IPV6](../../interface_guide/network_mode.md)を参照してください。

=== "IGMP Snooping"

    IGMPスヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。
    
    IGMPスヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

---

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する構成設定です。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in gateway"

    ドロップインゲートウェイは、AdGuard Home、暗号化DNS、VPNクライアントを含むメインルーターの機能を拡張します。
    
    ドロップインゲートウェイの設定については、以下のリンクを参照してください：
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU負荷を削減し、トラフィックパケットの転送を高速化できます。
    
    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御

=== "DPI License"

    DPI（Deep Packet Inspection）はインテリジェントネットワーク管理の中核機能です。従来のルーター器（送信元または宛先アドレスのみ識別）の制限を克服し、データパケットペイロードを深く分析し、機能ライブラリ比較を通じてユーザーがアクセスしたアプリケーションとウェブサイトを正確に識別し、洗練されたトラフィック分類と制御を可能にします。
    
    [Netify](https://www.netify.ai/){target="_blank"} と統合された GL.iNet DPI 機能は、軽量な組み込みプラグインを採用して効率的な展開を実現しています。Netify のオンライン更新シグネチャデータベースにより、信頼性の高い管理が可能になり、ネットワーク制御をより正確かつ効率的に行えます。

    詳細な手順については、[DPI License](../../interface_guide/dpi_license.md)を参照してください。

=== "Data Statistics"

    Data Statisticsは、アプリケーション別にネットワーク使用量を分類して視覚化するインテリジェントトラフィックインサイトダッシュボードを提供し、より良いネットワーク認識と制御のためにリアルタイムと履歴トラフィックを監視できます。

    詳細な手順については、[Data Statistics](../../interface_guide/data_statistics.md)を参照してください。

=== "Content Filter"

    Content Filterは、DPIベースの分類によるスマートオンライン安全性を提供し、悪質または有害なウェブサイトを自動的にブロックして、ネットワークを清洁で安全に保ちます。

    詳細な手順については、[Content Filter](../../interface_guide/content_filter.md)を参照してください。

---

=== "Parental Control"

    Parental Controlは、子どものデバイスを管理および制御するために設計されています。スクリーン時間の制限や特定コンテンツへのアクセス制限が含まれます。

    保護者による制御の設定については、[Parental Control](../../interface_guide/parental_control.md)を参照してください。

=== "QoS"

    QoS（Quality of Service）は、ネットワーク輻輳時にビデオコールやゲームなどの重要なアクティビティを優先して帯域幅割り当てを最適化し、レイテンシを削減して全体のなネットワークパフォーマンスを向上させます。これはローカルクライアントトラフィックとVPNクライアントトラフィック tunnelトラフィックに適用されますが、ルーターがVPNサーバーとして機能しているときに受信するトラフィックには適用されないことに注意してください。

    詳細な手順については、[QoS](../../interface_guide/qos.md)を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理してレイテンシと「bufferbloat」を最も小化し、よりスムーズなゲームと音声通話を確保します。

    詳細な手順については、[SQM](../../interface_guide/sqm.md)を参照してください。

## セキュリティ

=== "Port Forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Management Control"

    Management Controlでは、ネットワークとルーターを不正アクセスから保護するためのさまざまなセキュリティ設定を構成できます。このページには以下のオプションがあります：

    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーターのインターフェースへのアクセスを管理および制限します。
    * リモートアクセス制御：インターネット上のリモート場所からルーターのインターフェースへのアクセスを構成および制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    これらの設定は、ネットワーク環境を安全に保ち、ルーターと接続されたデバイスを保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG（Application Layer Gateway）機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション

=== "Plug-ins"

    プラグインは、既存のコンピュータプログラムに特定の機能または機能を追加するソフトウェアコンポーネントであり、カスタマイズと機能拡張を可能にします。
    
    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。リモートネットワークにアクセスするために静的IPアドレスが必要なユーザーに最も便利です。
    
    Dynamic DNSの設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージとは、複数のユーザーとデバイスがネットワーク上でファイルにアクセスして共有できる集中型データストレージソリューションを指します。
    
    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Homeは、ネットワーク全体の広告およびトラッカーブロッキングソリューションであり、家庭内ネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングするDNSサーバーとして機能します。
    
    AdGuard Homeの設定については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "ZeroTier"

    ZeroTierは、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全に仮想ネットワークを作成し、デバイスが同一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサービスです。
    
    Tailscaleの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "Tor"

    Tor（The Onion Routerのやや称）は、匿名通信を可能にするプライバシー重視のネットワークです。ユーザーの位置情報と使用状況を不明瞭にするために、一連のボランティアが運用するサーバー（ノード）を介してインターネットトラフィックをルーティングします。
    
    * [Torの設定方法](../../interface_guide/tor.md)

## システム

=== "Overview"

    Overviewページは、ルーターの現在のパフォーマンス指標とステータスのを含むスナップショットを提供します。このページでは以下を表示できます：

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーターのフラッシュストレージの使用率を確認し、ファームウェアと設定データのための十分な空き容量を確保します。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーターの操作を効果的に管理および監視するのに役立つ重要な洞察とコントロールを提供します。

    詳細な設定手順と詳細については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェースのパスワードを設定または変更でき、許可されたユーザーのみが設定を変更できるようにします。

    セキュリティ上の理由から、**Prevent Weak Password**をオンにすることをお勧めします。

    **Prevent Weak Password**をオンにすると、新しいパスワードの要件は以下の通りです：

    * 5文字で上63文字以下。
    * 文字（大文字小文字を区別）、数字、記号`` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``が許可されています。
    * 大文字、小文字、数字、記号のうち2種類で上が必要です。

=== "Upgrade"

    Upgrade ページでは、ルーターのファームウェアを最新バージョンへ更新できます。これにより、性能向上、セキュリティ強化、新機能の利用が可能になります。このページには次の2つのアップグレード方法があります。

    * ファームウェアオンラインアップグレード：メーカーのサーバーから最新バージョンを自動確認してインストールします。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善や修正を適用した状態にルーターを保てます。

    詳細な設定手順と詳細については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasksページにより、事前定義されたスケジュールに基づいてさまざまなルーター機能を自動化でき、利便性と効率性が向上します。このページの主要機能は次のとおりです：

    * LED表示スケジュール：特定の時間帯にルーターのLEDライトを自動的にオンまたはオフに設定し，光害を軽減します。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    
    これらのスケジューリングオプションは、ルーターの操作をより詳細に制御し、特定のニーズと好みに合わせることができます。

    詳細な設定手順と詳細については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現地時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な設定手順と詳細については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはExport Logボタンがあり、収集したすべてのログをエクスポートして技術サポートの分析にできます。この機能は、複雑な問題の診断と専門のサポートの取得に非常に便利です。

    詳細な設定手順と詳細については、[Log](../../interface_guide/log.md)を参照してください。

---

=== "Reset Firmware"

    Reset Firmwareページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。このプロセスは、現にインストールされているファームウェアバージョンのデフォルト設定にルーターを復元します。持続的な問題のトラブルシューティングや現在のファームウェアのデフォルト設定で新鲜に開始するのに便利です。

    詳細な設定手順と詳細については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Advanced Settings"

    Advanced Settingsページは、OpenWrt LuCIインターフェースを通じて高度な構成オプションへのアクセスを提供し、経験豊富なユーザーが基本インターフェースオプションを超えてルーターの設定と機能を微調整できます。これには、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な設定手順と詳細については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
