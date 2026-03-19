# Guía de usuario de Marble (GL-B3000)

## Descripción general del producto

El router Marble (GL-B3000) es una pieza decorativa en sí misma, ingeniosamente presentada como un marco de fotos para exhibir su obra favorita y realzar su espacio. Además de ser visualmente atractivo, el router Marble (GL-B3000) ofrece un rendimiento de primer nivel gracias a Wi-Fi 6 y a su compatibilidad con funciones VPN.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Contenido del paquete

- 1 x Marble (GL-B3000)
- 1 x Manual del usuario
- 1 x Tarjeta de agradecimiento
- 1 x Cable Ethernet
- 1 x Kit de montaje en pared
- 1 x Almohadilla adhesiva
- 1 x Soporte para router
- 1 x Marco de fotos (opcional)
- 1 x Adaptador de corriente
- 1 x Convertidor (según el país de envío)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Cómo configurar Marble

Vea estos vídeos de instalación y configuración, o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Encender

Ensamble las dos piezas del adaptador de corriente. Conéctelo al router y enchúfelo a una toma de corriente. El router se iniciará automáticamente.

### 2. Conectar un dispositivo

Conecte un dispositivo, por ejemplo un ordenador, un portátil o un smartphone, al router mediante Wi-Fi o un cable Ethernet.

- Ethernet

    Conecte su dispositivo al puerto LAN del router mediante un cable ethernet.

- Wi-Fi

    En su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi del router en la lista de redes disponibles e introduzca la contraseña. (Puede encontrar el nombre de red y la contraseña predeterminados impresos en la etiqueta del router).

### 3. Iniciar sesión en el panel de administración web

Abra un navegador web, introduzca `192.168.8.1` en la barra de direcciones e inicie sesión. Elija su idioma, establezca la contraseña de administrador y haga clic en **Apply**.

### 4. Configuración de Internet

**Nota:** Las siguientes instrucciones se aplican a los usuarios que configuran el router desde el panel de administración web de GL.iNet. Si prefiere usar la aplicación de GL.iNet, [descargue la aplicación](https://www.gl-inet.com/app/){target="_blank"} y siga las instrucciones que aparecen en pantalla.

Configure su Marble con uno de los métodos de conexión a Internet compatibles: Ethernet y Repeater. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure dos conexiones a Internet.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}

    Conecte un cable ethernet entre el puerto WAN del router y un dispositivo aguas arriba, como un módem.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Ethernet de la página INTERNET.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. En la página INTERNET del panel de administración web, localice la sección Repeater y haga clic en **Connect**.
    2. Seleccione una red Wi-Fi de la lista de redes disponibles.
    3. Introduzca la contraseña de la red y haga clic en **Apply**.

    Cuando la conexión a Internet se establezca correctamente, aparecerá un punto verde en la sección Repeater de la página INTERNET.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

---

## Cómo configurar una VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad cuando se usa como cliente VPN y permite acceder a una red remota cuando se usa como servidor VPN. Marble, al igual que otros routers GL.iNet, es compatible con OpenVPN y WireGuard. Además, también es compatible con Tor.

=== "OpenVPN"

    Marble, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor es un servicio centrado en la privacidad que le permite acceder a Internet de forma anónima. Para configurar Tor, siga este tutorial:

    * [Cómo configurar Tor](../../interface_guide/tor.md)

---

## Red inalámbrica y clientes

=== "Wireless"

    La página Wireless le permite configurar ajustes para las redes Wi-Fi de 5 GHz y 2,4 GHz, incluyendo activar o desactivar el Wi-Fi, ajustar la potencia TX, definir el nombre de la red Wi-Fi (SSID), activar o desactivar el BSSID aleatorio, seleccionar el modo de seguridad Wi-Fi, configurar la contraseña Wi-Fi, ajustar la visibilidad del SSID y elegir el modo Wi-Fi, el ancho de banda y el canal.

    Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, se muestra el nombre del dispositivo, el tipo de conexión (es decir, mediante ethernet o Wi-Fi), las direcciones IP y MAC, las velocidades de descarga y subida, el tráfico total y la posibilidad de bloquear el cliente o realizar otras acciones.

    Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    El servicio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} proporciona una forma sencilla de acceder de forma remota a los routers GL.iNet y gestionarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    Esta función está disponible a partir del firmware v4.7.

    AstroWarp es una plataforma de red avanzada diseñada para ofrecer redes remotas y gestión remota de dispositivos sin interrupciones. Creada específicamente para integrarse con routers GL.iNet, AstroWarp admite una gestión integral de dispositivos en redes completas, lo que permite controlar tanto los dispositivos superiores como los inferiores. Con un enfoque centrado en la gestión de toda la red y compatibilidad futura con control a nivel de hardware, AstroWarp ofrece una solución más sólida y fiable para gestionar dispositivos y mantener redes seguras y estables.

## Aplicaciones

=== "Plug-ins"

    Los plug-ins son funciones adicionales que amplían la funcionalidad del router. Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta especialmente útil para los usuarios que necesitan una dirección IP estática para acceder a una red remota. Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

---

=== "AdGuard Home"

    AdGuard Home es una herramienta de terceros que bloquea anuncios y rastreadores para mantenerle protegido.

    Para saber cómo activar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental control es un conjunto de ajustes diseñado para ayudarle a gestionar y controlar los dispositivos de sus hijos. Incluye la limitación del tiempo de pantalla y la restricción del acceso a determinados contenidos. Marble ofrece dos opciones de control parental: la versión local desarrollada por GL.iNet y la versión integrada de Bark, una aplicación de control parental.

    Para configurar el control parental, consulte [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar. Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier es un servicio VPN que le permite conectar sus dispositivos a una red virtual. Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

---

## Configuración de red

=== "Firewall"

    La página Firewall proporciona mejoras esenciales de seguridad para su red. Incluye funciones como Port Forwarding, Open Ports y DMZ. Estas herramientas le permiten gestionar y personalizar el flujo de tráfico de la red y reforzar su seguridad.

    * Port Forwarding: redirige tráfico específico desde Internet hacia dispositivos concretos de su red, permitiendo acceder a servicios como servidores de juegos o servidores web.
    * Open Ports: permite supervisar y controlar qué puertos del router están abiertos, lo que ayuda a evitar accesos no autorizados y posibles amenazas de seguridad.
    * DMZ (zona desmilitarizada): coloca un dispositivo fuera del firewall principal, permitiéndole tener acceso sin restricciones a Internet mientras protege al resto de la red frente a amenazas potenciales.

    Para ver instrucciones detalladas de configuración y más información, consulte [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo cellular, repeater y ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La página LAN le permite gestionar y configurar los ajustes de la red de área local del router. Entre las funciones principales de esta página se incluyen:

    * Dirección IP del router: modifique la dirección IP del router para adaptarla mejor a su configuración de red.
    * Máscara de red: establezca la máscara de subred de la red, que determina el tamaño de la red y el rango de direcciones IP.
    * DHCP: active o configure el protocolo Dynamic Host Configuration Protocol, que asigna automáticamente direcciones IP a los dispositivos de la red.
    * Reserva de direcciones: reserve direcciones IP específicas para determinados dispositivos, de modo que siempre reciban la misma dirección IP desde el servidor DHCP.

    Para ver instrucciones detalladas de configuración y más información, consulte [LAN](../../interface_guide/lan.md).

---

=== "Guest Network"

    La página Guest Network le permite crear y gestionar una red independiente para sus invitados, proporcionándoles acceso a Internet mientras mantiene segura su red principal. Entre las funciones principales de esta página se incluyen:

    * Gateway: configure un rango de direcciones IP específico para la red de invitados a fin de diferenciarla de la red principal.
    * DHCP: configure el protocolo Dynamic Host Configuration Protocol para la red de invitados, asignando automáticamente direcciones IP a los dispositivos que se conecten a ella.

    Estas funciones garantizan que sus invitados puedan disfrutar de acceso a Internet sin comprometer la seguridad ni el rendimiento de la red principal.

    Para ver instrucciones detalladas de configuración y más información, consulte [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La página DNS ofrece opciones para personalizar los ajustes del sistema de nombres de dominio del router, mejorando tanto la seguridad como el rendimiento. Entre las funciones principales de esta página se incluyen:

    * DNS cifrado: configure DNS cifrado para proteger sus datos de navegación frente a la supervisión o manipulación, garantizando privacidad y seguridad.
    * DNS manual: configure manualmente los servidores DNS de su elección, lo que le permite tener un control personalizado sobre las consultas DNS y obtener tiempos de resolución potencialmente más rápidos.
    * Proxy DNS: active el proxy DNS para enrutar las solicitudes DNS de sus dispositivos a través de un servidor DNS especificado, lo que proporciona una capa adicional de control sobre el tráfico DNS.

    Estos ajustes le permiten optimizar el rendimiento y la seguridad del DNS de su red según sus necesidades específicas.

    Para ver instrucciones detalladas de configuración y más información, consulte [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    La página Network Mode le permite configurar el router para que funcione en distintos modos, ofreciendo flexibilidad para adaptarse a diversas necesidades de red. Los modos disponibles incluyen:

    * Router: funciona como un router estándar, gestionando el tráfico entre la red local e Internet y ofreciendo funciones como NAT, firewall y DHCP.
    * Access Point: funciona como un punto de acceso, ampliando la red cableada existente mediante conectividad inalámbrica sin enrutar el tráfico.
    * Extender: funciona como un extensor de alcance, reforzando la señal de la red inalámbrica existente para cubrir un área mayor y eliminar zonas muertas.
    * WDS (Wireless Distribution System): es similar a Extender; elija WDS si el router principal es compatible con el modo WDS.

    Para ver instrucciones detalladas de configuración y más información, consulte [Network Mode](../../interface_guide/network_mode.md).

---

=== "IPv6"

    La página IPv6 le permite configurar los ajustes de IPv6 para su red, ofreciendo compatibilidad con la versión más reciente del protocolo de Internet. En esta página, puede activar IPv6 y elegir entre cuatro modos diferentes según las necesidades de su red:

    * Native: obtiene una dirección IPv6 directamente de su ISP, lo que permite una conectividad IPv6 nativa sencilla y eficiente.
    * Passthrough: permite que el tráfico IPv6 atraviese el router hacia los dispositivos de la red, actuando como un puente sin que el router gestione el enrutamiento IPv6 por sí mismo.
    * NAT6: utiliza Network Address Translation para IPv6 (NAT6) para traducir entre direcciones IPv6 internas y externas, de forma similar a como funciona NAT en IPv4.
    * Static IPv6: configura manualmente una dirección IPv6 estática para el router, proporcionando una dirección fija para una conectividad constante y una gestión más sencilla de los servicios de red.

    Estos ajustes le ayudan a aprovechar las ventajas de IPv6, como un espacio de direcciones ampliado, funciones de seguridad mejoradas y mejor rendimiento.

    Para ver instrucciones detalladas de configuración y más información, consulte [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    La página MAC Address le permite ver y gestionar las direcciones Media Access Control (MAC) asociadas al router. Entre las funciones principales de esta página se incluyen:

    * Factory Default: muestra las direcciones MAC predeterminadas para los modos Ethernet y Repeater del router, como referencia de la configuración original del hardware.
    * Clone: clona la dirección MAC de un dispositivo cliente específico. Esto resulta especialmente útil en entornos donde el acceso a la red está restringido a determinados dispositivos.
    * Manual: permite especificar manualmente una dirección MAC personalizada para el router. Además, puede usar el botón Random para generar una dirección MAC aleatoria, lo que aporta flexibilidad y mayor privacidad.

    Estas funciones le permiten gestionar eficazmente las direcciones MAC del router, garantizando compatibilidad y flexibilidad en distintos entornos de red.

    Para ver instrucciones detalladas de configuración y más información, consulte [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway amplía la funcionalidad del router principal con funciones que quizá no tenga, como AdGuard Home, DNS cifrado y VPN. Para configurar Drop-in Gateway, consulte [Cómo configurar Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    La página IGMP Snooping le permite configurar ajustes que optimizan la gestión del tráfico multicast dentro de su red. IGMP Snooping escucha y extrae información de los paquetes del protocolo IGMP, estableciendo y manteniendo tablas de reenvío multicast de capa 2. Esto garantiza que los datos de los grupos multicast se reenvíen solo a los hosts que se han unido a dichos grupos, evitando que tráfico multicast no deseado llegue a otros hosts.

    Estos ajustes ayudan a optimizar el rendimiento y la eficiencia de la red, especialmente en entornos con mucho tráfico multicast, como el streaming de vídeo o los juegos en línea.

    Para ver instrucciones detalladas de configuración y más información, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    La página Network Acceleration le permite activar funciones que reducen la carga de la CPU y aceleran el reenvío de paquetes, mejorando el rendimiento general de la red. Sin embargo, activar la aceleración de red puede entrar en conflicto con determinadas funciones.

    Para ver instrucciones detalladas de configuración y más información, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La página NAT Settings le permite configurar opciones de Network Address Translation (NAT) para optimizar aplicaciones específicas y mejorar el rendimiento de la red. Entre los ajustes principales de esta página se incluyen:

    * Activar Full Cone NAT: Full Cone NAT puede utilizarse para reducir la latencia en juegos, ofreciendo una ruta más directa y menos restrictiva para el tráfico de red. Sin embargo, activarlo puede ser menos seguro, ya que permite con mayor facilidad que hosts externos inicien conexiones con dispositivos internos.
    * Activar SIP ALG: Session Initiation Protocol Application Layer Gateway (SIP ALG) puede ayudar a mitigar los problemas causados por múltiples NAT, que pueden afectar a los servicios VoIP. Sin embargo, en la mayoría de los casos, SIP ALG puede no resultar beneficioso y puede provocar problemas como audio unidireccional, teléfonos que no suenan durante una llamada, cortes de llamada y llamadas que van directamente al buzón de voz.

    Estos ajustes le permiten adaptar el comportamiento NAT del router para ajustarlo mejor a las necesidades de su red, equilibrando las mejoras de rendimiento con posibles consideraciones de seguridad y funcionalidad.

    Para ver instrucciones detalladas de configuración y más información, consulte [NAT Settings](../../interface_guide/nat_settings.md).

---

## Configuración del sistema

=== "Overview"

    La página Overview ofrece una vista general completa del estado actual del router y de sus métricas de rendimiento. En esta página puede ver:

    * Carga media de la CPU: supervise la carga media de la CPU del router para evaluar el rendimiento e identificar posibles cuellos de botella.
    * Uso de memoria: compruebe cuánta memoria del router está en uso para ayudar a gestionar los recursos.
    * Uso de almacenamiento flash: vea el uso del almacenamiento flash del router para asegurarse de que hay espacio suficiente para el firmware y los datos de configuración.
    * Información del sistema: acceda a información detallada sobre el sistema del router, como la versión del firmware, el tiempo de actividad y el estado de la red.
    * Control LED: active o desactive los LED del router para personalizar los indicadores visuales del dispositivo.

    Estas funciones proporcionan información y controles esenciales para ayudarle a gestionar y supervisar el funcionamiento del router de forma eficaz.

    Para ver instrucciones detalladas de configuración y más información, consulte [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Online Upgrade: comprueba automáticamente si hay una nueva versión de firmware y la instala directamente desde el servidor del fabricante, simplificando el proceso.
    * Local Upgrade: permite cargar manualmente un archivo de firmware desde el ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Para ver instrucciones detalladas de configuración y más información, consulte [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite automatizar varias funciones del router según una programación predefinida, mejorando la comodidad y la eficiencia. Entre las funciones principales de esta página se incluyen:

    * Programación de visualización LED: establezca un horario para encender o apagar automáticamente los LED del router y reducir la contaminación lumínica en determinadas horas.
    * Reinicio programado: configure el router para que se reinicie automáticamente en intervalos específicos, lo que ayuda a mantener un rendimiento y una estabilidad óptimos.
    * Programación del estado del Wi-Fi de 5 GHz: cree un horario para activar o desactivar la banda Wi-Fi de 5 GHz en momentos concretos, optimizando el uso de la red y la eficiencia energética.
    * Programación del estado del Wi-Fi de 2,4 GHz: establezca un horario para controlar la banda Wi-Fi de 2,4 GHz, permitiendo gestionar mejor la disponibilidad de la red y el consumo energético.

    Estas opciones de programación le proporcionan un mayor control sobre el funcionamiento del router, asegurando que se adapte a sus necesidades y preferencias.

    Para ver instrucciones detalladas de configuración y más información, consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    La página Time Zone le permite establecer la zona horaria correcta para el router, garantizando que todas las tareas programadas, los registros y los eventos del sistema tengan marcas de tiempo precisas según su hora local.

    Para ver instrucciones detalladas de configuración y más información, consulte [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    La página Log proporciona acceso a varios registros que documentan las actividades y eventos del router, lo que facilita la resolución de problemas y la supervisión del rendimiento. Esta página incluye:

    * System Log: registros detallados de eventos y actividades a nivel del sistema.
    * Kernel Log: registros relacionados con las operaciones y eventos del kernel.
    * Crash Log: registros de fallos y errores del sistema, útiles para diagnosticar problemas críticos.
    * Cloud Log: registros de interacciones y actividades relacionadas con los servicios GoodCloud integrados en el router.
    * Nginx Log: registros del servidor web Nginx, si se utiliza en el router, que detallan el tráfico web y las operaciones del servidor.

    Además, la página incluye un botón Export Log, que le permite exportar todos los registros recopilados para su análisis por parte del soporte técnico. Esta función es muy valiosa para diagnosticar problemas complejos y obtener asistencia profesional.

    Para ver instrucciones detalladas de configuración y más información, consulte [Log](../../interface_guide/log.md).

=== "Security"

    La página Security le permite configurar varios ajustes de seguridad para proteger la red y el router frente a accesos no autorizados. Esta página incluye opciones para:

    * Admin Password: establecer o cambiar la contraseña de la interfaz de administración del router para garantizar que solo los usuarios autorizados puedan modificar la configuración.
    * Local Access Control: gestionar y restringir el acceso a la interfaz del router desde dispositivos conectados a la red local.
    * Remote Access Control: configurar y restringir el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Para ver instrucciones detalladas de configuración y más información, consulte [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    La página Reset Firmware le permite restablecer la versión actual del firmware del router a su configuración predeterminada, borrando todas las configuraciones personalizadas. Este proceso restaurará el router a la configuración predeterminada de la versión de firmware instalada en ese momento. Puede resultar útil para solucionar problemas persistentes o para comenzar de nuevo con la configuración predeterminada del firmware actual.

    Para ver instrucciones detalladas de configuración y más información, consulte [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La página Advanced Settings ofrece acceso a opciones de configuración avanzada a través de la interfaz OpenWrt LuCI, lo que permite a los usuarios con experiencia ajustar con precisión la configuración y las funciones del router más allá de las opciones básicas de la interfaz. Esto incluye configuraciones detalladas de red, ajustes del firewall y otras personalizaciones avanzadas del sistema.

    Para ver instrucciones detalladas de configuración y más información, consulte [Advanced Settings](../../interface_guide/advanced_settings.md).

