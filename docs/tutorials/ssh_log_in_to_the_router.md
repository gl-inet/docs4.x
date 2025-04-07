# SSH Log in to the Router

Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network. The best known example application is for remote login to computer systems by users. Sometime you need to have basic tools to SSH to the server. This guide is about how to SSH login to the GL.iNet routers.

---

## For Windows User

There are many tools, like Windows PowerShell, PuTTY, Bitvise.

### Using Bitvise

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Using PuTTY

#### 1. Download PuTTY

Download the latest PuTTY version from [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

#### 2. Install PuTTY

![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

#### 3. Launch PuTTY

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

Then input your admin password.

*Note: You need to use your password which you set up the router at the first time*.

![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

When you see a picture above, that means you are now SSH login the router successfully.

---

## For Linux/Mac User

The process on Linux and Mac OS are generally the same. Below we use Ubuntu as an example.

### Using Ubuntu

#### 1. Launch Terminal

Run Ubuntu.

![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

Click the `Terminal` icon to launch Terminal. Then input the following command:

`ssh root@192.168.8.1`

If you have ever connected to another router, host key verification failed may displayed as follow:

![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow"}

If this happens, run the command in the red box. Please copy the exact command which is displayed in your terminal.

`ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow"}

You may also encounter the following error when connecting:

`Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa`

This error is due to a change in the Openssh package from version 8.8. To fix it, open the **~/.ssh/config** file with a text editor (you can use for example Nano or Vim) and add the following lines:

    host 192.168.8.1
        HostkeyAlgorithms +ssh-rsa
        PubkeyAcceptedAlgorithms +ssh-rsa

Make sure to change the host IP if it is not the default one.

#### 2. Log In Router

Retry the SSH login command:

`ssh root@192.168.8.1`

![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

Type "yes". 

![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

Then input your router password. You can set this password when you first connect to your router.

![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

When you see a picture above, it means you login the router successfully.

## Troubleshooting

[No matching host key type found. Their offer: ssh-rsa](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915/11)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.