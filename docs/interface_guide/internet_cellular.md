# セルラー経よりでインターネットに接続

!!! 注意

    このガイドはファームウェアv4.8に基づいています古いファームウェアを使用している場合は、[こちら](internet_cellular_v4.7.md)をご覧ください。

---

ほとんどのGL.iNetルーターはセルラー接続をサポートしています。このガイドでは3つのタイプのモデルについて説明します：

1. **内蔵4G シングルSIMモデル**

    一部のモデルには、GL-E750（Mudi）のように、単一のSIMカードスロットを備えた内蔵4Gモジュールが含まれています。[シングルSIMモデルの設定](#setup-for-single-sim-models)をご覧ください。

2. **内蔵5G デュアルSIMモデル**

    一部のモデルには、GL-X3000（Spitz AX）のように、2つのSIMカードスロットを備えた内蔵5Gモジュールが含まれています。Web管理パネルのセルラー設定は若干異なる場合があります。[デュアルSIMモデルの設定](#setup-for-dual-sim-models)をご覧ください。

3. **USBモデム対応モデル**

    一部のモデルには内蔵SIMカードスロットがなく、USBポートがあり、USBモデム経よりでセルラー接続をサポートしています（例：GL-MT3000（Beryl AX））。[USBモデム の設定](#setup-for-usb-modem)をご覧ください。

**注意:** 一部のSIMカードは初めて使用する前にアクティベートが必要です。互換性を確保するために、ルーターに差し込む前にスマートフォンでSIMカードをアクティベートしてください。

## シングルSIMモデルの設定

で下の手順は、内蔵セルラーモデムとシングルSIMカードスロットを持つモデルに適用します。

ここでは**GL-E750 (Mudi)**を例にします。

ルーターの電源を切ってアクティベート済みのSIMをスロットに差し込み、電源を入れることをお勧めします。ルーターが起動した後にSIMカードを差し込んだ場合、Web管理パネルはから動のにアップデートされない場合があります。その場合、ページをアップデートするか、ルーターを再起動してください。

### から動設定

ルーターのWeb管理パネルにログインし、**インターネット** → **セルラー**に移動します。

1. SIMカードが差し込まれていない場合、ページに「SIMカードが検出されていません」と表示されます。

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. SIMカードを差し込みます。で下のように接続が開始されます。

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    から動のに接続されない場合は、**接続**ボタンをクリックしてください。

    SIMカードが検出されない場合は、検出されるか確認するためにルーターを再起動してみてください。

3. セルラーネットワークが接続されると、ページに緑のドットと一緒にネットワークの詳細が表示され、接続が成功したことが示されます。
    
    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

から動設定が失敗した場合は、[手動設定](#manual-setup-single-sim)をお試ししください。

### 手動設定 {#manual-setup-single-sim}

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動し、**SIMカード設定**をクリックします。

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

現にのSIMカードのセルラー設定を表示または変よりできます。

**注意**: 一部のSIMカードは特定のAPNを必要とする場合があります。SIMカードが登録できない場合は、キャリアに確認して制限がないか確認してください。必要に応じてルーターで正しいAPNを設定してください。

変よりを適用すると再接続がトリガーされます。

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN（Access Point Name）は、セルラーネットワーク接続に必要なゲートウェイパラメータです。ルーターがモバイルキャリアが提供するインターネットに接続できるようになります。デフォルトのAPNを使用するか、キャリアから提供されたカスタムAPNを設定できます。

- **プロトコル**: セルラー通信プロトコル（例：3G、QMI、またはQCM）。これは通例から動検出され、変よりしてモデムとキャリアの要件に一致させることができます。

- **ポート**: セルラーモデムと通信するために使用されるシリアルポートです。これは通例から動検出され、手動調全体は必要ありません。

- **TTL**: TTL（Time To Live）は、パケットがネットワークで生存できる最も大時間を定義します。デフォルトでは、ルーターはクライアントデバイスからの着信パケットのTTLを1つ減らして転送します。上書きする必要がある場合は、ここで固定値を設定できます。TTL設定はIPv4のみ有効です。

- **HL**: IPv6では、HL（Hop Limit）はネットワーク内のデータパケットの転送ホップ数を制限し、IPv4のTTLと same 等の役割を果たします。

- **MTU**: デフォルトのMTU値は1500バイトです。

- **認証**: キャリア-required認証方法を選択してください（例：NONE、PAP、CHAP）。資格情報が必要ない場合は、通例NONEに設定されています。

- **バンドマスキング**: ルーターに特定のバンドをブロックさせたり、特定のセルラーバンドのみを使用させたい場合は、バンドマスキングを有効にできます。詳細については[こちら](#band-masking)をクリックしてください。

## デュアルSIMモデルの設定

で下の手順は、2つのSIMカードをサポートする内蔵セルラーモデルに適用します。ページはシングルSIMモデルと若干異なる場合があります。

ここでは**GL-X3000 (Spitz AX)**を例にします。デュアルSIM、シングルスタンバイをサポートしており、これは2枚のSIMカードを持っていますが、一度に1枚のSIMのみアクティブにできます。2枚のSIMカードを切り替えることができます。

まずルーターの電源を切り、アクティベート済みのSIMカードを下部に差し込んでから、電源を入れることをお勧め합니다。ルーターが起動した後にSIMカードを差し込んだ場合、Web管理パネルはから動のにアップデートされない場合があります。そのの場合は、ページをアップデートするかルーターを再起動してください。

### から動設定

ルーターのWeb管理パネルにログインし、**インターネット** → **セルラー**に移動します。

1. SIMカードが差し込まれていない場合、ページに「SIMカードが検出されていません」と表示されます。

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. SIMカードが差し込まれている場合、ページはで下のように表示されます。**接続**をクリックします。

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    SIMカードが検出されない場合は、検出されるか確認するためにルーターを再起動してみてください。

3. セルラーネットワークが接続されると、ページに緑のドットと一緒にネットワークの詳細が表示され、接続が成功したことが示されます。

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. **詳細情報を見る**をクリックして、モデムの詳細、SIMカードの詳細、インターネットの詳細、セルラーシグナルを含む詳細情報を表示します。

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

から動設定が失敗した場合は、[手動設定](#manual-setup-dual-sim)をお試ししください。

### 手動設定 {#manual-setup-dual-sim}

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動し、**SIMカード設定**をクリックします。

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

現にのSIMカードのセルラー設定を表示または変よりできます。

**注意**: 一部のSIMカードは特定のAPNを必要とする場合があります。SIMカードが登録できない場合は、キャリアに確認して制限がないか確認してください。必要に応じてルーターで正しいAPNを設定してください。

変よりを適用すると再接続がトリガーされます。

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN（Access Point Name）は、セルラーネットワーク接続に必要なゲートウェイパラメータです。ルーターがモバイルキャリアが提供するインターネットに接続できるようになります。デフォルトのAPNを使用するか、キャリアから提供されたカスタムAPNを設定できます。

- **プロトコル**: モデムとキャリアに基づくから動検出されたセルラー通信プロトコル（例：QMIまたはQCM）。

- **ポート**: セルラーモデムとの通信のためにから動検出されたシリアルポート。

- **TTL**: TTL（Time To Live）は、パケットがネットワークで生存できる最も大時間を定義します。デフォルトでは、ルーターはクライアントデバイスからの着信パケットのTTLを1つ減らして転送します。上書きする必要がある場合は、ここで固定値を設定できます。TTL設定はIPv4のみ有効です。

- **HL**: IPv6では、HL（Hop Limit）はネットワーク内のデータパケットの転送ホップ数を制限し、IPv4のTTLと same 等の役割を果たします。

- **MTU**: デフォルトのMTU値は1500バイトです。

- **認証**: キャリア-required認証方法を選択してください（例：NONE、PAP、CHAP）。資格情報が必要ない場合は、通例NONEに設定されています。

- **バンドマスキング**: ルーターに特定のバンドをブロックさせたり、特定のセルラーバンドのみを使用させたい場合は、バンドマスキングを有効にできます。詳細については[こちら](#band-masking)をクリックしてください。

### SIMカードスロット設定

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動し、**SIMカード切替**をクリックします。

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

から動切り替えボタン、アクティブなSIMカード、ICCIDとネットワークオペレーターが表示されます。

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

2枚のSIMカードが差し込まれている場合は、**から動切り替え**を有効にできます。

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **から動切り替え**: SIM 1とSIM 2のから動切り替えを有効にします。SIMから動切り替えのネットワーク検出方法は、Multi-WANページで設定されたものと same じです。

- **優先SIMカードスロット**: 優先するSIMカードをSIM 1また縦SIM 2に設定してください。

- **フェイルオーバー間隔**: 利用可できるな値は5分から24時間です。

    フェイルオーバー後もインターネット接続がまだ利用できない場合、デバイスは優先SIMスロットに切り替わり、この間隔后再びフェイルオーバーを再試行します。

    このオプションは、優先SIMカードとバックアップSIMカードの両方にシグナルがない場合に適用されます。デバイスは、SIMカードの1つが有効なシグナルを取なければならないするまで、SIMカード間を切り替え続けます。

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **優先スロットのステータスをスケジュールで確認**
    
    有効になっていると、デバイスは毎日設定された時刻に優先SIMスロットを確認し、優先SIMがインターネット接続を回復した場合は切り替えを試みます。
    
    これにより、バックアップSIMが 過剰なデータを消費することが防げます。優先SIMにまだシグナルがない場合、デバイ스는バックアップSIMの使用を続行します。

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**注意**: から動切り替え機できるは、別のSIMカードにすぐには切り替わりません。まず、デバイスは現にのSIMがインターネットにアクセスできないことを確認する時間が必要です。次に、彼のSIMはスタンバイモードではないため、アクティブ化するために時間が必要です。

## USBモデムの設定

で下の手順は、内蔵SIMカードスロットがないが、外部USBモデムを接続するためのUSBポートを持つモデルに適用します。

ここでは、外部USBモデム**SIMPoYo uFi**を備えた**GL-MT3000 (Beryl AX)**を例にします。

ルーターの電源を切り、SIMカードをUSBモデムに差し込み、モデムをルーターのUSBポートに接続し、ルーターの電源を入れることをお勧めします。ルーターが起動した後にUSBモデムを差し込んだ場合、Web管理パネルはから動のにアップデートされない場合があります。そのの場合は、ページをアップデートするかルーターを再起動してください。

### クイック設定

1. まずルーターの電源を切ります。SIMカードをUSBモデムに差し込み、モデムをルーターのUSBポートに接続し、ルーターの電源を入れます。

2. ルーターのWeb管理パネルにログインし、**インターネット** → **テザリング**に移動し、**接続**をクリックします。

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    高級設定（例：TTL、HL、MTU）を設定する必要がある場合は、**高級**をクリックしてカスタマイズし、**接続**をクリックします。

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    接続が開始されます。

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. 接続されると、ページに緑のドットと一緒にネットワークの詳細が表示され、接続が成功したことが示されます。
    
    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **注意:** 初期設定の後、USBモデムを接続した状態でルーターを再起動するか、モデムを抜き差しすると、から動のに認識され、接続ボタンを再度クリックせずにネットワーク接続が確立されます。

### 対応モデム

これはテスト済みの対応モデムのリストです。

**SIMPoYo uFi**は、Wi-Fiホットスポットを備えたコンパクトなPlug & Play USB dongleで、どこでも高速で信頼性の高い接続を実現するように設計されています。ほとんどのGL.iNetルーターだけでなく、ノートパソコン、モバイルバッテリー、車のUSBポート、およびその彼のUSB電源でも動作します。英国および34のヨーロッパ諸国で30日間有効な10GBの無料データが含まれています。

| モデル                                  | セルラー | テスト済 | テスト実施者     | 備考* |
| -------------------------------------- | -------- | ------ | --------------- | --------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)                        | 5G    | はい    | GL.iNet         |           |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/)               | 4G    | はい    | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G       | はい    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G       | はい    | GL.iNet         |           |
| Quectel EC200A series                  | 4G       | はい    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G       | はい    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G       | はい    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G       | はい    | akw2312         |           |
| Quectel RM520N-GL                      | 5G       | はい    | akw2312         |           |
| Quectel UC20-E                         | 3G       | はい    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G       | はい    | GL.iNet         |           |
| Huawei E1550                           | 3G       | はい    | GL.iNet         |           |
| Huawei E3276                           | 4G       | はい    | GL.iNet         |           |
| Huawei E3372                           | 4G       | はい    | anonymous       |           |
| Huawei E3372h-320 (Ukraine)            | 4G       | はい    | anonymous       | Host-less |
| TP-Link MA260                          | 3G       | はい    | GL.iNet         |           |
| ZTE M823                               | 4G       | はい    | Arnas Risqianto |           |
| ZTE MF190                              | 3G       | はい    | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)             | 4G       | はい    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G       | はい    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G       | はい    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G       | はい    | anonymous       | Host-less |

- **QMI**: このモデムはQMIモードをサポートしています。SIMカード設定で、セルラー通信プロトコルとしてQMIを、シリアルポートとして**/dev/cdc-wdm0**を選択してください。

- **Host-less**: このモデムはテザリングモードをサポートしています。接続はルーターのテザリングインターフェース経よりで管理してください。セルラーインターフェース経よりではありません。

## トラフィック統計

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動し、**使用データ**をクリックします。

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

トラフィック統計ページが表示されます。SIMカードの使用データが表示され、データ制限設定を提供します。

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

使用量がデータ上限を超える場合は、**データ上限**または**使用データ**を手動で変よりしてください。そのそうでなければ、ネットワークが切断されるか、SIMカードがから動切り替えされる可できる性があります（デュアルSIMモデルの場合）。

- **使用データを変より**

    SIM 1/2の使用データの右側にある**変より**をクリックします。

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    次に使用データを変よりまたはリセットできます。

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **SIMデータ制限を設定**

    SIMデータ制限を設定したい場合は、まず**電源オフ時にデータを保存**を有効にします。これはデバイスの電源がオフになった後でもデータを保存できることを意味します。

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    次にSIM 1またはSIM 2の制限設定を有効にします。

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Dual-SIMモデルでは、 same 時に**SIMカードスロットから動切り替え**を有効にすることをお勧めします。SIM 1のデータ上限が設定されており、SIMカードスロットから動切り替えが有効な場合、SIM 1はデータ量がデータ上限を超えるとから動のにSIM 2に切り替わり、SIM 1は無効になります。

## 履歴シグナル記録

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動し、**履歴シグナル記録**をクリックします。

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

ここでセルラー接続の品質を確認できます。シグナルが弱い場合は、より良いシグナルをなければならないるために基に局の切り替えを試してください。

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

右上隅で異なる時間範囲を選択して、シグナル強度の履歴を表示します。

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## バンドマスキング

バンドマスキングを使用すると、特定のバンドをブロックしたり、優先するセルラーバンドのみを使用して弱いセルラーシグナルを改善できます。

ルーターのWeb管理パネルで、**インターネット** → **セルラー** → **SIMカード設定**に移動し、**バンドマスキングを有効にする**をオンにします。

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

**バンドマスキングモード**（ブロックまたはオープン）を選択し、LTEバンド、5G NSAバンド、5G SAバンドを選択します。

## SMS

[SMSチュートリアル](sms.md)をご覧ください。

## SMS転送

[SMS転送チュートリアル](../tutorials/sms_forwarding.md)をご覧ください。

## 基に局ロック

!!! 注意 "対応モデル"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus)はファームウェアver.4.7で降で本機できるをサポートしています。

高品質のシグナルを受信し安定したセルラー接続を確保するには、基に局ロックを試すことができます。

**注意:** ロックされた基に局は、キャリアとデバイスが サポート하는周波数バンドと一致している必要があります。一致しない場合、接続に失敗する可できる性があります。

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動します。右上の3時アイコンをクリックし、**基に局ロック**を選択します。

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

**スキャン**をクリックしてセルラーシグナル塔のスキャンを開始します。数分かかります。スキャン中はページをより新しないでください。

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

利用可できるな基に局が表示されます。

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

基に局をクリックして詳細を表示し、ロックします。

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**注意**:

1. セルラーインターフェースが有効な場合、デバイスはすべての基に局をスキャンできない場合があります。

2. ロックされた基に局がセルラー設定のバンドマスキングまたはAPNパラメータと一致しない場合、ルーターはセルラーネットワークに接続できません。

3. セルラー基に局をロックした後、ルーターを別の場所に移動しても、再起動後にロックされた基に局への接続を試み続けます。これにより、新しい場所でルーターがから動のにセルラーネットワークに接続できなくなる可できる性があります。この場合、現にのセルラー基に局のロックを解除するか、新しい基に局に手動でロックする必要があります。

## キャリアロック

この機できるはGL-X3000、GL-XE3000およびGL-X2000（ファームウェアver.4.8で降）でのみ利用可できるです。

特定のモバイルキャリアにロックすることで、ルーターはそのキャリアのネットワークのみを使用し、安定した接続を確保し、意図しないローミング費用を避けることができます。特にデバイスが彼の国のネットワークに接続する可できる性のある国境に域において重要です。

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動します。右上の3時アイコンをクリックし、**キャリアロック**を選択します。

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

3つのロックモードがあります:

- **から動**: 利用可できるなキャリアネットワークにから動のに接続します。
- **手動**: 特定のキャリアに手動でロックします。
- **手動-から動**: 手動ロックが失敗した場合、利用可できるなキャリアネットワークにから動のに切り替えます。

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## モデムATコマンド

モデムATコマンドは、セルラーメモデムと通信するために使用される標準のな指示です。この機できるを使用して、コマンドを送信し、モデムの状態を確認できます。

ルーターのWeb管理パネルで、**インターネット** → **セルラー**に移動します。右上の3時アイコンをクリックし、**モデムATコマンド**を選択します。

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

ATコマンドページが表示されます。

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

ショートカットが**手動コマンド**に設定されている場合、ATコマンドフィールドに希望するコマンドを入力できます。

ショートカットドロップダウンをクリックして、**プリセットコマンド**のリストから選択することもできます。

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

で下のコマンドがプリセットとして表示されます:

* IMEIリクエスト
* QCCIDリクエスト
* IMSIリクエスト
* シグナル品質チェック
* モデムリセット
* キャリア名
* SIMカード状態リクエスト

例として、ここではショートカット"IMEIリクエスト"が選択されています。**送信**をクリックすると、で下の結果が表示されます。

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

右下で、**デバッグ情報をエクスポート**をクリックして.jsonファイルをダウンロードできます。

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## トラブルシューティング

セルラー接続を確立できない場合は、で下のエラーメッセージをクリックして関連する解決策を確認してください。

??? 注意 "SIMカードなし / SIMカードが検出されていません"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    トラブルシューティングの提案をいくつかご紹介します。
    
    1. ページをより新し、数分待ってSIMカードが検出されるか確認してください。
    
    2. SIMカードが正しくインストールされていることを確認してください。SIMカードの切り欠きをカードスロットの相应するマークに合わせて、正しい挿入方へを確認してください。
    
    3. ルーターの電源を切り、SIMカードを抜いて差し直し、電源を入れ直してください。
    
    4. 可できるな場合は、別のSIMカードを試してみてください。

    問題が解決しない場合は、ログをダウンロードして[support@gl-inet.com](mailto:support@gl-inet.com)にお送りください。

??? 注意 "SIMカード未登録 / インターフェースは接続されているがインターネットにアクセスできません"

    この問題には2種類のエラーメッセージがあります:

    - SIMカード未登録

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - インターフェースは接続されているがインターネットにアクセスできません
    
        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    トラブルシューティングの提案をいくつかをご紹介します。

    1. ページをより新し、数分待ってエラーが消失するか確認してください。
    
    2. **切断**/**中止**をクリックし、**接続**をクリックして再接続を試みます。
    
    3. ルーターを再起動します。
    
    4. SIMカードのステータスを確認し、アクティブになっていることを確認してください。SIMカードをスマートフォンに挿入してテストし、有効なモバイルデータプランでインターネットに正常にアクセスできるか確認するか、ネットワークキャリアに確認してください。
    
    5. 一部のネットワークキャリアはネットワーク接続に3Gプロトコルが必要な場合があります。**SIMカード設定** → **プロトコル**に移動し、**3G**を選択して**適用**をクリックしてください。

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        デバイスはから動のに再接続します。接続が成功するか確認するために数分待ってください。

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        接続が成功すると、ページにはで下のように表示されます。

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}
    
    6. 一部のSIMカードには特別な使用制限がある場合があります（例：特定のAPNが必要）。SIMカードが登録できない場合は、キャリアに制限がないか確認してください。必要に応じて、**SIMカード設定** → **APN**に移動し、ルーターで正しいAPNを設定して**適用**をクリックしてください。

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}
    
    7. **もっと見る**をクリックしてセルラーシグナル強度を確認します。シグナルが弱い場合は、アテナントが正しくインストールされていることを確認してください。より良いシグナルを受信するために、ルーターを開けた障害物のない場所に移動してください。

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}
    
    8. **バンドマスキング**または**基に局ロック**が有効になっているか確認してください。有効になっている場合は、無効にして再接続を試みしてください。

    問題が解決しない場合は、ログをダウンロードして[support@gl-inet.com](mailto:support@gl-inet.com)にお送りください。

## IoT認証

### AT&T認証

リンク[AT&Tデバイス認証](https://iotdevices.att.com/certified-devices.aspx#)をクリックし、デバイス名を入力すると、見つけることができます。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile認証

リンク[T-Mobileデバイス認証](https://www.t-mobile.com/business/solutions/iot/device-certification)をクリックし、**フィルター**で5Gを選択すると、見つけることができます。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

相关文章

- [互联网ページ](internet.md)
- [各インターネットアクセス方式の優先度を設定する方法](multi-wan.md)
- [ same 時に複数のインターネットアクセス方式を使用する場合の負荷分散設定方法](multi-wan.md)

---

还有その彼問題吗？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}までご連絡ください。
