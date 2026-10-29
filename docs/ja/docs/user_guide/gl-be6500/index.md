# Flint 3e (GL-BE6500) ユーザーガイド {#flint-3e-gl-be6500-user-guide}

## 製品概要 {#product-overview}

Flint 3e (GL-BE6500) は、家庭ユーザーとスモールオフィス向けのデュアルバンドWi-Fi 7デスクトップルーターです。Multi-Link Operation（MLO）に対応し、互換性のあるデバイスは2.4 GHzと5 GHzの両帯域のリンクを使用して、干渉や混雑の影響を軽減できます。4K-QAM変調は、その他の条件が同一の場合、Wi-Fi 6の1024-QAMと比べて最大20%高い理論データレートを提供します。ルーターはデュアルバンド合計で最大6452 Mbpsの理論データレートに対応し、5 GHz帯では4×4 MIMOと160 MHzのチャンネル幅をサポートします。実際の速度はクライアントの性能やネットワーク環境によって異なります。

2.5G Ethernetポートを5基、USB 3.0ポートを1基搭載し、高速な有線接続とストレージ拡張に対応します。さらに、30以上のVPNサービスに対応し、WireGuard®とOpenVPN-DCOで最大680Mbpsの強力なVPNパフォーマンスを発揮します。無料のBark Parental Controlも利用でき、パフォーマンス、実用性、セキュリティを高いレベルで両立しています。

![gl-be6500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/hardware_info/be6500_interface.jpg){class="glboxshadow"}

**注：** Flint 3eとFlint 3の外観上の違いはシルク印刷の色です。Flint 3eは青、Flint 3は白です。

## パッケージ内容 {#package-contents}

- 1 x Flint 3e (GL-BE6500)
- 1 x 電源アダプター
- 1 x Ethernetケーブル
- 1 x ユーザーマニュアル
- 1 x サンキューカード
- 1 x 変換プラグ（配送先の国に応じたもの）

Flint 3eの開封動画は以下をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-E0LtWqshk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Flint 3eの設定方法 {#how-to-set-up-flint-3e}

以下のセットアップ動画を見るか、次の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/R40QsUFYuUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Flint 3eの電源を入れる {#1-power-on}

2ピース式の電源アダプターを組み立てます。ルーターに接続し、コンセントに挿すと自動的に起動します。

### 2. デバイスを接続する {#2-connect-device}

Wi-FiまたはEthernetを使用してデバイス（コンピュータ、ラップトップ、スマートフォンなど）をルーターに接続します。

- Ethernet

    Ethernetケーブルを使用してデバイスをルーターのLANポートに接続します。

- Wi-Fi

    デバイスで、Settings -> WLANを開き、利用可能なネットワークリストからルーターのWi-Fiネットワーク名を見つけ、パスワードを入力してネットワークに参加します。デフォルトのネットワーク名とパスワードはルーターのラベルに印刷されています。

### 3. Web管理パネルにログインする {#3-log-in-to-web-admin-panel}

Webブラウザーでアドレスバーに`192.168.8.1`を入力してログインします。言語を選択し、管理者パスワードを設定して、**Apply**をクリックします。

### 4. Flint 3eをインターネットに接続する {#4-internet-setup}

**注：** 以下の説明は、GL.iNet Web管理パネルでルーターを設定するユーザーに適用されます。GL.iNetアプリを使用する場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}して画面の説明に従ってください。

サポートされているインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用してFlint 3eを設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_ethernet.jpg){class="glboxshadow"}

    Flint 3eのWANポートをEthernetケーブルで上位デバイス（モデムなど）に接続します。
    
    インターネットに正常に接続されると、INTERNETページのEthernetセクションに緑色のドットが表示されます。

    詳細な手順については、[Ethernetケーブルでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_repeater.jpg){class="glboxshadow"}

    1. Web管理パネルのINTERNETページで、Repeaterセクションを見つけ、**Connect**をクリックします。
    2. 利用可能なWi-Fiネットワークから選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのRepeaterセクションに緑色のドットが表示されます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSBドングルなど）をUSBケーブルでルーターのUSBポートに接続します。
    2. モバイルデバイスでSettingsを開き、USB Tetheringを有効にします。
    3. Web管理パネルのINTERNETページで、Tetheringセクションの**Connect**をクリックします。
    
    ルーターがインターネットに正常に接続されると、INTERNETページのTetheringセクションに緑色のドットが表示されます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_cellular.jpg){class="glboxshadow"}

    Flint 3eのUSBポートにセルラーUSBモデムを挿入します。USBモデムのインターネット接続を、接続中のすべてのデバイスで共有する場合に便利です。

    インターネットに正常に接続されると、INTERNETページのCellularセクションに緑色のドットが表示されます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下は、Flint 3eのWeb管理パネルの機能の概要です。

## Wireless {#wireless}

Wirelessページでは、5 GHzと2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、送信出力（TX power）の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSIDの表示/非表示の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

また、Flint 3eはMLO Wi-Fi（Multi-Link Operation）をサポートしており、複数のWi-Fiネットワークを同時に組み合わせて、より高い帯域幅とより信頼性の高い接続を実現します。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients {#clients}

Clientsページには、接続されたデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレスとMACアドレス、ダウンロード速度とアップロード速度、合計トラフィックが表示され、クライアントをブロックしたりその他のアクションを実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}は、GL.iNetルーターにリモートでアクセスして管理するための簡単な方法を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarpは、シームレスなリモートネットワークとリモートデバイス管理を提供するために設計された高度なネットワーキングプラットフォームです。GL.iNetルーター連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位と下位のデバイス制御を可能にします。ネットワーク全体の管理と将来のハードウェアレベル制御のサポートに焦点を当てたAstroWarpは、デバイスの管理と安全で安定したネットワークの維持のためのより堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスと VPN サーバー間に安全で暗号化された通信を作成します。プライバシーとセキュリティを強化し（VPN クライアント）、リモートネットワークへのアクセス（VPN サーバー）も可能にします。Flint 3e は OpenVPN と WireGuard に対応しています。

=== "OpenVPN"
    
    Flint 3e（およびその他のGL.iNetルーター）は強力なセキュリティを提供するOpenVPNプロトコルをサポートしています。OpenVPNを設定するには、以下のチュートリアルに従ってください：

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Flint 3e（およびその他のGL.iNetルーター）は、高速性と利便性を備えたWireGuardプロトコルをサポートしています。WireGuardを設定するには、以下のチュートリアルに従ってください：

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク {#network}

=== "Multi-WAN"

    Multi-WAN は、Ethernet、Tethering、Cellular など複数のインターネット接続を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、スムーズで途切れにくいインターネットアクセスを維持できます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなど、限られた地理的領域内でコンピュータとデバイスを接続するネットワークです。高速データ転送とリソース共有を可能にし、デバイスが効率的に相互通信できます。
    
    LANの設定については、[LAN](../../interface_guide/lan.md)を参照してください。

=== "Guest Network"

    IPv4プライベートアドレス範囲192.168.0.0/16、172.16.0.0/12、または10.0.0.0/8内でサブネットを設定し、ゲートウェイとネットマスクIPアドレスを指定し、ゲストネットワークのAP分離などのセキュリティ設定を構成できます。

    ゲストネットワークの設定については、[Guest Network](../../interface_guide/guest_network.md)を参照してください。

=== "IoT Network"

    IoTデバイス専用のWi-Fiネットワークを作成できます。メインネットワークから分離することで、互換性とセキュリティを向上させます。

    IoT Network の設定については、[Lan](../../interface_guide/iot_network.md)を参照してください。

---

=== "DNS"

    DNSページでは、カスタムDNSサーバーの設定、DNSリバインディング攻撃対策の有効化、すべてのクライアントのDNS設定の上書き、およびカスタムDNSによるVPN DNSの上書きの許可を設定できます。上流デバイスから自動的に取得したDNSサーバーを使用するか、カスタムDNSサーバーを手動で指定できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "Ethernet Port"

    Ethernet Portページでは、WANポートとLANポートの設定、WAN/LANインターフェースのEthernetへの設定、WANインターフェースのMACモードとMACアドレスの指定、ネットワークポートのネゴシエート速度の確認を行えます。

    Ethernetポートの管理については、[Ethernet Port](../../interface_guide/ethernet_port.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4を置き換えるために設計された最新のインターネットプロトコルです。非常に大きなアドレス空間を提供し、インターネットに接続されるデバイス数の増加に対応するために不可欠な、ほぼ無制限の一意なIPアドレスを利用できます。
    
    IPV6の設定については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

=== "IGMP Snooping"

    IGMPスヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。
    
    IGMPスヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

---

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークに接続し、他のデバイスと通信する方法を決定する構成設定を指します。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in gateway"

    ドロップインゲートウェイは、AdGuard Home、暗号化DNS、VPNクライアントを含むメインルーターの機能を拡張します。
    
    ドロップインゲートウェイの設定については、以下のリンクを参照してください：
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU負荷を削減し、トラフィックパケットの転送を高速化できます。
    
    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御 {#flow-control}

=== "DPI Engine"

    DPI（Deep Packet Inspection）は、インテリジェントなネットワーク管理の中核となる機能です。送信元または宛先アドレスのみを識別する従来のルーターの制約を超え、パケットのペイロードを詳細に分析します。シグネチャライブラリとの照合により、ユーザーが利用するアプリケーションやWebサイトを正確に識別し、きめ細かなトラフィックの分類と制御を実現します。
    
    GL.iNetのDPI機能は[Netify](https://www.netify.ai/){target="_blank"}と統合され、効率的に導入できる軽量な組み込みプラグインを使用しています。Netifyのオンライン更新対応シグネチャデータベースにより、信頼性の高い管理と、より正確で効率的なネットワーク制御が可能になります。

    詳細な手順については、[DPI Engine](../../interface_guide/dpi_engine.md)を参照してください。

=== "Data Statistics"

    Data Statisticsは、アプリケーション別にネットワーク使用量を分類して可視化するインテリジェントなトラフィック分析ダッシュボードです。リアルタイムと過去のトラフィックを監視し、ネットワークの状態を把握して管理できます。

    詳細な手順については、[Data Statistics](../../interface_guide/data_statistics.md)を参照してください。

=== "Content Filter"

    Content Filterは、DPIベースの分類を利用したオンライン保護機能です。有害または悪意のあるWebサイトを自動的にブロックし、ネットワークを安全に保ちます。

    詳細な手順については、[Content Filter](../../interface_guide/content_filter.md)を参照してください。

---

=== "QoS"

    QoS（Quality of Service）は、ネットワークの混雑時にビデオ通話やゲームなどの重要な通信を優先し、帯域幅の割り当てを最適化します。これにより、遅延を軽減してネットワーク全体の性能を向上させます。この機能はローカルクライアントのトラフィックとVPNクライアントのトンネルトラフィックに適用されますが、ルーターがVPNサーバーとして受信するトラフィックには適用されません。

    詳細な手順については、[QoS](../../interface_guide/qos.md)を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファブロート」を抑え、ゲームや音声通話をより滑らかにします。

    詳細な手順については、[SQM](../../interface_guide/sqm.md)を参照してください。

=== "Parental Control"

    Parental Controlは、子どものデバイスを管理および制御するための機能です。画面の使用時間を制限し、特定のコンテンツへのアクセスを制限できます。

    ペアレンタルコントロールの設定については、[Parental Control](../../interface_guide/parental_control_v4.9.md)を参照してください。

## セキュリティ {#security}

=== "Port Forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "ACL"

    ACL（Access Control List）では、接続プロトコル、デバイスアドレス、ポートに基づくルールを作成し、ネットワークトラフィックを管理できます。ネットワークアクセスを許可するかブロックするかを制御します。複数のACLルールが競合する場合は、優先度の高いルールが適用されます。

    詳細は[ACL](../../interface_guide/acl.md)を参照してください。

=== "Admin Access"

    Admin Accessでは、不正なアクセスからネットワークとルーターを保護するための各種セキュリティ設定を行えます。このページには次の項目があります。

    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーターのインターフェースへのアクセスを管理および制限します。
    * リモートアクセス制御：インターネット経由でリモートの場所からルーターのインターフェースへのアクセスを構成および制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    詳細は[Admin Access](../../interface_guide/admin_access.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG（Application Layer Gateway）機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。
    
    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。ドメイン名をルーターの動的なパブリックIPアドレスに対応付けるため、固定IPアドレスがなくてもネットワークにリモートアクセスできます。
    
    Dynamic DNSの設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージとは、複数のユーザーとデバイスがネットワーク上でファイルにアクセスして共有できる集中型データストレージソリューションを指します。
    
    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Homeは、ネットワーク全体の広告およびトラッカーブロッキングソリューションであり、家庭内ネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングするDNSサーバーとして機能します。
    
    AdGuard Homeの設定については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "Bark"

    Flint 3eに統合されたBarkサービスは、子どものデジタル環境を保護し、包括的なオンライン保護を提供します。通常は有料サブスクリプションが必要ですが、Barkとの提携により、GL.iNetはFlint 3eを含む一部のルーターモデルでBark Homeプランを無料提供しています。追加料金なしで高度な監視とアラートを利用できます。

    詳細は[Bark](../../interface_guide/bark.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサービスです。
    
    Tailscaleの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "ZeroTier"

    ZeroTierは、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全に仮想ネットワークを作成し、デバイスが同一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tor"

    Tor（The Onion Routerの略）は、インターネット上での匿名通信を可能にするプライバシー重視のネットワークです。インターネットトラフィックをボランティアが運営する一連のサーバー（ノード）経由でルーティングしてユーザーの位置情報や利用状況を隠し、オンライン活動の追跡を困難にします。
    
    詳細は[Tor](../../interface_guide/tor.md)を参照してください。

## システム {#system}

=== "Overview"

    Overviewページでは、ルーターの現在の状態とパフォーマンス指標をまとめて確認できます。このページでは以下を表示できます：

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーターのフラッシュストレージの使用率を確認し、ファームウェアと設定データのための十分な空間を確保します。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーターの操作を効果的に管理および監視するのに役立つ重要な洞察とコントロールを提供します。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェース用パスワードを管理し、許可されたユーザーだけが設定を変更できるようにします。

    詳細は[Admin Password](../../interface_guide/admin_password.md)を参照してください。

=== "Upgrade"

    Upgradeページは、ルーターのファームウェアを最新バージョンにアップデートするために使用され、パフォーマンス、セキュリティ、新機能の向上を確保します。このページには2つのアップグレードオプションがあります：

    * ファームウェアオンラインアップグレード：メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルを手動でアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善と修正でルーターを最新の状態に保つことができます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasksページにより、事前定義されたスケジュールに基づいてさまざまなルーター機能を自動化でき、利便性と効率性が向上します。このページの主要機能は次のとおりです：

    * LED表示スケジュール：特定の時間帯にルーターのLEDライトを自動的にオンまたはオフに設定し、光害を軽減します。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fiステータススケジュール：5GHz / 2.4GHz / MLO Wi-Fiバンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力の管理を改善できます。
    
    これらのスケジューリングオプションは、ルーターの操作をより詳細に制御し、特定のニーズと好みに合わせることができます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

---

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現地時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Reset Firmware"

    Reset Firmwareページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定に戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはExport Logボタンがあり、収集したすべてのログをテクニカルサポートの分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的なサポートを受ける際に非常に役立ちます。

    詳細な手順については、[Log](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settingsページは、OpenWrt LuCIインターフェースを通じて高度な構成オプションへのアクセスを提供し、経験豊富なユーザーが基本インターフェースオプションを超えてルーターの設定と機能を微調整できます。これには、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
