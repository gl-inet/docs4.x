# Convexa-B (GL-B1300) ユーザーガイド {#convexa-b-gl-b1300-user-guide}

## 製品概要 {#product-overview}

Convexa-B (GL-B1300) は、商用および家庭ユーザーのワイヤレスインターネットアクセス需要を満たすための優れた製品です。ワイヤレスでインターネットを快適に利用するための最適な選択肢です。

![gl-b1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b1300/first_time_setup/router.jpg){class="glboxshadow"}

## パッケージ内容 {#package-contents}

同梱されるアダプターは配送先の国によって異なります。

パッケージには以下が含まれます。

- 1 x ユーザーマニュアル
- 1 x Convexa-B (GL-B1300)
- 1 x イーサネットケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター（選択されたプラグタイプ）

![gl-b1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b1300/first_time_setup/b1300_unboxing.jpg){class="glboxshadow"}

## 仕様 {#specifications}

[GL-B1300 仕様](https://www.gl-inet.com/products/gl-b1300/#specs){target="_blank"}

---

## 初回設定 {#first-time-setup}

すべての GL.iNet ルーターは、ほぼ同じセットアップ手順で使用を開始できます。[初回設定についてはこちら](../../faq/first_time_setup.md) を参照してください。

---

## INTERNET {#internet}

ルーターの Web 管理パネルにログインし、左側のメニューから **INTERNET** に移動します。

このページでは、Ethernet、Repeater、Tethering、Cellular などのインターネット接続タイプを選択できます。

### Ethernet {#ethernet}

イーサネットケーブルを使用して、ルーターを稼働中のモデムまたはネットワーク機器に接続し、インターネットへアクセスします。通常、この方法は最も高速で信頼性の高いインターネット接続を提供します。

[イーサネットケーブル経由でインターネットに接続する方法はこちら](../../interface_guide/internet_ethernet.md)

### Repeater {#repeater}

ルーターをリピーターとして設定し、既存の Wi-Fi ネットワークのカバー範囲を拡張します。リピーターとして動作する場合、範囲内の無線信号を受信して再送信し、カバー範囲を広げます。この方法は、1 台のルーターだけでは利用エリア全体をカバーできない場合に便利です。

[既存の Wi-Fi 経由でインターネットに接続する方法はこちら](../../interface_guide/internet_repeater.md)

### Tethering {#tethering}

有効なモバイルデータ通信を持つスマートフォンを USB ケーブルでルーターの USB ポートに接続し、インターネットへアクセスします。この方法により、ルーターに接続された複数のデバイスがスマートフォンのモバイルデータを使ってインターネットにアクセスできます。

[USB テザリング経由でインターネットに接続する方法はこちら](../../interface_guide/internet_tethering.md)

### Cellular {#cellular}

セルラー対応 USB モデムをルーターの USB ポートに接続して、ルーターをインターネットに接続します。この方法は、USB モデムのインターネット接続をすべての接続デバイスで共有する場合に便利です。

[USB モデム経由でインターネットに接続する方法はこちら](../../interface_guide/internet_cellular.md)

### Multi-WAN {#multi-wan}

Multi-WAN は、Ethernet や Repeater など複数のインターネット接続を同時に設定できるネットワーク機能です。最優先のインターネット接続が失敗した場合、ルーターは自動的に別のインターネット接続へ切り替えます。これは Failover とも呼ばれ、安定した途切れにくいインターネットアクセスを確保します。

各インターネット接続の優先順位を設定するには、[Multi-WAN](../../interface_guide/multi-wan.md) に移動してください。

また、Multi-WAN モードを Failover から Load Balance に切り替えることで、複数のネットワークインターフェースを同時に使用し、ルーターの総帯域幅を増やすこともできます。

---

## WIRELESS {#wireless}

ワイヤレス設定では、メイン Wi-Fi とゲスト Wi-Fi のネットワークセキュリティを管理できます。サイドメニューの **WIRELESS** からアクセスできます。

[ワイヤレス設定の詳細はこちら](../../interface_guide/wireless.md)

---

## CLIENTS {#clients}

クライアントとは、ルーターに接続されているデバイスのことです。クライアントをブロックしたり、ネットワーク速度を制限したりできます。この画面は、ルーターの Web 管理パネルのサイドメニューで **CLIENTS** をクリックすると表示されます。

[デバイスクライアントの管理についてはこちら](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNet ルーターには、30 以上の VPN サービスに対応する OpenVPN と WireGuard® がプリインストールされています。VPNクライアントを有効にすると、ルーターはVPNポリシー設定に従って、VPNアプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、GL.iNet ルーターは VPN サーバーとしても動作し、リモートロケーションのクライアントデバイスからのトラフィックを、公開インターネットへアクセスする前に VPN トンネル経由で VPN サーバーへ転送できます。

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

ステップごとの設定ガイドについては、以下のリンクを参照してください。

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

ステップごとの設定ガイドについては、以下のリンクを参照してください。

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS {#applications}

GL.iNet ルーターには、デバイス管理を簡素化し、ユーザーのインターネット体験を向上させ、ファームウェア更新を自動化するためのさまざまな追加機能が含まれています。

### Plug-ins {#plug-ins}

[**Plug-ins**](../../interface_guide/plugins.md) チュートリアルを参照してください。

### Dynamic DNS {#dynamic-dns}

[**Dynamic DNS**](../../interface_guide/ddns.md) チュートリアルを参照してください。

### GoodCloud {#goodcloud}

[**GoodCloud**](../../interface_guide/cloud.md) チュートリアルを参照してください。

---

## NETWORK {#network}

### Firewall {#firewall}

GL.iNet ルーターには、安全な接続とユーザーによる包括的な管理を実現するため、複数のファイアウォール機能が含まれています。Port Forwarding、Open Ports、DMZ などのファイアウォールルールを設定できます。

[GL.iNet ルーターのファイアウォールについてはこちら](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

[**Multi-WAN**](../../interface_guide/multi-wan.md) チュートリアルを参照してください。

### LAN {#lan}

[**LAN**](../../interface_guide/lan.md) チュートリアルを参照してください。

### DNS {#dns}

[**DNS**](../../interface_guide/dns.md) チュートリアルを参照してください。

### Network Mode {#network-mode}

[**Network Mode**](../../interface_guide/network_mode.md) チュートリアルを参照してください。

### IPv6 {#ipv6}

[**IPv6**](../../interface_guide/ipv6.md) チュートリアルを参照してください。

### MAC Address {#mac-address}

Mac Address ページは以前 Mac Clone と呼ばれていましたが、v4.2 以降 Mac Address に変更されました。

[**MAC Address**](../../interface_guide/mac_address.md) チュートリアルを参照してください。

### Drop-in Gateway {#drop-in-gateway}

[**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md) チュートリアルを参照してください。

### IGMP Snooping {#igmp-snooping}

[**IGMP Snooping**](../../interface_guide/igmp_snooping.md) チュートリアルを参照してください。

---

## SYSTEM {#system}

### Overview {#overview}

[**System Overview**](../../interface_guide/system_overview.md) チュートリアルを参照してください。

### Upgrade {#upgrade}

GL.iNet は、パフォーマンス向上、バグ修正、脆弱性修正のため、ルーターのファームウェアを定期的に更新しています。

[**Upgrade**](../../interface_guide/upgrade.md) チュートリアルを参照してください。

### Scheduled Tasks {#scheduled-tasks}

[**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) チュートリアルを参照してください。

### Admin Password {#admin-password}

この機能は v4.5 以降、[**Security**](../../interface_guide/security.md) に移動しました。

[**Admin Password**](../../interface_guide/admin_password.md) チュートリアルを参照してください。

### Time Zone {#time-zone}

[**Time Zone**](../../interface_guide/time_zone.md) チュートリアルを参照してください。

### Log {#log}

[**Log**](../../interface_guide/log.md) チュートリアルを参照してください。

### Security {#security}

この機能は v4.5 以降で利用できます。

[**Security**](../../interface_guide/security.md) チュートリアルを参照してください。

### Reset Firmware {#reset-firmware}

[**Reset Firmware**](../../interface_guide/reset_firmware.md) チュートリアルを参照してください。

### Advanced Settings {#advanced-settings}

[**Advanced Settings**](../../interface_guide/advanced_settings.md) チュートリアルを参照してください。
