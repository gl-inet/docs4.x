# レクリエーション車両で Spitz AX (GL-X3000) をセットアップおよび使用する方法

このガイドは、レクリエーション車両で Spitz AX をセットアップおよび使用する方法を示します。始める前に、以下の追加機器およびサービスを準備する必要があるかもしれません：

- 使用するインターネット接続方法に応じて、SIMカードまたはUSBケーブル（テザリング用）。SIMカードを使用する場合は、オペレーターにAPNを問い合わせてください。
- より良いカバレッジを得るための屋根アンテナ。
- 携帯電話カバレッジがないエリアに行く場合は、[Starlinkのサブスクリプション](https://www.starlink.com/roam)。

---

## 1. Spitz AX およびその他の機器をインストールする

旅を始める前に、以下の手順に従って Spitz AX をセットアップします。

### ステップ1: Spitz AX の設置場所を選ぶ

最大カバレッジのために中央で障害物のない場所を選ぶことをお勧めします。設置場所は電源から1メートル以内である必要があります。これは電源アダプターケーブルの長さです。

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Spitz AX を平らな面に置くことも、壁に取り付けることもできます。壁に取り付ける場合は、次のステップに従います。

### （オプション）ステップ2: Spitz AX を壁に取り付ける

Spitz AX を壁に取り付ける方法は2つあります：
- 付属の粘着パッドを使用する
- 壁取り付け具を使用する

パッケージには壁取り付け具が付属しています。Spitz AX を壁に取り付けるには、以下の手順に従います：

1. 取り付け具をネジで壁に取り付ける。
2. Spitz AX を取り付け具にスナップして取り付ける。

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### （オプション）ステップ3: RVの屋根アンテナを取り付ける

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

信号をより良くするために、Spitz AX に屋根アンテナを使用します。最適なネットワーク信号を提供する[MobileMarkのLTMG942マルチバンドアンテナ](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/)を使用することをお勧めします。他のブランドの屋根アンテナを使用する場合は、以下の要件を満たしていることを確認してください：

- 4つのセルラーアンテナ、受信周波数範囲600M～6GHz。
- 2つのWi-Fiアンテナ、受信周波数範囲：2.4G～2.5GHz、5.15～5.84GHz

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**注意:** 7-in-1アンテナ（GPSアンテナを含む）を使用することもできますが、Spitz AX には6つのアンテナのみを接続する必要があります。Spitz AX のDIV/GNSSインターフェースはGPS信号をサポートします。これはセルラーアンテナ（600M～6GHzの受信周波数）がGPSの周波数をカバーしているためです。Spitz AX はコマンドラインを使用してGPS位置を表示することをサポートしますが、現在地図上に位置を表示することはサポートしていません。

信号減衰を避けるために、屋根のアンテナから Spitz AX への高周波ケーブルは5メートルを超えないようにしてください。例えば、MobileMark 製の5メートルのケーブルは3000MHzでの信号受信を3dB減少させ、強度が半分になります。信号の周波数が高いほど、減衰が大きくなります。

[Spitz AX のアンテナを交換する方法を学ぶ。](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/)

---

### 2. Spitz AX のインターネット設定

旅行中にインターネットアクセスを確保するために、SIMカードを使用してインターネットを設定します。Spitz AX には 5GNR モジュールが内蔵されており、デュアル SIM カードをサポートしています。異なるモバイルネットワークキャリアは、SIMカード用に異なるセルラーパッケージを提供し、異なるAPNを使用します。設定にAPNを入力する必要があるため、オペレーターにVPNの確認をしてください。

#### SIMカードを設定する手順:

1. SIMカードを挿入します。
   ![SIMカードを挿入](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}

2. 電源アダプターを接続し、ルーターの電源を入れます。

#### APNを入力する手順:

1. ウェブブラウザに `192.168.8.1` を入力し、サインインします。
2. 左上にキャリアの名前が表示されます。**Manual Setup** をクリックします。
3. **APN** の横にAPNを入力します。
4. **Apply** をクリックします。

デュアル SIM カードを使用する場合、一度に動作するのは一つの SIM カードのみです。毎回手動で使用する SIM カードを選択するか、[自動切替機能](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models)を有効にします。ルーターが一つの SIM カードでインターネットにアクセスできないと検出した場合、自動的に他の SIM カードに切り替えます。切り替えには約1分かかります。

---

### 3. さまざまなシナリオで Spitz AX を使用

#### 道路上で

![道路上で](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

運転中は、前のステップで設定した SIM カードを使用してインターネットに接続できます。

#### キャンプ場で

![キャンプ場](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

旅行中にキャンプ場に停車した場合、サイトが提供する公共 Wi-Fi ネットワークを使用してセルラーデータを節約できます。[既存の Wi-Fi ネットワークに接続する方法を学ぶ。](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/)

一度 Wi-Fi ネットワークに接続すると、Spitz AX はネットワーク名とパスワードを記憶します。次回周辺にいるときに自動的に接続します。

![セルラー](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

セルラーカバー範囲外のエリア（例：人口の少ない砂漠地帯）に移動する場合は、衛星インターネットサービスであるStarlinkを使用してください。この方法では、セルラーカバー範囲が良好なエリアではSpitz AXの受信する5G信号を使用し、セルラーカバー範囲外のエリアではStarlinkを使用します。

Starlinkアンテナをセットアップする際は、遮るものがないことを確認してください。道路の両側の障害物（例：木々）が受信に影響するため、障害物から離れて駐車するようにしてください。

---

## 4. フェイルオーバーの優先順位を設定する
Spitz AXはマルチWAN（フェイルオーバーおよび負荷分散）をサポートしています。シナリオに基づいて異なるネットワークのフェイルオーバー優先順位を設定することができます。

| シナリオ| 優先順位 |
| --------| ------- |
| キャンプ場内（リピーターを使用してWi-Fiネットワークに接続） | <p> リピーターをセルラーより高い優先順位に設定します。</p> <p>キャンプ場を離れると、ルーターは自動的にセルラーに切り替わります。</p>|
| Starlink（イーサネット）+ セルラー | イーサネットよりセルラーを高い優先順位に設定します。 <p>セルラーカバー範囲のエリアでは、ルーターはセルラーネットワークを使用します。</p> <p>セルラーカバー範囲外のエリアに到達すると、ルーターは自動的にイーサネット経由でStarlinkに切り替わります。</p>|

フェイルオーバーの設定については、[フェイルオーバー](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/)セクションを参照してください。

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪問してください。