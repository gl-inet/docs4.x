# ネットワークアクセラレーション

Network Acceleration は CPU 負荷を軽減し、トラフィックのパケット転送を高速化しますが、一部の機能と競合する場合があります。

Network Acceleration を有効にすると、次の機能は正しく動作しません: Client Speed and Traffic Statistics、Client Speed Limit。

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

Web Admin Panel の左側で、**NETWORK** -> **Network Acceleration** に移動します。

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

3 つのモードがあります。

- **Auto**
    
    Auto モードでは、実際の使用状況に応じて 2 つのアクセラレーションモードが自動的に切り替わります。

- **Hardware Acceleration**

    Hardware Acceleration は <u>Ethernet</u> と <u>Repeater</u> で動作します。
    
    Hardware Acceleration は、NAT、パケット転送、チェックサム検証などの高頻度ネットワーク処理を NPU や HWNAT チップなどの専用ハードウェアへオフロードします。特に Ethernet（有線 WAN/LAN）と Repeater 接続で有効で、固定された通信経路とシンプルなルールの環境で高いスループット、低遅延、低 CPU 負荷を実現します。

- **Software Acceleration**

    Software Acceleration は <u>Cellular</u> で動作します。
    
    Software Acceleration は、最適化されたカーネルやドライバー（例: SWNAT）と組み合わせたルーターの汎用 CPU に依存します。Cellular（4G/5G）アクセスで利用されることが多く、ハードウェアアクセラレーションが使えない環境でも高い互換性と複雑なプロトコルへの対応を提供します。一方で、DPI、QoS、Port Forwarding などの高度な機能を使用している場合は、特に高帯域時に CPU がボトルネックになることがあります。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
