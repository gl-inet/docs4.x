# Brume 3 (GL-MT5000) ユーザーガイド {#brume-3-gl-mt5000-user-guide}

## 製品概要 {#product-overview}

Brume 3 (GL-MT5000) は、OpenWrt v21.02 で動作する高性能セキュリティゲートウェイです。MediaTek クアッドコア Cortex-A53 CPU、1GB RAM、プラグイン拡張用の 8GB eMMC ストレージを搭載しています。設置スペースが限られた環境に最適なコンパクト設計で、ホーム VPN のホスティング、サイトツーサイト SD-WAN、30 以上の VPN サービスに対応し、拠点間の安全な接続を実現します。さらに、GL.iNet の DPI 機能、ペアレンタルコントロール、AdGuard Home も備えており、テクノロジー愛好家やビジネスユーザーの多様なニーズに応えます。

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## パッケージ内容 {#package-contents}

- 1 x Brume 3 (GL-MT5000)
- 1 x 電源アダプター
- 1 x Ethernet ケーブル
- 1 x ユーザーマニュアル
- 1 x サンキューカード
- 1 x 変換プラグ（配送先の国に応じた仕様）

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/unboxing.png){class="glboxshadow"}

以下の Brume 3 の開封動画をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Brume 3 のセットアップ方法 {#how-to-set-up-brume-3}

セットアップ動画を視聴するか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwbdUy79WHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. 電源を入れる {#1-power-on}

2 ピース式の電源アダプターを組み立てます。Brume 3 に接続し、コンセントに差し込むと自動的に起動します。

### 2. デバイスを接続する {#2-connect-device}

Ethernet ケーブルを使用して、有線デバイス（コンピューターやノートパソコンなど）を Brume 3 の LAN ポートに接続します。

### 3. Web 管理パネルにログインする {#3-log-in-to-web-admin-panel}

**注：** 以下の手順は、GL.iNet Web 管理パネルでルーターを設定するユーザー向けです。

Web ブラウザを開き、アドレスバーに `192.168.8.1` と入力してログインします。言語を選択し、管理者パスワードを設定して **Apply** をクリックします。

### 4. インターネット設定 {#4-internet-setup}

対応しているインターネット接続方式（Ethernet、Tethering、Cellular（オプション））のいずれかを使用して、Brume 3 を設定します。[Multi-WAN](../../interface_guide/multi-wan.md) 機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Brume 3 の WAN ポートと、モデムなどの上位機器を Ethernet ケーブルで接続します。

    Brume 3 がインターネットに正常に接続されると、Web 管理パネルの INTERNET ページで「Ethernet」の横に緑のドットが表示され、Brume 3 本体の LED が白色に点灯します。

    詳細な手順については、[Ethernet ケーブル経由でインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. USB 3.0 データケーブルを使用して、モバイルデバイスを Brume 3 の USB Type-C ポートに接続します。
    2. モバイルデバイスの設定で USB テザリングを有効にします。
    3. Web 管理パネルの INTERNET ページで、「Tethering」セクションの **Connect** をクリックします。

    Brume 3 がインターネットに正常に接続されると、Web 管理パネルの INTERNET ページで「Tethering」の横に緑のドットが表示され、Brume 3 本体の LED が白色に点灯します。

    詳細な手順については、[USB テザリング経由でインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    この接続方法では、別途 USB-C to USB-A 変換ケーブルが必要です。

    別途用意した USB-C to USB-A 変換ケーブルを使用して、セルラー対応の USB モデムを Brume 3 の USB Type-C ポートに接続します。USB モデムのインターネット接続を、接続中のすべてのクライアントデバイスで共有する場合に便利です。

    Brume 3 がインターネットに正常に接続されると、Web 管理パネルの INTERNET ページで「Cellular」の横に緑のドットが表示され、Brume 3 本体の LED が白色に点灯します。

    詳細な手順については、[Cellular 経由でインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下は、Brume 3 の Web 管理パネルで利用できる機能の概要です。

## Clients {#clients}

Clients ページには、接続中のデバイス情報が表示されます。各クライアントについて、名前、IP アドレス、MAC アドレス、ダウンロード/アップロード速度、総トラフィックが表示され、クライアントのブロックやその他の操作も行えます。

Clients の設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} クラウド管理サービスは、GL.iNet ルーターへリモートアクセスして管理するための簡単な方法を提供します。

    GoodCloud の設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarp は、シームレスなリモートネットワークとリモートデバイス管理を提供する高度なネットワーキングプラットフォームです。GL.iNet ルーター連携向けに構築されており、ネットワーク全体にわたる包括的なデバイス管理をサポートし、上位デバイスと下位デバイスの両方を制御できます。ネットワーク全体の管理と将来的なハードウェアレベル制御を重視し、デバイス管理と安全で安定したネットワーク維持のための、より堅牢で信頼性の高いソリューションを提供します。

    AstroWarp の設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスと VPN サーバー間に安全で暗号化された通信を作成します。プライバシーとセキュリティを強化し（VPN クライアント）、リモートネットワークへのアクセス（VPN サーバー）も可能にします。Brume 3 は OpenVPN と WireGuard に対応しています。

=== "OpenVPN"

    Brume 3（およびその他の GL.iNet ルーター）は、強力なセキュリティを提供する OpenVPN プロトコルに対応しています。OpenVPN の設定については、次のチュートリアルを参照してください。

    * [OpenVPN クライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPN サーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 3（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルに対応しています。WireGuard の設定については、次のチュートリアルを参照してください。

    * [WireGuard クライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuard サーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク {#network}

=== "Multi-WAN"

    Multi-WAN は、Ethernet、Tethering、Cellular など複数のインターネット接続を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、スムーズで途切れにくいインターネットアクセスを維持できます。

    Multi-WAN の設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなど限られた範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。

    LAN の設定については、[Lan](../../interface_guide/lan.md)を参照してください。

=== "DNS"

    DNS ページでは、カスタム DNS サーバーの設定、DNS rebinding attack protection の有効化、すべてのクライアントの DNS 設定の上書き、カスタム DNS による VPN DNS の上書き許可を設定できます。また、DNS サーバー設定モードを自動にするか、Ethernet 接続の DNS サーバーを手動で指定するかを設定できます。

    DNS の設定については、[DNS](../../interface_guide/dns.md)を参照してください。

---

=== "Ethernet Port"

    Ethernet Port ページでは、WAN/LAN ポートの設定、WAN/LAN インターフェースの Ethernet への設定、WAN インターフェースの MAC モードと MAC アドレスの指定、ネットワークポートのネゴシエート速度の確認を行えます。

    Ethernet ポートの管理については、[Ethernet Port](../../interface_guide/ethernet_port.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。非常に大きなアドレス空間を提供し、インターネットに接続されるデバイス数の増加に対応するために必要な、ほぼ無制限の一意な IP アドレスを利用できます。

    IPv6 の設定については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

=== "IGMP Snooping"

    IGMP スヌーピングは、Ethernet スイッチでマルチキャストトラフィックを管理・制御するためのネットワーク最適化技術です。

    IGMP スヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

---

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する設定です。

    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in gateway"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN クライアントなど、メインルーターの機能を拡張します。

    Drop-in Gateway の設定については、次のリンクを参照してください。

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU 負荷を軽減し、トラフィックパケットの転送を高速化できます。

    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御 {#flow-control}

=== "DPI Engine"

    DPI（Deep Packet Inspection）は、インテリジェントなネットワーク管理の中核となる機能です。送信元または宛先アドレスしか識別できない従来のルーターの制約を克服し、データパケットのペイロードを詳細に分析します。特徴ライブラリとの照合により、ユーザーがアクセスしたアプリケーションや Web サイトを正確に識別し、きめ細かなトラフィック分類と制御を可能にします。

    GL.iNet の DPI 機能は [Netify](https://www.netify.ai/){target="_blank"} と統合されており、効率的に導入できる軽量な組み込みプラグインを採用しています。オンラインで更新される Netify のシグネチャデータベースにより、信頼性の高い管理を実現し、ネットワーク制御をより正確かつ効率的にします。

    詳細な手順については、[DPI Engine](../../interface_guide/dpi_engine.md)を参照してください。

=== "Data Statistics"

    Data Statistics は、ネットワーク使用状況をアプリケーションごとに分類して可視化するインテリジェントなトラフィック分析ダッシュボードを提供します。リアルタイムおよび過去のトラフィックを監視でき、ネットワークの状況把握と制御に役立ちます。

    詳細な手順については、[Data Statistics](../../interface_guide/data_statistics.md)を参照してください。

=== "Content Filter"

    Content Filter は、DPI ベースの分類を活用したスマートなオンライン保護機能です。有害または悪意のある Web サイトを自動的にブロックし、ネットワークをクリーンで安全な状態に保ちます。

    詳細な手順については、[Content Filter](../../interface_guide/content_filter.md)を参照してください。

---

=== "Parental Control"

    ペアレンタルコントロールは、お子様のデバイスを管理・制御するための機能です。画面使用時間の制限や、特定コンテンツへのアクセス制限などが含まれます。

    ペアレンタルコントロールの設定については、[Parental Control](../../interface_guide/parental_control.md)を参照してください。

=== "QoS"

    QoS（Quality of Service）は、ネットワークの混雑時にビデオ通話やゲームなどの重要な通信を優先して帯域幅の割り当てを最適化し、遅延を減らしてネットワーク全体のパフォーマンスを向上させます。この機能はローカルクライアントのトラフィックと VPN クライアントトンネルのトラフィックに適用されますが、ルーターが VPN サーバーとして動作している場合に受信するトラフィックには適用されません。

    詳細な手順については、[QoS](../../interface_guide/qos.md)を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファブロート（bufferbloat）」を最小限に抑え、ゲームや音声通話をよりスムーズにします。

    詳細な手順については、[SQM](../../interface_guide/sqm.md)を参照してください。

## セキュリティ {#security}

=== "Port Forwarding"

    ポートフォワーディングは、インターネット上のリモートサーバーやデバイスからプライベートネットワーク内のデバイスへアクセスできるようにします。

    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Management Control"

    Management Control では、不正アクセスからネットワークとルーターを保護するための各種セキュリティ設定を構成できます。このページには次のオプションがあります。

    * Local Access Control: ローカルネットワークに接続されたデバイスからルーターインターフェースへのアクセスを管理・制限します。
    * Remote Access Control: インターネット経由のリモートロケーションからルーターインターフェースへのアクセスを設定・制限し、外部脅威に対するセキュリティを強化します。
    * Open Ports on Router: ルーターで開いているポートを制御し、潜在的な脆弱性や不正アクセスを制限します。

    これらの設定は、安全なネットワーク環境を維持し、ルーターと接続デバイスの両方を保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "NAT Mode"

    NAT Mode ページでは、Full Cone NAT と SIP ALG（Application Layer Gateway）機能の有効化または無効化を設定できます。

    NAT 設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。

    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられた IP アドレスをリアルタイムで自動検出し、更新します。ドメイン名をルーターの動的なパブリック IP アドレスに対応付けるため、固定 IP アドレスがなくてもネットワークにリモートアクセスできます。

    Dynamic DNS の設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージは、複数のユーザーやデバイスがネットワーク経由でファイルへアクセスし共有できる、集中型のデータストレージソリューションです。

    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Home は、ホームネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングする DNS サーバーとして動作する、ネットワーク全体の広告・トラッカーブロックソリューションです。

    AdGuard Home の設定については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "ZeroTier"

    ZeroTier は、インターネット上に安全な仮想ネットワークを作成し、デバイス同士を同じローカルネットワーク上にあるかのように接続できるソフトウェア定義ネットワーキングソリューションです。

    ZeroTier の設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscale は、どこからでもデバイスやアプリケーションにアクセスできる VPN サービスです。

    Tailscale の設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "Tor"

    Tor は The Onion Router の略で、インターネット上で匿名通信を可能にするプライバシー重視のネットワークです。インターネットトラフィックを複数のボランティア運営サーバー（ノード）経由でルーティングし、ユーザーの場所や利用状況を分かりにくくすることで、オンライン活動の追跡を困難にします。

    * [Tor の設定方法](../../interface_guide/tor.md)

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

    詳細な設定手順と詳細情報については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Password ページでは、ルーターの管理インターフェース用パスワードを設定または変更し、許可されたユーザーのみが設定を変更できるようにします。

    セキュリティ上の理由から、**Prevent Weak Password** をオンにすることをおすすめします。

    **Prevent Weak Password** をオンにすると、新しいパスワードには次の要件が適用されます。

    * 5 文字以上、63 文字以下。
    * 英字（大文字と小文字を区別）、数字、記号 `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` を使用できます。
    * 英大文字、英小文字、数字、記号のうち少なくとも 2 種類を含める必要があります。

=== "Upgrade"

    Upgrade ページは、ルーターのファームウェアを最新バージョンへ更新し、性能、セキュリティ、新機能を向上させるために使用します。このページには 2 種類のアップグレード方法があります。

    * Firmware Online Upgrade: メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * Firmware Local Upgrade: コンピューターからファームウェアファイルを手動でアップロードしてルーターを更新し、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、ルーターを最新の改善や修正が含まれた状態に保てます。

    詳細な設定手順と詳細情報については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前に定義したスケジュールに基づいて各種ルーター機能を自動化し、利便性と効率を高められます。このページの主な機能は次のとおりです。

    * LED Display Schedule: 特定の時間帯にルーターの LED ライトを自動的にオンまたはオフにするスケジュールを設定し、光害を減らせます。
    * Schedule Reboot: 指定した間隔でルーターを自動再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。

    これらのスケジュール機能により、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細な設定手順と詳細情報については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

=== "Time Zone"

    Time Zone ページでは、ルーターに正しいタイムゾーンを設定し、すべてのスケジュールタスク、ログ、システムイベントが現地時間に基づいて正確に記録されるようにします。この設定は、正確な記録の維持と時間ベース設定の適切な実行に重要です。

    詳細な設定手順と詳細情報については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Log"

    Log ページでは、トラブルシューティングやパフォーマンス監視に役立つ、ルーターの動作やイベントを記録した各種ログへアクセスできます。このページには次の項目があります。

    * System Log: システムレベルのイベントや動作に関する詳細ログ。
    * Kernel Log: カーネルの処理やイベントに関するログ。
    * Crash Log: システムクラッシュやエラーの記録。重大な問題の診断に役立ちます。
    * Cloud Log: ルーターに統合された GoodCloud サービスに関連する操作や通信のログ。
    * Nginx Log: ルーターで Nginx Web サーバーを使用している場合のログ。Web トラフィックやサーバー動作の詳細を記録します。

    さらに、このページには Export Log ボタンがあり、収集されたすべてのログをテクニカルサポート分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に役立ちます。

    詳細な設定手順と詳細情報については、[Log](../../interface_guide/log.md)を参照してください。

---

=== "Reset Firmware"

    Reset Firmware ページでは、現在のファームウェアバージョンをデフォルト設定へリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定に戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細な設定手順と詳細情報については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションへアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えてルーターの設定や機能を細かく調整できます。詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な設定手順と詳細情報については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
