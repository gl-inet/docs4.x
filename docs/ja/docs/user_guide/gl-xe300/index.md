# GL-XE300 (Puli) ユーザーガイド {#puli-gl-xe300-user-guide}

## ハードウェア情報 {#product-overview}

GL-XE300（Puli）は、家庭向け、業務用、IoT用途に適したポータブル 4G スマートルーターです。OpenWrt に対応し、大容量ストレージも利用できるため、DIY IoT プロジェクトにも適しています。充電式バッテリーを内蔵しており、どこへでも持ち運べます。

![gl-xe300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/hardware_info/gl-xe300_interface.jpg){class="glboxshadow"}

[GL-XE300 仕様](https://www.gl-inet.com/products/gl-xe300/#specs){target="_blank"}

### PCB ピン設定 {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/hardware_info/gl-xe300_pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/hardware_info/gl-xe300_pinout.jpg" itemprop="thumbnail" alt="gl-xe300 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定 {#first-time-setup}

GL.iNet のすべてのデバイスは、ほぼ共通のシンプルなセットアップ手順で利用を開始できます。[初回セットアップはこちら](../../faq/first_time_setup.md)。

パッケージ内のアダプターは配送国によって異なることにご注意してください。

パッケージの中には何が入っていますか？

![gl-xe300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/first_time_setup/xe300_unboxing.jpg){class="glboxshadow"}

パッケージコンテンツ：

- 1 x ユーザーマニュアル
- 1 x Puli (GL-XE300)
- 1 x イーサネットケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター (選択されたプラグタイプ)

Puli の[開封動画](../../video_library/unboxing_first_set_up.md#gl-xe300-puli)もご覧ください。

---

## インターネット {#internet}

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続は以下の4つの方法がサポートされています:

### イーサネット {#ethernet}

イーサネットケーブルを使用して、ルーターをモデムや上位ネットワーク機器に接続します。通常、この方法が最も高速で安定したインターネット接続を提供します。

[イーサネット ケーブル経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_ethernet.png){class="glboxshadow"}

### リピーター {#repeater}

ルーターで既存の Wi-Fi 信号を受信し、その信号を再送信することで、Wi-Fi のカバー範囲を拡張します。1 台のルーターだけでは利用エリア全体を十分にカバーできない場合に特に有効です。

[既存の Wi-Fi 経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_repeater.png){class="glboxshadow"}

### テザリング {#tethering}

スマートフォンの通信データをケーブル経由でルーターと共有し、接続デバイスとのインターネット接続を確立します。この方法は、スマートフォンのデータを使ってインターネットにアクセスしたい場合に便利です。

[USBテザリング経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_tethering.png){class="glboxshadow"}

### セルラー {#cellular}

セルラー対応の USB モデムをルーターの USB ポートに挿入してインターネットに接続します。USB モデムの回線を接続中のすべてのデバイスで共有したい場合に便利です。

[USBモデム経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_cellular.png){class="glboxshadow"}

### 優先順位とロードバランス {#multi-wan}

[マルチWAN](../../interface_guide/multi-wan.md) では、各インターネットアクセス方式の優先順位や、複数のインターネットアクセス方式を同時に使用する場合のロードバランスを設定します。

---

## ワイヤレス {#wireless}

ワイヤレス設定では、ユーザーはプライマリ Wi-Fi とゲスト Wi-Fi のネットワーク セキュリティを管理することができます。サイド メニューの **ワイヤレス** に移動するとアクセスできます。

[ワイヤレス設定の詳細については、こちらをクリックしてください](../../interface_guide/wireless.md)

---

## クライアント {#clients}

クライアントはルーターに接続されているデバイスで あり、クライアントをブロックしたり、ネットワーク速度を制限したりすることができます。このインターフェイスには、ルーターの管理パネルのサイドメニューにある **クライアント** をクリックしてアクセスできます。

[デバイスクライアントの管理については、こちらをクリックしてください。](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNetルーターには、30以上のVPNサービスをサポートするOpenVPNとWireGuard®がプリインストールされています。VPNクライアントを有効にすると、ルーターはVPNポリシー設定に従って、VPNアプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、当社のルーターはVPNサーバーとしても機能し、パブリックのインターネットにアクセスする前に、遠隔にあるクライアントデバイスからのトラフィックをVPNトンネル経由でVPNサーバーにリダイレクトします。

### VPN ダッシュボード {#vpn-dashboard}

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

セットアップの手順については、以下のリンクをご参照ください：

- [**Setup OpenVPN クライアント**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN サーバー**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

セットアップの手順については、以下のリンクをご参照ください：

- [**Setup WireGuard クライアント**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard サーバー**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## アプリケーション {#applications}

GL.iNet ルーターには、デバイス管理の簡素化、インターネット利用体験の向上、ファームウェアアップデートの自動化などに役立つ、さまざまな追加機能が用意されています。

### プラグイン {#plug-ins}

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS {#dynamic-dns}

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud {#goodcloud}

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

### ネットワークストレージ {#network-storage}

 [**ネットワークストレージ**](../../interface_guide/network_storage.md)チュートリアルにアクセスしてください。

### AdGuard Home {#adguard-home}

 [**AdGuard Home**](../../interface_guide/adguardhome.md)チュートリアルにアクセスしてください。

### ペアレンタルコントロール {#parental-control}

 [**ペアレンタルコントロール**](../../interface_guide/parental_control.md)チュートリアルにアクセスしてください。

### ZeroTier {#zerotier}

 [**ZeroTier**](../../interface_guide/zerotier.md)チュートリアルにアクセスしてください。


---

## ネットワーク {#network}

### ファイアウォール {#firewall}

GL.iNetのルーターは、安全な接続とユーザーによる完全な監視を保証するため、複数のファイヤーウォール機能を備えています。ポート転送、オープンポート、DMZなどのファイアウォールルールを設定することができます。

[GL.iNetルーターのファイアウォールについて詳しくはこちら](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

 [**Multi-WAN**](../../interface_guide/multi-wan.md)チュートリアルにアクセスしてください。

### LAN {#lan}

 [**LAN**](../../interface_guide/lan.md) チュートリアルにアクセスしてください。

### DNS {#dns}

 [**DNS**](../../interface_guide/dns.md) チュートリアルにアクセスしてください。

### Network Mode {#network-mode}

 [**Network Mode**](../../interface_guide/network_mode.md) チュートリアルにアクセスしてください。

### IPv6 {#ipv6}

 [**IPv6**](../../interface_guide/ipv6.md) チュートリアルにアクセスしてください。

### MACアドレス {#mac-address}

MACアドレスページは、以前は「MAC Clone」と呼ばれていましたが、v4.2 以降は「MAC Address」に変更されています。

 [**MACアドレス**](../../interface_guide/mac_address.md)チュートリアルにアクセスしてください。

### ドロップイン・ゲートウェイ {#drop-in-gateway}

 [**ドロップイン・ゲートウェイ**](../../interface_guide/drop-in_gateway.md) チュートリアルにアクセスしてください。

### IGMPスヌーピング {#igmp-snooping}

 [**IGMPスヌーピング**](../../interface_guide/igmp_snooping.md) チュートリアルにアクセスしてください。

---

## システム {#system}

### 概要 {#overview}

 [**システム概要**](../../interface_guide/system_overview.md) チュートリアルにアクセスしてください。

### アップグレード {#upgrade}

GL.iNet は、性能向上、バグ修正、脆弱性対策のために、ルーターのファームウェアを定期的に更新しています。

 [**アップグレード**](../../interface_guide/upgrade.md) チュートリアルにアクセスしてください。

### スケジュールされたタスク {#scheduled-tasks}

 [**スケジュールされたタスク**](../../interface_guide/scheduled_tasks.md) チュートリアルにアクセスしてください。

### 管理者パスワード {#admin-password}

この機能はv4.5から[**セキュリティ**](../../interface_guide/security.md) に移動されました。

 [**管理者パスワード**](../../interface_guide/admin_password.md) チュートリアルにアクセスしてください。

### タイムゾーン {#time-zone}

  [**タイムゾーン**](../../interface_guide/time_zone.md) チュートリアルにアクセスしてください。

### ログ {#log}

 [**ログ**](../../interface_guide/log.md) チュートリアルにアクセスしてください。

### セキュリティ {#security}

この機能はv4.5から利用可能です。

 [**セキュリティ**](../../interface_guide/security.md) チュートリアルにアクセスしてください。

### ファームウェアをリセット {#reset-firmware}

 [**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルにアクセスしてください。

### 詳細設定 {#advanced-settings}

 [**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルにアクセスしてください。

