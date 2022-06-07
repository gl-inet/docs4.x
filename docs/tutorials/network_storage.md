# Network Storage

Some GL.iNet models support TF card, some models have USB port and support USB flash drive and portable external hard drive, you can set up Samba, WebDav, DLNA on this page for the disk.

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

    ![network storage, enable samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/enable_samba.png){class="glboxshadow"}

    Go to **Shared Folder** tab. Click **Add** button to add a shared folder.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/shared_folders.png){class="glboxshadow"}

    Choose a folder to share, then click **Next**.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/add_shared_folder.png){class="glboxshadow"}

    For security reasons, we do not recommend enabling **Anonymous Access**.

    If you leave the **Anonymous Access** off, you need to create a user by clicking the **+ Add User** button or choose an existing user, and then check the user in the option **Writable User** or **Read-Only User**. The User is for connecting to the Samba. You can manage the user in the **User Management** tab. 
    
    Finally, click the **Apply** button.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/shared_folder_settings.png){class="glboxshadow"}

    That is it. The access link can be found in **Shared Link**.

    ![network storage, shared link](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/shared_link.png){class="glboxshadow"}

    Click **Shared Link**, it will show the access link for each system. The Unix-like system include Android, iOS, macOS, Ubuntu etc.

    ![network storage, folder access link](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/folder_access_link.png){class="glboxshadow"}
    
    Then try to access the Samba on various OS, check out [here](#samba-client).

=== "WebDav"

    Toggle to enalbe WebDav, click **Apply**.

    ![network storage, enable webdav](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/enable_webdav.png){class="glboxshadow"}

=== "DLNA"

    Toggle to enalbe DLNA, modify **Share Path** if needed, click **Apply**. That is it.

    ![network storage, enable dlna](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/enable_dlna.png){class="glboxshadow"}

    Connect your smart TV to the router, it will find the DLNA Server.

## Samba Client

=== "Windows"

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

    ![documents samba](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/documents_4.png){class="glboxshadow" width="560"}

## WebDav Client

=== "Windows"

    [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [FileZilla Pro](https://filezillapro.com/){target="_blank"}, [RaiDrive](https://www.raidrive.com/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}

=== "Mac OS"

    [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [FileZilla Pro](https://filezillapro.com/){target="_blank"}, [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Connect to or disconnect from a WebDAV server on Mac](https://support.apple.com/en-gb/guide/mac-help/mchlp1546/mac){target="_blank"}

=== "Android"

    [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}

=== "iOS"

    [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}

