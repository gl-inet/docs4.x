# GoodCloud経由でLuCIインターフェースにアクセスする方法

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} は地理的な制限を超えて、ルーターを便利にリモート管理できるようにします。GoodCloud を使えば、ルーターの LuCI インターフェースにいつでもどこからでもアクセスでき、さまざまな設定を行ってネットワークを簡単に管理できます。

## 準備

- ハードウェア機器: インターネット設定が完了し、正常に動作している GL.iNet ルーター
- ネットワーク環境: ルーターが接続されているネットワークが安定しており、正常にインターネットへアクセスできること
- デバイスのバインド: [GL.iNet ルーターを GoodCloud アカウントにバインド](../interface_guide/cloud.md/#setup-your-goodcloud-account)しておく必要があります。GoodCloud アカウントをお持ちでない場合は、[登録](https://www.goodcloud.xyz/){target="_blank"}してください。

## GoodCloud経由でLuCIインターフェースにアクセスする手順

### ファームウェアバージョン 4.7 以降

v4.7 以降では、ルーターの Web 管理画面を経由せずに、GoodCloud プラットフォームから直接 LuCI ページへアクセスできます。

1. [こちら](https://www.goodcloud.xyz/){target="_blank"} から GoodCloud アカウントにログインします。

2. 左側で **Devices** -> **Bound Devices** に移動し、アクセスしたいデバイス名をクリックします。すると、Remote Web Access のアイコンが表示されます。

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    ポップアップウィンドウにはポート 80 が表示されます。これを **8080** に変更し、**Apply** をクリックします。

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. LuCI のログインページへリダイレクトされます。管理者パスワードを入力してログインします。

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. LuCI へのログインが完了しました。

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### ファームウェアバージョン 4.6 以前

1. [こちら](https://www.goodcloud.xyz/){target="_blank"} から GoodCloud アカウントにログインします。

2. 左側で **Devices** -> **Bound Devices** に移動し、アクセスしたいデバイス名をクリックします。すると、Remote Web Access のアイコンが表示されます。

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    ポップアップウィンドウにはポート 80 が表示されます。そのまま **Apply** をクリックします。

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. GL.iNet Admin Panel のログインページへリダイレクトされます。管理者パスワードを入力してログインします。

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. ログイン後、左側で SYSTEM -> Advanced Settings に移動し、ハイパーリンクをクリックして LuCI インターフェースへ移動します。

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    LuCI のログインページへリダイレクトされます。同じ管理者パスワードを入力してログインします。

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. LuCI へのログインが完了しました。

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
