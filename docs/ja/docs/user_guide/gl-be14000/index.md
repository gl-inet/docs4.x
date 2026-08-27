# Flint 4（GL-BE14000）ユーザーガイド

## 製品概要

Flint 4（GL‑BE14000）は、ホームルーターの可能性を広げます。MLO対応のトライバンドWi‑Fi 7を搭載し、最大速度は688 Mbps（2.4 GHz）+ 4323 Mbps（5 GHz）+ 8646 Mbps（6 GHz）です。有線接続では、10G SFP+ WAN/LANポート1基、10GE WAN/LANポート1基、2.5GE WAN/LANポート1基、2.5GE LANポート3基、1GE LANポート4基からなるマルチギガビットの有線バックボーンを備えています。高性能VPNにも対応し、WireGuard®とOpenVPN DCOのどちらでも最大1.5 Gbpsのスループットを実現します。さらに、2.4インチのタッチスクリーンを搭載しており、ネットワーク状態をリアルタイムで監視し、主要なネットワーク指標を本体で直接確認できます。

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## パッケージ内容

- 1 x Flint 4 (GL-BE14000)
- 1 x 電源アダプター
- 1 x Ethernetケーブル
- 1 x ユーザーマニュアル
- 1 x サンキューカード
- 1 x 変換プラグ（発送先の国に応じたもの）

Flint 4の開封動画を以下でご覧いただけます。

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Flint 4のセットアップ

セットアップ動画を見るか、次の手順を実行してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. 電源を入れる

2つの部品からなる電源アダプターを組み立てます。ルーターに接続してコンセントに差し込むと、自動的に起動します。

### 2. デバイスを接続する

パソコン、ノートパソコン、スマートフォンなどのデバイスをWi-FiまたはEthernetでルーターに接続します。

- Ethernet

    Ethernetケーブルを使用して、デバイスをルーターのLANポートに接続します。

- Wi-Fi

    デバイスの利用可能なネットワーク一覧からルーターのWi-Fiネットワーク名を選び、パスワードを入力して接続します。デフォルトのネットワーク名（SSID）とパスワードは、ルーターのラベルに記載されています。

### 3. Web管理パネルにログインする

Webブラウザーを開き、アドレスバーに`192.168.8.1`と入力してログインします。管理者パスワードとWi-Fi情報を設定し、**Apply**をクリックします。

### 4. インターネットを設定する

Ethernet（SFP+）、Ethernet（RJ45）、Repeater、Tethering、Cellularのいずれかの対応接続方式でFlint 4を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}
    
    Flint 4は10G SFP+ WAN/LANポートを搭載しており、光ファイバーアップリンク、高速スイッチのバックホール、高性能なネットワーク拡張に利用できます。このポートはデフォルトでWANに設定されていますが、必要に応じてLANへ切り替えられます。

    次の例では、光トランシーバーと光ファイバーケーブルを使用して、Flint 4の10G SFP+ポートをISPの光ファイバーアップリンクへ接続します。他の接続方法については、[Flint 4の10G SFP+ポートを接続する](../../faq/connecting_10g_sfp_plus_port_on_flint4.md)を参照してください。

    1. 対応する10G SFP+トランシーバーをFlint 4のSFP+ポートに挿入し、ISPの光ファイバーアップリンクへ接続します。  
    2. Flint 4は、DHCPを使用してネットワークパラメーター（IPアドレス、ゲートウェイ、DNS）を自動的に取得します。ISPがPPPoEまたは静的IPアドレスを要求する場合は、Web管理パネルでWAN接続を設定してください。
    3. インターネットに接続すると、タッチスクリーンのホームページにあるEthernetセクションが青色（有効）になります。タッチスクリーンでEthernetをタップするか、Web管理パネルにログインして接続の詳細を確認できます。

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}
    
    1. Ethernetケーブルを使用して、Flint 4のWANポートをISPモデム、ネットワークスイッチ、壁面のEthernetジャックなどの上流デバイスに接続します。
    2. Flint 4は、DHCPを使用してネットワークパラメーター（IPアドレス、ゲートウェイ、DNS）を自動的に取得します。ISPがPPPoEまたは静的IPアドレスを要求する場合は、Web管理パネルでWAN接続を設定してください。
    3. インターネットに接続すると、タッチスクリーンのホームページにあるEthernetセクションが青色（有効）になります。タッチスクリーンでEthernetをタップするか、Web管理パネルにログインして接続の詳細を確認できます。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. タッチスクリーンで**Repeater**をタップします。利用可能なWi-Fiネットワークのスキャンが開始されます。
    2. Flint 4で拡張するWi-Fiネットワークを選択します。
    3. パスワードを入力して**Apply**をタップします。
    4. インターネットに接続すると、タッチスクリーンのホームページにあるRepeaterセクションが青色（有効）になります。タッチスクリーンでRepeaterをタップするか、Web管理パネルにログインして接続の詳細を確認できます。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. USBケーブルを使用して、スマートフォンなどのモバイルデバイスをFlint 4のUSBポートに接続します。
    2. モバイルデバイスのSettingsを開き、**USB Tethering**または**Personal Hotspot**を有効にします。iPhoneで確認が表示された場合は、**Trust This Device**をタップします。
    3. Flint 4のタッチスクリーンで**Tethering**を選択し、**Connect**をタップします。ルーターがデバイスに接続します。
    4. インターネットに接続すると、タッチスクリーンのホームページにあるTetheringセクションが青色（有効）になります。タッチスクリーンでTetheringをタップするか、Web管理パネルにログインして接続の詳細を確認できます。

    **注**：接続に失敗する場合は、電源が12V 4Aであることを確認してください。電力が不足すると、USBポートに給電できないことがあります。上記の手順を繰り返すか、Web管理パネルにログインしてTethering接続の状態を確認してください。

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. セルラーモデムまたはUSBドングルをFlint 4のUSBポートに接続します。USBモデムのインターネット接続を、接続中のすべてのデバイスで共有できます。
    2. インターネットに接続すると、タッチスクリーンのホームページにあるCellularセクションが青色（有効）になります。タッチスクリーンでCellularをタップするか、Web管理パネルにログインして接続の詳細を確認できます。

---

以下では、Flint 4のWeb管理パネルで利用できる機能の概要を説明します。

## Wireless

Wirelessページでは、MLO Wi-Fi、Main Network、Guest Network、IoT Networkなど、Flint 4の各種Wi-Fiネットワークを設定できます。

詳細は[Wireless](../../interface_guide/wireless.md)を参照してください。

## クライアント

Clientsページには、接続中のデバイスに関する情報が表示されます。各クライアントの名前、IPアドレス、MACアドレス、ダウンロードおよびアップロード速度、総トラフィックを確認でき、クライアントのブロックやその他の操作も行えます。

詳細は[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}を使用すると、GL.iNetルーターへ簡単にリモートアクセスして管理できます。
    
    詳細は[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarpはGL.iNetルーターに統合された高度なネットワーク機能です。登録やログインを行わずに、自宅ネットワークへシームレスにリモートアクセスできます。トラフィック難読化を内蔵したAmneziaWGプロトコルにより、接続の安定性と安全性を維持し、外出先からの信頼性の高いリモートアクセスを実現します。GL.iNetルーターの管理パネルからAstroWarpネットワークを直接設定できます。アクセスコードでルーターをペアリングするだけで、トラベルルーターを自宅ネットワークへ数秒で安全に接続できます。
    
    詳細は[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバーの間に安全な暗号化通信を構築します。VPNクライアントとしてプライバシーと安全性を高めるほか、VPNサーバーとしてリモートネットワークへのアクセスを可能にします。Flint 4はOpenVPNとWireGuardプロトコルに対応しています。

=== "OpenVPN"
    
    Flint 4およびその他のGL.iNetルーターは、安全性に優れたOpenVPNプロトコルに対応しています。OpenVPNを設定するには、次のガイドを参照してください。

    * [OpenVPNクライアントを設定する](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーを設定する](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4およびその他のGL.iNetルーターは、高速で使いやすいWireGuardプロトコルに対応しています。WireGuardを設定するには、次のガイドを参照してください。

    * [WireGuardクライアントを設定する](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーを設定する](../../interface_guide/wireguard_server.md)

## ネットワーク

=== "Multi-WAN"

    Multi-WANを使用すると、セルラー、Repeater、Ethernetなど、複数のインターネット接続を同時にルーターへ設定できます。現在の接続が切断された場合、ルーターは自動的に別の接続へ切り替わるため、インターネットアクセスを途切れさせずに維持できます。

    詳細は[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "Subnet"

    Subnetページでは、LAN、Guest Network、IoT Network、カスタムVLAN Networkを一元管理できます。複数のサブネットを作成して管理し、さまざまな種類のデバイスやトラフィックを分離できます。

    詳細は[Subnet](../../interface_guide/subnet.md)を参照してください。

=== "Ethernet Port"

    Ethernet Portページでは、Ethernetポートの役割（WAN/LAN）とVLAN分割を管理し、MACアドレスやネゴシエート速度などの詳細を確認できます。

    詳細は[Ethernet Port](../../interface_guide/ethernet_port_v4.10.md)を参照してください。

---

=== "DNS"

    DNSページでは、カスタムDNSサーバーの設定、DNSリバインディング攻撃からの保護、すべてのクライアントのDNS設定の上書き、カスタムDNSによるVPN DNSの上書きができます。また、Ethernet接続のDNSサーバー設定を自動にするか、手動で指定できます。

    詳細は[DNS](../../interface_guide/dns.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4に代わる最新のInternet Protocolです。非常に広大なアドレス空間を備え、ほぼ無制限の一意なIPアドレスを提供できるため、インターネットへ接続するデバイスの増加に対応できます。
    
    詳細は[IPV6](../../interface_guide/network_mode.md)を参照してください。

=== "IGMP Snooping"

    IGMP snoopingは、Ethernetスイッチでマルチキャストトラフィックを管理および制御するためのネットワーク最適化技術です。
    
    詳細は[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

---

=== "Network Mode"

    Network Modeは、ネットワークの導入要件に応じてルーターが担う各種の動作上の役割と機能を指します。一般的なモードには、Router Mode、Extender Mode、Access Point Modeがあります。
    
    詳細は[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in Gateway"

    Drop-in Gatewayは、既存のメインルーターを交換または再設定せずに機能を拡張できる柔軟な機能です。GL.iNetルーターをDrop-in Gatewayとして設定することで、既存のネットワークへAdGuard Home、VPN、暗号化DNSなどの高度な機能を追加できます。

    Drop-in Gatewayの設定方法は、次のリンクを参照してください。
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Drop-in Gatewayを設定する](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network AccelerationはCPU負荷を軽減し、トラフィックパケットの転送を高速化します。
    
    詳細は[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御

=== "DPI Engine"

    DPI（Deep Packet Inspection）は、インテリジェントなネットワーク管理の中核となる機能です。送信元または宛先アドレスのみを識別する従来のルーターの制約を超え、パケットのペイロードを詳細に分析します。シグネチャライブラリとの照合により、ユーザーが利用するアプリケーションやWebサイトを正確に識別し、きめ細かなトラフィックの分類と制御を実現します。
    
    GL.iNetのDPI機能は[Netify](https://www.netify.ai/){target="_blank"}と統合され、効率的に導入できる軽量な組み込みプラグインを使用しています。Netifyのオンライン更新対応シグネチャデータベースにより、信頼性の高い管理と、より正確で効率的なネットワーク制御が可能になります。

    詳細は[DPI Engine](../../interface_guide/dpi_engine.md)を参照してください。

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

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「bufferbloat」を抑え、ゲームや音声通話をより滑らかにします。

    詳細は[SQM](../../interface_guide/sqm.md)を参照してください。

=== "Parental Control"

    Parental Controlは、子どものデバイスを管理および制御するための機能です。画面の使用時間を制限し、特定のコンテンツへのアクセスを制限できます。

    詳細は[Parental Control](../../interface_guide/parental_control_v4.9.md)を参照してください。

## セキュリティ

=== "Port Forwarding"

    Port Forwardingを使用すると、インターネット上のリモートサーバーやデバイスからプライベートネットワーク内のデバイスへアクセスできます。
    
    詳細は[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "ACL"

    ACL（Access Control List）では、接続プロトコル、デバイスアドレス、ポートに基づくルールを作成し、ネットワークトラフィックを管理できます。ネットワークアクセスを許可するかブロックするかを制御します。複数のACLルールが競合する場合は、優先度の高いルールが適用されます。

    詳細は[ACL](../../interface_guide/acl.md)を参照してください。

=== "Admin Access"

    Admin Accessでは、不正なアクセスからネットワークとルーターを保護するための各種セキュリティ設定を行えます。このページには次の項目があります。

    * Local Access Control：ローカルネットワークへ接続しているデバイスからルーターのインターフェースへのアクセスを管理および制限します。
    * Remote Access Control：インターネット上の遠隔地からルーターのインターフェースへのアクセスを設定および制限し、外部の脅威に対する安全性を高めます。
    * Open Ports on Router：ルーターで開くポートを制御し、潜在的な脆弱性や不正アクセスを抑えます。

    詳細は[Admin Access](../../interface_guide/admin_access.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG（Application Layer Gateway）機能を有効または無効にできます。

    詳細は[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加し、カスタマイズや機能拡張を可能にするソフトウェアコンポーネントです。
    
    詳細は[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスを自動的に検出し、リアルタイムで更新します。リモートネットワークへアクセスするために固定IPアドレスが必要な場合に便利です。
    
    詳細は[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    Network Storageは、複数のユーザーやデバイスがネットワーク経由でファイルへアクセスし、共有できる一元的なデータストレージソリューションです。
    
    詳細は[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Homeは、DNSサーバーとして動作し、ホームネットワークへ接続しているすべてのデバイスで不要なコンテンツをフィルタリングする、ネットワーク全体の広告およびトラッカーブロックソリューションです。
    
    詳細は[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "Bark"

    Flint 4に統合されたBarkサービスは、子どものデジタル環境を保護し、包括的なオンライン保護を提供します。通常は有料サブスクリプションが必要ですが、Barkとの提携により、GL.iNetはFlint 4を含む一部のルーターモデルでBark Homeプランを無料提供しています。追加料金なしで高度な監視とアラートを利用できます。

    詳細は[Bark](../../interface_guide/bark.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションへアクセスできるVPNサービスです。
    
    詳細は[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "ZeroTier"

    ZeroTierは、インターネット上に安全な仮想ネットワークを作成し、デバイスを同じローカルネットワーク上にあるかのように接続するSoftware-Defined Networkingソリューションです。
    
    詳細は[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tor"

    Tor（The Onion Router）は、インターネット上で匿名通信を実現するプライバシー重視のネットワークです。インターネットトラフィックをボランティアが運用する複数のサーバー（ノード）経由で転送し、ユーザーの位置や利用状況を隠してオンライン活動の追跡を困難にします。
    
    詳細は[Tor](../../interface_guide/tor.md)を参照してください。

## システム

=== "Overview"

    Overviewページでは、ルーターの現在の状態とパフォーマンス指標をまとめて確認できます。次の情報が表示されます。

    * CPU Average Load：ルーターCPUの平均負荷を監視し、性能を評価してボトルネックを特定できます。
    * Memory Usage：ルーターのメモリー使用量を確認し、リソース管理に役立てます。
    * Flash Usage：ルーターのフラッシュストレージ使用量を確認し、ファームウェアや設定データに十分な空き容量があるか確認できます。
    * Device Info：稼働時間、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/Nなど、ルーターシステムの詳細情報を確認できます。
    * External Storage：USBドライブやTFカードなど、ルーターに接続された外部ストレージの状態を確認できます。
    
    これらの情報と操作により、ルーターの動作を効率的に管理および監視できます。

    詳細は[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェース用パスワードを管理し、許可されたユーザーだけが設定を変更できるようにします。

    詳細は[Admin Password](../../interface_guide/admin_password.md)を参照してください。

=== "Upgrade"

    Upgradeページでは、ルーターのファームウェアを最新バージョンへ更新し、性能や安全性の向上、新機能を利用できます。次の2つの更新方法があります。

    * Firmware Online Upgrade：メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * Firmware Local Upgrade：コンピューターからファームウェアファイルを手動でアップロードし、更新するバージョンとタイミングを指定できます。

    詳細は[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasksページでは、事前に設定したスケジュールに基づいて各種ルーター機能を自動化できます。主な機能は次のとおりです。

    * LCD Display Schedule：指定した時間にルーターのLCDを自動的にオンまたはオフにし、不要な光を抑えます。
    * Schedule Reboot：指定した間隔でルーターを自動的に再起動し、最適な性能と安定性の維持に役立てます。
    * Wi-Fi Status Schedule：6GHz / 5GHz / 2.4GHz / MLO Wi-Fiバンドをスケジュールに従って制御し、ネットワークの可用性を管理して消費電力を抑えます。
    
    これらのスケジュール設定により、用途に応じてルーターの動作を細かく制御できます。

    詳細は[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。
    
=== "Display Management"

    Display Managementページでは、タッチスクリーンと関連設定を管理する各種機能を利用できます。

    ‒ Wallpaper：壁紙と画面のウェイク表示スタイルをカスタマイズします。
    ‒ Brightness：スライダーまたはパーセント値でタッチスクリーンの明るさを調整し、周囲の明るさに合わせます。
    ‒ Auto Lock：操作がない場合に画面を自動ロックするまでの時間を1分から30分の範囲で設定します。
    ‒ Screen Always On：タッチスクリーンを常に点灯させるか、操作がない場合に消灯させるかを選択します。
    ‒ Enable Screen Passcode：タッチスクリーンにパスコードを設定し、安全性をさらに高めます。

    詳細は[Display Management](../../interface_guide/display_management.md)を参照してください。

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定します。スケジュールされたタスク、ログ、システムイベントが現地時刻に基づいて正確に記録され、時刻に基づく設定が正しく実行されるようになります。

    詳細は[Time Zone](../../interface_guide/time_zone.md)を参照してください。

---

=== "Reset Firmware"

    Reset Firmwareページでは、現在インストールされているファームウェアバージョンをデフォルト設定へリセットし、すべてのカスタム設定を消去します。解決しない問題のトラブルシューティングや、現在のファームウェアを初期状態から設定し直す場合に役立ちます。

    詳細は[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Logページでは、ルーターの活動やイベントを記録した各種ログを確認し、トラブルシューティングや性能監視に利用できます。次のログがあります。

    * System Log：システムレベルのイベントと活動の詳細なログです。
    * Kernel Log：カーネルの動作とイベントに関するログです。
    * Crash Log：システムクラッシュとエラーの記録で、重大な問題の診断に役立ちます。
    * Cloud Log：ルーターに統合されたGoodCloudサービスに関する操作と活動のログです。
    * Nginx Log：ルーターがNginx Webサーバーを使用する場合のWebトラフィックとサーバー動作のログです。
    
    また、Export Logボタンを使用すると、収集したすべてのログをエクスポートしてテクニカルサポートで分析できます。複雑な問題の診断や専門的なサポートを受ける際に役立ちます。

    詳細は[Log](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settingsページでは、OpenWrt LuCIインターフェースから高度な設定へアクセスできます。上級ユーザーは、基本インターフェースを超えてルーターの設定と機能を細かく調整できます。詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細は[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。

## 適合宣言

GL TECHNOLOGIES (HONG KONG) LIMITEDは、無線機器[BE14000 Wi-Fi 7 Router, GL-BE14000]が指令2014/53/EUの基本要件およびその他の関連規定に適合することを宣言します。EU適合宣言の全文は、[https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}で確認できます。

EU向け：<br>
最大送信出力：<br>
CE: ≤20dBm EIRP (2.412GHz~2.472GHz); ≤23dBm EIRP (5.15GHz~5.35GHz); ≤30dBm EIRP (5.47GHz~5.725GHz); ≤13.98dBm (5.725GHz~5.85GHz); ≤23dBm EIRP (5.925GHz~6.425 GHz)
