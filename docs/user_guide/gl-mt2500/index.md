# GL-MT2500/GL-MT2500A(Brume 2) ユーザーガイド

## ハードウェア情報

GL-MT2500/GL-MT2500A(Brume 2) is a lightweight and powerful VPN Gateway that runs on OpenWrt v21.02 operating system. It is compactly designed to host a VPN server at home, or run SD-WAN (Site-to-Site) for small and medium-sized enterprises.

![gl-mt2500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

[GL-MT2500/GL-MT2500A specification](https://www.gl-inet.com/products/gl-mt2500/#specs){target="_blank"}

[LED Indication](../../faq/led.md#gl-mt2500)

### PCB ピン配置

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/gl-mt2500a_pinout.jpg" itemprop="contentUrl" data-size="1500x1313">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/gl-mt2500a_pinout.jpg" itemprop="thumbnail" alt="gl-mt2500 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

All of GL.iNet's devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup.md/).

Please note that the adapter within the package depends on your shipping country.

What’s inside the package? (The following figure shows the GL-MT2500A as an example.)

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

Package Contents:

- 1 x User manual
- 1 x Brume 2 (GL-MT2500 or GL-MT2500A)
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Warranty card
- 1 x Power adapter (Selected plug type)

---

## インターネット

The internet configuration interface lets users choose to establish the type of internet connection supported by the router.

Configure the internet network by selecting **INTERNET** in the side menu within the router's web Admin Panel. 

It supports three ways to connect to the internet as listed below:

### イーサネット

Ethernet 
Transmit data over an Ethernet cable using an Ethernet cable to connect the router to an active modem or an active network device. This method usually provides the fastest and most reliable Internet connection. 

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}

### テザリング

Establish internet access with connected devices by sharing a smartphone’s mobile data to the router via cable. This method is most useful when users wants to use the phone's data to access the internet.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

### セルラー

Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

### 優先順位とロードバランス

Go to [Multi-WAN](../../interface_guide/multi-wan.md) to set the priority of each Internet access method or the load balance when multiple Internet access methods are used at the same time.

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

---

## アプリケーション

GL.iNetルーターには、デバイス管理の簡素化、ユーザーのインターネット体験の向上、ファームウェアアップデートの自動化など、幅広いアドオン機能が含まれています。

### プラグイン

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

### ネットワークストレージ

 [**ネットワークストレージ**](../../interface_guide/network_storage.md)チュートリアルにアクセスしてください。

### AdGuard Home

 [**AdGuard Home**](../../interface_guide/adguardhome.md)チュートリアルにアクセスしてください。

### ペアレンタルコントロール

 [**ペアレンタルコントロール**](../../interface_guide/parental_control.md)チュートリアルにアクセスしてください。

### ZeroTier

 [**ZeroTier**](../../interface_guide/zerotier.md)チュートリアルにアクセスしてください。

### Tailscale

 [**Tailscale**](../../interface_guide/tailscale.md)チュートリアルにアクセスしてください。

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

### Log

Please visit the [**Log**](../../interface_guide/log.md) tutorial.

### Security

This feature is available since v4.5.

Please visit the [**Security**](../../interface_guide/security.md) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.

