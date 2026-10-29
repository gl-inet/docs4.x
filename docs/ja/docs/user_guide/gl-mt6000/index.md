# Flint 2 (GL-MT6000) ユーザーガイド {#flint-2-gl-mt6000-user-guide}

## 製品概要 {#product-overview}

Flint 2 (GL-MT6000) は、大容量データ通信、多数のデバイス接続、または超低遅延のゲーム環境に最適な Wi-Fi 6 対応の家庭・オフィス向けルーターです。Flint 2 は最大 900Mbps の高速 WireGuard VPN を提供します。また、マルチWAN、フェイルオーバー、ロードバランスなどの高度なネットワーク冗長化機能により、途切れのないネットワーク接続を実現します。

![gl-mt6000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/hardware_info/gl-mt6000_interface.jpg){class="glboxshadow"}

## 同梱物 {#package-contents}

- 1 x Flint 2 (GL-MT6000)
- 1 x ユーザーマニュアル
- 1 x サンキューカード
- 1 x イーサネットケーブル
- 1 x 電源アダプター
- 1 x 変換プラグ（配送先の国に応じた仕様）

![gl-mt6000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/first_time_setup/gl-mt6000_unboxing.jpg){class="glboxshadow"}

以下の Flint 2 の開封動画をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ru1O-zxKgKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Flint 2 のセットアップ方法 {#how-to-set-up-flint-2}

セットアップ動画を見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>（この動画では別の GL.iNet ルーターを使ってセットアップを説明していますが、手順は Flint 2 やその他のルーターモデルでも同じです。）</small>

### 1. 電源を入れる {#1-power-on}

2 ピース構成の電源アダプターを組み立ててルーターに接続し、コンセントに差し込みます。自動的に起動します。

### 2. デバイスを接続する {#2-connect-device}

デバイス（例: コンピューター、ノート PC、スマートフォン）を Wi-Fi またはイーサネットでルーターに接続します。

- イーサネット

    イーサネットケーブルを使用して、デバイスをルーターの LAN ポートに接続します。

- Wi-Fi

    デバイスで **設定** → **WLAN** を開き、利用可能なネットワーク一覧からルーターの Wi-Fi 名を見つけてパスワードを入力し、ネットワークに参加します。初期のネットワーク名とパスワードはルーター本体のラベルに記載されています。

### 3. Web管理パネルにログインする {#3-log-in-to-web-admin-panel}

Web ブラウザーを開き、アドレスバーに `192.168.8.1` を入力してログインします。言語を選択し、管理者パスワードを設定してから **Apply** をクリックします。

Wi-Fi 情報を確認する際、Wi-Fi 情報を変更した場合は、更新後の認証情報を使用してデバイスをルーターの Wi-Fi に再接続する必要があります。

### 4. インターネット設定 {#4-internet-setup}

**注：** 以下の手順は GL.iNet Web管理パネルを使用して設定するユーザー向けです。GL.iNet アプリをご利用の場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}して画面の指示に従ってください。

対応しているインターネット接続方法（イーサネット、リピーター、テザリング、セルラー）のいずれかを使用して、Flint 2 を設定します。[マルチWAN](../../interface_guide/multi-wan.md) 機能を使用する場合は、複数のインターネット接続を設定してください。

=== "イーサネット"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_ethernet.png){class="glboxshadow"}

    ルーターの WAN ポートとモデムなどの上流デバイスをイーサネットケーブルで接続します。

    インターネットへの接続に成功すると、INTERNET ページのイーサネットセクションに緑のドットが表示されます。

    詳細については[イーサネットケーブルでインターネットに接続する方法](../../interface_guide/internet_ethernet.md)をご参照ください。

=== "リピーター"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_repeater.png){class="glboxshadow"}

    1. Web管理パネルの INTERNET ページでリピーターセクションを見つけ、**Connect** をクリックします。
    2. 利用可能なネットワークから Wi-Fi ネットワークを選択します。
    3. パスワードを入力し、**Apply** をクリックします。

    インターネットへの接続に成功すると、INTERNET ページのリピーターセクションに緑のドットが表示されます。

    詳細については[既存の Wi-Fi ネットワーク経由でインターネットに接続する方法](../../interface_guide/internet_repeater.md)をご参照ください。

=== "テザリング"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_tethering.png){class="glboxshadow"}

    1. USB ケーブルを使用してモバイルデバイス（スマートフォンや USB ドングルなど）をルーターの USB ポートに接続します。
    2. モバイルデバイスの設定で USB テザリングを有効にします。
    3. Web管理パネルの INTERNET ページで、テザリングセクションの **Connect** をクリックします。

    インターネットへの接続に成功すると、INTERNET ページのテザリングセクションに緑のドットが表示されます。

    詳細については[USB テザリング経由でインターネットに接続する方法](../../interface_guide/internet_tethering.md)をご参照ください。

=== "セルラー"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_cellular.png){class="glboxshadow"}

    セルラー対応の USB モデムをルーターの USB ポートに挿入します。USB モデムのインターネットを接続された全デバイスで共有する場合に便利です。

    インターネットへの接続に成功すると、INTERNET ページのセルラーセクションに緑のドットが表示されます。

    詳細については[セルラー経由でインターネットに接続する方法](../../interface_guide/internet_cellular.md)をご参照ください。

---

## DNS {#dns}

ルーターのDNS設定は、ドメイン名をIPアドレスに変換する方法を制御します。このページでは、上流デバイスから自動取得したDNSサーバーを使用するか、カスタムDNSサーバーを設定できます。DNSオプションの設定や静的ホストルールの編集もできます。

詳細については、[DNS](../../interface_guide/dns_v4.11.md)を参照してください。

## Wireless {#wireless}

ワイヤレスページでは、5 GHz および 2.4 GHz Wi-Fi ネットワークの設定（Wi-Fi の有効/無効、送信電力、SSID、ランダム BSSID、セキュリティモード、パスワード、SSID 公開設定、Wi-Fi モード、帯域幅、チャンネル）を行えます。

ワイヤレスの設定については[ワイヤレス](../../interface_guide/wireless.md)をご参照ください。

## Mesh {#mesh}

Meshは、Wi-Fi EasyMesh™規格に基づいて家全体のWi-Fiカバレッジを拡張し、シームレスなローミングを実現する機能です。複数のGL.iNetルーターがある場合は、1台をメインルーター、残りをメッシュノードとして設定すると、家の中を移動してもシームレスにWi-Fiを利用できます。

詳細については、[Mesh](../../interface_guide/mesh.md)を参照してください。

## Clients {#clients}

クライアントページには、接続されたデバイスの情報（デバイス名、接続タイプ（Ethernet 経由か Wi-Fi 経由か）、IP アドレスと MAC アドレス、ダウンロード/アップロード速度、総トラフィック）が表示されます。IP の予約やクライアントのブロックなどの操作も行えます。

クライアントの設定については[クライアント](../../interface_guide/clients.md)をご参照ください。

## クラウドサービス {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Accountを使用すると、デバイスとクラウドサービスを接続して管理できます。GoodCloudとglinet Appの両方にシームレスにアクセスでき、安全で快適に利用できます。これにより、いつでもどこからでも、より便利にネットワークを管理できます。

    GL.iNet Accountの設定については、[GL.iNet Account](../../interface_guide/glinet_account.md)を参照してください。

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} サービスは、GL.iNet ルーターにリモートアクセスして管理するための簡単な方法を提供します。

    GoodCloud の設定については[GoodCloud](../../interface_guide/cloud.md)をご参照ください。

=== "GoodPAS"

    GoodPASは、シームレスなリモートアクセスとデバイス管理を実現する高度なネットワーク機能です。GL.iNetルーターとの統合専用に設計されており、トラフィック難読化機能を備えたAmneziaWGプロトコルを使用して、安全で安定した接続を確保します。GoodPASを使用すると、ホームネットワークにリモートアクセスできます。自宅のルーターがGoodPASの出口ノードとして機能している場合、GoodPAS経由で送信されるインターネットトラフィックには、そのルーターのWANパブリックIPアドレスが使用されます。

    GoodPAS の設定については、[GoodPAS](../../interface_guide/goodpas.md) を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスと VPN サーバーの間に安全で暗号化された通信を作成します。プライバシーとセキュリティを強化し（VPN クライアント）、リモートネットワークへのアクセスも可能にします（VPN サーバー）。Flint 2（およびその他の GL.iNet ルーター）は、OpenVPN と WireGuard に対応しています。

=== "OpenVPN"

    Flint 2（およびその他の GL.iNet ルーター）は、強固なセキュリティを提供する OpenVPN プロトコルをサポートしています。OpenVPN のセットアップには以下のチュートリアルに従ってください：

    * [OpenVPN クライアントのセットアップ方法](../../interface_guide/openvpn_client.md)
    * [OpenVPN サーバーのセットアップ方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 2（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルをサポートしています。WireGuard のセットアップには以下のチュートリアルに従ってください：

    * [WireGuard クライアントのセットアップ方法](../../interface_guide/wireguard_client.md)
    * [WireGuard サーバーのセットアップ方法](../../interface_guide/wireguard_server.md)

## ネットワーク {#network}

=== "マルチWAN"

    マルチ WAN は、複数のインターネット接続（セルラー、リピーター、イーサネットなど）を同時に設定できるネットワーキング機能です。現在のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れのないインターネットアクセスを維持できます。

    マルチ WAN の設定については[マルチWAN](../../interface_guide/multi-wan.md)をご参照ください。

=== "LAN"

    LANページでは、メインネットワーク、ゲストネットワーク、IoTネットワーク、カスタムVLANネットワークの設定と管理を一元的に行えます。複数のサブネットを作成・管理して、異なる種類のデバイスやトラフィックを分離できます。

=== "イーサネットポート"

    イーサネットポートページでは、WAN と LAN ポートの設定、WAN/LAN インターフェイスのイーサネットへの設定、WAN インターフェイスの MAC モードと MAC アドレスの指定、およびネットワークポートのネゴシエート速度の確認が行えます。

    Ethernet Portの設定については、[Ethernet Port](../../interface_guide/ethernet_port_v4.10.md)を参照してください。

=== "IPv6"

    IPv6（インターネットプロトコルバージョン 6）は IPv4 の後継として設計された最新のインターネットプロトコルです。大幅に広大なアドレス空間を提供し、インターネットに接続されるデバイスの増加に対応するための実質的に無制限のユニーク IP アドレスを可能にします。

    IPv6 の設定については[IPv6](../../interface_guide/ipv6.md)をご参照ください。

<br>

=== "IGMPスヌーピング"

    IGMP スヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理・制御するために使用されるネットワーク最適化技術です。

    IGMP スヌーピングの設定については[IGMPスヌーピング](../../interface_guide/igmp_snooping.md)をご参照ください。

=== "ネットワークモード"

    Network Modeページでは、さまざまなネットワーク展開要件に合わせてルーターの動作役割を設定できます。家庭のWi-Fiカバレッジから企業向けマルチリンクネットワークまで、用途に応じたモードを選択でき、各モードでは特定のルーター機能を有効または無効にして性能を最適化します。

    設定方法については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "ドロップイン・ゲートウェイ"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN クライアントなど、メインルーターの機能を拡張します。

    ドロップインゲートウェイの設定については、以下のリンクを参照してください：

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Drop-in Gatewayを設定する](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "ネットワークアクセラレーション"

    ネットワークアクセラレーションは CPU 負荷を軽減し、トラフィックパケット転送を高速化します。

    ネットワークアクセラレーションの設定については[ネットワークアクセラレーション](../../interface_guide/network_acceleration.md)をご参照ください。

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

<br>

=== "QoS"

    QoS（Quality of Service）は、ネットワークの混雑時にビデオ通話やゲームなどの重要な通信を優先し、帯域幅の割り当てを最適化します。これにより、遅延を軽減してネットワーク全体の性能を向上させます。この機能はローカルクライアントのトラフィックとVPNクライアントのトンネルトラフィックに適用されますが、ルーターがVPNサーバーとして受信するトラフィックには適用されません。

    詳細は[QoS](../../interface_guide/qos.md)を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファブロート」を抑え、ゲームや音声通話をより滑らかにします。

    詳細は[SQM](../../interface_guide/sqm.md)を参照してください。

=== "ペアレンタルコントロール"

    ペアレンタルコントロールは、お子様のデバイスを管理・制御するために設計された機能で、スクリーンタイムの制限や特定コンテンツへのアクセス制限が含まれます。

    ペアレンタルコントロールの設定については、[Parental Control](../../interface_guide/parental_control_v4.9.md)を参照してください。

## セキュリティ {#security}

=== "Security Scan"

    Security Scanは、ルーターのセキュリティチェックを実行します。ルーターのセキュリティ設定を評価し、セキュリティスコア、リスクの警告、最適化の提案を表示します。スキャン結果に基づいて設定を調整し、ルーターのセキュリティを向上させることができます。

    詳細については、[Security Scan](../../interface_guide/security_scan.md)を参照してください。

=== "ACL"

    ACL（Access Control List）では、接続プロトコル、デバイスアドレス、ポートに基づくルールを作成し、ネットワークトラフィックを管理できます。ネットワークアクセスを許可するかブロックするかを制御します。複数のACLルールが競合する場合は、優先度の高いルールが適用されます。

    詳細は[ACL](../../interface_guide/acl.md)を参照してください。

=== "Port Forwarding"

    ポート転送は、インターネット上のリモートサーバーやデバイスがプライベートネットワーク内のデバイスにアクセスできるようにします。

    ポートフォワーディングを設定するには、[Port Forwarding](../../interface_guide/port_forwarding.md) を参照してください。

<br>

=== "UPnP"

    UPnP（Universal Plug and Play）を使用すると、対応するLANデバイスやアプリケーションがGL.iNetルーターにポートマッピングを自動的に要求できます。これらのマッピングは、受信したWANトラフィックを指定されたLAN IPアドレスとポートに転送します。これにより、ポート転送ルールを手動で設定せずに、外部クライアントがローカルサービスに接続できます。

    詳細については、[UPnP](../../interface_guide/upnp.md)を参照してください。

=== "Admin Access"

    Admin Accessでは、不正なアクセスからネットワークとルーターを保護するための各種セキュリティ設定を行えます。このページには次の項目があります。

    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからのルーターインターフェイスへのアクセスを管理・制限します。
    * リモートアクセス制御：インターネット経由のリモートロケーションからのルーターインターフェイスへのアクセスを設定・制限し、外部脅威に対するセキュリティを強化します。
    * ルーターのオープンポート：ルーター上のオープンポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    詳細は[Admin Access](../../interface_guide/admin_access.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "プラグイン"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズと拡張を可能にします。

    プラグインの設定については[プラグイン](../../interface_guide/plugins.md)をご参照ください。

=== "ダイナミック DNS"

    ダイナミック DNS（DDNS）は、ドメインに関連付けられた IP アドレスをリアルタイムで自動的に検出・更新します。ドメイン名をルーターの動的なパブリックIPアドレスに対応付けるため、固定IPアドレスがなくてもネットワークにリモートアクセスできます。

    ダイナミック DNS の設定については[ダイナミック DNS](../../interface_guide/ddns.md)をご参照ください。

=== "ネットワークストレージ"

    ネットワークストレージとは、複数のユーザーやデバイスがネットワーク経由でファイルにアクセス・共有できる集中型データストレージソリューションです。

    ネットワークストレージの設定については[ネットワークストレージ](../../interface_guide/network_storage.md)をご参照ください。

<br>

=== "AdGuard Home"

    AdGuard Home は、ネットワーク全体の広告・トラッカーブロックソリューションです。DNS サーバーとして機能し、ホームネットワークに接続された全デバイスの不要なコンテンツをフィルタリングします。

    AdGuard Home の設定については[AdGuard Home](../../interface_guide/adguardhome.md)をご参照ください。

=== "Tailscale"

    Tailscale は、どこからでもデバイスやアプリケーションにアクセスできる VPN サービスです。

    Tailscale の設定については[Tailscale](../../interface_guide/tailscale.md)をご参照ください。

=== "ZeroTier"

    ZeroTier は、インターネット上で安全な仮想ネットワークを作成し、デバイスを同じローカルネットワーク上にあるかのように接続するソフトウェア定義ネットワーキングソリューションです。

    ZeroTier の設定については[ZeroTier](../../interface_guide/zerotier.md)をご参照ください。

=== "Tor"

    Tor（The Onion Router）は、インターネット上で匿名通信を可能にするプライバシー重視のネットワークです。ボランティアが運営するサーバー（ノード）を介してトラフィックをルーティングし、ユーザーの位置情報や利用状況を難読化することで、オンラインアクティビティの追跡を困難にします。

    詳細は[Tor](../../interface_guide/tor.md)を参照してください。

## システム {#system}

=== "概要"

    概要ページは、ルーターの現在の状態とパフォーマンスの包括的なスナップショットを提供します。このページでは以下を確認できます：

    * CPU 平均負荷：ルーターの CPU 平均負荷を監視し、パフォーマンスの評価とボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理を支援します。
    * LED 制御：ルーターの LED ライトのオン/オフを切り替え、視覚的インジケーターをカスタマイズします。
    * フラッシュ使用量：ルーターのフラッシュストレージの使用状況を確認し、十分な容量を確保します。
    * デバイス情報：稼働時間、ホスト名、モデル、アーキテクチャ、OpenWrt バージョン、カーネルバージョン、デバイス ID、デバイス MAC、デバイス S/N などのシステム詳細情報にアクセスできます。
    * 外部ストレージ：USB ドライブや TF カードなど、ルーターに接続された外部ストレージデバイスの状態を確認できます。

    これらの機能により、ルーターの動作を効果的に管理・監視するための重要な情報と制御を利用できます。

    詳細については[概要](../../interface_guide/system_overview.md)をご参照ください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェース用パスワードを管理し、許可されたユーザーだけが設定を変更できるようにします。

    詳細は[Admin Password](../../interface_guide/admin_password.md)を参照してください。

=== "アップグレード"

    アップグレードページは、ルーターのファームウェアを最新バージョンに更新し、性能、セキュリティ、新機能を向上させるために使用します。このページには 2 つのアップグレードオプションがあります：

    * ファームウェアオンラインアップグレード：メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルを手動でアップロードしてルーターを更新し、アップグレードするバージョンとタイミングを制御できます。

    これらのオプションにより、ルーターを最新の改善や修正が含まれた状態に保てます。

    詳細については[アップグレード](../../interface_guide/upgrade.md)をご参照ください。

=== "スケジュールされたタスク"

    スケジュールされたタスクページでは、事前に定義されたスケジュールに基づいて各種ルーター機能を自動化し、利便性と効率を高められます。主な機能は以下のとおりです：

    * LED ディスプレイスケジュール：特定の時間帯にルーターの LED ライトを自動的にオン/オフにするスケジュールを設定し、光害を減らせます。
    * スケジュール再起動：指定した間隔でルーターを自動的に再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * 5GHz / 2.4GHz Wi-Fi ステータススケジュール：5GHz / 2.4GHz Wi-Fi バンドを制御するスケジュールを設定し、ネットワークの可用性と消費電力を管理しやすくします。

    これらのスケジュール機能により、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細については[スケジュールされたタスク](../../interface_guide/scheduled_tasks.md)をご参照ください。

=== "タイムゾーン"

    タイムゾーンページでは、ルーターの正しいタイムゾーンを設定し、すべてのスケジュールされたタスク、ログ、システムイベントが現地時間に合わせて正確にタイムスタンプされるようにします。この設定は、正確な記録の維持と時間ベースの設定を適切に実行するために重要です。

    詳細については[タイムゾーン](../../interface_guide/time_zone.md)をご参照ください。

=== "ファームウェアのリセット"

    ファームウェアのリセットページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。このプロセスにより、現在インストールされているファームウェアのデフォルト設定にルーターが復元されます。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細については[ファームウェアのリセット](../../interface_guide/reset_firmware.md)をご参照ください。

<br>

=== "ログ"

    ログページでは、ルーターのアクティビティとイベントを記録するさまざまなログにアクセスでき、トラブルシューティングとパフォーマンス監視に役立ちます。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの動作とイベントに関連するログ。
    * クラッシュログ：重大な問題の診断に役立つシステムクラッシュとエラーの記録。
    * クラウドログ：ルーターに統合された GoodCloud サービスに関連する操作やアクティビティのログ。
    * Nginx ログ：ルーターで Nginx Web サーバーを使用している場合のログ。Web トラフィックやサーバー動作の詳細を記録します。

    さらに、このページには Export Log ボタンがあり、収集されたすべてのログをテクニカルサポート分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に役立ちます。

    詳細については[ログ](../../interface_guide/log.md)をご参照ください。

=== "詳細設定"

    詳細設定ページでは、OpenWrt LuCI インターフェイスを通じて高度な設定オプションにアクセスでき、上級ユーザーがルーターの設定と機能を細かく調整できます。詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細については[詳細設定](../../interface_guide/advanced_settings.md)をご参照ください。
