# Bezpieczeństwo

Ta funkcja jest dostępna od wersji firmware v4.5.

W lewym panelu bocznym panelu administracyjnego przejdź do **SYSTEM** -> **Security**.

Ta strona umożliwia konfigurację różnych ustawień zabezpieczeń chroniących sieć i router przed nieautoryzowanym dostępem.

## Hasło administratora

Tutaj możesz zmienić hasło logowania do panelu administracyjnego.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

Hasło administratora musi spełniać następujące wymagania:

- Minimum 10 znaków i maksimum 63 znaki.
- Dozwolone są litery (z rozróżnieniem wielkości), cyfry oraz symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
- Wymagane są co najmniej dwa z następujących typów znaków: wielkie litery, małe litery, cyfry i symbole.

## Kontrola dostępu

Kontrola dostępu, nazywana **Local Access Control** w firmware v4.7 i starszym, zarządza dostępem do różnych interfejsów zarządzania routerem.

Pomaga zapobiegać skanowaniu i próbom włamania na domyślne porty oraz unikać problemów sieciowych spowodowanych konfliktami portów.

**Uwaga**: Jeśli numer portu zostanie zmieniony w firmware, aby uzyskać dostęp do panelu administracyjnego, musisz wpisać prawidłowy numer portu. Jeśli go nie pamiętasz, przywróć router do domyślnego numeru portu.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Admin Panel

- **HTTP Port**: Domyślnie 80; używany do niezaszyfrowanego dostępu HTTP do panelu administracyjnego.

- **HTTPS Port**: Domyślnie 443; używany do bezpiecznego dostępu HTTPS do panelu administracyjnego.

- **Force HTTPS**: Po włączeniu dostęp do panelu administracyjnego będzie wymuszony przez bezpieczne połączenie HTTPS.

- **Auto-Logout Time**: Domyślnie ustawione na 5 minut; automatycznie wylogowuje nieaktywne sesje administratora po upływie tego czasu. Możesz dostosować czas automatycznego wylogowania w zakresie od 1 minuty do 3 godzin.

### LuCI

- **HTTP Port**: Domyślnie 8080; używany do niezaszyfrowanego dostępu HTTP do interfejsu LuCI.

- **HTTPS Port**: Domyślnie 8443; używany do bezpiecznego dostępu HTTPS do interfejsu LuCI.

- **Force HTTPS**: Po włączeniu dostęp do interfejsu LuCI będzie wymuszony przez bezpieczne połączenie HTTPS.

### SSH

- **Enable SSH**: Określa, czy dostęp SSH do routera jest dozwolony. Domyślnie jest włączony.

- **SSH Port**: Domyślnie 22; port używany do dostępu SSH do routera.

### Niedozwolone porty {#prohibited-port}

Jeśli przypiszesz numer portu, który koliduje z portem zarezerwowanym (lub z portem zarezerwowanym dla określonych usług przez przeglądarki albo konwencje sieciowe), pojawi się komunikat „This port is forbidden by the browser”.

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "Lista numerów portów niedozwolonych przez przeglądarkę"

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

## Kontrola zdalnego dostępu

Po włączeniu zdalnego dostępu możesz określić, z jakich lokalizacji będzie on dozwolony. Na przykład możesz zezwolić na zdalny dostęp do urządzeń domowych tylko z biura, rezygnując z części wygody na rzecz większego bezpieczeństwa.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: W przypadku problemów z siecią zezwolenie na Ping z portu WAN pomaga użytkownikom lub administratorom sieci sprawdzić, czy router jest prawidłowo podłączony, a także ocenić opóźnienia sieci i utratę pakietów.

- **HTTPS Remote Access**: Protokół HTTPS służy głównie do komunikacji między przeglądarkami internetowymi a serwerami WWW, zapewniając bezpieczną transmisję danych. Gdy użytkownik musi zdalnie zarządzać serwerem lub uzyskać dostęp do aplikacji webowej przez przeglądarkę, HTTPS pomaga zapewnić bezpieczeństwo i niezawodność transmisji danych.

- **SSH Remote Access**: Protokół SSH służy głównie do bezpiecznego dostępu do zdalnych komputerów i serwerów oraz do ich zarządzania, a także do transferu plików. Gdy użytkownik musi zdalnie logować się do serwera z poziomu wiersza poleceń lub skryptu w celu zarządzania systemem, transferu plików lub wykonania innych operacji, SSH tworzy bezpieczny tunel chroniący transmisję danych i prywatność.

- **Allow Remote Access from Specific IPs**: Ta funkcja działa razem z **Allow Ping from WAN**, **HTTPS Remote Access** lub **SSH Remote Access**. Możesz dodać wiele konkretnych adresów IP, aby umożliwić zdalne zarządzanie routerem tylko z urządzeń korzystających z tych adresów.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Otwarte porty na routerze

Aby usługi routera, takie jak WWW i FTP, były publicznie dostępne, odpowiednie porty muszą być otwarte na routerze.

Aby otworzyć port, kliknij **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

**Name:** Nazwa reguły nadawana przez użytkownika.

**Protocol:** Używany protokół. Możesz wybrać TCP, UDP albo jednocześnie TCP i UDP.

**Port:** Numer portu, który chcesz otworzyć.

**Enable:** Włącza lub wyłącza regułę.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
