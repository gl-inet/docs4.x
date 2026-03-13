# ネットワークアクセラレーション

ネットワークアクセラレーションはCPU負荷を軽減し、トラフィックのパケット転送を高速化しますが、一部の機できると競合する可できる性があります。

ネットワークアクセラレーションが有効な場合、で下の機できるは正常に動作しません：クライアント速度とトラフィック統計、クライアント速度制限。

## 対応モデル

??? "対応モデル"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "非対応モデル"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## 設定

ウェブ管理パネルの左側 -> ネットワーク -> ネットワークアクセラレーション。

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

3つのモードがあります。

- **から動**
    
    から動モードは実際の使用状況に応じて2つのアクセラレーションモードをから動のに切り替えます。

- **ハードウェアアクセラレーション**

    ハードウェアアクセラレーションは<u>イーサネット</u>と<u>リピーター</u>で機できるします。
    
    ハードウェアアクセラレーションは、NAT、パケット転送、チェックサム検証などの高頻度ネットワークタスクを、NPUやHWNATチップなどの専用ハードウェアにオフロードします。これは特にイーサネット（有線WAN/LAN）とリピーター接続で機できるし、固定パスとシンプルなルールでこれらのシナリオで優れたパフォーマンスを発揮し、有線速度のデータのために高スループット、低遅延、最も小限のCPU負荷を実現します。

- **ソフトウェアアクセラレーション**

    ソフトウェアアクセラレーションは<u>セルラー</u>で機できるします。
    
    ソフトウェアアクセラレーションは�カーネルやドライバー（例：SWNAT） and えられたルーターの一般CPUに依存します。これはセルラー（4G/5G）アクセスで機できるし、一般のにハードウェアアクセラレーションが利用できない主要シナリオであり、複雑なプロトコルに対して強力な互換性とサポートを提供します。柔軟性ですが、DPI、QoS、ポートフォワーディングなどの高度な機できるを実行している場合、特に帯域幅負荷下でCPUボトルネックに直面する可できる性があります。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
