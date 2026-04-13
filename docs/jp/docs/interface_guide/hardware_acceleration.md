# ハードウェアアクセラレーション

**Note**: このガイドはファームウェア v4.2 以前に適用されます。新しいバージョンについては、[Network Acceleration](network_acceleration.md) を参照してください。

---

ハードウェアアクセラレーション（hardware NAT、flow offloading、offloading とも呼ばれます）は、パケット転送処理を CPU からルーターの SoC/NIC ハードウェアへ移すことで CPU 負荷を軽減します。通常は最大スループットの向上と CPU 使用率の低減が期待できますが、Linux ネットワークスタック（netfilter/iptables/nftables）や、SQM（Smart Queue Management）で使われるカーネルのキューイング制御（qdisc）に依存する機能では重要なトレードオフがあります。

ハードウェアアクセラレーションを有効にすると、次の機能は正しく動作しません: Client Speed and Traffic Statistics、Client Speed Limit。

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

## クイック設定

Web Admin Panel の左側で、**NETWORK** -> **Hardware Acceleration** に移動します。

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

スイッチをオンにして、**Apply** をクリックします。

---

## Hardware NAT と Software NAT

* スループット（例: マルチギガビット回線）を最優先し、ルーター上で SQM やクライアントごとの帯域制御を使わない場合は、Hardware NAT / Network Acceleration を有効にしてください。最も高いスループットと低い CPU 使用率を実現できます。

* 低遅延、一貫した QoS、クライアント単位の制限が重要で、SQM（cake/fq_codel）を利用する場合は、Software NAT（ハードウェアオフロード無効）を使用してください。SQM と QoS はパケットがカーネルの qdisc スタックを通過する必要がありますが、オフロードされたパケットはこの経路を通らないため、帯域制御されません。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
