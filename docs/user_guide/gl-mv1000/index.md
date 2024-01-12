# Brume (GL-MV1000) ユーザーガイド

## ハードウェア情報

Brume (GL-MV1000) および Brume-W (GL-MV1000W)* は、最先端のコンピューティングを実行するために設計された強力で安定したネットワーキング製品です。Marvellの高性能チップセットを搭載したBrumeとBrume-W* は、最先端の暗号技術を驚異的なスピードで実行し、優れたVPNルーティング体験を提供します。 プリインストールされた OpenWrt とサポートされている Ubuntu、Brumeおよび Brume-W* により、商用 IoT プロジェクトの詳細な開発が可能になります。

Brume-W（GL-MV1000W）*は、Wi-Fiモジュールを内蔵したBrume（GL-MV1000）のスペシャルエディションで、2.4GHz Wi-Fiで最大300Mbpsの高速Wi-Fi性能を実現します。

[GL-MV1000 仕様](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

### PCB ピン配置

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/3/specification/mv1000/mv1000.png" itemprop="contentUrl" data-size="1786x1328">
      <img src="https://static.gl-inet.com/docs/router/en/3/specification/mv1000/mv1000.png" itemprop="thumbnail" alt="gl-mv1000 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

GL.iNetのすべてのデバイスは、シンプルでほぼ同じセットアッププロセスを持っています。 [初回セットアップについてはここをクリックしてください](../../faq/first_time_setup.md/)。

---


## インターネット

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続は以下の3つの方法がサポートされています:

### イーサネット

イーサネットケーブルを利用して、ルータをアクティブモデムまたはアクティブネットワークデバイスに接続してデータを転送します。この方法は通常、最も高速で信頼性の高いインターネット接続を提供します。

[イーサネット ケーブル経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}


### テザリング

スマートフォンの通信データをケーブル経由でルーターと共有し、接続デバイスとのインターネット接続を確立します。この方法は、スマートフォンのデータを使ってインターネットにアクセスしたい場合に便利です。

[USBテザリング経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### セルラー

セルラー対応のUSBモデムをルーターのUSBポートに挿入して、ルーターをインターネットに接続します。この方法は、USBモデムからすべての接続デバイスにインターネットアクセスを共有する場合に最も役立ちます。

[USBモデム経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### 優先順位とロードバランス

[マルチWAN](../../interface_guide/multi-wan.md) では、各インターネットアクセス方式の優先順位や、複数のインターネットアクセス方式を同時に使用する場合のロードバランスを設定します。
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
