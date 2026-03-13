# Spitz Plus (GL-X2000) ユーザーガイド

## 製品概要

Spitz Plus (GL-X2000) は、特に偏远に区やロードトリップで高速で信頼性の高い接続を提供するように設計された dual-SIM 4G LTE Wi-Fi 6 cellular gatewayです。3-Carrier Aggregation機できるを搭载し、ルーターは3つのキャリアバンドで same 時にデータをストリーミングし、3倍の利用可できる帯域幅を提供して輻輳を回避します。4つのインターネットアクセス方法（Cellular（SIMカード）、Ethernet、Repeater、Tethering）をサポートしています。Multi-WAN（フェイルオーバーとロードバランシング）、VPN（OpenVPNとWireguard）、保護者へけコントロール、AdGuard Home、ポート転送、Tailscaleなどをサポートします。

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## パッケージコンテンツ

パッケージ内のアダプターは発送国によって異なることに注意してください。

パッケージにはで下が含まれます：

- 1 x Spitz Plus (GL-X2000)
- 1 x ユーザーマニュアル
- 4 x 外部 antenna
- 1 x サンキューカード
- 1 x Ethernetケーブル
- 1 x 壁掛けキット
- 1 x 続いてパッド
- 4 x ねじ
- 1 x 电源アダプター
- 1 x コンバーター（発送国に基づいて）

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_unboxing.jpg){class="glboxshadow"}

## LEDインジケーター

| 状態 | 電源 | インターネット | 2.4GHz | 5GHz | Cellular |
| ----------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | ------- |
| 正常（インターネットに接続） | 緑 | 緑 | 緑 | 緑 | 緑 |
| インターネットに未接続 | 緑 | オフ | 緑 | 緑 | 緑 |
| ファームウェアアップデート中 | 緑 | 緑色時滅（0.5秒ごと） | 緑色時滅（0.5秒ごと） | 緑色時滅（0.5秒ごと） | 緑 |
| ルーターリセット中（リセットボタンを3秒で上押す） | 緑色時滅（1秒ごと） | 緑 | 緑 | 緑 | 緑 |
| ルーターを工場出荷時に復元（リセットボタンを10秒押す） | 高速緑色時滅（0.25秒ごと） | 緑 | 緑 | 緑 | 緑 |

## 仕様

[仕様](https://www.gl-inet.com/products/gl-x2000/#specs){target="_blank"}を参照してください。

## Spitz Plusの設定方法

Spitz Plusを設定するには、4つのサポートされているインターネット接続方法（Cellular（SIMが必要）、Ethernet、Repeater、Tethering）のいずれかを使用します。で下の設定動画を見るか、手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>（この動画ではSpitz PlusのCellular設定を示しています。彼のインターネット接続方法でSpitz Plusを設定する必要がある場合は、で下の手順を参照してください。）</small>

!!! note "開始する前に、で下の手順に従ってください（セルラー方式で接続する場合）："

    セルラー方式でインターネットに接続するには、少なくとも1枚のnano SIMカードが必要です。nano SIMカード 用意されている場合は、で下の手順に従ってください：
    
    1. SIMカードキャリアによって必要な場合はSIMカードを 有効化します.
    2. ルーターの電源をオフにします。
    3. SIMカードをSIMカードスロットに挿入します。（**注意：** 一度にアクティブなSIMカードは1枚のみです。もう1枚のSIMカード機できるはバックアップとしてのみ機できるします。）

### 1. Spitz Plusの電源を入れる

2つの電源アダプターを組み合わせます。ルーターに接続してコンセントに差し込みます。から動のに起動します。

### 2. Spitz Plusに接続

Wi-FiまたはEthernetを使用して、デバイス（コンピュータ、ラップトップ、スマートフォンなど）をルーターに接続します。

- Ethernet

    Ethernetケーブルを使用してデバイスをルーターLANポートに接続します。

- Wi-Fi

    デバイスでSettings -> WLANに移動し、利用可できるなネットワークリストでルーターWi-Fiネットワーク名を見つけ、パスワードを入力します。（デフォルトのネットワーク名とパスワードはルーターラベルに印刷されています。）

    デバイスで利用可できるなネットワークリストでルーターWi-Fiネットワーク名を見つけ、パスワードを入力してネットワークに参加します。デフォルトのネットワーク名とパスワードはルーターラベルに印刷されています。

### 3. WebGUIにログイン

Webブラウザを起動し、アドレスバーに`192.168.8.1`を入力すると、GL.iNet Web管理パネルに入ります。言語を選択して管理者パスワードを設定し、**Apply**をクリックします。

### 4. Spitz Plusをインターネットに接続

**注意：** で下の説明は、GL.iNet Web管理パネルを通じてルーターを設定するユーザーに適用されます。GL.iNetアプリより喜欢場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}して画面上の説明に従ってください。

サポートされているインターネット接続方法（Cellular、Ethernet、Repeater、Tethering）のいずれかを使用してSpitz Plusを設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機できるを使用する場合は、複数のインターネット接続を設定してください。

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    SIMカードをルーターに挿入している場合は、インターネットにから動のに接続されるはずです。SIMキャリアの名前とCellularセクションに緑色のドットが表示されます。
    
    そうでない場合は、ルーターの電源を切り、SIMカードを再挿入して電源を入れ直してください。
    
    詳細な手順については、[セルラーでインターネットに接続](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models)を参照してください。

    **注意**：Spitz PlusのeSIM機できるはファームウェアv4.7で上で利用可できるです。GL.iNetルーターでeSIM物理カードを使用する方法については[これ里](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)を参照してください

    問題が発生した場合は、[セルラーネットワークトラブルシューティングガイド](../../faq/cellular_network_troubleshooting_guide.md)を参照してください。

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}
    
    Spitz PlusのWANポートをEthernetケーブル経よりで上位デバイス（モデムなど）に接続します。
    
    インターネットに正常に 接続されると、INTERNETページのEthernetセクションに緑色のドットが表示されます。

    詳細な手順については、[Ethernetケーブルでインターネットに接続](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. 管理パネルのINTERNETページで、Repeaterセクションを見つけて**Connect**をクリックします。
    2. 利用可できるなネットワークからWi-Fiネットワークを選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    
    インターネットに正常に 接続されると、INTERNETページのRepeaterセクションに緑色のドットが表示されます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンまたはUSB dongle）をUSBケーブルでルーターUSBポートに接続します。
    2. モバイルデバイスでSettingsに移動し、USB Tetheringを有効にします。
    3. Web管理パネルのINTERNET画面のTetheringセクションで**Connect**をクリックします。
    
    インターネットに正常に 接続されると、INTERNETページのTetheringセクションに緑色のドットが表示されます。

    詳細な手順については、[USBテザリングでインターネットに接続](../../interface_guide/internet_tethering.md)を参照してください。

---

で下は、Spitz Plus WebGUI機できるの概要です。

## Wi-Fi

Wirelessページでは、5 GHzと2.4 GHz Wi-Fiネットワークの両方の設定を設定できます。Wi-Fiの有効化/無効化、TX功率の設定、Wi-Fi名（SSID）の指定、BSSIDの无線化の有効化、Wi-Fiセキュリティモードの選択、Wi-Fiパスワードの設定、SSID可视性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## クライアント

Clientsページでは、接続されたデバイスについての情报を表示します。各クライアントごとに、デバイス名、接続タイプ（EthernetまたはWi-Fi経より）、IPとMACアドレス、ダウンロードとアップロード速度、合計トラフィックが表示され、IPの予約、クライアントのブロックやその彼のアクションを実行できます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}は、GL.iNetルーターにリモートでアクセスして管理する簡単でシンプルな方法を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarpは、シームレスなリモートネットワーキングとリモート機器管理を提供するように設計された高度なネットワーキングプラットフォームです。GL.iNetルーター統合专门に構築され、ネットワーク全体の含まれるのなデバイス管理をサポートし、上位と下位のデバイス制御の両方を可できるにします。ネットワーク全体の管理とする来のハードウェアレベル制御のサポートに焦時を当てたAstroWarpは、デバイスを管理し、安全で安定したネットワークを維持するためのより堅牢で信頼できるソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

    **注意**：AstroWarpを使用するには、Spitz Plusをファームウェアv4.8で上にアップグレードしてください。

## VPN

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。プライバシーとセキュリティのレイヤーを追加し（VPNクライアント）、リモートネットワークへのアクセスを可できるにします（VPNサーバー）。Spitz PlusはOpenVPNとWireGuardをサポートしています。

=== "OpenVPN" 
    
    Spitz Plus（および彼のGL.iNetルーター）は、強度なセキュリティを提供するOpenVPNプロトコルをサポートしています。OpenVPNを設定するには、で下のチュートリアルに従ってください：

    * [OpenVPNクライアントの設定方法](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [OpenVPNサーバーの設定方法](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"
    
    Spitz Plus（および彼のGL.iNetルーター）は、高速性と利便性を提供するWireGuardプロトコルをサポートしています。WireGuardを設定するには、で下のチュートリアルに従ってください：

    * [WireGuardクライアントの設定方法](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [WireGuardサーバーの設定方法](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

## アプリケーション

=== "プラグイン"

    プラグインは、特定の機できるまたは機できるを既存のコンピュータプログラムに追加し、カスタマイズと機できるのへ上を可できるにするソフトウェアコンポーネントです。
    
    プラグインの設定については、[プラグイン](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連するIPアドレスをリアルタイムでから動のに検出してアップデートします。リモートネットワークにアクセスするために静のIPアドレスが必要なユーザーに便利です。
    
    Dynamic DNSの設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "ネットワークストレージ"

    ネットワークストレージは、複数のユーザーとデバイスがネットワーク上でファイルにアクセスして共有できる集中型データストレージソリューションを指します。
    
    ネットワークストレージの設定については、[ネットワークストレージ](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Homeは、広告をブロックして追跡をブロックし安全に保つサードパーティツールです。AdGuard Homeを有効にする方法については、[AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/)を参照してください。

=== "保護者へけコントロール"

    保護者へけコントロールは、子供のデバイスを管理·制御するために設計された一组の設定です。スクリーンタイムの制限と特定コンテンツへのアクセス制限が含まれます。Spitz Plusは、GL.iNetが開発したローカルバージョンと、Bark（保護者へけコントロールアプリ）の統合バージョンの2つの保護者へけコントロールオプションを提供します。
    
    保護者へけコントロールの設定については、[保護者へけコントロール](../../interface_guide/parental_control.md)を参照してください。

=== "Tailscale"

    Spitz Plusはファームウェアv4.7で上でTailscaleをサポートします。
    
    Tailscaleは、どこでもデバイスとアプリケーションにアクセスできるVPNサービです。
    
    Tailscaleの設定については、[Tailscale](../../interface_guide/parental_control.md)を参照してください。

=== "eSIM"

    Spitz Plusはファームウェアv4.7で上でeSIM機できるをサポートします。
    
    デバイスでeSIMを設定して管理する方法については、[このチュートリアル](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)を参照してください。

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## ネットワーク

=== "ポート転送"

    ポート転送により、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。ポート転送の設定については、[ポート転送](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards)を参照してください。

=== "Multi-WAN"

    Multi-WANは、ルーターを same 時に複数のインターネット接続（セルラー、Repeater、Ethernetなど）で設定できるネットワーク機できるです。現にのインターネット接続が失敗した場合、ルーターはから動のに別のインターネット接続に切り替えします。これにより、滑らかで途切れないインターネットアクセスが確保されます。
    
    Multi-WANの設定については、[Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/)を参照してください。

=== "LAN"

    LAN、またはLocal Area Networkは、から宅やオフィスなどの限られたに理の領域内でコンピュータとデバイスを接続するネットワークです。高速データ転送とリソース共有を可できるにし、デバイスが効率のに互いに通信できます。
    
    LANの設定については、[LANチュートリアル](../../interface_guide/lan.md)を参照してください。

---

=== "ゲストネットワーク"

    IPv4プライベートアドレス範囲192.168.0.0/16、172.16.0.0/10、または8.0.0.0/8内でサブネットを設定し、ゲートウェイとネットマスクIPアドレスを指定し、ゲストネットワークのAP分離などのセキュリティ設定を設定できます。
    
    LANの設定については、[LANチュートリアル](../../interface_guide/guest_network.md)を参照してください。

=== "DNS"

    DNSページでは、カスタムDNSサーバーを設定し、DNS再バインディング攻撃Protectionを有効化し、すべてのクライアントのDNS設定をオーバーライドし、カスタムDNSがVPN DNSをオーバーライドすることを許可し、DNSサーバー設定モードをから動またはEthernet接続から手動でDNSサーバーを指定するように設定できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "ポート管理"

    ポート管理ページでは、WANとLANポートを設定し、WAN/LANインターフェースをEthernetに設定し、WANインターフェースのMACモードとMACアドレスを指定し、ネットワークポート速率をネゴシエートできます。

    Ethernetポートの管理については、[ポート管理](../../interface_guide/network_port_management.md)を参照してください。

---

=== "ネットワークモード"

    ネットワークモードは、デバイスがネットワークに接続し、彼のデバイスと通信する方法を决定する構成設定を指します。
    
    ネットワークモードの設定については、[ネットワークモード](../../interface_guide/network_mode.md)を参照してください。

=== "IPv6"

    IPv6、またはInternet Protocol version 6は、IPv4を置き換えるために設計されたインターネットプロトコルの最も新バージョンです。非常にに大きなアドレス空間を提供し事実上無制限の数の固有のIPアドレスを可できるにし、インターネットに接続されるデバイスの数が増えているするために不可欠です。
    
    IPV6の設定については、[IPV6](../../interface_guide/network_mode.md)を参照してください。

=== "Drop-in Gateway"

    Drop-in Gatewayは、AdGuard Home、暗号化されたDNS、VPNなど、メインルーターにことのない機できるを拡張します。Drop-in Gatewayの設定については、[Drop-in Gatewayの設定方法](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/)を参照してください。

---

=== "IGMP Snooping"

    IGMP snoopingは、Ethernetスイッチで使用され、マルチキャストトラフィックを管理·制御するネットワーク最も適化テクニックです。
    
    IGMP snoopingの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "ネットワークアクセラレーション"

    ハードウェアアクセラレーションは、汎用CPUよりも特定のタスクをより効率的に実行するために専用のハードウェアコンポーネントを使用することを指します。
    
    ネットワークアクセラレーションの設定については、[ネットワークアクセラレーション](../../interface_guide/network_acceleration.md)チュートリアルを参照してください。

=== "NAT設定"

    NAT設定ページでは、Full Cone NATとSIP ALG（Application Layer Gateway）機できるの有効化/無効化できます。

    NAT設定については、[NAT設定](../../interface_guide/nat_settings.md)を参照してください。

## システム

=== "概要"

    概要ページでは、ルーター現にのパフォーマンス·使用状況の含まれるのなスナップショットを提供します。このページでは、次のことを表示できます：

    * CPU平均負荷：ルーターCPUの平均負荷を監視し、パフォーマンスの评估と潜にのなボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターメモリの使用量をチェックし、リソースの管理を支援します。
    * LEDコントロール：ルーターLEDライトのオン·オフを切り替え、デバイスの视觉インジケーターのカスタマイズを可できるにします。
    * フラッシュ使用量：ルーターフラッシュストレージの使用状況を表示し、ファームウェアと設定データのために非常にになスペースがあることを確認します。
    * デバイス情報：ルーターシステムの详细情報にアクセスし、稼働時間、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/Nが含まれます。
    * 外部ストレージ：USBドライブやTFカードなど、ルーターに接続された外部ストレージデバイスの状態を確認できます。
    
    これらの機できるは、本质のな洞察とコントロールを提供し、ルーターの动作を効果のに管理·監視するのを支援します。

    詳細な設定手順については、[概要](../../interface_guide/system_overview.md){target="_blank"}を参照してください。

=== "アップグレード"

    アップグレードページはルーターファームウェアを最も新バージョンにアップデートするために使用され、強化されたパフォーマンス、セキュリティ、新機できる，确保します。このページでは、アップグレードオプションが3つ提供されています：

    * ファームウェアオンラインアップグレード：メーカサーバーから直接最も新 firmwareバージョンをから動のにチェックしてインストールし、アップデートプロセスをシンプル化します。
    * ファームウェアローカルアップグレード：コンピュータからfirmwareファイルを手動でアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。
    * モジュールオンラインアップグレード：メーカサーバーから直接最も新4G/5Gモジュールバージョンをから動のにチェックしてインストールし、アップデートプロセスをシンプル化します。
    * モジュールローカルアップグレード：コンピュータからモジュールファイルを手動でアップロードして4G/5Gモジュールをアップデートします。

    これらのオプションにより、ルーターを最も新の改善と修正で最も新の状態に保つことができます。

    詳細な手順については、[アップグレード](../../interface_guide/upgrade.md){target="_blank"}を参照してください。

=== "スケジュールタスク"

    スケジュールタスクページでは、事前に定义されたスケジュールに基づいて各种ルーター機できるをから動化し、利便性と効率を高めます。このページの主な機できるは次のとおりです：

    * LEDディスプレイスケジュール：ルーターLEDライトをから動のにオン·オフにするスケジュールを設定し、特定時間帯の光害を減少します。
    * スケジュール再起動：ルーターを指定间隔でから動のに再起動するように设定し、最も適なパフォーマンスと安定性の维持に役立ちます。
    * Wi-Fiステータussケジュール：5GHz / 2.4GHz Wi-Fiバンドを制御するスケジュールを設定し、ネットワークの可用性と消費電力の管理を可できるにします。
    
    これらのスケジュールオプションにより、ルーター动作に対するより大のなコントロールが确保され、特定のニーズと好みに合わせることができます。

    詳細な手順については、[スケジュールタスク](../../interface_guide/scheduled_tasks.md){target="_blank"}を参照してください。

---

=== "タイムゾーン"

    タイムゾーンページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現に時間に基づいて正確にタイムスタンプ付けられます。この設定は、正確なレコードのメンテナンスと、時間ベースの構成の適切な実行に重要です。

    詳細な手順については、[タイムゾーン](../../interface_guide/time_zone.md){target="_blank"}を参照してください。

=== "ログ"

    ログページでは、ルーターアクティビティとイベントを記録した各种ログにアクセスでき、トラブルシューティングとパフォーマンス監視に役立ちます。このページにはで下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーのレコード。重大な問題の診断に役立ちます。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合はNginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはすべての收集したログをエクスポートして技術サポート分析できるようにするログのエクスポートボタンがあります。この機できるは、複雑な問題を诊断し、プロフェッショナルな支援をなければならないるために非常にに価値があります。

    詳細な手順については、[ログ](../../interface_guide/log.md){target="_blank"}を参照してください。

=== "セキュリティ"

    セキュリティページでは、ネットワークとルーターを不正アクセスから保护するための各种セキュリティ設定を設定できます。このページにはで下のオプションが含まれます：

    * 管理者パスワード：ルーター管理インターフェースのパスワードを設定または変よりし、認可されたユーザーのみが設定を変よりできるようにします。
    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからのルーターインターフェースへのアクセスを管理·制限します。
    * リモートアクセス制御：外部の脅威に対するセキュリティを強化するために、インターネット経よりでリモート locationsからのルーターインターフェースへのアクセスを設定·制限します。
    * ルーターで開いているポート：ルーターで開いているポートを制御し、潜にのな脆弱性と不正アクセスを制限します。

    これらの設定は、安全なネットワーク環境をメンテナンスし、ルーターと接続されたデバイスを保护するのを支援します。

    詳細な手順については、[セキュリティ](../../interface_guide/security.md)を参照してください。

---

=== "ファームウェアリセット"

    ファームウェアリセットページでは、ルーター現にのファームウェアバージョンをデフォルト設定にリセットでき、すべてのカスタム設定が消去されます。このプロセスは、ルーターをインストールされているファームウェアバージョンのデフォルト設定に戻します。持続のな問題のトラブルシューティングまたは現にのファームウェアのデフォルト設定でやり直す場合に便利です。

    詳細な手順については、[ファームウェアリセット](../../interface_guide/reset_firmware.md){target="_blank"}を参照してください。

=== "高度設定"

    高度設定ページでは、OpenWrt LuCIインターフェースを通じて高度な設定オプションにアクセスでき、経験豊富なユーザーが基本のなインターフェースオプションを超えてルーター設定と機できるを微調全体できます。これには、詳細なネットワーク設定、ファイアウォール設定、その彼の高度なシステムカスタマイズが含まれます。

    詳細な設定手順と详细情報については、[高度設定](../../interface_guide/advanced_settings.md){target="_blank"}を参照してください。
