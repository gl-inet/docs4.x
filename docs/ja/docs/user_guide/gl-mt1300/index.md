# Beryl (GL-MT1300) ユーザーガイド

## 製品概要

Beryl (GL-MT1300) は、パワフルなハードウェアと優れたサイバーセキュリティプロトコルを、独自のモダンなデザインに組み合わせた高性能なポケットサイズルーターです。ベストセラーモデル Slate (GL-AR750S) の上位版として、Beryl は新世代のトラベルルーターです。

![gl-mt1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/hardware_info/mt1300_interface.jpg){class="glboxshadow"}

## パッケージ内容

パッケージに同梱されるアダプターは、配送先の国によって異なります。

パッケージには以下が含まれています。

- 1 x ユーザーマニュアル
- 1 x Beryl (GL-MT1300)
- 1 x Ethernet ケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター (選択されたプラグタイプ)

![gl-mt1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/first_time_setup/mt1300_unboxing.jpg){class="glboxshadow"}

Beryl の[開封動画](../../video_library/unboxing_first_set_up.md/#gl-mt1300-beryl)もご覧ください。

## 仕様

[GL-MT1300 仕様](https://www.gl-inet.com/products/gl-mt1300/#specs){target="_blank"}

## 初回設定

すべての GL.iNet ルーターは、ほぼ同じ手順でセットアップできます。[初回セットアップの詳細はこちら](../../faq/first_time_setup.md/)。

## インターネット

ルーターの Web 管理パネルにログインし、左側のメニューから **インターネット** に移動します。

このページでは、Ethernet、Repeater、Tethering、Cellular などのインターネット接続タイプを選択できます。

### Ethernet

Ethernet ケーブルを使用して、ルーターを有効なモデムまたはネットワーク機器に接続し、インターネットにアクセスします。通常、この方法は最も高速で信頼性の高いインターネット接続を提供します。

[Ethernet ケーブルでインターネットに接続する方法はこちら](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_ethernet.png){class="glboxshadow"}

### Repeater

既存の Wi-Fi ネットワークのカバー範囲を拡張するために、ルーターをリピーターとして設定します。リピーターとして動作する場合、ルーターは範囲内の無線信号を受信して再送信し、カバー範囲を広げます。1 台のルーターでは利用エリア全体をカバーできない場合に便利です。

[既存の Wi-Fi 経由でインターネットに接続する方法はこちら](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_repeater.png){class="glboxshadow"}

### Tethering

USB ケーブルを使用して、ルーターの USB ポートをモバイルデータ通信が有効なスマートフォンに接続し、インターネットにアクセスします。この方法では、ルーターに接続された複数のデバイスがスマートフォンのモバイルデータ通信を使用してインターネットにアクセスできます。

[USB テザリングでインターネットに接続する方法はこちら](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_tethering.png){class="glboxshadow"}

### Cellular

セルラー対応の USB モデムをルーターの USB ポートに接続して、ルーターをインターネットに接続します。この方法は、USB モデムのインターネット接続をすべての接続デバイスに共有する場合に便利です。

[USB モデムでインターネットに接続する方法はこちら](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN は、複数のインターネット接続 (例: Ethernet、Repeater) を同時にルーターに設定できるネットワーク機能です。最優先のインターネット接続に障害が発生した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これはフェイルオーバーとも呼ばれ、安定した中断の少ないインターネット接続を維持します。

各インターネット接続の優先順位は、[Multi-WAN](../../interface_guide/multi-wan.md) で設定します。

また、Multi-WAN モードを Failover から Load Balance に切り替えると、複数のネットワークインターフェースを同時に使用して、ルーターの総帯域幅を増やすことができます。

---

## ワイヤレス

ワイヤレス設定では、メイン Wi-Fi とゲスト Wi-Fi のネットワークセキュリティを管理できます。サイドメニューの **ワイヤレス** からアクセスできます。

[ワイヤレス設定の詳細はこちら](../../interface_guide/wireless.md)

---

## クライアント

クライアントとは、ルーターに接続されているデバイスのことです。クライアントをブロックしたり、ネットワーク速度を制限したりできます。この画面は、ルーターの管理パネルのサイドメニューで **クライアント** をクリックすると表示されます。

[デバイスクライアントの管理の詳細はこちら](../../interface_guide/clients.md)

---

## VPN

GL.iNet ルーターには、OpenVPN と WireGuard の VPN サーバーおよび VPN クライアントがプリインストールされています。

### VPN ダッシュボード

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

詳しいセットアップ手順については、以下のリンクを参照してください。

- [**OpenVPN クライアントのセットアップ**](../../interface_guide/openvpn_client.md)
- [**OpenVPN サーバーのセットアップ**](../../interface_guide/openvpn_server.md)

### WireGuard

詳しいセットアップ手順については、以下のリンクを参照してください。

- [**WireGuard クライアントのセットアップ**](../../interface_guide/wireguard_client.md)
- [**WireGuard サーバーのセットアップ**](../../interface_guide/wireguard_server.md)

---

## アプリケーション

### プラグイン

[**プラグイン**](../../interface_guide/plugins.md) チュートリアルを参照してください。

### ダイナミック DNS

[**ダイナミック DNS**](../../interface_guide/ddns.md) チュートリアルを参照してください。

### GoodCloud

[**GoodCloud**](../../interface_guide/cloud.md) チュートリアルを参照してください。

### ネットワークストレージ

[**ネットワークストレージ**](../../interface_guide/network_storage.md) チュートリアルを参照してください。

---

## ネットワーク

### ファイアウォール

GL.iNet ルーターには、安全な接続とユーザーによる詳細な管理を実現するため、複数のファイアウォール機能が搭載されています。ポート転送、Open Ports、DMZ などのファイアウォールルールを設定できます。

[GL.iNet ルーターのファイアウォールの詳細はこちら](../../interface_guide/firewall.md)

### Multi-WAN

[**Multi-WAN**](../../interface_guide/multi-wan.md) チュートリアルを参照してください。

### LAN

[**LAN**](../../interface_guide/lan.md) チュートリアルを参照してください。

### DNS

[**DNS**](../../interface_guide/dns.md) チュートリアルを参照してください。

### ネットワークモード

[**ネットワークモード**](../../interface_guide/network_mode.md) チュートリアルを参照してください。

### IPv6

[**IPv6**](../../interface_guide/ipv6.md) チュートリアルを参照してください。

### MAC アドレス

Mac Address ページは以前 Mac Clone と呼ばれていましたが、v4.2 以降は Mac Address に変更されました。

[**MAC アドレス**](../../interface_guide/mac_address.md) チュートリアルを参照してください。

### Drop-in Gateway

[**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md) チュートリアルを参照してください。

### IGMP Snooping

[**IGMP Snooping**](../../interface_guide/igmp_snooping.md) チュートリアルを参照してください。

### ネットワークアクセラレーション

以前は [Hardware Acceleration](../../interface_guide/hardware_acceleration.md) と呼ばれていました。

[**ネットワークアクセラレーション**](../../interface_guide/network_acceleration.md) チュートリアルを参照してください。

---

## システム

### 概要

[**システム概要**](../../interface_guide/system_overview.md) チュートリアルを参照してください。

### アップグレード

GL.iNet は、パフォーマンスの向上、バグの解消、脆弱性の修正のために、ルーターのファームウェアを定期的に更新しています。

[**アップグレード**](../../interface_guide/upgrade.md) チュートリアルを参照してください。

### スケジュールされたタスク

[**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルを参照してください。

### 管理者パスワード

この機能は v4.5 以降、[**セキュリティ**](../../interface_guide/security.md) に移動しました。

[**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルを参照してください。

### タイムゾーン

[**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルを参照してください。

### トグルボタン設定

[**トグルボタン設定**](../../interface_guide/toggle_button_settings.md) チュートリアルを参照してください。

### ログ

[**ログ**](../../interface_guide/log.md) チュートリアルを参照してください。

### セキュリティ

この機能は v4.5 以降で利用できます。

[**セキュリティ**](../../interface_guide/security.md) チュートリアルを参照してください。

### ファームウェアのリセット

[**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルを参照してください。

### 詳細設定

[**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルを参照してください。
