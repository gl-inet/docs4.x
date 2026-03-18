# USBテザリングでインターネットに接続

USBケーブルを使ってスマートフォンからルーターへネットワークを共有することをテザリングと呼びます。ホストレスモデムは、モデムのセットアップ中もテザリングで動作します。

**注意:** 一部のモバイル通信事業者は、テザリングに制限を設けたり、追加料金を請求したりします。ご契約中の通信事業者にご確認ください。

## 設定

=== "iPhone"

    1. iPhoneをルーターのUSBポートにUSBケーブルで接続します。システムダイアログが表示され、デバイスを信頼するかどうか尋ねられます。**信頼**をタップして続行します。

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. iPhoneの**設定** -> **個人ホットスポット**に移動します。**彼のユーザーの参加を許可**を有効にします。

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. コンピュータまたは別のスマートフォンをルーターに接続し、ルーターのウェブ管理パネルにログインして、**インターネット** -> **テザリング**セクションに移動し、**接続**をクリックします。

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        TTL、HL、MTUなどの詳細設定が必要な場合は、**詳細設定**をクリックしてこれらの設定をカスタマイズし、**接続**をクリックします。

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        接続が始まります。

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. 接続に成功すると、スマートフォンの画面上部のステータスバーに個人ホットスポットのステータス（接続されているデバイスの数など）が表示されます。

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        ウェブ管理パネルにもテザリングの接続ステータスが表示されます。

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. AndroidスマートフォンをUSBケーブルでルーターのUSBポートに接続します。USB設定を求めるシステムダイアログが表示される場合があります。求められたら**USBテザリング**または**ファイル転送**を選択します。

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. スマートフォンの**設定** -> **ネットワークとインターネット** -> **個人ホットスポット**に移動します。**個人ホットスポット**または**USBテザリング**を有効にします。
    
        （USBテザリングを有効にする手順はブランドによって異なります。正確な場所についてはデバイスの設定を確認し、必要に応じてメーカーのサポートにお問い合わせください。）

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. コンピュータまたは別のスマートフォンをルーターに接続し、ルーターのウェブ管理パネルにログインして、**インターネット** -> **テザリング**セクションに移動し、**接続**をクリックします。

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        TTL、HL、MTUなどの詳細設定が必要な場合は、**詳細設定**をクリックしてこれらの設定をカスタマイズし、**接続**をクリックします。

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        接続が始まります。

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. 接続に成功すると、スマートフォンの画面上部のステータスバーに個人ホットスポットのステータス（接続されているデバイスの数など）が表示されます。
    
        ウェブ管理パネルにもテザリングの接続ステータスが表示されます。

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Androidの公式ドキュメントについては、[Androidでホットスポットまたはテザリングによるモバイル接続を共有する](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}をご覧ください。

## 警告

インターネットにアクセスできない場合、対応する警告が表示されます：

**「インターフェースは接続されていますが、インターネットにアクセスできません。」**

解決策：

1. スマートフォンにインターネットアクセスがあるか確認します。

2. [マルチWAN](multi-wan.md)ページでインターネットにアクセスできるかどうかを確認します。

## トラブルシューティング

接続に失敗した場合は、以下のトラブルシューティング手順を試してください：

- ルーターには元の電源を使用してください。
- USBケーブルの抜き差しをしてください。
- 別のUSBケーブルを使用してください。データ転送をサポートしているケーブルであることを確認してください（充電のみではない）。
- 「USBテザリング」を数回オフにしてオンにします（Androidスマートフォンの場合）。
- 「彼のユーザーの参加を許可」を数回オフにしてオンにします（iPhoneの場合）。
- スマートフォンを再起動して再試行してください。

---

関連記事

- [インターネットページ](internet.md)
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネットアクセス方式を同時に使用する場合のロードバランスを設定するには？](multi-wan.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
