# Guía de usuario de Slate AX (GL-AXT1800)

## Descripción general del producto

Slate AX (GL-AXT1800) es el primer router de viaje Wi-Fi 6 diseñado por GL.iNet. Incorpora un procesador de cuatro núcleos IPQ6000 a 1,2 GHz y funciona con OpenWrt 21.02. Gracias a la última tecnología Wi-Fi 6, puede disfrutar de mayor capacidad para dispositivos conectados y una velocidad inalámbrica más rápida tanto en viajes como en casa.

![gl-axt1800 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/hardware_info/gl-axt1800_interface.jpg){class="glboxshadow"}

## Contenido del paquete

- 1 x Slate AX (GL-AXT1800)
- 1 x Manual del usuario
- 1 x Cable Ethernet
- 1 x Tarjeta de agradecimiento
- 1 x Tarjeta de garantía
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

![gl-axt1800 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/first_time_setup/axt1800_unboxing.jpg){class="glboxshadow"}

## Cómo configurar Slate AX

Vea el video de configuración o siga los pasos indicados a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f7DYULL6ZSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encendido

Una el adaptador de corriente de dos piezas. Conéctelo al router y enchúfelo a una toma de corriente. El router se encenderá automáticamente.

### 2. Conectar un dispositivo

Conecte un dispositivo, por ejemplo un ordenador, portátil o smartphone, al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

- Wi-Fi

    En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. Puede encontrar el nombre y la contraseña predeterminados impresos en la etiqueta inferior del router.

### 3. Iniciar sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma y establezca la contraseña de administrador; a continuación, haga clic en **Apply**.

Al confirmar los datos de Wi‑Fi, tenga en cuenta que, si cambia la información de Wi‑Fi, deberá volver a conectar su dispositivo al Wi‑Fi del router utilizando las credenciales actualizadas.

### 4. Configuración de Internet

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router a través del panel de administración web de GL.iNet. Si prefiere usar la aplicación GL.iNet, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

Configure su Slate AX utilizando uno de los métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Si desea usar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_ethernet.png){class="glboxshadow"}

    Conecte un cable Ethernet entre el puerto WAN del router y un dispositivo ascendente, como un módem.
    
    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_repeater.png){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de entre las redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.
    
    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB del router mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.
    
    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.
    
=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del router. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

## Cómo configurar una VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad, como cliente VPN, y permite acceder a una red remota, como servidor VPN. Slate AX, al igual que otros routers GL.iNet, es compatible con OpenVPN y WireGuard. Además, es compatible con Tor.

=== "OpenVPN" 

    Slate AX, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una seguridad sólida. Para configurar OpenVPN, siga estos tutoriales:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate AX, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad. Para configurar WireGuard, siga estos tutoriales:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico de Internet a través de una serie de servidores (nodos) gestionados por voluntarios para ocultar la ubicación y el uso del usuario, dificultando el rastreo de la actividad en línea.
    
    * [How to set up Tor](../../interface_guide/tor.md).

---

## Inalámbrico y clientes

=== "Wireless"

    La página Wireless le permite configurar los ajustes de las redes Wi-Fi de 5 GHz y 2,4 GHz, incluidos la activación del Wi-Fi, la potencia de transmisión (TX), el nombre de la red Wi-Fi (SSID), la activación del BSSID aleatorio, la selección del modo de seguridad y contraseña, la visibilidad del SSID, el modo Wi-Fi, el ancho de banda y el canal.

    Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y carga, el tráfico total, y permite bloquear el cliente o realizar otras acciones.

    Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    El servicio [GoodCloud](https://www.goodcloud.xyz){target="_blank"} de GL.iNet proporciona una forma sencilla de acceder y gestionar remotamente routers GL.iNet.
    
    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una plataforma de red avanzada diseñada para proporcionar redes remotas y gestión remota de dispositivos de forma fluida. Desarrollada específicamente para la integración con routers GL.iNet, AstroWarp permite la gestión integral de dispositivos en redes completas, posibilitando el control de dispositivos superiores e inferiores. Con un enfoque en la gestión a nivel de red y compatibilidad futura con control a nivel de hardware, AstroWarp ofrece una solución más robusta y fiable para gestionar dispositivos y mantener redes seguras y estables.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

## Aplicaciones

=== "Plug-ins"

    Un plug-in es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo la personalización y mejora de sus capacidades.
    
    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta útil para los usuarios que necesitan una dirección IP estática para acceder a una red remota.
    
    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    El almacenamiento en red es una solución de almacenamiento centralizado que permite a múltiples usuarios y dispositivos acceder y compartir archivos a través de una red.
    
    Para configurar el almacenamiento en red, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores a nivel de red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a la red doméstica.
    
    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control está diseñado para ayudarle a gestionar y controlar los dispositivos de sus hijos. Incluye la limitación del tiempo de pantalla y la restricción del acceso a determinados contenidos.

    Para configurar Parental Control, consulte [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier es una solución de redes definidas por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.
    
    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.
    
    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

## Configuración de red

=== "Port Forwarding"

    El reenvío de puertos permite que servidores y dispositivos remotos en Internet accedan a dispositivos en una red privada.
    
    Para configurar el reenvío de puertos, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión actual, el router cambiará automáticamente a otra conexión a Internet. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o red de área local, es una red que conecta ordenadores y dispositivos en un área geográfica limitada, como un hogar u oficina. Permite la transferencia de datos a alta velocidad y el uso compartido de recursos, posibilitando que los dispositivos se comuniquen eficientemente entre sí.
    
    Para configurar LAN, consulte [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Permite establecer una subred dentro de los rangos de direcciones privadas IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, especificar las direcciones IP de puerta de enlace y máscara de red, y configurar ajustes de seguridad como el aislamiento de AP para la red de invitados.

    Para configurar la red de invitados, consulte [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección contra ataques de reenlace DNS y anular la configuración DNS de todos los clientes, permitir que el DNS personalizado anule el DNS de la VPN, y configurar el modo de ajustes del servidor DNS en automático o especificar manualmente servidores DNS desde la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "Port Management"

    La página Port Management le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC para la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para gestionar los puertos Ethernet, consulte [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    El modo de red hace referencia a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.
    
    Para configurar Network Mode, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Protocolo de Internet versión 6, es la versión más reciente del Protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones enormemente mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, esencial para dar cabida al creciente número de dispositivos conectados a Internet.
    
    Para configurar IPv6, consulte [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in Gateway amplía la funcionalidad del router principal con funciones que podría no tener, incluidas AdGuard Home, DNS cifrado y cliente VPN.
    
    Para configurar Drop-in Gateway, consulte los siguientes enlaces:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en conmutadores Ethernet para gestionar y controlar el tráfico multicast.
    
    Para configurar IGMP Snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    La página NAT Settings le permite activar o desactivar Full Cone NAT y la funcionalidad SIP ALG (Application Layer Gateway).

    Para configurar NAT Settings, consulte [NAT Settings](../../interface_guide/nat_settings.md).

## Configuración del sistema

=== "Overview"

    La página Overview ofrece una visión completa del estado actual del router y de sus métricas de rendimiento. En esta página puede ver:

    * CPU Average Load: Supervise la carga media de la CPU del router, lo que ayuda a evaluar el rendimiento e identificar posibles cuellos de botella.
    * Memory Usage: Compruebe cuánta memoria del router está en uso, lo que facilita la gestión de recursos.
    * LED Control: Active o desactive las luces LED del router, lo que permite personalizar los indicadores visuales del dispositivo.
    * Flash Usage: Consulte el uso del almacenamiento flash del router, asegurándose de que haya espacio suficiente para firmware y datos de configuración.
    * Device Info: Acceda a información detallada sobre el sistema del router, incluidos el tiempo de actividad, el nombre de host, el modelo, la arquitectura, la versión de OpenWrt, la versión del kernel, el ID del dispositivo, la MAC del dispositivo y el número de serie.
    * External Storage: Compruebe el estado de los dispositivos de almacenamiento externo conectados al router, como unidades USB o tarjetas TF.
    
    Estas funciones proporcionan información y controles esenciales, ayudándole a gestionar y supervisar eficazmente el funcionamiento del router.

    Consulte [Overview](../../interface_guide/system_overview.md) para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejoras de rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: Comprueba e instala automáticamente la última versión del firmware directamente desde el servidor del fabricante, simplificando el proceso de actualización.
    * Firmware Local Upgrade: Carga manualmente un archivo de firmware desde su ordenador para actualizar el router, proporcionando control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las últimas mejoras y correcciones.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones clave de esta página se incluyen:

    * LED Display Schedule: Establezca una programación para encender o apagar automáticamente las luces LED del router, reduciendo la contaminación lumínica en determinadas horas.
    * Schedule Reboot: Configure el router para reiniciarse automáticamente a intervalos especificados, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Wi-Fi Status Schedule: Establezca una programación para controlar la banda Wi-Fi de 5 GHz / 2,4 GHz, lo que permite una mejor gestión de la disponibilidad de la red y del consumo energético.
    
    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, garantizando que se adapte a sus necesidades y preferencias específicas.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Esta configuración es fundamental para mantener registros exactos y para la correcta ejecución de configuraciones basadas en tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

=== "Toggle Button Settings"

    La página Toggle Button Settings le permite configurar el interruptor físico del router, lo que permite asignar funciones específicas al botón para un acceso y control rápidos. Esta función proporciona accesos directos prácticos para tareas y ajustes habituales, mejora la experiencia de uso y simplifica la gestión del router.

    Consulte [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) para ver instrucciones detalladas.

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y los eventos del router, ayudando en la resolución de problemas y la supervisión del rendimiento. Esta página incluye:

    * System Log: Registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: Registros relacionados con las operaciones y eventos del kernel.
    * Crash Log: Registros de fallos del sistema y errores, útiles para diagnosticar problemas críticos.
    * Cloud Log: Registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Nginx Log: Registros del servidor web Nginx, si lo utiliza el router, que detallan el tráfico web y las operaciones del servidor.
    
    Además, la página incluye un botón Export Log, que le permite exportar todos los registros recopilados para que el soporte técnico los analice. Esta función es muy valiosa para diagnosticar problemas complejos y obtener asistencia profesional.

    Consulte [Log](../../interface_guide/log.md) para ver instrucciones detalladas.

---

=== "Security"

    La página Security le permite configurar varios ajustes de seguridad para proteger su red y router frente a accesos no autorizados. Esta página incluye opciones para:

    * Admin Password: Establezca o cambie la contraseña de la interfaz administrativa del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.
    * Local Access Control: Gestione y restrinja el acceso a la interfaz del router desde los dispositivos conectados a su red local.
    * Remote Access Control: Configure y restrinja el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, mejorando la seguridad frente a amenazas externas.
    * Open Ports on Router: Controle qué puertos están abiertos en el router, limitando posibles vulnerabilidades y accesos no autorizados.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware actualmente instalada. Esto puede resultar útil para solucionar problemas persistentes o para comenzar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings proporciona acceso a opciones de configuración avanzadas a través de la interfaz OpenWrt LuCI, permitiendo a los usuarios experimentados ajustar con precisión la configuración y las funciones del router más allá de las opciones de la interfaz básica. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para ver instrucciones detalladas.
