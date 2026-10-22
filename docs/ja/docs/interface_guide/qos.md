# QoS (Quality of Service) {#qos-quality-of-service}

**注**: この機能はファームウェア v4.9 で導入されました。

Mango 2 (GL-MG1300) など一部のモデルは、メモリ不足のため、ファームウェア v4.9 以降でも QoS に対応しません。詳しくは[対応モデル](#supported-models)をご覧ください。

---

Web 管理パネルの左側で、**FLOW CONTROL** -> **QoS** に移動します。

QoS (Quality of Service) は、ネットワークの混雑時に重要なアクティビティ（ビデオ通話、ゲームなど）を優先して帯域幅の割り当てを最適化し、遅延を低減してネットワーク全体のパフォーマンスを向上させます。

**注**:

1. この機能は、ルーターがゲートウェイとして動作しているときにルーターを通過するトラフィック（ローカルクライアントのトラフィックや VPN クライアントのトラフィックを含む）にのみ影響します。ルーターが VPN サーバーとして動作している場合の受信トラフィックには適用されません。
2. ルーターが Drop-in Gateway モードの場合、QoS は動作しません。
3. QoS と SQM を同時に有効にすることはできません。
4. QoS は Network Acceleration と併用できません。QoS を有効にすると、安定したパフォーマンスを確保するため Network Acceleration は自動的に無効になります。

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

スイッチをオンにして QoS を有効にし、以下の手順に従って設定を完了します。

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    WAN のアップロード速度とダウンロード速度（入力範囲：1～10000）を手動で入力するか、**Run Speedtest** をクリックして速度を測定し、自動入力します。速度テストを実行するには、インターネットに接続されている必要があります。

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **注**: 入力フィールドの値の単位は **Mbps**（メガビット/秒）です。参考として、換算した **MB/s**（メガバイト/秒）が表示されます。

2. **Scheduling Policy**

    ポリシーモードを 1 つ選択できます。Advanced ルールに一致したトラフィックには、基本ポリシーより Advanced ルールが優先して適用されます。

    - **Device Priority**

        このモードでは、WAN 接続が混雑しているときに、選択したローカルクライアントのネットワーク優先度が高くなります。**Add Device** をクリックし、WAN の負荷が高いときに帯域幅を優先的に割り当てるデバイスを選択します。

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        クライアント名、MAC アドレス、または IP アドレスでデバイスを検索できます。対象のデバイスを選択し、**Apply** をクリックします。

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        このモードでは、さまざまなアプリケーションの優先順位を設定できます。ルーターはそれに応じて帯域幅を割り当てます。

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        アプリケーションの優先順位をカスタマイズするには、**Customize** を選択し、**Pre-Set up** をクリックします。

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        ポップアップウィンドウでは、すべてのカテゴリがデフォルトで Medium Priority に設定されています。

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        必要に応じてカテゴリをドラッグして優先度を調整し、**Confirm** をクリックします。

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        このモードでは、優先度の高いトラフィック用の高度な QoS ルールを作成できます。**Add Rule** をクリックして、プロトコル、ポート、送信元 IP に基づくルールを定義します。

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Name、Protocol、Source Address、Destination Port を指定し、**Apply** をクリックします。

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## ファームウェア v4.9 ～ v4.10 の場合 {#for-firmware-v49-to-v410}

スイッチをオンにして QoS を有効にすると、ページが次のように表示されます。

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

トラフィック制御に使用する最大アップロード速度と最大ダウンロード速度（入力範囲：1～10000）を設定します。最適な効果を得るには、実際のインターネット帯域幅に合わせて設定してください。

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**注**: 入力フィールドの値の単位は **Mbps**（メガビット/秒）です。参考として、換算した **MB/s**（メガバイト/秒）が表示されます。

次に、さまざまなアプリケーションの優先順位を設定します。ルーターはそれに応じて帯域幅を割り当てます。

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

アプリケーションの優先順位をカスタマイズするには、**Customize** を選択し、**Pre-Set up** をクリックします。

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

ポップアップウィンドウでは、すべてのカテゴリがデフォルトで Medium Priority に設定されています。

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

必要に応じてカテゴリをドラッグして優先度を調整し、**Confirm** をクリックします。

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
