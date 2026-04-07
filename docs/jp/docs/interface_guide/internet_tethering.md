# USBテザリングでインターネットに接続する

USB ケーブルを使ってスマートフォンのネットワークをルーターと共有する方法をテザリングと呼びます。Host-less モデムも、セットアップ時にはテザリングとして動作します。

**注意:** 一部の通信事業者では、テザリングに制限を設けたり追加料金を請求したりする場合があります。事前に通信事業者へご確認ください。

## セットアップ

=== "iPhone"

    1. iPhone を USB ケーブルでルーターの USB ポートに接続します。デバイスを信頼するかどうかを尋ねるシステムダイアログが表示されたら、**Trust** をタップします。

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. iPhone の **Settings** -> **Personal Hotspot** に移動し、**Allow Others to Join** を有効にします。

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. パソコンまたは別のスマートフォンをルーターに接続し、ルーターの Web 管理パネルにログインして **INTERNET** -> **Tethering** に移動し、**Connect** をクリックします。

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        TTL、HL、MTU などの詳細設定が必要な場合は、**Advanced** をクリックして設定してから **Connect** をクリックします。

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        接続が開始されます。

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. 接続に成功すると、スマートフォン画面上部のステータスバーに、接続デバイス数などの Personal Hotspot の状態が表示されます。

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        Web 管理パネルにも Tethering の接続状態が表示されます。

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Android スマートフォンを USB ケーブルでルーターの USB ポートに接続します。USB の用途を選ぶシステムダイアログが表示された場合は、**USB Tethering** または **File Transfer** を選択します。

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. スマートフォンの **Settings** -> **Network & Internet** -> **Personal Hotspot** に移動し、**Personal Hotspot** または **USB Tethering** を有効にします。

        （USB テザリングを有効にする手順はメーカーによって異なります。正確な場所は端末の設定をご確認ください。必要に応じてメーカーのサポートへお問い合わせください。）

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. パソコンまたは別のスマートフォンをルーターに接続し、ルーターの Web 管理パネルにログインして **INTERNET** -> **Tethering** に移動し、**Connect** をクリックします。

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        TTL、HL、MTU などの詳細設定が必要な場合は、**Advanced** をクリックして設定してから **Connect** をクリックします。

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        接続が開始されます。

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. 接続に成功すると、スマートフォン画面上部のステータスバーに、接続デバイス数などの Personal Hotspot の状態が表示されます。

        Web 管理パネルにも Tethering の接続状態が表示されます。

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Android の公式ドキュメントについては、[Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"} を参照してください。

## 警告

インターネットに接続できない場合は、次の警告が表示されます。

**"The interface is connected, but the Internet can't be accessed."**

対処方法:

1. スマートフォンがインターネットに接続できているか確認します。

2. [Multi-WAN](multi-wan.md) ページで、インターネットへアクセスできるかどうかを確認します。

## トラブルシューティング

接続に失敗する場合は、次をお試しください。

- ルーターには純正の電源アダプターを使用する。
- USB ケーブルを抜き差しする。
- 別の USB ケーブルを使用する。充電専用ではなく、データ転送に対応している必要があります。
- （Android の場合）"USB Tethering" を数回オフ/オンする。
- （iPhone の場合）"Allow Others to Join" を数回オフ/オンする。
- スマートフォンを再起動してから再度試す。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネット接続方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット接続方法を同時に使用する場合、ロードバランスをどのように設定しますか？](multi-wan.md)

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
