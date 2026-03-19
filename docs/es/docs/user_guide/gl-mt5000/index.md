# Brume 3 (GL-MT5000) Guía del usuario

## Descripción general del producto

Brume 3 (GL-MT5000) es una puerta de enlace de seguridad de alto rendimiento que ejecuta OpenWrt v21.02, equipada con una CPU MediaTek Cortex-A53 de cuatro núcleos, 1 GB de RAM y 8 GB de almacenamiento eMMC para ampliar complementos. Tiene un diseño compacto, ideal para implementaciones con espacio limitado, y admite alojamiento VPN doméstico, SD-WAN site-to-site, así como más de 30 servicios VPN para una conectividad segura entre ubicaciones. Además, incorpora la función DPI de GL.iNet, así como Control parental y AdGuard Home, para cubrir las distintas necesidades de entusiastas de la tecnología y usuarios empresariales.

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## Contenido del paquete

- 1 x Brume 3 (GL-MT5000)
- 1 x Adaptador de corriente
- 1 x Cable Ethernet
- 1 x Manual del usuario
- 1 x Tarjeta de agradecimiento
- 1 x Convertidor (según el país de envío)

Vea a continuación el video de unboxing de Brume 3.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cómo configurar Brume 3

Vea este video de configuración o siga los pasos a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwbdUy79WHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encendido

Monte las dos piezas del adaptador de corriente. Conéctelo a su Brume 3 y enchúfelo a una toma de corriente. Se iniciará automáticamente.

### 2. Conecte un dispositivo

Conecte un dispositivo con cable (por ejemplo, un ordenador o un portátil) al puerto LAN de Brume 3 mediante un cable Ethernet.

### 3. Inicie sesión en el panel de administración web

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router mediante el panel de administración web de GL.iNet.

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma y establezca la contraseña de administrador; después, haga clic en **Apply**.

### 4. Configuración de Internet

Configure su Brume 3 usando uno de los métodos de conexión a Internet admitidos: Ethernet, Tethering y Cellular (opcional). Si desea usar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Conecte el puerto WAN de Brume 3 a un dispositivo ascendente (como un módem) mediante un cable Ethernet.

    Cuando Brume 3 se conecte correctamente a Internet, aparecerá un punto verde junto a "Ethernet" en la página INTERNET del panel de administración web y el LED físico de Brume 3 se iluminará en blanco fijo.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil al puerto USB Type-C de Brume 3 mediante un cable de datos USB 3.0.
    2. En la configuración de su dispositivo móvil, active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección "Tethering".

    Cuando Brume 3 se conecte correctamente a Internet, aparecerá un punto verde junto a "Tethering" en la página INTERNET del panel de administración web y el LED físico de Brume 3 se iluminará en blanco fijo.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    Para este método de conexión se requiere un cable adaptador USB-C a USB-A adicional.

    Conecte un módem USB celular al puerto USB Type-C de Brume 3 mediante un cable adaptador USB-C a USB-A adicional. Esto resulta útil para compartir Internet desde un módem USB con todos los dispositivos cliente conectados.

    Cuando Brume 3 se conecte correctamente a Internet, aparecerá un punto verde junto a "Cellular" en la página INTERNET del panel de administración web y el LED físico de Brume 3 se iluminará en blanco fijo.

    Consulte [Conectarse a Internet mediante cellular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

---

A continuación se muestra un resumen de las funciones del panel de administración web de Brume 3.

## Clients

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y carga, el tráfico total, y ofrece la posibilidad de bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    El servicio de gestión en la nube GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} ofrece una forma sencilla de acceder de forma remota a los routers GL.iNet y administrarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una plataforma de red avanzada diseñada para proporcionar redes remotas sin interrupciones y gestión remota de dispositivos. Diseñada específicamente para integrarse con los routers GL.iNet, AstroWarp admite una gestión integral de dispositivos en redes completas, lo que permite controlar tanto dispositivos superiores como inferiores. Gracias a su enfoque en la gestión de toda la red y al futuro soporte para control a nivel de hardware, AstroWarp ofrece una solución más sólida y fiable para administrar dispositivos y mantener redes seguras y estables.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad (cliente VPN) y le permite acceder a una red remota (servidor VPN). Brume 3 es compatible con OpenVPN y WireGuard.

=== "OpenVPN"

    Brume 3 (y otros routers GL.iNet) es compatible con el protocolo OpenVPN, que ofrece una seguridad sólida. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 3 (y otros routers GL.iNet) es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Red

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet (por ejemplo, cellular, repeater y ethernet) al mismo tiempo. Si la conexión a Internet actual falla, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o red de área local, es una red que conecta ordenadores y dispositivos dentro de un área geográfica limitada, como una casa u oficina. Permite transferencias de datos a alta velocidad y el uso compartido de recursos, lo que facilita que los dispositivos se comuniquen entre sí de forma eficiente.

    Para configurar LAN, consulte [Lan](../../interface_guide/lan.md).

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección contra ataques de DNS rebinding y sobrescribir la configuración DNS de todos los clientes, permitir que el DNS personalizado anule el DNS de la VPN, y configurar el modo de ajustes del servidor DNS para que sea automático o para especificar manualmente los servidores DNS de la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

---

=== "Ethernet Port"

    La página Ethernet Port le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC para la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para administrar los puertos Ethernet, consulte [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, o Protocolo de Internet versión 6, es la versión más reciente del Protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones mucho mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para configurar IGMP snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    El modo de red hace referencia a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurar el modo de red, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in gateway amplía las funciones de su router principal, incluidas AdGuard Home, DNS cifrado y cliente VPN.

    Para configurar Drop-in gateway, consulte estos enlaces:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Cómo configurar drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    La aceleración de red puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.

    Para configurar la aceleración de red, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Control de flujo

=== "DPI License"

    DPI (Deep Packet Inspection) es una capacidad central de la gestión inteligente de redes. Puede superar la limitación de los routers tradicionales (que solo identifican direcciones de origen o destino), analizar en profundidad la carga útil de los paquetes de datos e identificar con precisión las aplicaciones y los sitios web a los que accede el usuario mediante la comparación con bibliotecas de firmas, lo que permite una clasificación y un control del tráfico más detallados.

    Integrada con [Netify](https://www.netify.ai/){target="_blank"}, la función DPI de GL.iNet adopta un complemento integrado ligero para un despliegue eficiente. Con la base de datos de firmas de Netify actualizada en línea, permite una gestión fiable y hace que el control de red sea más preciso y eficiente.

    Consulte [DPI License](../../interface_guide/dpi_license.md) para ver instrucciones detalladas.

=== "Data Statistics"

    Data Statistics ofrece un panel inteligente de análisis de tráfico que clasifica y visualiza el uso de la red por aplicaciones, lo que le ayuda a supervisar el tráfico en tiempo real e histórico para lograr una mejor visibilidad y control de la red.

    Consulte [Data Statistics](../../interface_guide/data_statistics.md) para ver instrucciones detalladas.

=== "Content Filter"

    Content Filter proporciona seguridad inteligente en línea mediante clasificación basada en DPI y bloquea automáticamente sitios web dañinos o maliciosos para mantener su red limpia y segura.

    Consulte [Content Filter](../../interface_guide/content_filter.md) para ver instrucciones detalladas.

---

=== "Parental Control"

    Parental Control está diseñado para ayudarle a administrar y controlar los dispositivos de sus hijos. Incluye limitar el tiempo de pantalla y restringir el acceso a determinados contenidos.

    Para configurar el control parental, consulte [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) optimiza la asignación del ancho de banda al priorizar actividades críticas (por ejemplo, videollamadas o juegos) durante la congestión de la red, reduciendo la latencia y mejorando el rendimiento general. Tenga en cuenta que esto se aplica al tráfico de clientes locales y al tráfico del túnel de cliente VPN, pero no al tráfico recibido cuando el router funciona como servidor VPN.

    Consulte [QoS](../../interface_guide/qos.md) para ver instrucciones detalladas.

=== "SQM"

    SQM (Smart Queue Management) gestiona de forma inteligente el tráfico de red del router para minimizar la latencia y el "bufferbloat", garantizando una experiencia más fluida en juegos y llamadas de voz.

    Consulte [SQM](../../interface_guide/sqm.md) para ver instrucciones detalladas.

## Seguridad

=== "Port Forwarding"

    El reenvío de puertos permite que servidores y dispositivos remotos en Internet accedan a dispositivos dentro de una red privada.

    Para configurar el reenvío de puertos, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Management Control le permite configurar varios ajustes de seguridad para proteger su red y su router frente a accesos no autorizados. Esta página incluye las siguientes opciones:

    * Local Access Control: administre y restrinja el acceso a la interfaz del router desde dispositivos conectados a su red local.
    * Remote Access Control: configure y restrinja el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controle qué puertos están abiertos en el router para limitar posibles vulnerabilidades y accesos no autorizados.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

=== "NAT Mode"

    La página NAT Mode le permite activar o desactivar las funciones Full Cone NAT y SIP ALG (Application Layer Gateway).

    Para configurar los ajustes NAT, consulte [NAT Mode](../../interface_guide/nat_settings.md).

## Aplicaciones

=== "Plug-ins"

    Un complemento es un componente de software que añade funciones o características específicas a un programa existente, lo que permite personalizarlo y ampliar sus capacidades.

    Para configurar complementos, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta especialmente útil para usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    El almacenamiento en red hace referencia a una solución centralizada de almacenamiento de datos que permite a varios usuarios y dispositivos acceder a archivos y compartirlos a través de una red.

    Para configurar el almacenamiento en red, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores para toda la red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a una red doméstica.

    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima por Internet. Encamina el tráfico de Internet a través de una serie de servidores operados por voluntarios (nodos) para ocultar la ubicación y el uso del usuario, lo que dificulta rastrear sus actividades en línea.

    * [Cómo configurar Tor](../../interface_guide/tor.md)

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

    Para obtener instrucciones detalladas e información adicional, consulte [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La página Admin Password le permite establecer o cambiar la contraseña de la interfaz administrativa del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.

    Por motivos de seguridad, le recomendamos activar **Prevent Weak Password**.

    Cuando **Prevent Weak Password** está activado, los requisitos para las nuevas contraseñas son los siguientes.

    * 5 caracteres como mínimo y 63 caracteres como máximo.
    * Se permiten letras (distinguiendo mayúsculas y minúsculas), números y símbolos `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Se requieren al menos dos de estos tipos: letras mayúsculas, letras minúsculas, números y símbolos.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, lo que garantiza mejor rendimiento, mayor seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: compruebe e instale automáticamente la versión más reciente del firmware directamente desde el servidor del fabricante, lo que simplifica el proceso de actualización.
    * Firmware Local Upgrade: cargue manualmente un archivo de firmware desde su ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Para obtener instrucciones detalladas e información adicional, consulte [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar diversas funciones del router según un horario predefinido, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de la pantalla LED: establezca un horario para encender o apagar automáticamente las luces LED del router y reducir la contaminación lumínica en determinados momentos.
    * Reinicio programado: configure el router para que se reinicie automáticamente a intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router y garantizan que se adapte a sus necesidades y preferencias específicas.

    Para obtener instrucciones detalladas e información adicional, consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Este ajuste es fundamental para mantener registros exactos y para el correcto funcionamiento de las configuraciones basadas en el tiempo.

    Para obtener instrucciones detalladas e información adicional, consulte [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que ayuda a la resolución de problemas y a la supervisión del rendimiento. Esta página incluye:

    * Registro del sistema: registros detallados de eventos y actividades a nivel del sistema.
    * Registro del kernel: registros relacionados con las operaciones y eventos del kernel.
    * Registro de fallos: registros de bloqueos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Registro de la nube: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Registro de Nginx: registros del servidor web Nginx, si el router lo utiliza, con detalles sobre el tráfico web y las operaciones del servidor.

    Además, la página incluye un botón Export Log que le permite exportar todos los registros recopilados para su análisis por parte del soporte técnico. Esta función es muy útil para diagnosticar problemas complejos y obtener ayuda profesional.

    Para obtener instrucciones detalladas e información adicional, consulte [Log](../../interface_guide/log.md).

---

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a sus ajustes predeterminados, eliminando todas las configuraciones personalizadas. Este proceso restaurará el router a los ajustes predeterminados de la versión de firmware instalada actualmente. Puede resultar útil para solucionar problemas persistentes o para empezar de nuevo con la configuración predeterminada del firmware actual.

    Para obtener instrucciones detalladas e información adicional, consulte [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La página Advanced Settings ofrece acceso a opciones de configuración avanzada a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios con experiencia ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Para obtener instrucciones detalladas e información adicional, consulte [Advanced Settings](../../interface_guide/advanced_settings.md).
