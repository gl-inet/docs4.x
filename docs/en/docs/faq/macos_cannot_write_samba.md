# macOS cannot write to a Samba share

When using an exFAT-formatted storage device for a Samba share, some macOS devices may encounter one of the following errors when attempting to write files to the share.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Try solving this issue by the following methods.

1. **Check Samba share permissions​.**

    Ensure the Samba share is configured with write access. Log in to your router’s web Admin Panel, and verify the shared folder has "Read/Write" permissions enabled for your user account.

2. **Use the `cp -X file-name` command to copy the file.**

    Since Finder automatically adds extended attributes (e.g., resource forks, metadata) during transfers, which may conflict with Samba’s handling of exFAT storage, please try using the **cp -X file-name** command to copy the file.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Or use **cp -rX folder-name** command to copy the folder.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Restart your Mac.**

    Click the Apple menu and click on Restart. If problems persist, shut down, disconnect all external devices, wait 30 seconds, then restart.​

4. **Rename the file.**

    Right-click the file and click on Rename. Use simple names and avoid special characters like !@# or spaces.​

5. **Reconnect the storage device.**

    If using an external drive such as a USB drive, eject it first before unpluging it, wait 10 seconds, then plug it back in. You can also try different USB port.

6. **Repair disk errors with First Aid.**

    Corrupted disk data can cause write failures. You can use macOS Disk Utility to fix issues. 
    
    1. ​Open Finder -> Applications -> Utilities -> Disk Utility.​ 
    2. Select the drive/storage device (local or external) in the left sidebar.​ 
    3. Click First Aid -> Run. Wait for the process to complete.

7. **Adjust File System or Format the Drive​.**

    If using an exFAT-formatted drive, compatibility issues with Samba may occur on macOS. You can try the following methods.​
    
    - **Format to FAT32** (for external drives, cross-platform compatibility)
    
        1. Back up data on the drive first (formatting erases all files).​
        2. Open Disk Utility -> Select the drive -> Erase.​
        3. Choose "MS-DOS (FAT)" (FAT32) as the format -> Click Erase.​

    - **Format to ext4**
    
        !!! Note
        
            ext4 is primarily supported by Linux systems. After formatting to ext4, the storage device may be incompatible with Windows operating systems, potentially leading to issues such as inability to recognize or write to the drive on Windows devices.​
        
        1. Back up all data on the drive as formatting will erase it.​
        2. Use a tool like Disk Utility or a Linux system to format the drive to ext4.

8. **Update macOS and Clear Caches​.**

    Outdated software or corrupted caches can cause conflicts. Go to System Settings -> General -> Software Update and install the latest version, and clear system caches.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.