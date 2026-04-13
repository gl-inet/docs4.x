# Collie (GL-X300B) ユーザーガイド

## 製品概要

Collie（GL-X300B）は、高温環境や物理的リスクのある環境での利用を想定して設計された産業用セルラーゲートウェイです。Collie には 3 つのバージョンがあり、屋内の固定設備向け（GL-X300B-RS485 / GL-X300B-BLE）と、車載利用向け（GL-X300B-GPS）に分かれています。電気ノイズの多い環境における機器間通信にも適しています。

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

**GL-X300B-RS485、GL-X300B-BLE、GL-X300B-GPS の違いは何ですか？**

![gl-x300b series](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b_series.png){class="glboxshadow"}

![gl-x300b comparison](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/model_comparison.png){class="glboxshadow"}

- **GL-X300B-RS485** は RS485 インターフェース用の RS485 チップを搭載しています。産業オートメーションや IoT 分野の各種デバイスと双方向データ通信を行い、データ収集、制御、監視を実現します。

- **GL-X300B-BLE** は、2.4GHz Wi‑Fi、4G LTE、BLE 通信用の外部無指向性アンテナを 3 本搭載しています。全方向から信号を受信できるため、産業環境での設置場所に柔軟性があります。

- **GL-X300B-GPS** は、2 本の 2.4GHz Wi‑Fi アンテナ、2 本の 4G LTE アンテナ、1 本の GPS アンテナの計 5 本の外部アンテナを搭載しています。延長可能な有線アンテナにより、車両内で複数の受信ポイントを確保しやすく、高密度な都市部を移動する際の受信ムラを減らせます。

!!! Note

    BLE バージョンと GPS バージョンは最小注文数量の条件付きで提供されます。

## パッケージ内容

- 1 x ユーザーマニュアル
- 1 x Collie (GL-X300B-RS485)（2 年保証）
- 1 x Ethernet ケーブル
- 1 x 外部 4G アンテナ
- 2 x 外部 Wi‑Fi アンテナ
- 1 x 端子台（緑）
- 1 x 壁面取付キット
- 1 x DIN レールキット
- 1 x 電源アダプター
- 4 x 変換プラグ（US / UK / EU / AU）（3 か月保証）

![gl-x300b package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b-rs485_package.jpg){class="glboxshadow"}

## 仕様

[GL-X300B の仕様](https://www.gl-inet.com/products/gl-x300b/#specs){target="_blank"}

## 初回設定

GL.iNet のすべてのルーターは、ほぼ共通の手順でセットアップできます。[初回セットアップはこちら](../../faq/first_time_setup.md/)。

## INTERNET

ルーターの Web Admin Panel にログインし、左側メニューの **INTERNET** に移動します。

このページでは、モデルに応じて Ethernet、Repeater、Tethering、Cellular などの接続方法を選択できます。

Collie（GL-X300B）では、Ethernet、Repeater、Cellular の 3 種類の接続方式を利用できます。

### Ethernet

Ethernet ケーブルでルーターをモデムや上位ネットワーク機器に接続し、インターネットへアクセスします。通常、この方法が最も高速で安定した接続を提供します。

[イーサネットケーブルでインターネットに接続する方法はこちら](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### Repeater

ルーターをリピーターとして設定すると、既存の Wi‑Fi ネットワークの電波を受信して再送信し、カバー範囲を広げられます。1 台のルーターだけでは利用エリア全体を十分にカバーできない場合に便利です。

[既存の Wi‑Fi 経由でインターネットに接続する方法はこちら](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### Cellular

SIM カードをルーターの SIM カードスロットに挿入してインターネットに接続します。1 枚の SIM カードの回線を、接続されたすべてのデバイスで共有したい場合に便利です。

[セルラー経由でインターネットに接続する方法はこちら](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN は、ルーターに複数のインターネット接続（例: Ethernet、Repeater、Cellular）を同時に設定できる機能です。最優先の接続が失われた場合、ルーターは自動的に別の接続へ切り替えます。これは Failover とも呼ばれ、通信を途切れにくくします。

[Multi-WAN](../../interface_guide/multi-wan.md) で各インターネット接続の優先度を設定してください。

また、Multi-WAN モードを Failover から Load Balance に切り替えることで、複数のネットワークインターフェースを同時に使用し、ルーター全体の帯域幅を増やすこともできます。

---

## WIRELESS

Wireless 設定では、メイン Wi‑Fi と Guest Wi‑Fi のネットワークセキュリティを管理できます。左側メニューの **WIRELESS** からアクセスします。

[ワイヤレス設定の詳細はこちら](../../interface_guide/wireless.md)

---

## CLIENTS

Clients はルーターに接続されているデバイスです。クライアントのブロックやネットワーク速度の制限を行えます。ルーターの Admin Panel で左側メニューの **CLIENTS** をクリックすると利用できます。

[クライアント管理の詳細はこちら](../../interface_guide/clients.md)

---

## VPN

GL.iNet ルーターには、30 以上の VPN サービスに対応した OpenVPN と WireGuard® がプリインストールされています。接続されたネットワーク内のすべてのトラフィック（ゲストデバイスや VPN 暗号化を実行できないクライアントデバイスを含む）を自動的に暗号化できます。また、ルーターを VPN サーバーとして動作させ、離れた場所にあるクライアントデバイスのトラフィックを VPN トンネル経由で VPN サーバーへ転送してからパブリックインターネットへ接続することもできます。

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

セットアップ手順については、以下のリンクを参照してください。

- [**OpenVPN クライアントの設定**](../../interface_guide/openvpn_client.md)
- [**OpenVPN サーバーの設定**](../../interface_guide/openvpn_server.md)

### WireGuard

セットアップ手順については、以下のリンクを参照してください。

- [**WireGuard クライアントの設定**](../../interface_guide/wireguard_client.md)
- [**WireGuard サーバーの設定**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

GL.iNet ルーターには、デバイス管理の簡素化、インターネット利用体験の向上、ファームウェアアップデートの自動化などに役立つ、さまざまな追加機能が用意されています。

### Plug-ins

[**Plug-ins**](../../interface_guide/plugins.md) チュートリアルを参照してください。

### Dynamic DNS

[**Dynamic DNS**](../../interface_guide/ddns.md) チュートリアルを参照してください。

### GoodCloud

[**GoodCloud**](../../interface_guide/cloud.md) チュートリアルを参照してください。

---

## NETWORK

### Firewall

GL.iNet ルーターには、安全な接続とユーザーによる十分な管理を実現するための複数のファイアウォール機能が用意されています。Port Forwarding、Open Ports、DMZ などのファイアウォールルールを設定できます。

[GL.iNet ルーターのファイアウォールについて詳しくはこちら](../../interface_guide/firewall.md)

### Multi-WAN

[**Multi-WAN**](../../interface_guide/multi-wan.md) チュートリアルを参照してください。

### LAN

[**LAN**](../../interface_guide/lan.md) チュートリアルを参照してください。

### DNS

[**DNS**](../../interface_guide/dns.md) チュートリアルを参照してください。

### Network Mode

[**Network Mode**](../../interface_guide/network_mode.md) チュートリアルを参照してください。

### IPv6

[**IPv6**](../../interface_guide/ipv6.md) チュートリアルを参照してください。

### MAC Address

MAC Address ページは、以前は Mac Clone と呼ばれていましたが、v4.2 以降は MAC Address に変更されています。

[**MAC Address**](../../interface_guide/mac_address.md) チュートリアルを参照してください。

### Drop-in Gateway

[**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md) チュートリアルを参照してください。

### IGMP Snooping

[**IGMP Snooping**](../../interface_guide/igmp_snooping.md) チュートリアルを参照してください。

---

## SYSTEM

### Overview

[**System Overview**](../../interface_guide/system_overview.md) チュートリアルを参照してください。

### Upgrade

GL.iNet は、性能向上、バグ修正、脆弱性対策のために、ルーターのファームウェアを定期的に更新しています。

[**Upgrade**](../../interface_guide/upgrade.md) チュートリアルを参照してください。

### Scheduled Tasks

[**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) チュートリアルを参照してください。

### Admin Password

この機能は v4.5 から [**Security**](../../interface_guide/security.md) に移動しました。

[**Admin Password**](../../interface_guide/admin_password.md) チュートリアルを参照してください。

### Time Zone

[**Time Zone**](../../interface_guide/time_zone.md) チュートリアルを参照してください。

### Log

[**Log**](../../interface_guide/log.md) チュートリアルを参照してください。

### Security

この機能は v4.5 から利用できます。

[**Security**](../../interface_guide/security.md) チュートリアルを参照してください。

### Reset Firmware

[**Reset Firmware**](../../interface_guide/reset_firmware.md) チュートリアルを参照してください。

### Advanced Settings

[**Advanced Settings**](../../interface_guide/advanced_settings.md) チュートリアルを参照してください。
