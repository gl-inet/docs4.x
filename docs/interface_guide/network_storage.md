# ネットワーク・ストレージ

## コンテンツ

- [はじめに](#introduction)
- [ストレージ・デバイスの挿入](#insert-storage-device)
- [Sambaをセットアップする](#set-up-samba)
- [WebDAVをセットアップする](#set-up-webdav)
- [DLNAのセットアップ](#set-up-dlna)
- [Samba クライアント](#samba-client)
- [WebDAV クライアント](#webdav-client)

## はじめに

一部のGL.iNetモデルはMicroSD(TF)カードをサポートし、一部のモデルはUSBポートを搭載、USBフラッシュドライブとポータブル外付けハードドライブをサポートし、このページでディスクのSamba、WebDAV、DLNAを設定できます。

サポートされているディスクフォーマットはNTFS、FAT32です。

**注意**： USBハードディスクの消費電力はかなり高いです。外部電源と一緒に使用してください。そうしないと、故障の原因になる可能性があります。

**注意**： 一部のモデルにはUSBポート/MicroSDスロットがありますが、ストレージ容量に制限があり、ファイル共有には対応していません。

## 対応モデル

通常、USBポートまたはMicroSD(TF)スロットを搭載したモデルは、ファイル共有に対応しています。フラッシュ容量が32MB以下のデバイスの場合、ネットワークストレージ機能はまだサポートされていません。

| ルーターモデル                  | USBポート | MicroSDカード | Samba| Webdav| DLNA |
| :----------------------------- | :------: | :----------: | :---: | :---: | :---: |
| GL-XE3000 (Puli AX)            | √        | √            | √     | √     | √     |
| GL-X3000 (Spitz AX)            | √        | √            | √     | √     | √     |
| GL-MT3000 (Beryl AX)           | √        | -            | √     | √     | √     |
| GL-AXT1800 (Slate AX)          | √        | √            | √     | √     | √     |
| GL-A1300 (Slate Plus)          | √        | -            | √     | √     | √     |
| GL-MT2500/GL-MT2500A (Brume 2) | √        | -            | √     | √     | √     |
| GL-S1300 (Convexa-S)           | √        | -            | √     | √     | √     |
| GL-MT1300 (Beryl)              | √        | √            | -     | -     | -     |
| GL-AX1800 (Flint)              | √        | -            | √     | √     | √     |
| GL-AR750S (Slate)              | √        | √            | -     | -     | -     |
| GL-XE300 (Puli)                | √        | √            | -     | -     | -     |
| GL-X750 (Spitz)                | √        | √            | -     | -     | -     |
| GL-SFT1200 (Opal)              | √        | -            | -     | -     | -     |
| GL-B1300 (Convexa-B)           | √        | -            | -     | -     | -     |
| GL-AP1300 (Cirrus)             | -        | -            | -     | -     | -     |
| GL-X300B (Collie)              | -        | -            | -     | -     | -     |
| GL-MV1000/GL-MV1000W (Brume)   | √        | √            | √     | √     | √     |

## ストレージ・デバイスの挿入

TFカードの場合は、まずルーターの電源を切り、TFカードを挿入してからルーターの電源を入れる必要があります。

USBドライブの場合、USBポートに直接差し込むことができます。ポータブル外付けハードドライブの場合、別途電源をお持ちの場合は、電源に接続してください。

ウェブ管理パネル -> アプリケーション -> ネットワークストレージ

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

ディスクが見つかると

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Sambaをセットアップする

1. Sambaを有効にするにはトグルをオンにし、その他のパラメーターについては以下を参照し、**Apply**をクリックする。

    * WANからのWebDAVアクセスを許可します。上位のデバイスがWebDAVにアクセスできるようにしたい場合は、これを有効にします。

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. 次に、共有リンクを取得するように設定しましょう。 ディスクが検出されると、**クイック セットアップ共有**のリンクが表示されます。**クイック セットアップ共有** をクリックします。

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. ユーザーを追加します。すでにアカウントをお持ちの場合は、このステップはスキップされます。**次へ**をクリックします。

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. 三角形のアイコンをクリックしてすべてのフォルダーを表示し、共有するフォルダーを選択します。 または、disk1_part1をクリックしてディスク全体を共有します。 **次へ**をクリックします。

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. 共有フォルダの設定

    セキュリティ上の理由から、**匿名アクセス**を有効にすることはお勧めしません。

    作成したユーザーは、デフォルトで**Read-Only User**に追加されます。このアカウントをファイルの書き込みや削除ができるようにしたい場合は、Read-Only Userから外し、**Writable User**に追加します。**Apply** をクリックします。

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. フォルダアクセスリンク。 WindowsとUnix系OSのリンクが表示されます。Unix系OSには、Android、iOS、macOS、Ubuntuなどがあります。それでは、様々なOSでSambaにアクセスしてみてください。 [こちら](#samba-client)チェックします。

    **注意:** **WANからのSambaアクセスを許可する** を有効にしてWANからアクセスする場合、下図のルーターIP(デフォルト192.168.8.1)をインターネット(INTERNET)ページにあるWAN IPに置き換える必要があります。

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

---

## WebDAV のセットアップ

1. オンに切り替えるとWebDAVが有効になります。その他のパラメータについては、以下を参照し、**Apply**をクリックしてください。

    * WANからのWebDAVアクセスを許可します。上位のデバイスがWebDAVにアクセスできるようにしたい場合は、これを有効にします。

    * WebDAV プロトコル、**HTTP** は暗号化されません。使用する場合はリスクを負ってください。 **HTTPS** は暗号化されており、自己署名証明書を使用します。

    * WebDAV ポートは、競合しない限り、通常は変更する必要はありません。ポート番号の範囲は 1024 ～ 65535 です。

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. 次に、共有リンクを取得するように設定しましょう。 ディスクが検出されると、**クイック セットアップ共有**のリンクが表示されます。**クイック セットアップ共有** をクリックします。

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. ユーザーを追加します。すでにアカウントをお持ちの場合は、このステップはスキップされます。**次へ**をクリックします。

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. 三角形のアイコンをクリックしてすべてのフォルダーを表示し、共有するフォルダーを選択します。 または、disk1_part1 をクリックしてディスク全体を共有します。 **次へ**をクリックします。

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. 共有フォルダの設定。

    セキュリティ上の理由から、**匿名アクセス**を有効にすることはお勧めしません。

    作成したユーザーは、デフォルトで**Read-Only User**に追加されます。このアカウントをファイルの書き込みや削除ができるようにしたい場合は、Read-Only Userから外し、**Writable User**に追加します。**Apply** をクリックします。

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. フォルダアクセスリンク。 WindowsとUnix系OSのリンクが表示されます。Unix系OSには、Android、iOS、macOS、Ubuntuなどがあります。それでは、様々なOSでSambaにアクセスしてみてください。 [こちら](#webdav-client)チェックします。

    **注意:** **WANからのSambaアクセスを許可する** を有効にしてWANからアクセスする場合、下図のルーターIP(デフォルト192.168.8.1)をインターネット(INTERNET)ページにあるWAN IPに置き換える必要があります。

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

---

## DLNAのセットアップ

DLNAを有効に切り替え、必要に応じて**共有パス**を変更し、**Apply**をクリックします。これで完了です。

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.png){class="glboxshadow"}

スマートテレビをルーターに接続すると、DLNAサーバーが見つかります。

---

## Samba クライアント

=== "Windows"

    ここでは Windows 11 の例を示しますが、Windows 10 も同様です。

    ファイルエクスプローラーを開き、**このPC**（左ペイン）を右クリックします。表示されるコンテキストメニューから、**その他のオプションを表示** -> **ネットワークの場所を追加** を選択します。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

     **カスタムネットワークの場所を選択する** をクリックし、**次へ**をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Sambaアクセスリンクを入力します。**次へ**をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    この場所の名前を付けます。**次へ**をクリックしてください。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    **完了**をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    ユーザー名とパスワードが必要な場合は、クレデンシャルの入力を求められます。その後、**OK**をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    FinderでSambaにアクセスできます。

    Finderを開き、メニューのGo -> Connect to Serverをクリックします。Sambaアクセスリンクをコピー＆ペーストし ます。

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    ユーザー名とパスワードの入力を求められますが、ユーザー名は**共有フォルダ設定**を設定したときのものです。
    
    匿名アクセスを設定した場合は、下の画像で**ゲスト**を選択してください。

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}
    
    **続行**をクリックすると、Finder のサイドバーに Samba が表示されます。

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    SambaをサポートするAndroidアプリは多数ありますが、ここでは [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}の例をご紹介します。

    ホームページで**ネットワーク**をクリックします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    **新しい場所**をクリックします。
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    **SMB**をクリックします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    **ホスト**、**ユーザー名**、**パスワード**を入力してください。**匿名アクセス**の場合は、**匿名**にチェックを入れてください。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    iOS [ファイル](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}アプリはSambaをサポートしています。あるいは、他のアプリ、例えば[Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}を使うこともできます。

    次のセクションでは、それぞれ**Files**アプリと**Documents**アプリを使用してSambaに接続する方法を説明します。

    - [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} appによるSambaサーバーへの接続ガイド。

        **Files** アプリを開きます。デフォルトでインストールされているので、ホーム画面にあるはずです。現在**Files**は取り外し可能なアプリなので、表示されない場合はApp Storeから再インストールする必要があるかもしれません。

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        画面下部の**ブラウズ**タブにいることを確認します。右上の「...」（3つの点）アイコンをタップし、アプリのコンテキストメニューを表示します。
        
        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        メニューの上部にある**Connect to Server**オプションをタップします。次の画面で、サーバーの接続URLを入力します。URLは[共有リンク](#shared-link)にあります。 右上の**次へ**ボタンをタップして次に進みます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        保護された共有ネットワークに接続する場合は、次の画面で認証情報を入力します。**登録ユーザー**をタップし、**名前**と**パスワード**フィールドにSambaのユーザー名とパスワードを入力します。**匿名アクセス**を有効にすると、代わりに "ゲスト"をタップすることができます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        右上の**次へ**ボタンを押して接続を完了します。iOSデバイスがサーバーへの接続に成功し、利用可能な共有のリストが表示されるはずです。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        Samba共有はメニューの一番下、**共有**見出しの下にリストさ れます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} appによるSambaサーバーへの接続ガイド。

        右下のプラスボタンをクリックします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        **接続の追加**をクリックします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        **Windows SMB**をクリックします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **タイトル**は、この接続の名前です。**URL**はアクセス・リンクです。**ログイン**はユーザー名です。匿名アクセスの場合は、**ログイン**と**パスワード**は空のままにしてください。

        **完了**ボタンをクリックして設定を完了します。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV クライアント

=== "Windows"

    WebDAV をサポートするソフトウェアは多数あります、例えば [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}。
    
    以下は RaiDrive の例です。

    **追加** をクリックします。

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    **Storage** エリアで、**NAS** -> **WebDAV** をクリックします。

    **Address** エリアで、Address の近くにあるチェックボックスをオン/オフして https/http を切り替え、アドレスを入力します。

    **Account** エリアで、ユーザー名とパスワードを入力するか、**匿名**にチェックを入れます。

    最後に、**接続**をクリックすると、ファイルエクスプローラーにXドライブが追加されます。

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    WebDAVに対応したアプリは多数あります、例えば [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    FEファイルエクスプローラーの例です。
    
    追加ボタンをクリックします。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    **WebDAV**を選択します。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    接続設定を入力します。 匿名アクセスの場合は、**ユーザー名** と **パスワード** を空のままにしておきます。 次に、**保存して接続** をクリックします。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    *以下のセキュアサーバー（null）は信頼できない証明書を使用しています*という警告が表示されることがありますが、これは自己署名証明書を使用しているため、信頼してください。

=== "Android"

    WebDAVをサポートするiOSアプリはたくさんありますが、ここでは [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}の例を紹介します。

    注意：Cxファイルエクスプローラーは匿名アクセスをサポートしていません。

    ホームページで**ネットワーク**をクリックします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    **新しい場所**をクリックしてください。
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    **WebDAV**をクリックします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    **ホスト**、**ポート**、**ユーザー名**、**パスワード**を入力します。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    WebDAVをサポートするiOSアプリはたくさんあるが、ここでは [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}の例を紹介します。

    右下のプラスボタンをクリックします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    **接続の追加**をクリックします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    **WebDAV Server**をクリックします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **タイトル** は、この接続の名前です。 **URL** はアクセスリンクです。 **ログイン** はユーザー名です。

    **完了**ボタンをクリックして、このセットアップを完了します。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
