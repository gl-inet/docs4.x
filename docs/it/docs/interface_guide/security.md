# Security

Questa funzione e' disponibile dal firmware v4.5.

Sul lato sinistro del pannello di amministrazione web, vai su **SYSTEM** -> **Security**.

Questa pagina consente di configurare varie impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati.

## Admin Password

Qui puoi cambiare la password di accesso del pannello di amministrazione web.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

La password admin deve soddisfare i seguenti requisiti:

- Minimo 10 caratteri e massimo 63 caratteri.
- Sono consentiti lettere, con distinzione tra maiuscole e minuscole, numeri e simboli `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
- Sono richiesti almeno due tra lettere maiuscole, lettere minuscole, numeri e simboli.

## Access Control

Access Control, chiamato anche Local Access Control nel firmware v4.7 e precedenti, gestisce l'accesso alle diverse interfacce di gestione del router.

Puo' impedire scansioni e tentativi di intrusione sulla porta predefinita ed evitare problemi di rete causati da conflitti di porta.

**Nota**: se il numero di porta viene modificato nel firmware, devi inserire il numero di porta corretto per accedere al pannello di amministrazione. Se dimentichi il numero di porta, ripristina il router al numero di porta predefinito.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Admin Panel

- **HTTP Port**: il valore predefinito e' 80 ed e' usato per l'accesso HTTP non crittografato al pannello di amministrazione web.

- **HTTPS Port**: il valore predefinito e' 443 ed e' usato per l'accesso HTTPS sicuro al pannello di amministrazione web.

- **Force HTTPS**: se abilitato, l'accesso al pannello di amministrazione web viene forzato a usare una connessione HTTPS sicura.

- **Auto-Logout Time**: il valore predefinito e' 5 minuti; disconnette automaticamente le sessioni admin inattive dopo questo intervallo per motivi di sicurezza. Puoi personalizzare il tempo di auto-logout da 1 minuto a 3 ore.

### LuCI

- **HTTP Port**: il valore predefinito e' 8080, per l'accesso HTTP non crittografato all'interfaccia LuCI.

- **HTTPS Port**: il valore predefinito e' 8443, per l'accesso HTTPS sicuro all'interfaccia LuCI.

- **Force HTTPS**: se abilitato, l'accesso all'interfaccia LuCI viene forzato a usare una connessione HTTPS sicura.

### SSH

- **Enable SSH**: controlla se l'accesso SSH al router e' consentito. E' abilitato per impostazione predefinita.

- **SSH Port**: il valore predefinito e' 22, la porta usata per l'accesso SSH al router.

### Prohibited Port {#prohibited-port}

Se assegni un numero di porta in conflitto con una porta riservata, o riservata a servizi specifici in base alle convenzioni di browser o rete, comparira' il messaggio "This port is forbidden by the browser".

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "Elenco dei numeri di porta vietati dal browser"

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

Dopo aver abilitato l'accesso remoto, e' possibile impostare posizioni specifiche da cui consentire l'accesso, ad esempio permettendo l'accesso remoto ai dispositivi di casa solo dall'ufficio, sacrificando comodita' in favore di una maggiore sicurezza.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: quando si verifica un problema di rete, consentire il Ping dalla porta WAN puo' aiutare utenti o amministratori di rete a verificare se il router e' collegato correttamente, oltre a determinare latenza di rete e perdita di pacchetti.

- **HTTPS Remote Access**: il protocollo HTTPS viene usato principalmente per la comunicazione tra browser web e server web, fornendo una trasmissione sicura dei dati. Pertanto, quando gli utenti devono gestire server da remoto o accedere ad applicazioni web tramite browser, il protocollo HTTPS puo' essere usato per garantire la sicurezza e l'affidabilita' della trasmissione dei dati.

- **SSH Remote Access**: il protocollo SSH viene usato principalmente per accedere e gestire in modo sicuro computer e server remoti, oltre a eseguire trasferimenti di file. Quando gli utenti devono accedere da remoto ai server tramite righe di comando o script per gestione del sistema, trasferimento file e altre operazioni, il protocollo SSH puo' essere usato per creare un tunnel sicuro e garantire sicurezza e privacy dei dati.

- **Allow Remote Access from Specific IPs**: questa funzione viene usata insieme a **Allow Ping from WAN**, **HTTPS Remote Access** o **SSH Remote Access**. Puoi aggiungere piu' indirizzi IP specifici per gestire da remoto i router da dispositivi con tali IP specifici.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Open Ports on Router

I servizi del router, come web e FTP, richiedono che le rispettive porte siano aperte sul router per essere raggiungibili pubblicamente.

Per aprire una porta, fai clic su **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

**Name:** il nome della regola, che puo' essere specificato dall'utente.

**Protocol:** il protocollo usato. Puoi scegliere TCP, UDP oppure sia TCP sia UDP.

**Port:** il numero di porta che vuoi aprire.

**Enable:** abilita o disabilita la regola.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
