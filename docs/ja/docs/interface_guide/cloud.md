# GL.iNet GoodCloud

## はじめに

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、接続されたデバイスのリモート展開と管理を簡素化するように設計されたプラットフォームです。 GL.iNet ルーターにリモートでアクセスして管理する簡単な方法を提供します。ネットワーク デバイスをクラウド上で集中管理することにより、ユーザーはネットワーク構成の展開やソフトウェア アップグレードの実行などのバッチ管理タスクを効率的に実行できます。また、ルーターの Web 管理パネルにリモートでアクセスしたり、SSH 経由でルーターの端末に接続したりすることもでき、地域を超えたエンドツーエンドのネットワーク デバイス管理を実現します。

GoodCloud を使用すると、次のことが可能になります。

1. ルーターのリアルタイムステータスを確認する
    - オンライン/オフライン状態を監視する
    - リアルタイムの RAM 使用量と負荷平均を表示
    - オンラインとオフラインのステータス変化に関する電子メール アラートを受信する

2. ルーターをリモートでセットアップする
    - ルーター設定を構成する （SSIDやパスワードなど）
    - リモート SSH アクセス
    - WebUIへのリモートアクセス
    - ルーターへのアクセスを他のユーザーと共有する

3. 接続されているクライアントをリモートで監視する
    - ネットワークに接続されているデバイスを表示する
    - リアルタイムのトラフィックを監視し、クライアントをブロックする
    - 新しい接続に関する電子メールアラートを受信し、イベントをブロックします

4. バッチ操作を実行する
    - バッチ再起動
    - ファームウェアの一括アップグレード

5. サイト間の接続を確立する
    - バーチャル オフィス: オフィス ネットワークを他のブランチ オフィスに拡張します。
    - 出張: オフィス システムにリモート アクセス （OA、CRM、MySQLなど）
    - スマートホーム: ホームデバイスにリモートアクセス （IPカメラ、NASなど）

複数のデバイスを管理し、一括操作、マルチアカウント管理、カスタマイズされたソリューションなどの高度な機能を利用する必要がある場合は、付加価値プランを選択してください。詳細については、[here](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} をクリックしてください。お気軽に [support@gl-inet.com](mailto:support@gl-inet.com) までお問い合わせください。

## デバイスをクラウドにバインドする

デバイスのファームウェア バージョンに基づいて、デバイス バインド手順に対応するセクションを選択します。

### ファームウェア v4.10 以降の場合

1. GoodCloudを有効にします。

    ルーターの Web 管理パネルにログインし、**CLOUD SERVICE** -> **GoodCloud** に移動して、**Get Started** をクリックします。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    **GL.iNet Account** ページが表示されます。 「**Bind GL.iNet Account via URL**」をクリックします。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    ポップアップ ウィンドウで、「**Continue**」をクリックします。バインディングを完了するには、GoodCloud Web サイトにリダイレクトされます。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. ログインしてデバイスをバインドします。

    GL.iNet アカウントにログインします。アカウントをお持ちでない場合は、アカウントを作成してログインしてください。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    ログイン後、アカウントとデバイス ID、モデル、MAC アドレスなどのデバイス情報を確認します。デバイス名をカスタマイズし、**Bind** をクリックすると、ルーターがアカウントにバインドされます。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    確認メールが届かない場合は、スパム フォルダーを確認するか、数分待ってからもう一度お試しください。さらにサポートが必要な場合は、[support@gl-inet.com](mailto:support@gl-inet.com) まで電子メールを送信してください。

3. バインディングの詳細。

    バインドが成功したら、ルーターの Web 管理パネルに戻り、**CLOUD SERVICES** -> **GoodCloud** に移動します。このページには、GoodCloud プラットフォームへのリダイレクト エントリ、デバイス ID の詳細、および最近のクラウド ログが表示されます。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. リモートアクセス。

    ファームウェア v4.10 では、ルーターが GoodCloud にバインドされると、ルーターの Web 管理パネルと端末へのリモート アクセスがデフォルトで有効になります。

5. デバイスのバインドを解除します。

    ルーターのバインドを解除したい場合は、ルーターの Web 管理パネルにログインし、**CLOUD SERVICES** -> **GL.iNet Account** に移動します。 「**Unbind**」をクリックします。

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    あるいは、GoodCloud プラットフォームのバインドされたデバイスリストからデバイスを削除することもできます。ルーターの Web 管理パネルが同期して、最新のバインド ステータスが表示されます。

    問題が発生した場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

### ファームウェア v4.7 ～ v4.9 の場合

1. GoodCloudを有効にします。

    ルーターの Web 管理パネルにログインし、**CLOUD SERVICE** -> **GoodCloud** に移動します。

    [**Get Started**] ボタンをクリックすると、右上隅に [クラウド サービス] ポップアップ ウィンドウが表示されます。 「**Enable**」をクリックします。

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

2. ログインしてデバイスをバインドします。

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    アカウントをお持ちでない場合は、アカウントを作成してログインしてください。登録が完了すると、ルーターは自動的にアカウントにバインドされます。

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    確認メールが届かない場合は、スパム フォルダーを確認するか、数分待ってからもう一度お試しください。さらにサポートが必要な場合は、[support@gl-inet.com](mailto:support@gl-inet.com) まで電子メールを送信してください。

3. バインディングの詳細。

    バインドが成功したら、ルーターの Web 管理パネルに戻り、右上隅のクラウド アイコンをクリックすると、ユーザー名、バインド時間、デバイス ID、デバイス MAC、デバイス S/N などのバインドの詳細が表示されます。

    ![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

4. リモートアクセスを有効にします。

    Web 管理パネルで、**CLOUD SERVICES** -> **GoodCloud** に移動すると、ルーターのリモート アクセスを有効にできます。

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

    - **Remote SSH**: GoodCloud プラットフォームから SSH 経由でルーターの端末にリモート アクセスするため。

    - **Remote Web Access**: GoodCloud プラットフォームから HTTP/HTTPS 経由でルーターの Web 管理パネルにリモート アクセスする場合。

    - **View Logs**: GoodCloudによるAPI呼び出しログを表示します。

5. デバイスのバインドを解除します。

    ルーターのバインドを解除したい場合は、ルーターの Web 管理パネルにログインします。右上隅にある雲のアイコンをクリックし、「**Unbind**」をクリックします。

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    あるいは、GoodCloud プラットフォームのバインドされたデバイスリストからデバイスを削除することもできます。ルーターの Web 管理パネルが同期して、最新のバインド ステータスが表示されます。

    問題が発生した場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

### ファームウェアv4.6以前の場合

1. GoodCloudを有効にします。

    ルーターの Web 管理パネルにログインし、**APPLICATIONS** -> **GoodCloud** に移動します。スイッチを切り替えて GoodCloud を有効にします。

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    必要に応じて、**Remote SSH** および **Remote Web Access** を有効にし、最も近いサーバーを選択し、**Terms of Service & Privacy Policy** を読んで同意し、**Apply** をクリックします。

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: GoodCloud プラットフォームから SSH 経由でルーターの端末にリモート アクセスするため。

    - **Remote Web Access**: GoodCloud プラットフォームから HTTP/HTTPS 経由でルーターの Web 管理パネルにリモート アクセスする場合。

    - **Data Server**: デバイスの場所に最も近いサーバーを選択してください。アジア太平洋地域 (Japan)、アメリカ (Oregon)、ヨーロッパ (Ireland) の 3 つのオプションがあります。

2. アカウントにサインアップします。

    [GoodCloud](https://www.goodcloud.xyz){target="_blank"} にアクセスし、サインアップしてログインします。

    確認メールが届かない場合は、スパム フォルダーを確認するか、数分待ってからもう一度お試しください。さらにサポートが必要な場合は、[support@gl-inet.com](mailto:support@gl-inet.com) まで電子メールを送信してください。

3. デバイスを追加します。

    クラウド プラットフォームで、**Devices** -> **Bound Devices** -> **Add Devices** に移動します。

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    デバイスをGoodCloudアカウントにバインドするには、自動検出、手動追加、一括インポートの3つの方法があります。

    ??? "Auto Discover"

        ルーターとGoodCloud Webサイトへのアクセスに使用されるデバイスが同じネットワーク上にある場合は、**Auto discover**を試すことができます。

        ドロップダウン リストからデバイスを選択し、**DDNS / Device ID** を入力します。これはルーターの下部、または Web 管理パネルの GoodCloud ページにあります。

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        デバイス ID を見つけるには、[this link](../faq/where_to_find_the_device_id_mac_sn.md) を参照してください。

    ??? "Manually Add"

        お使いのデバイスがリストにない場合は、**Manually add** をクリックしてルーターの詳細を入力します。要求されたすべての情報は、ルーターの下部、または Web 管理パネルの GoodCloud ページにあります。

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** は、多数のデバイスを管理するユーザー向けに設計されています。 Microsoft Excel ファイルを介して複数のデバイスをインポートできます。

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. バインディングの詳細。

    バインドが成功したら、ルーターの Web 管理パネルに戻り、**APPLICATIONS** -> **GoodCloud** に移動します。このページには、ユーザー名やバインド時刻などのバインドの詳細が表示されます。

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

5. デバイスのバインドを解除します。

    ルーターのバインドを解除したい場合は、ルーターの Web 管理パネルにログインし、**APPLICATION** -> **GoodCloud** に移動して、**Unbind** をクリックします。

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    あるいは、GoodCloud プラットフォームのバインドされたデバイスリストからデバイスを削除することもできます。ルーターの Web 管理パネルが同期して、最新のバインド ステータスが表示されます。

    問題が発生した場合は、[support@gl-inet.com](mailto:support@gl-inet.com) にメールでお問い合わせください。
