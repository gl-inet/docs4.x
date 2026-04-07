# トグルボタン設定

Toggle Button Settings では、ルーター本体の物理トグルスイッチ（一部モデルでは mode switch とも呼ばれます）に特定の機能を割り当て、よく使う操作へすばやくアクセスできる便利なショートカットとして利用できます。

Web管理パネルで、このスイッチの動作をカスタマイズできます。

## 対応モデル

??? "Supported Models"
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

??? "Unsupported Models"
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

## Setup

Web管理パネルの左側で、**SYSTEM** -> **Toggle Button Settings** に移動します。

![toggle button settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings.jpg){class="glboxshadow"}

ファームウェア v4.8 より前では、トグルボタンの機能をカスタマイズできるオプションは以下のとおりです。

- No Function
- AdGuard Home
- OpenVPN Client
- Tor
- WireGuard Client

ファームウェア v4.8 以降では、Repeater、Wi-Fi、LED が追加され、より多くの選択肢からニーズに合わせて設定できます。

- No Function
- Repeater
- Wi-Fi (Main/Guest Wi-Fi)
- VPN
- Tor
- AdGuard Home
- LED

![toggle button 4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_4.8.png){class="glboxshadow"}

設定を適用する際は、トグルスイッチの on/off（left/right）位置に応じて、選択した機能をすぐに有効/無効にするかどうかを決められます。

**Note**: デバイスを再起動すると、システムはトグルスイッチの位置に応じて機能の状態を自動的に適用します。

たとえば、WireGuard Client をトグルスイッチで制御するよう設定した場合、スイッチが LEFT (ON) なら WireGuard Client は自動的に起動します。スイッチが RIGHT (OFF) なら WireGuard Client は無効のままです。

---

ご不明な点がありましたら、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
