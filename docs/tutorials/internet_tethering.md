# usbテザリングでインターネットに接続する

USBケーブルを使って、スマートフォンからルーターまでネットワークを共有することをテザリングといいます。ホストレスモデムは、モデムの設定中もテザリングで動作します。

**注意：**携帯電話会社によっては、テザリングに制限や追加料金が発生する場合があります。ご利用の携帯電話会社にご確認いただくことをお勧めします。

=== "iPhone"

    1. iPhoneをルーターのUSBポートに接続します。このコンピュータを信頼するかどうかを尋ねるメッセージがポップアップ表示されます。信頼する "をクリックして続行します。iPhoneをルーターに接続しているので、ここでルーターを信頼することになります。

        ![trust this computer](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. iPhone -> 設定 -> パーソナルホットスポット -> 「他の人の参加を許可する」をオンにします。

        ![turn on allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow"}

    3. Go to web Admin Panel, on the left side bar, choose "INTERNET" and click "Connect" in the middle of the page.

        ![tethering connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_find_device.png){class="glboxshadow"}

    4. 接続に成功すると、携帯電話の画面上部とWebのAdmin Panelに接続情報が表示されます。

        ![tethering](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow"}

        テザリングに接続しました。

        ![tethering](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/tethering_connected.png){class="glboxshadow"}

    接続に失敗した場合は、**Allow Others to Join**をオフにして、何度かオンにしてみてください。

=== "Android"

    Android携帯のテザリングは、iPhoneと同様の手順で行います。ルーターのUSBポートに接続すると、**USBを使用する**というダイアログが表示されるので、**ファイル転送/Androidオーディオ**を選択し、設定→パーソナルホットスポット→USBネットワーク共有にチェックを入れてください。

    Androidの公式ドキュメントはこちらをご覧ください。 [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}