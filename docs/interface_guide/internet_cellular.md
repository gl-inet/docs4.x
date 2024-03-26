# セルラー経由でインターネットに接続

ルーターは、セルラー経由でインターネットにアクセスすることができます。

3つのケースがあります：

1. GL-XE300(Puli) のように、一部のモデルには1 枚の SIM カードを備えた 3G/4G モデルが内蔵されています。[シングルSIMモデルの設定方法](#setup-for-single-sim-models)をご覧ください。

2. 一部のモデルにはUSB ポートがあり、GL-AXT1800(Slate AX) などは USB 3G/4G モデムに接続できます。 [シングルSIMモデルの設定方法](#setup-for-single-sim-models)をご覧ください。

3. GL-X3000(Spitz AX)のようにモデムを内蔵し、デュアルSIMカードをサポートするモデルもあります。インターフェイスが若干異なる場合があります。 [デュアルSIMモデルの設定方法](#setup-for-dual-sim-models)をご覧ください。

**注意:** 一部の SIM カードは初めて使用するときにアクティベートする必要がある場合があるため、ルーターで使用する前にスマートフォンでアクティベートしてください。

## シングルSIMモデルの設定

以下の設定手順は、一枚のみのSIMカードで内蔵モデムまたは外付けUSBモデムを使用する場合です。ここでは、GL-AXT1800（Slate AX）と外付けUSBモデムを例に説明します。

管理画面の左側 → インターネット→セルラー

1. まずルーターの電源を切り、SIMカードをUSBモデムに挿入してから、USBモデムをルーターのUSBポートに接続し、再度電源を入れるようにしてください。電源を入れた状態でUSBモデムを差し込むと、ページが変わらない可能性がありますので、ページをリフレッシュしてください。

2. 管理パネル->インターネット、セルラーのセクションにアクセスしてください。初回は自動的に接続されないかもしれませんが、左上のキャリア名とIMEIを読み込んだ後、**自動セットアップ**をクリックしてください。

    *互換性のないモデム* の警告は無視してください。

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

3. 接続

    **注意:** 一部の SIM カードには、特別な APN を使用する必要があるなど、特別な使用制限が設けられている場合があります。 SIM カードが登録できない場合、特別な制限がある場合は通信事業者にお問い合わせください。

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

4. しばらくすると接続されます。それ以外の場合は、[手動セットアップ](#manual-setup)をお試しください。

    usbモデムをルーターに接続して2回目に電源を入れると、通常は自動的に認識され、接続が確立されます。信号、モデム名、IMEIの情報は取得できない場合があります。

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

---

### 手動セットアップ

**自動セットアップ**が機能しない場合があります。**手動セットアップ**を試してください。

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/cellular_settings.png){class="glboxshadow"}

---

### 互換性のあるモデム

以前にテストした、サポートされているモデムのリストを次に示します。

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel UC20-E                         | 3G    | Yes    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Yes    | GL.iNet         |           |
| Huawei E1550                           | 3G    | Yes    | GL.iNet         |           |
| Huawei E3276                           | 4G    | Yes    | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G    | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Yes    | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Yes    | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Yes    |                 | Host-less |

*QMI: このモデムは QMI モードをサポートします。 **デバイス** リストで **/dev/cdc-wdm0** を選択してください。

*Host-less: このモデムはテザリング モードをサポートしています。3G/4G モデムではなく、テザリングを使用してセットアップしてください。

また、 [forum](https://forum.gl-inet.com){target="_blank"} で検索するか、質問を投稿することもできます。

## デュアルSIMモデルのセットアップ

一部のモデルはモデムを内蔵しており、デュアル SIM カードをサポートしており、インターフェイスは 1 つの SIM カード モデルと比較して若干異なる場合があります。

ここではGL-X3000（スピッツAX）を例に挙げます。 「デュアル SIM、シングル スタンバイ」をサポートしています。つまり、インターネット アクセス用に 2 枚の SIM カードを保持できますが、一度にアクティブにできるのは 1 枚の SIM カードだけであり、ユーザーはそれらを切り替えることができます。

まずルーターの電源を切り、SIMカードをスロットに挿入してから電源を入れ直すようにしてください。

管理画面の左側 →インターネット→セルラーセクター

SIMカードが検出されない場合

![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

SIMカードが挿入されている場合

![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

### SIMカードスロットの設定

現在のSIMカードをクリックします。

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

SIMカードスロットの設定ダイアログボックスが表示されます。

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

SIM カードが 2 枚挿入されている場合は、自動切り替えを有効にすることができます。

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

**注意**: 自動切り替え機能は、別の SIM カードにすぐには切り替わりません。 一方で、現在のSIMカードがインターネットにアクセスできないことを確認するのに時間がかかり、それを確認して初めて切り替えられます。もう一方の SIM カードはスタンバイ状態ではないため、アクティベートするのにも時間がかかります。

* オートスイッチ

    The Internet status is detected in the same way as the settings in the Multi-WAN page.

* フェイルオーバー間隔

    フェイルオーバー後にインターネット接続がまだ利用可能でない場合、デバイスは優先SIMスロットに切り替わり、この間隔の後にのみフェイルオーバーを再試行します。

    このオプションは、優先 SIM カードとバックアップ SIM カードの両方に信号がない場合に適用されます。 優先 SIM カードにも信号がない場合、デバイスはバックアップ SIM カードに切り替え、SIM カードの 1 つが信号を受信できるまで同様に切り替えます。

    ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/sim%20_card%20slot%20settings_failover%20interval.png){class="glboxshadow"}


* 優先スロットのスケジュール済みステータスの確認

    このオプションを有効にすると、デバイスは指定した時間に優先SIMスロットに切り替えようとします。これにより、インターネット接続が利用可能になったときに、優先SIMスロットの使用に切り替えることができます。

    この機能を有効にすると、デバイスは毎日この設定時間に優先 SIM への切り替えを試みます。たとえば、この機能はバックアップ SIM がデータを過剰に使用するのを防ぐことを目的としています。 優先 SIM にまだ信号がない場合は、バックアップ SIM への切り替えに失敗します。

    ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/sim%20_card%20slot%20settings_checking%20preferred%20slot%20status%20scheduled.png){class="glboxshadow"}

### トラフィック統計

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

### 手動セットアップ

**手動セットアップ**ボタンをクリックすると、セルラー設定ダイアログがポップアップします。

![cellular settings](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

現在の SIM カードのセルラー設定を表示または変更できます。また、事前に行った設定も保存され、手動で「保存された設定」に追加することもできます。

## SMS

 [SMSチュートリアル](sms.md)をご参照ください。

## SMSフォワーディング

[SMS フォワーディング・チュートリアル](../tutorials/sms_forwarding.md)をご参照ください。

## モデム管理

ボタンをクリックするとモデム管理ページに移動します。

![modem management button](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/modem_management_button.png){class="glboxshadow"}

モデムとATコマンドに関する情報が含まれています。

![modem management](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/modem_management.png){class="glboxshadow"}

モデム AT コマンドは、モデムを制御するために使用される命令です。

「ショートカット」オプションが「手動コマンド」として選択されている場合、「AT コマンド」フィールドに実行するコマンドを入力できます。

以下のATコマンドがあらかじめ設定されています。

* リクエストIMEI
* リクエストQCCID
* リクエストIMSI
* 信号品質のチェック
* モデムのリセット
* オペレーター名
* SIMカードのステータスをリクエスト

## キャリアプロファイル

同じキャリアまたは異なるキャリア用に異なるプロファイルを保存することができます。

プロファイル管理をクリックします

![manageprofile](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

新規プロファイルの追加または現在のプロファイルの保存

![addprofile](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

ニーズに合わせてキャリア独自のプロフィールを作成

![createprofile](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

保存したプロファイルは次回から選択できます

![selectprofile](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

必要なプロファイルを選択する

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## 信号塔のロック

信号塔ロックをクリックします。

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

利用可能な信号塔を選択し、ロックします

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

セルラーインターフェースを有効にすると、デバイスがすべてのタワーをスキャンできない場合があります。

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}


ロックされたタワーがセルラー設定のバンド・マスキングまたは APN パラメーターと一致しない場合、セルラー・イン ターフェースはインターネットに接続できません。

ここで、ロックのステータスを表示できます。

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}


## 過去の信号記録

GL-inet管理画面の左側で[インターネット]を選択し、右側のセルラーのセクションまでスクロールダウンし、アイコンをクリックしてポップアップ歴史信号値ウィンドウを表示することができます 

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

ルーターの信号強度をチェックすることで、インターネット接続の品質を判断することができます。インターネット接続の品質が悪い場合は、より良い信号を得るためにスイッチングを試すことができます。

異なる時間枠を選択することで、セルラーの電波強度履歴を表示できます。

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## バンドマスキング

**セル情報**の**詳細を見る**をクリックすると、バンド信号を確認できます。そうすれば、ルーターが必要な帯域にだけ接続したり、必要でない帯域には接続しないようにすることができます。

![cellinfo](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

**ブロック** または **オープン** にチェックを入れ、適用したいバンドについて以下から選択します。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

## 警告

インターネットにアクセスできない場合は、対応する警告が表示されます。インターネットにアクセスできるかどうかは、 [マルチWAN](multi-wan.md) のページをご覧ください。

- 警告： *インターフェースは接続されていますが、IPv4プロトコルでインターネットにアクセスできません。*

    解決方法：SIMカードがスマートフォンでインターネットに接続できるかどうかご確認ください。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット・アクセス方式を同時に使用する場合のロードバランスの設定方法は？](multi-wan.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
