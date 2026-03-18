# How to use WinSCP to modify files on GL.iNet routers

WinSCP is an easy tool to edit, copy and download files or directory on the router. You can copy file between a local computer and your router using FTP, SCP, SFTP, WebDAV or S3 file transfer protocols. It applies to the Windows operating system.

---

1. Download WinSCP from [here](https://winscp.net/eng/download.php){target="_blank"} and install on your Windows.

2. Connect to the router, then Run WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * File protocol: Choose `SCP` as the protocol.
    * Host name: Input the router IP. If you didn't change the IP of your router, it should be `192.168.8.1`
    * Port number: `22`
    * Username & Password: Input `root` as the username and enter your password. 

    Then click `Login` button.

3. After login, you will have full control of the router.

    You can choose, view, edit or transfer files/directories from/to the router.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    For example, if you want to edit firewall config, you can go to /etc/config, find the firewall file, right click on it and then choose **Edit**.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Now you can edit the file content freely. Be careful not to mess up the settings.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.