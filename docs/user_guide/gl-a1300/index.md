# Slate Plus (GL-A1300) ユーザーガイド

## ハードウェア情報

Slate Plus (GL-A1300) is a pocket-sized travel router with a powerful CPU optimized for network stability and processing VPN encryption efficiently. It includes our latest security features and runs on the latest OpenWrt operating system. It is designed for frequent travelers who have a heavy demand on using VPN networks.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

[GL-A1300 specification](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

[LED Indication](../../faq/led.md#gl-a1300)

### PCB ピン配置

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_pinout.jpg" itemprop="contentUrl" data-size="1500x1398">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_pinout.jpg" itemprop="thumbnail" alt="GL-A1300 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

All of GL.iNet’s devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup.md/).

Please note that the adapter within the package depends on your shipping country.

What’s inside the package?

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

Package Contents:

1 x User manual
1 x Slate Plus (GL-A1300)
1 x Ethernet Cable
1 x Warranty card
1 x Power adapter (Selected plug type)

---

## インターネット

The internet configuration interface lets users choose to establish the type of internet connection supported by the router.

Configure the internet network by selecting **INTERNET** in the side menu within the router's web Admin Panel. 

It supports four ways to connect to the internet as listed below:

### イーサネット

Transmit data over an Ethernet cable using an Ethernet cable to connect the router to an active modem or an active network device. This method usually provides the fastest and most reliable Internet connection. 

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### リピーター

Extend the Wi-Fi coverage area of an existing Wi-Fi network by using a router to receive wireless signals within range and forwarding the signals to a further distance. This method is most useful when a single router does not have enough range to cover the entire usage area.

[Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### テザリング

Establish internet access with connected devices by sharing a smartphone’s mobile data to the router via cable. This method is most useful when users wants to use the phone's data to access the internet.

[Click here to learn how to connect to the internet via usb tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### セルラー

Connect the router to the internet by inserting a cellular enabled USB modem into the router's USB port. This method is most useful for sharing internet access from a USB modem to all connected devices.

[Click here to learn how to connect to the internet via usb modem](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

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

---

## システム

### 概要

 [**システム概要**](../../interface_guide/system_overview.md) チュートリアルにアクセスしてください。

### アップグレード

GL.iNet は、パフォーマンスを向上させ、バグを解決し、脆弱性を修正するために、ルーターのファームウェアを定期的に更新します。

 [**アップグレード**](../../interface_guide/firmware_upgrade.md) チュートリアルにアクセスしてください。

### スケジュールされたタスク

 [**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルにアクセスしてください。

### 管理者パスワード

この機能はv4.5から[**セキュリティ**](../../interface_guide/security.md) に移動されました。

 [**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルにアクセスしてください。

### タイムゾーン

  [**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルにアクセスしてください。

### トグルボタンの設定

 [**トグルボタンの設定**](../../interface_guide/toggle_button_settings.md) チュートリアルにアクセスしてください。

### ログ

 [**ログ**](../../interface_guide/log.md) チュートリアルにアクセスしてください。

### セキュリティ

この機能はv4.5から利用可能です。

 [**セキュリティ**](../../interface_guide/security.md) チュートリアルにアクセスしてください。

### ファームウェアをリセット

 [**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルにアクセスしてください。

### 詳細設定

 [**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルにアクセスしてください。
