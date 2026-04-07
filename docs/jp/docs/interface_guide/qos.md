# QoS（Quality of Service）

QoS（Quality of Service）は、ネットワークが混雑しているときに重要なアクティビティ（ビデオ通話、ゲームなど）を優先して帯域幅を最適化し、遅延を抑えて全体的なネットワーク性能を向上させます。

**Note**:

1. この機能は現在 **GL-MT5000 (Brume 3)** でのみ利用できます。

2. この機能は、ルーターがゲートウェイとして処理するトラフィック（ローカルクライアントのトラフィックと VPNクライアントのトラフィックを含む）に影響しますが、ルーターが VPNサーバー として動作しているときの受信トラフィックには影響しません。

---

Web Admin Panel の左側で、**FLOW CONTROL** > **QoS** に移動します。

トラフィックスケジューリングのため、最初に最大アップロード速度と最大ダウンロード速度を設定します（入力範囲: 1 - 10000）。最適な結果を得るには、実際のインターネット帯域幅に合わせて設定してください。

次に、アプリケーションごとの優先度を設定すると、ルーターがその設定に応じて帯域幅を割り当てます。

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
