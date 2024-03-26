# USBテザリングでインターネットに接続

USBケーブルを使ってスマートフォンからルーターへネットワークを共有することをテザリングと呼びます。ホストレスモデムは、モデムのセットアップ中もテザリングで動作します。

** 注意:** 一部のモバイル通信事業者は、テザリングに制限を設けたり、追加料金を請求したりします。ご契約中の通信事業者にご確認ください。

=== "iPhone"

    1. iPhoneをルーターのUSBポートに接続します。 このコンピュータを信頼するかどうかを尋ねるメッセージがポップアップ表示されます。 「信頼」をクリックして続行します。 iPhone をルーターに接続しているので、ここではルーターを信頼します。

        ![trust this computer](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. iPhone -> 設定 -> 個人ホットスポット -> 「他のユーザーの参加を許可」をオンにします。

        ![turn on allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow"}

    3. パソコンまたは別のスマートフォンを使ってルーターに接続し、ウェブ管理パネルの左サイドバーで「インターネット」を選択し、ページ中央の「接続」をクリックします。

        ![tethering connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_find_device.png){class="glboxshadow"}

    4. 接続に成功すると、スマートフォンの画面上部とウェブの管理パネルに接続情報が表示されます。

        ![tethering](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow"}

        ウェブ管理画面でテザリングに接続。

        ![tethering](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_connected.png){class="glboxshadow"}

    接続に失敗した場合は、**他のユーザーの参加を許可する**を数回オフにしてオンにしてください。

=== "Android"

    Android携帯のテザリングは、iPhoneと同じような手順です。ルーターのUSBポートに接続すると、**Use USB for**というダイアログが出るので、**File Transfer/Android Audio**を選択し、設定→個人用ホットスポット→Usbネットワーク共有にチェックをします。

    For the Android official documentation for refer [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}


## 警告

インターネットにアクセスできない場合は、対応する警告が表示されます。インターネットにアクセスできるかどうかは、 [マルチWAN](multi-wan.md)ページをご覧ください。

- 警告：*インターフェースは接続されていますが、IPv4プロトコルでインターネットにアクセスできません。

    解決方法 ：スマートフォンがインターネットに接続できるかどうかご確認ください。

## 問題解決

    * オリジナルの電源をご使用ください。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット・アクセス方式を同時に使用する場合のロードバランスの設定方法は？](multi-wan.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
