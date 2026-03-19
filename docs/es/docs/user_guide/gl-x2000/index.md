# Spitz Plus (GL-X2000) Guía del usuario

## Descripción general del producto

Spitz Plus (GL-X2000) es una puerta de enlace celular 4G LTE Wi-Fi 6 con doble SIM diseñada para proporcionar conexiones rápidas y fiables, especialmente en zonas remotas y durante viajes por carretera. Con agregación de 3 portadoras, el router transmite datos en tres bandas de operador simultáneamente, proporcionando 3 veces más ancho de banda disponible para evitar la congestión. Ofrece cuatro métodos de acceso a Internet: Cellular (tarjetas SIM), Ethernet, Repeater y Tethering. Es compatible con multi-WAN (failover y balanceo de carga), VPN (OpenVPN y WireGuard), control parental, AdGuard Home, reenvío de puertos, Tailscale y mucho más.

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## Contenido del paquete

- 1 x Spitz Plus (GL-X2000)
- 1 x Manual del usuario
- 4 x Antenas externas
- 1 x Tarjeta de agradecimiento
- 1 x Cable Ethernet
- 1 x Kit de montaje en pared
- 1 x Almohadilla adhesiva
- 4 x Tornillos
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_unboxing.jpg){class="glboxshadow"}

## Indicadores LED

| Estado de funcionamiento                                                      | Power                               | Internet                    | 2.4GHz                      | 5GHz                        | Cellular |
| ----------------------------------------------------------------------------- | ----------------------------------- | --------------------------- | --------------------------- | --------------------------- | -------- |
| Normal (conectado a Internet)                                                 | Green                               | Green                       | Green                       | Green                       | Green    |
| No conectado a Internet                                                       | Green                               | Off                         | Green                       | Green                       | Green    |
| Actualizando firmware                                                         | Green                               | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Blinking green (every 0.5s) | Green    |
| Restableciendo el router (mantenga pulsado el botón "reset" durante > 3 s)   | Blinking green (every 1s)           | Green                       | Green                       | Green                       | Green    |
| Restaurando el router a valores de fábrica (mantenga pulsado "reset" 10 s)   | Fast blinking green (every 0.25s)   | Green                       | Green                       | Green                       | Green    |

## Cómo configurar Spitz Plus

Para configurar Spitz Plus, utilizará uno de los cuatro métodos de conexión a Internet admitidos: Cellular (requiere SIM), Ethernet, Repeater y Tethering. Vea este video de configuración o siga los pasos a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Este video muestra la configuración Cellular de Spitz Plus. Si necesita configurar Spitz Plus mediante otros métodos de conexión a Internet, consulte los pasos siguientes.)</small>

!!! note "Antes de empezar, siga estos pasos (si se conecta mediante el método cellular):"

    Se requiere al menos una tarjeta nano SIM para conectarse a Internet mediante el método cellular. Si ya tiene preparadas las tarjetas nano SIM, siga estos pasos:

    1. Active su(s) tarjeta(s) SIM si así lo requiere el operador.
    2. Apague el router.
    3. Inserte la(s) tarjeta(s) SIM en las ranuras correspondientes. (**Nota:** Solo una tarjeta SIM está activa a la vez. La otra solo funciona como respaldo).

### 1. Encendido

Monte las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. Se iniciará automáticamente.

### 2. Conecte un dispositivo

Conecte un dispositivo (por ejemplo, un ordenador, un portátil o un smartphone) al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

- Wi-Fi

    En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. (Puede encontrar el nombre de red y la contraseña predeterminados impresos en la etiqueta del router).

### 3. Inicie sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones y accederá al panel de administración web de GL.iNet. Elija un idioma y establezca la contraseña de administrador; después, haga clic en **Apply**.

### 4. Configuración de Internet

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router mediante el panel de administración web de GL.iNet. Si prefiere usar la aplicación GL.iNet, [descargue la app](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones en pantalla.

Configure su Spitz Plus usando uno de los métodos de conexión a Internet admitidos: Cellular, Ethernet, Repeater y Tethering. Si desea usar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    Si ya ha insertado la tarjeta SIM en el router, Internet debería conectarse automáticamente. Debería ver el nombre de su operador SIM y un punto verde en la sección Cellular.

    Si no es así, apague el router, vuelva a insertar la tarjeta SIM y enciéndalo de nuevo.

    Consulte [Conectarse a Internet mediante cellular](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models) para ver instrucciones detalladas.

    **Nota**: La función eSIM de Spitz Plus está disponible a partir del firmware v4.7. Aprenda a usar la tarjeta física eSIM en un router GL.iNet [aquí](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

    Si encuentra algún problema, consulte la [Guía de resolución de problemas de red cellular](../../faq/cellular_network_troubleshooting_guide.md).

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}

    Conecte el puerto WAN de Spitz Plus a un dispositivo ascendente (por ejemplo, un módem) mediante un cable Ethernet.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. En la página INTERNET del panel de administración, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi entre las redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Conecte su dispositivo móvil (por ejemplo, un smartphone o un dongle USB) al puerto USB del router mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la pantalla INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

---

A continuación se muestra un resumen de las funciones del panel de administración web de Spitz Plus.

## Wireless

La página Wireless le permite configurar ajustes para las redes Wi-Fi de 5 GHz y 2,4 GHz, incluida la activación o desactivación del Wi-Fi, el ajuste de la potencia TX, la especificación del nombre de la red Wi-Fi (SSID), la activación o desactivación del BSSID aleatorio, la selección del modo de seguridad Wi-Fi, la configuración de la contraseña Wi-Fi, la visibilidad del SSID, el modo Wi-Fi, el ancho de banda y el canal.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

## Clients

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, muestra el nombre del dispositivo, el tipo de conexión (es decir, mediante ethernet o Wi-Fi), las direcciones IP y MAC, las velocidades de descarga y carga, el tráfico total, y ofrece la posibilidad de reservar IP, bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} ofrece una forma sencilla de acceder de forma remota a los routers GL.iNet y administrarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una plataforma de red avanzada diseñada para proporcionar redes remotas sin interrupciones y gestión remota de dispositivos. Diseñada específicamente para integrarse con los routers GL.iNet, AstroWarp admite una gestión integral de dispositivos en redes completas, lo que permite controlar tanto dispositivos superiores como inferiores. Gracias a su enfoque en la gestión de toda la red y al futuro soporte para control a nivel de hardware, AstroWarp ofrece una solución más sólida y fiable para administrar dispositivos y mantener redes seguras y estables.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

    **Nota**: Actualice su Spitz Plus al firmware v4.8 o superior para usar AstroWarp.

## VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad (cliente VPN) y le permite acceder a una red remota (servidor VPN). Spitz Plus es compatible con OpenVPN y WireGuard.

=== "OpenVPN"

    Spitz Plus (y otros routers GL.iNet) es compatible con el protocolo OpenVPN, que ofrece una seguridad sólida. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Spitz Plus (y otros routers GL.iNet) es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Aplicaciones

=== "Plug-ins"

    Un complemento es un componente de software que añade funciones o características específicas a un programa existente, lo que permite personalizarlo y ampliar sus capacidades.

    Para configurar complementos, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta útil para usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    El almacenamiento en red hace referencia a una solución centralizada de almacenamiento de datos que permite a varios usuarios y dispositivos acceder a archivos y compartirlos a través de una red.

    Para configurar el almacenamiento en red, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una herramienta de terceros que bloquea anuncios y rastreo para mantenerle protegido. Para aprender a activar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    El control parental es un conjunto de ajustes diseñado para ayudarle a administrar y controlar los dispositivos de sus hijos. Incluye limitar su tiempo de pantalla y restringir el acceso a determinados contenidos. Spitz Plus ofrece dos opciones de control parental: la versión local desarrollada por GL.iNet y la versión integrada de Bark, una aplicación de control parental.

    Para configurar el control parental, consulte [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Spitz Plus es compatible con Tailscale a partir del firmware v4.7.

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM"

    Spitz Plus es compatible con la función eSIM a partir del firmware v4.7.

    Para aprender a configurar y gestionar eSIM en su dispositivo, consulte [este tutorial](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Red

=== "Port forwarding"

    El reenvío de puertos permite que servidores y dispositivos remotos en Internet accedan a dispositivos dentro de una red privada. Para configurar el reenvío de puertos, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet (por ejemplo, cellular, repeater y ethernet) al mismo tiempo. Si la conexión a Internet actual falla, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o red de área local, es una red que conecta ordenadores y dispositivos dentro de un área geográfica limitada, como una casa u oficina. Permite transferencias de datos a alta velocidad y el uso compartido de recursos, lo que facilita que los dispositivos se comuniquen entre sí de forma eficiente.

    Para configurar LAN, consulte [Lan Tutorial](../../interface_guide/lan.md).

---

=== "Guest Network"

    Le permite establecer una subred dentro de los rangos de direcciones privadas IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, especificar las direcciones IP de gateway y máscara de red, y configurar ajustes de seguridad como el aislamiento de AP para la red de invitados.

    Para configurar la red de invitados, consulte [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección contra ataques de DNS rebinding y sobrescribir la configuración DNS de todos los clientes, permitir que el DNS personalizado anule el DNS de la VPN, y configurar el modo de ajustes del servidor DNS para que sea automático o para especificar manualmente los servidores DNS de la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "Port Management"

    La página Port Management le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC para la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para administrar los puertos Ethernet, consulte [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    El modo de red hace referencia a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurar el modo de red, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Protocolo de Internet versión 6, es la versión más reciente del Protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones mucho mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad de su router principal con funciones que quizá no tenga, incluidas AdGuard Home, DNS cifrado y VPN. Para configurar drop-in gateway, consulte [Cómo configurar drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para configurar IGMP snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    La aceleración de red hace referencia al uso de componentes de hardware especializados para realizar tareas específicas de forma más eficiente que las CPU de propósito general.

    Para configurar la aceleración de red, consulte este tutorial de [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La página NAT Settings le permite activar o desactivar las funciones Full Cone NAT y SIP ALG (Application Layer Gateway).

    Para configurar los ajustes NAT, consulte [NAT Settings](../../interface_guide/nat_settings.md).

## Sistema

=== "Overview"

    La página Overview ofrece una visión general completa del estado actual y de las métricas de rendimiento de su router. En esta página puede ver:

    * Carga media de CPU: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Uso de memoria: compruebe cuánta memoria del router está en uso para facilitar la gestión de recursos.
    * Control LED: active o desactive las luces LED del router para personalizar los indicadores visuales del dispositivo.
    * Uso de flash: vea el uso del almacenamiento flash del router para asegurarse de que haya suficiente espacio para el firmware y los datos de configuración.
    * Información del dispositivo: acceda a información detallada del sistema del router, incluidos el tiempo de actividad, el nombre de host, el modelo, la arquitectura, la versión de OpenWrt, la versión del kernel, el ID del dispositivo, la MAC del dispositivo y el número de serie.
    * Almacenamiento externo: consulte el estado de los dispositivos de almacenamiento externo conectados al router, como unidades USB o tarjetas TF.

    Estas funciones le proporcionan información esencial y controles útiles para administrar y supervisar eficazmente el funcionamiento del router.

    Consulte [Overview](../../interface_guide/system_overview.md){target="_blank"} para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, lo que garantiza mejor rendimiento, mayor seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: compruebe e instale automáticamente la versión más reciente del firmware directamente desde el servidor del fabricante, lo que simplifica el proceso de actualización.
    * Firmware Local Upgrade: cargue manualmente un archivo de firmware desde su ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.
    * Module Online Upgrade: compruebe e instale automáticamente la versión más reciente del módulo 4G/5G directamente desde el servidor del fabricante, lo que simplifica el proceso de actualización.
    * Module Local Upgrade: cargue manualmente un archivo del módulo desde su ordenador para actualizar el módulo 4G/5G.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Consulte [Upgrade](../../interface_guide/upgrade.md){target="_blank"} para ver instrucciones detalladas.

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar diversas funciones del router según un horario predefinido, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de la pantalla LED: establezca un horario para encender o apagar automáticamente las luces LED del router y reducir la contaminación lumínica en determinados momentos.
    * Reinicio programado: configure el router para que se reinicie automáticamente a intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi: establezca un horario para controlar la banda Wi-Fi de 5 GHz / 2,4 GHz, lo que permite gestionar mejor la disponibilidad de la red y el consumo de energía.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router y garantizan que se adapte a sus necesidades y preferencias específicas.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"} para ver instrucciones detalladas.

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Este ajuste es fundamental para mantener registros exactos y para el correcto funcionamiento de las configuraciones basadas en el tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md){target="_blank"} para ver instrucciones detalladas.

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que ayuda a la resolución de problemas y a la supervisión del rendimiento. Esta página incluye:

    * Registro del sistema: registros detallados de eventos y actividades a nivel del sistema.
    * Registro del kernel: registros relacionados con las operaciones y eventos del kernel.
    * Registro de fallos: registros de bloqueos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Registro de la nube: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Registro de Nginx: registros del servidor web Nginx, si el router lo utiliza, con detalles sobre el tráfico web y las operaciones del servidor.

    Además, la página incluye un botón Export Log que le permite exportar todos los registros recopilados para su análisis por parte del soporte técnico. Esta función es muy útil para diagnosticar problemas complejos y obtener ayuda profesional.

    Consulte [Log](../../interface_guide/log.md){target="_blank"} para ver instrucciones detalladas.

=== "Security"

    La página Security le permite configurar varios ajustes de seguridad para proteger su red y su router frente a accesos no autorizados. Esta página incluye opciones para:

    * Admin Password: establecer o cambiar la contraseña de la interfaz administrativa del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.
    * Local Access Control: administrar y restringir el acceso a la interfaz del router desde dispositivos conectados a su red local.
    * Remote Access Control: configurar y restringir el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controlar qué puertos están abiertos en el router para limitar posibles vulnerabilidades y accesos no autorizados.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

---

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a sus ajustes predeterminados, eliminando todas las configuraciones personalizadas. Este proceso restaurará el router a los ajustes predeterminados de la versión de firmware instalada actualmente. Puede resultar útil para solucionar problemas persistentes o para empezar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"} para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings ofrece acceso a opciones de configuración avanzada a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios con experiencia ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Para obtener instrucciones detalladas e información adicional, consulte [Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}.
