# スケジュールされたタスク

ウェブ管理パネルの左側 -> システム -> スケジュールされたタスク

スケジュールタスクでは、LEDのオン/オフ、ルーターの再起動、Wi-Fiの有効化/無効化、TX powerレベルの切り替えなど、基本のな操作の毎日スケジュールを設定できます。

**注意**: この機能を使用する前に、まず[タイムゾーン](time_zone.md)で時刻を 同期させてください。設定した時刻にデバイスがシャットダウンしている場合、タスクは実行されません。

## LED表示スケジュール

この機能を使用すると、ルーターのLEDライトのオン/オフスケジュールを設定できます。

有効にすると、オンとオフの時間を設定し、毎週の有効日を設定して、**適用**をクリックします。

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

タッチスクリーン付きのモデル（例：GL-BE3600 Slate 7）の場合、LCD表示スケジュールでタッチスクリーンのオン/オフスケジュールを設定できます。

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## スケジュール再起動

この機能を使用すると、ルーターを自動的に再起動するスケジュールを設定できます。

有効にすると、再起動の時間と毎週の有効日を設定し、**適用**をクリックします。

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Wi-Fiスケジュール

この機能を使用すると、ルーターが サポートする Wi-Fi 周波数帯（2.4 GHz、5 GHz、6 GHz、MLO Wi-Fiなど）に基づいてWi-Fiスケジュールを設定できます。

MLO Wi-Fiはオン/オフスケジュジュールモードのみサポートしていますが、彼のすべてのWi-Fi周波数帯は2つのスケジュジュールモードをサポートしています：オン/オフの切り替えとTX powerの切り替え。

- **オン/オフの切り替え**: 特定の時間（例：就寝時にオフにして消費電力を削減）に無線ネットワークを自動的に有効または無効にすることで、接続の利便性と省エネのバランスを取ることができます。

- **TX powerの切り替え**: 特定の時間（使用率が低い時期に電力を低下するなど）自動的に無線送信電力（シグナル強度とカバレッジを決定）を調全体し、パフォーマンスとエネルギー効率のバランスを取ることができます。

### MLO Wi-Fiスケジュール

| 対応モデル              |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)       |    √    |
| GL-MT3600BE (Beryl 7)   |    √    |
| GL-BE6500 (Flint 3e)    |    √    |
| GL-BE9300 (Flint 3)    |    √    |
| GL-BE3600 (Slate 7)    |    √    |

MLOメインWi-FiとゲストWi-Fiの両方のオン/オフスケジュールを設定できます。

メインまたはゲストWi-Fiスケジュールを有効にし、オンとオフの時間を選択して、毎週の有効日を設定し、**適用**をクリックします。

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### 6 GHz Wi-Fiスケジュール

| 対応モデル              |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)       |    √    |
| GL-BE9300 (Flint 3)     |    √    |

Wi-Fiスケジュジュールモードが**オン/オフの切り替え**の場合、6 GHzメインWi-FiとゲストWi-Fiの両方のオン/オフスケジュールを設定できます。

メインまたはゲストWi-Fiスケジュールを有効にし、オンとオフの時間を選択して、毎週の有効日を設定し、**適用**をクリックします。

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Wi-Fiスケジュジュールモードが**TX powerの切り替え**の場合、6 GHzメインWi-FiのTX power切り替えスケジュールを設定できます。このスケジュジュールモードでは6 GHzゲストWi-Fiはサポートされていないことに注意してください。

メインWi-Fiスケジュールを有効にし、2つの定期アクションを設定してTX powerを切り替え、毎週の有効日を設定し、**適用**をクリックします。

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **切り替え**: 特定の時間（例：22:00）にTX Powerを特定のレベル（例：Low）に設定します。
- **復元**: 別の時間（例：07:00）にTX Powerを別のレベル（例：Max）に戻します。
- **曜日**: これらの設定の有効な曜日を選択します。

### 5 GHz Wi-Fiスケジュール

Wi-Fiスケジュジュールモードが**オン/オフの切り替え**の場合、5 GHzメインWi-FiとゲストWi-Fiの両方のオン/オフスケジュールを設定できます。

メインまたはゲストWi-Fiスケジュールを有効にし、オンとオフの時間を選択して、毎週の有効日を設定し、**適用**をクリックします。

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Wi-Fiスケジュジュールモードが**TX powerの切り替え**の場合、5 GHzメインWi-FiのTX power切り替えスケジュールを設定できます。このスケジュジュールモードでは5 GHzゲストWi-Fiはサポートされていないことに注意してください。

メインWi-Fiスケジュールを有効にし、2つの定期アクションを設定してTX powerを切り替え、毎週の有効日を設定し、**適用**をクリックします。

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **切り替え**: 特定の時間（例：22:00）にTX Powerを特定のレベル（例：Low）に設定します。
- **復元**: 別の時間（例：07:00）にTX Powerを別のレベル（例：Max）に戻します。
- **曜日**: これらの設定の有効な曜日を選択します。

### 2.4 GHz Wi-Fiスケジュール

Wi-Fiスケジュジュールモードが**オン/オフの切り替え**の場合、2.4 GHzメインWi-FiとゲストWi-Fiの両方のオン/オフスケジュールを設定できます。

メインまたはゲストWi-Fiスケジュールを有効にし、オンとオフの時間を選択して、毎週の有効日を設定し、**適用**をクリックします。

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Wi-Fiスケジュジュールモードが**TX powerの切り替え**の場合、2.4 GHzメインWi-FiのTX power切り替えスケジュールを設定できます。このスケジュジュールモードでは2.4 GHzゲストWi-Fiはサポートされていないことに注意してください。

メインWi-Fiスケジュールを有効にし、2つの定期アクションを設定してTX powerを切り替え、毎週の有効日を設定し、**適用**をクリックします。

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **切り替え**: 特定の時間（例：22:00）にTX Powerを特定のレベル（例：Low）に設定します。
- **復元**: 別の時間（例：07:00）にTX Powerを別のレベル（例：Max）に戻します。
- **曜日**: これらの設定の有効な曜日を選択します。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
