# データ統計

データ統計は、アプリケーションやプロトコルごとのネットワーク利用状況を把握できる、直感的なトラフィックダッシュボードです。過去 1 時間、1 日、7 日の履歴トレンド表示、利用ランキング、デバイスごとのトラフィック監視、不要なアプリのワンクリックブロックに対応しています。

**Note**:

1. データ統計は、ルーターが Drop-in Gateway モードのときは動作しません。
2. データ統計は **Network Acceleration** と併用できません。有効にすると、安定したパフォーマンスを確保するため **Network Acceleration** は自動的に無効になります。

## 対応モデル

!!! note "Supported Models"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## クイックセットアップ

Web Admin Panel の左側で、**FLOW CONTROL** -> **Data Statistics** に移動します。

右上のスイッチをオンにすると、**Application Total Data** を表示できます。

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

このページは 2 つの部分で構成されています。

- **Top 10 Apps by Bandwidth Usage**: 選択した期間における上位 10 個のアプリの帯域幅使用量を、時間ベースのトレンドチャート（例: 過去 1 日）で表示します。

    グラフにマウスカーソルを合わせると、特定時点における帯域幅消費量上位 10 個のアプリのデータ使用量を確認できます。

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: 各アプリケーションの Download、Upload、Total Bandwidth などの詳細なトラフィック指標を表示します。必要に応じて、検索バーで特定のアプリを検索できます。

    列ヘッダー横の並べ替え矢印をクリックすると、昇順または降順で一覧を並べ替えられます。

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## データ保存ルール

1. トラフィック統計は 15 秒ごとに RAM へ保存され、1 時間ごとにフラッシュへ書き込まれます。フラッシュメモリの寿命を保護するため、頻繁な書き込みは避けられています。

2. ソフト再起動ではデータは失われません。再起動前に、システムが RAM 内のデータを先にフラッシュへ書き込みます。

3. ハード再起動（電源の抜き差し）やファームウェア更新（設定保持あり）では、直近 1 時間分までのデータが失われる場合があります。

## 表示期間を切り替える

必要に応じて、Past hour、Past day、Past week の表示期間を切り替えられます。

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

選択した表示期間によって、データの見え方が変わります。

- **細かく確認したい場合（例: Past Hour）**: グラフには、より細かいリアルタイムの変動が表示されます。ピークは高く、落ち込みは急になり、帯域幅使用量の急増を把握しやすくなります。

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **全体像を確認したい場合（例: Past Day または Past Week）**: グラフはより長いタイムラインにデータを集約して表示します。曲線はなめらかになり、細かな変化よりも全体的なトラフィック傾向を把握しやすくなります。

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

## 統計をクリアする

必要に応じて、左上のほうきアイコンをクリックして統計をクリアできます。

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

クリア後、ページは以下のように更新されます。新しい統計の読み込みが始まるまで、少し待つ必要がある場合があります。

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
