# Opal (GL-SFT1200) ユーザーガイド

## 製品概要

Opal (GL-SFT1200) は、1200Mbps のワイヤレス転送速度に対応したポケットサイズのトラベルルーターです。持ち運びやすいコンパクト設計で、小規模ビジネス、小規模アパート、出張者のワイヤレスインターネットアクセス需要に対応できます。

![gl-sft1200 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/first_time_setup/gl-sft1200.jpg){class="glboxshadow"}

## パッケージ内容

- 1 x Opal (GL-SFT1200)
- 1 x ユーザーマニュアル
- 1 x イーサネットケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター
- 1 x 変換プラグ (配送先の国に基づく)

![gl-sft1200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/first_time_setup/sft1200_unboxing.jpg){class="glboxshadow"}

## Opal のセットアップ方法

このセットアップ動画を見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(この動画では別の GL.iNet ルーターを使ってセットアップを説明していますが、Opal および他のルーターモデルでも手順は同じです。)</small>

### 1. 電源を入れる

2 ピース構成の電源アダプターを組み合わせます。ルーターに接続し、コンセントに差し込みます。ルーターは自動的に起動します。

### 2. デバイスを接続する

Wi-Fi または Ethernet を使用して、コンピューター、ノート PC、スマートフォンなどのデバイスをルーターに接続します。

- Ethernet

    イーサネットケーブルを使用して、デバイスをルーターの LAN ポートに接続します。

- Wi-Fi

    デバイスで Settings -> WLAN に移動し、利用可能なネットワーク一覧からルーターの Wi-Fi ネットワーク名を見つけて、パスワードを入力します。デフォルトのネットワーク名とパスワードは、ルーター底面のラベルに印刷されています。

### 3. Web 管理パネルにログインする

Web ブラウザーを開き、アドレスバーに `192.168.8.1` と入力してログインします。言語を選択し、管理者パスワードを設定して、**Apply** をクリックします。

Wi-Fi 情報を変更した場合は、更新後の認証情報を使用してデバイスをルーターの Wi-Fi に再接続する必要があります。

### 4. インターネット設定

**Note:** 以下の手順は、GL.iNet Web Admin Panel でルーターを設定するユーザー向けです。GL.iNet アプリを使用したい場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"} し、画面の指示に従ってください。

Opal は、Ethernet、Repeater、Tethering、Cellular のいずれかの対応インターネット接続方式で設定できます。[Multi-WAN](../../interface_guide/multi-wan.md) 機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_ethernet.png){class="glboxshadow"}

    ルーターの WAN ポートと、モデムなどの上位機器の間をイーサネットケーブルで接続します。

    インターネットへの接続に成功すると、INTERNET ページの Ethernet セクションに緑色の点が表示されます。

    詳細な手順については、[イーサネットケーブル経由でインターネットに接続する](../../interface_guide/internet_ethernet.md) を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_repeater.png){class="glboxshadow"}

    1. Web Admin Panel の INTERNET ページで Repeater セクションを見つけ、**Connect** をクリックします。
    2. 利用可能なネットワークから Wi-Fi ネットワークを選択します。
    3. パスワードを入力し、**Apply** をクリックします。

    インターネットへの接続に成功すると、INTERNET ページの Repeater セクションに緑色の点が表示されます。

    詳細な手順については、[既存の Wi-Fi ネットワーク経由でインターネットに接続する](../../interface_guide/internet_repeater.md) を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_tethering.png){class="glboxshadow"}

    1. スマートフォンや USB ドングルなどのモバイルデバイスを、USB ケーブルでルーターの USB ポートに接続します。
    2. モバイルデバイスで Settings に移動し、USB Tethering を有効にします。
    3. Web Admin Panel の INTERNET ページで、Tethering セクションの **Connect** をクリックします。

    インターネットへの接続に成功すると、INTERNET ページの Tethering セクションに緑色の点が表示されます。

    詳細な手順については、[USB テザリング経由でインターネットに接続する](../../interface_guide/internet_tethering.md) を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_cellular.png){class="glboxshadow"}

    セルラー USB モデムをルーターの USB ポートに接続します。これは、USB モデムのインターネット接続をすべての接続デバイスで共有する場合に便利です。

    インターネットへの接続に成功すると、INTERNET ページの Cellular セクションに緑色の点が表示されます。

    詳細な手順については、[Cellular 経由でインターネットに接続する](../../interface_guide/internet_cellular.md) を参照してください。

## VPN の設定方法

VPN (virtual private network) は、デバイスと VPN サーバー間に安全で暗号化された通信を作成します。プライバシーとセキュリティを強化し (VPN client)、リモートネットワークへアクセスできるようにします (VPN server)。Opal は OpenVPN、WireGuard、Tor* に対応しています。

=== "OpenVPN"

    Opal およびその他の GL.iNet ルーターは、強力なセキュリティを提供する OpenVPN プロトコルに対応しています。OpenVPN を設定するには、以下のチュートリアルに従ってください。

    * [OpenVPN クライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPN サーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Opal およびその他の GL.iNet ルーターは、高速で便利な WireGuard プロトコルに対応しています。WireGuard を設定するには、以下のチュートリアルに従ってください。

    * [WireGuard クライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuard サーバーの設定方法](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor は The Onion Router の略で、インターネット上で匿名通信を可能にするプライバシー重視のネットワークです。インターネットトラフィックをボランティア運営の複数のサーバー (ノード) 経由でルーティングし、ユーザーの場所や利用状況を分かりにくくすることで、オンライン活動の追跡を困難にします。

    **Note:** Opal は Tor をネイティブにはサポートしていませんが、プラグインを通じて手動で Tor をインストールできます。詳細は [こちら](../../interface_guide/tor.md#manual-install) をクリックしてください。

## Wireless and clients

=== "Wireless"

    Wireless ページでは、Wi-Fi の有効化、TX power、Wi-Fi 名 (SSID)、randomized BSSID、Wi-Fi security mode と password、SSID visibility、Wi-Fi mode、bandwidth、channel など、5 GHz および 2.4 GHz Wi-Fi ネットワークの設定を構成できます。

    Wireless を設定するには、[Wireless](../../interface_guide/wireless.md) を参照してください。

=== "Clients"

    Clients ページには、接続されているデバイスの情報が表示されます。各クライアントについて、名前、IP アドレス、MAC アドレス、ダウンロード/アップロード速度、総トラフィックを確認でき、クライアントのブロックやその他の操作も実行できます。

    Clients を設定するには、[Clients](../../interface_guide/clients.md) を参照してください。

## Cloud services

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} サービスは、GL.iNet ルーターへリモートアクセスし管理するための簡単な方法を提供します。

    GoodCloud を設定するには、[GoodCloud](../../interface_guide/cloud.md) を参照してください。

=== "AstroWarp"

    AstroWarp は、シームレスなリモートネットワーキングとリモートデバイス管理を提供する高度なネットワークプラットフォームです。GL.iNet ルーター連携向けに構築されており、ネットワーク全体にわたる包括的なデバイス管理をサポートし、上位および下位デバイスの制御を可能にします。ネットワーク全体の管理と将来的なハードウェアレベル制御のサポートに重点を置くことで、AstroWarp はデバイス管理と安全で安定したネットワーク維持のための、より堅牢で信頼性の高いソリューションを提供します。

    AstroWarp を設定するには、[AstroWarp](../../interface_guide/astrowarp.md) を参照してください。

    **Note:** この機能を使用する前に、ルーターのファームウェアをバージョン 1.7 以上にアップグレードしてください。

## Applications

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。

    Plug-ins を設定するには、[Plug-ins](../../interface_guide/plugins.md) を参照してください。

=== "Dynamic DNS"

    Dynamic DNS (DDNS) は、ドメインに関連付けられた IP アドレスをリアルタイムで自動検出し更新します。リモートネットワークへアクセスするために固定 IP アドレスが必要なユーザーに特に便利です。

    Dynamic DNS を設定するには、[Dynamic DNS](../../interface_guide/ddns.md) を参照してください。

=== "Network Storage"

    Network storage は、複数のユーザーやデバイスがネットワーク経由でファイルにアクセスし共有できる集中型データストレージソリューションです。

    Network storage を設定するには、[Network Storage](../../interface_guide/network_storage.md) を参照してください。

    **Note:** この機能を使用する前に、ルーターのファームウェアをバージョン 1.7 以上にアップグレードしてください。

## Network settings

=== "Port Forwarding"

    Port forwarding により、インターネット上のリモートサーバーやデバイスがプライベートネットワーク内のデバイスにアクセスできます。

    Port forwarding を設定するには、[Port Forwarding](../../interface_guide/port_forwarding.md) を参照してください。

=== "Multi-WAN"

    Multi-WAN は、Cellular、Repeater、Ethernet など複数のインターネット接続を同時にルーターへ設定できるネットワーク機能です。現在のインターネット接続が失敗した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、安定した途切れにくいインターネットアクセスを確保できます。

    Multi-WAN を設定するには、[Multi-WAN](../../interface_guide/multi-wan.md) を参照してください。

=== "LAN"

    LAN (Local Area Network) は、家庭やオフィスなど限られた地理的範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できるようにします。

    LAN を設定するには、[Lan](../../interface_guide/lan.md) を参照してください。

---

=== "Guest Network"

    IPv4 プライベートアドレス範囲 192.168.0.0/16、172.16.0.0/12、10.0.0.0/8 内でサブネットを設定し、gateway と netmask IP アドレスを指定し、ゲストネットワークの AP isolation などのセキュリティ設定を構成できます。

    Guest network を設定するには、[Guest Network](../../interface_guide/guest_network.md) を参照してください。

=== "DNS"

    DNS ページでは、カスタム DNS サーバーの設定、DNS rebinding attack protection の有効化、すべてのクライアントの DNS 設定上書き、VPN DNS をカスタム DNS で上書きする設定、Ethernet 接続から DNS サーバー設定モードを自動または手動指定にする設定を構成できます。

    DNS を設定するには、[DNS](../../interface_guide/dns.md) を参照してください。

=== "Port Management"

    Port Management ページは、ファームウェア v4.7 以降で利用できます。

    このページでは、WAN および LAN ポートの構成、WAN/LAN インターフェースの Ethernet への設定、WAN インターフェースの MAC mode と MAC address の指定、ネットワークポートレートのネゴシエーション表示を行えます。

    Ethernet ポートを管理するには、[Port Management](../../interface_guide/ethernet_port.md) を参照してください。

---

=== "Network Mode"

    Network mode は、デバイスがネットワークに接続し、他のデバイスと通信する方法を決定する構成設定です。

    Network mode を設定するには、[Network Mode](../../interface_guide/network_mode.md) を参照してください。

=== "IPv6"

    IPv6 (Internet Protocol version 6) は、IPv4 を置き換えるために設計された最新の Internet Protocol です。非常に大きなアドレス空間を提供し、インターネットに接続されるデバイス数の増加に対応するために不可欠な、実質的に無制限の一意な IP アドレスを利用できます。

    IPV6 を設定するには、[IPV6](../../interface_guide/network_mode.md) を参照してください。

=== "Drop-in Gateway"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN client など、メインルーターの機能を拡張します。

    Drop-in gateway を設定するには、[How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md) を参照してください。

---

=== "IGMP Snooping"

    IGMP snooping は、Ethernet スイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。

    IGMP snooping を設定するには、[IGMP Snooping](../../interface_guide/igmp_snooping.md) を参照してください。

=== "Network Acceleration"

    Network acceleration は CPU 負荷を軽減し、トラフィックパケット転送を高速化できます。

    Network acceleration を設定するには、[Network Acceleration](../../interface_guide/network_acceleration.md) を参照してください。

=== "NAT Settings"

    NAT Settings ページでは、Full Cone NAT と SIP ALG (Application Layer Gateway) 機能を有効または無効にできます。

    NAT settings を設定するには、[NAT Settings](../../interface_guide/nat_settings.md) を参照してください。

## System settings

=== "Overview"

    Overview ページでは、ルーターの現在の状態とパフォーマンス指標を包括的に確認できます。このページでは、以下を確認できます。

    * CPU Average Load: ルーター CPU の平均負荷を監視し、パフォーマンス評価や潜在的なボトルネックの特定に役立ちます。
    * Memory Usage: ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LED Control: ルーターの LED ライトのオン/オフを切り替え、デバイスの表示をカスタマイズできます。
    * Flash Usage: ルーターのフラッシュストレージ使用状況を確認し、ファームウェアや設定データ用の十分な容量があるか確認できます。
    * Device Info: 稼働時間、hostname、model、architecture、OpenWrt version、kernel version、device ID、device MAC、device S/N など、ルーターシステムの詳細情報にアクセスできます。
    * External Storage: USB ドライブや TF カードなど、ルーターに接続された外部ストレージデバイスの状態を確認できます。

    これらの機能は、ルーターの動作を効果的に管理および監視するための重要な情報と制御を提供します。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md) を参照してください。

=== "Upgrade"

    Upgrade ページは、ルーターのファームウェアを最新バージョンへ更新し、パフォーマンス、セキュリティ、新機能を向上させるために使用します。このページには、アップグレードのための 2 つのオプションがあります。

    * Firmware Online Upgrade: メーカーのサーバーから最新ファームウェアバージョンを自動的に確認しインストールすることで、更新プロセスを簡素化します。
    * Firmware Local Upgrade: コンピューターからファームウェアファイルを手動でアップロードしてルーターを更新し、アップグレードバージョンやタイミングを制御できます。

    これらのオプションにより、ルーターを最新の改善や修正が適用された状態に保てます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md) を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前定義したスケジュールに基づいてルーターの各種機能を自動化し、利便性と効率を高められます。このページの主な機能は以下のとおりです。

    * LED Display Schedule: 特定の時間帯にルーターの LED ライトを自動的にオンまたはオフにするスケジュールを設定し、光害を軽減できます。
    * Schedule Reboot: 指定した間隔でルーターを自動再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fi Status Schedule: 5GHz / 2.4GHz Wi-Fi バンドを制御するスケジュールを設定し、ネットワーク利用可能時間と消費電力をより適切に管理できます。

    これらのスケジュールオプションにより、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md) を参照してください。

---

=== "Time Zone"

    Time Zone ページでは、ルーターの正しいタイムゾーンを設定し、すべての scheduled tasks、logs、system events がローカル時刻に基づいて正確にタイムスタンプされるようにします。この設定は、正確な記録の維持と時間ベースの設定を正しく実行するために重要です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md) を参照してください。

=== "Toggle Button Settings"

    Toggle Button Settings ページでは、ルーターの物理トグルボタンを設定し、特定の機能をボタンに割り当てて素早くアクセスおよび制御できます。この機能は一般的な操作や設定への便利なショートカットを提供し、ユーザー体験とルーター管理を簡素化します。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md) を参照してください。

=== "Log"

    Log ページでは、トラブルシューティングやパフォーマンス監視に役立つ、ルーターの動作やイベントを記録した各種ログにアクセスできます。このページには以下が含まれます。

    * System Log: システムレベルのイベントや動作の詳細ログ。
    * Kernel Log: カーネルの動作やイベントに関するログ。
    * Crash Log: 重大な問題の診断に役立つ、システムクラッシュやエラーの記録。
    * Cloud Log: ルーターに統合された GoodCloud サービスに関連するやり取りや動作のログ。
    * Nginx Log: ルーターで Nginx Web サーバーが使用されている場合のログ。Web トラフィックやサーバー動作の詳細を記録します。

    さらに、このページには Export Log ボタンがあり、技術サポートによる分析のために収集されたすべてのログをエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に有用です。

    詳細な手順については、[Log](../../interface_guide/log.md) を参照してください。

---

=== "Security"

    Security ページでは、不正アクセスからネットワークとルーターを保護するための各種セキュリティ設定を構成できます。このページには以下のオプションがあります。

    * Admin Password: ルーターの管理インターフェースのパスワードを設定または変更し、許可されたユーザーだけが設定を変更できるようにします。
    * Local Access Control: ローカルネットワークに接続されたデバイスからルーターインターフェースへのアクセスを管理および制限します。
    * Remote Access Control: インターネット経由でリモートロケーションからルーターインターフェースへアクセスする設定を構成および制限し、外部の脅威に対するセキュリティを強化します。
    * Open Ports on Router: ルーターで開いているポートを制御し、潜在的な脆弱性や不正アクセスを制限します。

    これらの設定により、ルーターと接続デバイスの両方を保護し、安全なネットワーク環境を維持できます。

    詳細な手順については、[Security](../../interface_guide/security.md) を参照してください。

=== "Reset Firmware"

    Reset Firmware ページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定へ戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直したい場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md) を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションにアクセスでき、経験豊富なユーザーが基本インターフェースを超えてルーターの設定や機能を細かく調整できます。これには、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md) を参照してください。
