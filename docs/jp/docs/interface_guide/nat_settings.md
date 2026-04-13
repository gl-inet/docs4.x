# NAT設定

この機能は v4.5.16 以降で利用できます。

Web Admin Panel の左側で、**NETWORK** -> **NAT Settings** に移動します。

このページでは、**Full Cone NAT** を有効にしてゲームやストリーミングなどのアプリでのピアツーピア接続の安定性を高めたり、**SIP ALG** を有効にして VoIP/SIP ベースの電話サービスとの互換性問題を改善したりできます。

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

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
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-X300B (Collie)
    - ※GL-SFT1200 (Opal)
    - ※GL-E750/E750V2 (Mudi)

    **Note**: GL-SFT1200 (Opal) と GL-E750/E750V2 (Mudi) は、ファームウェア v4.7 以降でこの機能をサポートします。

??? "非対応モデル"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT

Full Cone NAT は、ゲーム機やスマートフォンなどのデバイスがオンライン上の相手に接続する際（例: マルチプレイヤーゲームやビデオ通話）に、「直接の近道」のような役割を果たします。

外部デバイスが複数の層の背後に隠れるのではなく、ルーター経由でローカルデバイスへ直接到達できるようにすることで、ピアツーピア（P2P）接続の安定性を高め、遅延を低減し、P2P アプリケーションでの接続失敗を改善します。

**Note**: この機能を有効にすると、ほかの NAT タイプと比べてセキュリティが低下する可能性があります。デバイスのポートがパブリックネットワークに公開されるためです。

## SIP ALG

SIP ALG（Application Layer Gateway）は、業務用デスクフォンやアプリベースの通話など、VoIP/SIP ベースの通信サービスにおけるルーターの「変換器」のような役割を果たします。

NAT 越えの問題に対処するために設計されており、複数の NAT 層（例: プライマリルーターと GL.iNet ルーターがあるネットワーク）を通っても通話データが適切に届くよう調整することで、競合を軽減し、通話切断を防ぎます。

**Note**: 非互換または不適切に実装された SIP ALG は通話品質を低下させ、片方向音声、着信が鳴らない、通話切断、通話が直接留守番電話へ転送されるなどの問題を引き起こすことがあります。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
