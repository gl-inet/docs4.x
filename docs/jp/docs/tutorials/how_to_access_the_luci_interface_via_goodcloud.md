# GoodCloud経由でLuCIインターフェースにアクセスする方法

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="\_blank"} は、地理的な制限を超えてルーターをリモート管理できる便利なサービスです。GoodCloud を使えば、ルーターの LuCI インターフェースにいつでもどこからでもアクセスし、各種設定を行ってネットワークを管理できます。

## 準備

- ハードウェア: インターネット接続の設定が完了し、正常に動作している GL.iNet ルーター
- ネットワーク環境: ルーターが接続されているネットワークが安定しており、正常にインターネットへアクセスできること
- デバイスのバインド: GL.iNet ルーターを GoodCloud アカウントへ[バインド](../interface_guide/cloud.md/#setup-your-goodcloud-account)しておく必要があります。GoodCloud アカウントを持っていない場合は、[登録](https://www.goodcloud.xyz/){target="\_blank"}してください。

## GoodCloud経由でLuCIインターフェースにアクセスする手順

### ファームウェアバージョン 4.7 以降

v4.7 以降では、ルーターの Web 管理パネルを経由せず、GoodCloud プラットフォームから直接 LuCI ページへアクセスできます。

1. [こちら](https://www.goodcloud.xyz/){target="\_blank"} から GoodCloud アカウントにログインします。

2. 左側メニューで **Devices** -> **Bound Devices** に進み、アクセスしたいデバイス名をクリックします。すると、Remote Web Access のアイコンが表示されます。

   ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

   ポップアップウィンドウにはポート `80` が表示されます。これを **8080** に変更し、**Apply** をクリックします。

   ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. LuCI のログインページへリダイレクトされます。管理者パスワードを入力してログインします。

   ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. これで LuCI へのログインは完了です。

   ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### ファームウェアバージョン 4.6 以前

1. [こちら](https://www.goodcloud.xyz/){target="\_blank"} から GoodCloud アカウントにログインします。

2. 左側メニューで **Devices** -> **Bound Devices** に進み、アクセスしたいデバイス名をクリックします。すると、Remote Web Access のアイコンが表示されます。

   ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

   ポップアップウィンドウにはポート `80` が表示されます。そのまま **Apply** をクリックします。

   ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. GL.iNet 管理パネルのログインページへリダイレクトされます。管理者パスワードを入力してログインします。

   ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. ログイン後、左側メニューで **SYSTEM** -> **Advanced Settings** に進み、LuCI インターフェースへ移動するリンクをクリックします。

   ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

   LuCI のログインページへリダイレクトされるので、同じ管理者パスワードを入力してログインします。

   ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. これで LuCI へのログインは完了です。

   ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
