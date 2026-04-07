# SQM（Smart Queue Management）

SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延や「bufferbloat」を抑え、ゲームや音声通話をより快適にします。

**Note**:

1. この機能は現在 **GL-MT5000 (Brume 3)** でのみ利用できます。

2. この機能は、ルーターがゲートウェイとして処理するトラフィック（ローカルクライアントのトラフィックと VPNクライアントのトラフィックを含む）に影響しますが、ルーターが VPNサーバー として動作しているときの受信トラフィックには影響しません。

3. SQM はリソース消費が大きいため、低帯域幅または混雑したネットワークで特に効果を発揮します。高速回線で有効にすると、ピークスループットが低下する場合があります。

---

Web Admin Panel の左側で、**FLOW CONTROL** > > **SQM** に移動します。

トラフィックスケジューリングのため、最初に最大アップロード速度と最大ダウンロード速度を設定します（入力範囲: 1 - 10000）。最適な結果を得るには、実際のインターネット帯域幅に合わせて設定してください。

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

Queue Rule には次の 2 つのオプションがあります。

- **cake**: 全体的な遅延制御に優れた、スマートで自動的なトラフィックシェーピングです（推奨）。

- **fq_codel**: シンプルで効率的な公平キューイングで、基本的な遅延軽減を行います。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
