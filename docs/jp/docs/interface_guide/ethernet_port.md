# Ethernet Port

**Note**: このページはファームウェア v4.7 では **Port Management** として利用可能で、ファームウェア v4.8.3 で **Ethernet Port** に名称変更されました。

---

Web Admin Panel の左側で、**NETWORK** -> **Port Management** または **Ethernet Port** に移動します。

Ethernet ポートの役割（WAN/LAN）を管理し、MAC アドレスやネゴシエート速度などのポート詳細を確認できます。

## WAN

このセクションには、ポートの役割（WAN または LAN）、MAC アドレス、ネゴシエート速度が表示されます。

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

- **WAN/LAN**: 物理 WAN ポートの現在の動作モードです。必要に応じて LAN に設定できます。

- **MAC Mode**: デフォルトは Factory Mode です。Clone Mode または Random Mode に切り替えられます。

- **Mac Address**: WAN インターフェースの MAC アドレスです。

- **Negotiated Network Port Rate**: WAN インターフェースのリンク速度交渉結果です。有効なリンクが検出された場合にのみ表示されます。

## LAN

このセクションには、LAN ポートのネゴシエート速度が表示されます。有効なリンクが検出された場合にのみ表示されます。

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

一部のモデルでは、デュアルイーサネットWAN構成のために LAN 1 を WAN ポートへ切り替えることができます。詳細は [Dual-Ethernet WAN](#dual-ethernet-wan) を参照してください。

## Dual-Ethernet WAN

Dual-Ethernet WAN機能では、デフォルトの LAN イーサネットポートを2つ目の WAN ポートに切り替えて、デュアルイーサネットによるインターネット接続を利用できます。これにより、信頼性の高いバックアップ接続が可能になり、対応モデルでは帯域幅の集約もサポートされるため、帯域幅を多く使う用途にも対応できます。また、追加のハードウェアなしで、仕事用と個人用など2つの独立したネットワークへ同時に接続することもできます。

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

    **注意**: GL-E5800 (Mudi 7) には、イーサネットポートが1つ（デフォルトは LAN、WAN へ切り替え可能）と、**OTG対応 USB-C ポート** が搭載されています。Dual-Ethernet WAN用に2つ目のイーサネットポートを追加するには、別売りの USB-C-to-Ethernet アダプターを USB-C ポートへ接続してください。

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

LAN ポートを WAN ポートへ切り替えるには、以下の手順を実行します。

1. **Port Management** または **Ethernet Port** ページで **LAN** タブをクリックし、ポートの役割を WAN に切り替えてから **Apply** をクリックします。

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. ポップアップウィンドウで **Apply** をクリックします。

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. 選択したポートは WAN ポートとして動作します。続けて [こちら](multi-wan.md) で Multi-WAN を設定できます。

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
