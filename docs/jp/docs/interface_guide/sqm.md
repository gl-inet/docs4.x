# SQM（Smart Queue Management）

SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延や「bufferbloat」を抑え、ゲームや音声通話をより快適にします。

**Note**:

1. この機能は、ルーターがゲートウェイとして動作しているときに通過するトラフィックにのみ影響します。これにはローカルクライアントのトラフィックと VPN Client のトラフィックが含まれます。ルーターが VPN Server として動作しているときの受信トラフィックには適用されません。

2. SQM はリソース消費が大きいため、低帯域幅または混雑したネットワークで特に効果を発揮します。高速回線で有効にすると、ピークスループットが低下する場合があります。

3. SQM は、ルーターが Drop-in Gateway モードのときは動作しません。

4. SQM と QoS を同時に有効にすることはできません。

5. SQM は **Network Acceleration** と併用できません。有効にすると、安定したパフォーマンスを確保するため **Network Acceleration** は自動的に無効になります。

## 対応モデル

!!! note "Supported Models"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    ※ が付いたモデルは、ファームウェア v4.9 以降で SQM をサポートします。

## クイックセットアップ

Web Admin Panel の左側で、**FLOW CONTROL** -> **SQM** に移動します。

スイッチをオンにして SQM を有効にし、トラフィックスケジューリング用の最大アップロード速度と最大ダウンロード速度を設定します（入力範囲: 1 - 10000）。最適な結果を得るには、実際のインターネット帯域幅に合わせて設定してください。

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Note**: 入力欄の値は **Mbps**（メガビット毎秒）です。参考用として、換算後の **MB/s**（メガバイト毎秒）も表示されます。

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Queue Rule には次の 2 つのオプションがあります。

- **cake**: 全体的な遅延制御に優れた、スマートで自動的なトラフィックシェーピングです（推奨）。

- **fq_codel**: シンプルで効率的な公平キューイングで、基本的な遅延軽減を行います。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
