# GL.iNet GoodCloud

## コンテンツ

- [はじめに](#_2)
- [セットアップ](#_3)
    - [ルーターでGoodCloudを有効にする](#goodcloud)
    - [GoodCloudアカウント登録](#goodcloud_1)
    - [サーバーに域の選択](#_4)
    - [新規グループを追加する](#_5)
    - [デバイスの追加](#_6)
    - [ルーターウェブ管理パネルのバウンド情報](#web)
    - [ルーターのバインド解除](#_7)
- [デバイスの管理](#_8)
    - [デバイス情報とステータス](#_9)
    - [LTEシグナル](#lte)
    - [デバイス詳細情報](#_10)
    - [リモートアクセスWeb管理者パネル](#web_1)
    - [リモートアクセス・ルーターの端末](#_16)
    - [メールアラームの設定](#_17)
- [サイト・ツー・サイト](#site-to-site)
- [一括設定](#_18)
    - [単一デバイスの一括設定](#_19)
    - [複数のデバイスの一括設定](#_20)
    - [その彼の一括操作](#_21)
- [テンプレート管理](#_22)
    - [テンプレートの追加](#_23)
    - [アップグレード](#_24)
    - [テンプレートをルーターに適用する](#_25)
    - [複数のルーターにテンプレートを適用する](#_26)
- [タスクリスト](#_27)
- [GoodCloud と VPN](#goodcloudvpn)
- [Cloudをオフにする](#cloud)

## はじめに

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} cloud 管理サービスは、ルーターにリモートでアクセスして管理するための簡単かつシンプルな方法を提供します。で下にビデオによる紹介があります。

リモートデバイス管理ソリューション、GoodCloudのご紹介：

<iframe width="560" height="315" src="https://www.youtube.com/embed/JkV2PAy-_Og" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

中小企業へけGoodCloud Wi-Fi管理システムの簡単設定ガイド：

<iframe width="560" height="315" src="https://www.youtube.com/embed/7U1CwpKOKDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

特徴：

* ルーターのライブステータスを確認する
    - オンライン・オフラインのライブ・ステータス・チェック
    - ライブRAMとロードアベレージのチェック
    - LTEシグナル
    - オンライン・オフライン状態のアップデートを電子メールで通知

* ルーターをリモートでセットアップする
    - ルーター をリモートでセットアップする(SSID やキーなど)
    - リモートSSH
    - リモートアクセスWeb管理パネル

* ルーター上のクライアントをリモートで監視
    - ネットワークに接続しているユーザーを確認する
    - リアルタイムトラフィック監視とクライアントのブロック
    - 新規顧客とブロックに関する電子メールアラーム

* ルーターの一括操作
    - コンフィグテンプレートを設定し、ルーターを一括設定する
    - ルーターを一括でリブートまたはアップグレードする

* ルーターをグループで管理する
    - デバイスをグループごとに分ける
    - 1 ページでデバイスを管理

* サイト・ツー・サイト
    - バーチャルオフィス：オフィスのネットワークを彼のオフィスへ拡張
    - 出張：オフィスのOA、CRM、MySQLシステムにリモートアクセス
    - スマート ホーム: から宅のIP カメラ、NAS、その彼のデバイスにリモート アクセス

## セットアップ

クラウド機できるを有効にし、GoodCloudにバインドする方法については、で下のビデオチュートリアルがあります。

<iframe width="560" height="315" src="https://www.youtube.com/embed/mvJQZphSO1A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### ルーターでGoodCloudを有効にする

ウェブ管理画面の左側→アプリケーション→GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/enable_goodcloud.png){class="glboxshadow"}

上記の手順に従ってCloud機できるを有効にすると、ルーターがGoodCloudサーバーに接続できるようになります。

* **リモートSSH** は、GoodCloud経よりでルーターの端末にリモートアクセスするためのものです。 [こちら](#remote-access-routers-terminal)をご覧ください。

* **リモートWebアクセス** は、GoodCloud経よりでルーターのWeb管理パネルにリモートアクセスするためのものです。 [こちら](#remote-access-web-admin-panel)をご覧ください。

* **データサーバー**、お使いの機器に最もも近いサーバーをお選びください。データサーバーは、**アジアとても平洋**(日本)、**アメリカ**(オレゴン)、**ヨーロッパ**(アイルランド)の3つがあります。

### GoodCloudアカウント登録

  [https://www.goodcloud.xyz](https://www.goodcloud.xyz){target="_blank"}にアクセスし、サインアップしてからサインインします。 確認メールが届かない場合は、迷惑メールのフォルダをチェックするか、後でメールを確認してください。登録に問題がある場合は、 [support@glinet.biz](mailto:support@glinet.biz) までメールでお問い合わせください。

### サーバーのに域を選択

初回サインイン時に、に域を選択するダイアログが表示されます。Web管理パネル([Step of enable GoodCloud on router](#enable-goodcloud-on-router))で選択したデータサーバーと same じに域を選択してください。

右上隅でいつでもに域を変よりできます。

![select region button](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/select_region_button.png){class="glboxshadow"}

### 新しいグループを追加する

左側 -> グループリスト -> グループの追加

新しいグループを追加するには、で下の手順に従ってください。

![add group](https://static.gl-inet.com/goodcloud/docs/add-group.png){class="glboxshadow"}

グループ名、ことになる社名、説明、所ににを設定してください。

各デバイスはグループに属している必要があります。

### デバイスを追加

左側 -> デバイスリスト -> デバイス追加。 デバイスを GoodCloud アカウントにバインドするには、 **から動検出**、 **手動で追加**と**一括インポート**の 3 つの方法があります。

=== "から動検出"

    ルーターとPC(GoodCloudウェブサイトを開いたPC)が same じネットワーク内にある場合は、**から動検出**をお試しください。
    
    で下の手順に従ってデバイスを追加してください。

    ![add device](https://static.gl-inet.com/goodcloud/docs/add-device.png){class="glboxshadow"}

    デバイス ID を確認するには、[こちら](../faq/where_to_find_the_device_id_mac_sn.md)を確認してください。

        注意：ここで「DDNS/デバイスID」を入力するのは、ルーターが確かにオリジナル/有効であることを確認するためで す。

        グループを追加したことがない場合は、から動のにデフォルトのグループが作成されます。

    「アップデート」 をクリックすると、強制のにデバイスのから動検出が再開されます。

    ![auto discover](https://static.gl-inet.com/goodcloud/docs/auto-discover.png){class="glboxshadow"}

=== "手動で追加"

    から動検出できない場合は、「手動で追加」を試してください。入力が必要な情報はすべてルーターの背面に記載されています。

        注意：ここで「MAC」、「SN」、「DDNS」/「デバイスID」を入力するのは、ルーターが本当にオリジナルで有効かどうかを確認するためです。

    新しいモデルの場合、ルーターの背面に**デバイスID**が記載されています。

    ![manually add device](https://static.gl-inet.com/goodcloud/docs/manually-add-device-device-id.png){class="glboxshadow"}

    旧モデルの場合、ルーターの背面に**DDNS**と記載されています。**DDNS**の最も初の7文字のみが必要です。

    ![manually add device](https://static.gl-inet.com/goodcloud/docs/manually-add-device.png){class="glboxshadow"}

=== "一括インポート"

    「一括インポート」は、追加するデバイスが多数あるユーザーへけです。 「一括インポート」を使用すると、Microsoft Excel ファイルで多数のデバイスをインポートできます。

### ルーター Web 管理パネル上のバインド情報

ルーターをGoodCloudに追加した後、ルーターのウェブ管理パネルに戻り、左側の「アプリケーション」→「GoodCloud」を選択 して、

このページをアップデートすると、バインドされたGoodCloudのユーザー名と日付が表示されます。

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_bound_info.png){class="glboxshadow"}

### ルーターのバインドを解除

ルーターのバインドを解除したい場合は、ルーターのウェブ管理パネルの左側にある　アプリケーション->GoodCloudの**バインド解除**ボタンをクリックします。

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_unbind.png){class="glboxshadow"}

## デバイス管理

### デバイス情報とステータス

 [Goodcloud](https://www.goodcloud.xyz)にサインイン、左側のデバイスリストをチェックします。

![device list table](https://static.gl-inet.com/goodcloud/docs/device_list_table.png){class="glboxshadow"}

この表の最も初の列にアイコンがあります、

![online icon](https://static.gl-inet.com/goodcloud/docs/online_icon.png) このデバイスがオンラインであることを意味します。

![offline icon](https://static.gl-inet.com/goodcloud/docs/offline_icon.png) このデバイスがオフラインであることを意味します。

![deactovate icon](https://static.gl-inet.com/goodcloud/docs/deactivate_icon.png) このデバイスが非アクティブ化されており、これまでに GoodCloud に接続したことがないことを意味します。

![column selector](https://static.gl-inet.com/goodcloud/docs/column_selector.png){class="glboxshadow"}

表示させたい列を選択します。

`オンライン時間` はデバイスがGoodCloudに接続した最も新の時間です。

`オフライン時間` はデバイスがGoodCloudを切断した最も新の時間です。

`アップデート時間` は、デバイスがGoodCloudに接続または切断された最も新の時間です。

`IP`、ルーターがVPNクライアントを実行している場合、このIPはデフォルトでVPN IPになります。 <a href="#goodcloud-and-vpn">詳細はこちら</a>

### LTE シグナル

GL-MiFi、GL-X750などの4Gデバイスのみ使用可できるです。

デバイスリストページの列を切り替えます。

![device LTE signal](https://static.gl-inet.com/goodcloud/docs/lte_signal.png){class="glboxshadow"}

シグナル強度、タイプ、関連するパラメーターが表示されます。

![device LTE signal](https://static.gl-inet.com/goodcloud/docs/lte_signal_2.png){class="glboxshadow"}

### デバイス詳細情報

左側のデバイスリストで、オンラインデバイスの名前をクリックすると、WiFi、クライアントのデバイスを管理するページが開き、ルータ情報、メモリ使用量、稼働時間、ロードアベレージ、ログが表示されます。

![to device detail page](https://static.gl-inet.com/goodcloud/docs/to_device_detail.png){class="glboxshadow"}

#### デバイス情報

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-device-info.png){class="glboxshadow"}

#### WiFi

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-wifi.png){class="glboxshadow"}

すべてのWiFi設定を変よりします。

#### ルーターのステータス

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-router-status.png){class="glboxshadow"}

#### クライアントリスト

![device info](https://static.gl-inet.com/goodcloud/docs/edit-device-client-list.png){class="glboxshadow"}

#### タイムライン

「タイムライン」タブには、ルーターのアクティビティと、ルーターに関連するIoTデバイスによってアップロードされたメッセージが表示されます。

![device timeline](https://static.gl-inet.com/goodcloud/docs/timeline.png){class="glboxshadow"}

#### ツール

 `Ping`と`Traceroute`の2つのツールがあります。

![tools ping traceroute](https://static.gl-inet.com/goodcloud/docs/tools_ping_traceroute.png){class="glboxshadow"}

### リモートアクセスWeb管理パネル

注意：この機できるを使用するには、3.211にアップグレードしてください。

これらのアイコンが見つからない場合は、 [こちら](#enable-goodcloud-on-router)をチェックして、それが有効になっていることを確認してください。

この機できるが動作しない場合は、ブラウザのシークレットモードをお試しください。

![remote access web admin panel](https://static.gl-inet.com/goodcloud/docs/remote_access_web_admin_panel.png){class="glboxshadow"}

### リモートアクセス・ルーターの端末

注意：この機できるを使用するには、3.211にアップグレードしてください。

これらのアイコンが見つからない場合は、 [こちら](#enable-goodcloud-on-router)をチェックして、それが有効になっていることを確認してください。

この機できるが動作しない場合は、ブラウザのシークレットモードをお試しください。

![remote access web admin panel](https://static.gl-inet.com/goodcloud/docs/remote_access_terminal.png){class="glboxshadow"}

### メールアラームの設定

デバイスがオンライン、オフライン、新しいクライアントに接続されたときに電子メールアラームを設定することができます。

左側 -> 設定 -> アラーム設定で、アラームルールを作成します。

![create alarm rules](https://static.gl-inet.com/goodcloud/docs/create-alarm-rules.png){class="glboxshadow"}

次に、通知を受け取るメールアドレスを設定します。確実にメールを受信するために、admin@goodcloud.xyz をアドレス帳に追加してください。

![alarm rules](https://static.gl-inet.com/goodcloud/docs/alarm-rules.png){class="glboxshadow"}

## Site to Site

[GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md)を参照してください。

## 一括設定

この機できるを使用して、1つのデバイスに対して複数のパラメータを設定することも、複数のデバイスに対して複数のパラメータを設定することもできます。

   注意：この機できるはビジネスユーザーのみが利用できます。

### 単一デバイスの一括設定

単一デバイスを設定するには、で下のようにします。

  <a href="https://static.gl-inet.com/goodcloud/docs/modify_configuration.png" target="_blank"><img alt="Modify Configuration" src="https://static.gl-inet.com/goodcloud/docs/modify_configuration.png"></a>

下の画像の左側が正しいです。もし下の画像の右側のようなインターフェースであれば、最も新のテスト用ファームウェアにアップグレードしてください。

  <a href="https://static.gl-inet.com/goodcloud/docs/single_configuration.png" target="_blank"><img alt="Single Configuration" src="https://static.gl-inet.com/goodcloud/docs/single_configuration.png"></a>

変よりが必要な構成を確認し、値を入力します。
  
![Add Configuration](https://static.gl-inet.com/goodcloud/docs/add_configuration.png){class="glboxshadow"}

チェックされた構成は必須であり、ルールに適合する構成のみが記入可できるであります。 構成が配信された後、すぐに有効になるわけではありません。構成が有効になり、デバイスを再起動する必要があります。 上図の右下隅にある「Restart now（今すぐ再起動）」オプションをチェックすることができます。 構成が完たすると、デバイスはすぐに再起動します。

構成をプレビューし、配信を確認します。

![Preview Configuration](https://static.gl-inet.com/goodcloud/docs/preview_configuration.png){class="glboxshadow"}

**Restart now** オプションのチェックを外すと、プロンプトが表示されます。

<a href="https://static.gl-inet.com/goodcloud/docs/config_not_take_effect.png" target="_blank"><img alt="config not take effect" src="https://static.gl-inet.com/goodcloud/docs/config_not_take_effect.png"></a>

### 複数デバイスの一括設定

構成したいデバイスを選択します。

![mutiple configuration](https://static.gl-inet.com/goodcloud/docs/mutiple_configuration.png){class="glboxshadow" width="800"}

その彼の操作は、単一デバイスを操作する場合と same じです。

### その彼の一括操作

その彼の一括操作： 彼のグループへの移動、アップグレード、再起動、削除。

![Task](https://static.gl-inet.com/goodcloud/docs/task.png){class="glboxshadow"}

## テンプレート管理

よく使う構成をテンプレートとして保存し、一括で構成を変よりする際に素早く適用できます。

    注意：この機できるはビジネスユーザーのみが利用できます。

### テンプレートの追加

変よりが必要な構成を確認し、値を入力します。ほとんどのオプションはウェブ管理パネルと same じです。

![Add Template](https://static.gl-inet.com/goodcloud/docs/add_template.png){class="glboxshadow"}

#### アップグレード

**Upgrade Path**はカスタムファームウェアのアップグレード用です。ファームウェアとテキストファイルをウェブサーバーに置き、そのURLを**Upgrade Path**に置きます。例えば、 [https://fw.gl-inet.com/firmware/ar750/v1/](https://fw.gl-inet.com/firmware/ar750/v1/) は Upgrade Path、  **list-sha256.txt** ファイル [https://fw.gl-inet.com/firmware/ar750/v1/list-sha256.txt](https://fw.gl-inet.com/firmware/ar750/v1/list-sha256.txt) と対応するファームウェア・ファイル [https://fw.gl-inet.com/firmware/ar750/v1/openwrt-ar750-3.203-0701.bin](https://fw.gl-inet.com/firmware/ar750/v1/openwrt-ar750-3.203-0701.bin)があります。

    注意：GL-AX1800、GL-S1300、GL-B1300、GL-AP1300は今のところhttp pathのみサポートしています。

![Template info](https://static.gl-inet.com/goodcloud/docs/template_upgrade_path.png){class="glboxshadow"}

テキストファイルのコンテンツは [これ](https://fw.gl-inet.com/firmware/ar750/v1/list-sha256.txt)のようなもので、名前は**list-sha256.txt**とすべきである。4 つの列があり、初の列はファームウェアのバージョン、2番目の列はファームウェアファイルの名前、3番目の列はファームウェアファイルのsha256、4番目の列はファームウェアファイルのサイズである。

![gl-ar750 sha256](https://static.gl-inet.com/goodcloud/docs/ar750-sha256.png){class="glboxshadow"}

テンプレートに名前と説明を付けます。

![Template info](https://static.gl-inet.com/goodcloud/docs/template_info.png){class="glboxshadow"}

### ルーターにテンプレートを適用します。

テンプレートを作成し、このテンプレートをルーターに適用したい場合、 **デバイスリスト** テンプレートを適用したいルーターを見つけ、オンラインであることを確認し、アクション列で歯車のアイコンをクリックし、 **構成変より** 項目をクリックします。 **構成一括変より**ダイアログがポップアップします。

ダイアログの右上で、既に作成されているテンプレートを選択することができます。そして右下の**Apply**ボタンをクリックします。

テンプレートの構成を確認するために別のダイアログがポップアップし、一番下までスクロールして**確認**ボタンをクリックすると、今回の変よりにテンプレートの構成を上書きして読み込みます。

**Apply** ボタンをクリックします。**Apply** ボタンをクリックした後、ルーターが再起動され、有効になりますのでご注意ください。

### 複数のルーターにテンプレートを適用する

テンプレートを作成し、このテンプレートを複数のルーターに適用する場合、この手順は、1台のルーターに適用する手順とよく似ています。**デバイスリスト**ページでルーターを複数選択し、**一括操作**をクリックし、**構成変より**項目をクリックします。**一括構成変より**ダイアログが表示されます。

ダイアログの右上で、既に作成されているテンプレートを選択することができます。そして右下の**Apply**ボタンをクリックします。

テンプレートの構成を確認するために別のダイアログがポップアップし、一番下までスクロールして**確認**ボタンをクリックすると、今回の変よりにテンプレートの構成を上書きして読み込みます。

**Apply** ボタンをクリックします。**Apply** ボタンをクリックした後、ルーターが再起動され、有効になりますのでご注意ください。

## タスクリスト

タスクリストページでは、構成テンプレートの実行結果が表示されます。

    注意：この機できるはビジネスユーザーのみが利用できます。

![Task list](https://static.gl-inet.com/goodcloud/docs/task_list.png){class="glboxshadow"}

各デバイスと構成の実行結果をチェックすることができます。

![Task list detail info](https://static.gl-inet.com/goodcloud/docs/task_list_detail_info.png){class="glboxshadow"}

## GoodCloudとVPN

ルーターでGoodCloud機できるを有効にし、 same 時にVPNクライアントを起動した場合、デフォルトではルーターとGoodCloudサーバー間の接続もVPNを経よりしますが、VPN接続が不安定な場合や、VPNプロバイダーが誤ってGoodCloud接続をフィルタリングする場合がありますので、で下の設定でGoodCloud接続をVPNを経よりしないようにすることができます。

ウェブ管理パネルの左側、VPN -> VPNダッシュボード -> VPNクライアント -> グローバルオプション。

![Services from GL.iNet doesn't Use VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/goodcloud_donot_use_vpn.png){class="glboxshadow"}

ノードがVPNクライアントを実行している間にSite to Siteを実行することは推奨されません。

## cloudオフにする

GoodCloudサービスを停止するには、ルーターのウェブ管理パネルでサービスをオフにしてください。で下の手順に従ってください。GoodCloudウェブサイト上では何もする必要はありません。

![disable cloud](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/turn_off_cloud.png){class="glboxshadow"}

Cloudを無効にすると、で下のようなインターフェイスになります。

![after disable cloud](https://static.gl-inet.com/docs/router/en/4/tutorials/cloud/after_turn_off_cloud.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
