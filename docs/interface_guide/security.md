# Security

This feature is available since v4.5.

On the left side of web Admin Panel -> SYSTEM -> Security

## Admin Password

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.png){class="glboxshadow"}

Change the password of login the web Admin Panel. You have to input your current password to change it.

For security reasons, we recommend that you turn on **Prevent Weak Password**.

When **Prevent Weak Password** is turned on, the requirements for new passwords are as follows.

- 5 characters and maximum 63 characters.
- Letters (case senstive), numbers and symbols `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` are allowed.
- At least two of uppercase letters, lowercase letters, numbers, and symbols are required.

## Local Access Control

The local control feature can prevent scanning and intrusion attempts on the default port and avoid network problems caused by port conflicts.

**Note**: If the port number is modified in the firmware, you needs to enter the correct port number on the mobile phone to enter the admin panel. If the port number is forgotten, please reset the router to the default port number.

![security_default_local_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_default_local_access_control.png){class="glboxshadow"}

**Auto-Logout Time**: Interval between closing or hibernating the browser page and logging out.

### Prohibited Port

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "The list of port numbers prohibited by the browser is as follows:"

    | Port  | Description                              |
    | :-----| :--------------------------------------: |
    | 1     | tcpmux                                   |
    | 7     | echo                                     |
    | 9     | discard                                  |
    | 11    | systat                                   |
    | 13    | daytime                                  |
    | 15    | netstat                                  |
    | 17    | qotd                                     |
    | 19    | chargen                                  |
    | 20    | ftp data                                 |
    | 21    | ftp access                               |
    | 22    | ssh                                      |
    | 23    | telnet                                   |
    | 25    | smtp                                     |
    | 37    | time                                     |
    | 42    | name                                     |
    | 43    | nicname                                  |
    | 53    | domain                                   |
    | 69    | tftp                                     |
    | 77    | priv-rjs                                 |
    | 79    | finger                                   |
    | 87    | ttylink                                  |
    | 95    | supdup                                   |
    | 101   | hostriame                                |
    | 102   | iso-tsap                                 |
    | 103   | gppitnp                                  |
    | 104   | acr-nema                                 |
    | 109   | pop2                                     |
    | 110   | pop3                                     |
    | 111   | sunrpc                                   |
    | 113   | auth                                     |
    | 115   | sftp                                     |
    | 117   | uucp-path                                |
    | 119   | nntp                                     |
    | 123   | NTP                                      |
    | 135   | loc-srv /epmap                           |
    | 137   | netbios                                  |
    | 139   | netbios                                  |
    | 143   | imap2                                    |
    | 161   | snmp                                     |
    | 179   | BGP                                      |
    | 389   | ldap                                     |
    | 427   | SLP (Also used by Apple Filing Protocol) |
    | 465   | smtp+ssl                                 |
    | 512   | print / exec                             |
    | 513   | login                                    |
    | 514   | shell                                    |
    | 515   | printer                                  |
    | 526   | tempo                                    |
    | 530   | courier                                  |
    | 531   | chat                                     |
    | 532   | netnews                                  |
    | 540   | uucp                                     |
    | 548   | AFP (Apple Filing Protocol)              |
    | 554   | rtsp                                     |
    | 556   | remotefs                                 |
    | 563   | nntp+ssl                                 |
    | 587   | smtp (rfc6409)                           |
    | 601   | syslog-conn (rfc3195)                    |
    | 636   | ldap+ssl                                 |
    | 989   | ftps-data                                |
    | 990   | ftps                                     |
    | 993   | ldap+ssl                                 |
    | 995   | pop3+ssl                                 |
    | 1719  | h323gatestat                             |
    | 1720  | h323hostcall                             |
    | 1723  | pptp                                     |
    | 2049  | nfs                                      |
    | 3659  | apple-sasl / PasswordServer              |
    | 4045  | lockd                                    |
    | 5060  | sip                                      |
    | 5061  | sips                                     |
    | 6000  | X11                                      |
    | 6566  | sane-port                                |
    | 6665  | Alternate IRC [Apple addition]           |
    | 6666  | Alternate IRC [Apple addition]           |
    | 6667  | Standard IRC [Apple addition]            |
    | 6668  | Alternate IRC [Apple addition]           |
    | 6669  | Alternate IRC [Apple addition]           |
    | 6697  | IRC + TLS                                |
    | 10080 | Amanda                                   |

## Remote Access Control

After enabling remote access, specific locations can be set to allow access, such as enabling remote access to home devices only from the office, sacrificing convenience for improved security.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: When there is a network problem, allowing Ping from the WAN port can help users or network administrators check whether the router is properly connected, as well as determine network latency and packet loss.

- **HTTPS Remote Access**: HTTPS protocol is mainly used for communication between web browsers and web servers, providing secure data transmission guarantee. Therefore, when users need to remotely manage servers or access web applications through web browsers, HTTPS protocol can be used to ensure the security and reliability of data transmission.

- **SSH Remote Access**: SSH protocol is mainly used for securely accessing and managing remote computers and servers, as well as performing file transfer operations. When users need to remotely log in to servers through command lines or scripts for system management, file transfer, and other operations, SSH protocol can be used to establish a secure tunnel to ensure the security and privacy of data transmission.

- **Allow Remote Access from Specific IPs**: This function is used in conjunction with the **HTTPS Remote Access** or **SSH Remote Access**.You can add multiple specified IP addresses to remotely manage routers from devices with these specified IP addresses.

![add_ip_address](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address.png){class="glboxshadow"}

![add_ip_address_list](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_list.png){class="glboxshadow"}


---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.