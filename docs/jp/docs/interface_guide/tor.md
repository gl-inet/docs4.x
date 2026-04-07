# Tor

Tor（**The Onion Router** の略）は、匿名通信を実現するための無償のオープンソースソフトウェアです。プライバシーを保ちながらインターネットを利用するのに役立ちます。詳しくは [Tor について](https://www.torproject.org/){target="_blank"} をご覧ください。

**Note**: この機能は現在ベータ版であり、一部の国では問題が発生する可能性があります。Tor を有効にすると、以下の機能は正常に動作しません。

  - VPN
  - DNS
  - IPv6
  - ADGuard Home

## 対応モデル

??? "対応モデル"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Note**: * が付いたモデルは Tor をネイティブではサポートしていませんが、プラグインを使って手動でインストールできます。詳しくは [こちら](#manual-install) をご覧ください。

??? "非対応モデル"
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## クイックセットアップ

Web 管理パネル左側の **VPN** -> **Tor** を開きます。

ファームウェア ver.4.8.4 以降では、**APPLICATIONS** -> **Tor** を開いてください。

トグルスイッチをクリックして有効にし、必要に応じて **Custom Exit Nodes** を有効にしてから **Apply** をクリックします。

![enable tor](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/enable_tor.png){class="glboxshadow"}

接続が開始されます。ネットワークが要件を満たしていれば、接続済みと表示されます。

![tor connected](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/connected.png){class="glboxshadow" width="672"}

## 手動インストール {#manual-install}

**Note**: 一部のモデルではプラグインを使用して Tor を手動でインストールできますが、CPU 負荷が上がり、システム応答が遅くなる可能性があります。

Web 管理パネル左側の **APPLICATIONS** -> **Plug-ins** を開きます。

**gl-sdk4-ui-torview** を検索してインストールします。

![torview](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torpage.jpg){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
