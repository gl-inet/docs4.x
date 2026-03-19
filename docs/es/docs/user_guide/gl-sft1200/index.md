# Opal (GL-SFT1200) Guía del usuario

## Descripción general del producto

Opal (GL-SFT1200) es un router de viaje de bolsillo que admite una velocidad de transferencia inalámbrica de 1200 Mbps. Su diseño compacto está pensado para uso portátil y puede satisfacer las necesidades de acceso inalámbrico a Internet de pequeñas empresas, pequeños apartamentos o viajeros de negocios.

![gl-sft1200 interface](https://static.gl-inet.com/docs/router/en/3/setup/gl-sft1200/first_time_setup/gl-sft1200.jpg){class="glboxshadow"}

## Contenido del paquete

- 1 x Opal (GL-SFT1200)
- 1 x Manual del usuario
- 1 x Cable Ethernet
- 1 x Tarjeta de agradecimiento
- 1 x Tarjeta de garantía
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

![gl-sft1200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/first_time_setup/sft1200_unboxing.jpg){class="glboxshadow"}

## Cómo configurar Opal

Vea este video de configuración o siga los pasos a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Este video utiliza un router GL.iNet diferente para mostrar la configuración, pero los pasos son los mismos para Opal y otros modelos de router.)</small>

### 1. Encendido

Monte las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. Se iniciará automáticamente.

### 2. Conecte un dispositivo

Conecte un dispositivo (por ejemplo, un ordenador, un portátil o un smartphone) al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del router mediante un cable Ethernet.

- Wi-Fi

    En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. Puede encontrar el nombre de red y la contraseña predeterminados impresos en la etiqueta inferior del router.

### 3. Inicie sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma y establezca la contraseña de administrador; después, haga clic en **Apply**.

Tenga en cuenta que, si cambia la información de Wi‑Fi, deberá volver a conectar su dispositivo al Wi‑Fi del router usando las credenciales actualizadas.

### 4. Configuración de Internet

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router mediante el panel de administración web de GL.iNet. Si prefiere usar la aplicación GL.iNet, [descargue la app](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones en pantalla.

Configure su Opal usando uno de los métodos de conexión a Internet admitidos: Ethernet, Repeater, Tethering y Cellular. Si desea usar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_ethernet.png){class="glboxshadow"}

    Conecte un cable Ethernet entre el puerto WAN del router y un dispositivo ascendente, como un módem.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_repeater.png){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi entre las redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_tethering.png){class="glboxshadow"}

    1. Conecte su dispositivo móvil (por ejemplo, un smartphone o un dongle USB) al puerto USB del router mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active USB Tethering.
    3. En la página INTERNET del panel de administración web, haga clic en **Connect** en la sección Tethering.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Tethering de la página INTERNET.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del router. Esto resulta útil para compartir Internet desde un módem USB con todos los dispositivos conectados.

    Cuando se conecte correctamente a Internet, aparecerá un punto verde en la sección Cellular de la página INTERNET.

    Consulte [Conectarse a Internet mediante cellular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

## Cómo configurar una VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad (cliente VPN) y le permite acceder a una red remota (servidor VPN). Opal es compatible con OpenVPN, WireGuard y Tor*.

=== "OpenVPN"

    Opal (y otros routers GL.iNet) es compatible con el protocolo OpenVPN, que ofrece una seguridad sólida. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Opal (y otros routers GL.iNet) es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima por Internet. Encamina el tráfico de Internet a través de una serie de servidores operados por voluntarios (nodos) para ocultar la ubicación y el uso del usuario, lo que dificulta rastrear sus actividades en línea.

    **Nota:** Opal no es compatible con Tor de forma nativa, pero los usuarios pueden instalar Tor manualmente mediante un complemento. Haga clic [aquí](../../interface_guide/tor.md#manual-install) para ver más detalles.

## Wireless y Clients

=== "Wireless"

    La página Wireless le permite configurar ajustes para las redes Wi-Fi de 5 GHz y 2,4 GHz, lo que incluye activar el Wi-Fi, ajustar la potencia TX, especificar el nombre de la red Wi-Fi (SSID), activar el BSSID aleatorio, seleccionar el modo de seguridad Wi-Fi y la contraseña, configurar la visibilidad del SSID, y elegir el modo Wi-Fi, el ancho de banda y el canal.

    Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y carga, el tráfico total, y ofrece la posibilidad de bloquear el cliente o realizar otras acciones.

    Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    El servicio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} ofrece una forma sencilla de acceder de forma remota a los routers GL.iNet y administrarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una plataforma de red avanzada diseñada para proporcionar redes remotas sin interrupciones y gestión remota de dispositivos. Diseñada específicamente para integrarse con los routers GL.iNet, AstroWarp admite una gestión integral de dispositivos en redes completas, lo que permite controlar tanto dispositivos superiores como inferiores. Gracias a su enfoque en la gestión de toda la red y al futuro soporte para control a nivel de hardware, AstroWarp ofrece una solución más sólida y fiable para administrar dispositivos y mantener redes seguras y estables.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

    **Nota:** Actualice el firmware del router a la versión 1.7 o superior antes de utilizar esta función.

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

    **Nota:** Actualice el firmware del router a la versión 1.7 o superior antes de utilizar esta función.

## Configuración de red

=== "Port Forwarding"

    El reenvío de puertos permite que servidores y dispositivos remotos en Internet accedan a dispositivos dentro de una red privada.

    Para configurar el reenvío de puertos, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet (por ejemplo, cellular, repeater y ethernet) al mismo tiempo. Si la conexión a Internet actual falla, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o red de área local, es una red que conecta ordenadores y dispositivos dentro de un área geográfica limitada, como una casa u oficina. Permite transferencias de datos a alta velocidad y el uso compartido de recursos, lo que facilita que los dispositivos se comuniquen entre sí de forma eficiente.

    Para configurar LAN, consulte [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Le permite establecer una subred dentro de los rangos de direcciones privadas IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, especificar las direcciones IP de gateway y máscara de red, y configurar ajustes de seguridad como el aislamiento de AP para la red de invitados.

    Para configurar la red de invitados, consulte [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección contra ataques de DNS rebinding y sobrescribir la configuración DNS de todos los clientes, permitir que el DNS personalizado anule el DNS de la VPN, y configurar el modo de ajustes del servidor DNS para que sea automático o para especificar manualmente los servidores DNS de la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "Port Management"

    La página Port Management está disponible a partir del firmware v4.7.

    Esta página le permite configurar los puertos WAN y LAN, establecer la interfaz WAN/LAN en Ethernet, especificar el modo MAC y la dirección MAC para la interfaz WAN, y mostrar la velocidad negociada del puerto de red.

    Para administrar los puertos Ethernet, consulte [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    El modo de red hace referencia a los ajustes de configuración que determinan cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurar el modo de red, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Protocolo de Internet versión 6, es la versión más reciente del Protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones mucho mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad de su router principal, incluidas AdGuard Home, DNS cifrado y cliente VPN.

    Para configurar drop-in gateway, consulte [Cómo configurar drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para configurar IGMP snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    La aceleración de red puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.

    Para configurar la aceleración de red, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La página NAT Settings le permite activar o desactivar las funciones Full Cone NAT y SIP ALG (Application Layer Gateway).

    Para configurar los ajustes NAT, consulte [NAT Settings](../../interface_guide/nat_settings.md).

## Configuración del sistema

=== "Overview"

    La página Overview ofrece una visión general completa del estado actual y de las métricas de rendimiento de su router. En esta página puede ver:

    * Carga media de CPU: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Uso de memoria: compruebe cuánta memoria del router está en uso para facilitar la gestión de recursos.
    * Control LED: active o desactive las luces LED del router para personalizar los indicadores visuales del dispositivo.
    * Uso de flash: vea el uso del almacenamiento flash del router para asegurarse de que haya suficiente espacio para el firmware y los datos de configuración.
    * Información del dispositivo: acceda a información detallada del sistema del router, incluidos el tiempo de actividad, el nombre de host, el modelo, la arquitectura, la versión de OpenWrt, la versión del kernel, el ID del dispositivo, la MAC del dispositivo y el número de serie.
    * Almacenamiento externo: consulte el estado de los dispositivos de almacenamiento externo conectados al router, como unidades USB o tarjetas TF.

    Estas funciones le proporcionan información esencial y controles útiles para administrar y supervisar eficazmente el funcionamiento del router.

    Consulte [Overview](../../interface_guide/system_overview.md) para ver instrucciones detalladas.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, lo que garantiza mejor rendimiento, mayor seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: compruebe e instale automáticamente la versión más reciente del firmware directamente desde el servidor del fabricante, lo que simplifica el proceso de actualización.
    * Firmware Local Upgrade: cargue manualmente un archivo de firmware desde su ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar diversas funciones del router según un horario predefinido, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de la pantalla LED: establezca un horario para encender o apagar automáticamente las luces LED del router y reducir la contaminación lumínica en determinados momentos.
    * Reinicio programado: configure el router para que se reinicie automáticamente a intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi: establezca un horario para controlar la banda Wi-Fi de 5 GHz / 2,4 GHz, lo que permite gestionar mejor la disponibilidad de la red y el consumo de energía.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router y garantizan que se adapte a sus necesidades y preferencias específicas.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local. Este ajuste es fundamental para mantener registros exactos y para el correcto funcionamiento de las configuraciones basadas en el tiempo.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para ver instrucciones detalladas.

=== "Toggle Button Settings"

    La página Toggle Button Settings le permite configurar el interruptor físico del router, lo que le permite asignar funciones específicas al botón para un acceso y control rápidos. Esta función ofrece accesos directos prácticos para tareas y ajustes comunes, mejorando la experiencia del usuario y simplificando la gestión del router.

    Consulte [Toggle Button Settings](../../interface_guide/toggle_button_settings.md) para ver instrucciones detalladas.

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que ayuda a la resolución de problemas y a la supervisión del rendimiento. Esta página incluye:

    * Registro del sistema: registros detallados de eventos y actividades a nivel del sistema.
    * Registro del kernel: registros relacionados con las operaciones y eventos del kernel.
    * Registro de fallos: registros de bloqueos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Registro de la nube: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Registro de Nginx: registros del servidor web Nginx, si el router lo utiliza, con detalles sobre el tráfico web y las operaciones del servidor.

    Además, la página incluye un botón Export Log que le permite exportar todos los registros recopilados para su análisis por parte del soporte técnico. Esta función es muy útil para diagnosticar problemas complejos y obtener ayuda profesional.

    Consulte [Log](../../interface_guide/log.md) para ver instrucciones detalladas.

---

=== "Security"

    La página Security le permite configurar varios ajustes de seguridad para proteger su red y su router frente a accesos no autorizados. Esta página incluye opciones para:

    * Admin Password: establecer o cambiar la contraseña de la interfaz administrativa del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.
    * Local Access Control: administrar y restringir el acceso a la interfaz del router desde dispositivos conectados a su red local.
    * Remote Access Control: configurar y restringir el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controlar qué puertos están abiertos en el router para limitar posibles vulnerabilidades y accesos no autorizados.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a sus ajustes predeterminados, eliminando todas las configuraciones personalizadas. Este proceso restaurará el router a los ajustes predeterminados de la versión de firmware instalada actualmente. Puede resultar útil para solucionar problemas persistentes o para empezar de nuevo con la configuración predeterminada del firmware actual.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para ver instrucciones detalladas.

=== "Advanced Settings"

    La página Advanced Settings ofrece acceso a opciones de configuración avanzada a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios con experiencia ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para ver instrucciones detalladas.
