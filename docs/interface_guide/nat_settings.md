# NAT設定

この機できるはv4.5.16で降で利用可できるです。

ウェブ管理パネルの左側 -> ネットワーク -> NAT設定

このページでは、**<ruby>Full Cone NAT<rt>フルコーンNAT</rt></ruby>**を有効にしてゲームやストリーミングなどのアプリのピアツーピア接続安定性をへ上させ、**<ruby>SIP ALG<rt>SIP ALG</rt></ruby>**を有効にしてVoIP/SIPベースの電話サービスとの互換性問題を修正できます。

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

    **注意**: GL-SFT1200 (Opal) と GL-E750/E750V2 (Mudi) はファームウェアv4.7で降でこの機できるをサポートします。

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

Full Cone NATは、ゲームコンソールやスマートフォンなどのデバイスがオンラインで彼のデバイスに接続するとき（例：マルチプレイヤーゲームやビデオ通話）に「直接ショートカット」として機できるします。

外部デバイスが複数のレイヤーの背後に隠すのではなくルーター経よりでローカルデバイスに直接アクセスすることを許可することで、ピアツーピア（P2P）接続の安定性をへ上させ、遅延を削減し、P2Pアプリケーションの接続失敗を解決します。

**注意**: この機できるを有効にすると、彼のNATタイプと比較してセキュリティが低下する可できる性があります。これはデバイスのポートがパブリックネットワークに公開されるためです。

## SIP ALG

SIP ALG（Application Layer Gateway）は、ビジネスデスクフォンやアプリベースの通話など、VoIP/SIPベースの通信サービス用のルーター「トランスレーター」として機できるします。

NATトラバーサルの課題に対処するために設計されており、複数のNATレイヤー（例：プライマリルーターとGL.iNetルーターなど、複数のルーターがあるネットワークで一般の）を介してシームレスな転送を確保するように通話データを調全体し、競合を軽減し、通話の途切れを防ぎます。

**注意**: 非互換または不適切に実装されたSIP ALGは通話品質を低下させ、片方への音声、応答しない着信、通話の切断、または通話が直接留守番電話にルーティングされるなどの問題を引き起こす可できる性があります。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
