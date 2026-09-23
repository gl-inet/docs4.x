# データ統計

**注**: この機能はファームウェア v4.9 で導入されました。

Mango 2 (GL-MG1300) など一部のモデルは、メモリ不足のため、ファームウェア v4.9 以降でも Data Statistics に対応しません。詳しくは[対応モデル](#supported-models)をご覧ください。

---

Web 管理パネルの左側で、**FLOW CONTROL** -> **Data Statistics** に移動します。

データ統計は、アプリケーションおよびプロトコルごとのネットワーク使用状況を識別する直感的なトラフィック ダッシュボードを提供します。 1 時間、1 日、7 日間の履歴トレンドの表示をサポートし、使用状況ランキングを表示し、デバイスごとのトラフィックを監視し、ワンクリックで不要なアプリをブロックできます。

**注**:

1. ルーターがドロップイン ゲートウェイ モードの場合、データ統計は有効になりません。
2. データ統計はネットワーク アクセラレーションと併用できません。データ統計を有効にすると、ネットワーク アクセラレーションが自動的に無効になり、安定したパフォーマンスが保証されます。
3. データ統計は、クライアント ページにリストされているデバイスのトラフィック使用量のみを追跡します。デバイスがトンネル インターフェイス （VPNクライアント、Tailscale、AstroWarpなど） 経由でルーターに接続している場合、そのデバイスから発信されルーター経由で転送されるトラフィックは、これらの統計から除外されます。

## 対応モデル {#supported-models}

??? "対応モデル"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
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

## ファームウェア v4.11 以降の場合

右上隅にあるスイッチを切り替えて、**Application Total Data** を表示します。

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

このページは 2 つの部分で構成されています。

- **Top 10 Apps by Bandwidth Usage**: 時間ベースのトレンド チャート （過去1日など） を表示し、選択した期間における上位 10 個のアプリケーションの帯域幅消費量を示します。

    グラフの上にマウスを置くと、特定の時点での帯域幅を消費する上位 10 個のアプリのデータ使用量が表示されます。

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: ダウンロード、アップロード、総帯域幅など、各アプリケーションの詳細なトラフィック メトリックが表示されます。必要に応じて、検索バーで特定のアプリを検索します。

    列ヘッダーの横にある並べ替え矢印をクリックして、リストを昇順または降順に並べ替えます。

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### データストレージルール

1. トラフィック統計は 15 秒ごとに RAM に保存され、1 時間ごとにフラッシュに保存されます。フラッシュ メモリの寿命を保護するために、頻繁なフラッシュ書き込みが回避されます。

2. ソフト リブートによってデータが失われることはありません。システムは再起動する前に、まず RAM からフラッシュにデータを書き込みます。

3. （電源を抜き差しすること） のハード リブートまたはファームウェア アップグレード （設定を保持） を行うと、直近 1 時間までのデータが失われる可能性があります。

### クライアントセレクター

クライアント セレクターを使用すると、特定のクライアントを選択することも、デフォルトのすべてのクライアントを維持することもできます。グラフと統計テーブルは自動的に更新され、選択したデバイスのトラフィック データのみが表示されます。

**注**: この機能はファームウェア v4.11 で導入されました。

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### チャートビューの切り替え

アプリのトラフィック統計を表示するときに、必要に応じてグラフの種類を切り替えることができます。

**注**: この機能はファームウェア v4.11 で導入されました。

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: グラフは、選択した時間範囲にわたる帯域幅の使用状況を追跡します。連続的な曲線は、時間の経過とともにトラフィックがどのように変化するかを明らかにするため、使用量の増加傾向と減少傾向を特定するのに最適です。

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: このグラフは、アプリケーション全体の帯域幅使用量を並べて比較しています。個々のバーは、どのアプリがより多くの帯域幅を消費するかを一目で明確に示します。

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: このグラフは、合計帯域幅使用量を割合に分けて示しています。スライスは、各アプリケーションによって使用されるトラフィックの相対的な割合を視覚化します。

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### 時間範囲の切り替え

必要に応じて、時間範囲を過去 1 時間、過去 1 日、過去 1 週間の間で切り替えることができます。

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

選択した時間範囲によって、データの表示方法が決まります。

- **For a closer look （過去1時間など）**: チャートには、きめの細かいリアルタイムの変動が表示されます。ピークはより高く、低下はより急峻であるため、帯域幅使用量の突然の急増を簡単に発見できます。

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **For a broad overview （過去1日または過去1週間など）**: グラフは、データをより長いタイムラインに凝縮します。曲線はより滑らかになり、小さな変化ではなく全体的な交通傾向を示します。

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### 統計の消去

必要に応じて、左上隅のほうきアイコンをクリックして統計をクリアします。

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

クリア後、以下のようにページが更新されます。新しい統計の読み込みが開始されるまで、少しお待ちいただく必要がある場合があります。

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## ファームウェア v4.9 ～ v4.10 の場合

右上隅にあるスイッチを切り替えて、**Application Total Data** を表示します。

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

このページは 2 つの部分で構成されています。

- **Top 10 Apps by Bandwidth Usage**: 時間ベースのトレンド チャート （過去1日など） を表示し、選択した期間における上位 10 個のアプリケーションの帯域幅消費量を示します。

    グラフの上にマウスを置くと、特定の時点での帯域幅を消費する上位 10 個のアプリのデータ使用量が表示されます。

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: ダウンロード、アップロード、合計帯域幅など、各アプリケーションの詳細なトラフィック メトリックが表示されます。必要に応じて、検索バーで特定のアプリを検索します。

    列ヘッダーの横にある並べ替え矢印をクリックして、リストを昇順または降順に並べ替えます。

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### データストレージルール

1. トラフィック統計は 15 秒ごとに RAM に保存され、1 時間ごとにフラッシュに保存されます。フラッシュ メモリの寿命を保護するために、頻繁なフラッシュ書き込みが回避されます。

2. ソフト リブートによってデータが失われることはありません。システムは再起動する前に、まず RAM からフラッシュにデータを書き込みます。

3. ハード リブート （電源を抜き差しすること） またはファームウェア アップグレード （設定を保持） を行うと、直近 1 時間までのデータが失われる可能性があります。

### 時間範囲の切り替え

必要に応じて、時間範囲を過去 1 時間、過去 1 日、過去 1 週間の間で切り替えることができます。

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

選択した時間範囲によって、データの表示方法が決まります。

- **For a closer look （過去1時間など）**: チャートには、きめの細かいリアルタイムの変動が表示されます。ピークはより高く、低下はより急峻であるため、帯域幅使用量の突然の急増を簡単に発見できます。

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **For a broad overview （過去1日または過去1週間など）**: グラフは、データをより長いタイムラインに凝縮します。曲線はより滑らかになり、小さな変化ではなく全体的な交通傾向を示します。

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### 統計の消去

必要に応じて、左上隅のほうきアイコンをクリックして統計をクリアします。

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

クリア後​​、以下のようにページが更新されます。新しい統計の読み込みが開始されるまで、少しお待ちいただく必要がある場合があります。

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

まだ質問がありますか? [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
