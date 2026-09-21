# SQM (Smart Queue Management)

**注**: この機能はファームウェア v4.9 で導入されました。 Mango 2 (GL-MG1300) などの一部のモデルは、ファームウェア v4.9 以降を実行している場合でも、メモリ不足のため SQM をサポートしません。

Web 管理パネルの左側で、**FLOW CONTROL** -> **SQM** に移動します。

SQM (Smart Queue Management) は、ルーターのネットワーク トラフィックをインテリジェントに管理して、遅延と「バッファー肥大化」を最小限に抑え、スムーズなゲームと音声通話を保証します。

**注**:

1. この機能は、ルータがゲートウェイとして動作している場合にルータを通過するトラフィック (ローカル クライアント トラフィックや VPN クライアント トラフィックなど) にのみ影響します。ルーターが VPN サーバーとして機能する場合、受信トラフィックには適用されません。
2. SQM はリソースを大量に消費するため、低帯域幅または混雑したネットワークに最適に機能します。高速接続でこれを有効にすると、ピーク スループットが低下する可能性があります。
3. ルータがドロップイン ゲートウェイ モードの場合、SQM は有効になりません。
4. SQM と QoS を同時に有効にすることはできません。
5. SQM はネットワーク アクセラレーションと併用できません。 SQM を有効にすると、安定したパフォーマンスを確保するためにネットワーク アクセラレーションが自動的に無効になります。

## ファームウェア v4.11 以降の場合

スイッチを切り替えて SQM を有効にし、以下の手順に従って構成を完了します。

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    WAN のアップロード速度とダウンロード速度 （入力範囲：1～10000） を手動で入力するか、**Run Speedtest** をクリックして速度を測定し、フィールドに自動的に入力します。速度テストを実行するには、アクティブなインターネット接続が必要です。

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **注**: 入力フィールドに入力された値は、**Mbps** （メガビット/秒） です。同等の **MB/s** （メガバイト/秒） が参考のために表示されます。

2. **Queue Discipline**

    キューイング ルールを選択してトラフィックを管理し、負荷時の待ち時間を短縮します。

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: 優れた全体的な遅延制御を備えたスマートな自動トラフィック シェーピング （推奨）。

        **cake** がキュー規律として選択されている場合、**Cake Autorate** はオプション機能として使用できます。

        Cake Autorate は、プローブ RTT に基づいてリアルタイムで CAKE 帯域幅を増減するレイテンシー駆動のシェーパーです。アクティブな速度テストは実行されません。軽量の ping のみが使用されます。 WAN 帯域幅が変動する場合は常に推奨されます。安定したリンクでは必要ありません。

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **注**: Cake Autorate は継続的なバックグラウンド プローブ トラフィックを生成します。従量制課金接続を使用する場合は、この追加のデータ使用量を考慮してください。

        デフォルト設定は、ほとんどの接続に適しています。以下のパラメータが Cake Autorate にどのように影響するかを理解している場合にのみ変更してください。必要に応じて、**Reset to Default** をクリックしてデフォルトのプローブとしきい値の設定を復元します。

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: ネットワーク品質の調査に使用される、カンマで区切られた IP アドレスのリスト。

        - **Probe Interval**: 間隔を短くすると応答が速くなりますが、より多くの CPU リソースを消費します。

        - **Concurrent Probes**: 同時プローブの数はプローブ サーバーの数を超えてはなりません。値を大きくすると、CPU 負荷が増加します。

        - **Idle Detection Threshold**: 転送速度がこの値を下回ると、接続はアイドル状態とみなされます。この値は、設定された速度制限の 25% を超えてはなりません。

        - **Download Latency Threshold**: ダウンロードの遅延がこのしきい値を超えると、帯域幅の削減がトリガーされます。

        - **Upload Latency Threshold**: アップロードの遅延がこのしきい値を超えると、帯域幅の削減がトリガーされます。

    - **fq_codel**: 基本的な遅延を削減した、シンプルで効率的な公平なキューイング。

## ファームウェア v4.9 ～ v4.10 の場合

スイッチを切り替えて SQM を有効にし、トラフィック スケジュールの最大アップロード速度とダウンロード速度 （入力範囲：1～10000） を設定します。最良の結果を得るには、実際のインターネット帯域幅に合わせてください。

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**注**: 入力フィールドに入力された値は、**Mbps** （メガビット/秒） です。同等の **MB/s** （メガバイト/秒） が参考のために表示されます。

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

キュー ルールでは、次の 2 つのオプションを使用できます。

- **cake**: 優れた全体的な遅延制御を備えたスマートな自動トラフィック シェーピング （推奨）。

- **fq_codel**: 基本的な遅延を削減した、シンプルで効率的な公平なキューイング。

!!! tip

    QoS 設定と SQM 設定の違いは、QoS ではアプリケーションの優先順位を設定でき、それに応じてルーターが帯域幅を割り当てることです。一方、SQM ではキュー ルールを選択できます。

---

まだ質問がありますか? [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
