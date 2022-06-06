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

    If you leave the **Anonymous Access** off, you need to create a user by clicking the **+ Add User** button, and then check the user in the option **Writable User** or **Read-Only User**. Finally, click the **Apply** button.

    ![network storage, shared folder](https://static.gl-inet.com/docs/en/4/tutorials/network_storage/shared_folder_settings.png){class="glboxshadow"}

    That is it. Then try to access the Samba on various OS, check out [here](#samba-client).

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

=== "Android"

=== "iOS"

## WebDav Client

=== "Windows"

    [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [FileZilla Pro](https://filezillapro.com/){target="_blank"}, [RaiDrive](https://www.raidrive.com/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}

=== "Mac OS"

    [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [FileZilla Pro](https://filezillapro.com/){target="_blank"}, [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Connect to or disconnect from a WebDAV server on Mac](https://support.apple.com/en-gb/guide/mac-help/mchlp1546/mac){target="_blank"}

=== "Android"

    [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}

=== "iOS"

    [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}

