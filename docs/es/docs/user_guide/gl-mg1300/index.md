# Guía de usuario de Mango 2 (GL-MG1300)

## Descripción general del producto

Mango 2 (GL-MG1300) es el primer minirouter de viaje Wi-Fi 5 de doble banda de GL.iNet, con un diseño ultrafino y portátil. Ofrece velocidades teóricas de 400 Mbps (2,4 GHz) y 866 Mbps (5 GHz), con una configuración MIMO 2×2. Además, incluye OpenVPN y WireGuard preinstalados, admite más de 30 servicios VPN, cifra automáticamente todo el tráfico de red y permite la administración remota mediante GoodCloud, combinando rendimiento, funcionalidad y seguridad.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## Contenido del paquete

- 1 x Mango 2 (GL-MG1300)
- 1 x Manual de usuario
- 1 x Cable de alimentación USB-C a USB-C
- 1 x Tarjeta de agradecimiento

## Cómo configurar Mango 2

Para configurar Mango 2, utilice uno de los cuatro métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering o Cellular. Siga los pasos que se indican a continuación.

### 1. Encender

Conecte el cable de alimentación USB Type-C al puerto de alimentación del router. Conecte el otro extremo a un adaptador de corriente de 5 V/2 A (no incluido) y enchúfelo a una toma eléctrica.

### 2. Conectar un dispositivo

Conecte un dispositivo (por ejemplo, un ordenador, portátil o smartphone) al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte el dispositivo al puerto LAN del router con un cable Ethernet.

- Wi-Fi

    En el dispositivo, vaya a Settings -> WLAN, busque el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. El nombre y la contraseña predeterminados aparecen en la etiqueta de la parte inferior del router.

### 3. Iniciar sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija el idioma, establezca la contraseña de administrador y haga clic en **Apply**.

Si cambia los datos de la red Wi-Fi, deberá volver a conectar el dispositivo a la red Wi-Fi del router con las credenciales actualizadas.

### 4. Configuración de Internet

**Nota:** Las siguientes instrucciones se aplican a quienes configuren el router mediante el GL.iNet Web Admin Panel. Si prefiere usar la aplicación de GL.iNet, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

Configure Mango 2 mediante uno de los métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering o Cellular. Para utilizar [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Conecte el puerto WAN de Mango 2 a un dispositivo aguas arriba, por ejemplo un módem, mediante un cable Ethernet.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de la lista de redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB de Mango 2 mediante un cable USB.
    2. En el dispositivo móvil, vaya a Settings y active **USB Tethering** o **Personal Hotspot**. En un iPhone, pulse **Trust This Device** si se le solicita.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Con Mango 2, puede conectar directamente un módem USB-C o utilizar un adaptador USB-C a USB-A para conectar un módem USB-A.

    Conecte un módem USB celular al puerto USB de Mango 2. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Conectarse a Internet mediante conexión celular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

---

A continuación se ofrece una descripción general de las funciones del panel de administración web de Mango 2.

## Wireless

La página Wireless permite configurar Main Network, Guest Network e IoT Network. Para cada tipo de red Wi-Fi, puede configurar de forma independiente las bandas de 5 GHz y 2,4 GHz. También puede habilitar y definir los ajustes básicos de cada banda, como el SSID Wi-Fi, el modo de seguridad, la contraseña y el BSSID aleatorio.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

## Clients

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, se muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y subida, el tráfico total y la posibilidad de bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GL.iNet Account"

    GL.iNet Account permite conectar y administrar sus dispositivos y servicios en la nube. Puede acceder de forma integrada a GoodCloud y a la glinet App para administrar su red de forma segura y cómoda desde cualquier lugar y en cualquier momento.

    Para configurar GL.iNet Account, consulte [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} permite acceder y administrar de forma remota los routers GL.iNet de manera sencilla.

=== "GoodPAS"

    GoodPAS es una función de red avanzada diseñada para ofrecer acceso remoto y administración de dispositivos sin interrupciones. Creado específicamente para integrarse con routers GL.iNet, GoodPAS utiliza el protocolo AmneziaWG con ofuscación de tráfico integrada para proporcionar conexiones seguras y estables. Amplía de forma segura su red doméstica a cualquier lugar, permitiéndole acceder a los recursos del hogar mientras todo el tráfico parece proceder de la dirección IP pública de su casa.

## VPN

Una VPN (red privada virtual) crea una conexión segura y cifrada entre el dispositivo y el servidor VPN. Añade una capa de privacidad y seguridad (cliente VPN) y permite acceder a una red remota (servidor VPN). Mango 2 admite OpenVPN y WireGuard.

=== "OpenVPN"

    Mango 2, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Red

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Subnet centraliza la administración de LAN, Guest Network, IoT Network y las redes VLAN personalizadas, lo que permite crear y administrar varias subredes para aislar distintos tipos de dispositivos o tráfico.

    Para configurar esta función, consulte [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La página Ethernet Port le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC de la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para gestionar los puertos Ethernet, consulte [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección frente a ataques de DNS rebinding y sobrescribir los ajustes DNS de todos los clientes, permitir que el DNS personalizado reemplace al DNS de la VPN, y configurar el modo de ajustes del servidor DNS como automático o especificar manualmente servidores DNS desde la conexión Ethernet.

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

=== "Network Acceleration"

    Network acceleration puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.

    Para configurar Network Acceleration, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Control de flujo

=== "Parental Control"

    Parental Control está diseñado para ayudarle a gestionar y controlar los dispositivos de sus hijos. Incluye la limitación del tiempo de pantalla y la restricción del acceso a determinados contenidos.

    Para configurar el control parental, consulte [Parental Control](../../interface_guide/parental_control.md).

## Seguridad

=== "Port Forwarding"

    Port forwarding permite que servidores remotos y dispositivos de Internet accedan a dispositivos de una red privada.

    Para configurar Port Forwarding, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Admin Access"

    Admin Access permite configurar diversos ajustes de seguridad diseñados para proteger la red y el router frente al acceso no autorizado.

    Para configurar esta función, consulte [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La página NAT Settings le permite activar o desactivar la funcionalidad Full Cone NAT y SIP ALG (Application Layer Gateway).

    Para configurar NAT Settings, consulte [NAT Settings](../../interface_guide/nat_settings.md).

## Aplicaciones

=== "Plug-ins"

    Un plug-in es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo personalizarlo y ampliar sus capacidades.

    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta útil para los usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage se refiere a una solución de almacenamiento de datos centralizada que permite que varios usuarios y dispositivos accedan a archivos y los compartan a través de una red.

    Para configurar Network Storage, consulte [Network Storage](../../interface_guide/network_storage.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

## Sistema

=== "Overview"

    La página Overview ofrece una vista general completa del estado actual del router y de sus métricas de rendimiento. En esta página puede ver:

    * Carga media de la CPU: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Uso de memoria: compruebe cuánta memoria del router está en uso para ayudar a gestionar los recursos.
    * Control LED: active o desactive los LED del router para personalizar los indicadores visuales del dispositivo.
    * Flash: vea el uso del almacenamiento flash del router para asegurarse de que hay espacio suficiente para el firmware y los datos de configuración.
    * Información del dispositivo: acceda a información detallada sobre el sistema del router, como tiempo de actividad, nombre del host, modelo, arquitectura, versión de OpenWrt, versión del kernel, ID del dispositivo, MAC del dispositivo y S/N del dispositivo.
    * Almacenamiento externo: compruebe el estado de los dispositivos de almacenamiento externo conectados al router, como unidades USB o tarjetas TF.

    Estas funciones proporcionan información y controles esenciales para ayudarle a gestionar y supervisar el funcionamiento del router de forma eficaz.

    Consulte [Overview](../../interface_guide/system_overview.md) para ver instrucciones detalladas.

=== "Admin Password"

    La página Admin Password permite establecer o cambiar la contraseña de la interfaz administrativa del router.

    La contraseña de administrador debe cumplir los siguientes requisitos:

    * Un mínimo de 10 caracteres y un máximo de 63.
    * Se permiten letras (se distingue entre mayúsculas y minúsculas), números y los símbolos `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Se requieren al menos dos de estos tipos: letras mayúsculas, letras minúsculas, números y símbolos.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: comprueba automáticamente si hay una nueva versión de firmware y la instala directamente desde el servidor del fabricante, simplificando el proceso.
    * Firmware Local Upgrade: permite cargar manualmente un archivo de firmware desde el ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

---

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Control LED: active o desactive los LED del router para personalizar los indicadores visuales del dispositivo.
    * Reinicio programado: configure el router para que se reinicie automáticamente en intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi: establezca un horario para controlar las bandas Wi-Fi de 5 GHz / 2,4 GHz , permitiendo gestionar mejor la disponibilidad de la red y el consumo energético.

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

## Declaración de conformidad

Por la presente, GL TECHNOLOGIES (HONG KONG) LIMITED declara que el tipo de equipo radioeléctrico [Router mini de viaje doble banda, GL‑MG1300] cumple los requisitos esenciales y demás disposiciones pertinentes de la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la siguiente dirección de internet: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.