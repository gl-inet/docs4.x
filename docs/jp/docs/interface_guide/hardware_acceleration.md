# ハードウェアアクセラレーション

**注意**: この機能はv4.3で降、[ネットワークアクセラレーション](network_acceleration.md)に名称が変更されました。

このガイドはファームウェアv4.2で前に当てはまります。

---

ハードウェアアクセラレーション（ときにハードウェアNAT、フローオフロード、またはオフロードと呼ばれる）は、パケット転送をCPUからルーターのSoC/NICハードウェアに移すことでCPU負荷を軽減します。これにより通例、最大スループットがへ上しCPU使用率が削減されますが、特にLinuxネットワークスタック（netfilter / iptables / nftables）またはSQM（Smart Queue Management）で使用されるカーネルキューイングディシプリン（qdisc）に依存する機能については、重要なトレードオフがあります。

ハードウェアアクセラレーションが有効な場合、以下の機能は正常に動作しません：クライアント速度とトラフィック統計、クライアント速度制限。

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

ウェブ管理パネルの左側 -> ネットワーク -> ハードウェアアクセラレーション。

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

---

## クイック概要

**ハードウェアNAT vs. ソフトウェアNAT**

* スループット（例：マルチギガビットブロードバンド）を最もも重視し、ルーター上のSQMやクライアントごとのシェーピングが必要ない場合 -> ハードウェアNAT / ネットワークアクセラレーションを有効にします。これにより、最も高スループットと最も低CPU使用率が実現されます。

* 低遅延、一貫したQoSクライアントごとの制限が必要、またはSQM（cake/fq_codel）に依存する場合 -> ソフトウェアNATを使用します（ハードウェアオフロードを無効にします）。SQMとQoSはパケットがカーネルqdiscスタックを経よりすることを必要とします。オフロードされたパケットはこのパスをバイパスするため、シェーピングされません。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
