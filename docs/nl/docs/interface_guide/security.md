# Security {#security}

**Opmerking**: deze pagina is geïntroduceerd in firmware v4.5.

Ga links in het webbeheerpaneel naar **SYSTEM** -> **Security**.

Op deze pagina kun je verschillende beveiligingsinstellingen configureren om je netwerk en router tegen onbevoegde toegang te beschermen.

## Admin Password {#admin-password}

Hier kun je het aanmeldwachtwoord van het webbeheerpaneel wijzigen.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

Het beheerderswachtwoord moet aan de volgende eisen voldoen:

- Minimaal 10 en maximaal 63 tekens.
- De volgende tekens zijn toegestaan: letters (hoofdlettergevoelig), cijfers en symbolen `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
- Er zijn ten minste twee van de volgende typen vereist: hoofdletters, kleine letters, cijfers en symbolen.

## Access Control {#access-control}

Access Control, in firmware v4.7 en ouder Local Access Control genoemd, beheert de toegang tot verschillende beheerinterfaces van de router.

De functie kan scan- en inbraakpogingen op de standaardpoort voorkomen en netwerkproblemen door poortconflicten vermijden.

**Opmerking**: als het poortnummer in de firmware is gewijzigd, moet je het juiste poortnummer invoeren om het beheerpaneel te openen. Reset de router naar het standaardpoortnummer als je het poortnummer bent vergeten.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Admin Panel {#admin-panel}

- **HTTP Port**: standaard 80, voor niet-versleutelde HTTP-toegang tot het webbeheerpaneel.

- **HTTPS Port**: standaard 443, voor beveiligde HTTPS-toegang tot het webbeheerpaneel.

- **Force HTTPS**: wanneer dit is ingeschakeld, gebruikt toegang tot het webbeheerpaneel verplicht een beveiligde HTTPS-verbinding.

- **Auto-Logout Time**: standaard 5 minuten. Inactieve beheersessies worden na deze tijd om veiligheidsredenen automatisch afgemeld. Je kunt een tijd van 1 minuut tot 3 uur instellen.

### LuCI {#luci}

> Opmerking: installeer LuCI via **Advanced Settings** voordat je de toegangscontrole ervoor instelt.

- **HTTP Port**: standaard 8080, voor niet-versleutelde HTTP-toegang tot de LuCI-interface.

- **HTTPS Port**: standaard 8443, voor beveiligde HTTPS-toegang tot de LuCI-interface.

- **Force HTTPS**: wanneer dit is ingeschakeld, gebruikt toegang tot de LuCI-interface verplicht een beveiligde HTTPS-verbinding.

### SSH {#ssh}

- **Enable SSH**: bepaalt of SSH-toegang tot de router is toegestaan. De functie is standaard ingeschakeld.

- **SSH Port**: standaard 22, de poort voor SSH-toegang tot de router.

### Prohibited Port {#prohibited-port}

Als je een poortnummer toewijst dat conflicteert met een gereserveerde poort of een poort die door browser- of netwerkconventies voor specifieke diensten is gereserveerd, verschijnt de melding "This port is forbidden by the browser".

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "Lijst met poortnummers die door de browser zijn verboden"

    | Poort  | Beschrijving                              |
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

Nadat externe toegang is ingeschakeld, kun je specifieke locaties toestaan. Je kunt bijvoorbeeld externe toegang tot thuisapparaten alleen vanaf kantoor toestaan. Dit vermindert het gebruiksgemak maar verbetert de beveiliging.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: bij een netwerkprobleem kan het toestaan van ping vanaf de WAN-poort helpen controleren of de router goed is verbonden en de netwerklatentie en het pakketverlies bepalen.

- **HTTPS Remote Access**: HTTPS wordt voornamelijk gebruikt voor communicatie tussen webbrowsers en webservers en waarborgt veilige gegevensoverdracht. Gebruik HTTPS om servers op afstand te beheren of webtoepassingen via een browser te openen en de beveiliging en betrouwbaarheid van de gegevensoverdracht te waarborgen.

- **SSH Remote Access**: SSH wordt gebruikt om externe computers en servers veilig te openen en beheren en bestanden over te dragen. Gebruik SSH om via opdrachten of scripts op afstand bij servers aan te melden voor systeembeheer, bestandsoverdracht en andere handelingen. SSH maakt een beveiligde tunnel voor veilige en vertrouwelijke gegevensoverdracht.

- **Allow Remote Access from Specific IPs**: deze functie wordt samen met **Allow Ping from WAN**, **HTTPS Remote Access** of **SSH Remote Access** gebruikt. Je kunt meerdere IP-adressen toevoegen om routers op afstand te beheren vanaf apparaten met deze IP-adressen.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Open Ports on Router {#open-ports-on-router}

Voor openbare bereikbaarheid moeten de bijbehorende poorten voor routerdiensten, zoals web en FTP, op de router worden geopend.

Klik op **Add** om een poort te openen.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

- **Protocol:** selecteer `TCP/UDP`, `TCP` of `UDP`.

- **Port:** voer het poortnummer in dat je wilt openen.

- **Description:** voeg eventueel een beschrijving aan deze regel toe.

- **Enable:** schakel deze regel in of uit.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
