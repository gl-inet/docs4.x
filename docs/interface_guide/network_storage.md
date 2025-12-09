# Network Storage

## Contents

- [Introduction](#introduction)
- [Supported models](#supported-models)
- [Insert storage device](#insert-storage-device)
- [Set up Samba](#set-up-samba)
- [Set up WebDAV](#set-up-webdav)
- [Set up DLNA](#set-up-dlna)
- [Samba Client](#samba-client)
- [WebDAV Client](#webdav-client)

## Introduction

Network storage enables wireless file sharing across devices by connecting a USB drive or SD card to your router. The router converts the storage device into a shared network drive, accessible to all Wi-Fi-connected devices.

Some GL.iNet models have MicroSD(TF) card slots, while some models have USB ports, supporting USB flash drives and portable external hard drives. You can configure Samba, WebDAV, DLNA for these storage devices, which support common formats such as NTFS, FAT32, and EXT4.

!!! Note 

    1. The power consumption of a USB hard drive is quite high. Use it with an external power supply, otherwise it may cause malfunction.

    2. Some models have a USB port or MicroSD slot but have limited storage space and do not support network storage.

## Supported models

Usually, models with USB ports or MicroSD(TF) slots support network storage (i.e. file sharing). 

For devices with flash storage of 32MB or less, the Network Storage function is not yet supported.

| Router Model                           | Samba | Webdav | DLNA | USB Port | MicroSD Card |
| :------------------------------------- | :---: | :---: | :---: | :------: | :----------: |
| GL-BE3600 (Slate 7)                    | √     | √     | √     | √        | -            |
| GL-X2000 (Spitz Plus)                  | √     | √     | √     | √        | -            |
| GL-MT6000 (Flint 2)                    | √     | √     | √     | √        | -            |
| GL-XE3000 (Puli AX)                    | √     | √     | √     | √        | √            |
| GL-X3000 (Spitz AX)                    | √     | √     | √     | √        | √            |
| GL-MT3000 (Beryl AX)                   | √     | √     | √     | √        | -            |
| GL-MT2500/GL-MT2500A (Brume 2)         | √     | √     | √     | √        | -            |
| GL-AXT1800 (Slate AX)                  | √     | √     | √     | √        | √            |
| GL-AX1800 (Flint)                      | √     | √     | √     | √        | -            |
| GL-A1300 (Slate Plus)                  | √     | √     | √     | √        | -            |
| GL-S1300 (Convexa-S)                   | √     | √     | √     | √        | -            |
| GL-SFT1200 (Opal)</br>***FW 4.7.2**    | √     | -     | -     | √        | -            |
| GL-E750V2 (Mudi V2)</br>***FW 4.7.2**  | √     | -     | -     | √        | √            |
| GL-AR750S-EXT (Slate)</br>***FW 4.7.2**| √     | -     | -     | √        | √            |

## Insert Storage Device

For TF card, you need to power off the router first, insert the TF card and then power on the router.

For USB Drive, you can directly plug it into the USB port. For portable external hard drive, if you have a separate power supply, please connect it to the power supply.

Log in to the router's web Admin Panel, navigate to APPLICATIONS -> Network Storage.

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

Connect the storage device. When it is detected, the page is displayed as below.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Set Up Samba

1. Toggle on **Enable Samba** and click **Apply**.

    * Allow Access Samba from WAN: Enable it if you want the upstream devices to access Samba.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. Click **Quick Setup Share** to set the shared link.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. Add a user and click **Next**. This step will be skipped if you already have an account. 

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Click the triangle icon to show all folders. Select a folder for sharing, or click the disk name (disk1_part1) if you want to share the whole disk. Then click **Next**.

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Set up the shared folder.

    For security reasons, it is not recommended to enable **Anonymous Access**.

    The user created in the previous step will be added to **Read-Only User** by default. If you want this user to be able to write or delete files, remove it from Read-Only User and add it to **Writable User**, and click **Apply**.

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Obtain the folder access link. 

    The page will show the link for Windows and Unix-like OS. The Unix-like system includes Android, iOS, macOS, Ubuntu, etc. 
    
    Now you can access your shared folder over Samba service via these links. Click [here](#samba-client) for details.

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Note:** If you enable **Allow Access Samba from WAN** and access the shared folder from upper network, please replace the router IP (default 192.168.8.1) in the access link with your router's WAN IP, which can be found on the INTERNET page of the web admin panel.

---

## Set Up WebDAV

1. Toggle on **Enable WebDAV**, and click **Apply**.

    * Allow Access WebDAV from WAN: Enable it if you want the upstream devices to access WebDAV.

    * WebDAV Protocol: **HTTP** is not encrypted; use it at your own risk. **HTTPS** is encrypted and it uses self-signed certificate.

    * WebDAV Port: No need to modify the port number unless there’s a conflict. The recommended port number range is 1024 - 65535.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. Click **Quick Setup Share** to set the shared link.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. Add a user and click **Next**. This step will be skipped if you already have an account.

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Click the triangel icon to show all folders. Select a folder for sharing, or click the disk name (disk1_part1) to share the whole disk. Then click **Next**.

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Set up the shared folder.

    For security reasons, it is not recommended to enable **Anonymous Access**.

    The user created in the previous step will be added to **Read-Only User** by default. If you want this user to be able to write or delete files, remove it from Read-Only User and add it to **Writable User**, and click **Apply**.

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Obtain folder access link. 

    The page will show the link for Windows and Unix-like OS. The Unix-like system includes Android, iOS, macOS, Ubuntu, etc. 
    
    Now you can access your shared folder over WebDAV service via these links. Click [here](#webdav-client) for details.

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Note:** If you enabled **Allow Access WebDAV from WAN** and access the shared folder from upper network, please replace the router IP (default 192.168.8.1) in the access link with your router's WAN IP, which can be found on the INTERNET page of the web admin panel.

---

## Set Up DLNA

Toggle on **Enable DLNA**, and click **Apply**.

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

Connect your smart TV to the router, and it will find the DLNA Server.

---

## Samba Client

=== "Windows"

    Here is an example of Windows 11, which also applies to Windows 10.

    Open up File Explorer and then right-click on **This PC** (in the left pane). From the resulting context menu, select **Show more options** -> **Add a network location**

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Click **Choose a custom network location** and then click **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Enter the Samba access link. Then click **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Give a name of this location. Click **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Click **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    If it need username and password, it will ask to enter the credential. Then click **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    You can access Samba by the Finder.

    Open up the Finder and click Go -> Connect to Server on the menu. Copy & paste the Samba access link.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    It will ask for the username and password, the username is when you setup **Shared Folder Settings**.
    
    If you set up anonymous access, please choose **Guest** in the image below.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Click **Continue**, it will show the Samba on the sidebar of Finder.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    There are many Android apps that support Samba, here is an example of [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    At the home page, click **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Click **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Click **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Input the **Host**, **Username**, **Password**. If is **Anonymous Access**, please check the **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    iOS [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} app support Samba, or you can use other apps, for example [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    The next section describes how to connect to Samba using **Files** app and **Documents** app respectively.

    - Guide of connect to Samba server by [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} app.

        Open the **Files** app. It's installed by default so you should find it on your home screen. As **Files** is now a removable app, you might need to reinstall it from the App Store if it doesn't show up.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        Make sure you're on the **Browse** tab at the bottom of the screen. Tap the "…" (three dots) icon in the top-right to display the app's context menu.
        
        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        Tap the **Connect to Server** option near the top of the menu. On the next screen, enter your server's connection url. You can find the url in [Shared Link](#shared-link). Tap the **Next** button in the top-right to continue.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        The following screen lets you enter authentication credentials if you'll be connecting to a protected network share. Tap **Registered User** and fill out the **Name** and **Password** fields with your Samba username and password. You can tap "Guest" instead if you enable the **Anonymous Access**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        Press the **Next** button in the top-right to complete the connection. Your iOS device should successfully connect to the server and display a list of available shares.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        The Samba share will be listed at the bottom of menu, underneath the **Shared** heading.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - Guide of connect to Samba server by [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} app.

        Click the plus button in the lower right corner.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Click **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Click **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        The **Title** is for a name of this connection. **URL** is the access link. **Login** is the username. If is anonymous access, just leave **Login** and **Password** empty.

        Click **Done** button to complete this setup.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV Client

=== "Windows"

    There is a lot of software that supports WebDAV, for example [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.
    
    Here is an example of RaiDrive.

    Click **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    In the **Storage** area, click **NAS** -> **WebDAV**.

    In the **Address** area, check/uncheck the checkbox near Address to switch https/http, enter the address.

    In the **Account** area, enter username and password, or check the **Anonymous**.

    Finally, click **Connect**, it will add a X drive in the File Explorer.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    There is a lot of app that supports WebDAV, for example [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Here is an example of FE File Explorer.

    Click Add button.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Select **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Enter connection settings. If is anonymous access, just leave **User Name** and **Password** empty. Then clidk **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    It may has a warning says *The following secure server (null) uses an untrusted certificate. Trust this server?*, that is because it use self signed certificate, please trust it.

=== "Android"

    There are many iOS apps that support WebDAV, here is an example of [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Note: Cx File Explorer doesn't support anonymous access.

    At the home page, click **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Click **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Click **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Input the **Host**, **Port**, **Username**, **Password**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    There are many iOS apps that support WebDAV, here is an example of [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Click the plus button in the lower right corner.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Click **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Click **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    The **Title** is for a name of this connection. **URL** is the access link. **Login** is the username.

    Click **Done** button to complete this setup.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
