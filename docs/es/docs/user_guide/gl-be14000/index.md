# Guía del usuario de Flint 4 (GL-BE14000)

## Descripción general del producto

Flint 4 (GL‑BE14000) redefine las posibilidades de un router doméstico. Incorpora Wi-Fi 7 tribanda con MLO y ofrece velocidades máximas de 688 Mbps (2,4 GHz) + 4323 Mbps (5 GHz) + 8646 Mbps (6 GHz). Para las conexiones por cable, dispone de una completa infraestructura multigigabit formada por un puerto WAN/LAN SFP+ de 10G, un puerto WAN/LAN 10GE, un puerto WAN/LAN 2.5GE, tres puertos LAN 2.5GE y cuatro puertos LAN 1GE. Gracias a su VPN de alto rendimiento, alcanza un caudal de hasta 1,5 Gbps tanto con WireGuard® como con OpenVPN DCO. También incorpora una pantalla táctil de 2,4 pulgadas que permite supervisar el estado de la red en tiempo real y consultar directamente en el dispositivo las métricas principales.

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## Contenido del paquete

- 1 x Flint 4 (GL-BE14000)
- 1 x Adaptador de corriente
- 1 x Cable Ethernet
- 1 x Manual del usuario
- 1 x Tarjeta de agradecimiento
- 1 x Convertidor (según el país de destino)

Vea a continuación el vídeo de unboxing de Flint 4.

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cómo configurar Flint 4

Vea este vídeo de configuración o siga los pasos que aparecen a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encender

Monte las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. Se iniciará automáticamente.

### 2. Conectar un dispositivo

Conecte un dispositivo (por ejemplo, ordenador, portátil o smartphone) al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte el dispositivo al puerto LAN del router con un cable Ethernet.

- Wi-Fi

    En su dispositivo, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña para unirse a la red. Puede encontrar el nombre de red (SSID) y la contraseña predeterminados impresos en la etiqueta del router.

### 3. Inicie sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Configure la contraseña de administrador y los ajustes de Wi-Fi; después haga clic en **Apply**.

### 4. Configuración de Internet

Configure Flint 4 mediante uno de los métodos de conexión a Internet compatibles: Ethernet (SFP+), Ethernet (RJ45), Repeater, Tethering y Cellular. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}

    Flint 4 dispone de un puerto WAN/LAN SFP+ de 10G diseñado para enlaces ascendentes de fibra, backhaul de switches de alta velocidad y ampliaciones de red de alto rendimiento. Este puerto está configurado como WAN de forma predeterminada y puede cambiarse a LAN cuando sea necesario.

    El siguiente ejemplo muestra cómo conectar el puerto SFP+ de 10G de Flint 4 a un enlace ascendente de fibra del proveedor mediante un transceptor óptico y un cable de fibra para acceder a Internet. Consulte [Conectar el puerto SFP+ de 10G de Flint 4](../../faq/connecting_10g_sfp_plus_port_on_flint4.md) para conocer otras soluciones.

    1. Inserte un transceptor SFP+ de 10G compatible en el puerto SFP+ de Flint 4 y conéctelo al enlace ascendente de fibra de su proveedor de Internet.
    2. Flint 4 intentará obtener automáticamente mediante DHCP los parámetros de red (dirección IP, puerta de enlace y DNS). Si su proveedor requiere PPPoE o una dirección IP estática, ajuste la configuración de la conexión WAN en el panel de administración web.
    3. Cuando se conecte correctamente a Internet, la sección Ethernet de la pantalla de inicio se pondrá azul (activa). Puede tocar Ethernet en la pantalla táctil o iniciar sesión en el panel de administración web para consultar los detalles de la conexión.

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}

    1. Conecte el puerto WAN de Flint 4 a un dispositivo ascendente, por ejemplo un módem del proveedor, un switch de red o una toma Ethernet de pared, mediante un cable Ethernet.
    2. Flint 4 intentará obtener automáticamente mediante DHCP los parámetros de red (dirección IP, puerta de enlace y DNS). Si su proveedor requiere PPPoE o una dirección IP estática, ajuste la configuración de la conexión WAN en el panel de administración web.
    3. Cuando se conecte correctamente a Internet, la sección Ethernet de la pantalla de inicio se pondrá azul (activa). Puede tocar Ethernet en la pantalla táctil o iniciar sesión en el panel de administración web para comprobar los detalles de la conexión.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. Toque **Repeater** en la pantalla táctil. Empezará a buscar redes Wi-Fi disponibles.
    2. Seleccione la red Wi-Fi que desea ampliar con Flint 4.
    3. Introduzca la contraseña y toque **Apply**.
    4. Cuando se conecte correctamente a Internet, la sección Repeater de la pantalla de inicio se pondrá azul (activa). Puede tocar Repeater en la pantalla táctil o iniciar sesión en el panel de administración web para comprobar los detalles de la conexión.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. Conecte un dispositivo móvil, por ejemplo un smartphone, al puerto USB de Flint 4 mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active **USB Tethering** o **Personal Hotspot**. Si usa iPhone, pulse **Trust This Device** si se lo solicita.
    3. En la pantalla táctil de Flint 4, seleccione **Tethering** y pulse **Connect**. El router se conectará a su dispositivo.
    4. Cuando se conecte correctamente a Internet, la sección Tethering de la pantalla de inicio se pondrá azul (activa). Puede tocar Tethering en la pantalla táctil o iniciar sesión en el panel de administración web para comprobar los detalles de la conexión.

    **Nota**: Si la conexión falla, asegúrese de que la fuente de alimentación sea de 12V 4A, ya que una potencia insuficiente puede impedir que el puerto USB reciba alimentación. Repita los pasos anteriores o inicie sesión en el panel de administración web para comprobar el estado de la conexión Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. Conecte un módem celular o un dongle USB al puerto USB de Flint 4. Esto permite compartir la conexión a Internet de un módem USB con todos los dispositivos conectados.
    2. Cuando se conecte correctamente a Internet, la sección Cellular de la pantalla de inicio se pondrá azul (activa). Puede tocar Cellular en la pantalla táctil o iniciar sesión en el panel de administración web para comprobar los detalles de la conexión.

---

A continuación se ofrece una visión general de las funciones del panel de administración web de Flint 4.

## Wireless

La página Wireless permite configurar las distintas redes Wi-Fi de Flint 4, incluidas MLO Wi-Fi, Main Network, Guest Network e IoT Network.

Para obtener más información, consulte [Wireless](../../interface_guide/wireless.md).

## Clients

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y carga, el tráfico total, y ofrece la posibilidad de bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} proporciona una forma sencilla de acceder de forma remota a los routers GL.iNet y gestionarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una función de red avanzada integrada en los routers GL.iNet. Permite acceder de forma remota y sin interrupciones a su red doméstica sin necesidad de registrarse ni iniciar sesión. Gracias al protocolo AmneziaWG con ofuscación de tráfico integrada, mantiene la conexión estable y segura, por lo que resulta ideal para un acceso remoto fiable desde cualquier lugar. Los usuarios pueden configurar una red AstroWarp directamente desde el panel de administración del router GL.iNet. Solo tiene que emparejar sus routers con un código de acceso y podrá conectar de forma segura su router de viaje a su red doméstica en cuestión de segundos.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN, red privada virtual, crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad, cliente VPN, y le permite acceder a una red remota, servidor VPN. Flint 4 es compatible con los protocolos OpenVPN y WireGuard.

=== "OpenVPN"

    Flint 4, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    La página Subnet centraliza la administración de LAN, Guest Network, IoT Network y las redes VLAN personalizadas. Permite crear y administrar varias subredes para aislar distintos tipos de dispositivos o tráfico.

    Para obtener más información, consulte [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La página Ethernet Port permite administrar la función de los puertos Ethernet (WAN/LAN) y la segmentación VLAN, así como consultar detalles como la dirección MAC y la velocidad negociada.

    Para obtener más información, consulte [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección frente a ataques de DNS rebinding y sobrescribir los ajustes DNS de todos los clientes, permitir que el DNS personalizado reemplace al DNS de la VPN, y configurar el modo de ajustes del servidor DNS como automático o especificar manualmente servidores DNS desde la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, abreviatura de Internet Protocol version 6, es la versión más reciente del protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones muchísimo mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para obtener más información, consulte [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para obtener más información, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Network Mode se refiere a las distintas funciones y modos de funcionamiento que puede asumir un router para satisfacer diferentes necesidades de implementación. Entre los modos habituales se incluyen el modo router, el modo extensor y el modo de punto de acceso.

    Para configurar Network Mode, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway es una función flexible que permite ampliar las capacidades de un router principal existente sin sustituirlo ni volver a configurarlo. Al establecer un router GL.iNet como Drop-in Gateway, puede incorporar a la infraestructura existente funciones avanzadas como AdGuard Home, VPN y DNS cifrado.

    Para configurar drop-in gateway, consulte estos enlaces:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Cómo configurar Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.

    Para configurar la aceleración de red, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Control de flujo

=== "DPI Engine"

    DPI, Deep Packet Inspection, es una capacidad central de la gestión inteligente de redes. Puede superar la limitación de los routers tradicionales, que solo identifican direcciones de origen o destino, analizar en profundidad la carga útil de los paquetes de datos e identificar con precisión las aplicaciones y sitios web a los que accede el usuario mediante la comparación con bibliotecas de firmas, lo que permite una clasificación y un control del tráfico más detallados.

    Integrada con [Netify](https://www.netify.ai/){target="_blank"}, la función DPI de GL.iNet adopta un complemento integrado ligero para un despliegue eficiente. Con la base de datos de firmas de Netify actualizada en línea, permite una gestión fiable y hace que el control de red sea más preciso y eficiente.

    Consulte [DPI Engine](../../interface_guide/dpi_engine.md) para ver instrucciones detalladas.

=== "Data Statistics"

    Data Statistics ofrece un panel inteligente de análisis de tráfico que clasifica y visualiza el uso de la red por aplicaciones, lo que le ayuda a supervisar el tráfico en tiempo real e histórico para lograr una mejor visibilidad y control de la red.

    Consulte [Data Statistics](../../interface_guide/data_statistics.md) para ver instrucciones detalladas.

=== "Content Filter"

    Content Filter proporciona seguridad inteligente en línea mediante clasificación basada en DPI y bloquea automáticamente sitios web dañinos o maliciosos para mantener su red limpia y segura.

    Consulte [Content Filter](../../interface_guide/content_filter.md) para ver instrucciones detalladas.

---

=== "QoS"

    QoS, Quality of Service, optimiza la asignación del ancho de banda al priorizar actividades críticas, por ejemplo videollamadas o juegos, durante la congestión de la red, reduciendo la latencia y mejorando el rendimiento general. Tenga en cuenta que esto se aplica al tráfico de clientes locales y al tráfico del túnel de cliente VPN, pero no al tráfico recibido cuando el router funciona como servidor VPN.

    Consulte [QoS](../../interface_guide/qos.md) para ver instrucciones detalladas.

=== "SQM"

    SQM, Smart Queue Management, gestiona de forma inteligente el tráfico de red del router para minimizar la latencia y el bufferbloat, garantizando una experiencia más fluida en juegos y llamadas de voz.

    Consulte [SQM](../../interface_guide/sqm.md) para ver instrucciones detalladas.

=== "Parental Control"

    Parental Control está diseñado para ayudarle a administrar y controlar los dispositivos de sus hijos. Incluye limitar el tiempo de pantalla y restringir el acceso a determinados contenidos.

    Para obtener más información, consulte [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Seguridad

=== "Port Forwarding"

    El reenvío de puertos permite que servidores y dispositivos remotos en Internet accedan a dispositivos dentro de una red privada.

    Para configurar el reenvío de puertos, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, abreviatura de Access Control List, permite crear reglas para administrar el tráfico de red en función de los protocolos de conexión, las direcciones de los dispositivos y los puertos. Controla si se permite o bloquea el acceso a la red. Si varias reglas ACL entran en conflicto, el sistema aplica la que tenga mayor prioridad.

    Para obtener más información, consulte [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access le permite configurar varios ajustes de seguridad para proteger su red y su router frente a accesos no autorizados. Esta página incluye las siguientes opciones:

    * Local Access Control: administre y restrinja el acceso a la interfaz del router desde dispositivos conectados a su red local.
    * Remote Access Control: configure y restrinja el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controle qué puertos están abiertos en el router para limitar posibles vulnerabilidades y accesos no autorizados.

    Para obtener más información, consulte [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La página NAT Mode le permite activar o desactivar las funciones Full Cone NAT y SIP ALG, Application Layer Gateway.

    Para configurar los ajustes NAT, consulte [NAT Mode](../../interface_guide/nat_settings.md).

## Aplicaciones

=== "Plug-ins"

    Un complemento es un componente de software que añade funciones o características específicas a un programa existente, lo que permite personalizarlo y ampliar sus capacidades.

    Para configurar complementos, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS, DDNS, detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta especialmente útil para usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage se refiere a una solución centralizada de almacenamiento de datos que permite a varios usuarios y dispositivos acceder a archivos y compartirlos a través de una red.

    Para configurar Network Storage, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores para toda la red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a la red doméstica.

    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    El servicio Bark integrado en Flint 4 ayuda a proteger el entorno digital de sus hijos y ofrece una protección completa en línea. Normalmente requiere una suscripción de pago. Sin embargo, gracias a la colaboración con Bark, GL.iNet ofrece gratuitamente el plan Bark Home en determinados modelos de router, incluido Flint 4, con funciones avanzadas de supervisión y alertas sin coste adicional.

    Para obtener más información, consulte [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico por Internet a través de una serie de servidores operados por voluntarios, nodos, para ocultar la ubicación y el uso del usuario, lo que dificulta rastrear sus actividades en línea.

    Para obtener más información, consulte [Tor](../../interface_guide/tor.md).

## Sistema

=== "Overview"

    La página Overview ofrece una visión completa del estado actual y de las métricas de rendimiento del router. En esta página puede ver:

    * CPU Average Load: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Memory Usage: compruebe cuánta memoria del router está en uso para ayudar a administrar los recursos.
    * Flash Usage: vea el uso del almacenamiento flash del router para asegurarse de que haya espacio suficiente para el firmware y los datos de configuración.
    * Device Info: acceda a información detallada sobre el sistema del router, incluyendo tiempo de actividad, hostname, modelo, arquitectura, versión de OpenWrt, versión del kernel, ID del dispositivo, MAC del dispositivo y S/N del dispositivo.
    * External Storage: compruebe el estado de cualquier dispositivo de almacenamiento externo conectado al router, como unidades USB o tarjetas TF.

    Estas funciones proporcionan información y controles esenciales para ayudarle a gestionar y supervisar eficazmente el funcionamiento del router.

    Consulte [Overview](../../interface_guide/system_overview.md) para ver instrucciones detalladas.

=== "Admin Password"

    La página Admin Password permite administrar la contraseña de la interfaz de administración del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.

    Consulte [Admin Password](../../interface_guide/admin_password.md) para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, lo que garantiza un mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: comprueba automáticamente en el servidor del fabricante si existe una versión más reciente del firmware. Puede instalarla si está disponible en línea.
    * Firmware Local Upgrade: permite cargar manualmente un archivo de firmware desde su ordenador para actualizar el router, proporcionando control sobre la versión y el momento de la actualización.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

---

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Las funciones clave de esta página incluyen:

    * LCD Display Schedule: establezca un horario para encender o apagar automáticamente la pantalla LCD del router, reduciendo la contaminación lumínica en determinados momentos.
    * Schedule Reboot: configure el reinicio automático del router a intervalos especificados para ayudar a mantener un rendimiento y una estabilidad óptimos.
    * Wi-Fi Status Schedule: establezca un horario para controlar las bandas Wi-Fi de 6 GHz / 5 GHz / 2,4 GHz / MLO, administrar la disponibilidad de la red y reducir el consumo de energía.

    Estas opciones de programación le ofrecen un mayor control sobre el funcionamiento del router, asegurando que se adapte a sus necesidades y preferencias específicas.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

=== "Display Management"

    La página Display Management le ofrece una gama completa de funciones para gestionar la pantalla táctil y los ajustes relacionados.

    ‒ Wallpaper: personalice el fondo de pantalla y el estilo de activación de la pantalla.
    ‒ Brightness: ajuste el brillo de la pantalla táctil. Use el control deslizante o introduzca un porcentaje específico para adaptarlo a distintas condiciones de iluminación.
    ‒ Auto Lock: establezca el retardo para el bloqueo automático de la pantalla cuando no haya actividad. El rango es de 1 minuto a 30 minutos.
    ‒ Screen Always On: active o desactive esta opción para decidir si la pantalla táctil permanece encendida continuamente o se apaga tras un período de inactividad.
    ‒ Enable Screen Passcode: establezca un código de acceso para la pantalla táctil y añada una capa extra de seguridad.

    Consulte [Display Management](../../interface_guide/display_management.md) para ver instrucciones detalladas.

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, asegurando que todas las tareas programadas, registros y eventos del sistema queden marcados con precisión según su hora local. Este ajuste es fundamental para mantener registros precisos y para la correcta ejecución de configuraciones basadas en tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

---

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión de firmware actual del router a su configuración predeterminada y borrar todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware instalada actualmente. Puede resultar útil para resolver problemas persistentes o para empezar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para ver instrucciones detalladas.

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que ayuda en la solución de problemas y la supervisión del rendimiento. Esta página incluye:

    * System Log: registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: registros relacionados con las operaciones y eventos del kernel.
    * Crash Log: registros de fallos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Cloud Log: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Nginx Log: registros del servidor web Nginx, si se utiliza en el router, con detalles del tráfico web y de las operaciones del servidor.

    Además, la página ofrece un botón Export Log, que le permite exportar todos los registros recopilados para su análisis por soporte técnico. Esta función es muy útil para diagnosticar problemas complejos y obtener asistencia profesional.

    Consulte [Log](../../interface_guide/log.md) para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings proporciona acceso a opciones de configuración avanzadas a través de la interfaz LuCI de OpenWrt, lo que permite a los usuarios experimentados ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas de la interfaz. Esto incluye configuraciones de red detalladas, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para ver instrucciones detalladas.

## Declaración de Conformidad

Por la presente, GL TECHNOLOGIES (HONG KONG) LIMITED declara que el tipo de equipo radioeléctrico [BE14000 Wi-Fi 7 Router, GL-BE14000] es conforme con los requisitos esenciales y demás disposiciones pertinentes de la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.