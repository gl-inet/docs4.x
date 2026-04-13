# セルラーでインターネットに接続する

**注意**: このガイドはファームウェア v4.8 に基づいています。以前のバージョンについては、[こちら](internet_cellular_v4.7.md)を参照してください。

---

ほとんどの GL.iNet ルーターはセルラー接続に対応しています。このガイドでは、以下の3種類のモデルを説明します。

1. **4G シングル SIM 内蔵モデル**

    GL-E750 (Mudi) のように、4G モジュールと単一の SIM カードスロットを内蔵したモデルです。[シングル SIM モデルのセットアップ](#setup-for-single-sim-models) を参照してください。

2. **5G デュアル SIM 内蔵モデル**

    GL-X3000 (Spitz AX) のように、5G モジュールと2つの SIM カードスロットを内蔵したモデルです。Web 管理パネル上のセルラー設定画面はシングル SIM モデルと少し異なる場合があります。[デュアル SIM モデルのセットアップ](#setup-for-dual-sim-models) を参照してください。

3. **USB モデム対応モデル**

    一部のモデルには SIM カードスロットが内蔵されていませんが、USB ポートを備えており、GL-MT3000 (Beryl AX) のように USB モデム経由でセルラー接続を利用できます。[USB モデムのセットアップ](#setup-for-usb-modem) を参照してください。

**注意:** 一部の SIM カードは初回使用前に有効化が必要です。互換性を確保するため、ルーターへ挿入する前にスマートフォンで SIM カードを有効化してください。

## シングル SIM モデルのセットアップ {#setup-for-single-sim-models}

以下の手順は、セルラーモデムと単一の SIM カードスロットを内蔵したモデルに適用されます。

ここでは **GL-E750 (Mudi)** を例に説明します。

最初にルーターの電源を切り、事前に有効化した SIM カードをスロットに挿入してから電源を入れることをおすすめします。ルーターの起動後に SIM カードを挿入すると、Web 管理パネルが自動更新されない場合があります。その場合はページを更新するか、ルーターを再起動してください。

### 自動セットアップ

ルーターの Web 管理パネルにログインし、**INTERNET** -> **Cellular** に移動します。

1. SIM カードが挿入されていない場合、ページには "Your SIM card has not been detected" と表示されます。

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. SIM カードを挿入すると、デバイスは以下のように接続を開始します。

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    自動で接続されない場合は、利用可能であれば **Connect** ボタンをクリックしてください。

    SIM カードが検出されない場合は、ルーターを再起動して再度認識されるか確認してください。

3. セルラーネットワークへの接続に成功すると、ページには緑のドットとともにネットワーク情報が表示されます。

    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Auto Setup に失敗した場合は、[Manual Setup](#manual-setup-single-sim) を試してください。

### Manual Setup {#manual-setup-single-sim}

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動し、**SIM Card Settings** をクリックします。

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

現在使用中の SIM カードのセルラー設定を確認または変更できます。

**注意**: 一部の SIM カードでは特定の APN が必要な場合があります。SIM カードがネットワーク登録に失敗する場合は、制限がないか通信事業者へ確認してください。必要に応じて、ルーター上で正しい APN を設定してください。

変更を適用すると、再接続が行われます。

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN（Access Point Name）はセルラーネットワーク接続に必要なゲートウェイパラメーターです。モバイル通信事業者が提供するインターネットへルーターを接続するために使われます。デフォルト APN を使うことも、通信事業者から提供されたカスタム APN を設定することもできます。

- **Protocol**: セルラー通信プロトコル（3G、QMI、QCM など）です。通常は自動検出されますが、モデムや通信事業者の要件に合わせて変更できます。

- **Port**: セルラーモデムと通信するためのシリアルポートです。通常は自動検出されるため、手動調整は不要です。

- **TTL**: TTL（Time To Live）は、パケットがネットワーク内で生存できる最大時間を定義します。デフォルトでは、ルーターはクライアントデバイスから受信したパケットを転送する前に TTL を 1 減算します。上書きが必要な場合は、ここで固定値を設定できます。TTL 設定は IPv4 でのみ有効です。

- **HL**: IPv6 では HL（Hop Limit）がネットワーク内でのデータパケットの転送ホップ数を制限し、IPv4 の TTL に相当します。

- **MTU**: デフォルトの MTU 値は 1500 バイトです。

- **Authentication**: 通信事業者が要求する認証方式（NONE、PAP、CHAP など）を選択します。認証情報が不要な場合は通常 NONE のままです。

- **Band Masking**: 特定のバンドをブロックしたり、使用するセルラーバンドを限定したりしたい場合は Band Masking を有効にできます。詳細は [こちら](#band-masking) を参照してください。

## デュアル SIM モデルのセットアップ {#setup-for-dual-sim-models}

以下の手順は、デュアル SIM に対応したセルラーモデムを内蔵するモデルに適用されます。ページ構成はシングル SIM モデルと若干異なる場合があります。

ここでは **GL-X3000 (Spitz AX)** を例に説明します。このモデルは Dual SIM, Single Standby に対応しており、2枚の SIM カードを挿してセルラー接続に利用できますが、同時にアクティブにできる SIM カードは1枚だけです。2枚の SIM カードは手動で切り替えられます。

最初にルーターの電源を切り、事前に有効化した SIM カードをスロットへ挿入してから電源を入れることをおすすめします。ルーターの起動後に SIM カードを挿入すると、Web 管理パネルが自動更新されない場合があります。その場合はページを更新するか、ルーターを再起動してください。

### 自動セットアップ

ルーターの Web 管理パネルにログインし、**INTERNET** -> **Cellular** に移動します。

1. SIM カードが挿入されていない場合、ページには "Your SIM card has not been detected" と表示されます。

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. SIM カードを挿入すると、ページは次のように表示されます。**Connect** をクリックします。

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    SIM カードが検出されない場合は、ルーターを再起動して再度認識されるか確認してください。

3. セルラーネットワークへの接続に成功すると、ページには緑のドットとともにネットワーク情報が表示されます。

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. **View More Information** をクリックすると、モデム情報、SIM カード情報、インターネット情報、セルラー信号など、より詳しい情報を表示できます。

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Auto Setup に失敗した場合は、[Manual Setup](#manual-setup-dual-sim) を試してください。

### Manual Setup {#manual-setup-dual-sim}

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動し、**SIM Card Settings** をクリックします。

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

現在使用中の SIM カードのセルラー設定を確認または変更できます。

**注意**: 一部の SIM カードでは特定の APN が必要な場合があります。SIM カードがネットワーク登録に失敗する場合は、制限がないか通信事業者へ確認してください。必要に応じて、ルーター上で正しい APN を設定してください。

変更を適用すると、再接続が行われます。

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN（Access Point Name）はセルラーネットワーク接続に必要なゲートウェイパラメーターです。モバイル通信事業者が提供するインターネットへルーターを接続するために使われます。デフォルト APN を使うことも、通信事業者から提供されたカスタム APN を設定することもできます。

- **Protocol**: モデムと通信事業者に基づいて自動検出されたセルラー通信プロトコル（QMI、QCM など）です。

- **Port**: セルラーモデムと通信するためのシリアルポートで、自動検出されます。

- **TTL**: TTL（Time To Live）は、パケットがネットワーク内で生存できる最大時間を定義します。デフォルトでは、ルーターはクライアントデバイスから受信したパケットを転送する前に TTL を 1 減算します。上書きが必要な場合は、ここで固定値を設定できます。TTL 設定は IPv4 でのみ有効です。

- **HL**: IPv6 では HL（Hop Limit）がネットワーク内でのデータパケットの転送ホップ数を制限し、IPv4 の TTL に相当します。

- **MTU**: デフォルトの MTU 値は 1500 バイトです。

- **Authentication**: 通信事業者が要求する認証方式（NONE、PAP、CHAP など）を選択します。認証情報が不要な場合は通常 NONE のままです。

- **Band Masking**: 特定のバンドをブロックしたり、使用するセルラーバンドを限定したりしたい場合は Band Masking を有効にできます。詳細は [こちら](#band-masking) を参照してください。

### SIM カードスロット設定

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動し、**SIM Card Switch** をクリックします。

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

Auto Switch ボタン、現在アクティブな SIM カード、ICCID、Network Operator が表示されます。

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

SIM カードを2枚挿入している場合は、**Auto Switch** を有効にできます。

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch**: SIM 1 と SIM 2 を自動で切り替えます。SIM Auto Switch のネットワーク検出方式は、Multi-WAN ページで設定するものと同じです。

- **Preferred SIM Card Slot**: 優先して使用する SIM カードを SIM 1 または SIM 2 に設定します。

- **Failover Interval**: 5 分から 24 時間まで設定できます。

    フェイルオーバー後もインターネット接続が利用できない場合、デバイスは優先 SIM スロットに戻り、この間隔だけ待機してから再度フェイルオーバーを試みます。

    このオプションは、優先 SIM カードとバックアップ SIM カードの両方に信号がない場合に適用されます。どちらかが有効な信号を取得するまで、デバイスは SIM カードを切り替え続けます。

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    有効にすると、デバイスは毎日設定した時刻に優先 SIM スロットの状態を確認し、優先 SIM が再びインターネット接続を利用できるようになっていれば自動的に戻します。

    これにより、バックアップ SIM のデータ消費が過剰になるのを防げます。優先 SIM に引き続き信号がない場合は、バックアップ SIM の使用が継続されます。

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**注意**: Auto Switch 機能は、すぐに別の SIM カードへ切り替わるわけではありません。まず、現在の SIM でインターネットに接続できないことを確認する時間が必要です。さらに、もう一方の SIM はスタンバイ状態ではないため、有効化にも時間がかかります。

## USB モデムのセットアップ {#setup-for-usb-modem}

以下の手順は、SIM カードスロットを内蔵していないものの、外付け USB モデムを接続できる USB ポートを備えたモデルに適用されます。

ここでは **GL-MT3000 (Beryl AX)** と外付け USB モデム **SIMPoYo uFi** を例に説明します。

最初にルーターの電源を切り、事前に有効化した SIM カードを USB モデムへ挿入し、モデムをルーターの USB ポートに接続してから電源を入れることをおすすめします。ルーターの起動後に USB モデムを挿した場合は、Web 管理パネルが自動更新されないことがあります。その場合はページを更新するか、ルーターを再起動してください。

### クイックセットアップ

1. 最初にルーターの電源を切ります。USB モデムに SIM カードを挿入し、モデムをルーターの USB ポートへ接続してから電源を入れます。

2. ルーターの Web 管理パネルにログインし、**INTERNET** -> **Tethering** に移動して **Connect** をクリックします。

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    TTL、HL、MTU などの詳細設定が必要な場合は、**Advanced** をクリックして設定してから **Connect** をクリックします。

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    接続が開始されます。

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. 接続に成功すると、ページには緑のドットとともにネットワーク情報が表示されます。

    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **注意:** 初回設定後は、USB モデムを接続した状態でルーターを再起動した場合や、モデムを挿し直した場合でも、自動的に認識されて接続が確立されるため、再度 Connect ボタンをクリックする必要はありません。

### 対応モデム

これまでにテスト済みの対応モデム一覧です。

**SIMPoYo uFi** は、Wi-Fi ホットスポット機能を備えたコンパクトなプラグアンドプレイ USB ドングルで、どこでも高速で安定した接続を実現できるよう設計されています。ほとんどの GL.iNet ルーターに加え、ノートPC、モバイルバッテリー、車載 USB ポートなどの USB 電源でも問題なく利用できます。英国およびヨーロッパ34か国で使える 10GB の無料データが 30 日間付属します。

| Model                                                                        | Cellular | Tested | Tested by       | Comments* |
| --------------------------------------------------------------------------- | -------- | ------ | --------------- | --------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)          | 5G       | Yes    | GL.iNet         |           |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/) | 4G       | Yes    | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C                                              | 4G       | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C                                      | 4G       | Yes    | GL.iNet         |           |
| Quectel EC200A series                                                       | 4G       | Yes    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                                                      | 4G       | Yes    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL                                                | 4G       | Yes    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL                                                | 4G       | Yes    | akw2312         |           |
| Quectel RM520N-GL                                                           | 5G       | Yes    | akw2312         |           |
| Quectel UC20-E                                                              | 3G       | Yes    | GL.iNet         |           |
| ZTE ME909s-821                                                              | 4G       | Yes    | GL.iNet         |           |
| Huawei E1550                                                                | 3G       | Yes    | GL.iNet         |           |
| Huawei E3276                                                                | 4G       | Yes    | GL.iNet         |           |
| Huawei E3372                                                                | 4G       | Yes    | anonymous       |           |
| Huawei E3372h-320 (Ukraine)                                                 | 4G       | Yes    | anonymous       | Host-less |
| TP-Link MA260                                                               | 3G       | Yes    | GL.iNet         |           |
| ZTE M823                                                                    | 4G       | Yes    | Arnas Risqianto |           |
| ZTE MF190                                                                   | 3G       | Yes    | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)                                                  | 4G       | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)                                                    | 4G       | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)                                                   | 4G       | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                                                     | 4G       | Yes    | anonymous       | Host-less |

- **QMI**: このモデムは QMI モードに対応しています。SIM Card Settings でセルラー通信プロトコルを QMI にし、シリアルポートを **/dev/cdc-wdm0** に設定してください。

- **Host-less**: このモデムは Tethering モードに対応しています。Cellular インターフェースではなく、ルーターの Tethering インターフェースから接続を管理してください。

## トラフィック統計

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動し、**Data Used** をクリックします。

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Traffic Statistics ページが開きます。ここでは SIM カードごとの使用データ量を確認でき、データ上限も設定できます。

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Data Used が Data Cap Amount を超えた場合は、**Data Cap Amount** または **Data Used** を手動で変更してください。そうしないと、ネットワークが切断されたり、デュアル SIM モデルでは SIM カードが Auto Switch されたりする場合があります。

- **使用データ量を変更する**

    SIM 1/2 Data Used の右側にある **Modify** をクリックします。

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    使用データ量を変更またはリセットできます。

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **SIM のデータ上限を設定する**

    SIM のデータ上限を設定したい場合は、まず **Save data when power off** を有効にします。これにより、デバイスの電源を切っても使用データ量を保存できます。

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    次に、SIM 1 または SIM 2 の Limit Settings を有効にします。

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

デュアル SIM モデルでは、**SIM Card Slot Auto Switch** も同時に有効にすることをおすすめします。SIM 1 の Data Cap Amount を設定し、SIM Card Slot Auto Switch を有効にしている場合、SIM 1 のデータ使用量が上限を超えると、自動的に SIM 2 へ切り替わり、SIM 1 は無効になります。

## 信号履歴

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動し、**Historical Signal Record** をクリックします。

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

ここではセルラー接続の品質を確認できます。信号が弱い場合は、より良い信号を得るために接続先の基地局を切り替えてみてください。

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

右上で期間を切り替えると、異なる時間範囲の信号強度履歴を表示できます。

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## バンドマスキング

Band Masking を使うと、特定のバンドをブロックしたり、優先したいセルラーバンドだけを使用したりして、弱いセルラー信号の改善を図れます。

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** -> **SIM Card Settings** に移動し、**Enable Band Masking** をオンにします。

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

**Masking Mode**（Block または Open）を選択し、LTE Bands、5G NSA Bands、5G SA Bands を設定します。

## SMS

[SMS チュートリアル](sms.md) を参照してください。

## SMS転送

[SMS Forwarding チュートリアル](../tutorials/sms_forwarding.md) を参照してください。

## 基地局ロック

!!! note "対応モデル"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) はファームウェア ver.4.7 以降でこの機能をサポートします。

より高品質な信号を受信し、安定したセルラー接続を確保したい場合は、基地局ロックを試すことができます。

**注意:** ロックする基地局は、通信事業者とデバイスがサポートする周波数帯に一致している必要があります。一致しない場合、接続に失敗する可能性があります。

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動します。右上の三点アイコンをクリックし、**Lock Tower** を選択します。

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

**Scan** をクリックしてセルラー基地局のスキャンを開始します。完了まで数分かかります。スキャン中はページを更新しないでください。

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

利用可能な基地局が表示されます。

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

基地局をクリックすると詳細を確認し、その基地局にロックできます。

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**注意**:

1. Cellular インターフェースが有効な状態では、すべての基地局をスキャンできない場合があります。

2. ロックした基地局が、セルラー設定内の Band Masking や APN パラメーターと一致しない場合、ルーターはセルラーネットワークへ接続できません。

3. 基地局をロックした後にルーターを別の場所へ移動すると、再起動後も以前ロックした基地局への再接続を試みます。その結果、新しい場所でセルラーネットワークへ自動接続できない場合があります。この場合は、現在の基地局ロックを解除するか、新しい基地局へ手動でロックし直してください。

## 通信事業者ロック

この機能は GL-X3000、GL-XE3000、および GL-X2000（ファームウェア ver.4.8 以降）でのみ利用できます。

特定の通信事業者にロックすると、ルーターはその事業者のネットワークだけを使用します。これにより、安定した接続を維持しやすくなり、特に国境付近では意図しないローミング料金を回避できます。

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動します。右上の三点アイコンをクリックし、**Lock Operator** を選択します。

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

ロックモードは3種類あります。

- **Auto**: 利用可能な通信事業者ネットワークへ自動接続します。
- **Manual**: 特定の通信事業者へ手動でロックします。
- **Manual-Auto**: 手動ロックに失敗した場合、利用可能な通信事業者ネットワークへ自動的に切り替えます。

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## モデムATコマンド

Modem AT Command は、セルラーモデムと通信するための標準命令です。この機能を使うと、コマンドを送信してモデムの状態を確認できます。

ルーターの Web 管理パネルで **INTERNET** -> **Cellular** に移動します。右上の三点アイコンをクリックし、**Modem AT Command** を選択します。

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

AT Command ページが開きます。

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Shortcut が **Manual command** に設定されている場合は、AT Command フィールドに任意のコマンドを入力できます。

Shortcut のドロップダウンをクリックすると、**preset commands** の一覧から選択することもできます。

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

プリセットとして利用できるコマンドは次のとおりです。

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

例として、ここではショートカット "Request IMEI" を選択しています。"Send" をクリックすると、以下のような結果が表示されます。

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

右下の **Export Debug Info** をクリックすると、.json ファイルをダウンロードできます。

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## トラブルシューティング

セルラー接続を確立できない場合は、以下のエラーメッセージをクリックして該当する対処方法を確認してください。

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    トラブルシューティングの候補は次のとおりです。

    1. ページを更新し、数分待ってから SIM カードが検出されるか確認します。

    2. SIM カードが正しく装着されていることを確認します。SIM カードの切り欠きがスロットのマークと一致しているか確認してください。

    3. ルーターの電源を切り、SIM カードを抜き差ししてから再度電源を入れます。

    4. 利用可能であれば、別の SIM カードでも試してください。

    問題が解消しない場合は、ログをダウンロードして [support@gl-inet.com](mailto:support@gl-inet.com) へ送信してください。

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    この問題には、次の2種類のエラーメッセージがあります。

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed

        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    トラブルシューティングの候補は次のとおりです。

    1. ページを更新し、数分待ってエラーが消えるか確認します。

    2. **Disconnect**/**Abort** をクリックしてから **Connect** をクリックし、再接続を試します。

    3. ルーターを再起動します。

    4. SIM カードの状態を確認し、有効化されていることを確認します。SIM カードをスマートフォンに挿して、モバイルデータ通信プランが有効な状態で正常にインターネットへ接続できるかテストするか、通信事業者へ確認してください。

    5. 一部の通信事業者では、接続に 3G プロトコルが必要な場合があります。**SIM Card Settings** -> **Protocol** に移動し、**3G** を選択して **Apply** をクリックしてください。

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        デバイスは自動的に再接続します。数分待って接続に成功するか確認してください。

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        接続に成功すると、ページは次のように表示されます。

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. 一部の SIM カードには特別な利用制限（特定の APN が必要など）がある場合があります。SIM カードが登録に失敗する場合は、制限がないか通信事業者へ確認してください。

        必要に応じて、**SIM Card Settings** -> **APN** に移動し、ルーター上で正しい APN を設定してから **Apply** をクリックしてください。

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. **View More Information** をクリックしてセルラー信号強度を確認します。信号が弱い場合は、アンテナが正しく取り付けられているか確認してください。より良い受信のため、ルーターを開けた障害物の少ない場所へ移動してください。

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

    8. **Band Masking** または **Lock Tower** が有効になっていないか確認します。有効な場合は機能を無効にして再接続を試してください。

    問題が解消しない場合は、ログをダウンロードして [support@gl-inet.com](mailto:support@gl-inet.com) へ送信してください。

## IoT Certification {#iot-certification}

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
