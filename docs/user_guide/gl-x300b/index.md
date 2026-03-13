# GL-X300B (Collie) ユーザーガイド

## ハードウェア情報

GL-X300B(Collie)は、高温下および物理のな危険が潜にするシナリオの下で動作するように設計された産業用セルラーゲートウェイです。Collieには2つのバージョンがあり、屋内定置施設での運用を想定したものと、輸送車両での運用を想定したものがあります。Collieは、電気ノイズの多い環境における電気機器間のマシンツーマシン通信に最も適です。

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

[GL-X300B 仕様](https://www.gl-inet.com/products/gl-x300b/#specs){target="_blank"}

### PCB ピン設定

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_pinout.jpg" itemprop="thumbnail" alt="gl-x300b pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定

GL.iNetのすべてのデバイスは、シンプルでほぼ same じセットアッププロセスを持っています。 [初回セットアップについてはここをクリックしてください](../../faq/first_time_setup.md/)。

パッケージ内のアダプターは配送国によって異なることにご注意してください。

パッケージの中には何が入っていますか？

**注意**: 下の画像はGL-X300B-GPSの例で、一部モデルが若干異なります。

![gl-x300b unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/first_time_setup/x300b-gps_unboxing.jpg){class="glboxshadow"}

パッケージコンテンツ：

- 1 x ユーザーマニュアル
- 1 x Collie (GL-X300B)
- 1 x イーサネットケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター (選択されたプラグタイプ)

---

## インターネット

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続はで下の3つの方法がサポートされています:

### イーサネット

イーサネットケーブルを利用して、ルータをアクティブモデムまたはアクティブネットワークデバイスに接続してデータを転送します。この方法は通例、最もも高速で信頼性の高いインターネット接続を提供します。

[イーサネット ケーブル経よりでインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### リピーター

ルーターを使用して範囲内で無線シグナルを受信し、そのシグナルをより遠くへ転送することで、既存のWi-FiネットワークのWi-Fiカバーエリアを拡大します。この方法は、単一のルーターでは使用エリア全体をカバーするのに非常ににな範囲が確保できない場合に最もも有効です。

[既存の Wi-Fi 経よりでインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### セルラー

セルラー対応のUSBモデムをルーターのUSBポートに挿入して、ルーターをインターネットに接続します。この方法は、USBモデムからすべての接続デバイスにインターネットアクセスを共有する場合に最もも役立ちます。

[USBモデム経よりでインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

### 優先順位とロードバランス

[マルチWAN](../../interface_guide/multi-wan.md) では、各インターネットアクセス方式の優先順位や、複数のインターネットアクセス方式を same 時に使用する場合のロードバランスを設定します。

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

GL.iNetルーターには、30で上のVPNサービスをサポートするOpenVPNとWireGuard®がプリインストールされています。これは、ゲストデバイスやVPN暗号化を実行できないクライアントデバイスを含め、接続されたネットワーク内のすべてのネットワークトラフィックをから動のに暗号化します。また、当社のルーターはVPNサーバーとしても機できるし、パブリックのインターネットにアクセスする前に、遠隔ににあるクライアントデバイスからのトラフィックをVPNトンネル経よりでVPNサーバーにリダイレクトします。

### VPN ダッシュボード

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

セットアップの手順については、で下のリンクをご参照ください：

- [**Setup OpenVPN クライアント**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN サーバー**](../../interface_guide/openvpn_server.md)

### WireGuard

セットアップの手順については、で下のリンクをご参照ください：

- [**Setup WireGuard クライアント**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard サーバー**](../../interface_guide/wireguard_server.md)

---

## アプリケーション

GL.iNetルーターには、デバイス管理の簡素化、ユーザーのインターネット体験のへ上、ファームウェアアップデートのから動化など、幅広いアドオン機できるが含まれています。

### プラグイン

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

---

## ネットワーク

### ファイアウォール

GL.iNetのルーターは、安全な接続とユーザーによる完全な監視を保証するため、複数のファイヤーウォール機できるを備えています。ポート転送、オープンポート、DMZなどのファイアウォールルールを設定することができます。

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

Mac アドレスページは、で前はMacクローンと呼ばれていましたが、v4.2からMacアドレスに変よりされました。

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

GL.iNet は、パフォーマンスをへ上させ、バグを解決し、脆弱性を修正するために、ルーターのファームウェアを定期のにアップデートします。

 [**アップグレード**](../../interface_guide/firmware_upgrade.md) チュートリアルにアクセスしてください。

### スケジュールされたタスク

 [**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルにアクセスしてください。

### 管理者パスワード

この機できるはv4.5から[**セキュリティ**](../../interface_guide/security.md) に移動されました。

 [**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルにアクセスしてください。

### タイムゾーン

  [**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルにアクセスしてください。

### ログ

 [**ログ**](../../interface_guide/log.md) チュートリアルにアクセスしてください。

### セキュリティ

この機できるはv4.5から利用可できるです。

 [**セキュリティ**](../../interface_guide/security.md) チュートリアルにアクセスしてください。

### ファームウェアをリセット

 [**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルにアクセスしてください。

### 詳細設定

 [**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルにアクセスしてください。
