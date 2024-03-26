# リピータで既存のWi-Fiを経由してインターネットに接続する

リピーターの使用とは、ホテルやカフェで無料Wi-Fiを使用する場合など、既存の他のワイヤレスネットワークにルーターを接続することです。

デフォルトではWISP（ワイヤレス・インターネット・サービス・プロバイダー）モードで動作し、ルーターは独自のサブネットを作成し、パブリックネットワークから保護するファイアウォールとして機能します。

Web 管理パネルの左側 -> インターネット-> リピーター セクター

## 基本的な手順

![repeater](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

上の画像の**接続**をクリックします。

![repeater join wlan](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_join_wlan.png){class="glboxshadow"}

ドロップダウンリストからSSIDを選択し、パスワードを入力します。接続したいSSIDがリストにない場合は、上図の [他のネットワークに参加する](#join-other-network) をクリックしてください。

![repeater join network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_join_network.png){class="glboxshadow"}

[詳細設定](#join-network-advanced-setting)の場合

パスワードが正しければ、接続は成功します。

![repeater connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

## ネットワークの詳細設定に参加

ネットワークに参加する場合、2 つの追加オプションがあります。

![repeater join network advanced setting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_join_network_advanced_setting.png){class="glboxshadow"}

* **Lock BSSID**：このオ プ シ ョ ン を 有効 に す る と 、このSSID を使用す るネ ッ トワ ー クに切 り替えたときに、ルータは選択した BSSID に対応する AP にのみ接続します。

* **静的IPを手動で設定する**.

## リピーター・オプション

リピーターオプションの歯車アイコンをクリックします。

![repeater connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

![repeater options](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_options.png){class="glboxshadow"}

* **他の保存されたネットワークへの切り替えを許可する**. このオプションを有効にすると、現在のWi-Fiネットワークに接続できない場合、ルーターは自動的に他の保存されたネットワークに接続します。

* **バンド・セレクション**. 手動でバンドを選択した場合、ルーターは他のバンドのWi-Fiをスキャンしたり接続したりしません。

* **リピート DFS チャネルを許可する**. このオプションが有効になっている場合、ルーターが現在使用しているチャネルをレーダーが使用している場合、5GHz Wi-Fi は一時的に利用できなくなります。 そうしないと、ルーターは DFS チャネルを使用して Wi-Fi に接続できません。

* **2.4G用20MHz帯域幅の強制設定**. このオプションが有効な場合、デバイスは接続速度を低下させる代わりに、接続の安定性を要求します。 2.4G Wi-Fiを繰り返す場合のみ機能します。

## 既知のネットワークを管理する

既知のネットワークを削除するには、**ネットワーク切り替え**をクリックします。

![repeater connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

または**接続**をクリックしてください。

![repeater](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

**既知のネットワーク**セクターで、既知のネットワークを削除するにはゴミ箱アイコンをクリックし、ネットワークを設定するには歯車アイコンをクリックします。

![repeater known network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_known_networks.png){class="glboxshadow"}

## 他のネットワークに参加する

SSIDが利用可能なネットワークリストにない場合、またはSSIDが非表示になっている場合は、**他のネットワークに参加**をクリックします。

![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/join_other_network.png){class="glboxshadow gl-90-desktop"}

![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_join_other_network.png){class="glboxshadow"}

SSIDを入力し、**セキュリティー**は以下の3つのオプションがあります。

* なし、パスワードは必要ありません。
* WPA/WPA2/WPA3
* WPA/WPA2/WPA3 Enterpriseでは、EAP（Extensible Authentication Protocol）のため、認証にユーザー名とパスワードが必要です。

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/join_other_network_eap.png){class="glboxshadow gl-90-desktop"}

## リコネクション

以下の場合、ルーターのリピーターが時々WiFiに接続しようとします。手動でリコネクションをオフにすることができます。また、ssid/パスワードエラーの場合は、既知のネットワークから削除してください。

1. 最初の接続に失敗した後、リピーターのプロセス中に間違ったSSID/パスワードを入力した。

2. アップストリーム側のルーターのWiFiに接続した後、ルーターはアップストリーム側のルーターの電波圏外に移動する。

3. アップストリーム側のルーターのWiFiに接続した後、アップストリーム側のルーターがSSID/パスワードを変更した、または接続を制限した。

これは3つのフェーズに分けることができます、待機フェーズ、スキャンフェーズ、接続フェーズ。

**注意 **：スキャンフェーズと接続フェーズでいくつかの問題があります。

1. 待機フェーズでは何も問題ありません。

2. スキャンのフェーズで、スキャンされた帯域でデータパケットが損失する可能性があり、新しいデバイスの接続に問題が発生する可能性があります。GL-AXT1800、GL-AX1800の場合、ゲストWi-Fiは一時的にオフになります。

3. 接続フェーズでは、対応するバンドのMain Wi-Fiが数秒間切断されることがあります。 

## 警告

インターネットにアクセスできない場合は、対応する警告が表示されます。インターネットにアクセスできるかどうかは、 [マルチWAN](multi-wan.md) ページをご覧ください。

- 警告: *インターフェイスは接続されていますが、IPv4 プロトコルではインターネットにアクセスできません。*

    ![repeater wrning](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_repeater/repeater_warning.png){class="glboxshadow gl-90-desktop"}

    解決方法： リピータのアップストリームデバイスがインターネットにアクセスできるか確認してください。

## DFS

アップストリームの5G WiFiにリピータを接続する場合、ルータのWiFiはアップストリームのWiFiにDFSチャネルを使用するかどうかをフェローします。

* アップストリームWiFiがDFSチャネルを使用し、スキャン可能であれば、ルーターの5G WiFiは同じチャネルを使用します。

* ルーターの5G WiFiは、アップストリームWiFiがスキャン可能でない場合、または接続に失敗した場合、非DFSチャネルに切り替わります。

### 対応モデル

| ルーターモデル                  | サポート   |
| :----------------------------- | :-------: |
| GL-X3000 (Spitz AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-AXT1800 (Slate AX)          | √         |
| GL-A1300 (Slate Plus)          | -         |
| GL-MT2500/GL-MT2500A (Brume 2) | -         |
| GL-SFT1200 (Opal)              | -         |
| GL-S1300 (Convexa-S)           | -         |
| GL-MT1300 (Beryl)              | -         |
| GL-AX1800 (Flint)              | -         |
| GL-MT6000 (Flint 2)            | √         |
| GL-AR750S (Slate)              | -         |
| GL-AR750 (Creta)               | -         |
| GL-AR300M Series（Shadow）     | -         |
| GL-MT300N-V2（Mango）          | -         |
| GL-XE300 (Puli)                | -         |
| GL-XE3000 (Puli AX)            | √         |
| GL-X750 (Spitz)                | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-AP1300 (Cirrus)             | -         |
| GL-X300B (Collie)              | -         |
| GL-MV1000/GL-MV1000W (Brume)   | -         |

---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット・アクセス方式を同時に使用する場合のロードバランスの設定方法は？](multi-wan.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
