# Spitz AX (GL-X3000) をRVでセットアップして使う方法

このガイドでは、RVで Spitz AX をセットアップして使う方法を説明します。開始前に、必要に応じて以下の機材やサービスを準備してください。

- 利用するインターネット接続方法に応じた SIMカード、またはテザリング用のUSBケーブル
- より広い通信エリアを確保したい場合はルーフアンテナ
- セルラー通信圏外へ行く場合は [Starlink のサブスクリプション](https://www.starlink.com/roam){target="\_blank"}

SIMカードを使う場合は、事前に通信事業者へ APN を確認しておいてください。

---

## 1. Spitz AX と周辺機器を設置する

出発前に、以下の手順で Spitz AX を設置してください。

### Step 1: Spitz AX の設置場所を選ぶ

できるだけ通信範囲を広くするため、中央に近く、障害物の少ない場所へ設置することを推奨します。電源アダプターのケーブル長は 1 メートルなので、電源の近くに設置してください。

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Spitz AX は平らな場所に置くことも、壁面へ取り付けることもできます。壁面へ取り付ける場合は、次の手順へ進んでください。

### (Optional) Step 2: Spitz AX を壁に取り付ける

Spitz AX を壁に取り付ける方法は 2 通りあります。

- 付属の粘着パッドを使う
- 壁面取付用マウントを使う

パッケージには壁面取付用マウントが含まれています。壁に取り付ける場合は、以下の手順を実行してください。

1. ネジでマウントを壁に固定します。
2. Spitz AX をマウントにはめ込みます。

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Optional) Step 3: RV用ルーフアンテナを取り付ける

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

より良い受信状態を得るには、Spitz AX にルーフアンテナを接続してください。[MobileMark の LTMG942 multi-band antenna](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/){target="\_blank"} は最適なネットワーク受信性能を得やすいため、推奨されています。他社製のルーフアンテナを使う場合は、以下の要件を満たしていることを確認してください。

- セルラーアンテナ 4 本、受信周波数範囲 600M~6GHz
- Wi-Fi アンテナ 2 本、受信周波数範囲 2.4G~2.5GHz、5.15~5.84GHz

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Note**: GPSアンテナを含む 7-in-1 アンテナも使用できますが、Spitz AX に接続するのは 6 本のみです。Spitz AX の DIV/GNSS インターフェースは、セルラーアンテナの受信周波数範囲 600M~6GHz が GPS の周波数もカバーしているため、GPS信号に対応しています。Spitz AX はコマンドラインで GPS 位置情報を確認できますが、現時点では地図上への表示には対応していません。

信号減衰を避けるため、ルーフアンテナから Spitz AX までの高周波ケーブルは 5 メートル以内にしてください。たとえば MobileMark の 5 メートルケーブルでは、3000MHz の受信信号が 3dB 低下し、信号強度は半分になります。周波数が高いほど減衰も大きくなります。

[Spitz AX のアンテナ交換方法はこちらを参照してください。](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/){target="\_blank"}

---

## 2. Spitz AX のインターネット接続を設定する

移動中もインターネットへ接続できるように、まず SIMカードで通信を設定します。

Spitz AX には 5GNR モジュールが内蔵されており、デュアルSIMに対応しています。通信事業者によって利用できるプランや APN が異なるため、設定前に利用中の事業者へ APN を確認してください。

SIMカードを設定する手順は以下のとおりです。

1. SIMカードを挿入します。

   ![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}

2. 電源アダプターを接続し、ルーターの電源を入れます。

APN を入力するには、以下の手順を実行します。

1. Webブラウザーで `192.168.8.1` を開き、サインインします。
2. 左上に通信事業者名が表示されます。**Manual Setup** をクリックします。
3. **APN** の項目に APN を入力します。
4. **Apply** をクリックします。

デュアルSIMを使用している場合でも、同時に有効になるのは 1 枚だけです。都度手動で切り替えることもできますし、[Auto Switch 機能](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models){target="\_blank"} を有効にすることもできます。ルーターが一方の SIM で正常にインターネット接続できないと判断すると、もう一方の SIM に自動切り替えします。切り替えには約 1 分かかります。

---

## 3. シーン別に Spitz AX を使う

### 走行中

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

走行中は、前の手順で設定した SIMカードを使ってインターネットへ接続できます。

### キャンプ場

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

旅先のキャンプ場に滞在する場合は、施設が提供する公衆Wi-Fiへ接続してセルラーデータの消費を抑えられます。[既存のWi-Fiネットワークへ接続する方法はこちら。](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/){target="\_blank"}

一度 Wi-Fi ネットワークへ接続すると、Spitz AX はネットワーク名とパスワードを記憶します。次回その場所の近くへ行くと、自動的に再接続されます。

### セルラー通信圏外のエリア

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

セルラー通信圏外のエリア、たとえば人口の少ない砂漠地帯などへ行く場合は、衛星インターネットサービスの Starlink を利用してください。セルラー通信が良好なエリアでは Spitz AX が受信した 5G 信号を使い、セルラー通信が使えないエリアでは Starlink を使う運用ができます。

Starlink アンテナを設置するときは、遮るものがない場所を選んでください。道路脇の木などの障害物は受信に影響するため、できるだけ障害物から離れた場所へ駐車することを推奨します。

---

## 4. フェイルオーバーの優先順位を設定する

Spitz AX は multi-WAN をサポートしており、フェイルオーバーとロードバランシングを利用できます。利用シーンに応じて、各ネットワークのフェイルオーバー優先順位を設定してください。

| シナリオ                                                  | 優先順位                                                                                                                                                                                                                 |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| キャンプ場で Repeater を使って施設の Wi-Fi に接続する場合 | <p>Cellular より Repeater の優先順位を高く設定します。</p><p>キャンプ場を離れると、ルーターは自動的に Cellular へ切り替わります。</p>                                                                                    |
| Starlink（Ethernet）+ Cellular                            | <p>Ethernet より Cellular の優先順位を高く設定します。</p><p>セルラー通信圏内では、ルーターは Cellular を使用します。</p><p>セルラー通信圏外へ入ると、ルーターは自動的に Ethernet 経由の Starlink へ切り替わります。</p> |

フェイルオーバーの設定方法は、[Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/){target="\_blank"} を参照してください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
