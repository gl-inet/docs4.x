# モバイルネットワーク経よりでインターネットに接続する（ファームウェア v4.7 で前）

!!! note

    このガイドはファームウェア v4.7 で前に基づいています。最も新のファームウェアバージョンを使用している場合は、[こちら](internet_cellular.md)をご覧ください。

---

GL.iNetルーターのほとんどはモバイルネットワーク接続をサポートしています。このガイドでは3つのタイプのモデルを説明します：

1. **内蔵4G シングルSIMモデル**

    一部のモデルには、GL-XE300 (Puli) など、内蔵の4GモジュールとSIMカードスロットが1つ搭載されています。[シングルSIMモデルのセットアップ](#セットアップ-for-single-sim-models)をご覧ください。

2. **USBモデム対応モデル**

    一部のモデルにはUSBポートがあり、USBモデム経よりでモバイルネットワーク接続をサポートします（例：GL-AXT1800 (Slate AX)）。セットアップ手順は、内蔵4G シングルSIMモデルと類似しています。[シングルSIMモデルのセットアップ](#セットアップ-for-single-sim-models)をご覧ください。

3. **内蔵5G デュアルSIMモデル**

    一部のモデルには、GL-X3000 (Spitz AX) など、内蔵の5GモジュールとSIMカードスロットが2つ搭載されています。Web管理パネルのモバイル設定は若干異なる場合があります。[デュアルSIMモデルのセットアップ](#セットアップ-for-dual-sim-models)をご覧ください。

**注意:** 一部のSIMカードには、使用前にアクティベートが必要な場合があります。互換性を確保するために、SIMカードをルーターに差し込む前にスマートフォンでアクティベートしてください。

## シングルSIMモデルのセットアップ

で下の手順は、内蔵モバイルモデムとSIMカードスロットが1つあるモデル（例：GL-XE300 Puli）、または外部USBモデムを接続するためのUSBポートがあるモデル（例：GL-AXT1800 Slate AX）に適用されます。

ここでは、外部USBモデムを使用した**GL-AXT1800 (Slate AX)**を例として使用します。

最も初にルーターの電源を切ることを推奨します。USBモデムに事前にアクティベートされたSIMカードを差し込み、それをルーターのUSBポートに挿してください。その後、ルーターの電源を入れてください。

ルーターが起動後にUSBモデムを挿した場合、Web管理パネルがから動のにアップデートされない場合があります。その場合は、ページをアップデートするか、ルーターを再起動してください。

### から動セットアップ

ルーターのWeb管理パネルにログインし、**インターネット** -> **モバイルネットワーク**に移動します。

1. 初めてアクセスした時時ではから動のに接続しない場合がありますが、左上に通信事業者の名前とIMEIが表示されます。**から動セットアップ**をクリックします。

    *非対応モデム*の警告は無視してください。

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. 接続を開始します。

    **注意:** 一部のSIMカードには、特定のAPNが必要な場合がありますなど特別な使用制限がある場合があります。SIMカードが登録できない場合は、通信事業者に特別な制限があるかどうかお問い合わせください。

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. 接続に成功すると、緑の時でネットワーク詳細がページに表示されます。

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **注意:** 初回セットアップ後、USBモデムを挿した状態でルーターを再起動するか、モデムを再度挿すと、USBモデムがから動のに認識され、から動セットアップボタンをクリックせずにネットワーク接続が確立されます。

から動セットアップに失敗した場合は、[手動セットアップ](#manual-setup)をお試しください。

### 手動セットアップ

モバイルネットワークセクションで、**手動セットアップ**をクリックして、現にのSIMカードのモバイル設定を表示または変よりします。

**注意:** 一部のSIMカードには特定のAPNが必要な場合があります。SIMカードが登録できない場合は、通信事業者に制限があるかどうかお問い合わせください。必要な場合は、ルーター上で正しいAPNを設定してください。

変よりを適用すると再接続がトリガーされます。

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **プロトコル**: モバイル通信プロトコル（例：3G、QMI、またはQCM）。これは通例から動検出されますが、モデムと通信事業者の要件に合わせて変よりできます。

- **ポート**: モバイルモデムと通信するために使用するシリアルポートです。これは通例から動検出されており、手動調全体は不要です。

- **APN**: APN（Access Point Name）は、モバイルネットワーク接続に必要なゲートウェイパラメータです。これにより、ルーターはモバイル通信事業者提供のインターネットに接続できます。デフォルトのAPNを使用するか、通信事業者提供のカスタムAPNを設定できます。

- **PIN**: SIMカードがPINコードで保護されている場合は、ここに入力します。PINが設定されていない場合は、このフィールドはオプションです。

- **TTL**: TTL（Time To Live）は、パケットがネットワークで生存できる最も大時間を定義します。デフォルトでは、ルーターはクライアントデバイスからの着信パケットのTTLを1減らして転送します。上書きする必要がある場合は、ここで固定値を設定できます。TTL設定はIPv4のみ有効です。

- **サービス**: モバイルサービスタイプを選択して、モデムが使用するネットワーク技術を定義します。

- **ダイヤル号码**: 通信事業者が提供するダイヤルアップ番号を入力します。これは事前に設定されていることが多くほとんどの近代のなネットワークでは空白のままにできます。

- **認証**: 通信事業者が必要とする認証方法を選択します（例：NONE、PAP、CHAP）。認証情報が必要ない場合は、通例NONEに設定されています。

### 対応モデム

で下是事前にテストした対応モデムの一覧です。

| モデル                                  | 3G/4G | テスト済み | テスト者          | コメント* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | はい    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | はい    | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | はい    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | はい    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | はい    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | はい    | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | はい    | akw2312         |           |
| Quectel UC20-E                         | 3G    | はい    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | はい    | GL.iNet         |           |
| Huawei E1550                           | 3G    | はい    | GL.iNet         |           |
| Huawei E3276                           | 4G    | はい    | GL.iNet         |           |
| TP-Link MA260                          | 3G    | はい    | GL.iNet         |           |
| ZTE M823                               | 4G    | はい    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | はい    | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | はい    | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | はい    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | はい    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | はい    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | はい    | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | はい    | anonymous       | Host-less |

- **QMI**: このモデムはQMIモードをサポートしています。プロトコルとしてQMIを選択し、モバイルルーターのシリアルポートとして**/dev/cdc-wdm0**を選択してください。

- **Host-less**: このモデムはテザリングモードをサポートしています。モバイルネットワークインターフェースではなく、ルーターのテザリングインターフェースで接続を管理してください。

## デュアルSIMモデルのセットアップ

で下の手順は、内蔵モバイルモデムがデュアルSIMカードをサポートするモデルに適用されます。Web管理パネルは、シングルSIMモデルと若干異なる場合があります。

ここでは、**GL-X3000 (Spitz AX)**を例として使用します。Dual SIM、Single Standbyをサポートしています，これは2枚のSIMカードを持っていますが、一度に1枚のSIMのみアクティブにできます。2枚のSIMカードを切り替えることができます。

最も初にルーターの電源を切ることを推奨します。事前にアクティベートされたSIMカードカードをスロットに差し込んでください。ルーターが起動後にSIMカードを差し込んだ場合、Web管理パネルがから動のにアップデートされない場合があります。その場合は、ページをアップデートするか、ルーターを再起動してください。

### から動セットアップ

ルーターのWeb管理パネルにログインし、**インターネット** -> **モバイルネットワーク**に移動します。

1. SIMカードが差し込まれていない場合、ページにはで下のように表示されます。

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. SIMカードを差し込むと、ルーターはから動のに接続を開始します。

    接続に成功すると、ページにはで下のように表示されます。

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

から動のに接続しない場合は、**から動セットアップ**をクリックしてルーターが接続するまで待機するか、**手動セットアップ**を試してください。

### 手動セットアップ

モバイルネットワークセクションで、**手動セットアップ**をクリックしてモバイル設定に入ります。

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

現にのSIMカードのモバイル設定を表示または変よりできます。また、いくつか事前に設定されたプロファイルが保存されており、「保存済み設定」に手動で設定を追加できます。

### SIMカードスロット設定

モバイルネットワークセクションで、**現にのSIMカード**をクリックします。

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

**SIMカードスロット設定**に入ります。

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

2枚のSIMカードが差し込まれている場合、**から動切り替え**を有効にできます。

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

- **から動切り替え**: SIM 1とSIM 2間のから動切り替えを有効にします。SIMから動切り替えのネットワーク検出方法は、Multi-WANページで設定されたものと same じです。

- **優先SIMカードスロット**: 優先するSIMカードをSIM 1またはSIM 2に設定してください。

- **フェイルオーバー間隔**: 利用可できるな値は5分から24時間です。

    フェイルオーバー後でもインターネット接続が利用できない場合、デバイスは優先SIMカードスロットに戻り、フェイルオーバーを再試行する前にこの間隔待機します。

    このオプションは、優先SIMカードとバックアップSIMカードのの両方がシグナルがない場合に適用されます。デバイスは、いずれかの有効なシグナルを取なければならないするまでSIMカードを切り替えます。

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **優先スロットステータス確認スケジュール**

    有効にすると、デバイスは毎日設定された時刻に優先SIMカードスロットを確認し、優先SIMがインターネットアクセスを回復した場合は切り替えを試みます。

    これにより、バックアップSIMカードのデータ消費を防ぎます。優先SIMがまだシグナルがない場合、デバイスはバックアップSIMの使用を継続します。

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**注意**: から動切り替え機できるは別のSIMカードにすぐに切り替わりません。まず、デバイスは現にのSIMがインターネットにアクセスできないことを確認する必要があります。第二に、別のSIMはスタンバイモードではなく、アクティブ化に時間が必要です。

## トラフィック統計

モバイルネットワークセクションで、**トラフィック統計**をクリックします。

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

トラフィック統計ページに入ります。

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

[SMSチュートリアル](sms.md)をご覧ください。

## SMS転送

[SMS転送チュートリアル](../tutorials/sms_forwarding.md)をご覧ください。

## モデム管理

モバイルネットワークセクションで、右上の**ツール**ボタンをクリックしてモデム管理ページに入ります。

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

**モデム情報**と**ATコマンド**の2つのセクションがあります。

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

ATコマンドは、モバイルモデムと通信するために使用される標準のな命令です。

ショートカットが**手動コマンド**に設定されている場合、ATコマンドフィールドに 원하는コマンドを入力してモデムの状態を確認できます。

ドロップダウンから**プリセットコマンド**のリストを選択することもできます。

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

で下のコマンドがプリセットとして利用可できる：

* IMEIを要求
* QCCIDを要求
* IMSIを要求
* シグナル品質を確認
* モデムをリセット
* 通信事業者名
* SIMカードの状態を要求

例として、ここではショートカット「IMEIを要求」を選択しています。「送信」をクリックすると、で下の結果が表示されます。

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## 通信事業者プロファイル

 same じまたは異なる通信事業者の異なるプロファイルを保存できます。

モバイルネットワークセクションで、右上の**プロファイル**ボタンをクリックしてプロファイルを管理します。

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

新しいプロファイルを追加するか、現にの 프로필을保存します。

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

通信事業者の要件に基づいて独からのプロファイルを作成します。

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

次回、保存されたプロファイルを選択できます。

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

必要なプロファイルを任意で選択します。

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## 通信基に局のロック

この機できるはGL-X3000、GL-XE3000、GL-X2000（ファームウェアver.4.7で降）でのみ利用可できるです。

高品質なシグナルを受け取り、安定したモバイル接続を確保したい場合は、通信基に局のロックを試みることができます。

**注意:** ロックされた基に局は、キャリアとデバイスがサポートする周波数帯と一致する必要があります。一致しない場合、接続に失敗する可できる性があります。

モバイルネットワークセクションで、右上の**基に局**アイコンをクリックします。

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

利用可できるな基に局が表示されます。

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

基に局をクリックして詳細を表示し、それにロックします。

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

基に局の状態（例：ロック中/ロック解除）が上部に表示されます。

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**注意**:

1. モバイルネットワークインターフェースが有効になっている場合、デバイスがすべての基に局をスキャンできない場合があります。

2. ロックされた基に局がモバイル設定のバンドマスキングまたはAPNパラメータと一致しない場合、ルーターはモバイルネットワークに接続できません。

3. 通信基に局をロックした後、ルーターを別の場所に移動しても、再起動後にロックされた基に局への接続を試み続けます。これにより、新しい場所でルー器がから動のにモバイルネットワークに接続できなくなる可できる性があります。この場合、現にの通信基に局のロックを解除するか、新しい基に局に手動でロックする必要があります。

## 過去のシグナル記録

モバイルネットワークセクションで、右上の**シグナル**アイコンをクリックして過去のシグナル強度を確認します。

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

これにより、モバイル接続の品質を判断できます。シグナルが弱い場合は、より良いシグナルのために基に局を切り替えてみてください。

異なる時間枠を選択することで、モバイルシグナル強度の履歴を表示できます。

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## バンドマスキング

モバイルネットワークセクションで、**もっと見る**をクリックし、**セル情報**を選択してセルの詳細を確認します。

現に使用中のバンドとそのシグナル状態が表示されます。

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

シグナルが弱い場合は、バンドマスキングを有効にして特定のバンドをブロックできます。または、シグナルが良い場合は、ルーターに特定のモバイルバンドのみを使用させることができます。

**手動セットアップ**をクリックしてモバイル設定ページに入り、**バンドマスキング**を有効にします。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

**マスキングモード**（ブロックまたはオープン）を選択し、LTEバンド、5G NSAバンド、5G SAバンドを選択します。

## トラブルシューティング

モバイルネットワーク接続を確立できない場合は、で下のエラーメッセージをクリックして関連する解決策を確認してください。

??? note "SIMカードなし / SIMカードが検出されていません"

    1. ページをアップデートし、数分待ってSIMカードが検出されるかどうかを確認します。
    
    2. SIMカードが正しくインストールされていることを確認します。SIMカードのノッチをカードスロットの相应マークに齐して、正しい挿入方へを確認します。
    
    3. ルーターの電源をオフにし、SIMカードを取り出して再度差し込み、ルーターの電源を再度オンにします。
    
    4. 別のSIMカードを試してください（ある場合）。

    問題が解決しない場合は、ログをダウンロードし、[support@gl-inet.com](mailto:support@gl-inet.com)までお送りください。

??? note "SIMカード未登録 / インターフェースは接続されているが、インターネットにアクセスできません"

    1. ページをアップデートし、数分待ってエラーが消えるかどうかを確認します。
    
    2. **切断**/**中止**をクリックし、**接続**をクリックして再接続を試みます。
    
    3. ルーターを再起動します。
    
    4. SIMカードの状態を確認し、アクティベートされていることを確認します。SIMカードをスマートフォンに差し込んで、アクティブなモバイルデータプランでインターネットに正常にアクセスできるかどうかテストするか、ネットワーク通信事業者にお問い合わせください。
    
    5. 一部の通信事業者はネットワーク接続に3Gプロトコルが必要な場合があります。**手動セットアップ** -> **モバイル設定** -> **プロトコル**に移動し、**3G**を選択して**適用**をクリックしてください。

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        デバイスはから動のに再接続されます。接続が成功したかどうかを確認するために数分お待ちください。

    6. 一部のSIMカードには特別な使用制限がある場合があります（例：特定のAPNが必要です）。SIMカードが登録できない場合は、通信事業者に制限があるかどうかお問い合わせください。

        必要な場合は、**手動セットアップ** -> **モバイル設定** -> **APN**に移動し、ルーター上で正しいAPNを設定してから**適用**をクリックしてください。

    7. **もっと見る**をクリックし、**セル情報**を選択してモバイルシグナル強度を確認します。シグナルが弱い場合は、アンテナが正しくインストールされていることを確認します。より良いシグナルを受けるために、ルー器を開けた 장애物がない場所に移動します。
    
    8. **バンドマスキング**または**通信基に局のロック**が有効になっているかどうかを確認します。有効になっている場合は、その機できるを無効にして再接続してみてください。

    問題が解決しない場合は、ログをダウンロードし、[support@gl-inet.com](mailto:support@gl-inet.com)までお送りください。

## IoT認証

### AT&T認証

リンク[att device certification](https://iotdevices.att.com/certified-devices.aspx#)をクリックし、デバイスの名前を入力すると、見つけることができます。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile認証

リンク[t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification)をクリックし、**フィルター**で5Gを選択すると、見つけることができます。

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネットアクセス方法を same 時に使用する場合の負荷分散を設定するには？](multi-wan.md)

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
