# デュアルイーサネットWAN

デュアルイーサネットWAN機能を使用すると、デフォルトのLAN1を2番目のWANポートに切り替えることができ、デュアルバンド幅聚合（対応している場合）で高必要用途に信頼性の高いバックアップ接続を提供します。また、仕事と個人など2つの独立したネットワークに同時に接続でき、追加のハードウェアなしで柔軟性をへ上できます。

## 対応モデル

??? "対応モデル"
    - ※GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **注意**: GL-E5800 (Mudi 7)には1つのイーサネットポート（デフォルトLAN、WANに切り替え可能）と**<ruby>OTG対応<rt>OTG対応</rt></ruby>USB-Cポート**が装備されています。デュアルイーサネットWAN用の2番目のイーサネットポートを追加するには、USB-Cポートに別途販売されているUSB-C-to-イーサネットアダプタを接続してください。

??? "非対応モデル"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## セットアップ

1. ルーターのウェブ管理パネルにログインします。

2. **ネットワーク** -> **ポート管理** -> **LAN**タブに移動し、ポートのプロパティをWANに切り替えて、**適用**をクリックします。

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_1.png){class="glboxshadow"}

3. ポップアップウィンドウで、**適用**をクリックします。

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_2.png){class="glboxshadow"}

4. デュアルイーサネットWANを有効にすると、[こちら](../interface_guide/multi-wan.md)でマルチWAN機能を設定できます。
