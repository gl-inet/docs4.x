# GL-SFT1200 (Opal) ユーザーガイド

## ハードウェア情報

GL-SFT1200 (Opal) is a pocket-sized travel router supporting 1200Mbps wireless transfers speed. It is compactly designed for portable use, which can meet the needs of wireless internet access for small businesses, small apartments or business traveler.

![gl-sft1200 interface](https://static.gl-inet.com/docs/router/en/3/setup/gl-sft1200/first_time_setup/gl-sft1200.jpg){class="glboxshadow"}

[GL-SFT1200 specification](https://www.gl-inet.com/products/gl-sft1200/#specs){target="_blank"}

### PCB ピン配置

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/3/specification/gl-sft1200/gl-sft1200-pinout.jpg" itemprop="contentUrl" data-size="1500x1500">
      <img src="https://static.gl-inet.com/docs/router/en/3/specification/gl-sft1200/gl-sft1200-pinout.jpg" itemprop="thumbnail" alt="gl-sft1200 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

All of GL.iNet's devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup.md/).

Please note that the adapter within the package depends on your shipping country.

Package Contents:

- 1 x User manual
- 1 x Opal (GL-SFT1200)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Warranty card
- 1 x Power adapter (Selected plug type)

---

## インターネット

The internet configuration interface lets users choose to establish the type of internet connection supported by the router.

Configure the internet network by selecting **INTERNET** in the side menu within the router's web Admin Panel. 

It supports four ways to connect to the internet as listed below:

### イーサネット

Transmit data over an Ethernet cable using an Ethernet cable to connect the router to an active modem or an active network device. This method usually provides the fastest and most reliable Internet connection. 

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_ethernet.png){class="glboxshadow"}

### リピーター

Extend the Wi-Fi coverage area of an existing Wi-Fi network by using a router to receive wireless signals within range and forwarding the signals to a further distance. This method is most useful when a single router does not have enough range to cover the entire usage area.

[Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_repeater.png){class="glboxshadow"}

### テザリング

Establish internet access with connected devices by sharing a smartphone’s mobile data to the router via cable. This method is most useful when users wants to use the phone's data to access the internet.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_tethering.png){class="glboxshadow"}

### セルラー
 
Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_cellular.png){class="glboxshadow"}

### 優先順位とロードバランス

Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time.

---

## ワイヤレス

ワイヤレス設定では、ユーザーはプライマリ Wi-Fi とゲスト Wi-Fi のネットワーク セキュリティを管理することができます。サイド メニューの **ワイヤレス** に移動するとアクセスできます。

[ワイヤレス設定の詳細については、こちらをクリックしてください](../../interface_guide/wireless.md)

---

## クライアント

クライアントはルーターに接続されているデバイスで あり、クライアントをブロックしたり、ネットワーク速度を制限したりすることができます。このインターフェイスには、ルーターの管理パネルのサイドメニューにある **クライアント** をクリックしてアクセスできます。

[デバイスクライアントの管理については、こちらをクリックしてください。](../../interface_guide/clients.md)

---

## VPN

GL.iNetルーターには、30以上のVPNサービスをサポートするOpenVPNとWireGuard®がプリインストールされています。これは、ゲストデバイスやVPN暗号化を実行できないクライアントデバイスを含め、接続されたネットワーク内のすべてのネットワークトラフィックを自動的に暗号化します。また、当社のルーターはVPNサーバーとしても機能し、公共のインターネットにアクセスする前に、遠隔地にあるクライアントデバイスからのトラフィックをVPNトンネル経由でVPNサーバーにリダイレクトします。

### VPN ダッシュボード

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

セットアップの手順については、以下のリンクをご参照ください：

- [**Setup OpenVPN クライアント**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN サーバー**](../../interface_guide/openvpn_server.md)

### WireGuard

セットアップの手順については、以下のリンクをご参照ください：

- [**Setup WireGuard クライアント**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard サーバー**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## アプリケーション

GL.iNetルーターには、デバイス管理の簡素化、ユーザーのインターネット体験の向上、ファームウェアアップデートの自動化など、幅広いアドオン機能が含まれています。

### プラグイン

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

---

## ネットワーク

### ファイアウォール

GL.iNetのルーターは、安全な接続とユーザーによる完全な監視を保証するため、複数のファイヤーウォール機能を備えています。ポート転送、オープンポート、DMZなどのファイアウォールルールを設定することができます。

[GL.iNetルーターのファイアウォールについて詳しくはこちら](../../interface_guide/firewall.md)

### Multi-WAN

 [**Multi-WAN**](../../interface_guide/multi-wan.md)チュートリアルにアクセスしてください。

### LAN

 [**LAN**](../../interface_guide/lan.md) チュートリアルにアクセスしてください。

### DNS

 [**DNS**](../../interface_guide/dns.md) チュートリアルにアクセスしてください。

### Network Mode

 [**Network Mode**](../../interface_guide/network_mode.md) チュートリアルにアクセスしてください。

### IPv6

 [**IPv6**](../../interface_guide/ipv6.md) チュートリアルにアクセスしてください。

### MACアドレス

Mac アドレスページは、以前はMacクローンと呼ばれていましたが、v4.2からMacアドレスに変更されました。

 [**MACアドレス**](../../interface_guide/mac_address.md)チュートリアルにアクセスしてください。

### ドロップイン・ゲートウェイ

 [**ドロップイン・ゲートウェイ**](../../interface_guide/drop-in_gateway.md) チュートリアルにアクセスしてください。

### IGMPスヌーピング

 [**IGMPスヌーピング**](../../interface_guide/igmp_snooping.md) チュートリアルにアクセスしてください。

### ネットワークアクセラレーション

以前は[ハードウェア アクセラレーション](../../interface_guide/hardware_acceleration.md)と呼ばれていました。

[**ネットワークアクセラレーション**](../../interface_guide/network_acceleration.md) チュートリアルにアクセスしてください。
---

## SYSTEM

### Overview

Please visit the [**System Overview**](../../interface_guide/system_overview.md) tutorial.

### Upgrade

GL.iNet provides regular updates on our routers' firmware to improve performance, resolving bugs and fix vulnerabilities.

Please visit the [**Upgrade**](../../interface_guide/firmware_upgrade.md) tutorial.

### Scheduled Tasks

Please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.

### Admin Password

This feature has been moved to [**Security**](../../interface_guide/security.md) since v4.5.

Please visit the [**Admin Password**](../../interface_guide/admin_password.md) tutorial.

### Time Zone

Please visit the  [**Time Zone**](../../interface_guide/time_zone.md) tutorial.

### Toggle Button Settings

Please visit the [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md) tutorial.

### Log

Please visit the [**Log**](../../interface_guide/log.md) tutorial.

### Security

This feature is available since v4.5.

Please visit the [**Security**](../../interface_guide/security.md) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.
