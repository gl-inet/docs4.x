# Mudi 7 (GL-E5800) ユーザーガイド

## 製品概要

Mudi 7は、ロードウォリアーとビジネス旅行者へけのポータブル5G NR Wi-Fi 7トラベルルーターです。5Gハイスピード、デュアルSIMから動切替（フェイルオーバー）、Wi-Fi 7（320MHzチャンネルと4K QAM）を特徴とし、安定した高速接続を実現します。高速ダウンロード、4Kストリーミング、混雑したに域でも遅延のないビデオことになる議をサポートします。

タッチスクリーンを備えたMudi 7では、リアルタイムのデータ使用量、シグナル強度、接続されたデバイスを監視したり簡単なスワイプで設定を調全体したりできます。インターフェースにはワンタップのネットワーク最適化と動のなキュー（速度、バッテリーなど）が含まれ、手間のかからない直感のな制御を提供します。

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## パッケージコンテンツ

パッケージ内のアダプターは発送国によって異なることに注意してください。

パッケージには以下が含まれます：

- 1 x Mudi 7 (GL-E5800)
- 1 x バッテリーパック
- 1 x 10Gbps USB-C ケーブル
- 1 x トラベルケース
- 1 x ユーザーガイド
- 1 x 保証書

## Mudi 7の設定方法

### 1. Nano-SIMカードのインストール

まず、バッテリーカバーを外し、次にMudi 7のバッテリーを取り出します。

次に、Nano-SIMカードを挿入します。1枚のカードのみ使用する場合は、SIM 1を優先してください。

最も後に、バッテリーとカバーを元に戻します。

![install nano-sim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/install_nano-sim.png){class="glboxshadow"}

### 2. 電源を入れる

**3秒間**電源ボタンを長押しするか、電源アダプターを挿します。

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power_on.png){class="glboxshadow"}

次に、画面の指示に従ってデバイス初期化を完たするか、以下の手順に従って続行します。

### 3. Mudi 7に接続する

Wi-Fi、Ethernet cable、またはUSB cableを使用してデバイス（コンピュータ、ラップトップ、スマートフォンなど）をMudi 7に接続します。

- **Wi-Fi**

    <u>QRコード</u>: デバイスを使用してMudi 7の画面上のQRコードをスキャンします。次に、デバイスで「Join」をクリックして接続します。

    <u>手動接続</u>: デバイスで、Settings -> WLANを開き、利用可能なネットワークリストからMudi 7のWi-Fiネットワーク名を見つけ、パスワードを入力してネットワークに参加します。（デフォルトのネットワーク名とパスワードはラベルに印刷されています。）

- **Ethernet**

    Ethernet cableを使用してデバイスをMudi 7のEthernetポート（デフォルトLAN）に接続します。

- **USB**

    USB cableを使用してデバイスをMudi 7のUSB-Cポートに接続します。OTG対応USB-Cポートにより、次のステップでMudi 7のWebGUIにアクセスできます。

### 4. WebGUIにログインする

Webブラウザーでアドレスバーに`192.168.8.1`を入力し、Mudi 7のログインページにアクセスします。言語を選択し，管理者パスワードを設定して、**Apply**をクリックします。

### 5. Mudi 7をインターネットに接続する

サポートされているインターネット接続方法（Cellular、Ethernet、Repeater、Tethering、USB Ethernet）のいずれかを使用してMudi 7を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}
    
    Mudi 7には**組み込みeSIM**と**デュアルNano‑SIM**スロットが備わっています。eSIMパッケージを購入して（物理SIMカード不要）、またはNano‑SIMカードを挿入して5Gモバイルネットワークにアクセスできます。
    
    - eSIM: タッチスクリーンで**Cellular** -> **Active SIM Card**に移動し、eSIMを有効にしてから、eSIMプロファイルをアップロードするかeSIMプロファイルストアで購入します。

    - Nano‑SIM: Mudi 7のカバーを外し、バッテリーを取り出し、Nano-SIMカードをスロットに挿してから、バッテリーを取り付けます。

    インターネットに正常に接続されると、タッチスクリーンの右上にシグナルバーとcellularステータスが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

    !!! note

        1. 組み込みeSIMとSIM 2は相互に排彼のであり、同時にアクティブにできません。eSIMはデフォルトで無効です。eSIMを有効にすると、SIMカードが挿入されていてもSIM 2は機能しません。
        2. Mudi 7には組み込みeSIMが備わっているため、SIMPoYo eSIM物理カードはMudi 7ではeSIM機能なしで通例のSIMカードとして認識されます。

=== "Ethernet"
    
    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Mudi 7のEthernetポートをEthernet cableで上游ネットワークソース（ISPモデム、ネットワークスイッチ、または壁のEthernetジャック）に接続します。
    2. タッチスクリーンまたはWeb管理パネルで、**Network** -> **Ethernet Ports**に移動し、ポートの役割を**WAN**に設定し、**Apply**をクリックします。

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. インターネットに正常に接続されると、タッチスクリーンの右上にEthernetポートアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[Ethernet cableでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"
    
    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. タッチスクリーンまたはWeb管理パネルで、**Internet** -> **Repeater**に移動し、**Connect**をクリックします。Mudi 7は利用可能なWi-Fiネットワークのスキャンを開始します。
    2. Mudi 7が拡張するWi-Fiネットワークを選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    4. インターネットに正常に接続されると、タッチスクレンの右上にWi-Fiアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSB dongleなど）をUSB cableでMudi 7のUSB-Cポートに接続します。
    2. モバイルデバイスでSettingsを開き、**USB Tethering**を有効にします。iPhoneを使用する場合は、表示される場合は「Trust This Device」をタップします。
    3. Mudi 7は自動的にデバイスに接続します。接続しない場合は、上記の手順を繰り返すか、Web管理パネルにログインしてINTERNETページでTethering接続を確認します。
    4. インターネットに正常に接続されると、タッチスクレンの右上にチェーンリンクアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7は**OTG対応**USB-Cポートを備えており、**別途販売されているUSB‑C‑to‑Ethernetアダプター**を使用して2番目のEthernetポートを追加し、Dual-Ethernet WANを可能にします。

    <small>*USB OTG（On-The-Go）は、ルーターなどの互換性のあるデバイスがホストと周辺機器の役割を切り替えて、個別のホストデバイスなしで直接データ伝送と電力交互作用を可能にするUSB標準です。</small>

    1. 上游ネットワークソース（ISPモデム、ネットワークスイッチ、または壁のEthernetジャック）をUSB C-to-Ethernetアダプター経由でMudi 7のUSB-Cポートに接続します。
    2. タッチスクリーンまたはWeb管理パネルで、**Network** -> **Ethernet Ports** -> **USB Ethernet Port**に移動し、ポートの役割を**WAN**に設定し、**Apply**をクリックします。

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7は自動的にデバイスに接続します。接続しない場合は、上記の手順を繰り返すか、Web管理パネルにログインしてINTERNETページでUSB Ethernet接続を確認します。
    3. インターネットに正常に接続されると、タッチスクレンの右上にUSBアイコンとEthernetポートアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

## 修復とリセット

物理リセットボタンでネットワーク接続を修復したり、Mudi 7を工場出荷時にリセットしたりできます。

**注意**: リセットを実行する前に、Mudi 7が完全に起動していることを確認してください。電源投入直後にリセットボタンを押さないでください。U-Bootフェイルセーフモードがトリガーされる可能性があります。

カバーを外すと、以下のリセットボタンが表示されます。

![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

!!! note "ネットワーク修復"

    リセットボタンを**4秒間**長押ししてから離すと、ネットワークが修復されます。ボタンを長押ししている間は、画面上のプロンプトに注意し、指示に従って操作してください。

    これにより、Wi-Fi設定、VPN設定（無効）、システム設定などは維持されながら、ネットワークインターフェースが再起動します。

    **注意**:

    1. Wi-Fiが無効になっている場合、ソフトリセットによりWi-Fiがデフォルトの有効状態に復元されます。

    2. ソフトリセットは、デバイスを非routerモードからrouterモードに素早く切り替えるためでもあります。

!!! note "デバイスリセット"

    リセットボタンを**10秒間**長押ししてから離すと、ハードリセットが実行されます。ボタンを長押ししている間は、画面上のプロンプト注意し、指示に従って操作してください。
    
    これにより、すべての設定がクリアされます。慎重に行ってください。

---

以下はMudi 7 WebGUI機能の概述です。

## Wireless

Wirelessページでは、6 GHz、5 GHz、2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、TX電力の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSID可視性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

**注意**: Mudi 7のwireless設定には、彼のGL.iNet Wi-Fi 7ルーターとは異なる時がいくつかあります。

1. チップセットのハードウェア制約により、5 GHzと6 GHz Wi-Fiを同時に有効にできません。
2. Repeaterが有効になっている場合、Guest Networkは自動的に無効になります。
3. 規制により、屋外で使用する場合はWi-FiをOutdoorモードに切り替えする必要があります。これにより、カバー範囲が減少する可能性があります。Wirelessページの上部で、使用環境（IndoorまたはOutdoor）を切り替えることができます。

## Clients

Clientsページには、接続されたデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレスとMACアドレス、ダウンロード速度とアップロード速度、合計トラフィックが表示され、クライアントをブロックしたりその彼のアクションを実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}クラウド管理サービスは、GL.iNetルーター者に簡単かつシンプルにリモートアクセスと管理を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarpは、シームレスなリモートネットワークとリモートデバイス管理を提供するために設計された高度なネットワーキングプラットフォームです。GL.iNetルーター者連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位と下位のデバイス制御を可能にします。ネットワーク全体の管理とする来のハードウェアレベル制御のサポートに焦時を当てたAstroWarpは、デバイスの管理と安全で安定したネットワークの維持のためのより堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Mudi 7はOpenVPNとWireGuardをサポートしています。

=== "OpenVPN"
    
    Mudi 7（およびその彼のGL.iNetルーター者）は強力なセキュリティを提供するOpenVPNプロトコルをサポートしています。OpenVPNを設定するには、以下のチュートリアルに従ってください：

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Mudi 7（およびその彼のGL.iNetルーター者）は、高速性と利便性を備えたWireGuardプロトコルをサポートしています。WireGuardを設定するには、以下のチュートリアルに従ってください：

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク

=== "Multi-WAN"

    Multi-WANは、ルーターに複数のインターネット接続（ethernet、repeater、tethering、cellular、USB ethernetなど）を同時に設定できるネットワーキング機能です。現にのインターネット接続が失敗すると、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れないインターネットアクセスが確保されます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、から宅やオフィスなど、限られたに理の領域内でコンピュータとデバイスを接続するネットワークです。高速データ転送とリソース共有を可能にし、デバイスが効率のに相互通信できます。
    
    LANの設定については、[Lan](../../interface_guide/lan.md)を参照してください。

=== "Guest Network"

    IPv4プライベートアドレス範囲192.168.0.0/16、172.16.0.0/12、または10.0.0.0/8内でサブネットを設定し、ゲートウェイとネットマスクIPアドレスを指定し、ゲストネットワークのAP分離などのセキュリティ設定を構成できます。

    ゲストネットワークの設定については、[Guest Network](../../interface_guide/guest_network.md)を参照してください。

---

=== "DNS"

    DNSページでは、カスタムDNSサーバーを設定し、DNSリバインディング攻撃保護を有効にしてすべてのクライアントのDNS設定を上書きし、カスタムDNSがVPN DNSを上書きできるようにし、Ethernet接続からDNSサーバーを自動的に指定するか手動で指定するモードを構成できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "Ethernet Port"

    Ethernet Portページでは、Ethernetポートの役割（WAN/LANとして使用）の設定、WANインターフェースのMACモードとMACアドレスの切り替え、ネゴシエーション済みポート速度の表示を行うことができます。

    Mudi 7には単一のEthernetポートが備わっており、デフォルトでLANです。必要に応じて、タッチスクリーンまたはWeb管理パネルでWANポートに切り替えできます。

    Ethernetポートの管理については、[Port Management](../../interface_guide/ethernet_port.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4を置き換えるために設計されたインターネットプロトコルの最も新バージョンです。ほぼ無限の数の固有のIPアドレスを可能にする大幅なアドレス空間を提供し、インターネットに接続するデバイスの増加に対応するために不可欠です。
    
    IPV6の設定については、[IPV6](../../interface_guide/network_mode.md)を参照してください。

---

=== "IGMP Snooping"

    IGMPスヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。
    
    IGMPスヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークに接続し、彼のデバイスと通信する方法を決定する構成を指します。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

    **注意**: Mudi 7はRouter、Access Point、Extenderモードをサポートします。WDSモードはサポートされていません。

=== "Drop-in gateway"

    ドロップインゲートウェイは、AdGuard Home、暗号化DNS、VPNクライアントを含むメインルーター者の機能を拡張します。
    
    ドロップインゲートウェイの設定については、以下のリンクを参照してください：
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU負荷を削減し、トラフィックパケットの転送を高速化できます。
    
    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御

=== "Parental Control"

    Parental Controlは、子どものデバイスを管理および制御するために設計されています。スクリーン時間の制限や特定コンテンツへのアクセス制限が含まれます。

    保護者による制御の設定については、[Parental Control](../../interface_guide/parental_control.md)を参照してください。

## セキュリティ

=== "Port Forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Management Control"

    Management Controlでは、ネットワークとルーター者を不正アクセスから保護するためのさまざまなセキュリティ設定を構成できます。このページには以下のオプションがあります：

    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーター者のインターフェースへのアクセスを管理および制限します。
    * リモートアクセス制御：インターネット上のリモート場所からルーター者のインターフェースへのアクセスを構成および制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    これらの設定は、ネットワーク環境を安全に保ち、ルーター者と接続されたデバイスを保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション

=== "Plug-ins"

    プラグインは、既存のコンピュータプログラムに特定の機能または機能を追加するソフトウェアコンポーネントであり、カスタマイズと機能拡張を可能にします。
    
    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。リモートネットワークにアクセスするために静のIPアドレスが必要なユーザーに最もも便利です。
    
    Dynamic DNSの設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージとは、複数のユーザーとデバイスがネットワーク上でファイルにアクセスして共有できる集中型データストレージソリューションを指します。
    
    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Homeは、ネットワーク全体の広告およびトラッカーブロッキングソリューションであり、家庭内ネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングするDNSサーバーとして機能します。
    
    AdGuard Homeの設定については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "ZeroTier"

    ZeroTierは、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全に仮想ネットワークを作成し、デバイス same 一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサーシピスです。
    
    Tailscaleの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "Tor"

    Tor（The Onion Routerのやや称）は、匿名通信を可能にするプライバシー重視のネットワークです。ユーザーの位置情報と使用状況を不明瞭にするために、一連のボランティアが運用するサーバー（ノード）を介してインターネットトラフィックをルーティングします。
    
    * [Torの設定方法](../../interface_guide/tor.md)

## システム

=== "Overview"

    Overviewページは、ルーターの現にのパフォーマンス指標とステータスの含まれるのなスナップショットを提供します。このページでは以下を表示できます：

    * CPU平均負荷：ルーター者のCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーター者のメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーター者のLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーター者のフラッシュストレージの使用率を確認し、ファームウェアと設定データのための非常にな空間を確保します。
    * デバイス情報：ルーター者のシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーター者に接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーター者の操作を効果のに管理および監視するのに役立つ重要な洞察とコントロールを提供します。

    詳細な設定手順と詳細については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーター者の管理インターフェースのパスワードを設定または変更でき、許可されたユーザーのみが設定を変更できるようにします。

    セキュリティ上の理よりから、**Prevent Weak Password**をオンにすることをお勧めします。

    **Prevent Weak Password**をオンにすると、新しいパスワードの要件は以下の通りです：

    * 5文字で上63文字以下。
    * 文字（大文字小文字を区別）、数字、記号`` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``が許可されています。
    * 大文字、小文字、数字、記号のうち2種類で上が必要です。

=== "Upgrade"

    Upgradeページは、ルーター者のファームウェアを最も新バージョンにアップデートするために使用され、パフォーマンス、セキュリティ、新機能の向上を確保します。このページには2つのアップグレードオプションがあります：

    * ファームウェアオンラインアップグレード：製造元のサーバーから最も新バージョンを自動的に確認してインストールし、アップデートプロセスを簡素化します。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーター者をアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最も新の改善と修正でルーター者を最も新の状態に保つことができます。

    詳細な設定手順と詳細については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasksページでは、ルーター者を指定した間隔で自動的に再起動するように設定でき、最も適なパフォーマンスと安定性の維持に役立ちます。

    詳細な設定手順と詳細については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

    **注意**: Mudi 7はLED表示スケジュールとWi-Fiステータススケジュールをサポートしていません。

=== "Display Management"

    Display Managementページでは、タッチスクリーン表示とその関連設定を管理できます。
    
    - 壁紙：壁紙とウェイク表示スタイルをカスタマイズします。
    - 明るさ：タッチスクリーンの明るさを調全体します。スライダーを使用するか、特定のレベル（1〜10の範囲）を入力して、さまざまな照明条件に合わせます。
    - パーソナル署名：タッチスクリーンにカスタムテキストを追加して、独からのスタイルを表示したり簡単な識別を可能にします。
    - から動ロック：アクティビティがない場合にスクリーンが自動的にロックされるまでの遅延時間を設定します。範囲は15秒から5分です。
    - パスコード：セキュリティのレイヤーを追加するために、タッチスクリーンにパスコードを設定します。

    詳細な設定手順と詳細については、[Display Management](../../interface_guide/display_management.md)を参照してください。

=== "USB & Power"

    USB & Powerページでは、ルーター者のUSB機能と電源関連設定含まれるのな管理を提供します。
    
    **USB**

    - USBプロトコル切替：USBポートのUSB 2.0とUSB 3.1プロトコルを切り替えます。
    - デュアルロールUSBモード：ドロップダウンメニューからUSB動作モードを選択します。DeviceまたはHostに設定できます。
    - 電力方へ：ドロップダウンメニューからUSBポートの電力優先度を設定します。Input PriorityまたはOutput Priorityに設定できます。
    - 電力しきい値：USBポートの特定の電力しきい値パーセンテージを設定します。
    
    **Power**
    
    - Wi-Fiアイドルタイムアウト：Wi-Fiがスタンバイに入るまでのアイドル時間を設定します（10分から2時間の範囲、またはNever）。
    - Ethernetアイドルタイムアウト：Ethernetがスタンバイに切り替えられるまでのアイドル時間を設定します（10分から2時間の範囲、またはNever）。
    - 電源オフタイムアウト：アイドル時にルーター者が自動的に電源オフになるまでの遅延時間を設定します（1時間から12時間の範囲、またはNever）。
    - chargerでの電源オン：chargerに接続したときにルーター者が自動的に電源オンになるを有効/無効にする切り替え。
    - から動スタンバイ：省電力のためのから動システムスタンバイを有効/無効にする切り替え。

---

=== "Time Zone"

    Time Zoneページでは、ルーター者の正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現に時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な設定手順と詳細については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Reset Firmware"

    Reset Firmwareページでは、ルーター者の現にのファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。このプロセスは、現にインストールされているファームウェアバージョンのデフォルト設定にルーターを復元します。持続のな問題のトラブルシューティングや現にのファームウェアのデフォルト設定で新鮮に開始するのに便利です。

    詳細な設定手順と詳細については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Logページは、ルーター者のアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーター者に統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーター者で使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはExport Logボタンがあり、収集したすべてのログをエクスポートして技術サポートの分析にできます。この機能は、複雑な問題の診断と専門のサポートの取なければならないに非常に便利です。

    詳細な設定手順と詳細については、[Log](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settingsページは、OpenWrt LuCIインターフェースを通じて高度な構成オプションへのアクセスを提供し、経験豊富なユーザーが基本インターフェースオプションを超えてルーターの設定と機能を微調全体できます。これには、詳細なネットワーク設定、ファイアウォール設定、その彼の高度なシステムカスタマイズが含まれます。

    詳細な設定手順と詳細については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
