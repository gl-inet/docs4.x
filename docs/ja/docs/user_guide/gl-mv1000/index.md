# Brume (GL-MV1000) ユーザーガイド {#brume-gl-mv1000-user-guide}

## 製品概要 {#product-overview}

Brume (GL-MV1000) および Brume-W (GL-MV1000W) は、先進的なコンピューティングを行うために設計された、パワフルで安定したネットワーク製品です。Marvell の高性能チップセットにより、Brume と Brume-W* は最先端の暗号処理を高速に実行でき、優れた VPN ルーティング体験を提供します。OpenWrt がプリインストールされ、Ubuntu にも対応しているため、Brume と Brume-W* は商用 IoT プロジェクト向けの高度な開発にも対応できます。

Brume-W (GL-MV1000W) は Brume (GL-MV1000) の特別版で、内蔵 Wi-Fi モジュールを搭載しています。2.4GHz Wi-Fi で最大 300Mbps の高速 Wi-Fi 性能を提供します。

## 仕様 {#specifications}

[GL-MV1000 仕様](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

---

## 初回設定 {#first-time-setup}

すべての GL.iNet ルーターは、ほぼ同じ手順でセットアップできます。[初回セットアップの詳細はこちら](../../faq/first_time_setup.md)。

---

## インターネット {#internet}

ルーターの Web 管理パネルにログインし、左側のメニューから **INTERNET** に移動します。

このページでは、モデルに応じて Ethernet、Repeater、Tethering、Cellular などのインターネット接続タイプを選択できます。

Brume (GL-MV1000) は、Ethernet、Tethering、Cellular の 3 種類の接続タイプに対応しています。

### Ethernet {#ethernet}

Ethernet ケーブルを使用して、ルーターを稼働中のモデムまたはネットワーク機器に接続し、インターネットにアクセスします。通常、この方法は最も高速で信頼性の高いインターネット接続を提供します。

[Ethernet ケーブルでインターネットに接続する方法はこちら](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}

### Tethering {#tethering}

USB ケーブルを使用して、ルーターの USB ポートをモバイルデータ通信が有効なスマートフォンに接続し、インターネットにアクセスします。この方法では、ルーターに接続された複数のデバイスがスマートフォンのモバイルデータ通信を使用してインターネットにアクセスできます。

[USB テザリングでインターネットに接続する方法はこちら](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

セルラー対応の USB モデムをルーターの USB ポートに接続して、ルーターをインターネットに接続します。この方法は、USB モデムのインターネット接続をすべての接続デバイスに共有する場合に便利です。

[USB モデムでインターネットに接続する方法はこちら](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN は、複数のインターネット接続（例: Ethernet、Repeater）を同時にルーターに設定できるネットワーク機能です。最優先のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これはフェイルオーバーとも呼ばれ、安定した中断の少ないインターネット接続を維持します。

各インターネット接続の優先順位は、[Multi-WAN](../../interface_guide/multi-wan.md) で設定します。

また、Multi-WAN モードを Failover から Load Balance に切り替えると、複数のネットワークインターフェースを同時に使用して、ルーターの総帯域幅を増やすことができます。

---

## クライアント {#clients}

クライアントとは、ルーターに接続されているデバイスのことです。クライアントをブロックしたり、ネットワーク速度を制限したりできます。この画面は、ルーターの Web 管理パネルのサイドメニューで **CLIENTS** をクリックすると表示されます。

[デバイスクライアントの管理の詳細はこちら](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNet ルーターには、30 以上の VPN サービスに対応した OpenVPN と WireGuard® がプリインストールされています。VPN クライアントを有効にすると、ルーターは VPN ポリシー設定に従って、VPN アプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、GL.iNet ルーターは VPN サーバーとしても動作し、リモート拠点のクライアントデバイスからのトラフィックを、公開インターネットへアクセスする前に VPN トンネル経由で VPN サーバーへ転送できます。

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

### ペアレンタルコントロール {#parental-control}

[**ペアレンタルコントロール**](../../interface_guide/parental_control.md) チュートリアルを参照してください。

### ZeroTier {#zerotier}

[**ZeroTier**](../../interface_guide/zerotier.md) チュートリアルを参照してください。

### Tailscale {#tailscale}

[**Tailscale**](../../interface_guide/tailscale.md) チュートリアルを参照してください。

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

### トグルボタン設定 {#toggle-button-settings}

[**トグルボタン設定**](../../interface_guide/toggle_button_settings.md) チュートリアルを参照してください。

### ログ {#log}

[**ログ**](../../interface_guide/log.md) チュートリアルを参照してください。

### セキュリティ {#security}

この機能は v4.5 以降で利用できます。

[**セキュリティ**](../../interface_guide/security.md) チュートリアルを参照してください。

### ファームウェアのリセット {#reset-firmware}

[**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルを参照してください。

### 詳細設定 {#advanced-settings}

[**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルを参照してください。
