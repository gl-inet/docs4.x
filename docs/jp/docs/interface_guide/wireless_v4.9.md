# ワイヤレス（ファームウェア v4.9）

> このガイドはファームウェア v4.9 以降に適用されます。以前のバージョンについては [こちら](wireless.md) をクリックしてください。

Web Admin Panel の左側で、**WIRELESS** に移動します。

Wireless ページでは、MLO Wi-Fi（対応モデルのみ）、Main Network、Guest Network、IoT Network など、各種 Wi-Fi ネットワークを設定できます。対応する Wi-Fi バンドはモデルによって異なります。

## Multi-Link Operation (MLO)

??? "対応モデル"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "非対応モデル"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO（Multi-Link Operation）は Wi-Fi 7（802.11be）の中核機能の 1 つで、2.4 GHz、5 GHz、6 GHz など複数の周波数帯を同時に利用することで、ネットワーク性能の向上、レイテンシーの大幅な低減、接続安定性の強化を実現します。

Wi-Fi 7 クライアントは MLO Wi-Fi へ接続することを推奨します。マルチバンド接続により、ネットワークスループットと信頼性が大きく向上します。

**Add** をクリックして MLO Wi-Fi ネットワークを設定し、**Apply** をクリックします。利用可能な Wi-Fi バンドはモデルによって異なります。

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band: 少なくとも 2 つの無線バンドを選択します。
- Wi-Fi Security: 6 GHz バンドを選択した場合、利用可能なオプションは WPA3-SAE のみで、ほとんどの MLO 対応デバイスで最適に動作するため推奨されます。
- Enable Randomized BSSID: 6 GHz バンドを選択した場合、MLO Wi-Fi の 6 GHz BSSID は Main Wi-Fi と同期されます。

有効化すると、ページは次のように表示されます。

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo3.png){class="glboxshadow"}

## Main Network

Main Network はメインの Wi-Fi ネットワークです。異なる無線バンドでの同時ブロードキャストに対応しており、すべてデフォルトで有効になっています。Wi-Fi SSID、セキュリティモード、パスワード、ランダム化 BSSID、TX power、帯域幅、チャンネルなど、バンドごとに個別設定が可能です。

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main.png){class="glboxshadow"}

右側の歯車アイコンをクリックすると、各バンドの Wi-Fi 設定を表示または変更できます。利用可能な Wi-Fi バンドはモデルによって異なります。

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_2.4g.png){class="glboxshadow"}

## Guest Network

Guest Network は来訪者向けの専用 Wi-Fi ネットワークで、すべてのバンドがデフォルトで無効になっています。各バンドごとに Wi-Fi SSID、セキュリティモード、パスワード、ランダム化 BSSID の有効化など、基本設定を行えます。

**Add** をクリックして Guest Wi-Fi ネットワークを設定し、**Apply** をクリックします。利用可能な Wi-Fi バンドはモデルによって異なります。

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest2.png){class="glboxshadow"}

有効化すると、ページは次のように表示されます。

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest3.png){class="glboxshadow"}

## IoT Network

IoT Network はスマートデバイス向けの専用 Wi-Fi ネットワークで、すべてのバンドがデフォルトで無効になっています。各バンドごとに Wi-Fi SSID、セキュリティモード、パスワード、ランダム化 BSSID の有効化など、基本設定を行えます。

**Add** をクリックして IoT Wi-Fi ネットワークを設定し、**Apply** をクリックします。このネットワークには 6 GHz バンドは含まれず、利用可能な Wi-Fi バンドはモデルによって異なります。

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot2.png){class="glboxshadow"}

有効化すると、ページは次のように表示されます。

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot3.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご利用ください。
