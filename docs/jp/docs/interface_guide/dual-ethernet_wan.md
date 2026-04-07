# デュアルイーサネットWAN

デュアルイーサネットWAN機能では、デフォルトの LAN1 を2つ目の WAN ポートに切り替えて、デュアルイーサネット接続を実現できます。これにより、信頼性の高いバックアップ接続が可能になり、対応モデルでは帯域幅の集約もサポートされるため、高負荷な用途にも適しています。また、追加のハードウェアなしで、仕事用と個人用など2つの別々のネットワークへ同時接続することもできます。

## 対応モデル

??? "対応モデル"
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **注意**: GL-E5800 (Mudi 7) には、イーサネットポートが1つ（デフォルトは LAN、WAN へ切り替え可能）と、**OTG対応 USB-C ポート** が搭載されています。デュアルイーサネットWAN用に2つ目のイーサネットポートを追加するには、別売りの USB‑C‑to‑Ethernet アダプターを USB‑C ポートへ接続してください。

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

1. ルーターの Web 管理パネルにログインします。

2. **NETWORK** -> **Port Management** -> **LAN** タブに移動し、ポートのプロパティを WAN に切り替えて **Apply** をクリックします。

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_1.png){class="glboxshadow"}

3. ポップアップウィンドウで **Apply** をクリックします。

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_2.png){class="glboxshadow"}

4. デュアルイーサネットWANを有効にした後は、[こちら](../interface_guide/multi-wan.md)でマルチWAN機能を設定できます。

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
