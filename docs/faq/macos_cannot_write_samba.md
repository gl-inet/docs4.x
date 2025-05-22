# MacOS cannot write to a Samba share

When using an ExFAT-formatted storage device with a Samba share on macOS, some Mac devices may display an error message when trying to write a file: 

**"The operation can't be completed because an unexpected error occurred (error code 100093)."**

![macopyerror](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

This is because the Finder adds file attributes before transferring, making the file different from the original when copying.

You can solve this issue by the following methods.

Method 1. Change your storage device into **NTFS** format.

Method 2. Use the **cp -X file-name** command to copy the file.

![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

Or use **cp -rX floder-name** command to copy the folder.

![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.