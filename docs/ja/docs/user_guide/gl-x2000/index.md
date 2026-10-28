# Spitz Plus (GL-X2000) ユーザーガイド {#spitz-plus-gl-x2000-user-guide}

## 製品概要 {#product-overview}

Spitz Plus (GL-X2000) は、特に遠隔地やロードトリップ中に高速で安定した接続を提供するために設計された、デュアル SIM 対応の 4G LTE Wi-Fi 6 セルラーゲートウェイです。3キャリアアグリゲーション（3CA）により、Cat 4のシングルキャリア接続と比べて最大3倍の理論チャンネル帯域幅を提供できます。これは、集約するキャリアの帯域幅、および通信事業者と地域の基地局によるLTE 3CAのサポート状況に依存します。Cellular（SIM カード）、Ethernet、Repeater、Tethering の 4 種類のインターネット接続方式に対応しています。また、Multi-WAN（フェイルオーバーとロードバランシング）、VPN（OpenVPN と WireGuard）、ペアレンタルコントロール、AdGuard Home、ポートフォワーディング、Tailscale などにも対応しています。

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## パッケージ内容 {#package-contents}

- 1 x Spitz Plus (GL-X2000)
- 1 x ユーザーマニュアル
- 4 x 外部アンテナ
- 1 x サンキューカード
- 1 x RJ45 Ethernet ケーブル
- 1 x 壁掛けキット
- 1 x 粘着パッド
- 1 x 電源アダプター
- 1 x 変換プラグ（配送先の国に応じた仕様）

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_package.png){class="glboxshadow"}

## LED インジケーター {#led-indicators}

以下に、各イベントでの LED の状態を示します。各 LED のすべての状態については、[GL-X2000 LED インジケーターの状態](../../faq/led.md#gl-x2000){target="_blank"}を参照してください。

| デバイスの状態 | Power | Internet | 2.4GHz | 5GHz | Cellular |
| --- | --- | --- | --- | --- | --- |
| インターネット接続済み | 緑 | 緑 | 緑 | 緑 | 緑 |
| インターネット未接続 | 緑 | オフ | 緑 | 緑 | 緑 |
| ファームウェア更新中 | 緑 | 0.5 秒ごとに点滅 | 0.5 秒ごとに点滅 | 0.5 秒ごとに点滅 | 緑 |
| ネットワークリセット（Reset ボタンを 5 秒間押す） | 1 秒ごとに点滅 | 緑 | 緑 | 緑 | 緑 |
| 工場出荷時リセット（Reset ボタンを 10 秒間押す） | 0.25 秒ごとに高速点滅 | 緑 | 緑 | 緑 | 緑 |

## Spitz Plus のセットアップ方法 {#how-to-set-up-spitz-plus}

Spitz Plus をセットアップするには、対応している 4 つのインターネット接続方式（Cellular（SIM カードが必要）、Ethernet、Repeater、Tethering）のいずれかを使用します。以下のセットアップ動画を視聴するか、下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>（この動画では、Spitz Plus の Cellular 接続の設定を紹介しています。その他のインターネット接続方式で Spitz Plus を設定する場合は、以下の手順を参照してください。）</small>

!!! note "開始前の手順（Cellular で接続する場合）"

    Cellular 方式でインターネットに接続するには、少なくとも 1 枚の nano SIM カードが必要です。nano SIM カードを準備したら、次の手順を実行します。
    
    1. SIM カード事業者から求められている場合は、SIM カードを有効化します。
    2. ルーターの電源をオフにします。
    3. SIM カードを SIM カードスロットに挿入します。（**注：** 同時に有効になる SIM カードは 1 枚のみです。もう一方の SIM カードはバックアップとしてのみ機能します。）

### 1. 電源を入れる {#1-power-on}

2 ピース式の電源アダプターを組み立てます。ルーターに接続し、コンセントに差し込むと自動的に起動します。

### 2. デバイスを接続する {#2-connect-device}

コンピューター、ノートパソコン、スマートフォンなどのデバイスを Wi-Fi または Ethernet でルーターに接続します。

- Ethernet

    Ethernet ケーブルを使用して、デバイスをルーターの LAN ポートに接続します。

- Wi-Fi

    デバイスでSettings -> WLANに移動し、利用可能なネットワーク一覧からルーターのWi-Fiネットワーク名を探してパスワードを入力します。デフォルトのネットワーク名とパスワードは、ルーターのラベルに印刷されています。

### 3. Web 管理パネルにログインする {#3-log-in-to-web-admin-panel}

Web ブラウザを起動し、アドレスバーに `192.168.8.1` と入力すると、GL.iNet Web 管理パネルが表示されます。言語を選択し、管理者パスワードを設定して **Apply** をクリックします。

### 4. インターネット設定 {#4-internet-setup}

**注：** 以下の手順は、GL.iNet Web 管理パネルでルーターを設定するユーザー向けです。GL.iNet アプリを使用する場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}し、画面の指示に従ってください。

対応しているインターネット接続方式（Cellular、Ethernet、Repeater、Tethering）のいずれかを使用して、Spitz Plus を設定します。[Multi-WAN](../../interface_guide/multi-wan.md) 機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    SIM カードをルーターに挿入している場合、通常はインターネットに自動接続されます。Cellular セクションに SIM 事業者名と緑のドットが表示されます。
    
    接続されない場合は、ルーターの電源をオフにし、SIM カードを挿し直してから電源をオンにします。
    
    詳細な手順については、[Cellular 経由でインターネットに接続する](../../interface_guide/internet_cellular.md#setup-for-dual-sim-models)を参照してください。

    **注：** Spitz Plus の eSIM 機能は、ファームウェア v4.7 以降で利用できます。GL.iNet ルーターで eSIM 物理カードを使用する方法は、[こちら](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)を参照してください。

    問題が発生した場合は、[セルラーネットワークのトラブルシューティングガイド](../../faq/cellular_network_troubleshooting_guide.md)を参照してください。

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}
    
    Spitz Plus の WAN ポートと、モデムなどの上位機器を Ethernet ケーブルで接続します。
    
    インターネットへの接続に成功すると、INTERNET ページの Ethernet セクションに緑のドットが表示されます。

    詳細な手順については、[Ethernet ケーブル経由でインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. Web 管理パネルの INTERNET ページで Repeater セクションを探し、**Connect** をクリックします。
    2. 利用可能なネットワークから Wi-Fi ネットワークを選択します。
    3. パスワードを入力し、**Apply** をクリックします。
    
    インターネットへの接続に成功すると、INTERNET ページの Repeater セクションに緑のドットが表示されます。

    詳細な手順については、[既存の Wi-Fi ネットワーク経由でインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. スマートフォンや USB ドングルなどのモバイルデバイスを USB ケーブルでルーターの USB ポートに接続します。
    2. モバイルデバイスで Settings に移動し、USB Tethering を有効にします。
    3. Web 管理パネルの INTERNET 画面で、Tethering セクションの **Connect** をクリックします。
    
    インターネットへの接続に成功すると、INTERNET ページの Tethering セクションに緑のドットが表示されます。

    詳細な手順については、[USB テザリング経由でインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

---

以下では、Spitz Plus の Web 管理パネルの機能を概説します。

## Wireless {#wireless}

Wireless ページでは、5 GHz と 2.4 GHz の Wi-Fi ネットワークの設定を行えます。Wi-Fi の有効化/無効化、送信出力（TX power）の設定、Wi-Fi 名（SSID）の指定、ランダム化 BSSID の有効化/無効化、Wi-Fi セキュリティモードの選択、Wi-Fi パスワードの設定、SSID の表示設定、Wi-Fi モード、帯域幅、チャンネルの選択が含まれます。

Wireless の設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients {#clients}

Clients ページには、接続中のデバイス情報が表示されます。各クライアントについて、デバイス名、接続タイプ（Ethernet 経由か Wi-Fi 経由か）、IP アドレス、MAC アドレス、ダウンロード/アップロード速度、総トラフィックが表示され、IP の予約、クライアントのブロック、その他の操作も行えます。

Clients の設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、GL.iNet ルーターへリモートアクセスして管理するための簡単な方法を提供します。
    
    GoodCloud の設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarp は、シームレスなリモートネットワークとリモートデバイス管理を提供する高度なネットワーキングプラットフォームです。GL.iNet ルーター連携向けに構築されており、ネットワーク全体にわたる包括的なデバイス管理をサポートし、上位デバイスと下位デバイスの両方を制御できます。ネットワーク全体の管理と将来的なハードウェアレベル制御を重視し、デバイス管理と安全で安定したネットワーク維持のための、より堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarp の設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

    **注：** AstroWarp を使用するには、Spitz Plus のファームウェアを v4.8 以降にアップグレードしてください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスと VPN サーバー間に安全で暗号化された通信を作成します。プライバシーとセキュリティを強化し（VPN クライアント）、リモートネットワークへのアクセス（VPN サーバー）も可能にします。Spitz Plus は OpenVPN と WireGuard に対応しています。

=== "OpenVPN" 
    
    Spitz Plus（およびその他の GL.iNet ルーター）は、強力なセキュリティを提供する OpenVPN プロトコルに対応しています。OpenVPN の設定については、次のチュートリアルを参照してください。

    * [OpenVPN クライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPN サーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Spitz Plus（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルに対応しています。WireGuard の設定については、次のチュートリアルを参照してください。

    * [WireGuard クライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuard サーバーの設定方法](../../interface_guide/wireguard_server.md)

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。
    
    Plug-ins の設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられた IP アドレスをリアルタイムで自動検出し、更新します。ドメイン名をルーターの動的なパブリック IP アドレスに対応付けるため、固定 IP アドレスがなくてもネットワークにリモートアクセスできます。
    
    Dynamic DNS の設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージは、複数のユーザーやデバイスがネットワーク経由でファイルへアクセスし共有できる、集中型のデータストレージソリューションです。
    
    Network Storage の設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Home は、広告やトラッキングをブロックして安全を守るサードパーティ製ツールです。AdGuard Home を有効にする方法については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "Parental Control"

    ペアレンタルコントロールは、お子様のデバイスを管理・制御するための設定群です。画面使用時間の制限や、特定コンテンツへのアクセス制限などが含まれます。

    Parental Control の設定については、[Parental controls](../../interface_guide/parental_control.md)を参照してください。

=== "Tailscale"

    Spitz Plus は、ファームウェア v4.7 以降で Tailscale に対応しています。
    
    Tailscale は、どこからでもデバイスやアプリケーションにアクセスできる VPN サービスです。
    
    Tailscale の設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "eSIM"

    Spitz Plus は、ファームウェア v4.7 以降で eSIM 機能に対応しています。
    
    デバイスで eSIM を設定・管理する方法については、[このチュートリアル](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)を参照してください。

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## ネットワーク {#network}

=== "Port forwarding"

    ポートフォワーディングは、インターネット上のリモートサーバーやデバイスからプライベートネットワーク内のデバイスへアクセスできるようにします。ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Multi-WAN"

    Multi-WAN は、Cellular、Repeater、Ethernet など複数のインターネット接続を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これにより、スムーズで途切れにくいインターネットアクセスを維持できます。
    
    Multi-WAN の設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなど限られた範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。
    
    LAN の設定については、[Lan Tutorial](../../interface_guide/lan.md)を参照してください。

---

=== "Guest Network"

    IPv4 プライベートアドレス範囲 192.168.0.0/16、172.16.0.0/12、10.0.0.0/8 内でサブネットを設定し、ゲートウェイとネットマスク IP アドレスを指定し、ゲストネットワーク向けに AP isolation などのセキュリティ設定を構成できます。
    
    ゲストネットワークの設定については、[ゲストネットワーク](../../interface_guide/guest_network.md)を参照してください。

=== "DNS"

    DNSページでは、カスタムDNSサーバーの設定、DNSリバインディング攻撃対策の有効化、すべてのクライアントのDNS設定の上書き、およびカスタムDNSによるVPN DNSの上書きの許可を設定できます。上流デバイスから自動的に取得したDNSサーバーを使用するか、カスタムDNSサーバーを手動で指定できます。

    DNS の設定については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "Port Management"

    Port Management ページでは、WAN/LAN ポートの設定、WAN/LAN インターフェースの Ethernet への設定、WAN インターフェースの MAC モードと MAC アドレスの指定、ネットワークポートのネゴシエート速度の確認を行えます。

    Ethernet ポートの管理については、[Port Management](../../interface_guide/ethernet_port.md)を参照してください。

---

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する設定です。
    
    Network Mode の設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。非常に大きなアドレス空間を提供し、インターネットに接続されるデバイス数の増加に対応するために必要な、ほぼ無制限の一意な IP アドレスを利用できます。
    
    IPv6 の設定については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

=== "Drop-in Gateway"

    Drop-in Gateway は、AdGuard Home、暗号化 DNS、VPN など、メインルーターにない機能を追加します。Drop-in Gateway の設定については、[How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)を参照してください。

---

=== "IGMP Snooping"

    IGMP スヌーピングは、Ethernet スイッチでマルチキャストトラフィックを管理・制御するためのネットワーク最適化技術です。
    
    IGMP Snooping の設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "Network Acceleration"

    ハードウェアアクセラレーションは、汎用 CPU よりも効率的に特定の処理を実行するために、専用ハードウェアコンポーネントを使用する仕組みです。
    
    Network Acceleration の設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

=== "NAT Settings"

    NAT Settings ページでは、Full Cone NAT と SIP ALG（Application Layer Gateway）機能の有効化または無効化を設定できます。

    NAT 設定については、[NAT Settings](../../interface_guide/nat_settings.md)を参照してください。

## システム {#system}

=== "Overview"

    Overview ページでは、ルーターの現在の状態とパフォーマンス指標をまとめて確認できます。このページでは次の情報を確認できます。

    * CPU Average Load: ルーター CPU の平均負荷を監視し、パフォーマンス評価や潜在的なボトルネックの把握に役立ちます。
    * Memory Usage: ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LED Control: ルーターの LED ライトをオンまたはオフに切り替え、表示をカスタマイズできます。
    * Flash Usage: ルーターのフラッシュストレージ使用量を確認し、ファームウェアや設定データ用の空き容量を把握できます。
    * Device Info: 稼働時間、ホスト名、モデル、アーキテクチャ、OpenWrt バージョン、カーネルバージョン、デバイス ID、デバイス MAC、デバイス S/N など、ルーターのシステム情報にアクセスできます。
    * External Storage: USB ドライブや TF カードなど、ルーターに接続された外部ストレージデバイスの状態を確認できます。
    
    これらの機能により、ルーターの動作を効果的に管理・監視するための重要な情報と制御を利用できます。

    詳細な設定手順については、[Overview](../../interface_guide/system_overview.md){target="_blank"}を参照してください。

=== "Upgrade"

    Upgrade ページは、ルーターのファームウェアを最新バージョンへ更新し、性能、セキュリティ、新機能を向上させるために使用します。このページには 4 種類のアップグレード方法があります。

    * Firmware Online Upgrade: メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * Firmware Local Upgrade: コンピューターからファームウェアファイルを手動でアップロードしてルーターを更新し、アップグレードバージョンとタイミングを制御できます。
    * Module Online Upgrade: メーカーのサーバーで最新の 4G/5G モジュールバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * Module Local Upgrade: コンピューターからモジュールファイルを手動でアップロードして 4G/5G モジュールを更新します。

    これらのオプションにより、ルーターを最新の改善や修正が含まれた状態に保てます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md){target="_blank"}を参照してください。

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前に定義したスケジュールに基づいて各種ルーター機能を自動化し、利便性と効率を高められます。このページの主な機能は次のとおりです。

    * LED Display Schedule: 特定の時間帯にルーターの LED ライトを自動的にオンまたはオフにするスケジュールを設定し、光害を減らせます。
    * Schedule Reboot: 指定した間隔でルーターを自動再起動するよう設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fi Status Schedule: 5GHz / 2.4GHz Wi-Fi バンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力を管理しやすくします。
    
    これらのスケジュール機能により、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}を参照してください。

---

=== "Time Zone"

    Time Zone ページでは、ルーターに正しいタイムゾーンを設定し、すべてのスケジュールタスク、ログ、システムイベントが現地時間に基づいて正確に記録されるようにします。この設定は、正確な記録の維持と時間ベース設定の適切な実行に重要です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md){target="_blank"}を参照してください。

=== "Log"

    Log ページでは、トラブルシューティングやパフォーマンス監視に役立つ、ルーターの動作やイベントを記録した各種ログへアクセスできます。このページには次の項目があります。

    * System Log: システムレベルのイベントや動作に関する詳細ログ。
    * Kernel Log: カーネルの処理やイベントに関するログ。
    * Crash Log: システムクラッシュやエラーの記録。重大な問題の診断に役立ちます。
    * Cloud Log: ルーターに統合された GoodCloud サービスに関連する操作や通信のログ。
    * Nginx Log: ルーターで Nginx Web サーバーを使用している場合のログ。Web トラフィックやサーバー動作の詳細を記録します。
    
    さらに、このページには Export Log ボタンがあり、収集されたすべてのログをテクニカルサポート分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に役立ちます。

    詳細な手順については、[Log](../../interface_guide/log.md){target="_blank"}を参照してください。

=== "Security"

    Security ページでは、不正アクセスからネットワークとルーターを保護するための各種セキュリティ設定を構成できます。このページには次のオプションがあります。

    * Admin Password: ルーターの管理インターフェース用パスワードを設定または変更し、許可されたユーザーのみが設定を変更できるようにします。
    * Local Access Control: ローカルネットワークに接続されたデバイスからルーターインターフェースへのアクセスを管理・制限します。
    * Remote Access Control: インターネット経由のリモートロケーションからルーターインターフェースへのアクセスを設定・制限し、外部脅威に対するセキュリティを強化します。
    * Open Ports on Router: ルーターで開いているポートを制御し、潜在的な脆弱性や不正アクセスを制限します。

    これらの設定は、安全なネットワーク環境を維持し、ルーターと接続デバイスの両方を保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

---

=== "Reset Firmware"

    Reset Firmware ページでは、現在のファームウェアバージョンをデフォルト設定へリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定に戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"}を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションへアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えてルーターの設定や機能を細かく調整できます。詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズが含まれます。

    詳細な設定手順と詳しい情報については、[Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}を参照してください。
