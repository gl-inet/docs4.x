# トグルボタンの設定

一部のモデルにはトグルボタンがあり、ウェブ管理パネルでこのボタンの動作をカスタマイズできます。

## 対応モデル

??? "対応モデル"
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-MT1300 (Beryl)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-E750V2 (Mudi V2)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)

??? "非対応モデル"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

ウェブ管理パネルの左側 -> **システム** -> **トグルボタンの設定**

![toggle button settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings.jpg){class="glboxshadow"}

ファームウェアv4.8で前は、4つのオプションがあり、ユーザーがトグルボタンの機能をカスタマイズできます。

- 機能なし
- AdGuard Home
- OpenVPN Client
- Tor
- WireGuard Client

ファームウェアv4.8で降では、より多くのオプションが導入されました：リピーター、Wi-Fi、LED。ユーザーはニーズに応じてトグルボタンをカスタマイズできます。

- 機能なし
- リピーター
- Wi-Fi（メイン/ゲストWi-Fi）
- VPN
- Tor
- AdGuard Home
- LED

![toggle button settings 4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings_4.8.png){class="glboxshadow"}

設定を適用のときには、トグルスイッチのオン/オフ（左/右）位置に基づいて、選択した機能をすぐに有効/無効にするかどうかを決定できます。

**注意**：デバイスの再起動後、システムはトグルスイッチの位置に従って機能を自動的に適用します。

例場合あなたするWireGuard Client設定为よりトグルスイ制御：当スイに左侧（オン）时，WireGuard Clientことになるから動起動。当スイに右侧（オフ）时，WireGuard Client保持無効ステータス。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
