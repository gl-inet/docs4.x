# ネットワークストレージ

## コンテンツ

- [はじめに](#introduction)
- [対応モデル](#supported-models)
- [ストレージデバイスを挿入する](#insert-storage-device)
- [Samba をセットアップする](#set-up-samba)
- [WebDAV をセットアップする](#set-up-webdav)
- [DLNA をセットアップする](#set-up-dlna)
- [Samba クライアント](#samba-client)
- [WebDAV クライアント](#webdav-client)

## はじめに {#introduction}

ネットワークストレージを使うと、USB ドライブや SD カードをルーターに接続して、デバイス間でワイヤレスにファイル共有できます。ルーターがストレージデバイスを共有ネットワークドライブに変換し、Wi-Fi に接続しているすべてのデバイスからアクセスできるようにします。

GL.iNet の一部モデルには MicroSD(TF) カードスロットがあり、一部のモデルには USB ポートがあります。これらのストレージデバイスに対して Samba、WebDAV、DLNA を設定でき、NTFS、FAT32、EXT4 などの一般的なフォーマットに対応しています。

!!! Note

    1. USB ハードドライブは消費電力が高いため、外部電源と一緒に使用してください。そうしないと正常に動作しない場合があります。

    2. USB ポートまたは MicroSD スロットを搭載していても、ストレージ容量の制限によりネットワークストレージに対応していないモデルがあります。

    3. Web Admin Panel では共有フォルダーのみ管理できます。ストレージデバイス上のファイルを管理するには、[モバイルアプリ](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} を使用してください。

## 対応モデル {#supported-models}

通常、USB ポートまたは MicroSD(TF) スロットを備えたモデルは、ネットワークストレージ、つまりファイル共有に対応しています。

フラッシュストレージが 32MB 以下のデバイスでは、ネットワークストレージ機能はまだサポートされていません。

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
| GL-SFT1200 (Opal)</br>***FW 4.7.2**      |   √   |   -    |  -   |     √     |       -       |
| GL-E750V2 (Mudi V2)</br>***FW 4.7.2**    |   √   |   -    |  -   |     √     |       √       |
| GL-AR750S-EXT (Slate)</br>***FW 4.7.2**  |   √   |   -    |  -   |     √     |       √       |

## ストレージデバイスを挿入する {#insert-storage-device}

TF カードを使う場合は、まずルーターの電源を切り、TF カードを挿入してから電源を入れてください。

USB Drive はそのまま USB ポートに接続できます。ポータブル外付けハードドライブを使う場合は、別電源があるなら電源にも接続してください。

ルーターの Web Admin Panel にログインし、**APPLICATIONS** -> **Network Storage** に移動します。

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

ストレージデバイスを接続すると、認識後に以下のように表示されます。

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Samba をセットアップする {#set-up-samba}

1. **Enable Samba** をオンにし、**Apply** をクリックします。

    * Allow Access Samba from WAN: 上位ネットワーク側のデバイスから Samba へアクセスさせたい場合は有効にします。

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. **Quick Setup Share** をクリックして共有リンクを設定します。

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. ユーザーを追加し、**Next** をクリックします。すでにアカウントがある場合は、この手順はスキップされます。

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. 三角アイコンをクリックしてすべてのフォルダーを表示します。共有するフォルダーを選ぶか、ディスク全体を共有したい場合はディスク名（disk1_part1）をクリックして、**Next** をクリックします。

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. 共有フォルダーを設定します。

    セキュリティ上の理由から、**Anonymous Access** を有効にすることは推奨されません。

    前の手順で作成したユーザーは、デフォルトで **Read-Only User** に追加されます。このユーザーに書き込みや削除を許可したい場合は、**Read-Only User** から削除して **Writable User** に追加し、**Apply** をクリックしてください。

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. フォルダーのアクセスリンクを取得します。

    Windows 用と Unix 系 OS 用のリンクが表示されます。Unix 系 OS には Android、iOS、macOS、Ubuntu などが含まれます。

    これらのリンクを使って Samba 経由で共有フォルダーにアクセスできます。詳細は [こちら](#samba-client) をご覧ください。

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Note:** **Allow Access Samba from WAN** を有効にして上位ネットワークから共有フォルダーへアクセスする場合は、アクセスリンク内のルーター IP（デフォルトは 192.168.8.1）を、Web admin panel の **INTERNET** ページで確認できる WAN IP に置き換えてください。

---

## WebDAV をセットアップする {#set-up-webdav}

1. **Enable WebDAV** をオンにし、**Apply** をクリックします。

    * Allow Access WebDAV from WAN: 上位ネットワーク側のデバイスから WebDAV へアクセスさせたい場合は有効にします。

    * WebDAV Protocol: **HTTP** は暗号化されません。使用は自己責任です。**HTTPS** は暗号化され、自己署名証明書を使用します。

    * WebDAV Port: ポート番号は競合がない限り変更不要です。推奨ポート範囲は 1024 - 65535 です。

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. **Quick Setup Share** をクリックして共有リンクを設定します。

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. ユーザーを追加し、**Next** をクリックします。すでにアカウントがある場合は、この手順はスキップされます。

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. 三角アイコンをクリックしてすべてのフォルダーを表示します。共有するフォルダーを選ぶか、ディスク全体を共有したい場合はディスク名（disk1_part1）をクリックして、**Next** をクリックします。

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. 共有フォルダーを設定します。

    セキュリティ上の理由から、**Anonymous Access** を有効にすることは推奨されません。

    前の手順で作成したユーザーは、デフォルトで **Read-Only User** に追加されます。このユーザーに書き込みや削除を許可したい場合は、**Read-Only User** から削除して **Writable User** に追加し、**Apply** をクリックしてください。

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. フォルダーのアクセスリンクを取得します。

    Windows 用と Unix 系 OS 用のリンクが表示されます。Unix 系 OS には Android、iOS、macOS、Ubuntu などが含まれます。

    これらのリンクを使って WebDAV 経由で共有フォルダーにアクセスできます。詳細は [こちら](#webdav-client) をご覧ください。

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Note:** **Allow Access WebDAV from WAN** を有効にして上位ネットワークから共有フォルダーへアクセスする場合は、アクセスリンク内のルーター IP（デフォルトは 192.168.8.1）を、Web admin panel の **INTERNET** ページで確認できる WAN IP に置き換えてください。

---

## DLNA をセットアップする {#set-up-dlna}

**Enable DLNA** をオンにし、**Apply** をクリックします。

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

スマート TV をルーターに接続すると、DLNA サーバーが検出されます。

---

## Samba クライアント {#samba-client}

=== "Windows"

    ここでは Windows 11 を例に説明します。Windows 10 でも同様です。

    File Explorer を開き、左ペインの **This PC** を右クリックします。表示されたコンテキストメニューから **Show more options** -> **Add a network location** を選択します。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    **Choose a custom network location** をクリックして、**Next** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Samba のアクセスリンクを入力し、**Next** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    この場所の名前を入力し、**Next** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    **Finish** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    ユーザー名とパスワードが必要な場合は、認証情報の入力を求められます。入力後、**OK** をクリックします。

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Samba には Finder からアクセスできます。

    Finder を開き、メニューの Go -> Connect to Server をクリックして、Samba のアクセスリンクを貼り付けます。

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    ユーザー名とパスワードの入力を求められます。ユーザー名は **Shared Folder Settings** の設定時に指定したものです。

    匿名アクセスを設定している場合は、下の画面で **Guest** を選択してください。

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    **Continue** をクリックすると、Finder のサイドバーに Samba が表示されます。

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Samba に対応した Android アプリは多数あります。ここでは [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"} を例に説明します。

    ホーム画面で **NETWORK** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    **New Location** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    **SMB** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    **Host**、**Username**、**Password** を入力します。**Anonymous Access** の場合は **Anonymous** にチェックを入れてください。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    iOS の [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} アプリは Samba に対応しています。ほかにも、たとえば [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} を利用できます。

    以下では、**Files** アプリと **Documents** アプリで Samba サーバーに接続する方法を説明します。

    - [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} アプリで Samba サーバーに接続する方法。

        **Files** アプリを開きます。標準でインストールされていますが、**Files** は削除可能なアプリのため、表示されない場合は App Store から再インストールしてください。

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width="300"}

        画面下部の **Browse** タブを開いていることを確認し、右上の「...」（3 点）アイコンをタップしてメニューを表示します。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width="560"}

        メニュー上部の **Connect to Server** をタップします。次の画面でサーバーの接続 URL を入力します。URL は共有リンクで確認できます。右上の **Next** をタップします。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width="560"}

        保護されたネットワーク共有へ接続する場合は、認証情報を入力します。**Registered User** をタップし、Samba のユーザー名とパスワードを入力してください。**Anonymous Access** を有効にしている場合は **Guest** を選択できます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width="560"}

        右上の **Next** をタップすると接続が完了します。iOS デバイスがサーバーに接続され、利用可能な共有の一覧が表示されます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width="560"}

        Samba 共有は、メニュー下部の **Shared** の下に表示されます。

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width="560"}

    - [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} アプリで Samba サーバーに接続する方法。

        右下のプラスボタンをタップします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        **Add Connection** をタップします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        **Windows SMB** をタップします。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** は接続名、**URL** はアクセスリンク、**Login** はユーザー名です。匿名アクセスの場合は **Login** と **Password** を空欄のままにしてください。

        **Done** をタップして設定を完了します。

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV クライアント {#webdav-client}

=== "Windows"

    WebDAV に対応したソフトウェアは多数あります。たとえば [RaiDrive](https://www.raidrive.com/){target="_blank"}、[Cyberduck](https://cyberduck.io/download/){target="_blank"}、[WinSCP](https://winscp.net/eng/index.php){target="_blank"} などがあります。

    ここでは RaiDrive を例に説明します。

    **Add** をクリックします。

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    **Storage** エリアで **NAS** -> **WebDAV** を選択します。

    **Address** エリアでは、Address の横にあるチェックボックスで https/http を切り替えて、アドレスを入力します。

    **Account** エリアでは、ユーザー名とパスワードを入力するか、**Anonymous** をチェックします。

    最後に **Connect** をクリックすると、File Explorer に X ドライブが追加されます。

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    WebDAV に対応したアプリは多数あります。たとえば [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} や [Cyberduck](https://cyberduck.io/download/){target="_blank"} などがあります。

    ここでは FE File Explorer を例に説明します。

    Add ボタンをクリックします。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    **WebDAV** を選択します。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    接続設定を入力します。匿名アクセスの場合は **User Name** と **Password** を空欄のままにして、**Save & Connect** をクリックします。

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    *The following secure server (null) uses an untrusted certificate. Trust this server?* という警告が表示される場合があります。これは自己署名証明書を使用しているためです。信頼して続行してください。

=== "Android"

    WebDAV に対応した Android アプリは多数あります。ここでは [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"} を例に説明します。

    Note: Cx File Explorer は匿名アクセスに対応していません。

    ホーム画面で **NETWORK** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    **New Location** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    **WebDAV** をタップします。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    **Host**、**Port**、**Username**、**Password** を入力します。

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    WebDAV に対応した iOS アプリは多数あります。ここでは [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} を例に説明します。

    右下のプラスボタンをタップします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    **Add Connection** をタップします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    **WebDAV Server** をタップします。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** は接続名、**URL** はアクセスリンク、**Login** はユーザー名です。

    **Done** をタップして設定を完了します。

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## モバイルアプリを使う

Web Admin Panel では共有フォルダーのみ管理できます。ストレージデバイス上のファイルを管理するには、[モバイルアプリ](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} を使用してください。

- **ローカルネットワーク** 経由でアプリにアクセスすると、ストレージデバイスとその容量が表示され、読み書きに対応します。

- **クラウド** 経由でアプリにアクセスすると、ストレージデバイスとその容量は表示されますが、読み書きには対応しません。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
