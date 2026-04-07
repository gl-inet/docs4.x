# セルラーでインターネットに接続する（ファームウェア v4.7 以前）

**注意**: このガイドはファームウェア v4.7 以前に基づいています。新しいバージョンについては、[こちら](internet_cellular.md)を参照してください。

---

ほとんどの GL.iNet ルーターはセルラー接続に対応しています。このガイドでは、以下の3種類のモデルを説明します。

1. **4G シングル SIM 内蔵モデル**

    GL-XE300 (Puli) のように、4G モジュールと単一の SIM カードスロットを内蔵したモデルです。[シングル SIM モデルのセットアップ](#setup-for-single-sim-models) を参照してください。

2. **USB モデム対応モデル**

    GL-AXT1800 (Slate AX) のように USB ポートを備え、USB モデム経由でセルラー接続を利用できるモデルです。設定手順は 4G シングル SIM 内蔵モデルとほぼ同じです。[シングル SIM モデルのセットアップ](#setup-for-single-sim-models) を参照してください。

3. **5G デュアル SIM 内蔵モデル**

    GL-X3000 (Spitz AX) のように、5G モジュールと2つの SIM カードスロットを内蔵したモデルです。Web 管理パネル上のセルラー設定画面が少し異なる場合があります。[デュアル SIM モデルのセットアップ](#setup-for-dual-sim-models) を参照してください。

**注意:** 一部の SIM カードは初回使用前に有効化が必要です。互換性を確保するため、ルーターへ挿入する前にスマートフォンで SIM カードを有効化してください。

## シングル SIM モデルのセットアップ {#setup-for-single-sim-models}

以下の手順は、セルラーモデムと単一の SIM カードスロットを内蔵するモデル（例: GL-XE300 Puli）または外付け USB モデムを接続できる USB ポートを備えるモデル（例: GL-AXT1800 Slate AX）に適用されます。

ここでは、外付け USB モデムを接続した **GL-AXT1800 (Slate AX)** を例に説明します。

最初にルーターの電源を切り、事前に有効化した SIM カードを USB モデムへ挿入してから、モデムをルーターの USB ポートへ接続してください。その後、ルーターの電源を入れます。

ルーターの起動後に USB モデムを接続した場合、Web 管理パネルが自動更新されないことがあります。その場合はページを更新するか、ルーターを再起動してください。

### 自動セットアップ

ルーターの Web 管理パネルにログインし、**INTERNET** -> **Cellular** に移動します。

1. 初回アクセス時に自動接続されないことがありますが、左上には通信事業者名と IMEI が表示されるはずです。**Auto Setup** をクリックします。

    *Incompatible Modem* の警告は無視してください。

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. 接続が開始されます。

    **注意:** 一部の SIM カードには、特定の APN を必要とするなどの特別な利用制限があります。SIM カードが登録に失敗する場合は、制限がないか通信事業者へ確認してください。

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. 接続に成功すると、ページには緑のドットとともにネットワーク情報が表示されます。

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **注意:** 初回設定後は、USB モデムを接続したままルーターを再起動した場合や、モデムを挿し直した場合でも自動的に認識され、再度 Auto Setup ボタンを押さなくてもネットワーク接続が確立されます。

Auto Setup に失敗した場合は、[Manual Setup](#manual-setup) を試してください。

### 手動セットアップ {#manual-setup}

Cellular セクションで **Manual Setup** をクリックすると、現在の SIM カードのセルラー設定を確認または変更できます。

**注意**: 一部の SIM カードでは特定の APN が必要な場合があります。SIM カードがネットワーク登録に失敗する場合は、制限がないか通信事業者へ確認してください。必要に応じて、ルーター上で正しい APN を設定してください。

変更を適用すると、再接続が行われます。

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: セルラー通信プロトコル（3G、QMI、QCM など）です。通常は自動検出されますが、モデムや通信事業者の要件に合わせて変更できます。

- **Port**: セルラーモデムと通信するためのシリアルポートです。通常は自動検出されるため、手動調整は不要です。

- **APN**: APN（Access Point Name）はセルラーネットワーク接続に必要なゲートウェイパラメーターです。モバイル通信事業者が提供するインターネットへルーターを接続するために使われます。デフォルト APN を使うことも、通信事業者から提供されたカスタム APN を設定することもできます。

- **PIN**: SIM カードが PIN コードで保護されている場合は、ここに入力します。PIN を設定していない場合、この項目は任意です。

- **TTL**: TTL（Time To Live）は、パケットがネットワーク内で生存できる最大時間を定義します。デフォルトでは、ルーターはクライアントデバイスから受信したパケットを転送する前に TTL を 1 減算します。上書きが必要な場合は、ここで固定値を設定できます。TTL 設定は IPv4 でのみ有効です。

- **Service**: モデムが使用するネットワーク技術を定義するため、セルラーサービス種別を選択します。

- **Dial Number**: 通信事業者から提供されたダイヤル番号を入力します。多くの場合は事前設定済みで、最新のネットワークでは空欄のままで問題ありません。

- **Authentication**: 通信事業者が要求する認証方式（NONE、PAP、CHAP など）を選択します。認証情報が不要な場合は通常 NONE のままです。

### 対応モデム

これまでにテスト済みの対応モデム一覧です。

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | Yes    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | Yes    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Yes    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Yes    | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | Yes    | akw2312         |           |
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
| Verizon U620L (Verizon)                | 4G    | Yes    | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | Yes    | anonymous       | Host-less |

- **QMI**: このモデムは QMI モードに対応しています。セルラールーターでは、プロトコルに QMI、シリアルポートに **/dev/cdc-wdm0** を選択してください。

- **Host-less**: このモデムは Tethering モードに対応しています。Cellular インターフェースではなく、ルーターの Tethering インターフェースから接続を管理してください。

## デュアル SIM モデルのセットアップ {#setup-for-dual-sim-models}

以下の手順は、デュアル SIM をサポートするセルラーモデムを内蔵したモデルに適用されます。Web 管理パネルはシングル SIM モデルと若干異なる場合があります。

ここでは **GL-X3000 (Spitz AX)** を例に説明します。このモデルは Dual SIM, Single Standby に対応しており、セルラー接続用に2枚の SIM カードを挿入できますが、同時にアクティブにできる SIM カードは1枚だけです。2枚の SIM カードは手動で切り替えられます。

最初にルーターの電源を切り、事前に有効化した SIM カードをスロットへ挿入してから電源を入れることをおすすめします。ルーターの起動後に SIM カードを挿入すると、Web 管理パネルが自動更新されない場合があります。その場合はページを更新するか、ルーターを再起動してください。

### 自動セットアップ

ルーターの Web 管理パネルにログインし、**INTERNET** -> **Cellular** に移動します。

1. SIM カードが挿入されていない場合、ページは次のように表示されます。

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. SIM カードを挿入すると、ルーターは自動的に接続を開始します。

    接続に成功すると、ページは次のように表示されます。

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

自動的に接続されない場合は、**Auto Setup** をクリックして接続を待つか、**Manual Setup** を試してください。

### 手動セットアップ

Cellular セクションで **Manual Setup** をクリックして Cellular Settings に入ります。

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

現在の SIM カードのセルラー設定を確認または変更できます。また、いくつかの事前設定済みプロファイルも保存されており、"Saved Settings" に手動で設定を追加することもできます。

### SIMカードスロット設定

Cellular セクションで **Current SIM Card** をクリックします。

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

**SIM Card Slot Settings** に入ります。

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

SIM カードを2枚挿入している場合は、**Auto Switch** を有効にできます。

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

- **Auto Switch**: SIM 1 と SIM 2 を自動で切り替えます。SIM Auto Switch のネットワーク検出方式は、Multi-WAN ページで設定するものと同じです。

- **Preferred SIM Card Slot**: 優先して使用する SIM カードを SIM 1 または SIM 2 に設定します。

- **Failover Interval**: 5 分から 24 時間まで設定できます。

    フェイルオーバー後もインターネット接続が利用できない場合、デバイスは優先 SIM スロットに戻り、この間隔だけ待機してから再度フェイルオーバーを試みます。

    このオプションは、優先 SIM カードとバックアップ SIM カードの両方に信号がない場合に適用されます。どちらかが有効な信号を取得するまで、デバイスは SIM カードを切り替え続けます。

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    有効にすると、デバイスは毎日設定した時刻に優先 SIM スロットを確認し、優先 SIM が再びインターネットへ接続できる状態になっていれば自動で戻します。

    これにより、バックアップ SIM のデータ消費が過剰になるのを防げます。優先 SIM に引き続き信号がない場合は、バックアップ SIM の使用が継続されます。

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**注意**: Auto Switch 機能は、すぐに別の SIM カードへ切り替わるわけではありません。まず、現在の SIM でインターネットに接続できないことを確認する時間が必要です。さらに、もう一方の SIM はスタンバイ状態ではないため、有効化にも時間がかかります。

## トラフィック統計

Cellular セクションで **Traffic Statistics** をクリックします。

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Traffic Statistics ページが開きます。

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

[SMS チュートリアル](sms.md) を参照してください。

## SMS転送

[SMS Forwarding チュートリアル](../tutorials/sms_forwarding.md) を参照してください。

## モデム管理

Cellular セクションで、右上の **Tool** ボタンをクリックすると Modem Management ページに移動します。

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

このページには **Modem Info** と **AT Command** の2つのセクションがあります。

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

AT コマンドは、セルラーモデムと通信するための標準命令です。

Shortcut が **Manual command** に設定されている場合は、AT Command フィールドに任意のコマンドを入力してモデムの状態を確認できます。

Shortcut のドロップダウンをクリックすると、**preset commands** の一覧から選択することもできます。

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

プリセットとして利用できるコマンドは次のとおりです。

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

例として、ここではショートカット "Request IMEI" を選択しています。"Send" をクリックすると、以下のような結果が表示されます。

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## キャリアプロファイル

同じ通信事業者用でも別の通信事業者用でも、複数のプロファイルを保存できます。

Cellular セクションで、右上の **Profile** ボタンをクリックするとプロファイルを管理できます。

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

新しいプロファイルを追加することも、現在のプロファイルを保存することもできます。

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

通信事業者の要件に応じて独自のプロファイルを作成します。

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

次回以降は、保存したプロファイルを選択できます。

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

必要なプロファイルを選択してください。

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## 基地局ロック

この機能は GL-X3000、GL-XE3000、および GL-X2000（ファームウェア ver.4.7 以降）でのみ利用できます。

より高品質な信号を受信し、安定したセルラー接続を確保したい場合は、基地局ロックを試すことができます。

**注意:** ロックする基地局は、通信事業者とデバイスがサポートする周波数帯に一致している必要があります。一致しない場合、接続に失敗する可能性があります。

Cellular セクションで、右上の **Tower** アイコンをクリックします。

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

利用可能な基地局が表示されます。

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

基地局をクリックすると詳細を確認し、その基地局にロックできます。

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

上部に基地局の状態（Locked/Unlocked など）が表示されます。

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**注意**:

1. Cellular インターフェースが有効な状態では、すべての基地局をスキャンできない場合があります。

2. ロックした基地局が、セルラー設定内の Band Masking や APN パラメーターと一致しない場合、ルーターはセルラーネットワークへ接続できません。

3. 基地局をロックした後にルーターを別の場所へ移動すると、再起動後も以前ロックした基地局への再接続を試みます。その結果、新しい場所でセルラーネットワークへ自動接続できない場合があります。この場合は、現在の基地局ロックを解除するか、新しい基地局へ手動でロックし直してください。

## 信号履歴

Cellular セクションで、右上の **Signal** アイコンをクリックすると、信号強度の履歴を確認できます。

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

これにより、セルラー接続の品質を判断できます。信号が弱い場合は、より良い信号を得るために基地局を切り替えてみてください。

期間を切り替えることで、セルラー信号強度の履歴を確認できます。

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## バンドマスキング

Cellular セクションで **View More** をクリックし、**Cells Info** を選択してセル情報の詳細を確認します。

現在使用しているバンドと、その信号状態が表示されます。

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

信号が弱い場合は、Band Masking を有効にして特定のバンドをブロックできます。逆に信号が良好な場合は、ルーターが特定のセルラーバンドのみを使用するよう制限することもできます。

**Manual Setup** をクリックして Cellular Settings ページに入り、**Band Masking** を有効にします。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

**Masking Mode**（Block または Open）を選択し、LTE Bands、5G NSA Bands、5G SA Bands を設定します。

## トラブルシューティング

セルラー接続を確立できない場合は、以下のエラーメッセージをクリックして該当する対処方法を確認してください。

??? note "No SIM / Your SIM card has not been detected"

    1. ページを更新し、数分待ってから SIM カードが検出されるか確認します。

    2. SIM カードが正しく装着されていることを確認します。SIM カードの切り欠きがスロットのマークと一致しているか確認してください。

    3. ルーターの電源を切り、SIM カードを抜き差ししてから再度電源を入れます。

    4. 利用可能であれば、別の SIM カードでも試してください。

    問題が解消しない場合は、ログをダウンロードして [support@gl-inet.com](mailto:support@gl-inet.com) へ送信してください。

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. ページを更新し、数分待ってエラーが消えるか確認します。

    2. **Disconnect**/**Abort** をクリックしてから **Connect** をクリックし、再接続を試します。

    3. ルーターを再起動します。

    4. SIM カードの状態を確認し、有効化されていることを確認します。SIM カードをスマートフォンに挿して、モバイルデータ通信プランが有効な状態で正常にインターネットへ接続できるかテストするか、通信事業者へ確認してください。

    5. 一部の通信事業者では、接続に 3G プロトコルが必要な場合があります。**Manual Setup** -> **Cellular Settings** -> **Protocol** に移動し、**3G** を選択して **Apply** をクリックしてください。

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        デバイスは自動的に再接続します。数分待って接続に成功するか確認してください。

    6. 一部の SIM カードには特別な利用制限（特定の APN が必要など）がある場合があります。SIM カードが登録に失敗する場合は、制限がないか通信事業者へ確認してください。

        必要に応じて、**Manual Setup** -> **Cellular Settings** -> **APN** に移動し、ルーター上で正しい APN を設定してから **Apply** をクリックしてください。

    7. **View More** をクリックして **Cells Info** を選択し、セルラー信号強度を確認します。信号が弱い場合は、アンテナが正しく取り付けられているか確認してください。より良い受信のため、ルーターを開けた障害物の少ない場所へ移動してください。

    8. **Band Masking** または **Lock Tower** が有効になっていないか確認します。有効な場合は機能を無効にして再接続を試してください。

    問題が解消しない場合は、ログをダウンロードして [support@gl-inet.com](mailto:support@gl-inet.com) へ送信してください。

## IoT認証

### AT&T認証

リンク [att device certification](https://iotdevices.att.com/certified-devices.aspx#) を開き、デバイス名を入力すると確認できます。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile認証

リンク [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) を開き、**Filter** で 5G を選択すると確認できます。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}

---

関連記事

- [インターネットページ](internet.md)
- [各インターネット接続方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット接続方法を同時に使用する場合、ロードバランスをどのように設定しますか？](multi-wan.md)

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
