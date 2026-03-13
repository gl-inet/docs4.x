# Slate 7 (GL-BE3600) ユーザーガイド

## 製品概要

Slate 7 (GL-BE3600) は、GL.iNet初のWi-Fi 7対応デュアルバンドトラベルルーターです。Multi-Link Operationや4K QAMなどのフラッグシップWi-Fi 7技術を搭載し、688Mbps (2.4GHz) + 2882Mbps (5GHz) の理論のなデュアルバンド速度を実現し、8Kストリーミングやモバイルゲーム体験を可能にします。タッチスクリーンにより、ネットワークの状態を一目で確認し、直感のな基本操作を行うことができます。

2× 2.5G Ethernetポート (1 WAN + 1 LAN) と1× USB 3.0ポートを備え、高速有線接続と柔軟なストレージ拡張のニーズに対応します。Type-C PD電源 (5V/3A, 9V/3A, 12V/2.5A) もサポートしており、コンパクトで軽量なデザインで持ち運びに便利です。AdGuard Homeがプリインストールされており、30以上のVPNサービスに対応しているため、ネットワーク強力なセキュリティを提供します。モバイルの利便性とプロフェッショナルグレードのパフォーマンスを兼ね備えたSlate 7は、.remote workやモバイルネットワーク共有に最も適です。

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

## パッケージコンテンツ

パッケージには以下が含まれます：

- 1 x Slate 7 (GL-BE3600)
- 1 x ユーザーガイド
- 1 x サンキューカード
- 1 x Ethernet cable
- 1 x 電源コード
- 1 x US Power Adapter
- 3 x コンバーター (EU, UK, AU plugs)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

Slate 7の開栓動画については、以下を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/bEuwGm0hQ5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Slate 7の設定方法

Slate 7の設定には、Ethernet、Repeater、Tethering、Cellularの4つのインターネット接続方法が使えます。設定動画を見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(この動画では、Slate 7をRepeaterとして設定する方法を示しています。彼のインターネット接続方法でSlate 7を設定する必要がある場合は、以下の手順を参照してください。)</small>

### 1. Slate 7の電源を入れる

二分割の電源アダプターを組み合わせます。ルーターに接続し、コンセントに挿すと自動的に起動します。

### 2. タッチスクリーン

??? "電源オン"

    ルーターの電源を入れると、スクリーンにGL.iNetのロゴが表示され、その後にスタートアップ進捗バーが表示されます。

    ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){class="glboxshadow"}
    
    進捗バーが完全にロードされると、デバイスの起動が完たします。

??? "ネットワーク"

    ホームスクリーンには、4つのネットワーク接続タイプ（Ethernet、Repeater、Tethering、Cellular）を表す4つのアイコンが表示されます。

    ![network connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){class="glboxshadow"}

    |  色           | 状態                         |
    | :------------------ | :----------------------------- |
    | 緑             | ネットワーク接続済み              |
    | 黄              | ネットワーク接続中または異常接続（例：インターネットアクセスなし）   |
    | 白               | ネットワーク未接続          |

    いずれかのアイコンをクリックして、ネットワーク状態の詳細設定情報を表示します。

??? "機能"

    左右にスワイプして機能にアクセスできます。

    右から左にスワイプすると順に表示されます。一部の機能は管理パネルでの事前設定が必要です。左から右にスワイプすると、逆順で表示されます。

    - ネットワーク接続

        ![network connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){class="glboxshadow"}

    - トライバンドWi-Fiの詳細（SSID、パスワード、QRコード、スイッチボタンを含む）

        ![wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wifi-details.png){class="glboxshadow"}

    - OpenVPN

        ![openvpn](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/nordvpn-4.7.jpg){class="glboxshadow"}

    - WireGuard

        ![wireguard](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wireguard.png){class="glboxshadow"}

    - AdGuard Home

        ![adguard home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/adguard_home.png){class="glboxshadow"}

    - Tor

        ![tor](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/tor.png){class="glboxshadow"}

    - トラフィック統計（ルーター器を通過するすべてのトラフィックの平均速度を指します。速度は3秒ごとに計算されます。）

        ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/traffic_statistics.png){class="glboxshadow"}

    - CPU概要

        ![CPU overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/overview.png){class="glboxshadow"}

    - 時間

        ![time](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/time.png){class="glboxshadow"}

??? "システム"

    上から下にスワイプしてシステム設定にアクセスします：RebootとLock Screen。

    ![system settings](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/system_settings.png){class="glboxshadow"}

    - Reboot: 「Reboot」をクリックすると、「Slide To Reboot」のプロンプト（二段階認証）が表示され、ルーターは再起動プロセスを開始します。

        ![slide to reboot](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-reboot.png){class="glboxshadow"}

    - Lock Screen: 「Lock Screen」をクリックするとスクリーンがオフになります。スクリーンをタップして起こすと、最も後に表示していた機能ページが表示されます。もう一度クリックすると、「Slide To Unlock」のプロンプトが表示されます。

        ![slide to unlock](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-unlock.png){class="glboxshadow"}

### 3. Slate 7に接続する

Wi-FiまたはEthernetを使用してデバイス（コンピュータ、ラップトップ、スマートフォンなど）をルーターに接続します。

- Ethernet

    Ethernetケーブルを使用してデバイスをルーターのLANポートに接続します。

- Wi-Fi

    デバイスで、利用可能なネットワークリストからルーターのWi-Fiネットワーク名を見つけ、パスワードを入力してネットワークに参加します。デフォルトのネットワーク名とパスワードはルーターのラベルに印刷されています。

### 4. WebGUIにログインする

Webブラウザーでアドレスバーに`192.168.8.1`を入力してログインします。言語を選択し、管理者パスワードを設定して、**Apply**をクリックします。

### 5. Slate 7をインターネットに接続する

**注意:** 以下の説明は、GL.iNet Web管理パネルでルーターを設定するユーザーに適用されます。GL.iNetアプリを使用する場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}して画面の説明に従ってください。

サポートされているインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用してSlate 7を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class="glboxshadow"}
    
    Slate 7のWANポートをEthernetケーブルで上游デバイス（モデムなど）に接続します。
    
    インターネットに正常に接続されると、INTERNETページのEthernetセクションに緑色のドットが表示されます。

    詳細な手順については、[Ethernetケーブルでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class="glboxshadow"}

    1. Web管理パネルのINTERNET画面で、Repeaterセクションを見つけ、**Connect**をクリックします。
    2. 利用可能なWi-Fiネットワークから選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのRepeaterセクションに緑色のドットが表示されます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSBドングルなど）をUSBケーブルでルーターのUSBポートに接続します。
    2. モバイルデバイスでSettingsを開き、USB Tetheringを有効にします。
    3. Web管理パネルのINTERNET画面で、Tetheringセクションの**Connect**をクリックします。
    
    インターネットに正常に接続されると、INTERNETページのTetheringセクションに緑色のドットが表示されます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class="glboxshadow"}

    Slate 7のUSBポートにCellular USBモデムを挿します。これは、USBモデムからすべての接続デバイスにインターネットを共有するのに便利です。

    インターネットに正常に接続されると、INTERNETページのCellularセクションに緑色のドットが表示されます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下是Slate 7 WebGUI機能の概述。

## Wireless

Wirelessページでは、5 GHzと2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、TX電力の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSID可視性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

また、Slate 7はMLO Wi-Fi（Multi-Link Operation）をサポートしており、複数のWi-Fiネットワークを同時に組み合わせて、より高い帯域幅とより信頼性の高い接続を実現します。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients

Clientsページには、接続されたデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレスとMACアドレス、ダウンロード速度とアップロード速度、合計トラフィックが表示され、クライアントをブロックしたりその彼のアクションを実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}は、GL.iNetルーターに簡単かつシンプルにリモートアクセスと管理を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarpは、シームレスなリモートネットワークとリモートデバイス管理を提供するために設計された高度なネットワーキングプラットフォームです。GL.iNetルーター連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位と下位のデバイス制御を可能にします。ネットワーク全体の管理とする来のハードウェアレベル制御のサポートに焦時を当てたAstroWarpは、デバイスの管理と安全で安定したネットワークの維持のためのより堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Slate 7はOpenVPN、WireGuard、Torをサポートしています。

=== "OpenVPN"
    
    Slate 7（およびその彼のGL.iNetルーター器）は強力なセキュリティを提供するOpenVPNプロトコルをサポートしています。OpenVPNを設定するには、以下のチュートリアルに従ってください：

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Slate 7（およびその彼のGL.iNetルーター器）は、高速性と利便性に優れたWireGuardプロトコルをサポートしています。WireGuardを設定するには、以下のチュートリアルに従ってください：

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

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。リモートネットワークにアクセスするために静のIPアドレスが必要なユーザーに便利です。
    
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

    ZeroTierは、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全に仮想ネットワークを作成し、デバイスに same 一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサービです。
    
    Tailscapeの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

## ネットワーク

=== "Port forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Multi-WAN"

    Multi-WANは、ルーターに複数のインターネット接続（cellular、repeater、ethernetなど）を同時に設定できるネットワーキング機能です。現にのインターネット接続が失敗すると、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れないインターネットアクセスが確保されます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、から宅やオフィスなど、限られたに理の領域内でコンピュータとデバイスを接続するネットワークです。高速データ転送とリソース共有を可能にし、デバイスが効率のに相互通信できます。
    
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

    ネットワークモードは、デバイスがネットワークに接続し、彼のデバイスと通信する方法を決定する構成設定を指します。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4を置き換えるために設計されたインターネットプロトコルの最も新バージョンです。ほぼ無限の数の固有のIPアドレスを可能にする大幅なアドレス空間を提供し、インターネットに接続するデバイスの増加に対応するために不可欠です。
    
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

    Overviewページは、ルーターの現にのパフォーマンス指標とステータスの含まれるのなスナップショットを提供します。このページでは以下を表示できます：

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーター器のフラッシュストレージの使用率を確認し、ファームウェアと設定データのための非常にな空間を確保します。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーターの操作を効果のに管理および監視するのに役立つ重要な洞察とコントロールを提供します。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Upgrade"

    Upgradeページは、ルーターのファームウェアを最も新バージョンにアップデートするために使用され、パフォーマンス、セキュリティ、新機能の向上を確保します。このページには2つのアップグレードオプションがあります：

    * ファームウェアオンラインアップグレード：製造元のサーバーから最も新バージョンを自動的に確認してインストールし、アップデートプロセスを簡素化します。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最も新の改善と修正でルーターを最も新の状態に保つことができます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasksページにより、事前定義されたスケジュールに基づいてさまざまなルーター機能をから動化でき、利便性と効率性がへ上します。このページの主要機能は次のとおりです：

    * LED表示スケジュール：特定の時間帯にルーターのLEDライトを自動的にオンまたはオフに設定し、光害を軽減します。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最も適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fiステータススケジュール：5GHz / 2.4GHz / MLO Wi-Fiバンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力の管理を改善できます。
    
    これらのスケジューリングオプションは、ルーターの操作をより詳細に制御し、特定のニーズと好みに合わせることができます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

---

=== "Display Management"

    Display Managementページでは、タッチスクリーン表示と関連設定を含まれるのに管理できます。
    
    - 機能管理：タッチスクリーンに表示される機能を管理し、表示をニーズに合わせてカスタマイズします。
    - ロックスクリーン：ロックスクリーン設定をカスタマイズします。壁紙とウェイク表示を設定できます。
    - 明るさ：タッチスクリーンの明るさを調全体します。スライダーを使用するか、特定のレベル（1〜10の範囲）を入力して、さまざまな照明条件に合わせます。
    - から動ロック：アクティビティがない場合にスクリーンが自動的にロックされるまでの遅延時間を設定します。範囲は1〜30分です。
    - スクリーン常時時灯：タッチスクリーンが継続のにオン Stayまたはに一定時間後にオフにするかを決定するオプションを切り替えます。
    - スクリーンパスコードの有効化：タッチスクリーンのパスコードを有効にして、追加のセキュリティレイヤーを追加します。

    詳細な手順については、[Display Management](../../interface_guide/display_management.md)を参照してください。

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現に時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Toggle Button Settings"

    Toggle Button Settingsページでは、ルーターの物理トグルボタンを構成でき、ボタンに特定の機能を割り当ててクイックアクセスと制御を可能にします。この機能は、一般的なタスクと設定への便利なショートカットを提供し、ユーザーエクスペリエンスをへ上させ、ルーターの管理を簡素化します。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md)を参照してください。

---

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはExport Logボタンがあり、収集したすべてのログをエクスポートして技術サポートの分析にできます。この機能は、複雑な問題の診断と専門のサポートの取なければならないに非常に便利です。

    詳細な手順については、[Log](../../interface_guide/log.md)を参照してください。

=== "Security"

    Securityページでは、ネットワークとルーター器を不正アクセスから保護するためのさまざまなセキュリティ設定を構成できます。このページには以下のオプションがあります：

    * 管理者パスワード：ルーター器の管理インターフェースのパスワードを設定または変更し、許可されたユーザーのみが設定を変更できるようにします。
    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーター器のインターフェースへのアクセスを管理および制限します。
    * リモートアクセス制御：インターネット上のリモート場所からルーター器のインターフェースへのアクセスを構成および制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    これらの設定は、ネットワーク環境を安全に保ち、ルーターと接続されたデバイスを保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "Reset Firmware"

    Reset Firmwareページでは、ルーターの現にのファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。このプロセスは、現にインストールされているファームウェアバージョンのデフォルト設定にルーターを復元します。持続のな問題のトラブルシューティングや現にのファームウェアのデフォルト設定で新鮮に開始するのに便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Advanced Settings"

    Advanced Settingsページは、OpenWrt LuCIインターフェースを通じて高度な構成オプションへのアクセスを提供し、経験豊富なユーザーが基本インターフェースオプションを超えてルーターの設定と機能を微調全体できます。これには、詳細なネットワーク設定、ファイアウォール設定、その彼の高度なシステムカスタマイズが含まれます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
