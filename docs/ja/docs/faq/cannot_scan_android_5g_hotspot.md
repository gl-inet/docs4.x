# Android 5Gホットスポットをスキャンできない

GL.iNetルーターをAndroidスマホの5Gホットスポットにリピーターとして接続することは、インターネットにアクセスする一般的な方法の1つです。

ただし、Androidスマホの5Gホットスポットをスキャンできない場合、Wi-Fiチャンネルが原因である可能性があります。

一部の Android スマートフォンでは、5G ホットスポットがデフォルトで米国のチャンネルに設定されています。GL.iNet ルーターを米国以外で購入した場合、この問題が発生する可能性があります。

以下の手順で、LuCI インターフェースから GL.iNet ルーターの Wi-Fi 国コードを変更できます。

1. GL.iNetルーターにログインし、**SYSTEM** -> **Advanced Settings** -> **Go to LuCI** に移動します。同じ管理者パスワードで LuCI にログインします。

2. Wi-Fi 設定を編集します。

    **Network** -> **Wireless** に移動し、5G Wi-Fi を見つけて右側の **Edit** をクリックします。

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. 国コードとして US を選択します。

    Wireless ページで、**Device Configuration** の **Advanced Settings** タブを開き、5GHz Wi-Fi の国コードとして US (United States) を選択します。

    ![5gus](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. **Save & Apply** をクリックしてからログアウトします。

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    その後、Androidスマホの5Gホットスポットを再度スキャンしてみてください。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}を訪問してください。
