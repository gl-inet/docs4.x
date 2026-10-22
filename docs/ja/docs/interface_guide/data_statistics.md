# データ統計 {#data-statistics}

**注**: この機能はファームウェア v4.9 で導入されました。

Mango 2 (GL-MG1300) など一部のモデルは、メモリ不足のため、ファームウェア v4.9 以降でもデータ統計に対応していません。詳しくは[対応モデル](#supported-models)をご覧ください。

---

Web 管理パネルの左側で、**FLOW CONTROL** -> **Data Statistics** に移動します。

データ統計は、アプリケーションやプロトコルごとのネットワーク使用状況を把握できる直感的なトラフィックダッシュボードです。1 時間、1 日、7 日間の履歴トレンドの表示、使用量ランキングの表示、デバイスごとのトラフィック監視、不要なアプリのワンクリックでのブロックに対応しています。

**注**:

1. ルーターがドロップインゲートウェイモードの場合、データ統計は機能しません。
2. データ統計はネットワークアクセラレーションと併用できません。安定したパフォーマンスを確保するため、データ統計を有効にするとネットワークアクセラレーションは自動的に無効になります。
3. データ統計が集計するのは、クライアントページに表示されているデバイスのトラフィック使用量のみです。デバイスがトンネルインターフェイス（VPNクライアント、Tailscale、AstroWarp など）経由でルーターに接続している場合、そのデバイスから発信されルーター経由で転送されるトラフィックは、統計の対象外になります。

## 対応モデル {#supported-models}

??? "対応モデル"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "非対応モデル"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## ファームウェア v4.11 以降の場合 {#for-firmware-v411-and-above}

右上のスイッチを切り替えて、**Application Total Data** を表示します。

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

このページは 2 つの部分で構成されています。

- **Top 10 Apps by Bandwidth Usage**: 時系列のトレンドグラフ（過去 1 日など）で、選択した期間における上位 10 個のアプリケーションの帯域幅消費量を表示します。

    グラフにマウスを重ねると、特定の時点における帯域幅消費量上位 10 個のアプリのデータ使用量が表示されます。

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: ダウンロード、アップロード、総帯域幅など、各アプリケーションの詳細なトラフィック指標が表示されます。必要に応じて、検索バーで特定のアプリを検索できます。

    列ヘッダーの横にある並べ替え矢印をクリックすると、リストを昇順または降順に並べ替えられます。

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### データストレージルール {#data-storage-rules}

1. トラフィック統計は 15 秒ごとに RAM に保存され、1 時間ごとにフラッシュに保存されます。フラッシュメモリの寿命を保護するため、頻繁なフラッシュへの書き込みは行いません。

2. ソフトリブートではデータは失われません。システムは再起動する前に、まず RAM からフラッシュにデータを書き込みます。

3. ハードリブート（電源の抜き差し）またはファームウェアアップグレード（設定を保持）を行うと、直近 1 時間までのデータが失われる可能性があります。

### クライアントセレクター {#client-selector}

クライアントセレクターでは、特定のクライアントを選択するか、デフォルトの All（すべてのクライアント）のままにできます。グラフと統計テーブルは自動的に更新され、選択したデバイスのトラフィックデータのみが表示されます。

**注**: この機能はファームウェア v4.11 で導入されました。

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### チャートビューの切り替え {#switch-chart-views}

App Traffic Statistics を表示する際、必要に応じてグラフの種類を切り替えられます。

**注**: この機能はファームウェア v4.11 で導入されました。

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: 選択した時間範囲における帯域幅使用量の推移を表示します。連続した曲線でトラフィックの時間的な変化がわかるため、使用量の増加傾向や減少傾向の把握に適しています。

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: アプリケーションごとの帯域幅使用量を並べて比較します。各バーにより、どのアプリが多くの帯域幅を消費しているかが一目でわかります。

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: 帯域幅の総使用量を割合で示します。各扇形は、それぞれのアプリケーションが使用するトラフィックの相対的な割合を表します。

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### 時間範囲の切り替え {#switch-time-range}

必要に応じて、時間範囲を Past hour（過去 1 時間）、Past day（過去 1 日）、Past week（過去 1 週間）の間で切り替えられます。

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

選択した時間範囲によって、データの表示方法が決まります。

- **詳細に確認する場合（Past Hour など）**: グラフには、リアルタイムに近い細かな変動が表示されます。山はより高く、谷はより急になるため、帯域幅使用量の急増を見つけやすくなります。

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **全体的な傾向を確認する場合（Past Day や Past Week など）**: グラフは、より長い期間のデータをまとめて表示します。曲線はより滑らかになり、細かな変化ではなく全体的なトラフィックの傾向を示します。

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### 統計の消去 {#clear-statistics}

必要に応じて、左上のほうきアイコンをクリックして統計をクリアします。

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

クリア後、以下のようにページが更新されます。新しい統計の読み込みが始まるまで、しばらく時間がかかる場合があります。

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## ファームウェア v4.9 ～ v4.10 の場合 {#for-firmware-v49-to-v410}

右上のスイッチを切り替えて、**Application Total Data** を表示します。

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

このページは 2 つの部分で構成されています。

- **Top 10 Apps by Bandwidth Usage**: 時系列のトレンドグラフ（過去 1 日など）で、選択した期間における上位 10 個のアプリケーションの帯域幅消費量を表示します。

    グラフにマウスを重ねると、特定の時点における帯域幅消費量上位 10 個のアプリのデータ使用量が表示されます。

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: ダウンロード、アップロード、合計帯域幅など、各アプリケーションの詳細なトラフィック指標が表示されます。必要に応じて、検索バーで特定のアプリを検索できます。

    列ヘッダーの横にある並べ替え矢印をクリックすると、リストを昇順または降順に並べ替えられます。

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### データストレージルール {#data-storage-rules_1}

1. トラフィック統計は 15 秒ごとに RAM に保存され、1 時間ごとにフラッシュに保存されます。フラッシュメモリの寿命を保護するため、頻繁なフラッシュへの書き込みは行いません。

2. ソフトリブートではデータは失われません。システムは再起動する前に、まず RAM からフラッシュにデータを書き込みます。

3. ハードリブート（電源の抜き差し）またはファームウェアアップグレード（設定を保持）を行うと、直近 1 時間までのデータが失われる可能性があります。

### 時間範囲の切り替え {#switch-time-range_1}

必要に応じて、時間範囲を Past hour（過去 1 時間）、Past day（過去 1 日）、Past week（過去 1 週間）の間で切り替えられます。

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

選択した時間範囲によって、データの表示方法が決まります。

- **詳細に確認する場合（Past Hour など）**: グラフには、リアルタイムに近い細かな変動が表示されます。山はより高く、谷はより急になるため、帯域幅使用量の急増を見つけやすくなります。

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **全体的な傾向を確認する場合（Past Day や Past Week など）**: グラフは、より長い期間のデータをまとめて表示します。曲線はより滑らかになり、細かな変化ではなく全体的なトラフィックの傾向を示します。

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### 統計の消去 {#clear-statistics_1}

必要に応じて、左上のほうきアイコンをクリックして統計をクリアします。

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

クリア後、以下のようにページが更新されます。新しい統計の読み込みが始まるまで、しばらく時間がかかる場合があります。

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
