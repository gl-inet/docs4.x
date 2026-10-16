# ワイヤレス（ファームウェア v4.8 以前）

このページの内容は、ファームウェア v4.8.x 以前に基づいています。デバイスで別のファームウェアバージョンを使用している場合は、以下のセレクターで該当するガイドに切り替えてください。

<div class="gl-link-select" data-label="ファームウェアバージョン" data-placeholder="ファームウェア v4.8 以前" markdown="1">

- [ファームウェア v4.9 以降](wireless.md)

</div>

---


Web 管理パネルの左側で、**WIRELESS** に移動します。

Wireless ページでは、2.4 GHz、5 GHz、6 GHz、MLO Wi-Fi など、個別の Wi-Fi ネットワークを設定できます（利用可否はモデルによって異なります）。各バンドは、メイン Wi‑Fi またはゲスト Wi‑Fi として設定でき、柔軟にワイヤレス管理を行えます。

**注意**: 5 GHz Wi-Fi に対応していないモデル（GL-MT300N-V2 (Mango)、GL-X300B (Collie) など）や、Wi‑Fi 機能自体を搭載していないモデル（GL-MT5000 (Brume 3)、GL-MT2500/GL-MT2500A (Brume 2) など）があります。

## MLO Wi-Fi

| 対応モデル               |           |
| :----------------------- | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000) | √         |
| Beryl 7 (GL-MT3600BE)    | √         |
| Flint 3e (GL-BE6500)     | √         |
| Flint 3 (GL-BE9300)      | √         |
| Slate 7 (GL-BE3600)      | √         |

MLO（Multi-Link Operation）は Wi-Fi 7（802.11be）の中核機能の1つで、2.4 GHz、5 GHz、6 GHz など複数の周波数帯を同時に利用することで、ネットワーク性能の向上、遅延の大幅な低減、接続の安定性向上を実現します。

以下のタブをクリックすると、MLO メイン Wi-Fi と MLO ゲスト Wi-Fi の設定を確認できます。

=== "MLO Wi-Fi"

    MLO メイン Wi-Fi では、Wi-Fi の有効/無効、無線バンドの選択（2つ以上）、ランダム BSSID の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、Wi-Fi パスワード、SSID 表示などを設定できます。

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - MLO Wi-Fi の無線バンドに 6 GHz が含まれている場合、6 GHz Wi-Fi の BSSID が変わると MLO Wi-Fi の BSSID も同期して変更されます。

    - MLO Wi-Fi のデフォルトの Wi-Fi セキュリティは WPA3-SAE で、MLO に対応したほとんどのデバイスに適しています。

=== "MLO Guest Wi-Fi"

    MLO ゲスト Wi-Fi では、Wi-Fi の有効/無効、無線バンドの選択（2つ以上）、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、パスワード、SSID 表示など、簡易的な設定を行えます。

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## 6 GHz Wi-Fi

| 対応モデル               |           |
| :----------------------- | :-------: |
| Slate 7 Pro (GL-BE10000) | √         |
| Mudi 7 (GL-E5800)        | √         |
| Flint 3 (GL-BE9300)      | √         |

6 GHz Wi-Fi は、2.4 GHz および 5 GHz 帯と比べて混雑が少なく、より高速で安定したワイヤレス接続を提供します。

以下のタブをクリックすると、6 GHz メイン Wi-Fi と 6 GHz ゲスト Wi-Fi の設定を確認できます。

=== "6 GHz Wi-Fi"

    6 GHz メイン Wi-Fi では、Wi-Fi の有効/無効、TX power、ランダム BSSID の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、Wi-Fi パスワード、SSID 表示、Wi-Fi モード、帯域幅、チャネルなどを設定できます。

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - Enable PSC: PSC（Preferred Scanning Channel）を有効にすると、接続性の高いチャネルのみが予約され、6 GHz デバイスの接続を確保できます。

=== "6 GHz Guest Wi-Fi"

    6 GHz ゲスト Wi-Fi では、Wi-Fi の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、パスワード、SSID 表示など、簡易的な設定を行えます。

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## 5 GHz Wi-Fi

以下のタブをクリックすると、5 GHz メイン Wi-Fi と 5 GHz ゲスト Wi-Fi の設定を確認できます。

=== "5 GHz Wi-Fi"

    5 GHz メイン Wi-Fi では、Wi-Fi の有効/無効、TX power、ランダム BSSID の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、Wi-Fi パスワード、SSID 表示、Wi-Fi モード、帯域幅、チャネルなどを設定できます。

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "5 GHz Guest Wi-Fi"

    5 GHz ゲスト Wi-Fi では、Wi-Fi の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、パスワード、SSID 表示など、簡易的な設定を行えます。

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## 2.4 GHz Wi-Fi

以下のタブをクリックすると、2.4 GHz メイン Wi-Fi と 2.4 GHz ゲスト Wi-Fi の設定を確認できます。

=== "2.4 GHz Wi-Fi"

    2.4 GHz メイン Wi-Fi では、Wi-Fi の有効/無効、TX power、ランダム BSSID の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、Wi-Fi パスワード、SSID 表示、Wi-Fi モード、帯域幅、チャネルなどを設定できます。

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "2.4 GHz Guest Wi-Fi"

    2.4 GHz ゲスト Wi-Fi では、Wi-Fi の有効/無効、Wi-Fi 名（SSID）、Wi-Fi セキュリティ、パスワード、SSID 表示など、簡易的な設定を行えます。

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## 一般的な Wi-Fi 設定

* Wi-Fi SSID の横にある QR コードアイコンにカーソルを合わせると、Wi‑Fi の QR コードが表示されます。スマートフォンやタブレットで読み取ることで、対応する Wi‑Fi ネットワークにすばやく接続できます。

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: デフォルトで有効になっており、固定BSSIDによるルーターの追跡を防ぎます。詳細は[Randomized BSSID](#randomized-bssid)を参照してください。

* ルーターが[リピーター](internet_repeater.md)として動作している間は、**Bandwidth** と **Channel** は変更できません。中継先ネットワークの設定に従います。

* **Channel** を **Auto** に設定している場合、ルーターの Wi-Fi は自動的に DFS チャネルへ切り替わりません。

* 非 DFS チャネルから DFS チャネルへ切り替えると、次のような警告が表示されます。

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* **Bandwidth** を **160 MHz** に設定している場合（一部モデルのみ対応）、Channel 設定で非 DFS チャネルまたは Auto を選択していても、Wi-Fi は常に DFS チャネルを使用します。

## Randomized BSSID {#randomized-bssid}

Randomized BSSIDは、ファームウェアv4.6以降で利用でき、デフォルトで有効になっているプライバシー保護機能です。固定のWi-Fi BSSID（ルーターの無線インターフェースのMACアドレス）によるルーターの位置特定や追跡を防ぎます。

**固定BSSIDがプライバシー上のリスクとなる理由**

AndroidやiOSなどのモバイルOSは、利用者のデバイスから収集したデータに基づくWi-Fi測位を位置情報サービスに使用しています。

1. スマートフォンやノートPCなどのクライアントデバイスが、検出したBSSIDと自身のGPS位置情報を、OSやデバイスの提供元のサーバーへ定期的にアップロードします。

2. 提供元が、このデータをBSSIDと位置情報を対応付ける世界規模のデータベースに集約します。

3. Wi-Fiが有効なデバイスは、GPSがなくても、このデータベースに問い合わせて周辺のBSSIDから自身の位置を推定できます。

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

その結果、固定BSSIDを持つルーターは一定の位置を示すビーコンのように機能します。リモートから位置を特定でき、旅行中などの移動も継続的に追跡される可能性があります。攻撃者がこうしたデータベースを照会し、ルーターを探したり、BSSIDのベンダー情報（OUI）から機器の特徴を識別したりすることもあります。

**Randomized BSSIDによる保護の仕組み**

この機能を有効にすると、ルーターはランダムなBSSIDを生成し、起動のたびに更新します。BSSIDが変わり続けるため、提供元のデータベースで固定の位置に結び付けられなくなり、追跡に使われるBSSIDと位置の対応関係を断ち切ります。

| 状態 | 動作 |
| ----------------- | ---------------------- |
| 有効（デフォルト） | 起動のたびに新しいランダムBSSIDを生成して更新します |
| 無効 | ルーターの実際の工場出荷時MACアドレスをBSSIDとして使用します |

**注意**:

1. BSSIDはルーターの再起動時にのみ変化し、動作中は変わりません。
2. ゲストWi-FiのBSSIDは、同じ周波数帯のメインWi-FiのBSSIDと一致します。
3. MLO Wi-Fiの無線帯域に6 GHzが含まれる場合、MLO Wi-FiのBSSIDは6 GHz Wi-FiのBSSIDと同期します。
4. Randomized BSSIDはルーターのBSSIDを使った追跡を防ぎますが、クライアントデバイス自身による位置情報の報告は防げません。また、プライバシーを完全に保護する機能ではなく、SSID、チャンネル、信号の特徴は引き続き観測できます。

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご利用ください。
