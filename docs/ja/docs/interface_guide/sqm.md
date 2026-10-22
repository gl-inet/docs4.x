# SQM (Smart Queue Management) {#sqm-smart-queue-management}

**注**: この機能はファームウェア v4.9 で導入されました。

Mango 2 (GL-MG1300) など一部のモデルは、メモリ不足のため、ファームウェア v4.9 以降でも SQM に対応しません。

---

Web 管理パネルの左側で、**FLOW CONTROL** -> **SQM** に移動します。

SQM (Smart Queue Management) は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファーブロート（bufferbloat）」を最小限に抑え、ゲームや音声通話をよりスムーズにします。

**注**:

1. この機能は、ルーターがゲートウェイとして動作しているときにルーターを通過するトラフィック（ローカルクライアントのトラフィックや VPN クライアントのトラフィックを含む）にのみ影響します。ルーターが VPN サーバーとして動作している場合の受信トラフィックには適用されません。
2. SQM はリソースを大量に消費するため、低帯域幅または混雑したネットワークで最も効果を発揮します。高速回線で有効にすると、ピークスループットが低下する場合があります。
3. ルーターが Drop-in Gateway モードの場合、SQM は動作しません。
4. SQM と QoS を同時に有効にすることはできません。
5. SQM は Network Acceleration と併用できません。SQM を有効にすると、安定したパフォーマンスを確保するため Network Acceleration は自動的に無効になります。

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

スイッチをオンにして SQM を有効にし、以下の手順に従って設定を完了します。

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    WAN のアップロード速度とダウンロード速度（入力範囲：1～10000）を手動で入力するか、**Run Speedtest** をクリックして速度を測定し、自動入力します。速度テストを実行するには、インターネットに接続されている必要があります。

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **注**: 入力フィールドの値の単位は **Mbps**（メガビット/秒）です。参考として、換算した **MB/s**（メガバイト/秒）が表示されます。

2. **Queue Discipline**

    トラフィックを管理し、高負荷時の遅延を低減するためのキューイングルールを選択します。

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: 全体的な遅延制御に優れた、スマートな自動トラフィックシェーピングです（推奨）。

        Queue Discipline として **cake** を選択した場合は、オプション機能として **Cake Autorate** を使用できます。

        Cake Autorate は、プローブの RTT に基づいて CAKE の帯域幅をリアルタイムで増減する、遅延ベースのシェーパーです。速度テストは実行せず、軽量な ping のみを使用します。WAN 帯域幅が変動する環境では有効にすることを推奨します。安定した回線では必要ありません。

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **注**: Cake Autorate はバックグラウンドでプローブトラフィックを継続的に発生させます。従量制の回線を使用している場合は、この追加のデータ使用量を考慮してください。

        デフォルト設定はほとんどの接続に適しています。以下のパラメーターは、Cake Autorate への影響を理解している場合にのみ変更してください。必要に応じて **Reset to Default** をクリックすると、プローブとしきい値の設定をデフォルトに戻せます。

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: ネットワーク品質のプローブに使用する IP アドレスのリストです（カンマ区切り）。

        - **Probe Interval**: 間隔を短くすると応答が速くなりますが、より多くの CPU リソースを消費します。

        - **Concurrent Probes**: 同時プローブ数はプローブサーバーの数を超えないようにする必要があります。値を大きくすると CPU 負荷が増加します。

        - **Idle Detection Threshold**: 転送速度がこの値を下回ると、接続はアイドル状態とみなされます。この値は、設定した速度制限の 25% 以下にする必要があります。

        - **Download Latency Threshold**: ダウンロードの遅延がこのしきい値を超えると、帯域幅が引き下げられます。

        - **Upload Latency Threshold**: アップロードの遅延がこのしきい値を超えると、帯域幅が引き下げられます。

    - **fq_codel**: 基本的な遅延低減機能を備えた、シンプルで効率的なフェアキューイングです。

## ファームウェア v4.9 ～ v4.10 の場合 {#for-firmware-v49-to-v410}

スイッチをオンにして SQM を有効にし、トラフィック制御に使用する最大アップロード速度と最大ダウンロード速度（入力範囲：1～10000）を設定します。最適な効果を得るには、実際のインターネット帯域幅に合わせて設定してください。

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**注**: 入力フィールドの値の単位は **Mbps**（メガビット/秒）です。参考として、換算した **MB/s**（メガバイト/秒）が表示されます。

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Queue Rule では、次の 2 つのオプションを選択できます。

- **cake**: 全体的な遅延制御に優れた、スマートな自動トラフィックシェーピングです（推奨）。

- **fq_codel**: 基本的な遅延低減機能を備えた、シンプルで効率的なフェアキューイングです。

!!! tip

    QoS と SQM の設定の違いは、QoS ではアプリケーションの優先順位を設定し、ルーターがそれに応じて帯域幅を割り当てるのに対し、SQM ではキュールールを選択する点です。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
