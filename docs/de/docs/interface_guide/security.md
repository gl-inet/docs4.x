# Sicherheit

Diese Funktion ist seit Firmware v4.5 verfügbar.

Gehen Sie in der Web-Adminoberfläche auf der linken Seite zu **SYSTEM** -> **Security**.

Auf dieser Seite können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen.

## Admin-Passwort

Hier können Sie das Anmeldepasswort der Web-Adminoberfläche ändern.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

Das Admin-Passwort muss die folgenden Anforderungen erfüllen:

- Mindestens 10 und höchstens 63 Zeichen.
- Buchstaben (Groß-/Kleinschreibung wird unterschieden), Zahlen und Symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sind erlaubt.
- Mindestens zwei der folgenden Kategorien sind erforderlich: Großbuchstaben, Kleinbuchstaben, Zahlen und Symbole.

## Zugriffskontrolle

Die Zugriffskontrolle, in Firmware v4.7 und früher auch als Local Access Control bezeichnet, verwaltet den Zugriff auf die verschiedenen Verwaltungsschnittstellen des Routers.

Sie kann Scan- und Eindringversuche auf dem Standardport verhindern und Netzwerkprobleme vermeiden, die durch Portkonflikte verursacht werden.

**Hinweis**: Wenn die Portnummer in der Firmware geändert wurde, müssen Sie die richtige Portnummer eingeben, um auf das Admin Panel zuzugreifen. Wenn Sie die Portnummer vergessen haben, setzen Sie den Router bitte auf die Standardportnummer zurück.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Admin Panel

- **HTTP Port**: Standardmäßig 80; wird für unverschlüsselten HTTP-Zugriff auf das Web-Admin-Panel verwendet.

- **HTTPS Port**: Standardmäßig 443; wird für sicheren HTTPS-Zugriff auf das Web-Admin-Panel verwendet.

- **Force HTTPS**: Wenn aktiviert, wird der Zugriff auf das Web-Admin-Panel zur Verwendung einer sicheren HTTPS-Verbindung erzwungen.

- **Auto-Logout Time**: Standardmäßig auf 5 Minuten eingestellt. Nach dieser Zeit werden inaktive Admin-Sitzungen aus Sicherheitsgründen automatisch abgemeldet. Sie können die automatische Abmeldezeit anpassen; der Bereich reicht von 1 Minute bis 3 Stunden.

### LuCI

- **HTTP Port**: Standardmäßig 8080; für unverschlüsselten HTTP-Zugriff auf die LuCI-Oberfläche.

- **HTTPS Port**: Standardmäßig 8443; für sicheren HTTPS-Zugriff auf die LuCI-Oberfläche.

- **Force HTTPS**: Wenn aktiviert, wird der Zugriff auf die LuCI-Oberfläche zur Verwendung einer sicheren HTTPS-Verbindung erzwungen.

### SSH

- **Enable SSH**: Legt fest, ob SSH-Zugriff auf den Router erlaubt ist. Standardmäßig ist diese Option aktiviert.

- **SSH Port**: Standardmäßig 22; der Port, der für den SSH-Zugriff auf den Router verwendet wird.

### Verbotene Ports

Wenn Sie eine Portnummer zuweisen, die mit einem reservierten Port kollidiert (oder mit einem Port, der von Browsern bzw. Netzwerkkonventionen für bestimmte Dienste reserviert ist), erscheint ein Hinweis mit der Meldung "This port is forbidden by the browser".

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "Liste der vom Browser verbotenen Portnummern"

    | Port  | Beschreibung                            |
    | :-----| :-------------------------------------: |
    | 1     | tcpmux                                  |
    | 7     | echo                                    |
    | 9     | discard                                 |
    | 11    | systat                                  |
    | 13    | daytime                                 |
    | 15    | netstat                                 |
    | 17    | qotd                                    |
    | 19    | chargen                                 |
    | 20    | ftp data                                |
    | 21    | ftp access                              |
    | 22    | ssh                                     |
    | 23    | telnet                                  |
    | 25    | smtp                                    |
    | 37    | time                                    |
    | 42    | name                                    |
    | 43    | nicname                                 |
    | 53    | domain                                  |
    | 69    | tftp                                    |
    | 77    | priv-rjs                                |
    | 79    | finger                                  |
    | 87    | ttylink                                 |
    | 95    | supdup                                  |
    | 101   | hostriame                               |
    | 102   | iso-tsap                                |
    | 103   | gppitnp                                 |
    | 104   | acr-nema                                |
    | 109   | pop2                                    |
    | 110   | pop3                                    |
    | 111   | sunrpc                                  |
    | 113   | auth                                    |
    | 115   | sftp                                    |
    | 117   | uucp-path                               |
    | 119   | nntp                                    |
    | 123   | NTP                                     |
    | 135   | loc-srv /epmap                          |
    | 137   | netbios                                 |
    | 139   | netbios                                 |
    | 143   | imap2                                   |
    | 161   | snmp                                    |
    | 179   | BGP                                     |
    | 389   | ldap                                    |
    | 427   | SLP (Also used by Apple Filing Protocol) |
    | 465   | smtp+ssl                                |
    | 512   | print / exec                            |
    | 513   | login                                   |
    | 514   | shell                                   |
    | 515   | printer                                 |
    | 526   | tempo                                   |
    | 530   | courier                                 |
    | 531   | chat                                    |
    | 532   | netnews                                 |
    | 540   | uucp                                    |
    | 548   | AFP (Apple Filing Protocol)             |
    | 554   | rtsp                                    |
    | 556   | remotefs                                |
    | 563   | nntp+ssl                                |
    | 587   | smtp (rfc6409)                          |
    | 601   | syslog-conn (rfc3195)                   |
    | 636   | ldap+ssl                                |
    | 989   | ftps-data                               |
    | 990   | ftps                                    |
    | 993   | ldap+ssl                                |
    | 995   | pop3+ssl                                |
    | 1719  | h323gatestat                            |
    | 1720  | h323hostcall                            |
    | 1723  | pptp                                    |
    | 2049  | nfs                                     |
    | 3659  | apple-sasl / PasswordServer             |
    | 4045  | lockd                                   |
    | 5060  | sip                                     |
    | 5061  | sips                                    |
    | 6000  | X11                                     |
    | 6566  | sane-port                               |
    | 6665  | Alternate IRC [Apple addition]          |
    | 6666  | Alternate IRC [Apple addition]          |
    | 6667  | Standard IRC [Apple addition]           |
    | 6668  | Alternate IRC [Apple addition]          |
    | 6669  | Alternate IRC [Apple addition]          |
    | 6697  | IRC + TLS                               |
    | 10080 | Amanda                                  |

## Fernzugriffskontrolle

Nach dem Aktivieren des Fernzugriffs können bestimmte Orte für den Zugriff festgelegt werden, z. B. indem Fernzugriff auf Geräte zu Hause nur vom Büro aus erlaubt wird. Das ist weniger bequem, erhöht aber die Sicherheit.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: Wenn ein Netzwerkproblem vorliegt, kann das Erlauben von Ping vom WAN-Port Benutzern oder Netzwerkadministratoren helfen zu prüfen, ob der Router korrekt verbunden ist, sowie Netzwerklatenz und Paketverlust zu ermitteln.

- **HTTPS Remote Access**: Das HTTPS-Protokoll wird hauptsächlich für die Kommunikation zwischen Webbrowsern und Webservern verwendet und bietet eine sichere Datenübertragung. Wenn Benutzer Server per Fernzugriff verwalten oder über Webbrowser auf Webanwendungen zugreifen müssen, kann das HTTPS-Protokoll genutzt werden, um die Sicherheit und Zuverlässigkeit der Datenübertragung zu gewährleisten.

- **SSH Remote Access**: Das SSH-Protokoll wird hauptsächlich für den sicheren Zugriff auf und die Verwaltung von entfernten Computern und Servern sowie für Dateiübertragungen verwendet. Wenn Benutzer sich für Systemverwaltung, Dateiübertragung und andere Vorgänge per Fernzugriff über Kommandozeilen oder Skripte an Servern anmelden müssen, kann das SSH-Protokoll genutzt werden, um einen sicheren Tunnel einzurichten und die Sicherheit sowie Vertraulichkeit der Datenübertragung zu gewährleisten.

- **Allow Remote Access from Specific IPs**: Diese Funktion wird zusammen mit **Allow Ping from WAN**, **HTTPS Remote Access** oder **SSH Remote Access** verwendet. Sie können mehrere bestimmte IP-Adressen hinzufügen, um Router per Fernzugriff von Geräten mit diesen angegebenen IP-Adressen aus zu verwalten.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Offene Ports auf dem Router

Damit Dienste des Routers wie Web und FTP öffentlich erreichbar sind, müssen die jeweiligen Ports auf dem Router geöffnet werden.

Um einen Port zu öffnen, klicken Sie auf **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

**Name:** Der Name der Regel, der vom Benutzer festgelegt werden kann.

**Protocol:** Das verwendete Protokoll. Sie können TCP, UDP oder sowohl TCP als auch UDP wählen.

**Port:** Die Portnummer, die Sie öffnen möchten.

**Enable:** Aktivieren oder deaktivieren Sie die Regel.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
