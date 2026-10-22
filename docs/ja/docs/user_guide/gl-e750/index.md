# Mudi V2 (GL-E750V2) ユーザーガイド {#mudi-v2-gl-e750v2-user-guide}

**注：** Mudi V2 (GL-E750V2) と Mudi (GL-E750) は同じファームウェアで動作します。Mudi (GL-E750) を使用している場合、最新の機能を使用するには[ファームウェアをアップグレード](https://dl.gl-inet.com/?model=e750)してください。

## 製品概要 {#product-overview}

Mudi V2 (GL-E750V2) は、世界各国の通信事業者に対応したポータブル4G LTEトラベルルーターです。OpenWrtとGL.iNetのSDK 4.0上で完全にオープンソースで動作し、高いカスタマイズ性と豊富な機能を備えています。Mudi V2 (GL-E750V2) は300Mbps (2.4GHz) と433Mbps (5GHz) のWi-Fi速度に対応し、最大1TBのMicroSDカードを使用できます。7000mAhのバッテリーを内蔵しています。また、Multi-WAN（フェイルオーバーとロードバランス）に対応しており、すべてのデバイスで安定した接続を確保できます。

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/hardware_info/e750_interface.jpg){class="glboxshadow"}

## ボタン {#button}

- 電源ボタンを**3秒間押す**：デバイスの電源を入れる

- 電源ボタンを**3〜5秒間押す**：スタンバイモードに入る

- 電源ボタンを**5秒以上押す**：デバイスの電源を切る

    （3秒間押すと、まずOLED画面に「Standby Mode On」が表示されます。そのまま、「Standby Mode On」の下に「Shut Down」が表示されるまで電源ボタンを押し続けてください。3秒のカウントダウンの後、デバイスの電源が切れます。）

## スタンバイモード {#standby-mode}

スタンバイモードでは、Mudi V2 (GL-E750V2) は電力を節約するためにWi-Fiと4Gをオフにします。このモードではMudi V2 (GL-E750V2) に接続できません。

スタンバイモードをオンまたはオフにするには、電源ボタンを3秒間押します。OLED画面に「Standby Mode On」または「Standby Mode Off」が表示されます。

## パッケージ内容 {#package-contents}

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Mudi V2 (GL-E750V2) 携帯式4G LTEルーター
- 1 x 電源アダプター
- 4 x 変換プラグ（US、EU、UK、AUプラグ）
- 1 X ユーザーマニュアル
- 1 x 保証書
- 1 x Ethernetケーブル
- 1 x USB-Cポートレプリケーター
- 1 x USB-C to USB-Cケーブル
- 1 x USB-A to USB-Cケーブル
- 1 x 収納ポーチ
- 1 x サンキューカード

---

## 初期設定 {#first-time-setup}

動画を視聴するか、以下の手順に従ってMudi V2をセットアップしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. SIMカードを挿入する {#1-insert-a-sim-card}

SIMカードとオプションのMicroSDカードをMudi V2 (GL-E750V2) に挿入します。

注：SIMカードを使用する場合は、電源を入れる前にデバイスに挿入する必要があります。

1. Mudi V2 (GL-E750V2) を裏返します。
2. カバーの縁の近くにある穴に指を入れます。
3. 縁に沿って指をスライドさせます。
4. カバーが少し（約25～30度）持ち上がったら、引き上げて開きます。
5. 角の近くにある記号の向きに従って、カードをカードスロットに挿入します。
6. カバーを押し下げて閉じます。

### 2. 電源を入れる {#2-power-on}

電源ボタンを押してデバイスの電源を入れます。

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_power-on.png){class="glboxshadow"}

Mudi V2 (GL-E750V2) の電源が切れている場合でも、電源ボタンを押すとバッテリー状態を確認できます。電源ボタンを押すと、OLED画面にバッテリー状態が表示されます。

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_battery.png){class="glboxshadow"}

必ず標準の5V/2A電源アダプターを使用してください。それ以外のアダプターを使用すると、故障の原因となる場合があります。

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_charge.png){class="glboxshadow"}

---

## インターネット {#internet}

ルーターのWeb管理パネルにログインし、左側のメニューから**INTERNET**に移動します。

このページでは、Ethernet、Repeater、Tethering、Cellularなどのインターネット接続タイプを選択できます。

### Ethernet {#ethernet}

Ethernetケーブルを使用して、ルーターを稼働中のモデムまたはネットワーク機器に接続し、インターネットにアクセスします。通常、この方法は最も高速で信頼性の高いインターネット接続を提供します。

[Ethernetケーブルでインターネットに接続する方法についてはこちらをクリック](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

ルーターをリピーターとして設定し、既存のWi-Fiネットワークのカバー範囲を拡張します。リピーターとして動作する場合、範囲内の無線信号を受信して再送信し、カバー範囲を広げます。この方法は、1台のルーターでは利用エリア全体をカバーできない場合に便利です。

[既存のWi-Fiでインターネットに接続する方法についてはこちらをクリック](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

モバイルデータ通信が有効なスマートフォンをUSBケーブルでルーターのUSBポートに接続し、インターネットにアクセスします。この方法により、ルーターに接続された複数のデバイスがスマートフォンのモバイルデータを使ってインターネットにアクセスできます。

[USBテザリングでインターネットに接続する方法についてはこちらをクリック](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Mudi V2の背面カバーを外し、SIMカードをSIMカードスロットに挿入してインターネットに接続します。この方法は、1枚のSIMカードのインターネット接続を、接続中のすべてのデバイスで共有する場合に便利です。

[セルラーでインターネットに接続する方法についてはこちらをクリック](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_cellular.png){class="glboxshadow"}

GL.iNetルーターでeSIM物理カードを使用する方法については、こちらを参照してください：[GL.iNetルーターでeSIM物理カードを使用する方法](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

---

## ワイヤレス {#wireless}

ワイヤレス設定では、メインWi-FiとゲストWi-Fiのネットワークセキュリティを管理できます。サイドメニューの**WIRELESS**からアクセスできます。

[ワイヤレス設定の詳細についてはこちらをクリック](../../interface_guide/wireless.md)

---

## クライアント {#clients}

クライアントとは、ルーターに接続されているデバイスのことです。クライアントをブロックしたり、ネットワーク速度を制限したりできます。この画面は、ルーターのWeb管理パネルのサイドメニューで**CLIENTS**をクリックすると表示されます。

[デバイスクライアントの管理の詳細についてはこちらをクリック](../../interface_guide/clients.md)

---

## VPN {#vpn}

GL.iNetルーターには、30以上のVPNサービスに対応したOpenVPNとWireGuard®がプリインストールされています。VPNクライアントを有効にすると、ルーターはVPNポリシー設定に従って、VPNアプリを実行できないデバイスを含むネットワーク上のデバイスのトラフィックを暗号化できます。また、GL.iNetルーターはVPNサーバーとしても動作し、リモート拠点にあるクライアントデバイスからのトラフィックを、公開インターネットへアクセスする前にVPNトンネル経由でVPNサーバーへ転送できます。

### VPNダッシュボード {#vpn-dashboard}

- [**VPNダッシュボード**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

セットアップ手順については、以下のリンクを参照してください。

- [**OpenVPNクライアントの設定**](../../interface_guide/openvpn_client.md)
- [**OpenVPNサーバーの設定**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

セットアップ手順については、以下のリンクを参照してください。

- [**WireGuardクライアントの設定**](../../interface_guide/wireguard_client.md)
- [**WireGuardサーバーの設定**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## アプリケーション {#applications}

GL.iNetルーターには、デバイス管理の簡素化、インターネット利用体験の向上、ファームウェア更新の自動化などに役立つ、幅広い追加機能が用意されています。

### プラグイン {#plug-ins}

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルを参照してください。

### Dynamic DNS {#dynamic-dns}

[**Dynamic DNS**](../../interface_guide/ddns.md)チュートリアルを参照してください。

### GoodCloud {#goodcloud}

[**GoodCloud**](../../interface_guide/cloud.md)チュートリアルを参照してください。

---

## ネットワーク {#network}

### ファイアウォール {#firewall}

GL.iNetルーターには、安全な接続を確保し、ユーザーがネットワークを十分に管理できるよう、複数のファイアウォール機能が搭載されています。Port Forwarding、Open Ports、DMZなどのファイアウォールルールを設定できます。

[GL.iNetルーターのファイアウォールの詳細についてはこちらをクリック](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan}

[**Multi-WAN**](../../interface_guide/multi-wan.md)チュートリアルを参照してください。

### LAN {#lan}

[**LAN**](../../interface_guide/lan.md)チュートリアルを参照してください。

### DNS {#dns}

[**DNS**](../../interface_guide/dns.md)チュートリアルを参照してください。

### ネットワークモード {#network-mode}

[**ネットワークモード**](../../interface_guide/network_mode.md)チュートリアルを参照してください。

### IPv6 {#ipv6}

[**IPv6**](../../interface_guide/ipv6.md)チュートリアルを参照してください。

### MACアドレス {#mac-address}

MACアドレスページは、以前は「Mac Clone」という名称でしたが、v4.2以降は「Mac Address」に変更されました。

[**MACアドレス**](../../interface_guide/mac_address.md)チュートリアルを参照してください。

### IGMP Snooping {#igmp-snooping}

[**IGMP Snooping**](../../interface_guide/igmp_snooping.md)チュートリアルを参照してください。

---

## システム {#system}

### 概要 {#overview}

[**システム概要**](../../interface_guide/system_overview.md)チュートリアルを参照してください。

### アップグレード {#upgrade}

GL.iNetは、パフォーマンスの向上、バグの修正、脆弱性への対処のため、ルーターのファームウェアを定期的に更新しています。

[**アップグレード**](../../interface_guide/upgrade.md)チュートリアルを参照してください。

### OLED画面設定 {#oled-screen-settings}

このページでは、Mudi V2 (GL-E750V2) のOLED画面に表示される情報を調整できます。

### スケジュールタスク {#scheduled-tasks}

[**スケジュールタスク**](../../interface_guide/scheduled_tasks.md)チュートリアルを参照してください。

### 管理者パスワード {#admin-password}

この機能はv4.5以降[**セキュリティ**](../../interface_guide/security.md)に移動しました。

[**管理者パスワード**](../../interface_guide/admin_password.md)チュートリアルを参照してください。

### タイムゾーン {#time-zone}

[**タイムゾーン**](../../interface_guide/time_zone.md)チュートリアルを参照してください。

### トグルボタン設定 {#toggle-button-settings}

[**トグルボタン設定**](../../interface_guide/toggle_button_settings.md)チュートリアルを参照してください。

### ログ {#log}

[**ログ**](../../interface_guide/log.md)チュートリアルを参照してください。

### ファームウェアリセット {#reset-firmware}

[**ファームウェアリセット**](../../interface_guide/reset_firmware.md)チュートリアルを参照してください。

### 詳細設定 {#advanced-settings}

[**詳細設定**](../../interface_guide/advanced_settings.md)チュートリアルを参照してください。
