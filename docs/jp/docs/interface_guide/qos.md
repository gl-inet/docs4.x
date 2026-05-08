# QoS（Quality of Service）

QoS（Quality of Service）は、ネットワーク混雑時に重要なアクティビティ（ビデオ通話、ゲームなど）を優先して帯域幅配分を最適化し、遅延を抑えながら全体的なネットワーク性能を向上させます。

**Note**:

1. この機能は、ルーターがゲートウェイとして動作しているときに通過するトラフィックにのみ影響します。これにはローカルクライアントのトラフィックと VPN Client のトラフィックが含まれます。ルーターが VPN Server として動作しているときの受信トラフィックには適用されません。
2. QoS は、ルーターが Drop-in Gateway モードのときは動作しません。
3. QoS と SQM を同時に有効にすることはできません。
4. QoS は **Network Acceleration** と併用できません。有効にすると、安定したパフォーマンスを確保するため **Network Acceleration** は自動的に無効になります。

## 対応モデル

!!! note "Supported Models"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    ※ が付いたモデルは、ファームウェア v4.9 以降で QoS をサポートします。

## クイックセットアップ

Web Admin Panel の左側で、**FLOW CONTROL** -> **QoS** に移動します。

スイッチをオンにして QoS を有効にすると、ページは以下のように表示されます。

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

トラフィックスケジューリングのため、最大アップロード速度と最大ダウンロード速度を設定します（入力範囲: 1 - 10000）。最適な結果を得るには、実際のインターネット帯域幅に合わせて設定してください。

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Note**: 入力欄の値は **Mbps**（メガビット毎秒）です。参考用として、換算後の **MB/s**（メガバイト毎秒）も表示されます。

その後、アプリケーションごとの優先度を設定すると、ルーターがその設定に応じて帯域幅を割り当てます。

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## アプリ優先度をカスタマイズする

アプリケーション優先度をカスタマイズするには、**Customize** を選択して **Pre-Set up** をクリックします。

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

ポップアップウィンドウでは、すべてのカテゴリがデフォルトで Medium Priority に設定されています。

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

各カテゴリをドラッグして必要に応じて優先度を調整し、**Confirm** をクリックします。

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
