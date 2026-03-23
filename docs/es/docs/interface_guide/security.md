# Seguridad

Esta función está disponible desde el firmware v4.5.

En el lado izquierdo del panel de administración web, vaya a **SYSTEM** -> **Security**.

Esta página le permite configurar varios ajustes de seguridad para proteger su red y su router frente a accesos no autorizados.

## Contraseña de administrador

Aquí puede cambiar la contraseña de inicio de sesión del panel de administración web.

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

La contraseña de administrador debe cumplir los siguientes requisitos:

- Mínimo 10 caracteres y máximo 63 caracteres.
- Se permiten letras, distinguiendo entre mayúsculas y minúsculas, números y los símbolos ``! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~``.
- Se requieren al menos dos de estos tipos: letras mayúsculas, letras minúsculas, números y símbolos.

## Control de acceso

Access Control, también llamado Local Access Control en el firmware v4.7 y anteriores, gestiona el acceso a las distintas interfaces de administración del router.

Puede evitar intentos de escaneo e intrusión en el puerto predeterminado, así como problemas de red causados por conflictos de puertos.

**Nota**: Si el número de puerto se ha modificado en el firmware, deberá introducir el puerto correcto para acceder al panel de administración. Si olvidó el número de puerto, restablezca el router al puerto predeterminado.

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### Panel de administración

- **HTTP Port**: El valor predeterminado es 80 y se utiliza para el acceso HTTP sin cifrar al panel de administración web.

- **HTTPS Port**: El valor predeterminado es 443 y se utiliza para el acceso HTTPS seguro al panel de administración web.

- **Force HTTPS**: Cuando está habilitado, el acceso al panel de administración web se fuerza a utilizar una conexión HTTPS segura.

- **Auto-Logout Time**: El valor predeterminado es 5 minutos. Por motivos de seguridad, cierra automáticamente las sesiones de administración inactivas una vez transcurrido ese tiempo. Puede personalizar el tiempo de cierre automático, desde 1 minuto hasta 3 horas.

### LuCI

- **HTTP Port**: El valor predeterminado es 8080 y se usa para el acceso HTTP sin cifrar a la interfaz LuCI.

- **HTTPS Port**: El valor predeterminado es 8443 y se usa para el acceso HTTPS seguro a la interfaz LuCI.

- **Force HTTPS**: Cuando está habilitado, el acceso a la interfaz LuCI se fuerza a utilizar una conexión HTTPS segura.

### SSH

- **Enable SSH**: Controla si se permite el acceso SSH al router. Está habilitado de forma predeterminada.

- **SSH Port**: El valor predeterminado es 22, el puerto utilizado para el acceso SSH al router.

### Puerto prohibido {#prohibited-port}

Si asigna un número de puerto que entra en conflicto con un puerto reservado, o con uno reservado para servicios específicos por los navegadores o las convenciones de red, aparecerá un aviso indicando "This port is forbidden by the browser".

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "Lista de números de puerto prohibidos por el navegador"

    | Port  | Descripción                              |
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

## Control de acceso remoto

Después de habilitar el acceso remoto, se pueden definir ubicaciones específicas desde las que se permitirá el acceso. Por ejemplo, puede habilitar el acceso remoto a dispositivos del hogar solo desde la oficina, sacrificando comodidad a cambio de mayor seguridad.

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: Cuando hay un problema de red, permitir Ping desde el puerto WAN puede ayudar a los usuarios o a los administradores de red a comprobar si el router está conectado correctamente, así como a determinar la latencia y la pérdida de paquetes.

- **HTTPS Remote Access**: El protocolo HTTPS se utiliza principalmente para la comunicación entre navegadores web y servidores web, proporcionando una garantía de transmisión segura de datos. Por tanto, cuando los usuarios necesiten administrar servidores de forma remota o acceder a aplicaciones web desde el navegador, pueden usar HTTPS para garantizar la seguridad y la fiabilidad de la transmisión de datos.

- **SSH Remote Access**: El protocolo SSH se utiliza principalmente para acceder y administrar de forma segura equipos y servidores remotos, así como para realizar operaciones de transferencia de archivos. Cuando los usuarios necesiten iniciar sesión remotamente en servidores mediante líneas de comandos o scripts para administración del sistema, transferencia de archivos u otras operaciones, pueden usar SSH para establecer un túnel seguro que garantice la seguridad y la privacidad de la transmisión de datos.

- **Allow Remote Access from Specific IPs**: Esta función se utiliza junto con **Allow Ping from WAN**, **HTTPS Remote Access** o **SSH Remote Access**. Puede añadir varias direcciones IP específicas para gestionar routers de forma remota desde dispositivos con esas direcciones IP.

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## Open Ports on Router

Los servicios del router, como web y FTP, requieren que sus respectivos puertos estén abiertos en el router para poder ser accesibles públicamente.

Para abrir un puerto, haga clic en **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

**Name:** El nombre de la regla, que puede ser especificado por el usuario.

**Protocol:** El protocolo utilizado. Puede elegir TCP, UDP o ambos, TCP y UDP.

**Port:** El número de puerto que desea abrir.

**Enable:** Habilita o deshabilita la regla.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
