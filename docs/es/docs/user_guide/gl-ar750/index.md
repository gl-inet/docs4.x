# Guía de usuario de Creta (GL-AR750)

## Descripción general del producto

Creta (GL-AR750) es un router AC de doble banda para viajes. La compatibilidad simultánea con doble banda admite hasta 733 Mbps (2,4 GHz: 300 Mbps + 5 GHz: 433 Mbps) de velocidad de transmisión inalámbrica. Creta puede convertir una red pública en una Wi-Fi privada para navegar de forma segura. El almacenamiento externo admite MicroSD de hasta 128 GB. OpenWrt/LEDE y OpenVPN vienen preinstalados. De este modo, Creta ofrece a los usuarios preocupados por la privacidad una VPN rápida y sencilla que utiliza criptografía de última generación.

![ar750 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/product_info/ar750_overview.png){class="glboxshadow"}

### Especificaciones

[Especificaciones del GL-AR750](https://www.gl-inet.com/products/gl-ar750/#specs){target="_blank"}

## Cómo configurar Creta

Para configurar Creta, utilizará uno de los cuatro métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Vea el video de configuración o siga los pasos indicados a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Este video usa un router GL.iNet diferente para mostrar la configuración, pero los pasos son los mismos para Creta y otros modelos de router.)</small>

### 1. Encender Creta

Conecte el cable de alimentación Micro USB al puerto de alimentación del router. Asegúrese de utilizar un adaptador de corriente estándar de 5 V/2 A.

!!! Note

    No se admite la conexión en caliente de la tarjeta TF. Si desea usar una tarjeta TF, insértela antes de encender el router.

### 2. Conectar su dispositivo a Creta

Conecte su ordenador o dispositivo móvil al router mediante Wi-Fi o Ethernet.

=== "Wi-Fi"

    En su dispositivo, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. (Puede encontrar el nombre y la contraseña predeterminados impresos en la etiqueta del router.)

=== "Ethernet"

    Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

### 3. Conectar Creta a Internet

**Nota:** Las siguientes instrucciones están dirigidas a quienes conectan el router a Internet mediante el panel de administración web. Si prefiere usar la aplicación GL.iNet en lugar del panel de administración web, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

#### 1. Iniciar sesión en el panel de administración web del router

En la barra de direcciones del navegador web, introduzca `192.168.8.1`. Elija su idioma y haga clic en **Next**. Establezca la contraseña de administrador y haga clic en **Apply**.

#### 2. Configurar el método de conexión a Internet

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/ethernet.png){class="glboxshadow"}
    
    Conecte un cable Ethernet al puerto WAN del router y a un dispositivo ascendente, como un módem. Si se conecta a Internet correctamente, aparecerá un punto verde junto a "Ethernet."

    Consulte [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/repeater.png){class="glboxshadow"}

    1. En la pantalla principal del panel de administración web, localice la sección "Repeater" y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi.
    3. Introduzca la contraseña de la red y haga clic en **Apply**.
    
    Si se conecta a Internet correctamente, aparecerá un punto verde junto al nombre de la red Wi-Fi.

    Consulte [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/tethering.png){class="glboxshadow"}

    1. Conecte su smartphone al router mediante un cable USB y active la compartición de red en el menú Hotspot personal de la configuración.
    2. En la pantalla principal del panel de administración web, localice la sección "Tethering" y haga clic en **Connect**.
    3. Si se conecta a Internet correctamente, aparecerá un punto verde junto a "Tethering."

    Consulte [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/usb_modem.png){class="glboxshadow"}

    1. Inserte un módem USB con capacidad celular en el puerto USB del router.
    2. En la pantalla principal del panel de administración web, localice la sección "Cellular" y haga clic en **Connect**.
    3. Si se conecta a Internet correctamente, aparecerá un punto verde junto a "Cellular."

    Consulte [Connect to the Internet via a USB modem](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

**Nota:** Si desea usar la función Multi-WAN, deberá configurar más de un método de conexión a Internet.

---

## Cómo configurar una VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad, como cliente VPN, y permite acceder a una red remota, como servidor VPN. Creta, al igual que otros routers GL.iNet, es compatible con OpenVPN y WireGuard.

=== "OpenVPN" 

    Creta, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una seguridad sólida. Para configurar OpenVPN, siga estos tutoriales:

    * [How to set up an OpenVPN client](../../interface_guide/openvpn_client.md)
    * [How to set up an OpenVPN server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Creta, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad. Para configurar WireGuard, siga estos tutoriales:

    * [How to set up a WireGuard client](../../interface_guide/wireguard_client.md)
    * [How to set up a WireGuard server](../../interface_guide/wireguard_server.md)

---

## Más aplicaciones

=== "Plug-ins"

    Plug-ins son funciones adicionales que amplían la funcionalidad del router. Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta especialmente útil para los usuarios que necesitan una dirección IP estática para acceder a una red remota. Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    El servicio de gestión en la nube [GoodCloud](https://www.goodcloud.xyz){target="_blank"} de GL.iNet proporciona una forma sencilla de acceder y gestionar remotamente routers GL.iNet. Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

---

## Configuración de red

=== "Firewall"

    La página Firewall proporciona mejoras de seguridad esenciales para su red. Incluye funciones como Port Forwarding, Open Ports y DMZ. Estas herramientas le permiten gestionar y personalizar el flujo de tráfico de su red y reforzar su seguridad.

    * Port Forwarding: Redirige tráfico específico de Internet a dispositivos concretos dentro de su red, lo que permite acceder a servicios como servidores de juegos o servidores web.
    * Open Ports: Supervisa y controla qué puertos del router están abiertos, lo que ayuda a evitar accesos no autorizados y posibles amenazas de seguridad.
    * DMZ (Demilitarized Zone): Coloca un dispositivo fuera del firewall principal, permitiéndole acceso sin restricciones a Internet mientras protege el resto de la red frente a amenazas potenciales.

    Para ver instrucciones detalladas y más información, consulte [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión actual, el router cambiará automáticamente a otra conexión a Internet. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La página LAN le permite gestionar y configurar la red de área local del router. Entre las funciones clave disponibles en esta página se incluyen:

    * Router IP Address: Modifique la dirección IP del router para adaptarla mejor a la configuración de la red.
    * Netmask: Configure la máscara de subred de la red, que determina su tamaño y el rango de direcciones IP.
    * DHCP: Active o configure el protocolo Dynamic Host Configuration Protocol, que asigna automáticamente direcciones IP a los dispositivos de la red.
    * Address Reservation: Reserve direcciones IP específicas para determinados dispositivos, garantizando que siempre reciban la misma dirección IP del servidor DHCP.

    Para ver instrucciones detalladas y más información, consulte [LAN](../../interface_guide/lan.md).

---

=== "DNS"

    La página DNS ofrece opciones para personalizar la configuración del sistema de nombres de dominio del router, mejorando tanto la seguridad como el rendimiento. Entre las funciones clave disponibles en esta página se incluyen:

    * Encrypted DNS: Configure DNS cifrado para proteger sus datos de navegación frente a supervisión o manipulación, garantizando privacidad y seguridad.
    * Manual DNS: Configure manualmente los servidores DNS que prefiera, lo que permite un control personalizado sobre las consultas DNS y tiempos de resolución potencialmente más rápidos.
    * DNS Proxy: Active un proxy DNS para enrutar las solicitudes DNS de sus dispositivos a través de un servidor DNS específico, añadiendo una capa adicional de control sobre el tráfico DNS.

    Estas opciones le permiten optimizar el rendimiento y la seguridad DNS de su red según sus necesidades específicas.

    Para ver instrucciones detalladas y más información, consulte [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    La página Network Mode le permite configurar el router para funcionar en distintos modos, ofreciendo flexibilidad para cubrir varias necesidades de red. Los modos disponibles incluyen:

    * Router: Funciona como un router estándar, gestionando el tráfico entre la red local e Internet, y proporcionando funciones como NAT, firewall y DHCP.
    * Access Point: Funciona como punto de acceso, ampliando la red cableada existente mediante conectividad inalámbrica sin enrutar tráfico.
    * Extender: Funciona como extensor de alcance, reforzando la señal de la red inalámbrica existente para cubrir una zona mayor y eliminar zonas muertas.
    * WDS (Wireless Distribution System): Similar a Extender; elija WDS si su router principal admite el modo WDS.

    Para ver instrucciones detalladas y más información, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    La página IPv6 le permite configurar los ajustes IPv6 de la red, proporcionando compatibilidad con el protocolo de Internet más reciente. En esta página puede activar IPv6 y seleccionar entre cuatro modos distintos según las necesidades de su red:

    * Native: Obtiene una dirección IPv6 directamente del ISP, permitiendo conectividad IPv6 nativa de forma directa y eficiente.
    * Passthrough: Permite que el tráfico IPv6 atraviese el router hasta los dispositivos de la red, actuando como puente sin que el router gestione el enrutamiento IPv6 por sí mismo.
    * NAT6: Utiliza Network Address Translation para IPv6 (NAT6) para traducir entre direcciones IPv6 internas y externas, de forma similar a cómo funciona NAT para IPv4.
    * Static IPv6: Configura manualmente una dirección IPv6 estática para el router, proporcionando una dirección fija para una conectividad constante y una gestión más sencilla de los servicios de red.

    Estas opciones le ayudan a aprovechar las ventajas de IPv6, como un espacio de direcciones mayor, funciones de seguridad mejoradas y mejor rendimiento.

    Para ver instrucciones detalladas y más información, consulte [IPv6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    La página MAC Address le permite ver y gestionar las direcciones MAC asociadas al router. Entre las funciones clave disponibles en esta página se incluyen:

    * Factory Default: Muestra las direcciones MAC predeterminadas para los modos Ethernet y Repeater del router, lo que sirve de referencia para la configuración original del hardware.
    * Clone: Clona la dirección MAC de un dispositivo cliente específico. Esto resulta especialmente útil en entornos donde el acceso a la red está restringido a determinados dispositivos.
    * Manual: Especifique manualmente una dirección MAC personalizada para el router. Además, puede usar el botón Random para generar una dirección MAC aleatoria, proporcionando flexibilidad y mayor privacidad.

    Estas funciones le permiten gestionar eficazmente las direcciones MAC del router, garantizando compatibilidad y flexibilidad en distintos entornos de red.

    Para ver instrucciones detalladas y más información, consulte [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad del router principal con funciones que podría no tener, incluidas AdGuard Home, DNS cifrado y VPN. Para configurar Drop-in Gateway, consulte [How to set up Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    La página IGMP Snooping le permite configurar opciones que optimizan la gestión del tráfico multicast dentro de la red. IGMP Snooping escucha y extrae información de paquetes del protocolo IGMP, estableciendo y manteniendo tablas de reenvío multicast de capa 2. Esto garantiza que los datos de grupos multicast se reenvíen únicamente a los hosts que se han unido al grupo multicast, evitando que tráfico multicast no deseado llegue a otros hosts.

    Estas opciones ayudan a optimizar el rendimiento y la eficiencia de la red, especialmente en entornos con tráfico multicast importante, como streaming de video o juegos en línea.

    Para ver instrucciones detalladas y más información, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Configuración del sistema

=== "Overview"

    La página Overview ofrece una visión completa del estado actual del router y de sus métricas de rendimiento. En esta página puede ver:

    * CPU Average Load: Supervise la carga media de la CPU del router, lo que ayuda a evaluar el rendimiento e identificar posibles cuellos de botella.
    * Memory Usage: Compruebe cuánta memoria del router está en uso, lo que facilita la gestión de recursos.
    * Flash Usage: Consulte el uso del almacenamiento flash del router, asegurándose de que haya espacio suficiente para firmware y datos de configuración.
    * LED Control: Active o desactive las luces LED del router, lo que permite personalizar los indicadores visuales del dispositivo.
    * System Info: Acceda a información detallada sobre el sistema del router, incluida la versión del firmware, el tiempo de actividad y el estado de la red.
    
    Estas funciones proporcionan información y controles esenciales, ayudándole a gestionar y supervisar eficazmente el funcionamiento del router.

    Para ver instrucciones detalladas y más información, consulte [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejoras de rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Online Upgrade: Comprueba e instala automáticamente la última versión del firmware directamente desde el servidor del fabricante, simplificando el proceso de actualización.
    * Local Upgrade: Carga manualmente un archivo de firmware desde su ordenador para actualizar el router, proporcionando control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las últimas mejoras y correcciones.

    Para ver instrucciones detalladas y más información, consulte [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones clave de esta página se incluyen:

    * LED Display Schedule: Establezca una programación para encender o apagar automáticamente las luces LED del router, reduciendo la contaminación lumínica en determinadas horas.
    * Schedule Reboot: Configure el router para reiniciarse automáticamente a intervalos especificados, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * 5GHz Wi-Fi Status Schedule: Establezca una programación para activar o desactivar la banda Wi-Fi de 5 GHz en determinados momentos, optimizando el uso de la red y la eficiencia energética.
    * 2.4GHz Wi-Fi Status Schedule: Establezca una programación para controlar la banda Wi-Fi de 2,4 GHz, lo que permite una mejor gestión de la disponibilidad de la red y del consumo energético.
    
    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, garantizando que se adapte a sus necesidades y preferencias específicas.

    Para ver instrucciones detalladas y más información, consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    La página Admin Password le permite establecer o cambiar la contraseña de la interfaz administrativa del router, garantizando que solo los usuarios autorizados puedan acceder y modificar la configuración del router. Esta contraseña es fundamental para mantener la seguridad e integridad de la red, protegiéndola frente a accesos no autorizados y cambios de configuración.

    Para ver instrucciones detalladas y más información, consulte [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Esta configuración es fundamental para mantener registros exactos y para la correcta ejecución de configuraciones basadas en tiempo.

    Para ver instrucciones detalladas y más información, consulte [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La página Toggle Button Settings le permite configurar el interruptor físico del router, lo que permite asignar funciones específicas al botón para un acceso y control rápidos. Esta función proporciona accesos directos prácticos para tareas y ajustes habituales, mejora la experiencia de uso y simplifica la gestión del router.

    Para ver instrucciones detalladas y más información, consulte [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y los eventos del router, ayudando en la resolución de problemas y la supervisión del rendimiento. Esta página incluye:

    * System Log: Registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: Registros relacionados con las operaciones y eventos del kernel.
    * Crash Log: Registros de fallos del sistema y errores, útiles para diagnosticar problemas críticos.
    * Cloud Log: Registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Nginx Log: Registros del servidor web Nginx, si lo utiliza el router, que detallan el tráfico web y las operaciones del servidor.
    
    Además, la página incluye un botón Export Log, que le permite exportar todos los registros recopilados para que el soporte técnico los analice. Esta función es muy valiosa para diagnosticar problemas complejos y obtener asistencia profesional.

    Para ver instrucciones detalladas y más información, consulte [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware actualmente instalada. Esto puede resultar útil para solucionar problemas persistentes o para comenzar de nuevo con la configuración predeterminada del firmware actual.

    Para ver instrucciones detalladas y más información, consulte [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La página Advanced Settings proporciona acceso a opciones de configuración avanzadas a través de la interfaz OpenWrt LuCI, permitiendo a los usuarios experimentados ajustar con precisión la configuración y las funciones del router más allá de las opciones de la interfaz básica. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Para ver instrucciones detalladas y más información, consulte [Advanced Settings](../../interface_guide/advanced_settings.md).
