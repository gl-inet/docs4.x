# データ統計

データ統計は、アプリケーションごとのネットワーク利用状況を分類して可視化するインテリジェントなトラフィックインサイトダッシュボードです。リアルタイムおよび過去のトラフィックを監視できるため、ネットワーク状況の把握と制御に役立ちます。

**Note**:

1. この機能は現在 **GL-MT5000 (Brume 3)** でのみ利用できます。

2. この機能は **Network Acceleration** と同時には使用できません。有効にすると、正常に動作させるため **Network Acceleration** は自動的に無効になります。

---

## クイックセットアップ

Web Admin Panel の左側で、**FLOW CONTROL** > **Data Statistics** に移動します。

右上のスイッチをオンにすると、**Application Total Data** を表示できます。

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage**: 選択した期間における上位 10 個のアプリの帯域幅使用量を、時間ベースのトレンドチャート（例: 過去 1 日）で表示します。

    必要に応じて、表示期間を Past Hour、Past Day、Past Week に切り替えられます。

- **App Traffic Statistics**: 各アプリケーションの Download、Upload、Total Bandwidth などの詳細なトラフィック指標を表示します。

    必要に応じて、検索バーで特定のアプリを検索できます。

## データ保存ルール

1. トラフィック統計は 15 秒ごとに RAM へ保存され、1 時間ごとにフラッシュへ書き込まれます。フラッシュメモリの寿命を保護するため、頻繁な書き込みは避けられています。

2. ソフト再起動ではデータは失われません。再起動前に、システムが RAM 内のデータを先にフラッシュへ書き込みます。

3. ハード再起動（電源の抜き差し）やファームウェア更新（設定保持あり）では、直近 1 時間分までのデータが失われる場合があります。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
