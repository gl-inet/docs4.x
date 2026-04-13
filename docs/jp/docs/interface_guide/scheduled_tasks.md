# スケジュールされたタスク

Web管理パネルの左側で、**SYSTEM** -> **Scheduled Tasks** に移動します。

Schedule Tasks では、LED のオン/オフ、ルーターの再起動、Wi-Fi の有効化/無効化、TX power レベルの切り替えなど、基本操作の毎日スケジュールを設定できます。

**Note**: この機能を使う前に、まず [Time Zone](time_zone.md) で時刻を同期してください。設定した時刻にデバイスの電源がオフになっている場合、そのタスクは実行されません。

## LED表示スケジュール

この機能では、ルーターの LED ライトのオン/オフスケジュールを設定できます。

有効にしたら、オンとオフの時刻を設定し、毎週の有効日を選択して、**Apply** をクリックします。

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

タッチスクリーン搭載モデル（例: GL-BE3600 Slate 7）では、LCD display schedule でタッチスクリーンのオン/オフスケジュールを設定できます。

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## 再起動スケジュール

この機能では、ルーターを自動的に再起動するスケジュールを設定できます。

有効にしたら、再起動時刻を設定し、毎週の有効日を選択して、**Apply** をクリックします。

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Wi-Fiスケジュール

この機能では、ルーターが対応する Wi-Fi 周波数帯（2.4 GHz、5 GHz、6 GHz、MLO Wi-Fi など）ごとに Wi-Fi スケジュールを設定できます。

MLO Wi-Fi は **Turn On/Off** のみ対応し、それ以外の Wi-Fi 周波数帯は **Turn On/Off** と **Switch TX Power** の 2 つのスケジュールモードをサポートしています。

- **Turn On/Off**: 特定の時刻に無線ネットワークを自動で有効または無効にし、接続の利便性と省電力のバランスを取れます。たとえば就寝時間中にオフにして不要な消費電力を抑えられます。

- **Switch TX Power**: 特定の時刻に無線送信電力（信号強度とカバレッジを決定）を自動調整し、性能と省電力のバランスを取れます。たとえば使用量が少ない時間帯に電力を下げることができます。

### MLO Wi-Fiスケジュール

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

MLO Main Wi-Fi と Guest Wi-Fi の両方について、オン/オフスケジュールを設定できます。

Main または Guest Wi-Fi Schedule を有効にし、オンとオフの時刻を設定し、毎週の有効日を選択して、**Apply** をクリックします。

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### 6 GHz Wi-Fi Schedule

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-BE9300 (Flint 3)      |    √    |

Wi-Fi スケジュールモードが **Turn On/Off** の場合、6 GHz Main Wi-Fi と Guest Wi-Fi の両方についてオン/オフスケジュールを設定できます。

Main または Guest Wi-Fi Schedule を有効にし、オンとオフの時刻を設定し、毎週の有効日を選択して、**Apply** をクリックします。

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Wi-Fi スケジュールモードが **Switch TX Power** の場合、6 GHz Main Wi-Fi の TX power 切り替えスケジュールを設定できます。このスケジュールモードでは 6 GHz Guest Wi-Fi はサポートされません。

Main Wi-Fi Schedule を有効にし、TX power を切り替える 2 つの時刻指定アクションを設定し、毎週の有効日を選択して、**Apply** をクリックします。

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: 特定の時刻（例: 22:00）に、TX Power を指定レベル（例: Low）へ設定します。
- **Restore**: 別の時刻（例: 07:00）に、TX Power を別のレベル（例: Max）へ戻します。
- **days**: これらの設定を有効にする曜日を選択します。

### 5 GHz Wi-Fi Schedule

Wi-Fi スケジュールモードが **Turn On/Off** の場合、5 GHz Main Wi-Fi と Guest Wi-Fi の両方についてオン/オフスケジュールを設定できます。

Main または Guest Wi-Fi Schedule を有効にし、オンとオフの時刻を設定し、毎週の有効日を選択して、**Apply** をクリックします。

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Wi-Fi スケジュールモードが **Switch TX Power** の場合、5 GHz Main Wi-Fi の TX power 切り替えスケジュールを設定できます。このスケジュールモードでは 5 GHz Guest Wi-Fi はサポートされません。

Main Wi-Fi Schedule を有効にし、TX power を切り替える 2 つの時刻指定アクションを設定し、毎週の有効日を選択して、**Apply** をクリックします。

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: 特定の時刻（例: 22:00）に、TX Power を指定レベル（例: Low）へ設定します。
- **Restore**: 別の時刻（例: 07:00）に、TX Power を別のレベル（例: Max）へ戻します。
- **days**: これらの設定を有効にする曜日を選択します。

### 2.4 GHz Wi-Fi Schedule

Wi-Fi スケジュールモードが **Turn On/Off** の場合、2.4 GHz Main Wi-Fi と Guest Wi-Fi の両方についてオン/オフスケジュールを設定できます。

Main または Guest Wi-Fi Schedule を有効にし、オンとオフの時刻を設定し、毎週の有効日を選択して、**Apply** をクリックします。

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Wi-Fi スケジュールモードが **Switch TX Power** の場合、2.4 GHz Main Wi-Fi の TX power 切り替えスケジュールを設定できます。このスケジュールモードでは 2.4 GHz Guest Wi-Fi はサポートされません。

Main Wi-Fi Schedule を有効にし、TX power を切り替える 2 つの時刻指定アクションを設定し、毎週の有効日を選択して、**Apply** をクリックします。

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: 特定の時刻（例: 22:00）に、TX Power を指定レベル（例: Low）へ設定します。
- **Restore**: 別の時刻（例: 07:00）に、TX Power を別のレベル（例: Max）へ戻します。
- **days**: これらの設定を有効にする曜日を選択します。

---

ご不明な点がありましたら、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
