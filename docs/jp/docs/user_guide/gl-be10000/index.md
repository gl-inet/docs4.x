# Slate 7 Pro (GL-BE10000) ユーザーガイド

## 製品概要

Slate 7 Pro (GL-BE10000) は、トライバンド Wi-Fi 7 対応のポータブルトラベルルーターです。Slate 7 (GL-BE3600) の上位モデルとして、上面に大型タッチスクリーンを搭載し、1GB DDR4 RAM と 8GB eMMC フラッシュストレージにより、安定した動作とプラグイン互換性を実現します。WireGuard® は最大 1,100 Mbps、OpenVPN-DCO は最大 1,000 Mbps の高速 VPN に対応し、2× 2.5G Ethernet ポート（1 WAN + 1 LAN）、1× USB-C 3.0 ポート、PD 給電を備えているため、旅行やモバイル用途でも高い接続性と利便性を提供します。

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## パッケージ内容

パッケージには以下が含まれます。

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x ユーザーマニュアル
- 1 x サンキューカード
- 1 x Ethernet ケーブル
- 1 x 電源ケーブル
- 1 x 電源アダプター
- 4 x 変換プラグ（US / EU / UK / AU）

## Slate 7 Pro の設定方法

Slate 7 Pro は、Ethernet、Repeater、Tethering、Cellular の 4 つのインターネット接続方法に対応しています。以下の手順に従って設定してください。

### 1. 電源を入れる

2 分割の電源アダプターを組み立て、ルーターに接続してコンセントへ差し込みます。自動的に起動します。

### 2. タッチスクリーン

ルーターの電源を入れると、画面に GL.iNet ロゴが表示され、その後に起動の進行バーが表示されます。

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){class="glboxshadow" width="360"}

進行バーが最後まで読み込まれると、デバイスの起動が完了し、ウェルカム画面が表示されます。画面の案内に従って管理者パスワードと Wi-Fi ネットワークを設定してください。

![set admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){class="glboxshadow" width="360"}

![set WiFi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){class="glboxshadow" width="360"}

その後、ホーム画面が表示されます。左側にはシステム時刻やネットワーク速度などのリアルタイムシステム情報が表示され、Wi-Fi、Clients、VPN などのショートカットタイルが並びます。右側には Ethernet、Repeater、Tethering、Cellular の 4 つの接続モード用ショートカットタイルが表示されます。

![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){class="glboxshadow" width="360"}

4 つのショートカットタイルは、色によってネットワーク状態を示します。

![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){class="glboxshadow" width="360"}

- **青**: 接続中 / インターネット接続済み
- **黄**: 接続中 / ネットワーク異常
- **白**: 非アクティブな接続

### 3. デバイスを接続する

Wi-Fi または Ethernet を使って、デバイス（コンピューター、ノート PC、スマートフォンなど）をルーターに接続します。

- Ethernet

    Ethernet ケーブルを使って、デバイスをルーターの LAN ポートへ接続します。

- Wi-Fi

    デバイスで利用可能なネットワークリストを開き、ルーターの Wi-Fi ネットワーク名を選択してパスワードを入力します。デフォルトのネットワーク名（SSID）とパスワードは、ルーター本体のラベルに記載されています。

### 4. Web 管理パネルにログインする

Web ブラウザーを開き、アドレスバーに `192.168.8.1` を入力してログインします。言語を選択し、管理者パスワードを設定して **Apply** をクリックします。

### 5. インターネットを設定する

対応するインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかで Slate 7 Pro を設定します。[Multi-WAN](../../interface_guide/multi-wan.md) 機能を利用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}

    1. Slate 7 Pro の WAN ポートを Ethernet ケーブルで上位機器（ISP モデム、ネットワークスイッチ、壁面 Ethernet ジャックなど）に接続します。
    2. Slate 7 Pro は IP アドレス、ゲートウェイ、DNS サーバーなどのネットワークパラメーターを自動取得し、Ethernet 接続を確立します。
    3. インターネット接続に成功すると、タッチスクリーンのホーム画面にある Ethernet セクションが青色（アクティブ）になります。タッチスクリーンの Ethernet をタップするか、Web 管理パネルにログインして接続の詳細を確認できます。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. タッチスクリーンで **Repeater** をタップします。利用可能な Wi-Fi ネットワークのスキャンが始まります。
    2. Slate 7 Pro で中継したい Wi-Fi ネットワークを選択します。
    3. パスワードを入力して **Apply** をタップします。
    4. インターネット接続に成功すると、タッチスクリーンのホーム画面にある Repeater セクションが青色（アクティブ）になります。タッチスクリーンの Repeater をタップするか、Web 管理パネルにログインして接続の詳細を確認できます。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンや USB ドングルなど）を USB ケーブルでルーターの USB ポートに接続します。
    2. モバイルデバイスの設定で **USB Tethering** または **Personal Hotspot** を有効にします。iPhone を使用している場合は、表示されたら **Trust This Device** をタップしてください。
    3. タッチスクリーンで **Tethering** を選択し、**Connect** をタップします。ルーターがデバイスへ接続します。
    4. インターネット接続に成功すると、タッチスクリーンのホーム画面にある Tethering セクションが青色（アクティブ）になります。タッチスクリーンの Tethering をタップするか、Web 管理パネルにログインして接続の詳細を確認できます。

    **Note**: 接続に失敗する場合は、電源の供給電圧が 9V 3A を上回っていることを確認してください。電力が不足していると、USB ポートへ給電できないことがあります。上記の手順をやり直すか、Web 管理パネルにログインして Tethering の接続状態を確認してください。

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. セルラー USB モデムを Slate 7 Pro の USB ポートに接続します。USB モデムの回線を、接続されているすべてのデバイスで共有したい場合に便利です。
    2. インターネット接続に成功すると、タッチスクリーンのホーム画面にある Cellular セクションが青色（アクティブ）になります。タッチスクリーンの Cellular をタップするか、Web 管理パネルにログインして接続の詳細を確認できます。

---

以下は、Slate 7 Pro Web 管理パネルの主な機能の概要です。

## Wireless

Wireless ページでは、6GHz、5GHz、2.4GHz Wi-Fi ネットワークの設定を構成できます。Wi-Fi の有効化、TX 電力の設定、Wi-Fi 名（SSID）の指定、ランダム BSSID の有効化、Wi-Fi セキュリティモードとパスワードの選択、SSID 表示設定、Wi-Fi モード、帯域幅、チャネルの選択などが含まれます。

さらに、Slate 7 Pro は MLO Wi-Fi（Multi-Link Operation）にも対応しており、複数の無線ネットワークを同時に組み合わせることで、より高い帯域幅と信頼性の高い接続を実現できます。

Wireless の設定については、[Wireless](../../interface_guide/wireless.md) を参照してください。

## Clients

Clients ページには、接続中のデバイスに関する情報が表示されます。各クライアントについて、名前、IP アドレス、MAC アドレス、ダウンロード速度、アップロード速度、合計トラフィックを確認でき、クライアントをブロックしたり、その他の操作を実行したりできます。

Clients の設定については、[Clients](../../interface_guide/clients.md) を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、GL.iNet ルーターへ簡単にリモートアクセスして管理できるクラウドサービスです。

    GoodCloud の設定については、[GoodCloud](../../interface_guide/cloud.md) を参照してください。

=== "AstroWarp"

    AstroWarp は、GL.iNet ルーターに統合された高度なネットワーク機能です。登録やログインなしで自宅ネットワークへシームレスにリモートアクセスでき、トラフィック難読化を内蔵した AmneziaWG プロトコルにより、どこからでも安定かつ安全な接続を実現します。ルーター同士をアクセスコードでペアリングするだけで、トラベルルーターを自宅ネットワークへ数秒で安全に接続できます。

    AstroWarp の設定については、[AstroWarp](../../interface_guide/astrowarp.md) を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスと VPN サーバー間に安全な暗号化トラフィックを作成します。VPN クライアントとしてプライバシーとセキュリティを強化できるほか、VPN サーバーとしてリモートネットワークへアクセスすることもできます。Slate 7 Pro は OpenVPN と WireGuard をサポートしています。

=== "OpenVPN"

    Slate 7 Pro（および他の GL.iNet ルーター）は、高いセキュリティを備えた OpenVPN プロトコルをサポートしています。OpenVPN を設定するには、以下のチュートリアルを参照してください。

    * [OpenVPN クライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPN サーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 Pro（および他の GL.iNet ルーター）は、高速で扱いやすい WireGuard プロトコルをサポートしています。WireGuard を設定するには、以下のチュートリアルを参照してください。

    * [WireGuard クライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuard サーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク

=== "Multi-WAN"

    Multi-WAN は、ルーターに複数のインターネット接続（cellular、repeater、ethernet など）を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生すると、ルーターは自動的に別のインターネット接続へ切り替え、安定したインターネットアクセスを維持します。

    Multi-WAN の設定については、[Multi-WAN](../../interface_guide/multi-wan.md) を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなどの限られた範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。

    LAN の設定については、[Lan](../../interface_guide/lan.md) を参照してください。

=== "Guest Network"

    ゲストネットワークでは、IPv4 プライベートアドレス範囲 192.168.0.0/16、172.16.0.0/12、または 10.0.0.0/8 内でサブネットを設定し、ゲートウェイやネットマスク IP アドレスを指定し、AP 分離などのセキュリティ設定を構成できます。

    ゲストネットワークの設定については、[Guest Network](../../interface_guide/guest_network.md) を参照してください。

---

=== "DNS"

    DNS ページでは、カスタム DNS サーバーの設定、DNS リバインディング攻撃保護の有効化、すべてのクライアントの DNS 設定の上書き、カスタム DNS による VPN DNS の上書き、Ethernet 接続から DNS サーバーを自動取得または手動指定するモードの設定ができます。

    DNS の設定については、[DNS](../../interface_guide/dns.md) を参照してください。

=== "Ethernet Port"

    Ethernet Port ページでは、WAN と LAN ポートの設定、WAN/LAN インターフェースを Ethernet に設定する操作、WAN インターフェースの MAC モードと MAC アドレスの指定、ネゴシエートされたネットワークポート速度の表示が行えます。

    Ethernet ポートの管理については、[Ethernet Port](../../interface_guide/ethernet_port.md) を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。非常に広いアドレス空間を持ち、インターネットに接続されるデバイス数の増加に対応するために不可欠です。

    IPV6 の設定については、[IPV6](../../interface_guide/network_mode.md) を参照してください。

---

=== "IGMP Snooping"

    IGMP スヌーピングは、Ethernet スイッチでマルチキャストトラフィックを管理・制御するためのネットワーク最適化技術です。

    IGMP スヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md) を参照してください。

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークへどのように接続し、他のデバイスと通信するかを決定する構成設定です。

    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md) を参照してください。

=== "Drop-in Gateway"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN クライアントなど、メインルーターの機能を拡張します。

    ドロップインゲートウェイの設定については、以下のリンクを参照してください。

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network Acceleration は、CPU 負荷を軽減し、トラフィックパケット転送を高速化できます。

    Network Acceleration の設定については、[Network Acceleration](../../interface_guide/network_acceleration.md) を参照してください。

## フロー制御

=== "DPI Engine"

    DPI（Deep Packet Inspection）は、インテリジェントなネットワーク管理を支える中核機能です。従来のルーターが送信元または宛先アドレスの識別にとどまるのに対し、パケットペイロードを詳細に解析し、シグネチャライブラリとの照合によってユーザーがアクセスしているアプリケーションや Web サイトを正確に識別できます。これにより、より細かなトラフィック分類と制御が可能になります。

    [Netify](https://www.netify.ai/){target="_blank"} と統合された GL.iNet の DPI 機能は、軽量な組み込みプラグインを採用して効率的な展開を実現しています。Netify のオンライン更新シグネチャデータベースにより、より正確かつ効率的なネットワーク管理を行えます。

    詳細な手順については、[DPI Engine](../../interface_guide/dpi_engine.md) を参照してください。

=== "Data Statistics"

    Data Statistics は、アプリケーション別にネットワーク使用量を分類して可視化するインテリジェントなトラフィック分析ダッシュボードです。リアルタイムおよび履歴トラフィックを監視し、ネットワークの状況把握と制御に役立ちます。

    詳細な手順については、[Data Statistics](../../interface_guide/data_statistics.md) を参照してください。

=== "Content Filter"

    Content Filter は、DPI ベースの分類により、有害または悪意のある Web サイトを自動的にブロックするオンライン安全機能です。ネットワークをクリーンで安全な状態に保つのに役立ちます。

    詳細な手順については、[Content Filter](../../interface_guide/content_filter.md) を参照してください。

---

=== "Parental Control"

    Parental Control は、子どものデバイスを管理・制御するための機能です。スクリーンタイムの制限や、特定コンテンツへのアクセス制限などが含まれます。

    Parental Control の設定については、[Parental Control](../../interface_guide/parental_control.md) を参照してください。

=== "QoS"

    QoS（Quality of Service）は、ネットワーク混雑時にビデオ通話やゲームなどの重要な通信を優先し、帯域配分を最適化することで、遅延を減らしてネットワーク全体のパフォーマンスを向上させます。これはローカルクライアントトラフィックと VPN クライアントトンネルトラフィックに適用されますが、ルーターが VPN サーバーとして受信するトラフィックには適用されません。

    詳細な手順については、[QoS](../../interface_guide/qos.md) を参照してください。

=== "SQM"

    SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理し、遅延やバッファブロートを最小限に抑えることで、ゲームや音声通話をより滑らかにします。

    詳細な手順については、[SQM](../../interface_guide/sqm.md) を参照してください。

## セキュリティ

=== "Port Forwarding"

    ポートフォワーディングにより、インターネット上のリモートサーバーやデバイスが、プライベートネットワーク内のデバイスへアクセスできるようになります。

    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md) を参照してください。

=== "Management Control"

    Management Control では、ネットワークやルーターを不正アクセスから保護するための各種セキュリティ設定を構成できます。このページには以下の項目があります。

    * Local Access Control: ローカルネットワークに接続されたデバイスから、ルーターの管理画面へアクセスできる範囲を管理・制限します。
    * Remote Access Control: インターネット経由でのリモートアクセスを構成・制限し、外部からの脅威に対するセキュリティを強化します。
    * Open Ports on Router: ルーター上で開放するポートを管理し、潜在的な脆弱性や不正アクセスのリスクを抑えます。

    これらの設定により、ルーターと接続デバイスを保護しながら、安全なネットワーク環境を維持できます。

    詳細な手順については、[Security](../../interface_guide/security.md) を参照してください。

=== "NAT Mode"

    NAT Mode ページでは、Full Cone NAT と SIP ALG（Application Layer Gateway）機能の有効 / 無効を切り替えられます。

    NAT 設定については、[NAT Mode](../../interface_guide/nat_settings.md) を参照してください。

## アプリケーション

=== "Plug-ins"

    プラグインは、既存のプログラムへ特定の機能を追加し、カスタマイズや機能拡張を可能にするソフトウェアコンポーネントです。

    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md) を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられた IP アドレスをリアルタイムで自動検出して更新します。リモートネットワークへアクセスするために固定 IP アドレスが必要な場合に特に便利です。

    Dynamic DNS の設定については、[Dynamic DNS](../../interface_guide/ddns.md) を参照してください。

=== "Network Storage"

    ネットワークストレージは、複数のユーザーやデバイスがネットワーク経由でファイルへアクセスし、共有できる集中型のデータ保存ソリューションです。

    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md) を参照してください。

---

=== "AdGuard Home"

    AdGuard Home は、家庭内ネットワーク全体で広告やトラッカーをブロックするソリューションであり、接続されたすべてのデバイスに対して不要なコンテンツをフィルタリングする DNS サーバーとして動作します。

    AdGuard Home の設定については、[AdGuard Home](../../interface_guide/adguardhome.md) を参照してください。

=== "Tailscale"

    Tailscale は、どこからでもデバイスやアプリケーションへアクセスできる VPN サービスです。

    Tailscale の設定については、[Tailscale](../../interface_guide/tailscale.md) を参照してください。

=== "ZeroTier"

    ZeroTier は、インターネット上に安全な仮想ネットワークを構築し、デバイスを同一のローカルネットワークにあるかのように接続できるソフトウェア定義ネットワーキングソリューションです。

    ZeroTier の設定については、[ZeroTier](../../interface_guide/zerotier.md) を参照してください。

=== "Tor"

    Tor（The Onion Router）は、匿名通信を実現するプライバシー重視のネットワークです。インターネットトラフィックを複数のボランティア運用ノード経由で中継することで、ユーザーの位置情報や利用状況を追跡しにくくします。

    * [Tor の設定方法](../../interface_guide/tor.md)

## システム

=== "Overview"

    Overview ページでは、ルーターの現在の状態やパフォーマンス指標を一目で確認できます。主な内容は以下のとおりです。

    * CPU Average Load: ルーター CPU の平均負荷を監視し、性能評価やボトルネック特定に役立ちます。
    * Memory Usage: ルーターで使用中のメモリ量を確認し、リソース管理に役立てられます。
    * LED Control: ルーターの LED ライトをオン / オフでき、視覚インジケーターを調整できます。
    * Flash Usage: フラッシュストレージの使用状況を確認し、ファームウェアや設定データのための十分な空き容量を確保できます。
    * Device Info: 稼働時間、ホスト名、モデル、アーキテクチャ、OpenWrt バージョン、カーネルバージョン、デバイス ID、デバイス MAC、デバイス S/N などの詳細情報を確認できます。
    * External Storage: USB ドライブや TF カードなど、接続された外部ストレージデバイスの状態を確認できます。

    これらの機能により、ルーターの動作を効果的に管理・監視できます。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md) を参照してください。

=== "Admin Password"

    Admin Password ページでは、ルーターの管理インターフェース用パスワードを設定または変更できます。権限のあるユーザーだけが設定を変更できるようにするための重要な項目です。

    セキュリティのため、**Prevent Weak Password** を有効にすることを推奨します。

    **Prevent Weak Password** を有効にした場合、新しいパスワードは以下の条件を満たす必要があります。

    * 5 文字以上 63 文字以下
    * 使用可能文字: 英字（大文字 / 小文字を区別）、数字、記号 `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``
    * 大文字、小文字、数字、記号のうち少なくとも 2 種類を含むこと

    詳細な手順については、[Admin Password](../../interface_guide/admin_password.md) を参照してください。

=== "Upgrade"

    Upgrade ページでは、ルーターのファームウェアを最新バージョンへ更新できます。これにより、パフォーマンス、セキュリティ、新機能を改善できます。このページには次の 2 つのアップグレード方法があります。

    * Firmware Online Upgrade: メーカーのサーバーから最新ファームウェアを自動確認し、そのままインストールします。
    * Firmware Local Upgrade: コンピューターからファームウェアファイルを手動でアップロードし、アップグレードするバージョンやタイミングを管理できます。

    これらの方法により、ルーターを常に最新の改善や修正に追従させることができます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md) を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、あらかじめ設定したスケジュールに基づいて、さまざまなルーター機能を自動化できます。主な機能は次のとおりです。

    * LCD Display Schedule: ルーターの LCD 画面を自動的にオン / オフするスケジュールを設定し、特定時間帯の光を抑えられます。
    * Schedule Reboot: 指定した間隔でルーターを自動再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fi Status Schedule: 6GHz / 5GHz / 2.4GHz / MLO Wi-Fi バンドを制御するスケジュールを設定し、ネットワーク可用性や消費電力を管理できます。

    これらの設定により、ルーターの動作をより柔軟にコントロールできます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md) を参照してください。

=== "Display Management"

    Display Management ページでは、タッチスクリーン表示と関連設定を幅広く管理できます。

    ‒ Wallpaper: 壁紙や画面ウェイク時の表示スタイルをカスタマイズします。
    ‒ Brightness: タッチスクリーンの明るさを調整します。スライダーまたは数値入力で周囲の明るさに合わせて設定できます。
    ‒ Auto Lock: 操作がない場合に画面を自動ロックするまでの時間を設定します。範囲は 1 分から 30 分です。
    ‒ Screen Always On: タッチスクリーンを常時点灯させるか、無操作時に消灯させるかを切り替えます。
    ‒ Enable Screen Passcode: タッチスクリーン用のパスコードを設定し、追加のセキュリティを確保します。

    詳細な手順については、[Display Management](../../interface_guide/display_management.md) を参照してください。

=== "Time Zone"

    Time Zone ページでは、ルーターのタイムゾーンを正しく設定できます。これにより、スケジュールタスク、ログ、システムイベントに記録される時刻が現地時間に合わせて正確になります。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md) を参照してください。

---

=== "Toggle Button Settings"

    Toggle Button Settings ページでは、ルーターの物理トグルボタンに特定の機能を割り当て、すばやく操作できるように設定できます。よく使う機能へのショートカットとして利用でき、ルーター管理をより簡単にします。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md) を参照してください。

=== "Reset Firmware"

    Reset Firmware ページでは、現在インストールされているファームウェアバージョンの設定を初期状態に戻し、すべてのカスタム設定を消去できます。現在のファームウェアのままでトラブルシューティングしたい場合や、まっさらな状態からやり直したい場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md) を参照してください。

=== "Log"

    Log ページでは、ルーターの動作やイベントを記録するさまざまなログを確認でき、トラブルシューティングやパフォーマンス監視に役立ちます。このページには以下が含まれます。

    * System Log: システムレベルのイベントや動作に関する詳細ログ
    * Kernel Log: カーネルの動作やイベントに関するログ
    * Crash Log: システムクラッシュやエラーの記録。重大な問題の診断に役立ちます。
    * Cloud Log: ルーターに統合された GoodCloud サービスに関する操作ログ
    * Nginx Log: ルーターで使用されている場合、Nginx Web サーバーのアクセスや動作に関するログ

    さらに、Export Log ボタンにより収集したログをまとめてエクスポートでき、技術サポートによる分析にも活用できます。

    詳細な手順については、[Log](../../interface_guide/log.md) を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションにアクセスできます。基本インターフェースでは扱わない、詳細なネットワーク設定、ファイアウォール設定、システムカスタマイズなどを行いたい上級ユーザー向けの機能です。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md) を参照してください。
