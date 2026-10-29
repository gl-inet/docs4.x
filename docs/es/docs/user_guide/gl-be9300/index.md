# Guía de usuario de Flint 3 (GL-BE9300) {#flint-3-gl-be9300-user-guide}

## Descripción general del producto {#product-overview}

Flint 3 (GL-BE9300) es un router de escritorio Wi-Fi 7 de triple banda diseñado para usuarios domésticos, pequeñas oficinas y escenarios de alta demanda. Es compatible con Wi-Fi 7 Multi-Link Operation (MLO), combinando de forma inteligente sus bandas de 2,4 GHz, 5 GHz y 6 GHz en una sola conexión para reducir interferencias y congestión. Junto con 4K QAM, ofrece velocidades teóricas de 688 Mbps (2,4 GHz), 2882 Mbps (5 GHz) y 5765 Mbps (6 GHz). La conectividad MLO o de 6 GHz proporciona el máximo rendimiento, mientras que la banda de 2,4 GHz puede dedicarse a dispositivos IoT.

Cuenta con 5 puertos Ethernet 2.5G (1 WAN dedicado, 1 WAN/LAN conmutable y 3 LAN), compatibles con configuraciones dual-WAN con un ancho de banda compartido máximo de 5 Gbps, además de 1 puerto USB 3.0 para ampliar la funcionalidad. También viene con AdGuard Home preinstalado para bloqueo de anuncios y antirrastreo, es compatible con Bark Parental Control y con más de 30 servicios VPN, y permite la gestión remota mediante GoodCloud, equilibrando a la perfección rendimiento, practicidad y seguridad.

![gl-be9300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/hardware_info/be9300_interface.jpg){class="glboxshadow"}

## Contenido del paquete {#package-contents}

- 1 x Flint 3 (GL-BE9300)
- 1 x Adaptador de corriente
- 1 x Cable Ethernet
- 1 x Manual del usuario
- 1 x Tarjeta de agradecimiento
- 1 x Convertidor (según el país de envío)

Vea a continuación el vídeo de unboxing de Flint 3.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qAq6IFtKtj0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cómo configurar Flint 3 {#how-to-set-up-flint-3}

Vea este vídeo de configuración o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WQqD-8NrAOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encender {#1-power-on}

Ensamble las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. El router se iniciará automáticamente.

### 2. Conectar un dispositivo {#2-connect-device}

Conecte un dispositivo, por ejemplo un ordenador, un portátil o un smartphone, al router mediante Wi-Fi o Ethernet.

- Ethernet

  Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

- Wi-Fi

  En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña para unirse a la red. Puede encontrar el nombre de red y la contraseña predeterminados impresos en la etiqueta del router.

### 3. Iniciar sesión en el panel de administración web {#3-log-in-to-web-admin-panel}

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma, establezca la contraseña de administrador y haga clic en **Apply**.

### 4. Configuración de Internet {#4-internet-setup}

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router desde el panel de administración web de GL.iNet. Si prefiere usar la aplicación de GL.iNet, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

Configure su Flint 3 con uno de los métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_ethernet.jpg){class="glboxshadow"}

    Conecte el puerto WAN de Flint 3 a un dispositivo aguas arriba, por ejemplo un módem, mediante un cable ethernet.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_repeater.jpg){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de la lista de redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_tethering.jpg){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB del router mediante un cable USB.
    2. En el dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_cellular.jpg){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB de Flint 3. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Conectarse a Internet mediante conexión celular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

---

A continuación se ofrece una visión general de las funciones del panel de administración web de Flint 3.

## Wireless {#wireless}

La página Wireless le permite configurar ajustes para las redes Wi-Fi de 6 GHz, 5 GHz y 2,4 GHz, incluyendo activar el Wi-Fi, ajustar la potencia TX, definir el nombre de la red Wi-Fi (SSID), activar el BSSID aleatorio, seleccionar el modo de seguridad Wi-Fi y la contraseña, configurar la visibilidad del SSID y elegir el modo Wi-Fi, el ancho de banda y el canal.

Además, Flint 3 es compatible con MLO Wi-Fi, es decir, Multi-Link Operation, que combina varias redes inalámbricas simultáneamente para lograr mayor ancho de banda y conexiones más fiables.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh es una función basada en el estándar Wi-Fi EasyMesh™ que amplía la cobertura Wi-Fi de todo el hogar y permite una itinerancia fluida. Si tiene varios routers GL.iNet, configure uno como router principal y los demás como nodos mesh para desplazarse por su hogar sin interrupciones en la conexión Wi-Fi.

Para configurar Mesh, consulte [Mesh](../../interface_guide/mesh.md).

## Clients {#clients}

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, se muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y subida, el tráfico total y la posibilidad de bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account permite conectar y administrar sus dispositivos y servicios en la nube. Puede acceder de forma integrada a GoodCloud y a la glinet App para administrar su red de forma segura y cómoda desde cualquier lugar y en cualquier momento.

    Para configurar GL.iNet Account, consulte [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} proporciona una forma sencilla de acceder de forma remota a los routers GL.iNet y gestionarlos.
    
    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS es una función de red avanzada diseñada para ofrecer acceso remoto y administración de dispositivos sin interrupciones. Creado específicamente para integrarse con routers GL.iNet, GoodPAS utiliza el protocolo AmneziaWG con ofuscación de tráfico integrada para proporcionar conexiones seguras y estables. GoodPAS permite acceder de forma remota a su red doméstica. Cuando el router de su casa actúa como nodo de salida de GoodPAS, el tráfico de Internet enviado a través de GoodPAS utiliza la dirección IP pública WAN de ese router.

    Para configurar GoodPAS, consulte [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad (cliente VPN) y le permite acceder a una red remota (servidor VPN). Flint 3 es compatible con OpenVPN y WireGuard.

=== "OpenVPN"

    Flint 3, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 3, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Esta página permite configurar y administrar de forma centralizada **Main Network**, **Guest Network**, **IoT Network** y las **VLAN Networks** personalizadas. Puede crear y administrar varias subredes para aislar distintos tipos de dispositivos o tráfico.

    Para configurar esta función, consulte [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La página Ethernet Port le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC de la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para gestionar los puertos Ethernet, consulte [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección contra ataques de reenlace DNS, anular la configuración DNS de todos los clientes y permitir que el DNS personalizado anule el DNS de la VPN. Puede utilizar servidores DNS obtenidos automáticamente de los dispositivos de la red superior o especificar manualmente servidores DNS personalizados.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, es la versión más reciente del protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones muchísimo mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.
    
    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.
    
    Para configurar IGMP Snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).
    
---

=== "Network Mode"

    La página Network Mode permite configurar la función operativa del router según distintas necesidades de despliegue. Puede elegir entre varios modos, desde la cobertura Wi-Fi doméstica hasta redes empresariales de varios enlaces; cada modo habilita o deshabilita funciones específicas del router para optimizar el rendimiento.

    Para configurar esta función, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad del router principal, incluyendo AdGuard Home, DNS cifrado y cliente VPN.
    
    Para configurar drop-in gateway, consulte estos enlaces:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Cómo configurar Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.
    
    Para configurar Network Acceleration, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Control de flujo {#flow-control}

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

    Para configurar el control parental, consulte [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Seguridad {#security}

=== "Port Forwarding"

    Port forwarding permite que servidores remotos y dispositivos de Internet accedan a dispositivos de una red privada.

    Para configurar Port Forwarding, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, abreviatura de Access Control List, permite crear reglas para administrar el tráfico de red en función de los protocolos de conexión, las direcciones de los dispositivos y los puertos. Controla si se permite o bloquea el acceso a la red. Si varias reglas ACL entran en conflicto, el sistema aplica la que tenga mayor prioridad.

    Para obtener más información, consulte [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access le permite configurar varios ajustes de seguridad para proteger su red y su router frente a accesos no autorizados. Esta página incluye las siguientes opciones:

    * Local Access Control: gestionar y restringir el acceso a la interfaz del router desde dispositivos conectados a la red local.
    * Remote Access Control: configurar y restringir el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controlar qué puertos están abiertos en el router, limitando posibles vulnerabilidades y accesos no autorizados.

    Para obtener más información, consulte [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La página NAT Mode le permite activar o desactivar la funcionalidad Full Cone NAT y SIP ALG.

    Para configurar los ajustes NAT, consulte [NAT Mode](../../interface_guide/nat_settings.md).

## Aplicaciones {#applications}

=== "Plug-ins"

    Un plug-in es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo personalizarlo y ampliar sus capacidades.

    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Asigna un nombre de dominio a la dirección IP pública dinámica de su router, de modo que pueda acceder a su red de forma remota sin necesidad de una dirección IP estática.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage se refiere a una solución de almacenamiento de datos centralizada que permite que varios usuarios y dispositivos accedan a archivos y los compartan a través de una red.
    
    Para configurar Network Storage, consulte [Network Storage](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores para toda la red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a una red doméstica.
    
    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Bark"

    El servicio Bark integrado en Flint 3 ayuda a proteger el entorno digital de sus hijos y ofrece una protección completa en línea. Normalmente requiere una suscripción de pago. Sin embargo, gracias a la colaboración con Bark, GL.iNet ofrece gratuitamente el plan Bark Home en determinados modelos de router, incluido Flint 3, con funciones avanzadas de supervisión y alertas sin coste adicional.

    Para obtener más información, consulte [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.
    
    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.
    
    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico de Internet a través de una serie de servidores operados por voluntarios (nodos) para ocultar la ubicación y el uso del usuario, lo que dificulta el rastreo de la actividad en línea.
    
    Para obtener más información, consulte [Tor](../../interface_guide/tor.md).

## Sistema {#system}

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

=== "Admin Password"

    La página Admin Password permite administrar la contraseña de la interfaz de administración del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.

    Consulte [Admin Password](../../interface_guide/admin_password.md) para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: comprueba automáticamente en el servidor del fabricante si existe una versión más reciente del firmware. Puede instalarla si está disponible en línea.
    * Firmware Local Upgrade: permite cargar manualmente un archivo de firmware desde el ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de visualización LED: establezca un horario para encender o apagar automáticamente los LED del router y reducir la contaminación lumínica en determinadas horas.
    * Reinicio programado: configure el router para que se reinicie automáticamente en intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi: establezca un horario para controlar las bandas Wi-Fi de 6 GHz / 5 GHz / 2,4 GHz / MLO, permitiendo gestionar mejor la disponibilidad de la red y el consumo energético.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, asegurando que se adapte a sus necesidades y preferencias.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Este ajuste es fundamental para mantener registros exactos y para la correcta ejecución de las configuraciones basadas en el tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware instalada en ese momento. Puede resultar útil para solucionar problemas persistentes o para comenzar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para ver instrucciones detalladas.

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que facilita la resolución de problemas y la supervisión del rendimiento. Esta página incluye:

    * System Log: registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: registros relacionados con las operaciones y eventos del kernel.
    * Crash Log: registros de fallos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Cloud Log: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Nginx Log: registros del servidor web Nginx, si se utiliza en el router, que detallan el tráfico web y las operaciones del servidor.
    
    Además, la página incluye un botón Export Log, que le permite exportar todos los registros recopilados para su análisis por parte del soporte técnico. Esta función es muy valiosa para diagnosticar problemas complejos y obtener asistencia profesional.

    Consulte [Log](../../interface_guide/log.md) para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings ofrece acceso a opciones de configuración avanzada a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios con experiencia ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas de la interfaz. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para ver instrucciones detalladas.

## Declaración de Conformidad {#declaration-of-conformity}

Por la presente, GL TECHNOLOGIES (HONG KONG) LIMITED declara que el tipo de equipo de radio [Router Wi-Fi 7 BE9300, GL-BE9300] cumple los requisitos esenciales y demás disposiciones pertinentes de la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la siguiente dirección de internet: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
