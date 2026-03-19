# Guía de usuario de Brume 2 (GL-MT2500/GL-MT2500A)

## Descripción general del producto

Brume 2 (GL-MT2500/GL-MT2500A) es una pasarela VPN ligera y potente que ejecuta el sistema operativo OpenWrt v21.02. Su diseño compacto permite alojar un servidor VPN en casa o ejecutar SD-WAN (Site-to-Site) para pequeñas y medianas empresas.

![gl-mt2500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

## Contenido del paquete

- 1 x Brume 2 (GL-MT2500/GL-MT2500A)
- 1 x Manual del usuario
- 1 x Cable Ethernet
- 1 x Tarjeta de agradecimiento
- 1 x Tarjeta de garantía
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

La siguiente imagen muestra el GL-MT2500A como ejemplo.

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

## Cómo configurar Brume 2

Para configurar Brume 2, puede usar uno de los métodos de conexión a Internet compatibles: Ethernet, Tethering y Cellular. Repeater no es compatible porque Brume 2 no dispone de módulo Wi-Fi. Vea este vídeo de configuración o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rpi_loOwUQM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encender

Ensamble las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. El router se iniciará automáticamente.

### 2. Conectar un dispositivo

Conecte su dispositivo, por ejemplo un ordenador o un portátil, al puerto LAN del router mediante un cable Ethernet.

### 3. Iniciar sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma, establezca la contraseña de administrador y haga clic en **Apply**.

### 4. Configuración de Internet

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}

    Conecte un cable ethernet entre el puerto WAN del router y un dispositivo aguas arriba, como un módem.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB del router mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del router. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Conectarse a Internet mediante conexión celular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

**Nota:** Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de un método de conexión a Internet.

## Cómo configurar una VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad cuando se usa como cliente VPN y permite acceder a una red remota cuando se usa como servidor VPN. Brume 2, al igual que otros routers GL.iNet, es compatible con OpenVPN y WireGuard. Además, también es compatible con Tor.

=== "OpenVPN"

    Brume 2, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 2, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico de Internet a través de una serie de servidores operados por voluntarios (nodos) para ocultar la ubicación y el uso del usuario, lo que dificulta el rastreo de la actividad en línea.

    * [Cómo configurar Tor](../../interface_guide/tor.md).

## Clients

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, se muestra el nombre del dispositivo, las direcciones IP y MAC, las velocidades de descarga y subida, el tráfico total, y ofrece la posibilidad de reservar IP, bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    El servicio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} proporciona una forma sencilla de acceder de forma remota a los routers GL.iNet y gestionarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una plataforma de red avanzada diseñada para ofrecer redes remotas y gestión remota de dispositivos sin interrupciones. Creada específicamente para integrarse con routers GL.iNet, AstroWarp admite una gestión integral de dispositivos en redes completas, lo que permite controlar tanto los dispositivos superiores como los inferiores. Con un enfoque centrado en la gestión de toda la red y compatibilidad futura con control a nivel de hardware, AstroWarp ofrece una solución más sólida y fiable para gestionar dispositivos y mantener redes seguras y estables.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

## Aplicaciones

=== "Plug-ins"

    Un plugin es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo personalizarlo y ampliar sus capacidades.

    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta útil para los usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage se refiere a una solución de almacenamiento de datos centralizada que permite que varios usuarios y dispositivos accedan a archivos y los compartan a través de una red.

    Para configurar Network Storage, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores para toda la red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a una red doméstica.

    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental control es un conjunto de ajustes diseñado para ayudarle a gestionar y controlar los dispositivos de sus hijos. Incluye la limitación del tiempo de pantalla y la restricción del acceso a determinados contenidos. Brume 2 ofrece dos opciones de control parental: la versión local desarrollada por GL.iNet y la versión integrada de Bark, una aplicación de control parental.

    Para configurar el control parental, consulte [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

## Configuración de red

=== "Port forwarding"

    Port forwarding permite que servidores remotos y dispositivos de Internet accedan a dispositivos de una red privada. Para configurar el reenvío de puertos, consulte [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, es una red que conecta ordenadores y dispositivos dentro de un área geográfica limitada, como una vivienda u oficina. Permite transferencias de datos de alta velocidad y compartir recursos, lo que hace posible que los dispositivos se comuniquen entre sí de forma eficiente.

    Para configurar LAN, consulte [Lan Tutorial](../../interface_guide/lan.md).

---

=== "Guest Network"

    Le permite establecer una subred dentro de los rangos de direcciones privadas IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, especificar las direcciones IP de puerta de enlace y máscara de red, y configurar ajustes de seguridad como el aislamiento AP para la red de invitados.

    Para configurar Guest Network, consulte [Lan Tutorial](../../interface_guide/guest_network.md).

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección frente a ataques de DNS rebinding y sobrescribir los ajustes DNS de todos los clientes, permitir que el DNS personalizado reemplace al DNS de la VPN, y configurar el modo de ajustes del servidor DNS como automático o especificar manualmente servidores DNS desde la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "Network Port Management"

    La página Network Port Management le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC de la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

---

=== "Network Mode"

    Network mode se refiere a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurar Network Mode, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, es la versión más reciente del protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones muchísimo mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad del router principal con funciones que quizá no tenga, como AdGuard Home, DNS cifrado y VPN.

    Para configurar drop-in gateway, consulte [Cómo configurar drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para configurar IGMP Snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Hardware acceleration se refiere al uso de componentes de hardware especializados para realizar tareas concretas con mayor eficiencia que una CPU de propósito general.

    Para configurar la aceleración de red, consulte este tutorial de [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La página NAT Settings le permite activar o desactivar la funcionalidad Full Cone NAT y SIP ALG (Application Layer Gateway).

    Para configurar NAT Settings, consulte [NAT Settings](../../interface_guide/nat_settings.md).

## Configuración del sistema

=== "Overview"

    La página Overview ofrece una vista general completa del estado actual del router y de sus métricas de rendimiento. En esta página puede ver:

    * Carga media de la CPU: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Uso de memoria: compruebe cuánta memoria del router está en uso para ayudar a gestionar los recursos.
    * Control LED: active o desactive los LED del router para personalizar los indicadores visuales del dispositivo.
    * Uso de almacenamiento flash: vea el uso del almacenamiento flash del router para asegurarse de que hay espacio suficiente para el firmware y los datos de configuración.
    * Información del dispositivo: acceda a información detallada sobre el sistema del router, como tiempo de actividad, nombre del host, modelo, arquitectura, versión de OpenWrt, versión del kernel, ID del dispositivo, MAC del dispositivo y S/N del dispositivo.
    * Almacenamiento externo: compruebe el estado de los dispositivos de almacenamiento externo conectados al router, como unidades USB o tarjetas TF.

    Estas funciones proporcionan información y controles esenciales para ayudarle a gestionar y supervisar el funcionamiento del router de forma eficaz.

    Consulte [Overview](../../interface_guide/system_overview.md) para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: comprueba automáticamente si hay una nueva versión de firmware y la instala directamente desde el servidor del fabricante, simplificando el proceso.
    * Firmware Local Upgrade: permite cargar manualmente un archivo de firmware desde el ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de visualización LED: establezca un horario para encender o apagar automáticamente los LED del router y reducir la contaminación lumínica en determinadas horas.
    * Reinicio programado: configure el router para que se reinicie automáticamente en intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, asegurando que se adapte a sus necesidades y preferencias.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Este ajuste es fundamental para mantener registros exactos y para la correcta ejecución de las configuraciones basadas en el tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que facilita la resolución de problemas y la supervisión del rendimiento. Esta página incluye:

    * System Log: registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: registros relacionados con las operaciones y eventos del kernel.
    * Crash Log: registros de fallos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Cloud Log: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Nginx Log: registros del servidor web Nginx, si se utiliza en el router, que detallan el tráfico web y las operaciones del servidor.

    Además, la página incluye un botón Export Log, que le permite exportar todos los registros recopilados para su análisis por parte del soporte técnico. Esta función es muy valiosa para diagnosticar problemas complejos y obtener asistencia profesional.

    Consulte [Log](../../interface_guide/log.md) para ver instrucciones detalladas.

=== "Security"

    La página Security le permite configurar varios ajustes de seguridad para proteger la red y el router frente a accesos no autorizados. Esta página incluye opciones para:

    * Admin Password: establecer o cambiar la contraseña de la interfaz de administración del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.
    * Local Access Control: gestionar y restringir el acceso a la interfaz del router desde dispositivos conectados a la red local.
    * Remote Access Control: configurar y restringir el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controlar qué puertos están abiertos en el router, limitando posibles vulnerabilidades y accesos no autorizados.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

---

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware instalada en ese momento. Puede resultar útil para solucionar problemas persistentes o para comenzar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings ofrece acceso a opciones de configuración avanzada a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios con experiencia ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas de la interfaz. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para ver instrucciones detalladas.

