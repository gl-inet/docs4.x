# Guía del usuario de Fortify (GL-MT6000)

## Descripción general del producto

Fortify (GL-MT6000) es un enrutador Wi-Fi 6 de marca compartida lanzado conjuntamente por GL.iNet y ExpressVPN. Cada unidad viene con una suscripción gratuita a ExpressVPN por un año. Los usuarios pueden canjear la suscripción y conectar sus cuentas directamente en el Panel de administración web del enrutador. Una vez activado, todo el tráfico que pase a través del enrutador aprovechará la red de alta velocidad y el cifrado sólido de ExpressVPN para proteger toda su conexión de red y su privacidad en línea.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Cómo configurar Fortify

### 1. Encendido

Junte el adaptador de corriente de dos piezas. Conéctelo a su enrutador Fortify y conéctelo a una toma de corriente. Se iniciará automáticamente.

### 2. Conectar dispositivo

Conecte un dispositivo (por ejemplo, computadora, computadora portátil o teléfono inteligente) al enrutador a través de Wi-Fi o Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del enrutador mediante un cable Ethernet.

- Wifi

    En su dispositivo, vaya a Configuración -> WLAN, ubique el nombre de la red Wi-Fi de su enrutador en la lista de redes disponibles e ingrese la contraseña para unirse a la red. Puede encontrar el nombre de red predeterminado y la contraseña impresos en la etiqueta del enrutador.

### 3. Inicie sesión en el Panel de administración web

Abra un navegador web, ingrese `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma en la esquina superior derecha, establezca su contraseña de administrador y luego haga clic en **Next**. La contraseña debe tener entre 10 y 63 caracteres y contener al menos dos de los siguientes: letras mayúsculas, letras minúsculas, números y símbolos especiales.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Configura tu wifi. Tenga en cuenta que si cambia la información de Wi-Fi, deberá volver a conectar su dispositivo al Wi-Fi del enrutador utilizando las credenciales actualizadas.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Configuración de Internet

**Nota:** Las siguientes instrucciones se aplican a quienes configuren el router mediante el panel de administración web de GL.iNet. Si prefiere la [aplicación GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, descárguela y siga las instrucciones en pantalla.

Configure su Fortify utilizando uno de los métodos de conexión a Internet admitidos: Ethernet, repetidor, anclaje a red y celular. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Conecte un cable Ethernet entre el puerto WAN de su enrutador Fortify y un dispositivo ascendente, como un módem.

    Una vez conectado correctamente a Internet, el LED del enrutador se vuelve blanco fijo.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para obtener instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. En el panel de administración web, vaya a INTERNET -> sección Repetidor y haga clic en **Connect**.
    2. Seleccione una Wi-Fi de las redes disponibles.
    3. Ingrese la contraseña y luego haga clic en **Apply**.

    Una vez conectado correctamente a Internet, el LED del enrutador se vuelve blanco fijo.

    Consulte [Conectarse a Internet a través de una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para obtener instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Conecte su teléfono inteligente al puerto USB del enrutador mediante un cable USB.
    2. En su teléfono inteligente, vaya a Configuración y habilite Anclaje a red USB. Para iPhone, confíe en este dispositivo y habilite Personal Hotspot.
    3. En el panel de administración web, vaya a INTERNET -> sección Anclaje a red y haga clic en **Connect**.

    Una vez conectado correctamente a Internet, el LED del enrutador se vuelve blanco fijo.

    Consulte [Conectarse a Internet mediante anclaje a red USB](../../interface_guide/internet_tethering.md) para obtener instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del enrutador. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Una vez conectado correctamente a Internet, el LED del enrutador se vuelve blanco fijo.

    Consulte [Conectarse a Internet a través del celular](../../interface_guide/internet_cellular.md) para obtener instrucciones detalladas.

---

A continuación se muestra una descripción general de las funciones del Panel de administración web de Fortify.

## Inalámbrico

La página Inalámbrica le permite configurar las redes Wi-Fi de Fortify, incluida la red principal, la red de invitados y la red IoT. Cada red admite las bandas de 2,4 GHz y 5 GHz.

Para configurar la conexión inalámbrica, consulte [Inalámbrico](../../interface_guide/wireless.md).

## Clientes

La página Clientes muestra información sobre los dispositivos conectados, incluido el nombre del dispositivo, el tipo de conexión, las direcciones IP y MAC, las velocidades de carga y descarga, el tráfico y brinda la posibilidad de bloquear un cliente específico con un solo clic o realizar otras acciones.

Consulte [Clientes](../../interface_guide/clients.md) para obtener más detalles.

## Servicios en la nube

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} proporciona una manera fácil y sencilla de acceder y administrar de forma remota sus enrutadores GL.iNet.

    Consulte [GoodCloud](../../interface_guide/cloud.md) para obtener más detalles.

=== "AstroWarp"

    AstroWarp es una función creada para una conexión remota perfecta en enrutadores GL.iNet. Adopta el protocolo AmneziaWG con ofuscación de tráfico incorporada, lo que brinda acceso remoto estable y seguro en cualquier momento y lugar.

    Consulte [AstroWarp](../../interface_guide/astrowarp.md) para obtener más detalles.

## VPN

Una VPN (red privada virtual) establece túneles de tráfico cifrados y seguros entre su dispositivo local y el servidor VPN. Agrega una capa adicional de privacidad y seguridad al cliente VPN y permite el acceso a la red del servidor VPN remoto.

Fortify se integra con [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, lo que le permite activar una conexión ExpressVPN en minutos. Cada dispositivo Fortify viene con una suscripción gratuita a ExpressVPN por un año. Puede canjear la suscripción y conectar su cuenta ExpressVPN directamente en el panel de administración web del enrutador. Una vez que la conexión VPN esté habilitada, todo el tráfico dirigido a través del enrutador utilizará los servidores de alta velocidad y el cifrado sólido de ExpressVPN para proteger toda su red y su privacidad en línea.

Para canjear la suscripción gratuita y configurar el túnel VPN, consulte la [Guía de activación de ExpressVPN](../../interface_guide/expressvpn_activation_guide.md).

Para configurar un servidor OpenVPN, consulte [Servidor OpenVPN](../../interface_guide/openvpn_server.md).

Para configurar un servidor WireGuard, consulte [Servidor WireGuard](../../interface_guide/wireguard_server.md).

## Red

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar su enrutador con múltiples conexiones a Internet (por ejemplo, celular, repetidor y Ethernet) al mismo tiempo. Si su conexión a Internet actual falla, el enrutador cambiará automáticamente a otra conexión a Internet. Esto garantiza un acceso a Internet fluido e ininterrumpido.

Consulte [Multi-WAN](../../interface_guide/multi-wan.md) para obtener más detalles.

=== "LAN"

    Una LAN, o red de área local, es una red que conecta computadoras y dispositivos dentro de un área geográfica limitada, como un hogar u oficina. Esta es la red local a la que se une su dispositivo cuando está conectado al Wi-Fi principal o mediante un cable Ethernet. La página LAN cubre la configuración básica, la configuración del servidor DHCP y la reserva de dirección.

    Consulte [LAN](../../interface_guide/lan.md) para obtener más detalles.

=== "Guest Network"

    La página Red de invitados le permite crear una red Wi-Fi dedicada para los visitantes. Aislado de la red principal, mejora la seguridad al tiempo que proporciona un cómodo acceso a Internet. Puede configurar una subred de invitados dentro de los rangos de direcciones privadas IPv4 `192.168.0.0/16`, `172.16.0.0/12` o `10.0.0.0/8`, especificar la puerta de enlace y las direcciones IP de la máscara de red.

    Consulte [Red de invitados](../../interface_guide/guest_network.md) para obtener más detalles.

=== "IoT Network"

    La página Red IoT le permite crear una red Wi-Fi dedicada para dispositivos IoT. Aislado de la red principal, ofrece mayor compatibilidad y seguridad.

    Consulte [Red IoT](../../interface_guide/iot_network.md) para obtener más detalles.

<br>

=== "DNS"

    La configuración de DNS de su enrutador controla cómo se traducen los nombres de dominio en direcciones IP. Esta página le permite utilizar los servidores DNS obtenidos automáticamente de los dispositivos ascendentes, o establecer servidores personalizados y configurar prioridades de DNS.

    Consulte [DNS](../../interface_guide/dns.md) para obtener más detalles.

=== "Ethernet Port"

    La página Puerto Ethernet le permite administrar las funciones de los puertos Ethernet (WAN/LAN) y ver los detalles del puerto, como la dirección MAC y la velocidad negociada.

    Consulte [Puerto Ethernet](../../interface_guide/ethernet_port.md) para obtener más detalles.

=== "IPv6"

    IPv6, o Protocolo de Internet versión 6, es la versión más reciente del Protocolo de Internet diseñada para reemplazar IPv4. Proporciona un espacio de direcciones mucho mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, lo cual es esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Consulte [IPV6](../../interface_guide/network_mode.md) para obtener más detalles.

=== "IGMP Snooping"

    La vigilancia IGMP es una técnica de optimización de red utilizada en conmutadores Ethernet para gestionar y controlar el tráfico de multidifusión.

    Consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md) para obtener más detalles.

<br>

=== "Network Mode"

    El modo de red se refiere a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurar el modo de red, consulte [Modo de red](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad de su enrutador principal con funciones que quizás no tenga, incluidos AdGuard Home, DNS cifrado y VPN.

    Para configurar la puerta de enlace directa, consulte [Cómo configurar la puerta de enlace directa](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    La aceleración de la red puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.

    Para configurar la aceleración de red, consulte [Aceleración de red](../../interface_guide/network_acceleration.md).

## Control de flujo

=== "DPI Engine"

DPI (Inspección profunda de paquetes) es una capacidad central de la gestión inteligente de redes. Puede superar la limitación de los enrutadores tradicionales (que solo identifican las direcciones de origen o destino), analizar en profundidad las cargas útiles de los paquetes de datos e identificar con precisión las aplicaciones y los sitios web a los que acceden los usuarios a través de la comparación de bibliotecas de funciones, lo que permite una clasificación y control refinados del tráfico.

    Integrada con [Netify](https://www.netify.ai/){target="_blank"}, la función GL.iNet DPI adopta un complemento integrado liviano para una implementación eficiente. Con la base de datos de firmas actualizada en línea de Netify, permite una gestión confiable, lo que hace que el control de la red sea más preciso y eficiente.

    Consulte [Motor DPI](../../interface_guide/dpi_engine.md) para obtener más detalles.

=== "Data Statistics"

    Estadísticas de datos ofrece un panel de información de tráfico inteligente que clasifica y visualiza el uso de la red por aplicaciones, lo que le ayuda a monitorear el tráfico histórico y en tiempo real para un mejor conocimiento y control de la red.

    Consulte [Estadísticas de datos](../../interface_guide/data_statistics.md) para obtener más detalles.

=== "Content Filter"

    Content Filter proporciona seguridad en línea inteligente impulsada por una clasificación basada en DPI, que bloquea automáticamente sitios web dañinos o maliciosos para mantener su red limpia y segura.

    Consulte [Filtro de contenido](../../interface_guide/content_filter.md) para obtener más detalles.

<br>

=== "QoS"

    QoS (calidad de servicio) optimiza la asignación de ancho de banda al priorizar actividades críticas (por ejemplo, videollamadas, juegos) durante la congestión de la red, reduciendo la latencia y mejorando el rendimiento general de la red. Tenga en cuenta que esto se aplica al tráfico del cliente local y al tráfico del túnel del cliente VPN, pero no al tráfico recibido cuando el enrutador funciona como servidor VPN.

    Consulte [QoS](../../interface_guide/qos.md) para obtener más detalles.

=== "SQM"

    SQM (Smart Queue Management) gestiona de forma inteligente el tráfico de red de su enrutador para minimizar la latencia y el "bufferbloat", lo que garantiza juegos y llamadas de voz más fluidos.

    Consulte [SQM](../../interface_guide/sqm.md) para obtener más detalles.

=== "Parental Control"

    El control parental está diseñado para ayudarlo a administrar y controlar los dispositivos de sus hijos. Incluye limitar su tiempo frente a la pantalla y restringir su acceso a cierto contenido.

    Consulte [Control parental](../../interface_guide/parental_control_v4.9.md) para obtener más detalles.

## Seguridad

=== "Port forwarding"

    El reenvío de puertos permite que servidores y dispositivos remotos en Internet accedan a dispositivos en una red privada.

    Consulte [Reenvío de puertos](../../interface_guide/port_forwarding.md) para obtener más detalles.

=== "ACL"

    ACL, abreviatura de Lista de control de acceso, le permite crear reglas para administrar el tráfico de red en función de protocolos de conexión, direcciones de dispositivos y puertos. Controla si se permite o bloquea el acceso a la red. Si varias reglas de ACL entran en conflicto, el sistema aplica la que tiene mayor prioridad.

    Consulte [ACL](../../interface_guide/acl.md) para obtener más detalles.

=== "Admin Access"

    El acceso de administrador le permite configurar varias configuraciones de seguridad para proteger su red y su enrutador del acceso no autorizado. Esta página incluye las siguientes opciones:

    * Control de acceso: administre y restrinja el acceso a la interfaz del enrutador desde dispositivos conectados a su red local.
    * Control de acceso remoto: Configure y restrinja el acceso a la interfaz del enrutador desde ubicaciones remotas a través de Internet, mejorando la seguridad contra amenazas externas.
    * Puertos abiertos en el enrutador: controle qué puertos están abiertos en el enrutador, limitando posibles vulnerabilidades y accesos no autorizados.

    Consulte [Acceso de administrador](../../interface_guide/admin_access.md) para obtener más detalles.

=== "NAT Mode"

    La página Modo NAT le permite habilitar o deshabilitar la funcionalidad Full Cone NAT y SIP ALG (Application Layer Gateway).

    Consulte [Modo NAT](../../interface_guide/nat_settings.md) para obtener más detalles.

## Aplicaciones

=== "Plug-ins"

    Un complemento es un componente de software que agrega características o funcionalidades específicas a un programa informático existente, lo que permite personalizar y mejorar sus capacidades.

    Consulte [Complementos](../../interface_guide/plugins.md) para obtener más detalles.

=== "Dynamic DNS"

    El DNS dinámico (DDNS) detecta y actualiza automáticamente la dirección IP asociada a un dominio en tiempo real. Es útil para usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Consulte [DNS dinámico](../../interface_guide/ddns.md) para obtener más detalles.

=== "Network Storage"

    El almacenamiento en red se refiere a una solución de almacenamiento de datos centralizada que permite que múltiples usuarios y dispositivos accedan y compartan archivos a través de una red.

    Consulte [Almacenamiento de red](../../interface_guide/network_storage.md) para obtener más detalles.

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de rastreadores y anuncios en toda la red que actúa como un servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a una red doméstica.

    Consulte [AdGuard Home](../../interface_guide/adguardhome.md) para obtener más detalles.

<br>

=== "Bark"

    El servicio [Bark](https://www.bark.us/){target="_blank"} puede ayudar a proteger el mundo digital de su hijo y brindarle una protección integral en línea. Por lo general, requiere una suscripción paga. Sin embargo, como parte de la asociación de GL.iNet con Bark, ofrecemos el plan Bark Home de forma gratuita en Fortify (GL-MT6000), que brinda monitoreo y alertas avanzadas sin costo adicional.

    Consulte [Bark](../../interface_guide/bark.md) para obtener más detalles.

=== "Tailscale"

    Tailscale es un servicio VPN que hace que sus dispositivos y aplicaciones sean accesibles en cualquier parte del mundo, de forma segura y sin esfuerzo.

    Fortify (GL-MT6000) se integra con Tailscale, lo que le permite unir el enrutador a una red virtual de Tailscale. Una vez conectado, podrá acceder a él de forma remota, incluidos sus recursos WAN y LAN.

    Consulte [Tailscale](../../interface_guide/tailscale.md) para obtener más detalles.

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Consulte [ZeroTier](../../interface_guide/zerotier.md) para obtener más detalles.

=== "Tor"

    Tor (derivado de The Onion Router) es un software gratuito y de código abierto que permite la comunicación anónima. Ayuda a los usuarios a explorar Internet con privacidad.

    Consulte [Tor](../../interface_guide/tor.md) para obtener más detalles.

## Sistema

=== "Overview"

    La página Descripción general proporciona una instantánea completa del estado actual y las métricas de rendimiento de su enrutador. En esta página puedes ver:

    * Carga promedio de CPU: monitoree la carga promedio en la CPU de su enrutador, lo que ayuda a evaluar el rendimiento e identificar posibles cuellos de botella.
    * Uso de memoria: verifique cuánta memoria de su enrutador está en uso, lo que ayuda en la administración de recursos.
    * Control LED: enciende o apaga las luces LED del enrutador, lo que permite personalizar los indicadores visuales del dispositivo.
    * Uso de Flash: vea la utilización del almacenamiento flash del enrutador, asegurando que haya suficiente espacio para el firmware y los datos de configuración.
    * Información del dispositivo: acceda a información detallada sobre el sistema de su enrutador, incluido el tiempo de actividad, el nombre de host, el modelo, la arquitectura, la versión de OpenWrt, la versión del kernel, la ID del dispositivo, la MAC del dispositivo y el S/N del dispositivo.
    * Almacenamiento externo: verifique el estado de cualquier dispositivo de almacenamiento externo conectado al enrutador, como unidades USB o tarjetas TF.

    Estas funciones brindan información y controles esenciales que lo ayudan a administrar y monitorear de manera efectiva el funcionamiento de su enrutador.

    Consulte [Descripción general](../../interface_guide/system_overview.md) para obtener más detalles.

=== "Admin Password"

    La página Contraseña de administrador le permite configurar o cambiar la contraseña para la interfaz administrativa del enrutador.

    Consulte [Contraseña de administrador](../../interface_guide/admin_password.md) para obtener más detalles.

=== "Upgrade"

    La página Actualizar se utiliza para actualizar el firmware de su enrutador a la última versión, lo que garantiza un mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones:

    * Actualización de firmware en línea: busque e instale automáticamente la última versión de firmware directamente desde el servidor del fabricante, simplificando el proceso de actualización.
    * Actualización local de firmware: cargue manualmente un archivo de firmware desde su computadora para actualizar el enrutador, brindando control sobre la versión y el tiempo de actualización.

    Consulte [Actualización](../../interface_guide/upgrade.md) para obtener más detalles.

=== "Scheduled Tasks"

    La página Tareas programadas le permite automatizar varias funciones del enrutador según una programación predefinida, lo que mejora la comodidad y la eficiencia. Las características clave de esta página incluyen:

    * Horario de pantalla LED: establezca un horario para encender o apagar automáticamente las luces LED del enrutador, reduciendo la contaminación lumínica durante momentos específicos.
    * Programar reinicio: configure su enrutador para que se reinicie automáticamente en intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación de estado de Wi-Fi de 5 GHz/2,4 GHz: establezca una programación para controlar la banda Wi-Fi de 5 GHz/2,4 GHz, lo que permite una mejor gestión de la disponibilidad de la red y el consumo de energía.

    Estas opciones de programación le brindan un mayor control sobre las operaciones de su enrutador, asegurando que satisfaga sus necesidades y preferencias específicas.

    Consulte [Tareas programadas](../../interface_guide/scheduled_tasks.md) para obtener más detalles.

<br>

=== "Time Zone"

    La página Zona horaria le permite configurar la zona horaria correcta para su enrutador, lo que garantiza que todas las tareas programadas, registros y eventos del sistema tengan una marca de tiempo precisa según su hora local. Esta configuración es crucial para mantener registros precisos y para la ejecución adecuada de configuraciones basadas en tiempo.

    Consulte [Zona horaria](../../interface_guide/time_zone.md) para obtener más detalles.

=== "Reset Firmware"

La página Restablecer firmware le permite restablecer la versión actual del firmware de su enrutador a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el enrutador a la configuración predeterminada de la versión de firmware instalada actualmente. Esto puede resultar útil para solucionar problemas persistentes o comenzar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Restablecer firmware](../../interface_guide/reset_firmware.md) para obtener más detalles.

=== "Log"

    La página Registro brinda acceso a varios registros que registran las actividades y eventos del enrutador, lo que ayuda en la resolución de problemas y el monitoreo del rendimiento. Esta página incluye:

    * Registro del sistema: registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: Registros relacionados con las operaciones y eventos del kernel.
    * Registro de fallos: registros de fallos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Cloud Log: Registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados con el enrutador.
    * Registro de Nginx: registros del servidor web Nginx, si lo utiliza el enrutador, que detallan el tráfico web y las operaciones del servidor.

    Además, la página presenta un botón Exportar registro, que le permite exportar todos los registros recopilados para su análisis de soporte técnico. Esta función es invaluable para diagnosticar problemas complejos y obtener asistencia profesional.

    Consulte [Registro](../../interface_guide/log.md) para obtener más detalles.

=== "Advanced Settings"

    La página Configuración avanzada brinda acceso a opciones de configuración avanzadas a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios experimentados ajustar la configuración y las funcionalidades de su enrutador más allá de las opciones básicas de la interfaz. Esto incluye configuraciones de red detalladas, configuraciones de firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Configuración avanzada](../../interface_guide/advanced_settings.md) para obtener más detalles.
