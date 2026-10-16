# GL.iNet GoodCloud

## はじめに {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、接続されたデバイスのリモート展開と管理を簡素化するために設計されたプラットフォームです。GL.iNet ルーターにリモートでアクセスして管理する簡単な方法を提供します。ネットワークデバイスをクラウド上で一元管理することで、ネットワーク構成の展開やソフトウェアのアップグレードなどの一括管理タスクを効率的に実行できます。また、ルーターの Web 管理パネルにリモートでアクセスしたり、SSH 経由でルーターのターミナルに接続したりすることもでき、地域をまたいだエンドツーエンドのネットワークデバイス管理を実現します。

GoodCloud では、次のことができます。

1. ルーターのリアルタイムステータスを確認する
    - オンライン/オフライン状態を監視する
    - リアルタイムの RAM 使用量と負荷平均を表示する
    - オンライン/オフライン状態の変化に関するメールアラートを受信する

2. ルーターをリモートで設定する
    - ルーター設定（SSID やパスワードなど）を構成する
    - リモート SSH アクセス
    - WebUI へのリモートアクセス
    - ルーターへのアクセス権を他のユーザーと共有する

3. 接続されているクライアントをリモートで監視する
    - ネットワークに接続されているデバイスを表示する
    - リアルタイムのトラフィックを監視し、クライアントをブロックする
    - 新しい接続やブロックイベントに関するメールアラートを受信する

4. 一括操作を実行する
    - 一括再起動
    - ファームウェアの一括アップグレード

5. サイトツーサイト接続を確立する
    - バーチャルオフィス: オフィスネットワークを他の支社に拡張する
    - 出張: オフィスのシステム（OA、CRM、MySQL など）にリモートアクセスする
    - スマートホーム: 自宅のデバイス（IP カメラ、NAS など）にリモートアクセスする

複数のデバイスを管理し、一括操作、マルチアカウント管理、カスタマイズされたソリューションなどの高度な機能を利用したい場合は、付加価値プランをお選びください。詳細は[こちら](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"}をご覧ください。お気軽に [support@gl-inet.com](mailto:support@gl-inet.com) までお問い合わせください。

## デバイスをクラウドにバインドする {#bind-devices-to-cloud}

デバイスのファームウェアバージョンに応じて、該当するセクションのバインド手順を参照してください。

### ファームウェア v4.10 以降の場合 {#for-firmware-v410-and-above}

1. GoodCloud を有効にします。

    ルーターの Web 管理パネルにログインし、**CLOUD SERVICE** -> **GoodCloud** に移動して、**Get Started** をクリックします。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    **GL.iNet Account** ページが表示されます。**Bind GL.iNet Account via URL** をクリックします。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    ポップアップウィンドウで **Continue** をクリックします。GoodCloud の Web サイトにリダイレクトされるので、そこでバインドを完了します。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. ログインしてデバイスをバインドします。

    GL.iNet アカウントにログインします。アカウントをお持ちでない場合は、アカウントを登録してからログインしてください。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    ログイン後、アカウント情報と、デバイス ID、モデル、MAC アドレスなどのデバイス情報を確認します。デバイス名を任意に設定して **Bind** をクリックすると、ルーターがアカウントにバインドされます。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    確認メールが届かない場合は、迷惑メールフォルダを確認するか、数分待ってから再度お試しください。さらにサポートが必要な場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

3. バインドの詳細。

    バインドが完了したら、ルーターの Web 管理パネルに戻り、**CLOUD SERVICES** -> **GoodCloud** に移動します。このページには、GoodCloud プラットフォームへのリンク、デバイスの識別情報、最近のクラウドログが表示されます。

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. リモートアクセス。

    ファームウェア v4.10 では、ルーターを GoodCloud にバインドすると、ルーターの Web 管理パネルとターミナルへのリモートアクセスがデフォルトで有効になります。

5. デバイスのバインドを解除します。

    ルーターのバインドを解除する場合は、ルーターの Web 管理パネルにログインし、**CLOUD SERVICES** -> **GL.iNet Account** に移動して、**Unbind** をクリックします。

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    または、GoodCloud プラットフォームの Bound Devices リストからデバイスを削除することもできます。ルーターの Web 管理パネルにも同期され、最新のバインド状態が表示されます。

    問題が発生した場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

### ファームウェア v4.7～v4.9 の場合 {#for-firmware-v47-to-v49}

1. GoodCloud を有効にします。

    ルーターの Web 管理パネルにログインし、**CLOUD SERVICE** -> **GoodCloud** に移動します。

    **Get Started** ボタンをクリックすると、右上に **Cloud Service** ポップアップウィンドウが表示されます。**Enable** をクリックします。

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

2. ログインしてデバイスをバインドします。

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    アカウントをお持ちでない場合は、アカウントを登録してからログインしてください。登録が完了すると、ルーターは自動的にアカウントにバインドされます。

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    確認メールが届かない場合は、迷惑メールフォルダを確認するか、数分待ってから再度お試しください。さらにサポートが必要な場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

3. バインドの詳細。

    バインドが完了したら、ルーターの Web 管理パネルに戻り、右上のクラウドアイコンをクリックすると、ユーザー名、バインド日時、Device ID、Device MAC、Device S/N などのバインドの詳細が表示されます。

    ![binding details](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/binding_details.png){class="glboxshadow"}

4. リモートアクセスを有効にします。

    Web 管理パネルで **CLOUD SERVICES** -> **GoodCloud** に移動すると、ルーターのリモートアクセスを有効にできます。

    ![enable remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_remote_access.png){class="glboxshadow"}

    - **Remote SSH**: GoodCloud プラットフォームから SSH 経由でルーターのターミナルにリモートアクセスするための機能です。

    - **Remote Web Access**: GoodCloud プラットフォームから HTTP/HTTPS 経由でルーターの Web 管理パネルにリモートアクセスするための機能です。

    - **View Logs**: GoodCloud による API 呼び出しのログを表示します。

5. デバイスのバインドを解除します。

    ルーターのバインドを解除する場合は、ルーターの Web 管理パネルにログインします。右上のクラウドアイコンをクリックし、**Unbind** をクリックします。

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    または、GoodCloud プラットフォームの Bound Devices リストからデバイスを削除することもできます。ルーターの Web 管理パネルにも同期され、最新のバインド状態が表示されます。

    問題が発生した場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

### ファームウェア v4.6 以前の場合 {#for-firmware-v46-or-earlier}

1. GoodCloud を有効にします。

    ルーターの Web 管理パネルにログインし、**APPLICATIONS** -> **GoodCloud** に移動します。スイッチをオンにして GoodCloud を有効にします。

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    必要に応じて **Remote SSH** と **Remote Web Access** を有効にし、最も近いサーバーを選択します。**Terms of Service & Privacy Policy** を読んで同意し、**Apply** をクリックします。

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: GoodCloud プラットフォームから SSH 経由でルーターのターミナルにリモートアクセスするための機能です。

    - **Remote Web Access**: GoodCloud プラットフォームから HTTP/HTTPS 経由でルーターの Web 管理パネルにリモートアクセスするための機能です。

    - **Data Server**: デバイスの設置場所に最も近いサーバーを選択してください。Asia Pacific (Japan)、America (Oregon)、Europe (Ireland) の 3 つの選択肢があります。

2. アカウントを登録します。

    [GoodCloud](https://www.goodcloud.xyz){target="_blank"} にアクセスし、アカウントを登録してログインします。

    確認メールが届かない場合は、迷惑メールフォルダを確認するか、数分待ってから再度お試しください。さらにサポートが必要な場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

3. デバイスを追加します。

    クラウドプラットフォームで、**Devices** -> **Bound Devices** -> **Add Devices** に移動します。

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    デバイスを GoodCloud アカウントにバインドするには、Auto Discover、Manually Add、Bulk Import の 3 つの方法があります。

    ??? "Auto Discover"

        ルーターと、GoodCloud の Web サイトにアクセスするデバイスが同じネットワーク上にある場合は、**Auto discover** を試すことができます。

        ドロップダウンリストからデバイスを選択し、**DDNS / Device ID** を入力します。これはルーターの底面、または Web 管理パネルの GoodCloud ページで確認できます。

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        デバイス ID の確認方法については、[こちら](../faq/where_to_find_the_device_id_mac_sn.md)を参照してください。

    ??? "Manually Add"

        デバイスがリストにない場合は、**Manually add** をクリックしてルーターの情報を入力します。必要な情報はすべて、ルーターの底面、または Web 管理パネルの GoodCloud ページで確認できます。

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** は、多数のデバイスを管理するユーザー向けの機能です。Microsoft Excel ファイルを使用して複数のデバイスをインポートできます。

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. バインドの詳細。

    バインドが完了したら、ルーターの Web 管理パネルに戻り、**APPLICATIONS** -> **GoodCloud** に移動します。このページには、ユーザー名やバインド日時などのバインドの詳細が表示されます。

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info.png){class="glboxshadow"}

5. デバイスのバインドを解除します。

    ルーターのバインドを解除する場合は、ルーターの Web 管理パネルにログインし、**APPLICATION** -> **GoodCloud** に移動して、**Unbind** をクリックします。

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    または、GoodCloud プラットフォームの Bound Devices リストからデバイスを削除することもできます。ルーターの Web 管理パネルにも同期され、最新のバインド状態が表示されます。

    問題が発生した場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までメールでお問い合わせください。

## デバイスの管理 {#manage-devices}

### システム情報と操作 {#system-info-and-actions}

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** では、アカウントにバインドされているすべてのデバイスのシステム情報（モデル、バージョン、MAC アドレス、IP アドレスなど）とステータス（オンライン、オフラインなど）を確認できます。

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

デバイスを選択すると、右上から設定の変更、ファームウェアのアップデート、デバイスへのリモートアクセス、再起動、リセットなどの操作を実行できます。

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

リストのヘッダー右端にある歯車アイコンをクリックすると、表示する列とその順序をカスタマイズでき、重要なデバイス情報に絞って確認できます。

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### デバイスの詳細 {#device-details}

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** でデバイス名をクリックすると、デバイスの詳細ページに移動します。このページには、ルーターの基本情報、統計データ、ネットワーク設定、クライアントリストなどが表示されます。

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### 基本情報 {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### 統計情報 {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### ネットワーク設定 {#network-settings}

このページには、ルーターのネットワーク構成と Wi-Fi 設定が表示されます。

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### クライアントリスト {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## リモートアクセス {#remote-access}

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** で、アクセスしたいデバイスの名前をクリックして詳細ページを開くと、右上にリモート操作が表示されます。

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

**Remote GUI** をクリックすると、ルーターの Web 管理パネルにリモートでアクセスできます。

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

このオプションがグレーアウトしている、または使用できない場合は、この機能が無効になっている可能性があります。GoodCloud からアクセスする前に、まずルーターの Web 管理パネルでこの機能を有効にしてください。

このオプションはクリックできるものの反応がない場合は、ブラウザのシークレットモード/InPrivate モードをお試しください。

### Remote SSH {#remote-ssh}

**Remote SSH** をクリックすると、SSH 経由でルーターのターミナルにリモートでアクセスできます。

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

このオプションがグレーアウトしている、または使用できない場合は、この機能が無効になっている可能性があります。GoodCloud からアクセスする前に、まずルーターの Web 管理パネルでこの機能を有効にしてください。

このオプションはクリックできるものの反応がない場合は、ブラウザのシークレットモード/InPrivate モードをお試しください。

## 設定の変更 {#modify-settings}

1 台または複数台のデバイスに対して、複数のパラメータを設定できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** で設定したいデバイスを選択し、右上の **Settings** -> **Modify Settings** をクリックします。

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

ここでは、ワイヤレス、イーサネット、セキュリティ、ポート転送、LAN、システム設定など、ルーターのネットワーク設定を確認および変更できます。

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## メールアラーム {#email-alarm}

デバイスのステータスが変化したとき（オンライン/オフライン）や、新しいクライアントが接続したときに通知するメールアラームを設定できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** で、右上の **Add Rule** ボタンをクリックします。

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

監視したいデバイスを選択し、**Next** をクリックします。

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

デバイスのオンライン/オフライン状態などのトリガーイベントを選択し、**Next** をクリックします。

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

ルールの設定内容を確認し、**Apply** をクリックします。

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Notifications リストでは、作成したアラートルールを確認できます。個人ユーザーが作成できるアラートルールは 1 つまでです。デバイスの一括管理が必要な場合は、お気軽にお問い合わせいただき、プランをアップグレードしてください。

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## サイトツーサイト {#site-to-site}

[GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md) を参照してください。

## GoodCloud と VPN {#goodcloud-and-vpn}

ルーターで **GoodCloud** と **VPN client** を同時に有効にした場合、デフォルトでは、ルーターと GoodCloud サーバー間の接続は VPN を経由しません。これにより、GoodCloud サービスへのより安定した接続が確保されます。

ただし、GoodCloud の接続を VPN 経由にしたい場合は、ルーターの Web 管理パネルでこの設定を変更できます。VPN -> VPN Dashboard -> VPN Client -> Options に移動し、「Services from GL.iNet Use VPN」オプションを有効にしてください。

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

GoodCloud を VPN 経由でルーティングすると、特に次のような場合に、クラウド接続の安定性に影響する可能性があることに注意してください。

* VPN 接続が不安定である
* VPN プロバイダーが GoodCloud のトラフィックをフィルタリングまたはブロックしている
* VPN によって接続の遅延が大幅に増加する

最適なパフォーマンスと信頼性を得るため、通常は GoodCloud が VPN をバイパスするデフォルト設定のままにしておくことをお勧めします。

## ログの表示 {#view-logs}

必要に応じて、Activity Logs、Device Logs、Upgrade Logs、Alert Logs、Device Settings Logs などの GoodCloud ログを確認できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** に移動し、ドロップダウンリストから表示したいログを選択します。

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## クラウドの無効化 {#disable-cloud}

デバイスをクラウドプラットフォームに接続する必要がなくなった場合は、ルーターの Web 管理パネルでクラウドサービスを無効にできます。

??? "ファームウェア v4.6 以前の場合"

    ルーターの Web 管理パネルにログインし、**APPLICATIONS** -> **GoodCloud** に移動して、スイッチをオフにして GoodCloud を無効にし、**Apply** をクリックします。

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    無効にすると、画面は次のように表示されます。

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "ファームウェア v4.7 以降の場合"

    ルーターの Web 管理パネルにログインし、右上のクラウドアイコンをクリックします。**Cloud Service** ポップアップで歯車アイコンをクリックし、**Disable** を選択します。

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    無効にすると、画面は次のように表示されます。

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## アカウントの削除 {#delete-account}

セキュリティ上の理由から、使用しなくなったアカウントは削除できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} プラットフォームで、右上のユーザー名をクリックし、**Personal Center** を選択します。ページの一番下までスクロールし、**Delete Account** をクリックします。

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    削除すると、関連するすべてのサービス、データ、個人情報が完全に消去され、復元することはできません。

    アカウントがいずれかの組織に所属している場合は、アカウントを削除する前に、すべての組織から退出してください。

---

まだご質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
