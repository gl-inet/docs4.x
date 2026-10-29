# Guía de usuario de Slate Plus (GL-A1300) {#slate-plus-gl-a1300-user-guide}

## Descripción general del producto {#product-overview}

Slate Plus (GL-A1300) es un router de viaje de tamaño bolsillo con una CPU potente, optimizada para la estabilidad de la red y para procesar el cifrado VPN de forma eficiente. Incluye nuestras funciones de seguridad más recientes y ejecuta la última versión del sistema operativo OpenWrt. Está diseñado para viajeros frecuentes con una alta demanda de uso de redes VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Contenido del paquete {#package-contents}

Tenga en cuenta que el adaptador incluido en el paquete depende del país de envío.

El paquete incluye:

- 1 manual de usuario
- 1 Slate Plus (GL-A1300)
- 1 cable Ethernet
- 1 x Tarjeta de agradecimiento
- 1 tarjeta de garantía
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Cómo configurar Slate Plus {#how-to-set-up-slate-plus}

Vea el video de configuración o siga los pasos indicados a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Si necesita más ayuda, consulte [Configuración inicial](../../faq/first_time_setup.md).

### 1. Encendido {#1-power-on}

Una el adaptador de corriente de dos piezas. Conéctelo al router y enchúfelo a una toma de corriente. El router se encenderá automáticamente.

### 2. Conectar un dispositivo {#2-connect-device}

Conecte un dispositivo, por ejemplo un ordenador, portátil o smartphone, al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

- Wi-Fi

    En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. Puede encontrar el nombre y la contraseña predeterminados impresos en la etiqueta inferior del router.

### 3. Iniciar sesión en el panel de administración web {#3-log-in-to-web-admin-panel}

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma y establezca la contraseña de administrador; a continuación, haga clic en **Apply**.

Al confirmar los datos de Wi‑Fi, tenga en cuenta que, si cambia la información de Wi‑Fi, deberá volver a conectar su dispositivo al Wi‑Fi del router utilizando las credenciales actualizadas.

### 4. Configuración de Internet {#4-internet-setup}

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router a través del panel de administración web de GL.iNet. Si prefiere usar la aplicación GL.iNet, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

Configure su Slate Plus con uno de los métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

    Conecte un cable Ethernet entre el puerto WAN del router y un dispositivo ascendente, como un módem.
    
    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de entre las redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.
    
    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB del router mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.
    
    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del router. Esto es útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Una vez conectado correctamente a Internet, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

---

## Wireless {#wireless}

La página Wireless permite configurar los ajustes de las redes Wi-Fi de 5 GHz y 2.4 GHz, incluidos la activación de Wi-Fi, la potencia de transmisión, el nombre de Wi-Fi (SSID), el modo de seguridad y la contraseña de Wi-Fi, la visibilidad del SSID, el modo Wi-Fi, el ancho de banda y el canal.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless_v4.8.md).

## Clients {#clients}

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y carga, el tráfico total, y permite bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## VPN {#vpn}

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad (cliente VPN) y le permite acceder a una red remota (servidor VPN). Slate Plus (y otros routers GL.iNet) es compatible con OpenVPN y WireGuard. Además, también admite Tor.

=== "OpenVPN"

    Slate Plus (y otros routers GL.iNet) es compatible con el protocolo OpenVPN, que ofrece una seguridad sólida. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate Plus (y otros routers GL.iNet) es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico de Internet a través de una serie de servidores (nodos) gestionados por voluntarios para ocultar la ubicación y el uso del usuario, dificultando el rastreo de la actividad en línea.
    
    * [Cómo configurar Tor](../../interface_guide/tor.md).

## Aplicaciones {#applications}

=== "Plug-ins"

    Un plugin es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo personalizarlo y ampliar sus capacidades.
    
    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Asigna un nombre de dominio a la dirección IP pública dinámica de su router, de modo que pueda acceder a su red de forma remota sin necesidad de una dirección IP estática.
    
    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    El servicio de gestión en la nube [GoodCloud](https://www.goodcloud.xyz){target="_blank"} de GL.iNet proporciona una forma sencilla de acceder y gestionar remotamente routers GL.iNet.
    
    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "Network Storage"

    El almacenamiento en red es una solución de almacenamiento centralizado que permite a múltiples usuarios y dispositivos acceder y compartir archivos a través de una red.
    
    Para configurar el almacenamiento en red, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores a nivel de red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a la red doméstica.
    
    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control está diseñado para ayudarle a administrar y controlar los dispositivos de sus hijos. Incluye limitar el tiempo de pantalla y restringir el acceso a determinados contenidos.

    Para configurar el control parental, consulte [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier es una solución de redes definidas por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.
    
    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.
    
    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

## Network {#network}

=== "Firewall"

    La página Firewall proporciona mejoras esenciales de seguridad para su red. Incluye funciones como Port Forwarding, Open Ports y DMZ. Estas herramientas le permiten gestionar y personalizar el flujo de tráfico de la red y reforzar su seguridad.

    * Port Forwarding: redirige tráfico específico desde Internet hacia dispositivos concretos de su red, permitiendo acceder a servicios como servidores de juegos o servidores web.
    * Open Ports: permite supervisar y controlar qué puertos del router están abiertos, lo que ayuda a evitar accesos no autorizados y posibles amenazas de seguridad.
    * DMZ (zona desmilitarizada): expone un dispositivo a Internet reenviándole todo el tráfico entrante.

    Para configurar opciones relacionadas con el firewall, consulte [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo Ethernet, Repeater y Tethering, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o red de área local, es una red que conecta ordenadores y dispositivos en un área geográfica limitada, como un hogar u oficina. Permite la transferencia de datos a alta velocidad y el uso compartido de recursos, posibilitando que los dispositivos se comuniquen eficientemente entre sí.
    
    Para configurar LAN, consulte [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Permite establecer una subred dentro de los rangos de direcciones privadas IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, especificar las direcciones IP de puerta de enlace y máscara de red, y configurar ajustes de seguridad como el aislamiento de AP para la red de invitados.

    Para configurar la red de invitados, consulte [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección contra ataques de reenlace DNS, anular la configuración DNS de todos los clientes y permitir que el DNS personalizado anule el DNS de la VPN. Puede utilizar servidores DNS obtenidos automáticamente de los dispositivos de la red superior o especificar manualmente servidores DNS personalizados.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    El modo de red hace referencia a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.
    
    Para configurar Network Mode, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Protocolo de Internet versión 6, es la versión más reciente del Protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones enormemente mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, esencial para dar cabida al creciente número de dispositivos conectados a Internet.
    
    Para configurar IPv6, consulte [IPV6](../../interface_guide/ipv6.md).

=== "MAC Address"

    La página MAC Address le permite ver y gestionar las direcciones Media Access Control (MAC) asociadas al router. Entre las funciones principales de esta página se incluyen:

    * Factory Default: muestra las direcciones MAC predeterminadas para los modos Ethernet y Repeater del router, como referencia de la configuración original del hardware.
    * Clone: clona la dirección MAC de un dispositivo cliente específico. Esto resulta especialmente útil en entornos donde el acceso a la red está restringido a determinados dispositivos.
    * Manual: permite especificar manualmente una dirección MAC personalizada para el router. Además, puede usar el botón Random para generar una dirección MAC aleatoria, lo que aporta flexibilidad y mayor privacidad.

    Estas funciones le permiten gestionar eficazmente las direcciones MAC del router, garantizando compatibilidad y flexibilidad en distintos entornos de red.

    Para gestionar MAC Address, consulte [MAC Address](../../interface_guide/mac_address.md).

---

=== "Drop-in Gateway"

    Drop-in gateway amplía la funcionalidad del router principal, incluyendo AdGuard Home, DNS cifrado y cliente VPN.
    
    Para configurar drop-in gateway, consulte estos enlaces:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Cómo configurar Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en conmutadores Ethernet para gestionar y controlar el tráfico multicast.
    
    Para configurar IGMP Snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    La página NAT Settings le permite activar o desactivar Full Cone NAT y la funcionalidad SIP ALG (Application Layer Gateway).

    Para configurar NAT Settings, consulte [NAT Settings](../../interface_guide/nat_settings.md).

## Sistema {#system}

=== "Overview"

    La página Overview ofrece una visión completa del estado actual del router y de sus métricas de rendimiento. En esta página puede ver:

    * CPU Average Load: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Memory Usage: Compruebe cuánta memoria del router está en uso, lo que facilita la gestión de recursos.
    * LED Control: Active o desactive las luces LED del router, lo que permite personalizar los indicadores visuales del dispositivo.
    * Flash Usage: Consulte el uso del almacenamiento flash del router, asegurándose de que haya espacio suficiente para firmware y datos de configuración.
    * Device Info: Acceda a información detallada sobre el sistema del router, incluidos el tiempo de actividad, el nombre de host, el modelo, la arquitectura, la versión de OpenWrt, la versión del kernel, el ID del dispositivo, la MAC del dispositivo y el número de serie.
    * External Storage: Compruebe el estado de los dispositivos de almacenamiento externo conectados al router, como unidades USB o tarjetas TF.
    
    Estas funciones proporcionan información y controles esenciales, ayudándole a gestionar y supervisar eficazmente el funcionamiento del router.

    Consulte [Overview](../../interface_guide/system_overview.md) para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejoras de rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: Comprueba automáticamente en el servidor del fabricante si existe una versión más reciente del firmware. Puede instalarla si está disponible en línea.
    * Firmware Local Upgrade: Carga manualmente un archivo de firmware desde su ordenador para actualizar el router, proporcionando control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las últimas mejoras y correcciones.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones clave de esta página se incluyen:

    * LED Display Schedule: Establezca una programación para encender o apagar automáticamente las luces LED del router, reduciendo la contaminación lumínica en determinadas horas.
    * Schedule Reboot: Configure el router para reiniciarse automáticamente a intervalos especificados, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi: establezca un horario para controlar la banda Wi-Fi de 5 GHz / 2,4 GHz, lo que permite gestionar mejor la disponibilidad de la red y el consumo de energía.
    
    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, garantizando que se adapte a sus necesidades y preferencias específicas.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Esta configuración es fundamental para mantener registros exactos y para la correcta ejecución de configuraciones basadas en tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

=== "Toggle Button Settings"

    La página Toggle Button Settings le permite configurar el interruptor físico del router, lo que le permite asignar funciones específicas al botón para un acceso y control rápidos. Esta función ofrece accesos directos prácticos para tareas y ajustes comunes, mejorando la experiencia del usuario y simplificando la gestión del router.

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

    **Nota**: Esta función está disponible a partir de la versión 4.5.

    La página Security le permite configurar varios ajustes de seguridad para proteger su red y router frente a accesos no autorizados. Esta página incluye opciones para:

    * Admin Password: Establezca o cambie la contraseña de la interfaz administrativa del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.
    * Local Access Control: Gestione y restrinja el acceso a la interfaz del router desde los dispositivos conectados a su red local.
    * Remote Access Control: Configure y restrinja el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, mejorando la seguridad frente a amenazas externas.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.
    
    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware actualmente instalada. Esto puede resultar útil para solucionar problemas persistentes o para comenzar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings proporciona acceso a opciones de configuración avanzadas a través de la interfaz OpenWrt LuCI, permitiendo a los usuarios experimentados ajustar con precisión la configuración y las funciones del router más allá de las opciones de la interfaz básica. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para ver instrucciones detalladas.
