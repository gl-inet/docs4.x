# GL-AP1300 (Cirrus) ユーザーガイド

## ハードウェア情報

GL-AP1300（Cirrus）は、MU-MIMO Wi-Fi を採用した業務向けのシーリングマウント型無線アクセスポイントです。PoE給電とウォッチドッグタイマーを備え、幅広いエンタープライズ用途に対応します。GoodCloud 管理システムにより、デバイスを簡単かつ便利に管理でき、どこからでも安全なリモートアクセスを利用できます。

[GL-AP1300 仕様](https://www.gl-inet.com/products/gl-ap1300/#specs){target="_blank"}

### PCB ピン設定

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/3/specification/gl-ap1300/GL-AP1300-PINOUT-1.jpg" itemprop="contentUrl" data-size="6000x4000">
      <img src="https://static.gl-inet.com/docs/router/en/3/specification/gl-ap1300/GL-AP1300-PINOUT-1.jpg" itemprop="thumbnail" alt="gl-ap1300 pinout" loading="lazy" />
    </a>
  </figure>
</div>

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/3/specification/gl-ap1300/GL-AP1300-PINOUT-2.jpg" itemprop="contentUrl" data-size="6000x4000">
      <img src="https://static.gl-inet.com/docs/router/en/3/specification/gl-ap1300/GL-AP1300-PINOUT-2.jpg" itemprop="thumbnail" alt="gl-ap1300 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

GL.iNet のすべてのデバイスは、ほぼ共通のシンプルなセットアップ手順で利用を開始できます。[初回セットアップはこちら](../../faq/first_time_setup.md)。

---

## インターネット

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続は以下の4つの方法がサポートされています:

### イーサネット

イーサネットケーブルを使用して、ルーターをモデムや上位ネットワーク機器に接続します。通常、この方法が最も高速で安定したインターネット接続を提供します。

[イーサネット ケーブル経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)


### リピーター

ルーターで既存のWi-Fi信号を受信し、その信号を再送信することで、Wi-Fiのカバー範囲を拡張します。1台のルーターだけでは利用エリア全体を十分にカバーできない場合に特に有効です。

[既存の Wi-Fi 経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_repeater.md)


### テザリング

スマートフォンの通信データをケーブル経由でルーターと共有し、接続デバイスとのインターネット接続を確立します。この方法は、スマートフォンのデータを使ってインターネットにアクセスしたい場合に便利です。

[USBテザリング経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_tethering.md)


### セルラー

セルラー対応のUSBモデムをルーターのUSBポートに挿入してインターネットに接続します。USBモデムの回線を接続中のすべてのデバイスで共有したい場合に便利です。

[USBモデム経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_cellular.md)


### 優先順位とロードバランス

[マルチWAN](../../interface_guide/multi-wan.md) では、各インターネットアクセス方式の優先順位や、複数のインターネットアクセス方式を同時に使用する場合のロードバランスを設定します。

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

GL.iNetルーターには、30以上のVPNサービスをサポートするOpenVPNとWireGuard®がプリインストールされています。これは、ゲストデバイスやVPN暗号化を実行できないクライアントデバイスを含め、接続されたネットワーク内のすべてのネットワークトラフィックを自動的に暗号化します。また、当社のルーターはVPNサーバーとしても機能し、パブリックのインターネットにアクセスする前に、遠隔にあるクライアントデバイスからのトラフィックをVPNトンネル経由でVPNサーバーにリダイレクトします。

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

GL.iNetルーターには、デバイス管理の簡素化、インターネット利用体験の向上、ファームウェアアップデートの自動化などに役立つ、さまざまな追加機能が用意されています。

### プラグイン

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

### AdGuard Home

 [**AdGuard Home**](../../interface_guide/adguardhome.md)チュートリアルにアクセスしてください。

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

MACアドレスページは、以前は「MAC Clone」と呼ばれていましたが、v4.2 以降は「MAC Address」に変更されています。

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

GL.iNet は、性能向上、バグ修正、脆弱性対策のために、ルーターのファームウェアを定期的に更新しています。

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

