# Convexa-S (GL-S1300) ユーザーガイド {#convexa-s-gl-s1300-user-guide}

## 製品概要 {#product-overview}

Convexa-S (GL-S1300) は、ビームフォーミング Wi-Fi とオプションの Bluetooth を備え、すべての IoT デバイスを接続できるユニークなスマートホームゲートウェイです。合計 1267Mbps の Wi-Fi 速度、3 つのギガビットポートを備え、MU-MIMO と Wi-Fi SON に対応してデッドゾーンを解消します。8GB ストレージと OpenWrt により、VPN、ネットワークストレージ、カスタマイズ可能なソリューションを利用でき、さらに GoodCloud によるリモート管理にも対応しています。

![gl-s1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s1300/hardware_info/s1300_interface.jpg){class="glboxshadow"}

## 仕様 {#specifications}

[GL-S1300 仕様](https://www.gl-inet.com/products/gl-s1300/#specs){target="_blank"}

---

## 初回設定 {#first-time-setup}

すべての GL.iNet ルーターは、ほぼ同じ手順でセットアップできます。[初回セットアップの詳細はこちら](../../faq/first_time_setup.md)。

---

## インターネット {#internet}

ルーターの Web 管理パネルにログインし、左側のメニューから **インターネット** に移動します。

このページでは、Ethernet、Repeater、Tethering、Cellular などのインターネット接続タイプを選択できます。

### Ethernet {#ethernet}

Ethernet ケーブルを使用して、ルーターを有効なモデムまたはネットワーク機器に接続し、インターネットにアクセスします。通常、この方法は最も高速で信頼性の高いインターネット接続を提供します。

[Ethernet ケーブルでインターネットに接続する方法はこちら](../../interface_guide/internet_ethernet.md)

### Repeater {#repeater}

既存の Wi-Fi ネットワークのカバー範囲を拡張するために、ルーターをリピーターとして設定します。リピーターとして動作する場合、ルーターは範囲内の無線信号を受信して再送信し、カバー範囲を広げます。1 台のルーターでは利用エリア全体をカバーできない場合に便利です。

[既存の Wi-Fi 経由でインターネットに接続する方法はこちら](../../interface_guide/internet_repeater.md)

### Tethering {#tethering}

USB ケーブルを使用して、ルーターの USB ポートをモバイルデータ通信が有効なスマートフォンに接続し、インターネットにアクセスします。この方法では、ルーターに接続された複数のデバイスがスマートフォンのモバイルデータ通信を使用してインターネットにアクセスできます。

[USB テザリングでインターネットに接続する方法はこちら](../../interface_guide/internet_tethering.md)

### Cellular {#cellular}

セルラー対応の USB モデムをルーターの USB ポートに接続して、ルーターをインターネットに接続します。この方法は、USB モデムのインターネット接続をすべての接続デバイスに共有する場合に便利です。

[USB モデムでインターネットに接続する方法はこちら](../../interface_guide/internet_cellular.md)

### Multi-WAN {#multi-wan}

Multi-WAN は、複数のインターネット接続 (例: Ethernet、Repeater) を同時にルーターに設定できるネットワーク機能です。最優先のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これはフェイルオーバーとも呼ばれ、安定した中断の少ないインターネット接続を維持します。

各インターネット接続の優先順位は、[Multi-WAN](../../interface_guide/multi-wan.md) で設定します。

また、Multi-WAN モードを Failover から Load Balance に切り替えると、複数のネットワークインターフェースを同時に使用して、ルーターの総帯域幅を増やすことができます。

---

## ワイヤレス {#wireless}

ワイヤレス設定では、メイン Wi-Fi とゲスト Wi-Fi のネットワークセキュリティを管理できます。サイドメニューの **ワイヤレス** からアクセスできます。

[ワイヤレス設定の詳細はこちら](../../interface_guide/wireless.md)

---

## クライアント {#clients}

クライアントとは、ルーターに接続されているデバイスのことです。クライアントをブロックしたり、ネットワーク速度を制限したりできます。この画面は、ルーターの管理パネルのサイドメニューで **クライアント** をクリックすると表示されます。

[デバイスクライアントの管理の詳細はこちら](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNet ルーターには、30 以上の VPN サービスに対応した OpenVPN と WireGuard® がプリインストールされています。VPNクライアントを有効にすると、ルーターはVPNポリシー設定に従って、VPNアプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、GL.iNet ルーターは VPN サーバーとしても動作し、リモート拠点のクライアントデバイスからのトラフィックを、公開インターネットへアクセスする前に VPN トンネル経由で VPN サーバーへ転送できます。

### VPN ダッシュボード {#vpn-dashboard}

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

セットアップ手順については、以下のリンクを参照してください。

- [**OpenVPN クライアントのセットアップ**](../../interface_guide/openvpn_client.md)
- [**OpenVPN サーバーのセットアップ**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

セットアップ手順については、以下のリンクを参照してください。

- [**WireGuard クライアントのセットアップ**](../../interface_guide/wireguard_client.md)
- [**WireGuard サーバーのセットアップ**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## アプリケーション {#applications}

GL.iNet ルーターには、デバイス管理の簡素化、インターネット利用体験の向上、ファームウェア更新の自動化などに役立つ、幅広い追加機能が用意されています。

### プラグイン {#plug-ins}

[**プラグイン**](../../interface_guide/plugins.md) チュートリアルを参照してください。

### ダイナミック DNS {#dynamic-dns}

[**ダイナミック DNS**](../../interface_guide/ddns.md) チュートリアルを参照してください。

### GoodCloud {#goodcloud}

[**GoodCloud**](../../interface_guide/cloud.md) チュートリアルを参照してください。

### ネットワークストレージ {#network-storage}

[**ネットワークストレージ**](../../interface_guide/network_storage.md) チュートリアルを参照してください。

### AdGuard Home {#adguard-home}

[**AdGuard Home**](../../interface_guide/adguardhome.md) チュートリアルを参照してください。

---

## ネットワーク {#network}

### ファイアウォール {#firewall}

GL.iNet ルーターには、安全な接続とユーザーによる詳細な管理を実現するため、複数のファイアウォール機能が搭載されています。ポート転送、Open Ports、DMZ などのファイアウォールルールを設定できます。

[GL.iNet ルーターのファイアウォールの詳細はこちら](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

[**Multi-WAN**](../../interface_guide/multi-wan.md) チュートリアルを参照してください。

### LAN {#lan}

[**LAN**](../../interface_guide/lan.md) チュートリアルを参照してください。

### DNS {#dns}

[**DNS**](../../interface_guide/dns.md) チュートリアルを参照してください。

### ネットワークモード {#network-mode}

[**ネットワークモード**](../../interface_guide/network_mode.md) チュートリアルを参照してください。

### IPv6 {#ipv6}

[**IPv6**](../../interface_guide/ipv6.md) チュートリアルを参照してください。

### MAC アドレス {#mac-address}

Mac Address ページは以前 Mac Clone と呼ばれていましたが、v4.2 以降は Mac Address に変更されました。

[**MAC アドレス**](../../interface_guide/mac_address.md) チュートリアルを参照してください。

### Drop-in Gateway {#drop-in-gateway}

[**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md) チュートリアルを参照してください。

### IGMP Snooping {#igmp-snooping}

[**IGMP Snooping**](../../interface_guide/igmp_snooping.md) チュートリアルを参照してください。

### ネットワークアクセラレーション {#network-acceleration}

以前は [Hardware Acceleration](../../interface_guide/hardware_acceleration.md) と呼ばれていました。

[**ネットワークアクセラレーション**](../../interface_guide/network_acceleration.md) チュートリアルを参照してください。

---

## システム {#system}

### 概要 {#overview}

[**システム概要**](../../interface_guide/system_overview.md) チュートリアルを参照してください。

### アップグレード {#upgrade}

GL.iNet は、パフォーマンスの向上、バグの解消、脆弱性の修正のために、ルーターのファームウェアを定期的に更新しています。

[**アップグレード**](../../interface_guide/upgrade.md) チュートリアルを参照してください。

### スケジュールされたタスク {#scheduled-tasks}

[**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルを参照してください。

### 管理者パスワード {#admin-password}

この機能は v4.5 以降、[**セキュリティ**](../../interface_guide/security.md) に移動しました。

[**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルを参照してください。

### タイムゾーン {#time-zone}

[**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルを参照してください。

### ログ {#log}

[**ログ**](../../interface_guide/log.md) チュートリアルを参照してください。

### セキュリティ {#security}

この機能は v4.5 以降で利用できます。

[**セキュリティ**](../../interface_guide/security.md) チュートリアルを参照してください。

### ファームウェアのリセット {#reset-firmware}

[**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルを参照してください。

### 詳細設定 {#advanced-settings}

[**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルを参照してください。
