# Mango 2 (GL-MG1300) ユーザーガイド {#mango-2-gl-mg1300-user-guide}

## 製品概要 {#product-overview}

Mango 2 (GL-MG1300) は、GL.iNet初のデュアルバンドWi-Fi 5対応ミニトラベルルーターで、薄型かつ携帯性に優れた設計です。2×2 MIMO構成により、理論上のデュアルバンド速度は2.4 GHzで400 Mbps、5 GHzで866 Mbpsです。OpenVPNとWireGuardをプリインストールし、30以上のVPNサービスに対応し、VPNクライアントを有効にするとネットワークトラフィックを暗号化できます。また、GoodCloudによるリモート管理にも対応し、性能、実用性、セキュリティを両立します。

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## パッケージ内容 {#package-contents}

- Mango 2 (GL-MG1300) x 1
- ユーザーマニュアル x 1
- USB-C - USB-C電源ケーブル x 1
- サンキューカード x 1

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/unboxing.png){class="glboxshadow"}

以下のMango 2の開梱動画をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/xwHgLdWPwPc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Mango 2の設定方法 {#how-to-set-up-mango-2}

Mango 2を設定するには、Ethernet、Repeater、Tethering、Cellularの4種類のインターネット接続方法のいずれかを使用します。以下の手順に従ってください。

### 1. 電源を入れる {#1-power-on}

USB Type-C電源ケーブルをルーターの電源ポートに接続します。もう一方の端を5 V/2 Aの電源アダプター（別売）に接続し、コンセントに差し込みます。

### 2. デバイスを接続する {#2-connect-device}

パソコン、ノートパソコン、スマートフォンなどのデバイスを、Wi-FiまたはEthernetでルーターに接続します。

- Ethernet

    Ethernetケーブルを使用して、デバイスをルーターのLANポートに接続します。

- Wi-Fi

    デバイスでSettings -> WLANを開き、利用可能なネットワーク一覧からルーターのWi-Fiネットワーク名を選択してパスワードを入力します。初期ネットワーク名とパスワードは、ルーター底面のラベルに記載されています。

### 3. Web管理パネルにログインする {#3-log-in-to-web-admin-panel}

Webブラウザーを開き、アドレスバーに`192.168.8.1`と入力してログインします。言語を選択して管理者パスワードを設定し、**Apply**をクリックします。

Wi-Fi情報を変更した場合は、更新後の認証情報を使用してデバイスをルーターのWi-Fiに再接続してください。

### 4. インターネット設定 {#4-internet-setup}

**注：** 以下は、GL.iNet Web管理パネルでルーターを設定する場合の手順です。GL.iNetアプリを使用する場合は、[アプリをダウンロード](https://www.gl-inet.com/app/){target="_blank"}し、画面の指示に従ってください。

Ethernet、Repeater、Tethering、Cellularのいずれかを使用してMango 2を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)を使用する場合は、複数のインターネット接続を設定してください。

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Mango 2 の WAN ポートを Ethernet ケーブルで上位機器（モデムなど）に接続します。

    インターネットに正常に接続されると、INTERNETページのEthernetセクションに緑色のドットが表示されます。

    詳細な手順については、[Ethernetケーブルでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. Web管理パネルのINTERNETページで、Repeaterセクションを見つけ、**Connect**をクリックします。
    2. 利用可能なWi-Fiネットワークから選択します。
    3. パスワードを入力し、**Apply**をクリックします。

    インターネットに正常に接続されると、INTERNETページのRepeaterセクションに緑色のドットが表示されます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSBドングルなど）をUSBケーブルでMango 2のUSBポートに接続します。
    2. モバイルデバイスでSettingsを開き、**USB Tethering**または**Personal Hotspot**を有効にします。iPhoneで確認が表示された場合は、**Trust This Device**をタップします。
    3. Web管理パネルのINTERNETページで、Tetheringセクションの**Connect**をクリックします。

    インターネットに正常に接続されると、INTERNETページのTetheringセクションに緑色のドットが表示されます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Mango 2では、USB-Cモデムを直接接続するか、USB-C - USB-Aアダプターを使用してUSB-Aモデムを接続できます。

    セルラー対応のUSBモデムをMango 2のUSBポートに挿します。USBモデムのインターネット接続を、接続中のすべてのデバイスで共有する場合に便利です。

    インターネットに正常に接続されると、INTERNETページのCellularセクションに緑色のドットが表示されます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

---

以下では、Mango 2のWeb管理パネルの機能について説明します。

## Wireless {#wireless}

Wirelessページでは、Main Network、Guest Network、IoT Networkを設定できます。各Wi-Fiネットワークで5 GHz帯と2.4 GHz帯を個別に設定でき、Wi-Fi SSID、セキュリティモード、パスワード、ランダムBSSIDなど、各帯域の基本設定も有効化および変更できます。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

## Clients {#clients}

Clients ページには、接続中のデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレス、MACアドレス、ダウンロード速度、アップロード速度、合計トラフィックを確認でき、クライアントをブロックしたり、その他の操作を実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Accountを使用すると、デバイスとクラウドサービスを接続して管理できます。GoodCloudとglinet Appの両方にシームレスにアクセスでき、安全で快適に利用できます。これにより、いつでもどこからでも、より便利にネットワークを管理できます。

    GL.iNet Accountの設定については、[GL.iNet Account](../../interface_guide/glinet_account.md)を参照してください。

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}を使用すると、GL.iNetルーターに簡単にリモートアクセスして管理できます。

=== "GoodPAS"

    GoodPASは、シームレスなリモートアクセスとデバイス管理を実現する高度なネットワーク機能です。GL.iNetルーターとの統合専用に設計されており、トラフィック難読化機能を備えたAmneziaWGプロトコルを使用して、安全で安定した接続を確保します。GoodPASを使用すると、ホームネットワークにリモートアクセスできます。自宅のルーターがGoodPASの出口ノードとして機能している場合、GoodPAS経由で送信されるインターネットトラフィックには、そのルーターのWANパブリックIPアドレスが使用されます。

    GoodPAS の設定については、[GoodPAS](../../interface_guide/goodpas.md) を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間に安全な暗号化接続を確立します。プライバシーとセキュリティを強化し（VPNクライアント）、リモートネットワークへのアクセスを可能にします（VPNサーバー）。Mango 2はOpenVPNとWireGuardに対応しています。

=== "OpenVPN"

    Mango 2（およびその他の GL.iNet ルーター）は、高いセキュリティを提供する OpenVPN プロトコルをサポートしています。OpenVPN を設定するには、以下のチュートリアルを参照してください。

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルをサポートしています。WireGuard を設定するには、以下のチュートリアルを参照してください。

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク {#network}

=== "Multi-WAN"

    Multi-WANは、ルーターに複数のインターネット接続（セルラー、リピーター、イーサネットなど）を同時に設定できるネットワーク機能です。現在のインターネット接続に障害が発生すると、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れないインターネットアクセスが確保されます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "Subnet"

    このページでは、**Main Network**、**Guest Network**、**IoT Network**、カスタムの**VLAN Networks**を一元的に設定・管理できます。複数のサブネットを作成・管理して、異なる種類のデバイスやトラフィックを分離できます。

    設定方法については、[Subnet](../../interface_guide/subnet.md)を参照してください。

=== "Ethernet Port"

    Ethernet Portページでは、WAN/LANポートの設定、WAN/LANインターフェースのEthernetへの設定、WANインターフェースのMACモードとMACアドレスの指定、ネットワークポートのネゴシエート速度の確認を行うことができます。

    Ethernet Portの設定については、[Ethernet Port](../../interface_guide/ethernet_port_v4.10.md)を参照してください。

=== "DNS"

    DNSページでは、カスタムDNSサーバーの設定、DNSリバインディング攻撃対策の有効化、すべてのクライアントのDNS設定の上書き、およびカスタムDNSによるVPN DNSの上書きの許可を設定できます。上流デバイスから自動的に取得したDNSサーバーを使用するか、カスタムDNSサーバーを手動で指定できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

---

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。ほぼ無制限の固有IPアドレスを提供する広大なアドレス空間を備え、インターネット接続デバイスの増加に対応するうえで不可欠です。

    IPV6の設定については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

=== "IGMP Snooping"

    IGMPスヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。
    
    IGMPスヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "Network Mode"

    Network Modeページでは、さまざまなネットワーク展開要件に合わせてルーターの動作役割を設定できます。家庭のWi-Fiカバレッジから企業向けマルチリンクネットワークまで、用途に応じたモードを選択でき、各モードでは特定のルーター機能を有効または無効にして性能を最適化します。

    設定方法については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU負荷を削減し、トラフィックパケットの転送を高速化できます。

    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御 {#flow-control}

Parental Controlは、子どものデバイスを管理および制御するために設計されています。スクリーン時間の制限や特定コンテンツへのアクセス制限が含まれます。

ペアレンタルコントロールの設定については、[Parental Control](../../interface_guide/parental_control_v4.9.md)を参照してください。

## セキュリティ {#security}

=== "Port Forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。

    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Admin Access"

    Admin Accessでは、不正アクセスからネットワークとルーターを保護するための各種セキュリティ設定を構成できます。

    設定方法については、[Admin Access](../../interface_guide/admin_access.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG（Application Layer Gateway）機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータープログラムに特定の機能を追加するソフトウェアコンポーネントで、機能のカスタマイズや拡張を可能にします。

    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。ドメイン名をルーターの動的なパブリックIPアドレスに対応付けるため、固定IPアドレスがなくてもネットワークにリモートアクセスできます。

    Dynamic DNSの設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージとは、複数のユーザーとデバイスがネットワーク上でファイルにアクセスして共有できる集中型データストレージソリューションを指します。

    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサービスです。

    Tailscaleの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

## システム {#system}

=== "Overview"

    Overviewページでは、ルーターの現在の状態とパフォーマンス指標をまとめて確認できます。このページでは次の情報を確認できます。

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * Flash：ルーターのフラッシュストレージの使用率を確認し、ファームウェアや設定データ用の十分な空き容量があるかを確認できます。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。

    これらの機能により、ルーターの動作を効果的に管理・監視するための重要な情報と制御を利用できます。

    詳細な手順については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェース用パスワードを設定または変更できます。

    管理者パスワードは次の要件を満たす必要があります。

    * 10文字以上63文字以下。
    * 英字（大文字と小文字を区別）、数字、および記号 `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` を使用できます。
    * 大文字、小文字、数字、記号のうち、少なくとも2種類を含める必要があります。

=== "Upgrade"

    Upgrade ページでは、ルーターのファームウェアを最新バージョンへ更新できます。これにより、性能向上、セキュリティ強化、新機能の利用が可能になります。このページには次の2つのアップグレード方法があります。

    * ファームウェアオンラインアップグレード：メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善や修正を適用した状態にルーターを保てます。

    詳細な手順については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasks ページでは、事前定義したスケジュールに基づいてルーター機能を自動化でき、利便性と効率が向上します。主な機能は次のとおりです。

    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターをカスタマイズします。
    * スケジュール再起動：ルーターを指定した間隔で自動的に再起動するように設定し、最適なパフォーマンスと安定性の維持に役立ちます。
    * Wi-Fiステータススケジュール：5GHz / 2.4GHzバンドを制御するスケジュールを設定し、ネットワーク可用性と消費電力の管理を改善できます。

    これらのスケジュール機能により、ルーターの動作をより細かく制御し、特定のニーズや好みに合わせられます。

    詳細な手順については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現地時間に基づく正確なタイムスタンプが付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な手順については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Toggle Button Settings"

    Toggle Button Settingsページでは、ルーターの物理トグルボタンを構成でき、ボタンに特定の機能を割り当ててクイックアクセスと制御を可能にします。この機能は、一般的なタスクと設定への便利なショートカットを提供し、ユーザーエクスペリエンスを向上させ、ルーターの管理を簡素化します。

    詳細な手順については、[Toggle Button Settings](../../interface_guide/toggle_button_settings.md)を参照してください。

---

=== "Reset Firmware"

    Reset Firmwareページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。この処理により、ルーターは現在インストールされているファームウェアバージョンのデフォルト設定に戻ります。継続的な問題のトラブルシューティングや、現在のファームウェアのデフォルト設定からやり直す場合に便利です。

    詳細な手順については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには次の項目があります。

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターでNginx Webサーバーを使用している場合のログ。Webトラフィックやサーバー動作の詳細を記録します。

    さらに、このページにはExport Logボタンがあり、収集されたすべてのログをテクニカルサポートによる分析用にエクスポートできます。この機能は、複雑な問題の診断や専門的な支援を受ける際に役立ちます。

    詳細な手順については、[Log](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションにアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えて、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズを行えます。

    詳細な手順については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。
