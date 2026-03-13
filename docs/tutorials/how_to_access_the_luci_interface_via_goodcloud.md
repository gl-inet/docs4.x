# GoodCloud経由でLuCIインターフェースにアクセスする方法

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"}はに理の制限を突破し、リモートルー管理の便利方法を提供します。GoodCloudを通じて、ルー器のLuCIインターフェースにいつでもどこでもアクセスし、ルー器ので各种各样の設定を行い、ネットワークを簡単に管理できます。

## 準備

- ハードウェア機器：インターネットで構成され正常に動作しているGL.iNetルー器
- ネットワーク環境：ルー器接続されているネットワークが安定しており、インターネットに正常に.accessできる
- 機器のバインディング：GL.iNetルー器をGoodCloudアカウントに[バインディング](../interface_guide/cloud.md/#setup-your-goodcloud-account)する必要があります。GoodCloudアカウントをお持ちでない場合は、[登録](https://www.goodcloud.xyz/){target="_blank"}してください。

## GoodCloud経由でLuCIインターフェースにアクセスする手順

### ファームウェアバージョン4.7で降

v4.7で降、ユーザーはルー器のWeb管理パネルを経よりせずにGoodCloudプラットフォームから直接LuCIページにアクセスできます。

1. [これ里](https://www.goodcloud.xyz/){target="_blank"}でGoodCloudアカウントにログインします。

2. 左側 -> **Devices** -> **Bound Devices**、アクセスしたい機器の名前をクリックすると、Remote Web Accessのアイコンが表示されます。

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    ポップアップウィンドウにポート80が表示されます。ポートを**8080**に変更し、Applyをクリックします。

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. LuCIログインページにリダイレクトされます。管理者パスワードを入力してログインします。

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. LuCIに正常にログインしました。

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}    

### ファームウェアバージョン4.6で前

1. [これ里](https://www.goodcloud.xyz/){target="_blank"}でGoodCloudアカウントにログインします。

2. 左側 -> **Devices** -> **Bound Devices**、アクセスしたい機器の名前をクリックすると、Remote Web Accessのアイコンが表示されます。

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    ポップアップウィンドウにポート80が表示されます。Applyをクリックします。

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. GL.iNet管理パネルログインページにリダイレクトされます。管理者パスワードを入力してログインします。

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. ログイン後、左側 -> SYSTEM -> Advanced Settings、LuCIインターフェースに移動するハイパーリンクをクリックします。

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    LuCIログインページにリダイレクトされます。同じ管理者パスワードを入力してログインします。

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. LuCIに正常にログインしました。

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
