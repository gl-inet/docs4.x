# ネットワークストレージ

## コンテンツ

- [はじめに](#introduction)
- [対応モデル](#supported-models)
- [ストレージデバイスの挿入](#insert-storage-device)
- [Sambaをセットアップする](#set-up-samba)
- [WebDAVをセットアップする](#set-up-webdav)
- [DLNAをセットアップする](#set-up-dlna)
- [Sambaクライアント](#samba-client)
- [WebDAVクライアント](#webdav-client)

## はじめに

USBドライブまたはSDカードをルーターに接続することで、デバイス間でワイヤレスにファイルを共有できます。ルーターはストレージデバイスを共有ネットワークドライブとして扱い、Wi-Fiに接続されたすべてのデバイスからアクセスできるようにします。

GL.iNetの一部モデルにはMicroSD（TF）カードスロットがあり、一部モデルにはUSBポートがあります。これらのストレージデバイスに対して、Samba、WebDAV、DLNAを設定できます。NTFS、FAT32、EXT4などの一般的なフォーマットに対応しています。

!!! 注意

    1. USBハードドライブは消費電力が大きいため、外部電源と併用してください。そうしないと、正常に動作しない場合があります。

    2. 一部のモデルにはUSBポートまたはMicroSDスロットがありますが、内蔵ストレージ容量の制限により、ネットワークストレージに対応していません。

    3. Web管理パネルでは共有フォルダーのみ管理できます。ストレージデバイス上のファイルを管理するには、[モバイルアプリ](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}を使用してください。

## 対応モデル

通常、USBポートまたはMicroSD（TF）スロットを搭載したモデルは、ネットワークストレージ、つまりファイル共有に対応しています。

フラッシュストレージが32MB以下のデバイスでは、ネットワークストレージ機能はまだサポートされていません。

| ルーターモデル                           | Samba | WebDAV | DLNA | USBポート | MicroSDカード |
| :--------------------------------------- | :---: | :----: | :--: | :-------: | :-----------: |
| GL-E5800 (Mudi 7)                        |   √   |   √    |  √   |     √     |       -       |
| GL-MT5000 (Brume 3)                      |   √   |   √    |  √   |     √     |       -       |
| GL-BE3600 (Slate 7)                      |   √   |   √    |  √   |     √     |       -       |
| GL-X2000 (Spitz Plus)                    |   √   |   √    |  √   |     √     |       -       |
| GL-MT6000 (Flint 2)                      |   √   |   √    |  √   |     √     |       -       |
| GL-XE3000 (Puli AX)                      |   √   |   √    |  √   |     √     |       √       |
| GL-X3000 (Spitz AX)                      |   √   |   √    |  √   |     √     |       √       |
| GL-MT3000 (Beryl AX)                     |   √   |   √    |  √   |     √     |       -       |
| GL-MT2500/GL-MT2500A (Brume 2)           |   √   |   √    |  √   |     √     |       -       |
| GL-AXT1800 (Slate AX)                    |   √   |   √    |  √   |     √     |       √       |
| GL-AX1800 (Flint)                        |   √   |   √    |  √   |     √     |       -       |
| GL-A1300 (Slate Plus)                    |   √   |   √    |  √   |     √     |       -       |
| GL-S1300 (Convexa-S)                     |   √   |   √    |  √   |     √     |       -       |
| GL-SFT1200 (Opal)</br>**\*FW 4.7.2**     |   √   |   -    |  -   |     √     |       -       |
| GL-E750V2 (Mudi V2)</br>**\*FW 4.7.2**   |   √   |   -    |  -   |     √     |       √       |
| GL-AR750S-EXT (Slate)</br>**\*FW 4.7.2** |   √   |   -    |  -   |     √     |       √       |

## ストレージデバイスの挿入

TFカードを使用する場合は、まずルーターの電源を切り、TFカードを挿入してから電源を入れてください。

USBドライブは、そのままUSBポートに接続できます。ポータブル外付けハードドライブを使用する場合は、別電源があるならそちらにも接続してください。

ルーターのWeb管理パネルにログインし、**アプリケーション** -> **ネットワークストレージ** に移動します。

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

ストレージデバイスを接続すると、認識後に以下のように表示されます。

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Sambaをセットアップする {#set-up-samba}

1. **Enable Samba** をオンにし、**Apply** をクリックします。
   - **Allow Access Samba from WAN**: 上位ネットワーク側のデバイスからSambaにアクセスさせたい場合は有効にします。

   ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. **Quick Setup Share** をクリックして共有リンクを設定します。

   ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. ユーザーを追加し、**Next** をクリックします。すでにアカウントがある場合、この手順はスキップされます。

   ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. 三角アイコンをクリックしてすべてのフォルダーを表示します。共有するフォルダーを選択するか、ディスク全体を共有したい場合はディスク名（disk1_part1）をクリックし、**Next** をクリックします。

   ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. 共有フォルダーを設定します。

   セキュリティ上、**Anonymous Access** を有効にすることは推奨しません。

   前の手順で作成したユーザーは、デフォルトで **Read-Only User** に追加されます。このユーザーに書き込みや削除を許可したい場合は、**Read-Only User** から外し、**Writable User** に追加して **Apply** をクリックしてください。

   ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. フォルダーのアクセスリンクを取得します。

   Windows用とUnix系OS用のリンクが表示されます。Unix系OSにはAndroid、iOS、macOS、Ubuntuなどが含まれます。

   これらのリンクを使ってSamba経由で共有フォルダーにアクセスできます。詳細は[こちら](#samba-client)をご覧ください。

   ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

   **注意:** **Allow Access Samba from WAN** を有効にして上位ネットワークから共有フォルダーにアクセスする場合は、アクセスリンク内のルーターIP（デフォルトは192.168.8.1）を、Web管理パネルの **INTERNET** ページで確認できるWAN IPに置き換えてください。

---

## WebDAVをセットアップする {#set-up-webdav}

1. **Enable WebDAV** をオンにし、**Apply** をクリックします。
   - **Allow Access WebDAV from WAN**: 上位ネットワーク側のデバイスからWebDAVにアクセスさせたい場合は有効にします。

   - **WebDAV Protocol**: **HTTP** は暗号化されません。使用は自己責任です。**HTTPS** は暗号化されますが、自己署名証明書を使用します。

   - **WebDAV Port**: ポート競合がない限り変更は不要です。推奨ポート範囲は1024〜65535です。

   ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. **Quick Setup Share** をクリックして共有リンクを設定します。

   ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. ユーザーを追加し、**Next** をクリックします。すでにアカウントがある場合、この手順はスキップされます。

   ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. 三角アイコンをクリックしてすべてのフォルダーを表示します。共有するフォルダーを選択するか、ディスク全体を共有したい場合はディスク名（disk1_part1）をクリックし、**Next** をクリックします。

   ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. 共有フォルダーを設定します。

   セキュリティ上、**Anonymous Access** を有効にすることは推奨しません。

   前の手順で作成したユーザーは、デフォルトで **Read-Only User** に追加されます。このユーザーに書き込みや削除を許可したい場合は、**Read-Only User** から外し、**Writable User** に追加して **Apply** をクリックしてください。

   ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. フォルダーのアクセスリンクを取得します。

   Windows用とUnix系OS用のリンクが表示されます。Unix系OSにはAndroid、iOS、macOS、Ubuntuなどが含まれます。

   これらのリンクを使ってWebDAV経由で共有フォルダーにアクセスできます。詳細は[こちら](#webdav-client)をご覧ください。

   ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

   **注意:** **Allow Access WebDAV from WAN** を有効にして上位ネットワークから共有フォルダーにアクセスする場合は、アクセスリンク内のルーターIP（デフォルトは192.168.8.1）を、Web管理パネルの **INTERNET** ページで確認できるWAN IPに置き換えてください。

---

## DLNAをセットアップする {#set-up-dlna}

**Enable DLNA** をオンにし、**Apply** をクリックします。

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

スマートTVをルーターに接続すると、DLNAサーバーが検出されます。

---

## Sambaクライアント

=== "Windows"

    ここではWindows 11を例に説明しますが、Windows 10でも同様です。

    エクスプローラーを開き、左ペインの **This PC** を右クリックします。表示されたコンテキストメニューから **Show more options** -> **Add a network location** を選択します。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    **Choose a custom network location** をクリックし、**Next** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Sambaのアクセスリンクを入力し、**Next** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    この場所の名前を入力し、**Next** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    **Finish** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    ユーザー名とパスワードが必要な場合は、認証情報の入力を求められます。入力後、**OK** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    SambaにはFinderからアクセスできます。

    Finderを開き、メニューの **Go** -> **Connect to Server** をクリックして、Sambaのアクセスリンクを貼り付けます。

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    ユーザー名とパスワードの入力を求められます。ユーザー名は **Shared Folder Settings** で設定したものです。

    匿名アクセスを設定している場合は、下の画面で **Guest** を選択してください。

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    **Continue** をクリックすると、FinderのサイドバーにSambaが表示されます。

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Sambaに対応したAndroidアプリは多数あります。ここでは [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"} を例にします。

    ホーム画面で **NETWORK** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    **New Location** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    **SMB** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    **Host**、**Username**、**Password** を入力します。匿名アクセスの場合は **Anonymous** にチェックを入れてください。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    iOSの[Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}アプリはSambaに対応しています。ほかにも、[Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} などのアプリを利用できます。

    以下では、**Files** アプリと **Documents** アプリでSambaサーバーに接続する方法を説明します。

    - [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} アプリでSambaサーバーに接続する方法。

        **Files** アプリを開きます。通常は標準でインストールされています。**Files** は削除可能なアプリのため、表示されない場合はApp Storeから再インストールしてください。

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        画面下部の **Browse** タブを開き、右上の「...」アイコンをタップしてメニューを表示します。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        **Connect to Server** をタップします。次の画面でサーバーの接続URLを入力します。URLは共有リンクで確認できます。右上の **Next** をタップします。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        保護されたネットワーク共有に接続する場合は、認証情報を入力します。**Registered User** を選び、Sambaのユーザー名とパスワードを入力してください。匿名アクセスを有効にしている場合は **Guest** を選択できます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        右上の **Next** をタップすると接続が完了します。iOSデバイスがサーバーに接続され、利用可能な共有の一覧が表示されます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        Samba共有は、メニュー下部の **Shared** の下に表示されます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} アプリでSambaサーバーに接続する方法。

        右下のプラスボタンをタップします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        **Add Connection** をタップします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        **Windows SMB** をタップします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** は接続名、**URL** はアクセスリンク、**Login** はユーザー名です。匿名アクセスの場合は **Login** と **Password** を空欄のままにします。

        **Done** をタップして設定を完了します。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAVクライアント

=== "Windows"

    WebDAVに対応したソフトウェアは多数あります。例えば [RaiDrive](https://www.raidrive.com/){target="_blank"}、[Cyberduck](https://cyberduck.io/download/){target="_blank"}、[WinSCP](https://winscp.net/eng/index.php){target="_blank"} などがあります。

    ここではRaiDriveを例に説明します。

    **Add** をクリックします。

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    **Storage** エリアで **NAS** -> **WebDAV** を選択します。

    **Address** エリアでは、Address横のチェックボックスで https/http を切り替え、アドレスを入力します。

    **Account** エリアでは、ユーザー名とパスワードを入力するか、**Anonymous** をチェックします。

    最後に **Connect** をクリックすると、エクスプローラーにXドライブが追加されます。

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    WebDAVに対応したアプリは多数あります。例えば [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} や [Cyberduck](https://cyberduck.io/download/){target="_blank"} などがあります。

    ここではFE File Explorerを例に説明します。

    Addボタンをクリックします。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    **WebDAV** を選択します。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    接続設定を入力します。匿名アクセスの場合は **User Name** と **Password** を空欄のままにしてください。その後、**Save & Connect** をクリックします。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    *The following secure server (null) uses an untrusted certificate. Trust this server?* という警告が表示される場合があります。これは自己署名証明書を使用しているためです。問題なければ信頼してください。

=== "Android"

    WebDAVに対応したAndroidアプリは多数あります。ここでは [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"} を例にします。

    注意: Cx File Explorerは匿名アクセスに対応していません。

    ホーム画面で **NETWORK** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    **New Location** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    **WebDAV** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    **Host**、**Port**、**Username**、**Password** を入力します。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    WebDAVに対応したiOSアプリは多数あります。ここでは [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} を例にします。

    右下のプラスボタンをタップします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    **Add Connection** をタップします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    **WebDAV Server** をタップします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** は接続名、**URL** はアクセスリンク、**Login** はユーザー名です。

    **Done** をタップして設定を完了します。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## モバイルアプリの使い方

Web管理パネルでは共有フォルダーのみ管理できます。ストレージデバイス上のファイルを管理するには、[モバイルアプリ](https://www.gl-inet.com/app/#download-app-glinet){target="\_blank"}を使用してください。

- **ローカルネットワーク**経由でアプリにアクセスすると、ストレージデバイスとその容量が表示され、読み書きが可能です。

- **クラウド**経由でアプリにアクセスすると、ストレージデバイスとその容量は表示されますが、読み書きはできません。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご利用ください。
