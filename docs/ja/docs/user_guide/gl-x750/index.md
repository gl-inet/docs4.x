# GL-X750 (Spitz) ユーザーガイド {#spitz-gl-x750-user-guide}

## ハードウェア情報 {#product-overview}

Spitzは3G/4Gデュアルバンド無線ルーターで、スマートホームやIoT分野で広く使用されています。OpenWRT OSを搭載し、様々なアプリケーションシナリオに合わせて独自のファームウェアをコンパイルすることができます。ミニPCIe 3G/4Gモジュールを内蔵しており、異なる通信事業者をサポートし、世界中で使用できます。
Spitz (GL-X750V2) は (GL-X750)の進化版です。4Gパフォーマンスを向上させるため、再設計されたPCBAと最適化されたアンテナが搭載されています。

![gl-x750 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/x750v2_interface.jpg){class="glboxshadow"}

[GL-X750 仕様](https://www.gl-inet.com/products/gl-x750/#specs){target="_blank"}

### PCB ピン設定 {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/gl-x750_pinout.jpg" itemprop="contentUrl" data-size="1500x1175">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/gl-x750_pinout.jpg" itemprop="thumbnail" alt="gl-x750 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回設定 {#first-time-setup}

GL.iNetのすべてのデバイスは、シンプルでほぼ同じセットアッププロセスを持っています。 [初回セットアップについてはここをクリックしてください](../../faq/first_time_setup.md)。

---

## インターネット {#internet}

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続は以下の4つの方法がサポートされています:

### イーサネット {#ethernet}

イーサネットケーブルを利用して、ルータをアクティブモデムまたはアクティブネットワークデバイスに接続してデータを転送します。この方法は通常、最も高速で信頼性の高いインターネット接続を提供します。

[イーサネット ケーブル経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_ethernet.png){class="glboxshadow"}

### リピーター {#repeater}

ルーターを使用して範囲内で無線シグナルを受信し、そのシグナルをより遠くへ転送することで、既存のWi-FiネットワークのWi-Fiカバーエリアを拡大します。この方法は、単一のルーターでは使用エリア全体をカバーするのに十分な範囲が確保できない場合に最も有効です。

[既存の Wi-Fi 経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_repeater.png){class="glboxshadow"}

### テザリング {#tethering}

スマートフォンの通信データをケーブル経由でルーターと共有し、接続デバイスとのインターネット接続を確立します。この方法は、スマートフォンのデータを使ってインターネットにアクセスしたい場合に便利です。

[USBテザリング経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_tethering.png){class="glboxshadow"}

### セルラー {#cellular}

セルラー対応のUSBモデムをルーターのUSBポートに挿入して、ルーターをインターネットに接続します。この方法は、USBモデムからすべての接続デバイスにインターネットアクセスを共有する場合に最も役立ちます。

[USBモデム経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_cellular.png){class="glboxshadow"}

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

---

## アプリケーション {#applications}

GL.iNetルーターには、デバイス管理の簡素化、ユーザーのインターネット体験の向上、ファームウェアアップデートの自動化など、幅広いアドオン機能が含まれています。

### プラグイン {#plug-ins}

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS {#dynamic-dns}

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud {#goodcloud}

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

### ペアレンタルコントロール {#parental-control}

 [**ペアレンタルコントロール**](../../interface_guide/parental_control.md)チュートリアルにアクセスしてください。

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

Mac アドレスページは、以前はMacクローンと呼ばれていましたが、v4.2からMacアドレスに変更されました。

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

GL.iNet は、パフォーマンスを向上させ、バグを解決し、脆弱性を修正するために、ルーターのファームウェアを定期的にアップデートします。

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

