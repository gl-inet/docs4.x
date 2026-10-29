# Guía de usuario de Beryl AX (GL-MT3000) {#beryl-ax-gl-mt3000-user-guide}

## Descripción general del producto {#product-overview}

Beryl AX (GL-MT3000) es un router de viaje de bolsillo AX3000 que utiliza el protocolo Wi-Fi 6. Es una versión mejorada de Beryl (GL-MT1300). Funciona con un procesador de doble núcleo MT7981B a 1,3 GHz y ofrece más del doble de velocidad Wi-Fi total. Está diseñado para dar soporte a familias con uso intensivo de Wi-Fi y, al mismo tiempo, mantiene un diseño compacto ideal para viajar.

![gl-mt3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/hardware_info/mt3000_interface.jpg){class="glboxshadow"}

## Contenido del paquete {#package-contents}

- 1 x Beryl AX (GL-MT3000)
- 1 x Manual del usuario
- 1 x Cable Ethernet
- 1 x Tarjeta de agradecimiento
- 1 x Tarjeta de garantía
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

![gl-MT3000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/first_time_setup/mt3000_unboxing.jpg){class="glboxshadow"}

## Cómo configurar Beryl AX {#how-to-set-up-beryl-ax}

Vea este vídeo de configuración o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encender {#1-power-on}

Ensamble las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. El router se iniciará automáticamente.

### 2. Conectar un dispositivo {#2-connect-device}

Conecte un dispositivo, por ejemplo un ordenador, un portátil o un smartphone, al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

- Wi-Fi

    En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. Puede encontrar el nombre de red y la contraseña predeterminados impresos en la etiqueta del router.

### 3. Iniciar sesión en el panel de administración web {#3-log-in-to-web-admin-panel}

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma, establezca la contraseña de administrador y haga clic en **Apply**.

Al confirmar los datos de Wi‑Fi, tenga en cuenta que, si cambia la información de la red, tendrá que volver a conectar su dispositivo al Wi‑Fi del router con las credenciales actualizadas.

### 4. Configuración de Internet {#4-internet-setup}

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router desde el panel de administración web de GL.iNet. Si prefiere usar la aplicación de GL.iNet, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

Configure su Beryl AX con uno de los métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_ethernet.png){class="glboxshadow"}

    Conecte un cable ethernet entre el puerto WAN del router y un dispositivo aguas arriba, por ejemplo un módem.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_repeater.png){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de la lista de redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB del router mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3000/internet/mt3000_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del router. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Conectarse a Internet mediante conexión celular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

## DNS {#dns}

Los ajustes DNS del router controlan cómo se traducen los nombres de dominio en direcciones IP. Esta página permite utilizar los servidores DNS obtenidos automáticamente de los dispositivos de nivel superior o definir servidores personalizados. También puede configurar opciones DNS y editar reglas de hosts estáticos.

Para obtener más información, consulte [DNS](../../interface_guide/dns_v4.11.md).

## Wireless {#wireless}

La página Wireless le permite configurar ajustes para las redes Wi-Fi de 5 GHz y 2,4 GHz, incluyendo activar o desactivar el Wi-Fi, ajustar la potencia TX, definir el nombre de la red Wi-Fi (SSID), activar o desactivar el BSSID aleatorio, seleccionar el modo de seguridad Wi-Fi, configurar la contraseña Wi-Fi, ajustar la visibilidad del SSID y elegir el modo Wi-Fi, el ancho de banda y el canal.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh es una función basada en el estándar Wi-Fi EasyMesh™ que amplía la cobertura Wi-Fi de todo el hogar y permite una itinerancia fluida. Si tiene varios routers GL.iNet, configure uno como router principal y los demás como nodos mesh para desplazarse por su hogar sin interrupciones en la conexión Wi-Fi.

Para obtener más información, consulte [Mesh](../../interface_guide/mesh.md).

## Clients {#clients}

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, se muestra el nombre del dispositivo, el tipo de conexión (es decir, mediante ethernet o Wi-Fi), las direcciones IP y MAC, las velocidades de descarga y subida, el tráfico total, y ofrece la posibilidad de reservar IP, bloquear el cliente o realizar otras acciones.

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

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad, como cliente VPN, y permite acceder a una red remota, como servidor VPN. Beryl AX, al igual que otros routers GL.iNet, es compatible con OpenVPN y WireGuard.

=== "OpenVPN"

    Beryl AX, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Beryl AX, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La página LAN permite configurar y gestionar de forma centralizada la red principal, la red de invitados, la red IoT y las redes VLAN personalizadas. Puede crear y gestionar varias subredes para aislar distintos tipos de dispositivos o tráfico.

=== "Ethernet Port"

    La página Ethernet Port le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC para la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para gestionar los puertos Ethernet, consulte [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, es la versión más reciente del protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones muchísimo mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

---

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para configurar IGMP Snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

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

=== "Network Quality"

    El panel Network Quality supervisa la calidad de la conexión a internet en tiempo real. Evalúa la capacidad de respuesta, la latencia y el rendimiento DNS, y detecta caídas de conexión y pérdida de paquetes. Estas métricas ayudan a identificar inestabilidades de la red y problemas de conectividad que las pruebas de ancho de banda por sí solas pueden no revelar.

    Para obtener más información, consulte [Network Quality](../../interface_guide/network_quality.md).

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

    Parental Control está diseñado para ayudarle a gestionar y controlar los dispositivos de sus hijos. Incluye la limitación del tiempo de pantalla y la restricción del acceso a determinados contenidos.

    Para configurar el control parental, consulte [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Seguridad {#security}

=== "Security Scan"

    Security Scan realiza una comprobación de seguridad del router. Evalúa sus ajustes de seguridad y genera una puntuación de seguridad, junto con alertas de riesgo y sugerencias de optimización. Puede ajustar la configuración según los resultados del análisis para mejorar la seguridad del router.

    Para obtener más información, consulte [Security Scan](../../interface_guide/security_scan.md).

=== "ACL"

    ACL, abreviatura de Access Control List, permite crear reglas para administrar el tráfico de red en función de los protocolos de conexión, las direcciones de los dispositivos y los puertos. Controla si se permite o bloquea el acceso a la red. Si varias reglas ACL entran en conflicto, el sistema aplica la que tenga mayor prioridad.

    Para obtener más información, consulte [ACL](../../interface_guide/acl.md).

=== "Port Forwarding"

    Port forwarding permite que servidores remotos y dispositivos de Internet accedan a dispositivos de una red privada.

    Para configurar Port Forwarding, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

---

=== "UPnP"

    UPnP (Universal Plug and Play) permite que los dispositivos y aplicaciones LAN compatibles soliciten automáticamente asignaciones de puertos en los routers GL.iNet. Estas asignaciones reenvían el tráfico WAN entrante a direcciones IP y puertos LAN específicos, permitiendo que los clientes externos se conecten a servicios locales sin configurar manualmente reglas de reenvío de puertos.

    Para obtener más información, consulte [UPnP](../../interface_guide/upnp.md).

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

    Un plugin es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo personalizarlo y ampliar sus capacidades.

    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Asigna un nombre de dominio a la dirección IP pública dinámica de su router, de modo que pueda acceder a su red de forma remota sin necesidad de una dirección IP estática.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage se refiere a una solución de almacenamiento de datos centralizada que permite que varios usuarios y dispositivos accedan a archivos y los compartan a través de una red.

    Para configurar Network Storage, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores para toda la red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a una red doméstica.

    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico de Internet a través de una serie de servidores operados por voluntarios (nodos) para ocultar la ubicación y el uso del usuario, lo que dificulta el rastreo de la actividad en línea.

    Para configurar Tor, consulte [Tor](../../interface_guide/tor.md).

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

---

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de visualización LED: establezca un horario para encender o apagar automáticamente los LED del router y reducir la contaminación lumínica en determinadas horas.
    * Reinicio programado: configure el router para que se reinicie automáticamente en intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi: establezca un horario para controlar las bandas Wi-Fi de 5 GHz / 2,4 GHz, permitiendo gestionar mejor la disponibilidad de la red y el consumo energético.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, asegurando que se adapte a sus necesidades y preferencias.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Este ajuste es fundamental para mantener registros exactos y para la correcta ejecución de las configuraciones basadas en el tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

=== "Toggle Button Settings"

    La página Toggle Button Settings le permite configurar el interruptor físico del router y asignarle funciones específicas para un acceso y control rápidos. Esta función ofrece accesos directos cómodos para tareas y ajustes habituales, mejorando la experiencia de uso y simplificando la gestión del router.

    Consulte [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) para ver instrucciones detalladas.

---

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

Por la presente, GL TECHNOLOGIES (HONG KONG) LIMITED declara que el tipo de equipo de radio [Router Wi-Fi 6 AX3000, GL-MT3000] cumple con los requisitos esenciales y demás disposiciones pertinentes de la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la siguiente dirección de internet: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
