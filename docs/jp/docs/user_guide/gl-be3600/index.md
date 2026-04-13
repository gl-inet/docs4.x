# Slate 7 (GL-BE3600) ユーザーガイド

## 製品概要

Slate 7 (GL-BE3600) は、GL.iNet初のWi-Fi 7対応デュアルバンドトラベルルーターです。Multi-Link Operation や 4K QAM などの先進的な Wi-Fi 7 技術を搭載し、理論値で 688Mbps（2.4GHz）+ 2882Mbps（5GHz）の通信速度を実現します。8Kストリーミングやモバイルゲームにも対応し、タッチスクリーンでネットワーク状態の確認や基本操作を直感的に行えます。

2× 2.5G Ethernet ポート（1 WAN + 1 LAN）と 1× USB 3.0 ポートを備え、高速な有線接続と柔軟なストレージ拡張に対応します。Type-C PD 電源（5V/3A、9V/3A、12V/2.5A）にも対応しており、コンパクトで軽量なため持ち運びにも便利です。AdGuard Home をプリインストールし、30種類以上のVPNサービスに対応しているため、ネットワークに高いセキュリティを提供します。モバイル性とプロ向け性能を兼ね備えた Slate 7 は、リモートワークやモバイルネットワーク共有に適しています。

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

## パッケージコンテンツ

パッケージには以下が含まれます：

- 1 x Slate 7 (GL-BE3600)
- 1 x ユーザーガイド
- 1 x サンキューカード
- 1 x Ethernetケーブル
- 1 x 電源コード
- 1 x US電源アダプター
- 3 x 変換プラグ（EU、UK、AU）

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

Slate 7 の開封動画は以下をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/bEuwGm0hQ5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Slate 7の設定方法

Slate 7の設定には、Ethernet、Repeater、Tethering、Cellularの4つのインターネット接続方法が使えます。設定動画を見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(この動画では、Slate 7 を Repeater として設定する方法を紹介しています。その他のインターネット接続方法で設定する場合は、以下の手順を参照してください。)</small>

### 1. Slate 7の電源を入れる

二分割の電源アダプターを組み合わせます。ルーターに接続し、コンセントに挿すと自動的に起動します。

### 2. タッチスクリーン

??? "電源オン"

    ルーターの電源を入れると、スクリーンにGL.iNetのロゴが表示され、その後にスタートアップ進捗バーが表示されます。

    ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){class="glboxshadow"}
    
    進捗バーが最後まで読み込まれると、デバイスの起動が完了します。

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

    - トラフィック統計（ルーターを通過するすべての通信の平均速度を表示します。速度は3秒ごとに計算されます。）

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

    - Lock Screen: 「Lock Screen」をクリックするとスクリーンがオフになります。画面をタップして起動すると、最後に表示していた機能ページが再び表示されます。もう一度クリックすると、「Slide To Unlock」のプロンプトが表示されます。

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
    
    Slate 7 の WAN ポートを Ethernet ケーブルで上位機器（モデムなど）に接続します。
    
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

以下は Slate 7 WebGUI の主な機能の概要です。

## Wireless

Wirelessページでは、5 GHzと2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、TX電力の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSID可視性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

また、Slate 7はMLO Wi-Fi（Multi-Link Operation）をサポートしており、複数のWi-Fiネットワークを同時に組み合わせて、より高い帯域幅とより信頼性の高い接続を実現します。

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

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Slate 7はOpenVPN、WireGuard、Torをサポートしています。

=== "OpenVPN"
    
    Slate 7（およびその他の GL.iNet ルーター）は、高いセキュリティを提供する OpenVPN プロトコルをサポートしています。OpenVPN を設定するには、以下のチュートリアルを参照してください。

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Slate 7（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルをサポートしています。WireGuard を設定するには、以下のチュートリアルを参照してください。

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

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出して更新します。固定IPアドレスなしでリモートネットワークへアクセスしたい場合に便利です。
    
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

    ZeroTier は、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全な仮想ネットワークを構築し、デバイスを同一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscale は、どこからでもデバイスやアプリケーションにアクセスできるVPNサービスです。
    
    Tailscale の設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

## ネットワーク

=== "Port forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Multi-WAN"

    Multi-WAN は、ルーターに複数のインターネット接続（cellular、repeater、ethernet など）を同時に設定できる機能です。現在のインターネット接続に障害が発生すると、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、安定したインターネットアクセスを維持できます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなどの限られた地理的範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。
    
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

    ネットワークモードは、デバイスがネットワークに接続し、他のデバイスと通信する方法を決定する構成設定です。
    
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

    Overview ページでは、ルーターの現在のパフォーマンス指標とステータスを含む概要を確認できます。このページでは以下を表示できます。

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーターのフラッシュストレージ使用率を確認し、ファームウェアや設定データのための十分な空き容量を確保します。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーターの動作を効果的に管理・監視するのに役立つ重要な情報と制御機能を提供します。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Upgrade"

    Upgrade ページでは、ルーターのファームウェアを最新バージョンへ更新できます。これにより、性能向上、セキュリティ強化、新機能の利用が可能になります。このページには次の2つのアップグレード方法があります。

    * ファームウェアオンラインアップグレード：メーカーのサーバーから最新バージョンを自動確認してインストールします。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善や修正を適用した状態にルーターを保てます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前定義したスケジュールに基づいてルーター機能を自動化でき、利便性と効率が向上します。主な機能は次のとおりです。

    * LED表示スケジュール：特定の時間帯にルーターのLEDライトを自動的にオンまたはオフに設定し、光害を軽減します。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最も適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fiステータススケジュール：5GHz / 2.4GHz / MLO Wi-Fiバンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力の管理を改善できます。
    
    これらのスケジューリングオプションは、ルーターの操作をより詳細に制御し、特定のニーズと好みに合わせることができます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

---

=== "Display Management"

    Display Management ページでは、タッチスクリーン表示と関連設定を管理できます。
    
    - 機能管理：タッチスクリーンに表示される機能を管理し、表示をニーズに合わせてカスタマイズします。
    - ロックスクリーン：ロックスクリーン設定をカスタマイズします。壁紙とウェイク表示を設定できます。
    - 明るさ：タッチスクリーンの明るさを調整します。スライダーを使用するか、特定のレベル（1〜10）を入力して、照明条件に合わせて設定できます。
    - 自動ロック：操作がない場合にスクリーンが自動的にロックされるまでの時間を設定します。範囲は1〜30分です。
    - スクリーン常時点灯：タッチスクリーンを常にオンにするか、一定時間後にオフにするかを切り替えます。
    - スクリーンパスコードの有効化：タッチスクリーンのパスコードを有効にして、追加のセキュリティレイヤーを追加します。

    詳細な手順については、[Display Management](../../interface_guide/display_management.md)を参照してください。

=== "Time Zone"

    Time Zone ページでは、ルーターの正しいタイムゾーンを設定できます。これにより、すべてのスケジュールタスク、ログ、システムイベントに現地時間で正確なタイムスタンプが付与されます。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Toggle Button Settings"

    Toggle Button Settings ページでは、ルーターの物理トグルボタンを設定し、特定の機能を割り当ててすばやく操作できるようにします。この機能により、よく使うタスクや設定へのショートカットを提供し、ユーザー体験を向上させ、ルーター管理を簡単にします。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md)を参照してください。

---

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、このページには Export Log ボタンがあり、収集したすべてのログをエクスポートして技術サポートによる分析に利用できます。複雑な問題の診断や専門的なサポートを受ける際に非常に便利です。

    詳細な手順については、[Log](../../interface_guide/log.md)を参照してください。

=== "Security"

    Security ページでは、ネットワークとルーターを不正アクセスから保護するためのさまざまなセキュリティ設定を構成できます。このページには以下のオプションがあります。

    * 管理者パスワード：ルーターの管理インターフェースのパスワードを設定または変更し、許可されたユーザーのみが設定を変更できるようにします。
    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーターのインターフェースへのアクセスを管理・制限します。
    * リモートアクセス制御：インターネット上のリモート環境からルーターのインターフェースへアクセスする条件を構成・制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    これらの設定は、ネットワーク環境を安全に保ち、ルーターと接続されたデバイスを保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "Reset Firmware"

    Reset Firmware ページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。持続的な問題のトラブルシューティングや、現在のファームウェアの初期設定からやり直したい場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションへアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えて、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズを行えます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
