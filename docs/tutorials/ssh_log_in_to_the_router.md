# SSH Log in to the Router

Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network. The best known example application is for remote login to computer systems by users. Sometime you need to have basic tools to SSH to the server. This guide is about how to SSH login to the GL.iNet routers.

---

## For Windows User

There are ways to access the router terminal on Windows, including via Windows Cmd, PowerShell, Bitvise, or PuTTY.

### Using Windows Cmd

1. Open Command Prompt

    Press **Win** + **R** (Windows key + R key) to open the Run box. Type **cmd** and hit Enter. 

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    A black command prompt window will pop up.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Log in to the Router

    In the command prompt window, type `ssh root@192.168.8.1` and press Enter.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Note**: 192.168.8.1 is the router's default IP address. If you changed it before, use your custom IP instead.

    Next, type your router's admin password and press Enter. **For security, the password does not show on screen**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    If the password is correct, you'll log in to your router successfully.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Troubleshooting"

    1. **Error: Connection timed out**
    
        Ensure your device (such as laptop) is connected to the router. Reconnect to the router's Wi-Fi or LAN port and try again.

    2. **Error: Permission denied**

        Ensure you type the correct admin password. If you forgot the password, reset the router by pressing the RESET button for 10 seconds.

### Using PowerShell

1. Open Windows PowerShell

    Click the search icon on the taskbar, type **PowerShell**, select **Windows PowerShell** and **run it as an administrator**.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Log in to the router

    In the PowerShell window, type `ssh root@192.168.8.1` and press Enter.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Note**: 192.168.8.1 is the router's default IP address. If you changed it before, use your custom IP instead.

    The system will prompt you to confirm the connection. Type `yes` and press Enter.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    You will be prompted to enter the router's admin password. Input the correct admin password and press Enter. **For security, the password does not show on screen**.
    
    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}
    
    Then you will successfully log in to your router's terminal.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Troubleshooting"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        This happens if the router's security key changed (e.g., after a factory reset or firmware update), or if you have previously connected to another router, causing the host key verification to fail.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        To fix it, please open File Explorer, go to `C:\Users\Administrator\.ssh`, find a file named **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Double click on the known_hosts file and open it with Notepad.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Delete the entry related to the router IP address (e.g. 192.168.8.1), and save the file. Exit the File Explorer.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Back in PowerShell, use the command `ssh root@192.168.8.1` to connect to the router again. It will prompt you to confirm connection. Type `yes` and press enter, then input the router's login password. You will then successfully log in to your router's terminal.

    2. **What should I do if I changed the router's SSH port?**
    
        If you have changed the router's SSH port, specify the port via the "-p" parameter when using the ssh command. For example: 
        
        ``ssh -p [new port number] [username]@[router IP address]``

### Using Bitvise

Watch this video to log in to your router via Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Using PuTTY

1. Download PuTTY

    Download the latest PuTTY version from [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Install PuTTY

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Launch PuTTY

    Click **PuTTY** from the Start Menu.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    You will see the following Configuration Window.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Input Host Name (or IP address) `192.168.8.1`, keep Port as default `22`, select connection type as `SSH`.

    Input `Your Session` in saved sessions, and `Save` your content. 

    Then click `Open` at the bottom.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    A security alert will pop-up as below, click `Yes`.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Then input your admin password. **For security, the password does not show on screen**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    When you see a picture above, that means you are now SSH login the router successfully.

---

## For Linux/Mac User

The process on Linux and Mac OS are generally the same. Below we use Ubuntu as an example.

### Using Ubuntu

1. Launch Terminal.

    Run Ubuntu. Double click on the Terminal icon to launch Terminal. 
    
    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Log in to the router.

    Input the SSH login command: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    The system will prompt you to confirm the connection. Type "yes" and hit Enter. 

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Then input your router's admin password. **For security, the password does not show on screen**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    When you see a picture above, it means you log in to the router successfully.

??? "Troubleshooting"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        This happens if the router's security key changed (e.g., after a factory reset or firmware update), or if you have previously connected to another router, causing the host key verification to fail.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        If this happens, run the command in the red box above. Please copy the exact command which is displayed in your terminal.

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Then try connecting again.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**
    
        You may encounter this error when connecting. This error is due to a change in the Openssh package from version 8.8. To fix it, open the **~/.ssh/config** file with a text editor (for example, you can use Nano or Vim) and add the following lines:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Make sure to change the host IP if it is not the default one.

        More discussion about this issue, please refer to [here](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.