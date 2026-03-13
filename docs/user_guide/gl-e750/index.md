# Mudi V2 (GL-E750V2) ユーザーガイド

**注意：** Mudi V2 (GL-E750V2) と Mudi (GL-E750) は same じファームウェアで動作します。Mudi (GL-E750) を使用している場合、最も新の機できるとを使用するには[ファームウェアをアップグレード](https://dl.gl-inet.com/?model=e750)してください。

## 製品概要

Mudi V2 (GL-E750V2) は、世界中の通信事業者に対応する便携式4G LTE旅行用ルーターです。OpenWrtとGL.iNetのSDK 4.0で完全にオープンソースで動作し、カスタマイズ機できると一组の機できるを提供します。Mudi V2 (GL-E750V2) は300Mbps (2.4GHz) と433Mbps (5GHz) のWi-Fi速度をサポートし、最も大1TBのMicroSDカードをサポートします。7000mAhの内蔵バッテリーがあります。また、すべての機器のためのスムーズな接続を確保するためにMulti-WAN（フェイルオーバーとロードバランス）をサポートします。

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

## ボタン

- 電源ボタンを**3秒間押す**：デバイスの電源を入れる

- 電源ボタンを**3〜5秒間押す**：スタンバイモードに入る

- 電源ボタンを**5秒で上押す**：デバイスの電源を切る

    （3秒間押すと、OLED画面に「Standby Mode On」が最も初に表示されます。「Shut Down」が「Standby Mode On」の下に表示されるまで電源ボタンを押し続けてください。3秒のカウントダウンがあり、デバイスの電源が切れます。）

## スタンバイモード

スタンバイモードでは、Mudi V2 (GL-E750V2) は電力を節約するためにWi-Fiと4Gをオフにします。このモードではMudi V2 (GL-E750V2) に接続できません。

スタンバイモードをオンまたはオフにするには、電源ボタンを3秒間押します。OLED画面に「Standby Mode On」または「Standby Mode Off」が表示されます。

## パッケージコンテンツ

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Mudi V2 (GL-E750V2) 便携式4G LTEルーター
- 1 x 電源アダプター
- 4 x コンバーター（米国、EU、英国、オーストラリアプラグ）
- 1 X ユーザーマニュアル
- 1 x 保証カード
- 1 x Ethernetケーブル
- 1 x USB-Cポートレプリケーター
- 1 x USB-C to USB-Cケーブル
- 1 x USB-A to USB-Cケーブル
- 1 x ポーチバッグ
- 1 x サンキューカード

---

## 初期設定

設定動画を見るか、手順に従ってMudi V2を設定します。

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. SIMカードを挿入

SIMカードとオプションのMicroSDカードをMudi V2 (GL-E750V2) に挿入します。

注意：SIMカードを使用する場合は、電源を入れる前にデバイスに挿入する必要があります。

1. Mudi V2 (GL-E750V2) の裏面にへけます。
2. ぶたの端の近く，指を穴に差し込みます。
3. 端に沿ってスライドします。
4. ぶたが少し（上から約25度から30度くらい）上がったら、引いて開きます。
5. 角の近くのシンボルの建議に従って，卡をカードスロットに挿入します。
6. ふたを押してカバーウェイプレートを閉じます。

### 2. 電源を入れる

電源ボタンを押してデバイスの電源を入れます。

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_power-on.png){class="glboxshadow"}

Mudi V2 (GL-E750V2) の電源が切れている場合でも、電源ボタンを押すとバッテリー状態を確認できます。电源ボタンを押すと，OLED画面にバッテリー状態が表示されます。

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_battery.png){class="glboxshadow"}

標準のな5V/2A電源アダプターを使用していることを確認してください。 そうでない場合は 故障が発生する可能性があります.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_charge.png){class="glboxshadow"}

---

## インターネット

ルーターWeb管理パネルにログインし，左侧メニューから**INTERNET**に移動します。

このページでは、Ethernet、Repeater、Tethering、Cellularなどのインターネット接続タイプを選択できます。

### Ethernet

アクティブなモデムまたはアクティブなネットワーク機器にEthernetケーブルを接続してインターネットにアクセスします。この方法は，通例，最も速で最もも信頼性の高いインターネット接続を提供します。

[Ethernetケーブルでインターネットに接続する方法についてはこれ里をクリック](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

ルーターをRepeaterとして設定して，既存のWi-FiネットワークのWi-Fi覆盖範囲を拡張します。Repeaterとして，范围内でWi-Fiシグナルを受信して再送信し therebyカバレッジを拡張します。この方法は，単一のリーターが全体个使用エリアを覆盖できない場合に便利です。

[既存のWi-Fiでインターネットに接続する方法についてはこれ里をクリック](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

ルーターUSBポートをUSBケーブルでアクティブなモバイルデータを持つスマートフォンに接続してインターネットにアクセスします。この方法により，ルーターに接続された複数の機器がスマートフォンのモバイルデータを使用してインターネットにアクセスできます。

[USBテザリングでインターネットに接続する方法についてはこれ里をクリック](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular

Mudi V2から背面カバーを外し，SIMカードをSIMカードスロットに挿入してインターネットに接続します。この方法は，単一のSIMカードからすべての接続機器にインターネットアクセスを共有するのに便利です。

[セルラーでインターネットに接続する方法についてはこれ里をクリック](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

GL.iNetルーターでeSIM物理カードを使用するには，ここをクリックしてください：[GL.iNetルーターでeSIM物理カードを使用する方法](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

---

## Wi-Fi

Wi-Fi設定では，侧面メニューから**WIRELESS**に移動して，プライマリWi-FiとGuest Wi-Fiのネットワークセキュリティを管理できます。

[Wi-Fi設定の詳細についてはこれ里をクリック](../../interface_guide/wireless.md)

---

## クライアント

クライアントはルーターに接続された機器で，クライアントをブロックしたり，ネットワーク速度を制限したりできます。インターフェースは，ルーター管理パネルの侧面メニューの**CLIENTS**をクリックしてアクセスできます。

[機器クライアントの管理の詳細についてはこれ里をクリック](../../interface_guide/clients.md)

---

## VPN

GL.iNetルーターにはOpenVPNとWireGuard®がプレインストールされており，30で上のVPNサービスをサポートします。接続されたネットワーク内のすべてのネットワークトラフィックをから動のに暗号化します（VPN暗号化を実行できないゲスト機器やクライアント機器を含む）。私たちのルーターはVPNサーバーとして機できるし，パブリックインターネットにアクセスする前に，リモートロケーションのクライアント機器からのトラフィックをVPNトンネルを経てVPNサーバーにリダイレクトできます。

### VPNダッシュボード

- [**VPNダッシュボード**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

段階のな設定ガイドについては，で下のリンクを参照してください：

- [**OpenVPNクライアントの設定**](../../interface_guide/openvpn_client.md)
- [**OpenVPNサーバーの設定**](../../interface_guide/openvpn_server.md)

### WireGuard

段階のな設定ガイドについては，で下のリンクを参照してください：

- [**WireGuardクライアントの設定**](../../interface_guide/wireguard_client.md)
- [**WireGuardサーバーの設定**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## アプリケーション

GL.iNetルーターには，機器管理をシンプル化し，ユーザーのインターネット体験をへ上させ，ファームウェアアップデートをから動化等機できるの幅広い追加機できるが含まれています。

### プラグイン

[**プラグイン**](../../interface_guide/plugins.md)チュートリアルを参照してください。

### Dynamic DNS

[**Dynamic DNS**](../../interface_guide/ddns.md)チュートリアルを参照してください。

### GoodCloud

[**GoodCloud**](../../interface_guide/cloud.md)チュートリアルを参照してください。

---

## ネットワーク

### ファイアウォール

GL.iNetルーターには，安全な接続とユーザーの完全な Oversight を确保するための複数のファイアウォール機できるが含まれています。Port Forwarding，Open Ports，DMZを含むファイアウォールルールを設定できます。

[GL.iNetルーターのファイアウォールの詳細についてはこれ里をクリック](../../interface_guide/firewall.md)

### Multi-WAN

[**Multi-WAN**](../../interface_guide/multi-wan.md)チュートリアルを参照してください。

### LAN

[**LAN**](../../interface_guide/lan.md)チュートリアルを参照してください。

### DNS

[**DNS**](../../interface_guide/dns.md)チュートリアルを参照してください。

### ネットワークモード

[**ネットワークモード**](../../interface_guide/network_mode.md)チュートリアルを参照してください。

### IPv6

[**IPv6**](../../interface_guide/ipv6.md)チュートリアルを参照してください。

### MACアドレス

Macアドレスページはで前はMac Cloneと呼ばれていましたが，v4.2で降Macアドレスに変よりされました。

[**MACアドレス**](../../interface_guide/mac_address.md)チュートリアルを参照してください。

### IGMP Snooping

[**IGMP Snooping**](../../interface_guide/igmp_snooping.md)チュートリアルを参照してください。

---

## システム

### 概要

[**システム概要**](../../interface_guide/system_overview.md)チュートリアルを参照してください。

### アップグレード

GL.iNetは，パフォーマンスをへ上させ，バグを解決し，脆弱性を修正するために，ルーターファームウェアの定期のアップデートを提供します。

[**アップグレード**](../../interface_guide/upgrade.md)チュートリアルを参照してください。

### OLED画面設定

このページでは，Mudi V2 (GL-E750V2) のOLED画面に表示される情報を調全体できます。

### スケジュールタスク

[**スケジュールタスク**](../../interface_guide/scheduled_tasks.md)チュートリアルを参照してください。

### 管理者パスワード

この機できるはv4.5で降[**セキュリティ**](../../interface_guide/security.md)に移りました。

[**管理者パスワード**](../../interface_guide/admin_password.md)チュートリアルを参照してください。

### タイムゾーン

[**タイムゾーン**](../../interface_guide/time_zone.md)チュートリアルを参照してください。

### トグルボタン設定

[**トグルボタン設定**](../../interface_guide/toggle_button_settings.md)チュートリアルを参照してください。

### ログ

[**ログ**](../../interface_guide/log.md)チュートリアルを参照してください。

### ファームウェアリセット

[**ファームウェアリセット**](../../interface_guide/reset_firmware.md)チュートリアルを参照してください。

### 高度設定

[**高度設定**](../../interface_guide/advanced_settings.md)チュートリアルを参照してください。
