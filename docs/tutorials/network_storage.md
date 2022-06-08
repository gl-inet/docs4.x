# Network Storage

Some GL.iNet models support TF card, some models have USB port and support USB flash drive and portable external hard drive, you can set up Samba, WebDAV, DLNA on this page for the disk.

The supported disk formats are NTFS, exFAT, FAT32, Ext3, Ext4.

## Setup

For TF card, you need to power off the router first, insert the TF card and then power on the router.

For USB Drive, you can directly plug it into the USB port. For portable external hard drive, if you have a separate power supply, please connect it to the power supply.

Go to web Admin Panel -> APPLICATIONS -> Network Storage

![network storage](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

When a disk is found.

![network storage, disk found](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

=== "Samba"

    Toggle to enalbe Samba, click **Apply**.

    ![network storage, enable samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_to_enable.png){class="glboxshadow"}

    Go to **Shared Folder** tab. Click **+ Add** button to add a shared folder.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_shared_folders.png){class="glboxshadow"}

    Choose a folder to share, then click **Next**.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_add_shared_folder.png){class="glboxshadow"}

    For security reasons, we do not recommend enabling **Anonymous Access**.

    If you leave the **Anonymous Access** off, you need to create a user by clicking the **+ Add User** button or choose an existing user, and then check the user in the option **Writable User** or **Read-Only User**. The User is for the connection to the Samba Server. You can manage the user in the **User Management** tab.
    
    Finally, click the **Apply** button.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_shared_folder_settings.png){class="glboxshadow"}

    That is it. The access link can be found in **Shared Link**.

    ![network storage, shared link](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_shared_link.png){class="glboxshadow"}

    Click **Shared Link**, it will show the access link for each system. The Unix-like system include Android, iOS, macOS, Ubuntu etc.

    **Note:** If you enabled **Allow Access Samba from WAN** and access from WAN, you need to replace the Router IP (default 192.168.8.1) in the figure below with WAN IP which can be found in the INTERNET page.

    ![network storage, folder access link](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_folder_access_link.png){class="glboxshadow"}
    
    Then try to access the Samba on various OS, check out [here](#samba-client).

=== "WebDAV"

    Toggle to enalbe WebDAV.

    For the protocol, **HTTP** is not encrypted, using on your risk; **HTTPS** is encrypted, it uses self signed certificate.
    
    Then click **Apply**.

    ![network storage, enable webdav](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/webdav/enable_webdav.png){class="glboxshadow"}

    Go to **Shared Folder** tab. Click **+ Add** button to add a shared folder.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_shared_folders.png){class="glboxshadow"}

    Choose a folder to share, then click **Next**.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/samba/samba_add_shared_folder.png){class="glboxshadow"}

    Select the **Share Protocol** as **WebDAV**.

    For security reasons, we do not recommend enabling **Anonymous Access**.

    If you leave the **Anonymous Access** off, you need to create a user by clicking the **+ Add User** button or choose an existing user, and then check the user in the option **Writable User** or **Read-Only User**. The User is for the connection to the WebDAV Server. You can manage the user in the **User Management** tab.

    Finally, click the **Apply** button.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/webdav/webdav_shared_folder_settings.png){class="glboxshadow"}

    That is it. The access link can be found in **Shared Link**.

    ![network storage, shared link](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/webdav/webdav_share_link.png){class="glboxshadow"}

    Click **Shared Link**, it will show the access link for each system. The Unix-like system include Android, iOS, macOS, Ubuntu etc.

    **Note:** If you enabled **Allow Access Samba from WAN** and access from WAN, you need to replace the Router IP (default 192.168.8.1) in the figure below with WAN IP which can be found in the INTERNET page.

    ![network storage, folder access link](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/webdav/webdav_folder_access_link.png){class="glboxshadow"}

    Then try to access the WebDAV on various OS, check out [here](#webdav-client).

=== "DLNA"

    Toggle to enalbe DLNA, modify **Share Path** if needed, click **Apply**. That is it.

    ![network storage, enable dlna](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/enable_dlna.png){class="glboxshadow"}

    Connect your smart TV to the router, it will find the DLNA Server.

## Samba Client

=== "Windows"

    Here is an example of Windows 11, Windows 10 is similar.

    Open up File Explorer and then right-click on **This PC** (in the left pane). From the resulting context menu, select **Show more options** -> **Add a network location**

    ![windows 11 add network location](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/windows11_add_network_location.png){class="glboxshadow"}

    Click **Choose a custom network location** and then click **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/windows11_add_network_location_2.png){class="glboxshadow"}

    Enter the Samba access link. Then click **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/windows11_add_network_location_3.png){class="glboxshadow"}

    Give a name of this location. Click **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/windows11_add_network_location_4.png){class="glboxshadow"}

    Click **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/windows11_add_network_location_5.png){class="glboxshadow"}

    If it need username and password, it will ask to enter the credential. Then click **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/windows11_add_network_location_6.png){class="glboxshadow"}

=== "Mac OS"

    You can access Samba by the Finder.

    Open up the Finder and click Go -> Connect to Server on the menu. Copy & paste the Samba access link.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/finder_connect_to_server.png){class="glboxshadow"}

    It will ask for the username and password, the username is when you setup **Shared Folder Settings**.
    
    If you set up anonymous access, please choose **Guest** in the image below.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/finder_username_password.png){class="glboxshadow"}

    Click **Continue**, it will show the Samba on the sidebar of Finder.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    There are many Android apps that support Samba, here is an example of [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    At the home page, click **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Click **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Click **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Input the **Host**, **Username**, **Password**. If is **Anonymous Access**, please check the **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    There are many iOS apps that support Samba, here is an example of [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}. 
    
    **Note:** Documents doesn't support anonymous access.

    Click the plus button in the lower right corner.

    ![documents samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_1.png){class="glboxshadow" width="560"}

    Click **Add Connection**.

    ![documents samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_2.png){class="glboxshadow" width="560"}

    Click **Windows SMB**.

    ![documents samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_3.png){class="glboxshadow" width="560"}

    The **Title** is for a name of this connection. **URL** is the access link. **Login** is the username.

    Click **Done** button to complete this setup.

    ![documents samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV Client

=== "Windows"

    There is a lot of software that supports WebDAV, for example [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.
    
    Here is an example of RaiDrive.

    Click **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/raidrive_add.png){class="glboxshadow"}

    In the **Storage** area, click **NAS** -> **WebDAV**.

    In the **Address** area, check/uncheck the checkbox near Address to switch https/http, enter the address.

    In the **Account** area, enter username and password, or check the **Anonymous**.

    Finally, click **Connect**, it will add a X drive in the File Explorer.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    There is a lot of app that supports WebDAV, for example [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Here is an example of FE File Explorer.

    Click Add button.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/fe_file_explorer_add.png){class="glboxshadow"}

    Select **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/fe_file_explorer_webdav.png){class="glboxshadow"}

    Enter connection settings. If is anonymous access, just leave **User Name** and **Password** empty. Then clidk **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    It may has a warning says *The following secure server (null) uses an untrusted certificate. Trust this server?*, that is because it use self signed certificate, please trust it.

=== "Android"

    There are many iOS apps that support WebDAV, here is an example of [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    At the home page, click **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Click **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Click **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Input the **Host**, **Username**, **Password**. If is **Anonymous Access**, please check the **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    There are many iOS apps that support WebDAV, here is an example of [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.
    
    **Note:** Documents doesn't support anonymous access.

    Click the plus button in the lower right corner.

    ![documents WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_1.png){class="glboxshadow" width="560"}

    Click **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_2.png){class="glboxshadow" width="560"}

    Click **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_3.png){class="glboxshadow" width="560"}

    The **Title** is for a name of this connection. **URL** is the access link. **Login** is the username.

    Click **Done** button to complete this setup.

    ![documents WebDAV](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_4_webdav.png){class="glboxshadow" width="560"}
