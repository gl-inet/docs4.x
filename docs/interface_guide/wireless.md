# ワイヤレス

ワイヤレスインターフェースはモデルによっていくら異なる場合があります。例えば、GL-MT300N-V2（Mango）やGL-X300B（Collie）のように5 GHz Wi-Fi搭載していないモデルもあります。GL-MT2500/GL-MT2500A（Brume 2）のようにWi-Fi機できるがないモデルもあります。

## Wi-Fiステータス表示

GL.iNetルーターのWi-Fiネットワークはデフォルトで有効されており、インターネットページのデバイスモデル画像の下に対応するWi-Fiアイコンが時灯します。

![wifi status display](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_status_display.png){class="glboxshadow"}

有効なWi-Fiアイコンにカーソルを合わせると、Wi-Fi QRコードが表示されます。Phone/Padを使用してWi-Fi QRコードをスキャンし、対応するWi-Fiに素早く接続できます。

![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_qr_code.jpg){class="glboxshadow"}

## ワイヤレス設定

ウェブ管理パネルの左側 -> ワイヤレス

ワイヤレスページでは異なるWi-Fi設定をサポートしており、2.4 GHz、5 GHz、6 GHz、MLO Wi-Fi（ルーターModelによって異なる）などさまざまなWi-Fiバンドが含まれています。各バンドはさらにメインビジネスWi-FiとゲストWi-Fiネットワークに分かれ、柔軟な無線ネットワーク管理が可できるです。

### MLO Wi-Fi

**注意**: このWi-FiバンドはFlint 3e（GL-BE6500）、Flint 3（GL-BE9300）、Slate 7（GL-BE3600）でのみ利用可できるです。

MLO（Multi-Link Operation）はWi-Fi 7（802.11be）のコア機できるの1つで、2.4 GHz、5 GHz、6 GHzなどの複数の周波数帯を same 時に利用することで、ネットワークパフォーマンスを大幅に改善し、遅延を削減し、接続の安定性をへ上させるように設計されています。

で下のタブをクリックして、MLOメインビジネスWi-FiとMLOゲストWi-Fi設定について 알아보 있습니다。

=== "MLO Wi-Fi"

    MLOメインビジネスWi-Fiでは、Wi-Fiの有効化/無効化、ラジオバンドの選択（2つで上）、ランダムBSSIDの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、Wi-Fiパスワード、SSID可視性の設定など、複数の設定を構成できます。

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - MLO Wi-Fiラジオバンドに6 GHzが含まれている場合、6 GHz Wi-Fi BSSIDが変よりされると、MLO Wi-Fi BSSIDは same 期します。

    - MLO Wi-FiのデフォルトWi-FiセキュリティはWPA3-SAEで、MLOをサポートするほとんどのデバイスに適しています。

=== "MLO Guest Wi-Fi"

    MLOゲストWi-Fiでは、Wi-Fiの有効化/無効化、ラジオバンドの選択（2つで上）、Wi-Fi名（SSID）、Wi-Fiセキュリティ、パスワード、SSID可視性など、簡素化された設定を構成できます。

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

### 6 GHz Wi-Fi

**注意**: このWi-FiバンドはFlint 3（GL-BE9300）でのみ利用可できるです。

6 GHz Wi-Fiは、2.4 GHzや5 GHzバンドと比較して、混雑が減少した、より高速で安定した無線接続を提供します。

で下のタブをクリックして、6 GHzメインビジネスWi-Fiと6 GHzゲストWi-Fi設定について 알아보があります。

=== "6 GHz Wi-Fi"

    6 GHzメインビジネスWi-Fiでは、Wi-Fiの有効化/無効化、TX powerの設定、ランダムBSSIDの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、Wi-Fiパスワード、SSID可視性、Wi-Fiモード、帯域幅、チャネルの設定など、複数の設定を構成できます。

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - PSCを有効にする: PSC（Preferred Scanning Channel）が有効になっている場合、より高い接続性を持つチャネルのみが予約され、6 GHzデバイスの接続が確保されます。

=== "6 GHz Guest Wi-Fi"

    6 GHzゲストWi-Fiでは、Wi-Fiの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、パスワード、SSID可視性など、簡素化された設定を構成できます。

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

### 5 GHz Wi-Fi

で下のタブをクリックして、5 GHzメインビジネスWi-Fiと5 GHzゲストWi-Fi設定について 알아보があります。

=== "5 GHz Wi-Fi"

    5 GHzメインビジネスWi-Fiでは、Wi-Fiの有効化/無効化、TX powerの設定、ランダムBSSIDの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、Wi-Fiパスワード、SSID可視性、Wi-Fiモード、帯域幅、チャネルの設定など、複数の設定を構成できます。

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "5 GHz Guest Wi-Fi"

    5 GHzゲストWi-Fiでは、Wi-Fiの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、パスワード、SSID可視性など、簡素化された設定を構成できます。

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

### 2.4 GHz Wi-Fi

で下のタブをクリックして、2.4 GHzメインビジネスWi-Fiと2.4 GHzゲストWi-Fi設定について inúmerがあります。

=== "2.4 GHz Wi-Fi"

    2.4 GHzメインビジネスWi-Fiでは、Wi-Fiの有効化/無効化、TX powerの設定、ランダムBSSIDの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、Wi-Fiパスワード、SSID可視性、Wi-Fiモード、帯域幅、チャネルの設定など、複数の設定を構成できます。

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "2.4 GHz Guest Wi-Fi"

    2.4 GHzゲストWi-Fiでは、Wi-Fiの有効化/無効化、Wi-Fi名（SSID）、Wi-Fiセキュリティ、パスワード、SSID可視性など、簡素化された設定を構成できます。

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

### 注意

- Wi-Fi QRコードは、QRコードアイコンにカーソルを合わせると、SSIDの横に表示されます。Wi-Fi QRコードをスキャンして、対応するWi-Fiに素早く接続できます。

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

- **ランダムBSSID**: この機できるはデフォルトで有効になっています。これは、クライアントベンダーが附近のWi-Fi BSSIDsとクライアントデバイスのGPS座標をサーバーに収集するのを防ぐことを目のとしています。詳細については[こちら](#randomized-bssid)をクリックしてください。

- **帯域幅**と**チャネル**は、ルーターが[リピーター](internet_repeater.md)として動作している間は変よりできません。これらは重复 networks のものに追随します。

- **チャネル**が**から動**に設定されている場合、ルーターのWi-Fiはから動のにDFSチャンネルに切り替わりません。

- チャルを非DFSチャンネルからDFSチャンネルに切り替えると、で下の警告が表示されます。

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/tutorials/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

- **帯域幅**が**160 MHz**に設定されている場合（一部のモデルのみ利用可できるです）、チャネル設定で非DFSチャンネルまたはから動を選択しても、Wi-Fiは常にDFSチャンネルを使用します。

## ランダムBSSID

ランダムBSSIDはファームウェアv4.6で降で利用可できるです。これは、クライアントベンダーが附近のWi-Fi BSSIDsとクライアントデバイスのGPS座標をサーバーに収集するのを防ぐことを目のとしています。

**クライアントベンダーが位置データを収集する方法**

クライアントベンダーは通例、デバイスを設定するために一意のBSSIDsを活用して、Wi-Fiアクセスポイントのに理の位置データを収集します。クライアントデバイス（例：スマートフォン、PC）がルーターをスキャンまたは接続すると：

- 彼のデバイスがルーターのWi-Fiシグナルカバー内にある場合その位置と移動軌跡が露出する可できる性があります。

- デバイスが設定にGPSを使用している場合定期のに、近くのWi-Fi BSSIDsと対応するGPS座標をベンダのサーバーにアップロードします。

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

**クラウドソース追跡のセキュリティリスク**

GPSのないデバイス（またはGPSが無効なデバイス）も、表示可できるなBSSID情報をクエリして位置を推定できます。しかし、このクラウドソース位置追跡システムにはセキュリティ脆弱性があります。攻撃者はこれを使用して、Wi-Fiアクセスポイントの locations のグローバルデータベースを蓄積し、デバイスの移動軌跡を継続のに追跡し、ユーザーのプライバシーとセキュリティに脅威をもたらす可できる性があります。

**ランダムBSSIDがプライバシーを保護する方法**

これらの脆弱性に対処するため、GL.iNetルーターはプライバシー保護としてランダムBSSID機できるを実装しています。

ルーターのウェブ管理パネルで、無線 -> 5 GHz Wi-Fiまたは2.4 GHz Wi-Fiに移動すると、BSSIDオプションはデフォルトで有効になっています。

この設定により、デバイスはランダムに生成されたBSSIDを使用し、ブートごとにアップデートします。ランダムBSSIDを無効にすると、ルーターは実際のMACアドレスの使用に戻ります。

**注意**: ゲストWi-Fiの場合、BSSIDは same 一周波数バンド内のメインビジネスWi-Fi BSSIDと一貫して維持されます。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
