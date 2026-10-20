# Slate Plus (GL-A1300) ユーザーガイド {#slate-plus-gl-a1300-user-guide}

## 製品概要 {#product-overview}

Slate Plus（GL-A1300）は、ネットワークの安定性と VPN 暗号化の効率的な処理に最適化された高性能 CPU を搭載した、ポケットサイズのトラベルルーターです。最新のセキュリティ機能を備え、最新の OpenWrt オペレーティングシステムで動作します。VPN ネットワークを頻繁に利用する旅行者向けに設計されています。

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## パッケージ内容 {#package-contents}

パッケージに含まれるアダプターは、配送先の国によって異なります。

パッケージには以下が含まれます。

- 1 x ユーザーマニュアル
- 1 x Slate Plus (GL-A1300)
- 1 x イーサネットケーブル
- 1 x 保証書
- 1 x 電源アダプター（選択したプラグタイプ）

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## LED表示 {#led-indication}

[LED 表示](../../faq/led.md#gl-a1300)

## 仕様 {#specifications}

[GL-A1300 仕様](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

## 初回設定 {#first-time-setup}

すべての GL.iNet ルーターは、シンプルでほぼ共通のセットアップ手順で設定できます。[初回セットアップの詳細はこちら](../../faq/first_time_setup.md)。

Slate Plus をセットアップするには、サポートされている 4 つのインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用します。以下のセットアップ動画を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## インターネット {#internet}

インターネット設定画面では、ルーターが対応しているインターネット接続タイプを選択して、接続を確立できます。

ルーターの Web 管理パネルのサイドメニューで **INTERNET** を選択し、インターネット接続を設定します。

以下の 4 つの方法でインターネットに接続できます。

### イーサネット {#ethernet}

イーサネットケーブルでルーターを稼働中のモデムまたはネットワーク機器に接続し、データを送受信します。通常、この方法は最も高速で信頼性の高いインターネット接続を提供します。

[イーサネットケーブルでインターネットに接続する方法はこちら](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### リピーター {#repeater}

ルーターで範囲内の無線信号を受信し、さらに遠くへ転送することで、既存の Wi-Fi ネットワークのカバー範囲を拡張します。1 台のルーターでは利用エリア全体をカバーできない場合に特に便利です。

[既存の Wi-Fi 経由でインターネットに接続する方法はこちら](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### テザリング {#tethering}

スマートフォンのモバイルデータ通信をケーブル経由でルーターと共有し、接続されたデバイスからインターネットにアクセスできるようにします。スマートフォンのデータ通信を使用してインターネットにアクセスしたい場合に特に便利です。

[USB テザリングでインターネットに接続する方法はこちら](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### セルラー {#cellular}

セルラー対応の USB モデムをルーターの USB ポートに挿入して、インターネットに接続します。この方法は、USB モデムのインターネット接続を、接続中のすべてのデバイスで共有する場合に特に便利です。

[USB モデムでインターネットに接続する方法はこちら](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### 優先順位とロードバランス {#priority-and-load-balance}

複数のインターネット接続方法を同時に使用する場合は、[Multi-WAN](../../interface_guide/multi-wan.md) で各接続方法の優先順位またはロードバランスを設定します。

---

## ワイヤレス {#wireless}

ワイヤレス設定では、メイン Wi-Fi とゲスト Wi-Fi のネットワークセキュリティを管理できます。サイドメニューの **WIRELESS** からアクセスできます。

[ワイヤレス設定の詳細はこちら](../../interface_guide/wireless.md)

---

## クライアント {#clients}

クライアントとは、ルーターに接続されているデバイスのことです。クライアントをブロックしたり、ネットワーク速度を制限したりできます。この画面は、ルーターの管理パネルのサイドメニューで **CLIENTS** をクリックすると表示されます。

[デバイスクライアントの管理の詳細はこちら](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNet ルーターには、30 以上の VPN サービスに対応した OpenVPN と WireGuard® がプリインストールされています。VPN クライアントを有効にすると、ルーターは VPN ポリシー設定に従って、VPN アプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、GL.iNet ルーターは VPN サーバーとしても動作し、リモート拠点にあるクライアントデバイスからのトラフィックを、公開インターネットへアクセスする前に VPN トンネル経由で VPN サーバーへ転送できます。

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

---

## アプリケーション {#applications}

GL.iNet ルーターには、デバイス管理の簡素化、インターネット利用体験の向上、ファームウェア更新の自動化などに役立つ、幅広い追加機能が用意されています。

### プラグイン {#plug-ins}

[**プラグイン**](../../interface_guide/plugins.md) チュートリアルを参照してください。

### ダイナミックDNS {#dynamic-dns}

[**ダイナミックDNS**](../../interface_guide/ddns.md) チュートリアルを参照してください。

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

GL.iNet ルーターには、安全な接続を確保し、ユーザーがネットワークを十分に管理できるよう、複数のファイアウォール機能が搭載されています。ポート転送、オープンポート、DMZ などのファイアウォールルールを設定できます。

[GL.iNet ルーターのファイアウォールの詳細はこちら](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan}

[**Multi-WAN**](../../interface_guide/multi-wan.md) チュートリアルを参照してください。

### LAN {#lan}

[**LAN**](../../interface_guide/lan.md) チュートリアルを参照してください。

### DNS {#dns}

[**DNS**](../../interface_guide/dns.md) チュートリアルを参照してください。

### ネットワークモード {#network-mode}

[**ネットワークモード**](../../interface_guide/network_mode.md) チュートリアルを参照してください。

### IPv6 {#ipv6}

[**IPv6**](../../interface_guide/ipv6.md) チュートリアルを参照してください。

### MACアドレス {#mac-address}

MAC アドレスページは、以前は「MAC Clone」という名称でしたが、v4.2 以降は「MAC Address」に変更されました。

[**MACアドレス**](../../interface_guide/mac_address.md) チュートリアルを参照してください。

### ドロップイン・ゲートウェイ {#drop-in-gateway}

[**ドロップイン・ゲートウェイ**](../../interface_guide/drop-in_gateway.md) チュートリアルを参照してください。

### IGMPスヌーピング {#igmp-snooping}

[**IGMPスヌーピング**](../../interface_guide/igmp_snooping.md) チュートリアルを参照してください。

---

## システム {#system}

### 概要 {#overview}

[**システム概要**](../../interface_guide/system_overview.md) チュートリアルを参照してください。

### アップグレード {#upgrade}

GL.iNet は、パフォーマンスの向上、バグの修正、脆弱性への対処のため、ルーターのファームウェアを定期的に更新しています。

[**アップグレード**](../../interface_guide/upgrade.md) チュートリアルを参照してください。

### スケジュールされたタスク {#scheduled-tasks}

[**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルを参照してください。

### 管理者パスワード {#admin-password}

この機能は、v4.5 以降 [**セキュリティ**](../../interface_guide/security.md) に移動しました。

[**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルを参照してください。

### タイムゾーン {#time-zone}

[**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルを参照してください。

### トグルボタンの設定 {#toggle-button-settings}

[**トグルボタンの設定**](../../interface_guide/toggle_button_settings.md) チュートリアルを参照してください。

### ログ {#log}

[**ログ**](../../interface_guide/log.md) チュートリアルを参照してください。

### セキュリティ {#security}

この機能は v4.5 以降で利用できます。

[**セキュリティ**](../../interface_guide/security.md) チュートリアルを参照してください。

### ファームウェアのリセット {#reset-firmware}

[**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルを参照してください。

### 詳細設定 {#advanced-settings}

[**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルを参照してください。
