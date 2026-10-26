# Security {#security}

**Note**: This page was introduced in firmware v4.5.

Öppna **SYSTEM** -> **Security** på vänster sida i webbadministrationspanelen.

På sidan kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst.

## Admin Password {#admin-password}

Här kan du ändra inloggningslösenordet för webbadministrationspanelen.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

The admin password must meet the following requirements:

- Minimum 10 characters and maximum 63 characters.
- Letters (case sensitive), numbers and symbols `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` are allowed.
- Minst två av följande teckentyper krävs: versaler, gemener, siffror och symboler.

## Access Control {#access-control}

Access Control, som heter Local Access Control i firmware v4.7 och tidigare, hanterar åtkomsten till routerns olika hanteringsgränssnitt.

Funktionen kan förhindra skanning och intrångsförsök på standardporten och undvika nätverksproblem som orsakas av portkonflikter.

**Obs!** Om portnumret ändras i firmware måste du ange rätt portnummer för att öppna administratörspanelen. Om du glömmer portnumret återställer du routern till standardportnumret.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Admin Panel {#admin-panel}

- **HTTP Port**: Defaults to 80, used for unencrypted HTTP access to the web admin panel.

- **HTTPS Port**: Defaults to 443, used for secure HTTPS access to the web admin panel.

- **Force HTTPS**: När alternativet är aktiverat måste webbadministrationspanelen öppnas via en säker HTTPS-anslutning.

- **Auto-Logout Time**: Standardvärdet är 5 minuter. Inaktiva administratörssessioner loggas automatiskt ut efter denna tid av säkerhetsskäl. Tiden kan anges från 1 minut till 3 timmar.

### LuCI {#luci}

> Obs! Installera LuCI under **Advanced Settings** innan du konfigurerar åtkomstkontroll för det.

- **HTTP Port**: Defaults to 8080, for unencrypted HTTP access to the LuCI interface.

- **HTTPS Port**: Defaults to 8443, for secure HTTPS access to the LuCI interface.

- **Force HTTPS**: När alternativet är aktiverat måste LuCI-gränssnittet öppnas via en säker HTTPS-anslutning.

### SSH {#ssh}

- **Enable SSH**: It controls whether SSH access to the router is permitted. It is enabled by default.

- **SSH Port**: Defaults to 22, the port used for SSH access to the router.

### Prohibited Port {#prohibited-port}

Om du anger ett portnummer som står i konflikt med en reserverad port, eller en port som webbläsare eller nätverkskonventioner reserverar för vissa tjänster, visas meddelandet "This port is forbidden by the browser".

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

## Remote Access Control {#remote-access-control}

När fjärråtkomst har aktiverats kan du ange platser som får ansluta, till exempel endast tillåta fjärråtkomst till hemenheter från kontoret. Det förbättrar säkerheten men minskar bekvämligheten.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: Vid nätverksproblem kan Ping från WAN-porten hjälpa användare eller nätverksadministratörer att kontrollera om routern är korrekt ansluten och mäta nätverkslatens och paketförlust.

- **HTTPS Remote Access**: HTTPS används främst för kommunikation mellan webbläsare och webbservrar och ger säker dataöverföring. Använd HTTPS för att säkerställa säker och tillförlitlig överföring när servrar fjärrhanteras eller webbprogram öppnas via en webbläsare.

- **SSH Remote Access**: SSH används främst för säker åtkomst till och hantering av fjärrdatorer och servrar samt filöverföring. Vid fjärrinloggning på servrar via kommandorad eller skript kan SSH upprätta en säker tunnel som skyddar dataöverföringen.

- **Allow Remote Access from Specific IPs**: Funktionen används tillsammans med **Allow Ping from WAN**, **HTTPS Remote Access** eller **SSH Remote Access**. Du kan lägga till flera angivna IP-adresser och fjärrhantera routrar från enheter med dessa adresser.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Open Ports on Router {#open-ports-on-router}

Routerns tjänster, till exempel webb och FTP, kräver att respektive port öppnas på routern för att vara offentligt åtkomliga.

To open a port, click **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

- **Protocol:** Välj `TCP/UDP`, `TCP` eller `UDP`.

- **Port:** Ange portnumret som du vill öppna.

- **Description:** Add a description to this rule (optional).

- **Enable:** Toggle to enable or disable this rule.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
