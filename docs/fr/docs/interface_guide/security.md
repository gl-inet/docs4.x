# Sécurité

Cette fonctionnalité est disponible depuis le firmware v4.5.

Dans la partie gauche du panneau d'administration web, accédez à **SYSTEM** -> **Security**.

Cette page vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés.

## Mot de passe administrateur

Vous pouvez modifier ici le mot de passe de connexion du panneau d'administration web.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

Le mot de passe administrateur doit respecter les exigences suivantes :

- Au minimum 10 caractères et au maximum 63 caractères.
- Les lettres (distinction majuscules/minuscules), les chiffres et les symboles `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sont autorisés.
- Au moins deux catégories parmi les lettres majuscules, les lettres minuscules, les chiffres et les symboles sont requises.

## Contrôle d'accès

Le contrôle d'accès, également appelé **Local Access Control** dans le firmware v4.7 et les versions antérieures, gère l'accès aux différentes interfaces de gestion du routeur.

Il permet d'éviter les tentatives de scan et d'intrusion sur les ports par défaut, ainsi que les problèmes réseau causés par des conflits de ports.

**Remarque** : si le numéro de port est modifié dans le firmware, vous devez saisir le numéro correct pour accéder au panneau d'administration. Si vous l'avez oublié, réinitialisez le routeur afin de restaurer le numéro de port par défaut.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Panneau d'administration

- **HTTP Port** : 80 par défaut ; utilisé pour l'accès HTTP non chiffré au panneau d'administration web.

- **HTTPS Port** : 443 par défaut ; utilisé pour l'accès HTTPS sécurisé au panneau d'administration web.

- **Force HTTPS** : lorsqu'il est activé, l'accès au panneau d'administration web est forcé en HTTPS.

- **Auto-Logout Time** : réglé sur 5 minutes par défaut ; déconnecte automatiquement les sessions administrateur inactives après ce délai pour renforcer la sécurité. Vous pouvez le personnaliser de 1 minute à 3 heures.

### LuCI

- **HTTP Port** : 8080 par défaut, pour l'accès HTTP non chiffré à l'interface LuCI.

- **HTTPS Port** : 8443 par défaut, pour l'accès HTTPS sécurisé à l'interface LuCI.

- **Force HTTPS** : lorsqu'il est activé, l'accès à l'interface LuCI est forcé en HTTPS.

### SSH

- **Enable SSH** : contrôle si l'accès SSH au routeur est autorisé. Cette option est activée par défaut.

- **SSH Port** : 22 par défaut ; port utilisé pour l'accès SSH au routeur.

### Port interdit {#prohibited-port}

Si vous attribuez un numéro de port en conflit avec un port réservé (ou réservé à certains services par les navigateurs ou conventions réseau), un message s'affichera indiquant : "This port is forbidden by the browser".

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "Liste des numéros de ports interdits par le navigateur"

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

## Contrôle d'accès à distance

Après activation de l'accès à distance, il est possible d'autoriser uniquement certains emplacements, par exemple permettre l'accès aux appareils domestiques uniquement depuis le bureau, au prix d'un peu moins de confort mais avec une meilleure sécurité.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN** : en cas de problème réseau, autoriser Ping depuis le port WAN peut aider les utilisateurs ou administrateurs réseau à vérifier si le routeur est correctement connecté, ainsi qu'à évaluer la latence et la perte de paquets.

- **HTTPS Remote Access** : le protocole HTTPS est principalement utilisé pour la communication entre navigateurs web et serveurs web, afin d'assurer une transmission sécurisée des données.

- **SSH Remote Access** : le protocole SSH sert principalement à accéder en toute sécurité à des ordinateurs et serveurs distants et à les administrer, ainsi qu'à effectuer des transferts de fichiers.

- **Allow Remote Access from Specific IPs** : cette fonction s'utilise avec **Allow Ping from WAN**, **HTTPS Remote Access** ou **SSH Remote Access**. Vous pouvez ajouter plusieurs adresses IP spécifiques pour gérer le routeur à distance depuis ces adresses.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

## Ports ouverts sur le routeur

Cette section affiche les ports actuellement ouverts sur le routeur et vous permet d'en ouvrir ou fermer selon vos besoins.

![open_ports](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
