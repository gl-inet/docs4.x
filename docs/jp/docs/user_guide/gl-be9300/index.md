# Flint 3 (GL-BE9300) ユーザーガイド

## 製品概要

Flint 3 (GL-BE9300) は、家庭ユーザー、スモールオフィス、高必要シナリオ向けのWi-Fi 7トライバンドデスクトップルーターです。Wi-Fi 7 Multi-Link Operation (MLO)をサポートし、2.4GHz、5GHz、6GHzバンドをインテリジェントに単一接続にマージして、干渉と輻輳を削減します。4K QAMと組み合わせることで、688Mbps (2.4GHz) + 2882Mbps (5GHz) + 5765Mbps (6GHz)の理論のなトライバンド速度を実現します。MLOまたは6GHz接続はピークパフォーマンスを提供し、2.4GHzバンドはIoTデバイス専用に使用できます。

5× 2.5G Ethernetポート（1専用WAN、1切替可能WAN/LAN、3 LAN）を備え、5Gbps最大共有帯域幅でdual-WANセットアップをサポート plus 1× USB 3.0ポートで拡張機能を備えています。さらに、AdGuard Home（広告ブロッキングとトラッカー防止）がプリインストールされており、Bark Parental Controlと30以上のVPNサービスをサポートし、GoodCloudによるリモート管理を可能にします—パフォーマンス、実用性、セキュリティの完璧なバランスを実現しています。

![gl-be9300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/hardware_info/be9300_interface.jpg){class="glboxshadow"}

## パッケージコンテンツ

パッケージには以下が含まれます：

- 1 x Flint 3 (GL-BE9300)
- 1 x 電源アダプター
- 1 x Ethernet cable
- 1 x ユーザーガイド
- 1 x サンキューカード
- 1 x コンバーター（発送国により異なります）

Flint 3の開栓動画については、以下を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/qAq6IFtKtj0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Flint 3の設定方法

Flint 3の設定には，Ethernet、Repeater、Tethering、Cellularの4つのインターネット接続方法が使えます。設定動画を見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/WQqD-8NrAOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Flint 3の電源を入れる

二分割の電源アダプターを組み合わせます。ルーターに接続し、コンセントに挿すと自動的に起動します。

### 2. Flint 3に接続する

Wi-FiまたはEthernetを使用してデバイス（コンピュータ、ラップトップ、スマートフォンなど）をルーターに接続します。

- Ethernet

    Ethernet cableを使用してデバイスをルーターのLANポートに接続します。

- Wi-Fi

    デバイスで、Settings -> WLANを開き，利用可能なネットワークリストからルーターのWi-Fiネットワーク名を見つけ、パスワードを入力してネットワークに参加します。デフォルトのネットワーク名とパスワードはルーターのラベルに印刷されています。

### 3. WebGUIにログインする

Webブラウザーでアドレスバーに`192.168.8.1`を入力してログインします。言語を選択し，管理者パスワードを設定して、**Apply**をクリックします。

### 4. Flint 3をインターネットに接続する

**注意:** 以下の説明は、GL.iNet Web管理パネルでルーターを設定するユーザーに適用されます。GL.iNetアプリを使用する場合は，[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}して画面の説明に従ってください。

サポートされているインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用してFlint 3を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_ethernet.jpg){class="glboxshadow"}

    Flint 3のWANポートをEthernet cableで上位デバイス（モデムなど）に接続します。
    
    インターネットに正常に接続されると、INTERNETページのEthernetセクションに緑色のドットが表示されます。

    詳細な手順については、[Ethernet cableでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_repeater.jpg){class="glboxshadow"}

    1. Web管理パネルのINTERNETページで、Repeaterセクションを見つけ、**Connect**をクリックします。
    2. 利用可能なWi-Fiネットワークから選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのRepeaterセクションに緑色のドットが表示されます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSB dongleなど）をUSB cableでルーターのUSBポートに接続します。
    2. モバイルデバイスでSettingsを開き、USB Tetheringを有効にします。
    3. Web管理パネルのINTERNETページで、Tetheringセクションの**Connect**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのTetheringセクションに緑色のドットが表示されます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_cellular.jpg){class="glboxshadow"}

    Flint 3のUSBポートにCellular USBモデムを挿します。これは、USBモデムからすべての接続クライアントデバイスにインターネットを共有するのに便利です。

    インターネットに正常に接続されると、INTERNETページのCellularセクションに緑色のドットが表示されます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下はFlint 3 WebGUI機能の概要です。

## Wireless

Wirelessページでは、6GHz、5 GHz、2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、TX電力の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSID可視性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

また、Flint 3はMLO Wi-Fi（Multi-Link Operation）をサポートしており、複数のWi-Fiネットワークを同時に組み合わせて、より高い帯域幅とより信頼性の高い接続を実現します。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients

Clientsページには、接続されたデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレスとMACアドレス、ダウンロード速度とアップロード速度、合計トラフィックが表示され、クライアントをブロックしたりその他のアクションを実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}は、GL.iNetルーターに簡単かつシンプルにリモートアクセスと管理を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarpは、シームレスなリモートネットワークとリモートデバイス管理を提供するために設計された高度なネットワーキングプラットフォームです。GL.iNetルーター連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位と下位のデバイス制御を可能にします。ネットワーク全体の管理と将来のハードウェアレベル制御のサポートに焦点を当てたAstroWarpは、デバイスの管理と安全で安定したネットワークの維持のためのより堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Flint 3はOpenVPN、WireGuard、Torをサポートしています。

=== "OpenVPN"
    
    Flint 3（およびその他のGL.iNetルーター）は強力なセキュリティを提供するOpenVPNプロトコルをサポートしています。OpenVPNを設定するには、以下のチュートリアルに従ってください：

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 3（およびその他のGL.iNetルーター）は、高速性と利便性を備えたWireGuardプロトコルをサポートしています。WireGuardを設定するには、以下のチュートリアルに従ってください：

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor（The Onion Routerのやや称）は、匿名通信を可能にするプライバシー重視のネットワークです。ユーザーの位置情報と使用状況を不明瞭にするために、一連のボランティアが運用するサーバー（ノード）をを通じてインターネットトラフィックをルーティングします。
    
    * [Torの設定方法](../../interface_guide/tor.md)

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

=== "Parental Control"

    Parental Controlは、子どものデバイスを管理および制御するために設計されています。スクリーン時間の制限や特定コンテンツへのアクセス制限が含まれます。

    保護者による制御の設定については、[Parental controls](../../interface_guide/parental_control.md)を参照してください。

=== "ZeroTier"

    ZeroTierは、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全に仮想ネットワークを作成し、デバイスが同一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサービスです。
    
    Tailscaleの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

## ネットワーク

=== "Port forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Multi-WAN"

    Multi-WANは、ルーターに複数のインターネット接続（cellular、repeater、ethernetなど）を同時に設定できるネットワーキング機能です。現在のインターネット接続が失敗すると、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れないインターネットアクセスが確保されます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなど、限られた地理的領域内でコンピュータとデバイスを接続するネットワークです。高速データ転送とリソース共有を可能にし、デバイスが効率的に相互通信できます。
    
    LANの設定については、[Lan](../../interface_guide/lan.md)を参照してください。

---

=== "Guest Network"

    IPv4プライベートアドレス範囲192.168.0.0/16、172.16.0.0/12、または10.0.0.0/8内でサブネットを設定し、ゲートウェイとネットマスクIPアドレスを指定し、ゲストネットワークのAP分離などのセキュリティ設定を構成できます。

    ゲストネットワークの設定については、[Guest Network](../../interface_guide/guest_network.md)を参照してください。

=== "DNS"

    DNSページでは、カスタムDNSサーバーを設定し、DNSリバインディング攻撃保護を有効にしてすべてのクライアントのDNS設定を上書きし、カスタムDNSがVPN DNSを上書きできるようにし、Ethernet接続からDNSサーバーを自動的に指定するか手動で指定するモードを構成できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "Port Management"

    Port Managementページでは、WANとLANポートの設定、WAN/LANインターフェースをEthernetに設定、WANインターフェースのMACモードとMACアドレスの指定、ネットワークポート速度のネゴシエーション表示を行うことができます。

    Ethernetポートの管理については、[Port Management](../../interface_guide/ethernet_port.md)を参照してください。

---

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークに接続し、他のデバイスと通信する方法を決定する構成設定を指します。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4を置き換えるために設計されたインターネットプロトコルの最新バージョンです。ほぼ無限の数の固有のIPアドレスを可能にする大幅なアドレス空間を提供し、インターネットに接続するデバイスの増加に対応するために不可欠です。
    
    IPV6の設定については、[IPV6](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in Gateway"

    Drop-in Gatewayは、AdGuard Home、暗号化DNS、VPNクライアントを含むメインルーターの機能を拡張します。
    
    ドロップインゲートウェイの設定については、以下のリンクを参照してください：
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMPスヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。
    
    IGMPスヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU負荷を削減し、トラフィックパケットの転送を高速化できます。
    
    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

=== "NAT Settings"

    NAT Settingsページでは、Full Cone NATとSIP ALG（Application Layer Gateway）機能を有効または無効にできます。

    NAT設定については、[NAT Settings](../../interface_guide/nat_settings.md)を参照してください。

## システム設定

=== "Overview"

    Overviewページは、ルーターの現在のパフォーマンス指標とステータスのを含むスナップショットを提供します。このページでは以下を表示できます：

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーターのフラッシュストレージの使用率を確認し、ファームウェアと設定データのための十分な空間を確保します。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーターの操作を効果的に管理および監視するのに役立つ重要な洞察とコントロールを提供します。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Upgrade"

    Upgradeページは、ルーターのファームウェアを最新バージョンにアップデートするために使用され、パフォーマンス、セキュリティ、新機能の向上を確保します。このページには2つのアップグレードオプションがあります：

    * ファームウェアオンラインアップグレード：製造元のサーバーから最新バージョンを自動的に確認してインストールし、アップデートプロセスを簡素化します。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善と修正でルーターを最新の状態に保つことができます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasksページにより、事前定義されたスケジュールに基づいてさまざまなルーター機能を自動化でき，利便性と効率性が向上します。このページの主要機能は次のとおりです：

    * LED表示スケジュール：特定の時間帯にルーターのLEDライトを自動的にオンまたはオフに設定し，光害を軽減します。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fiステータススケジュール：6GHz / 5GHz / 2.4GHz / MLO Wi-Fiバンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力の管理を改善できます。
    
    これらのスケジューリングオプションは、ルーターの操作をより詳細に制御し、特定のニーズと好みに合わせることができます。

    詳細な手順については，[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

---

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現地時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはExport Logボタンがあり、収集したすべてのログをエクスポートして技術サポートの分析にできます。この機能は、複雑な問題の診断と専門のサポートの取得に非常に便利です。

    詳細な手順については、[Log](../../interface_guide/log.md)を参照してください。

---

=== "Security"

    Securityページでは、ネットワークとルーターを不正アクセスから保護するためのさまざまなセキュリティ設定を構成できます。このページには以下のオプションがあります：

    * 管理者パスワード：ルーターの管理インターフェースのパスワードを設定または変更し、許可されたユーザーのみが設定を変更できるようにします。
    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーターのインターフェースへのアクセスを管理および制限します。
    * リモートアクセス制御：インターネット上のリモート場所からルーターのインターフェースへのアクセスを構成および制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    これらの設定は、ネットワーク環境を安全に保ち、ルーターと接続されたデバイスを保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "Reset Firmware"

    Reset Firmwareページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。このプロセスは、現にインストールされているファームウェアバージョンのデフォルト設定にルーターを復元します。持続的な問題のトラブルシューティングや現在のファームウェアのデフォルト設定で新鮮に開始するのに便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Advanced Settings"

    Advanced Settingsページは、OpenWrt LuCIインターフェースを通じて高度な構成オプションへのアクセスを提供し、経験豊富なユーザーが基本インターフェースオプションを超えてルーターの設定と機能を微調整できます。これには、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
