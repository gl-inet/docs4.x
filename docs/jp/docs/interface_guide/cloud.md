# GL.iNet GoodCloud

## 目次

- [はじめに](#introduction)
- [デバイスを GoodCloud にバインドする](#bind-devices-to-goodcloud)
    - [ファームウェア v4.6 以前の場合](#for-firmware-v46-or-earlier)
        - [GoodCloud を有効にする](#enable-goodcloud)
        - [アカウントを登録する](#sign-up-an-account)
        - [デバイスを追加する](#add-devices)
        - [バインド情報](#binding-details)
        - [デバイスのバインドを解除する](#unbind-device)
    - [ファームウェア v4.7 以降の場合](#for-firmware-v47-or-later)
        - [Cloud Service を有効にする](#enable-cloud-service)
        - [バインド情報](#binding-details_1)
        - [デバイスのバインドを解除する](#unbind-device_1)
- [デバイスを管理する](#manage-devices)
    - [システム情報と操作](#system-info-and-actions)
    - [デバイスの詳細](#device-details)
        - [基本情報](#basic-info)
        - [統計情報](#statistics)
        - [ネットワーク設定](#network-settings)
        - [クライアント一覧](#clients-list)
- [リモートアクセス](#remote-access)
    - [Remote GUI](#remote-gui)
    - [Remote SSH](#remote-ssh)
- [設定を変更する](#modify-settings)
- [メールアラーム](#email-alarm)
- [Site to Site](#site-to-site)
- [GoodCloud と VPN](#goodcloud-and-vpn)
- [ログを表示する](#view-logs)
- [Cloud を無効にする](#disable-cloud)
- [アカウントを削除する](#delete-account)

## はじめに {#introduction}

GL.iNet の [GoodCloud](https://www.goodcloud.xyz){target="_blank"} は、接続されたデバイスのリモート展開と管理を簡素化するためのプラットフォームです。GL.iNet ルーターへ簡単にリモートアクセスし、管理できます。ネットワークデバイスをクラウド上で一元管理することで、ネットワーク設定の展開やソフトウェアアップグレードなどの一括管理作業を効率よく実行できます。また、ルーターの Web 管理画面へリモートアクセスしたり、SSH 経由でルーターのターミナルに接続したりできるため、地域をまたいだエンドツーエンドのネットワークデバイス管理を実現できます。

GoodCloud では、次のことが可能です。

1. ルーターのリアルタイム状態を確認する
    - オンライン / オフライン状態を監視する
    - RAM 使用率とロードアベレージをリアルタイムで確認する
    - オンライン / オフライン状態の変化に関するメールアラートを受け取る

2. ルーターをリモートで設定する
    - ルーター設定（SSID やパスワードなど）を構成する
    - Remote SSH でアクセスする
    - WebUI にリモートアクセスする
    - ほかのユーザーとルーターへのアクセス権を共有する

3. 接続中のクライアントをリモートで監視する
    - ネットワークに接続しているデバイスを確認する
    - リアルタイムのトラフィックを監視し、クライアントをブロックする
    - 新規接続やブロックイベントに関するメールアラートを受け取る

4. 一括操作を実行する
    - 一括再起動
    - 一括ファームウェアアップグレード

5. Site-to-Site 接続を構築する
    - 仮想オフィス: オフィスネットワークを他の支社へ拡張する
    - 出張時: オフィスシステム（OA、CRM、MySQL など）へリモートアクセスする
    - スマートホーム: 自宅のデバイス（IP カメラ、NAS など）へリモートアクセスする

複数のデバイスを管理し、一括操作、複数アカウント管理、カスタマイズソリューションなどの高度な機能を利用したい場合は、付加価値プランをご検討ください。詳細は [こちら](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} をご覧ください。ご不明な点があれば、[support@glinet.biz](mailto:support@glinet.biz) までお気軽にお問い合わせください。

## デバイスを GoodCloud にバインドする {#bind-devices-to-goodcloud}

デバイスをクラウドプラットフォームへ正常に接続するには、お使いのファームウェアバージョンに対応するバインド手順に従ってください。

### ファームウェア v4.6 以前の場合 {#for-firmware-v46-or-earlier}

#### GoodCloud を有効にする {#enable-goodcloud}

ルーターの Web 管理画面にログインし、**APPLICATIONS** -> **GoodCloud** に移動します。スイッチを切り替えて GoodCloud を有効にします。

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

必要に応じて **Remote SSH** と **Remote Web Access** を有効にし、最寄りのサーバーを選択して、**Terms of Service & Privacy Policy** を確認のうえ同意し、**Apply** をクリックします。

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH**: GoodCloud 経由でルーターのターミナルへリモートアクセスするための機能です。

- **Remote Web Access**: GoodCloud 経由でルーターの Web 管理画面へリモートアクセスするための機能です。

- **Data Server**: デバイスの設置場所に最も近いサーバーを選択してください。選択肢は Asia Pacific (Japan)、America (Oregon)、Europe (Ireland) の 3 つです。

#### アカウントを登録する {#sign-up-an-account}

[GoodCloud の Web サイト](https://www.goodcloud.xyz){target="_blank"} にアクセスし、アカウントを登録してログインします。

認証メールが届かない場合は、迷惑メールフォルダーを確認するか、数分待ってから再度お試しください。登録時に問題がある場合は、[support@glinet.biz](mailto:support@glinet.biz) までメールでお問い合わせください。

#### デバイスを追加する {#add-devices}

クラウドプラットフォームで **Devices** -> **Bound Devices** -> **Add Devices** に移動します。

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

デバイスを GoodCloud アカウントにバインドする方法は 3 つあります。Auto Discover、Manually Add、Bulk Import です。

??? "Auto Discover"

    ルーターと [GoodCloud の Web サイト](https://www.goodcloud.xyz){target="_blank"} にアクセスしている端末が同じネットワーク上にある場合は、**Auto discover** をお試しください。

    ドロップダウンリストからデバイスを選択し、**DDNS / Device ID** を入力します。これらの情報は、ルーター本体の底面、または Web 管理画面の GoodCloud ページで確認できます。

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Device ID の確認方法については、[こちらのリンク](../faq/where_to_find_the_device_id_mac_sn.md) を参照してください。

??? "Manually Add"

    デバイスが一覧に表示されない場合は、**Manually add** をクリックし、ルーターの情報を入力してください。必要な情報はすべて、ルーター本体の底面、または Web 管理画面の GoodCloud ページで確認できます。

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** は、多数のデバイスを管理するユーザー向けの機能です。Microsoft Excel ファイルを使用して複数のデバイスをまとめてインポートできます。

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### バインド情報 {#binding-details}

バインドに成功したら、ルーターの Web 管理画面に再度ログインし、**APPLICATIONS** -> **GoodCloud** に移動します。このページを更新すると、バインド済みの GoodCloud ユーザー名と日付が表示されます。

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### デバイスのバインドを解除する {#unbind-device}

ルーターのバインドを解除する場合は、ルーターの Web 管理画面にログインし、**APPLICATION** -> **GoodCloud** に移動して **Unbind** をクリックします。

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

または、GoodCloud プラットフォームの Bound Devices List から該当するデバイスを削除することもできます。すると、ルーターの Web 管理画面に最新のデバイスバインド状態が同期されます。

問題がある場合は、[support@glinet.biz](mailto:support@glinet.biz) までメールでお問い合わせください。

### ファームウェア v4.7 以降の場合 {#for-firmware-v47-or-later}

#### Cloud Service を有効にする {#enable-cloud-service}

ルーターの Web 管理画面にログインし、**CLOUD SERVICE** -> **GoodCloud** に移動します。

**Get Started** ボタンをクリックすると、右上に Cloud Service のポップアップウィンドウが表示されます。**Enable** をクリックして Cloud Service を使用します。

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

GoodCloud アカウントにログインします。

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

アカウントをお持ちでない場合は、登録してからログインしてください。登録が完了すると、ルーターは自動的にこのアカウントにバインドされます。

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

認証メールが届かない場合は、迷惑メールフォルダーを確認するか、数分待ってから再度お試しください。登録時に問題がある場合は、[support@glinet.biz](mailto:support@glinet.biz) までメールでお問い合わせください。

#### バインド情報 {#binding-details_1}

バインドが完了したら、ルーターの Web 管理画面に再度ログインし、右上の Cloud アイコンをクリックします。すると、バインド済みの GoodCloud ユーザー名と日付、Device ID、Device MAC、Device S/N などのバインド情報を確認できます。

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

Web 管理画面で **CLOUD SERVICES** -> **GoodCloud** に移動すると、ルーターのリモートアクセスを有効または無効にできます。

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH**: GoodCloud 経由でルーターのターミナルへリモートアクセスするための機能です。

- **Remote Web Access**: GoodCloud 経由でルーターの Web 管理画面へリモートアクセスするための機能です。

- **View Logs**: GoodCloud による API 呼び出しログを表示します。

#### デバイスのバインドを解除する {#unbind-device_1}

ルーターのバインドを解除する場合は、ルーターの Web 管理画面にログインし、右上のクラウドアイコンをクリックして **Unbind** を選択します。

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

または、GoodCloud プラットフォームの Bound Devices List から該当するデバイスを削除することもできます。すると、ルーターの Web 管理画面に最新のデバイスバインド状態が同期されます。

問題がある場合は、[support@glinet.biz](mailto:support@glinet.biz) までメールでお問い合わせください。

## デバイスを管理する {#manage-devices}

### システム情報と操作 {#system-info-and-actions}

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** では、アカウントにバインドされているすべてのデバイスのシステム情報（モデル、バージョン、MAC アドレス、IP アドレスなど）と状態（オンライン、オフラインなど）を確認できます。

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

デバイスを選択すると、右上から設定変更、ファームウェア更新、デバイスへのリモートアクセス、再起動、リセットなどの操作を実行できます。

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

リストヘッダー右端の歯車アイコンをクリックすると、列の表示内容や順序をカスタマイズでき、必要なデバイス情報を見やすく表示できます。

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### デバイスの詳細 {#device-details}

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** でデバイス名をクリックすると、デバイス詳細ページに移動します。このページでは、ルーターの基本情報、統計データ、ネットワーク設定、クライアント一覧などを確認できます。

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### 基本情報 {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### 統計情報 {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### ネットワーク設定 {#network-settings}

このページには、ルーターのネットワーク設定と Wi-Fi 設定が表示されます。

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### クライアント一覧 {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## リモートアクセス {#remote-access}

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** でアクセスしたいデバイス名をクリックして詳細ページに入ると、右上にリモート操作が表示されます。

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

**Remote GUI** をクリックすると、ルーターの Web 管理画面へリモートアクセスできます。

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

この項目がグレーアウトしている、または利用できない場合は、この機能が無効になっている可能性があります。まずルーターの Web 管理画面で有効にしてから、GoodCloud 経由でアクセスしてください。

この項目をクリックできるのに反応しない場合は、ブラウザーのシークレットモード / InPrivate モードでお試しください。

### Remote SSH {#remote-ssh}

**Remote SSH** をクリックすると、SSH 経由でルーターのターミナルへリモートアクセスできます。

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

この項目がグレーアウトしている、または利用できない場合は、この機能が無効になっている可能性があります。まずルーターの Web 管理画面で有効にしてから、GoodCloud 経由でアクセスしてください。

この項目をクリックできるのに反応しない場合は、ブラウザーのシークレットモード / InPrivate モードでお試しください。

## 設定を変更する {#modify-settings}

1 台のデバイスに対しても、複数台のデバイスに対しても、さまざまなパラメーターを設定できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** で設定したいデバイスを選択し、右上の **Settings** -> **Modify Settings** をクリックします。

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

ここでは、無線、Ethernet、セキュリティ、ポートフォワーディング、LAN、システム設定を含むルーターのネットワーク設定を確認および変更できます。

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## メールアラーム {#email-alarm}

デバイスの状態変化（オンライン / オフライン）や新しいクライアントの接続時に、メールアラームを設定できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** で、右上の **Add Rule** ボタンをクリックします。

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

監視したいデバイスを選択し、**Next** をクリックします。

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

デバイスのオンライン / オフライン状態など、トリガーイベントを選択し、**Next** をクリックします。

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

ルール設定を確認し、**Apply** をクリックします。

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Notifications 一覧では、作成したアラートルールを確認できます。個人ユーザーが作成できるアラートルールは 1 件までです。複数デバイスの一括管理が必要な場合は、プランのアップグレードについてお気軽にお問い合わせください。

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site {#site-to-site}

[GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md) を参照してください。

## GoodCloud と VPN {#goodcloud-and-vpn}

ルーターで **GoodCloud** と **VPN client** を同時に有効にした場合、ルーターと GoodCloud サーバー間の接続は、デフォルトでは VPN を経由しません。これにより、GoodCloud サービスへの接続がより安定します。

ただし、GoodCloud への接続を VPN 経由にしたい場合は、ルーターの Web 管理画面で設定を変更できます。VPN -> VPN Dashboard -> VPN Client -> Options に移動し、"Services from GL.iNet Use VPN" を有効にしてください。

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

なお、GoodCloud を VPN 経由にすると、特に次のような場合にクラウド接続の安定性へ影響することがあります。

* VPN 接続が不安定な場合
* VPN プロバイダーが GoodCloud のトラフィックをフィルタリングまたはブロックしている場合
* VPN によって接続遅延が大きくなる場合

一般的には、性能と信頼性を最適化するため、GoodCloud が VPN をバイパスするデフォルト設定のまま使用することを推奨します。

## ログを表示する {#view-logs}

必要に応じて GoodCloud のログを確認できます。Activity Logs、Device Logs、Upgrade Logs、Alert Logs、Device Settings Logs などに対応しています。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** に移動し、ドロップダウンリストから表示したいログを選択します。

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Cloud を無効にする {#disable-cloud}

デバイスをクラウドプラットフォームへ接続したくない場合は、ルーターの Web 管理画面で Cloud Service を無効にできます。

??? "For firmware v4.6 or earlier"

    ルーターの Web 管理画面にログインし、**APPLICATIONS** -> **GoodCloud** に移動して、スイッチを切り替えて GoodCloud を無効にし、**Apply** をクリックします。

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    無効にすると、画面は次のように表示されます。

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "For firmware v4.7 or later"

    ルーターの Web 管理画面にログインし、右上のクラウドアイコンをクリックします。

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    無効にすると、画面は次のように表示されます。

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## アカウントを削除する {#delete-account}

セキュリティ上の理由から、使用しなくなったアカウントは削除できます。

[GoodCloud](https://www.goodcloud.xyz){target="_blank"} プラットフォームで、右上のユーザー名をクリックして **Personal Center** を選択します。ページ下部までスクロールし、**Delete Account** をクリックします。

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    削除すると、関連するすべてのサービス、データ、個人情報が完全に消去され、復元することはできません。

    アカウントがいずれかの組織に所属している場合は、アカウントを削除する前に、まずすべての組織から退出してください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
