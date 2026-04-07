# Convexa-B (GL-B1300) ユーザーガイド

## ハードウェア情報

Convexa-B (GL-B1300)は、商用およびホームユーザーの無線インターネットアクセスニーズを満たすための優れた製品です。ワイヤレスインターネットを快適に利用するための最良の選択肢です。

![gl-b1300 interface](https://static.gl-inet.com/docs/router/en/3/setup/gl-b1300/first_time_setup/router.jpg){class="glboxshadow"}

[GL-B1300 仕様](https://www.gl-inet.com/products/gl-b1300/#specs){target="_blank"}

### PCB ピン設定

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/2/hardware/b1300/src/GL-B1300_V1.31_PINOUT.jpg" itemprop="contentUrl" data-size="960x720">
      <img src="https://static.gl-inet.com/docs/router/en/2/hardware/b1300/src/GL-B1300_V1.31_PINOUT.jpg" itemprop="thumbnail" alt="gl-b1300 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

GL.iNetのすべてのデバイスは、シンプルでほぼ同じセットアッププロセスを持っています。 [初回セットアップについてはここをクリックしてください](../../faq/first_time_setup.md/)。

![gl-b1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b1300/first_time_setup/b1300_unboxing.jpg){class="glboxshadow"}

パッケージ内のアダプターは配送先の国によって異なります。

同梱物：

- 1 x ユーザーマニュアル
- 1 x Convexa-B (GL-B1300)
- 1 x イーサネットケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター (選択されたプラグタイプ)

---

## インターネット

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続は以下の4つの方法がサポートされています:

### イーサネット

イーサネットケーブルを使用して、ルーターをアクティブなモデムまたはネットワークデバイスに接続してインターネットにアクセスします。この方法は通常、最も高速で信頼性の高いインターネット接続を提供します。

[イーサネット ケーブル経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)

### リピーター

ルーターをリピーターとして使用し、既存の Wi-Fi ネットワークのカバーエリアを拡大します。リピーターは範囲内の無線信号を受信して再送信し、カバーエリアを延長します。この方法は、1 台のルーターだけでは使用エリア全体をカバーできない場合に役立ちます。

[既存の Wi-Fi 経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_repeater.md)

### テザリング

スマートフォンの通信データをケーブル経由でルーターと共有し、接続デバイスとのインターネット接続を確立します。この方法は、スマートフォンのデータを使ってインターネットにアクセスしたい場合に便利です。

[USBテザリング経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_tethering.md)

### セルラー

セルラー対応の USB モデムをルーターの USB ポートに挿入して、インターネットに接続します。この方法は、USB モデムからすべての接続デバイスにインターネットアクセスを共有する場合に役立ちます。

[USBモデム経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_cellular.md)

### 優先順位とロードバランス

[マルチWAN](../../interface_guide/multi-wan.md) では、各インターネットアクセス方式の優先順位や、複数のインターネットアクセス方式を同時に使用する場合のロードバランスを設定します。

---

## ワイヤレス

ワイヤレス設定では、プライマリ Wi-Fi およびゲスト Wi-Fi のネットワークセキュリティを管理できます。サイドメニューの **WIRELESS** からアクセスできます。

[ワイヤレス設定の詳細については、こちらをクリックしてください](../../interface_guide/wireless.md)

---

## クライアント

クライアントはルーターに接続されているデバイスで あり、クライアントをブロックしたり、ネットワーク速度を制限したりすることができます。このインターフェイスには、ルーターの管理パネルのサイドメニューにある **クライアント** をクリックしてアクセスできます。

[デバイスクライアントの管理については、こちらをクリックしてください。](../../interface_guide/clients.md)

---

## VPN

GL.iNetルーターには、30以上のVPNサービスをサポートするOpenVPNとWireGuard®がプリインストールされています。これは、ゲストデバイスやVPN暗号化を実行できないクライアントデバイスを含め、接続されたネットワーク内のすべてのネットワークトラフィックを自動的に暗号化します。また、当社のルーターはVPNサーバーとしても機能し、パブリックのインターネットにアクセスする前に、遠隔にあるクライアントデバイスからのトラフィックをVPNトンネル経由でVPNサーバーにリダイレクトします。

### VPN ダッシュボード

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

セットアップの手順については、以下のリンクをご参照ください：

- [**OpenVPN クライアントのセットアップ**](../../interface_guide/openvpn_client.md)
- [**OpenVPN サーバーのセットアップ**](../../interface_guide/openvpn_server.md)

### WireGuard

セットアップの手順については、以下のリンクをご参照ください：

- [**WireGuard クライアントのセットアップ**](../../interface_guide/wireguard_client.md)
- [**WireGuard サーバーのセットアップ**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## アプリケーション

GL.iNet ルーターには、デバイス管理の簡素化、ユーザーのインターネット体験の向上、ファームウェアの自動更新など、幅広いアドオン機能が含まれています。

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

### ネットワークモード

 [**ネットワークモード**](../../interface_guide/network_mode.md) チュートリアルにアクセスしてください。

### IPv6

 [**IPv6**](../../interface_guide/ipv6.md) チュートリアルにアクセスしてください。

### MACアドレス

Mac アドレスページは、で前はMacクローンと呼ばれていましたが、v4.2からMacアドレスに変更されました。

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

GL.iNet は、パフォーマンスを向上させ、バグを解消し、脆弱性を修正するために、ルーターのファームウェアを定期的にアップデートします。

 [**アップグレード**](../../interface_guide/upgrade.md) チュートリアルにアクセスしてください。

### スケジュールされたタスク

 [**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルにアクセスしてください。

### 管理者パスワード

この機能はv4.5から[**セキュリティ**](../../interface_guide/security.md) に移動されました。

 [**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルにアクセスしてください。

### タイムゾーン

  [**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルにアクセスしてください。

### ログ

 [**ログ**](../../interface_guide/log.md) チュートリアルにアクセスしてください。

### セキュリティ

この機能はv4.5から利用可能です。

 [**セキュリティ**](../../interface_guide/security.md) チュートリアルにアクセスしてください。

### ファームウェアをリセット

 [**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルにアクセスしてください。

### 詳細設定

 [**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルにアクセスしてください。