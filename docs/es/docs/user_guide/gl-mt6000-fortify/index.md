# Guía de usuario de Fortify (GL-MT6000)

## Descripción del producto

Fortify (GL-MT6000) es un router Wi-Fi 6 de marca conjunta lanzado por GL.iNet y ExpressVPN. Cada unidad incluye una suscripción gratuita de un año a ExpressVPN. Los usuarios pueden canjear la suscripción y vincular sus cuentas directamente desde el panel de administración web del router. Una vez activado, todo el tráfico que pase por el router usará la red de alta velocidad y el cifrado robusto de ExpressVPN para proteger toda la conexión de red y la privacidad en línea.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Cómo configurar Fortify

### 1. Encender

Monte el adaptador de corriente de dos piezas. Conéctelo al router Fortify y enchúfelo a una toma de corriente. El router se iniciará automáticamente.

### 2. Conectar un dispositivo

Conecte un dispositivo, por ejemplo un ordenador, portátil o smartphone, al router mediante Wi-Fi o Ethernet.

- Ethernet

    Conecte el dispositivo al puerto LAN del router con un cable Ethernet.

- Wi-Fi

    En el dispositivo, vaya a Settings -> WLAN, busque el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. El nombre y la contraseña predeterminados están impresos en la etiqueta del router.

### 3. Iniciar sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija el idioma en la esquina superior derecha, configure la contraseña de administrador y haga clic en **Next**. La contraseña debe tener entre 10 y 63 caracteres e incluir al menos dos de estos tipos: letras mayúsculas, letras minúsculas, números y símbolos especiales.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Configure el Wi-Fi. Si cambia la información del Wi-Fi, deberá volver a conectar el dispositivo a la red Wi-Fi del router con las nuevas credenciales.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Configurar Internet

**Note:** Las siguientes instrucciones son para usuarios que configuran el router mediante el panel de administración web de GL.iNet. Si prefiere la [app GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, descárguela y siga las indicaciones en pantalla.

Configure Fortify con uno de los métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Si desea usar [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Conecte un cable Ethernet entre el puerto WAN del router Fortify y un dispositivo ascendente, como un módem.

    Cuando la conexión a Internet se establezca correctamente, el LED del router quedará en blanco fijo.

    Consulte [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) para obtener instrucciones detalladas.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. En el panel de administración web, vaya a la sección INTERNET -> Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de la lista de redes disponibles.
    3. Introduzca la contraseña y haga clic en **Apply**.

    Cuando la conexión a Internet se establezca correctamente, el LED del router quedará en blanco fijo.

    Consulte [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) para obtener instrucciones detalladas.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Conecte el smartphone al puerto USB del router con un cable USB.
    2. En el smartphone, vaya a Settings y active USB Tethering. En iPhone, confíe en este dispositivo y active Personal Hotspot.
    3. En el panel de administración web, vaya a la sección INTERNET -> Tethering y haga clic en **Connect**.

    Cuando la conexión a Internet se establezca correctamente, el LED del router quedará en blanco fijo.

    Consulte [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) para obtener instrucciones detalladas.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Conecte un módem USB celular al puerto USB del router para compartir Internet del módem USB con todos los dispositivos conectados.

    Cuando la conexión a Internet se establezca correctamente, el LED del router quedará en blanco fijo.

    Consulte [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) para obtener instrucciones detalladas.

---

A continuación se muestra una descripción general de las funciones del panel de administración web de Fortify.

## Wireless

La página Wireless permite configurar las redes Wi-Fi de Fortify, incluidas Main Network, Guest Network e IoT Network. Cada red admite las bandas de 2,4 GHz y 5 GHz.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless_v4.9.md).

## Clients

La página Clients muestra información sobre los dispositivos conectados, como nombre, tipo de conexión, direcciones IP y MAC, velocidades de descarga y subida, tráfico, y permite bloquear clientes específicos con un clic o realizar otras acciones.

Consulte [Clients](../../interface_guide/clients.md) para más detalles.

## Servicios en la nube

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} ofrece una forma sencilla de acceder y administrar routers GL.iNet de forma remota.

    Consulte [GoodCloud](../../interface_guide/cloud.md) para más detalles.

=== "AstroWarp"

    AstroWarp está diseñado para redes remotas fluidas en routers GL.iNet. Usa el protocolo AmneziaWG con ofuscación de tráfico integrada para ofrecer acceso remoto estable y seguro.

    Consulte [AstroWarp](../../interface_guide/astrowarp.md) para más detalles.

## VPN

Una VPN (red privada virtual) establece túneles de tráfico seguros y cifrados entre el dispositivo local y el servidor VPN. Añade privacidad y seguridad al cliente VPN y permite acceder a la red remota del servidor VPN.

Fortify se integra con [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, lo que permite activar una conexión ExpressVPN en minutos. Cada dispositivo Fortify incluye una suscripción gratuita de un año a ExpressVPN, que puede canjear y vincular desde el panel de administración web.

Para canjear la suscripción gratuita y configurar un túnel VPN, consulte [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md).

Para configurar un servidor OpenVPN, consulte [OpenVPN Server](../../interface_guide/openvpn_server.md).

Para configurar un servidor WireGuard, consulte [WireGuard Server](../../interface_guide/wireguard_server.md).

## Red

=== "Multi-WAN"

    Multi-WAN permite usar varias conexiones a Internet al mismo tiempo, por ejemplo cellular, repeater y ethernet. Si la conexión actual falla, el router cambiará automáticamente a otra conexión.

    Consulte [Multi-WAN](../../interface_guide/multi-wan.md) para más detalles.

=== "LAN"

    LAN es la red local a la que se une el dispositivo cuando se conecta al Wi-Fi principal o mediante un cable Ethernet. La página LAN cubre Basic Settings, DHCP Server Settings y Address Reservation.

    Consulte [LAN](../../interface_guide/lan.md) para más detalles.

=== "Guest Network"

    Guest Network crea una red Wi-Fi dedicada para visitantes. Está aislada de la red principal y permite configurar una subred de invitados dentro de rangos IPv4 privados como `192.168.0.0/16`, `172.16.0.0/12` o `10.0.0.0/8`.

    Consulte [Guest Network](../../interface_guide/guest_network.md) para más detalles.

=== "IoT Network"

    IoT Network permite crear una red Wi-Fi dedicada para dispositivos IoT, aislada de la red principal para mejorar compatibilidad y seguridad.

    Consulte [IoT Network](../../interface_guide/iot_network.md) para más detalles.

<br>

=== "DNS"

    DNS controla cómo se traducen los nombres de dominio en direcciones IP. Puede usar servidores DNS obtenidos automáticamente, establecer servidores personalizados y configurar prioridades DNS.

    Consulte [DNS](../../interface_guide/dns.md) para más detalles.

=== "Ethernet Port"

    Ethernet Port permite administrar las funciones de los puertos WAN/LAN y ver detalles como dirección MAC y velocidad negociada.

    Consulte [Ethernet Port](../../interface_guide/ethernet_port.md) para más detalles.

=== "IPv6"

    IPv6 es la versión más reciente del protocolo de Internet y proporciona un espacio de direcciones mucho mayor que IPv4.

    Consulte [IPV6](../../interface_guide/network_mode.md) para más detalles.

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red usada en switches Ethernet para administrar y controlar tráfico multicast.

    Consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md) para más detalles.

<br>

=== "Network Mode"

    Network Mode define cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurarlo, consulte [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía las funciones del router principal con AdGuard Home, DNS cifrado y VPN.

    Para configurarlo, consulte [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    Network Acceleration puede reducir la carga de CPU y acelerar el reenvío de paquetes.

    Para configurarlo, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) analiza el contenido de los paquetes para identificar aplicaciones y sitios web con mayor precisión mediante una biblioteca de firmas. La función DPI de GL.iNet se integra con [Netify](https://www.netify.ai/){target="_blank"}.

    Consulte [DPI Engine](../../interface_guide/dpi_engine.md) para más detalles.

=== "Data Statistics"

    Data Statistics categoriza y visualiza el uso de red por aplicaciones para ayudarle a supervisar tráfico en tiempo real e histórico.

    Consulte [Data Statistics](../../interface_guide/data_statistics.md) para más detalles.

=== "Content Filter"

    Content Filter usa clasificación basada en DPI para bloquear automáticamente sitios web dañinos o maliciosos.

    Consulte [Content Filter](../../interface_guide/content_filter.md) para más detalles.

<br>

=== "QoS"

    QoS prioriza actividades críticas, como videollamadas o juegos, durante la congestión de red. Se aplica al tráfico local de clientes y a túneles de VPN Client, pero no al tráfico recibido cuando el router funciona como VPN Server.

    Consulte [QoS](../../interface_guide/qos.md) para más detalles.

=== "SQM"

    SQM (Smart Queue Management) administra el tráfico para reducir la latencia y el bufferbloat.

    Consulte [SQM](../../interface_guide/sqm.md) para más detalles.

=== "Parental Control"

    Parental Control ayuda a administrar los dispositivos de sus hijos, limitar el tiempo de pantalla y restringir el acceso a ciertos contenidos.

    Consulte [Parental Control](../../interface_guide/parental_control_v4.9.md) para más detalles.

## Seguridad

=== "Port forwarding"

    Port forwarding permite que servidores y dispositivos remotos de Internet accedan a dispositivos de una red privada.

    Consulte [Port Forwarding](../../interface_guide/port_forwarding.md) para más detalles.

=== "ACL"

    ACL (Access Control List) permite crear reglas para administrar el tráfico de red según protocolos, direcciones de dispositivos y puertos. Si varias reglas entran en conflicto, el sistema aplica la de mayor prioridad.

    Consulte [ACL](../../interface_guide/acl.md) para más detalles.

=== "Admin Access"

    Admin Access incluye ajustes de seguridad para proteger la red y el router contra accesos no autorizados, como Access Control, Remote Access Control y Open Ports on Router.

    Consulte [Admin Access](../../interface_guide/admin_access.md) para más detalles.

=== "NAT Mode"

    NAT Mode permite activar o desactivar Full Cone NAT y SIP ALG.

    Consulte [NAT Mode](../../interface_guide/nat_settings.md) para más detalles.

## Aplicaciones

=== "Plug-ins"

    Un plug-in añade funciones específicas a un programa o sistema existente.

    Consulte [Plug-ins](../../interface_guide/plugins.md) para más detalles.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio.

    Consulte [Dynamic DNS](../../interface_guide/ddns.md) para más detalles.

=== "Network Storage"

    Network Storage proporciona almacenamiento centralizado para que varios usuarios y dispositivos accedan y compartan archivos en la red.

    Consulte [Network Storage](../../interface_guide/network_storage.md) para más detalles.

=== "AdGuard Home"

    AdGuard Home bloquea anuncios y rastreadores en toda la red actuando como servidor DNS para filtrar contenido no deseado.

    Consulte [AdGuard Home](../../interface_guide/adguardhome.md) para más detalles.

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} puede ayudar a proteger el mundo digital de sus hijos. Como parte de la colaboración entre GL.iNet y Bark, Fortify (GL-MT6000) ofrece el plan Bark Home gratis.

    Consulte [Bark](../../interface_guide/bark.md) para más detalles.

=== "Tailscale"

    Tailscale permite acceder de forma segura a sus dispositivos y aplicaciones desde cualquier lugar. Fortify (GL-MT6000) puede unirse a una red virtual de Tailscale para acceso remoto a recursos WAN y LAN.

    Consulte [Tailscale](../../interface_guide/tailscale.md) para más detalles.

=== "ZeroTier"

    ZeroTier crea redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Consulte [ZeroTier](../../interface_guide/zerotier.md) para más detalles.

=== "Tor"

    Tor es software libre y de código abierto para comunicación anónima y navegación con mayor privacidad.

    Consulte [Tor](../../interface_guide/tor.md) para más detalles.

## Sistema

=== "Overview"

    Overview muestra el estado actual y métricas del router, como CPU Average Load, Memory Usage, LED Control, Flash Usage, Device Info y External Storage.

    Consulte [Overview](../../interface_guide/system_overview.md) para más detalles.

=== "Admin Password"

    Admin Password permite establecer o cambiar la contraseña de la interfaz administrativa del router.

    Consulte [Admin Password](../../interface_guide/admin_password.md) para más detalles.

=== "Upgrade"

    Upgrade se usa para actualizar el firmware del router. Incluye Firmware Online Upgrade y Firmware Local Upgrade.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para más detalles.

=== "Scheduled Tasks"

    Scheduled Tasks automatiza funciones del router según una programación, como LED Display Schedule, Schedule Reboot y 5GHz / 2.4GHz Wi-Fi Status Schedule.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para más detalles.

<br>

=== "Time Zone"

    Time Zone establece la zona horaria correcta para tareas programadas, registros y eventos del sistema.

    Consulte [Time Zone](../../interface_guide/time_zone.md) para más detalles.

=== "Reset Firmware"

    Reset Firmware restaura el firmware actual a sus ajustes predeterminados y borra las configuraciones personalizadas.

    Consulte [Reset Firmware](../../interface_guide/reset_firmware.md) para más detalles.

=== "Log"

    Log permite acceder a System Log, Kernel Log, Crash Log, Cloud Log y Nginx Log. El botón Export Log exporta los registros recopilados para análisis de soporte técnico.

    Consulte [Log](../../interface_guide/log.md) para más detalles.

=== "Advanced Settings"

    Advanced Settings abre la interfaz OpenWrt LuCI para configuración avanzada.

    Consulte [Advanced Settings](../../interface_guide/advanced_settings.md) para más detalles.
