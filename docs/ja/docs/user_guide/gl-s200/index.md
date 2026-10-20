# GL-S200 ユーザーガイド {#gl-s200-user-guide}

## ハードウェア情報 {#product-overview}

GL-S200はBLEプロトコルをサポートする小型スレッドゲートウェイで、高度にカスタマイズ可能なOpenWrtオペレーティングシステム上で動作し、クラウドデバイス管理をサポートします。様々なスマートホームデバイスへの接続や、スマートビルディングの大量デバイス接続に対応する多機能設計です。

![gl-s200 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_interface.jpg){class="glboxshadow"}

[GL-s200 仕様](https://www.gl-inet.com/products/gl-s200/#specs){target="_blank"}

### GL-S200 PCB ピン設定 {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="contentUrl" data-size="1500x1235">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="thumbnail" alt="gl-s200 pinout" loading="lazy" />
    </a>
  </figure>
</div>

### GLスレッド開発ボードのピン設定 {#gl-thread-dev-board-pinout}

![gl thread dev board pinout](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl_thread_dev_board_pinout.jpg){class="glboxshadow"}

---

## 初回設定 {#first-time-setup}

GL.iNetのすべてのデバイスは、シンプルでほぼ同じセットアッププロセスを持っています。 [初回セットアップについてはここをクリックしてください](../../faq/first_time_setup.md)。

パッケージ内のアダプターは配送国によって異なることにご注意してください。

パッケージの中には何が入っていますか？

![gl-s200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/first_time_setup/s200_unboxing.jpg){class="glboxshadow"}

同梱物：

- 1 x ユーザーマニュアル
- 1 x GL-S200
- 1 x イーサネットケーブル
- 1 x サンキューカード
- 1 x 保証書
- 1 x 電源アダプター (選択されたプラグタイプ)

Check out GL-S200's [unboxing video](../../video_library/unboxing_first_set_up.md#gl-s200).

---

## インターネット {#internet}

インターネット設定画面では、ルーターがサポートしてるインターネット接続タイプを選択できます。

ルータのWeb管理パネル内のサイドメニューで**インターネット**を選択して、インターネットネットワークを設定します。

インターネットへの接続は以下2つの方法がサポートされています:

### イーサネット {#ethernet}

イーサネットケーブルを使用して、ルーターをアクティブなモデムまたはネットワークデバイスに接続してインターネットにアクセスします。この方法は通常、最も高速で信頼性の高いインターネット接続を提供します。

[イーサネット ケーブル経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_ethernet.png){class="glboxshadow"}

### リピーター {#repeater}

ルーターをリピーターとして使用し、既存の Wi-Fi ネットワークのカバーエリアを拡大します。リピーターは範囲内の無線信号を受信して再送信し、カバーエリアを延長します。この方法は、1 台のルーターだけでは使用エリア全体をカバーできない場合に役立ちます。

[既存の Wi-Fi 経由でインターネットに接続する方法については、ここをクリックしてください。](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_repeater.png){class="glboxshadow"}

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

## Thread Mesh {#thread-mesh}

Please refer to [Thread Mesh](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/thread_mesh/) on IoT Docs.

---

## GL Dev Board {#gl-dev-board}

Please refer to [GL Dev Board](https://docs.gl-inet.com/iot/en/iot_dev_board/) on IoT Docs.

---

## Bluetooth {#bluetooth}

Please refer to [Bluetooth](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/bluetooth/) on IoT Docs.

---

## VPN {#vpn}

GL.iNetルーターには、30以上のVPNサービスをサポートするOpenVPNとWireGuard®がプリインストールされています。VPNクライアントを有効にすると、ルーターはVPNポリシー設定に従って、VPNアプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、当社のルーターはVPNサーバーとしても機能し、パブリックのインターネットにアクセスする前に、遠隔にあるクライアントデバイスからのトラフィックをVPNトンネル経由でVPNサーバーにリダイレクトします。

### VPN ダッシュボード {#vpn-dashboard}

- [**VPN ダッシュボード**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

セットアップの手順については、以下のリンクをご参照ください：

- [**OpenVPN クライアントのセットアップ**](../../interface_guide/openvpn_client.md)
- [**OpenVPN サーバーのセットアップ**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

セットアップの手順については、以下のリンクをご参照ください：

- [**WireGuard クライアントのセットアップ**](../../interface_guide/wireguard_client.md)
- [**WireGuard サーバーのセットアップ**](../../interface_guide/wireguard_server.md)

---

## アプリケーション {#applications}

GL.iNetルーターには、デバイス管理の簡素化、ユーザーのインターネット体験の向上、ファームウェアの自動更新など、幅広いアドオン機能が含まれています。

### プラグイン {#plug-ins}

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルにアクセスしてください。

### ダイナミックDNS {#dynamic-dns}

 [**ダイナミックDNS**](../../interface_guide/ddns.md)チュートリアルにアクセスしてください。

### GoodCloud {#goodcloud}

 [**GoodCloud**](../../interface_guide/cloud.md)チュートリアルにアクセスしてください。

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

### IPv6 {#ipv6}

 [**IPv6**](../../interface_guide/ipv6.md) チュートリアルにアクセスしてください。

### MACアドレス {#mac-address}

Mac アドレスページは、以前はMacクローンと呼ばれていましたが、v4.2からMacアドレスに変更されました。

 [**MACアドレス**](../../interface_guide/mac_address.md)チュートリアルにアクセスしてください。

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

### トグルボタンの設定 {#toggle-button-settings}

 [**トグルボタンの設定**](../../interface_guide/toggle_button_settings.md) チュートリアルにアクセスしてください。

### ログ {#log}

 [**ログ**](../../interface_guide/log.md) チュートリアルにアクセスしてください。

### セキュリティ {#security}

この機能はv4.5から利用可能です。

 [**セキュリティ**](../../interface_guide/security.md) チュートリアルにアクセスしてください。

### ファームウェアをリセット {#reset-firmware}

 [**ファームウェアのリセット**](../../interface_guide/reset_firmware.md) チュートリアルにアクセスしてください。

### 詳細設定 {#advanced-settings}

 [**詳細設定**](../../interface_guide/advanced_settings.md) チュートリアルにアクセスしてください。
