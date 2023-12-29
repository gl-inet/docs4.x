# GL-S200 ユーザーガイド

## ハードウェア情報

GL-S200 is a miniaturized Thread gateway supporting BLE protocol that runs on a highly customizable OpenWrt operating system and supports cloud device management. It has a versatile design for connecting to various smart home devices, or mass device connectivity for smart buildings.

![gl-s200 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_interface.jpg){class="glboxshadow"}

[GL-s200 specification](https://www.gl-inet.com/products/gl-s200/#specs){target="_blank"}

### GL-S200 PCB ピン配置

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="contentUrl" data-size="1500x1235">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="thumbnail" alt="gl-s200 pinout" loading="lazy" />
    </a>
  </figure>
</div>

### GL Thread Dev Board Pinout

![gl thread dev board pinout](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl_thread_dev_board_pinout.jpg){class="glboxshadow"}

---

## 初回設定

All of GL.iNet's devices have a simple and almost identical setup process, [click here to learn about the first time setup](../../faq/first_time_setup.md/).

Please note that the adapter within the package depends on your shipping country.

What's inside the package?

![gl-s200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/first_time_setup/s200_unboxing.jpg){class="glboxshadow"}

Package Contents:

- 1 x User manual
- 1 x GL-S200
- 1 x Ethernet cable
- 1 x Thank you card
- 1 x Warranty card
- 1 x Power adapter (Selected plug type)

Check out GL-S200's [unboxing video](../../video_library/unboxing_first_set_up.md#gl-s200).

---

## インターネット

The internet configuration interface lets users choose to establish the type of internet connection supported by the router.

Configure the internet network by selecting **INTERNET** in the side menu within the router's web Admin Panel. 

It supports two ways to connect to the internet as listed below:

### イーサネット

Transmit data over an Ethernet cable using an Ethernet cable to connect the router to an active modem or an active network device. This method usually provides the fastest and most reliable Internet connection. 

[Click here to learn how to connect to the internet via an ethernet cable](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_ethernet.png){class="glboxshadow"}

### リピーター

Extend the Wi-Fi coverage area of an existing Wi-Fi network by using a router to receive wireless signals within range and forwarding the signals to a further distance. This method is most useful when a single router does not have enough range to cover the entire usage area.

[Click here to learn how to connect to the internet via an existing Wi-Fi](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_repeater.png){class="glboxshadow"}

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

## Thread Mesh

Please refer to [Thread Mesh](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/thread_mesh/) on IoT Docs.

---

## GL Dev Board

Please refer to [GL Dev Board](https://docs.gl-inet.com/iot/en/iot_dev_board/) on IoT Docs.

---

## Bluetooth

Please refer to [Bluetooth](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/bluetooth/) on IoT Docs.

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

### IPv6

 [**IPv6**](../../interface_guide/ipv6.md) チュートリアルにアクセスしてください。

### MACアドレス

Mac アドレスページは、以前はMacクローンと呼ばれていましたが、v4.2からMacアドレスに変更されました。

 [**MACアドレス**](../../interface_guide/mac_address.md)チュートリアルにアクセスしてください。

### IGMPスヌーピング

 [**IGMPスヌーピング**](../../interface_guide/igmp_snooping.md) チュートリアルにアクセスしてください。

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
