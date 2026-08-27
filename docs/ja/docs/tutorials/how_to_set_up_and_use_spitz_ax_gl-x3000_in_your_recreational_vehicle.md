# RVでSpitz AX (GL-X3000) をセットアップして使用する方法

このガイドでは、RVでSpitz AXをセットアップして使用する方法を説明します。開始前に、必要に応じて以下の追加機器やサービスを準備してください。

- 使用するインターネット接続方法に応じて、SIMカードまたはテザリング用のUSBケーブル。SIMカードを使用する場合は、通信事業者にAPNを確認してください。
- より広い通信範囲が必要な場合は、ルーフアンテナ。
- セルラー通信圏外の場所へ行く場合は、[Starlinkのサブスクリプション](https://www.starlink.com/roam)。

---

## 1. Spitz AXとその他の機器を設置する

出発前に、以下の手順に従ってSpitz AXを設置してください。

### 手順1: Spitz AXの設置場所を選ぶ

通信範囲を最大限に確保するため、中央に近く、遮るもののない場所を選ぶことを推奨します。電源アダプターのケーブル長は 1 メートルなので、設置場所が電源から 1 メートル以内であることを確認してください。

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Spitz AXは平らな場所に置くことも、壁に取り付けることもできます。壁に取り付ける場合は、次の手順に進んでください。

### （任意）手順2: Spitz AXを壁に取り付ける

Spitz AXを壁に取り付ける方法は2つあります:
- 付属の粘着パッドを使う
- 壁面取付用マウントを使う

壁面取付用マウントはパッケージに同梱されています。Spitz AXを壁に取り付けるには、以下の手順に従ってください。

1. 壁にネジでマウントを取り付けます。
2. Spitz AXをマウントにはめ込みます。

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### （任意）手順3: RV用ルーフアンテナを取り付ける

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

より良い信号を得るには、Spitz AXにルーフアンテナを使用してください。最適なネットワーク信号を得るため、[MobileMark's LTMG942 multi-band antenna](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/) の使用を推奨します。他社製のルーフアンテナを使用する場合は、以下の要件を満たしていることを確認してください。

- セルラーアンテナ 4 本、受信周波数範囲 600M~6GHz。
- Wi-Fiアンテナ 2 本、受信周波数範囲: 2.4G~2.5GHz、5.15~5.84GHz

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Note:** GPSアンテナを含む 7-in-1 アンテナも使用できますが、Spitz AXに接続する必要があるのは6本のアンテナだけです。Spitz AXのDIV/GNSSインターフェースは、セルラーアンテナ（受信周波数 600M~6GHz）がGPSの周波数帯もカバーしているため、GPS信号に対応しています。Spitz AXはコマンドラインでGPS位置情報を確認できますが、現時点では地図上への表示には対応していません。

信号の減衰を避けるため、ルーフアンテナからSpitz AXまでの高周波ケーブルは 5 メートルを超えないようにしてください。（たとえば、MobileMarkの高周波ケーブルが 5 メートルの場合、3000MHz における受信信号は 3dB 低下し、信号強度は半分になります。信号の周波数が高いほど、減衰も大きくなります。）

[Spitz AXのアンテナ交換方法はこちらをご覧ください。](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/)

---

## 2. Spitz AXのインターネットを設定する

移動中もインターネットへ接続できるように、SIMカードを使ってインターネットを設定してください。

Spitz AXには5GNRモジュールが内蔵されており、デュアルSIMカードに対応しています。モバイル通信事業者によってSIMカード向けの通信プランやAPNが異なります。設定でAPNを入力する必要があるため、通信事業者にAPNを確認してください。

SIMカードを設定するには、以下の手順に従ってください。

1. SIMカードを挿入します。
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. 電源アダプターを接続し、ルーターの電源を入れます。

APNを入力するには、以下の手順に従ってください。

1. Webブラウザーで `192.168.8.1` を入力し、サインインします。
2. 左上に通信事業者名が表示されます。**Manual Setup** をクリックします。
3. **APN** の横にAPNを入力します。
4. **Apply** をクリックします。

2枚のSIMカードを使用する場合でも、同時に動作するのは1枚だけです。その都度、使用するSIMカードを手動で選択できます。あるいは、[Auto Switch feature](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models) を有効にしてください。ルーターが一方のSIMカードでインターネットに正常にアクセスできないことを検知すると、もう一方のSIMカードへ自動的に切り替わります。切り替えには約 1 分かかります。

---

## 3. さまざまなシナリオでSpitz AXを使う

### 移動中

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

走行中は、前の手順で設定したSIMカードを使ってインターネットに接続できます。

### キャンプ場

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

旅行中にキャンプ場へ立ち寄った場合は、施設が提供する公衆Wi-Fiネットワークを利用してセルラーデータの消費を抑えられます。[既存のWi-Fiネットワークへの接続方法はこちら。](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/)

一度Wi-Fiネットワークに接続すると、Spitz AXはネットワーク名とパスワードを記憶します。次にその場所の近くへ行ったとき、自動的に接続されます。

### セルラー圏外のエリア

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

セルラー通信圏外の場所（たとえば人口の少ない砂漠地帯）を走行する場合は、衛星インターネットサービスのStarlinkを使用してください。このように、セルラー通信が良好な場所ではSpitz AXが受信した 5G 信号を使い、セルラー通信圏外ではStarlinkを使用できます。

Starlinkアンテナを設置するときは、周囲に遮るものがないことを確認してください。道路の両側にある障害物（たとえば木）は受信に影響するため、できるだけ障害物のない場所に駐車してください。

---

## 4. フェイルオーバーの優先順位を設定する
Spitz AXはmulti-WAN（フェイルオーバーとロードバランシング）に対応しています。利用シーンに応じて、各ネットワークのフェイルオーバー優先順位を設定できます。

| Scenario| Priority |
| --------| ------- |
| キャンプ場（repeater を使ってそのWi-Fiネットワークに接続）    | <p> Cellular より repeater の優先順位を高く設定します。</p> <p>キャンプ場を離れると、ルーターは自動的に Cellular に切り替わります。</p>|
| Starlink (ethernet) + cellular | Cellular の優先順位を ethernet より高く設定します。 <p>セルラー通信圏内では、ルーターは cellular ネットワークを使用します。</p> <p>セルラー通信圏外に入ると、ルーターは自動的に ethernet 経由のStarlinkへ切り替わります。</p>|

フェイルオーバーを設定するには、[Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/) を参照してください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
