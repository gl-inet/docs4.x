# Beryl 7 (GL-MT3600BE) ユーザーガイド

## 製品概要

Beryl 7 (GL-MT3600BE) は、ビジネス旅行や休暇などのモバイルシナリオ向けに設計されたWi-Fi 7対応デュアルバンドトラベルルーターです。Beryl AXのアップグレード版として、Multi-Link Operation (MLO)や4K QAMなどのWi-Fi 7技術をサポートし、理論的なデュアルバンド速度は688Mbps (2.4GHz) + 2882Mbps (5GHz) — 8Kストリーミングやモバイルゲームなどの高速ニーズに対応できます。

MediaTekクアッドコアプロセッサーで動作し、512MB NANDフラッシュストレージを備え安定したマルチタスクとさまざまなOpenWrtプラグインとの互換性を確保します。2x 2.5G Ethernetポート (1 WAN + 1 LAN) と1x USB 3.0ポートを備え、高速有線接続とストレージ拡張の両方のニーズに対応します。PD互換性により、標準のスマートフォン充電器のーブルで電源を供給できるため、荷物を軽くできます。120で上のデバイス same 時接続をサポートしており、移動中の生活に最適なポータブルデザインが特徴です。

![gl-mt3600be interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/hardware_info/mt3600be_interface.png){class="glboxshadow"}

## パッケージコンテンツ

パッケージには以下が含まれます：

- 1 x Beryl 7 (GL-MT3600BE)
- 1 x 電源アダプター
- 1 x Ethernet cable
- 1 x ユーザーガイド
- 1 x サンキューカード
- 3 x コンバーター (EU, UK, AU plugs)

Beryl 7の開栓動画については、以下を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/xZHmP3B8VlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Beryl 7の設定方法

Beryl 7の設定には，Ethernet、Repeater、Tethering、Cellularの4つのインターネット接続方法が使えます。設定動画を見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ey-Z3MEOPpw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Beryl 7の電源を入れる

二分割の電源アダプターを組み合わせます。ルーターに接続し，コンセントに挿すと自動的に起動します。

### 2. Beryl 7に接続する

Wi-FiまたはEthernetを使用してコンピュータまたはモバイルデバイスをルーターに接続します。

- Ethernet

    Ethernet cableを使用してデバイスをルーターのLANポートに接続します。

- Wi-Fi

    デバイスで、Settings -> WLANを開き，利用可能なネットワークリストからルーターのWi-Fiネットワーク名を見つけ、パスワードを入力してネットワークに参加します。（デフォルトのネットワーク名とパスワードはラベルに印刷されています。）

### 3. WebGUIにログインする

Webブラウザーでアドレスバーに`192.168.8.1`を入力してログインします。言語を選択し，管理者パスワードを設定して、**Apply**をクリックします。

### 4. Beryl 7をインターネットに接続する

**注意:** 以下の説明は、GL.iNet Web管理パネルでルーターを設定するユーザーに適用されます。GL.iNetアプリを使用する場合は，[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}して画面の説明に従ってください。

サポートされているインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用してBeryl 7を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_ethernet.png){class="glboxshadow"}
    
    Beryl 7 の WAN ポートを Ethernet ケーブルで上位機器（モデムなど）に接続します。
    
    インターネットに正常に接続されると、INTERNETページのEthernetセクションに緑色のドットが表示されます。

    詳細な手順については、[Ethernet cableでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_repeater.png){class="glboxshadow"}

    1. Web管理パネルのINTERNETページで、Repeaterセクションを見つけ、**Connect**をクリックします。
    2. 利用可能なWi-Fiネットワークから選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのRepeaterセクションに緑色のドットが表示されます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_tethering.png){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSB dongleなど）をUSB cableでBeryl 7のUSBポートに接続します。
    2. モバイルデバイスでSettingsを開き、USB Tetheringを有効にします。
    3. Web管理パネルのINTERNETページで、Tetheringセクションの**Connect**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのTetheringセクションに緑色のドットが表示されます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_cellular.png){class="glboxshadow"}

    Beryl 7のUSBポートにCellular USBモデムを挿します。これは、USBモデムからすべての接続クライアントデバイスにインターネットを共有するのに便利です。

    インターネットに正常に接続されると、INTERNETページのCellularセクションに緑色のドットが表示されます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下はBeryl 7 WebGUI機能の概要です。

## Wireless

Wirelessページでは、5 GHzと2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、TX電力の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSID可視性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

また、Beryl 7はMLO Wi-Fi（Multi-Link Operation）をサポートしており、複数のWi-Fiネットワークを同時に組み合わせて、より高い帯域幅とより信頼性の高い接続を実現します。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients

Clients ページには、接続中のデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレス、MACアドレス、ダウンロード速度、アップロード速度、合計トラフィックを確認でき、クライアントをブロックしたり、その他の操作を実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}は、GL.iNetルーターに簡単かつシンプルにリモートアクセスと管理を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarp は、シームレスなリモートネットワーク接続とリモートデバイス管理を実現する高度なネットワーキングプラットフォームです。GL.iNet ルーターとの連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位・下位デバイスの制御も可能にします。将来的なハードウェアレベル制御にも対応できる設計で、安全かつ安定したネットワークを維持するための堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Beryl 7はOpenVPN、WireGuard、Torをサポートしています。

=== "OpenVPN"

    Beryl 7（およびその他の GL.iNet ルーター）は、高いセキュリティを提供する OpenVPN プロトコルをサポートしています。OpenVPN を設定するには、以下のチュートリアルを参照してください。

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Beryl 7（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルをサポートしています。WireGuard を設定するには、以下のチュートリアルを参照してください。

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor（The Onion Routerのやや称）は、匿名通信を可能にするプライバシー重視のネットワークです。ユーザーの位置情報と使用状況を不明瞭にするために、一連のボランティアが運用するサーバー（ノード）を介してインターネットトラフィックをルーティングします。
    
    * [Torの設定方法](../../interface_guide/tor.md)

## アプリケーション

=== "Plug-ins"

    プラグインは、既存のコンピュータプログラムに特定の機能または機能を追加するソフトウェアコンポーネントであり、カスタマイズと機能拡張を可能にします。
    
    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。リモートネットワークにアクセスするために静的IPアドレスが必要なユーザーに便利です。
    
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

    LAN（Local Area Network）は、自宅やオフィスなどの限られた物理的な範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。
    
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

    ネットワークモードは、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する構成設定です。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。ほぼ無制限の固有IPアドレスを提供する広大なアドレス空間を備え、インターネット接続デバイスの増加に対応するうえで不可欠です。
    
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

## システム

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

    Upgrade ページでは、ルーターのファームウェアを最新バージョンへ更新できます。これにより、性能向上、セキュリティ強化、新機能の利用が可能になります。このページには次の2つのアップグレード方法があります。

    * ファームウェアオンラインアップグレード：メーカーのサーバーから最新バージョンを自動確認してインストールします。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善や修正を適用した状態にルーターを保てます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前定義したスケジュールに基づいてルーター機能を自動化でき、利便性と効率が向上します。主な機能は次のとおりです。

    * LED表示スケジュール：特定の時間帯にルーターのLEDライトを自動的にオンまたはオフに設定し，光害を軽減します。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fiステータススケジュール：5GHz / 2.4GHz / MLO Wi-Fiバンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力の管理を改善できます。
    
    これらのスケジューリングオプションは、ルーターの操作をより詳細に制御し、特定のニーズと好みに合わせることができます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}を参照してください。

---

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現地時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md){target="_blank"}を参照してください。

=== "Toggle Button Settings"

    Toggle Button Settingsページでは、ルーターの物理トグルボタンを構成でき、ボタンに特定の機能を割り当ててクイックアクセスと制御を可能にします。この機能は、一般的なタスクと設定への便利なショートカットを提供し、ユーザーエクスペリエンスを向上させ、ルーターの管理を簡素化します。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md)を参照してください。

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

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションにアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えて、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズを行えます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
