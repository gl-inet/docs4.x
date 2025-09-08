# Security

This feature is available since v4.5.

On the left side of web Admin Panel -> SYSTEM -> Security

## Admin Password

You can change the login password of the web Admin Panel here.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

The requirements for the admin passwords are as follows.

- Minimum 10 characters and maximum 63 characters.
- Letters (case senstive), numbers and symbols `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` are allowed.
- At least two of uppercase letters, lowercase letters, numbers, and symbols are required.

## Access Control

The Access Control, also called Local Access Control in firmware v4.7 and earlier, manages access for different management interfaces of the router.

It can prevent scanning and intrusion attempts on the default port and avoid network problems caused by port conflicts.

**Note**: If the port number is modified in the firmware, you need to enter the correct port number to access the admin panel. If you forgot the port number, please reset the router to the default port number.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Admin Panel

- **HTTP Port**: Defaults to 80, used for unencrypted HTTP access to the web admin panel.

- **HTTPS Port**: Defaults to 443, used for secure HTTPS access to the web admin panel.

- **Force HTTPS**: When enabled, access to the web admin panel is enforced to use a secure HTTPS connection.

- **Auto-Logout Time**: Set to 5 minutes by default, it automatically logs out idle admin sessions after this duration for security. You can customize the auto-logout time, ranging from 1 minute to 3 hours.

### LuCI

- **HTTP Port**: Defaults to 8080, for unencrypted HTTP access to the LuCI interface.

- **HTTPS Port**: Defaults to 8443, for secure HTTPS access to the LuCI interface.

- **Force HTTPS**: When enabled, access to the LuCI interface is enforced to use a secure HTTPS connection.

### SSH

- **Enable SSH**: It controls whether SSH access to the router is permitted. It is enabled by default.

- **SSH Port**: Defaults to 22, the port used for SSH access to the router.

### Prohibited Port

If you assign a port number that conflicts with a reserved port (or one reserved for specific services by browsers/network conventions), a prompt will appear stating "This port is forbidden by the browser".

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "List of port numbers prohibited by the browser"

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

- **Allow Remote Access from Specific IPs**: This function is used in conjunction with **Allow Ping from WAN**, **HTTPS Remote Access** or **SSH Remote Access**. You can add multiple specified IP addresses to remotely manage routers from devices with these specified IP addresses.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Open Ports on Router

The router's services, such as web and FTP, requires their respective ports to be opened on the router in order to be publicly reachable.

To open a port, click **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

**Name:** The name of the rule which can be specified by the user.

**Protocol:** The protocol used, you can choose TCP, UDP, or both TCP and UDP.

**Port:** The port number that you want to open.

**Enable:** Enable or disable of the rule.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.