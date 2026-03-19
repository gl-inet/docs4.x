# Guía de usuario de Mudi 7 (GL-E5800)

## Descripción general del producto

Mudi 7 es un router de viaje portátil 5G NR Wi-Fi 7 diseñado para usuarios en movimiento y viajeros de negocios, ofreciendo redes privadas y fiables para proteger los datos frente a amenazas cibernéticas. Incorpora 5G de alta velocidad, conmutación automática entre doble SIM (failover) y Wi-Fi 7 (canales de 320 MHz y 4K QAM) para una conectividad rápida y estable, ideal para descargas veloces, streaming 4K y videoconferencias sin cortes incluso en zonas concurridas.

Equipado con pantalla táctil, Mudi 7 le permite supervisar en tiempo real el uso de datos, la intensidad de la señal, los dispositivos conectados y la velocidad de los clientes, además de ajustar la configuración con simples toques para un control intuitivo y sin complicaciones.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Contenido del paquete

- 1 x Mudi 7 (GL-E5800)
- 1 x Pack de batería
- 1 x Cable USB-C de 10 Gbps
- 1 x Funda de viaje
- 1 x Manual del usuario

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Vea a continuación el vídeo de unboxing de Mudi 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cómo configurar Mudi 7

Vea este vídeo de configuración o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Instalar la tarjeta SIM

Instale una o dos tarjetas Nano-SIM en su Mudi 7. Si prefiere usar eSIM, omita este paso y vaya al paso 2.

Primero, retire la tapa de la batería y saque la batería de Mudi 7.

Después, inserte la(s) tarjeta(s) Nano-SIM. Si usa solo una tarjeta, dé prioridad a SIM 1.

Por último, vuelva a colocar la batería y la tapa.

![install nano-sim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/install_nano-sim.png){class="glboxshadow"}

### 2. Encender

Mantenga pulsado el botón de encendido durante **3 segundos** o conecte un adaptador de corriente.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power_on.png){class="glboxshadow"}

### 3. Ajustes básicos

Siga las instrucciones que aparecen en pantalla para configurar los ajustes básicos, incluidos **screen passcode**, **admin password**, **Wi-Fi name**, **Wi-Fi password** y **frequency bands**.

**Consejo**: la contraseña de administrador predeterminada son los últimos 9 caracteres del S/N del dispositivo, seguidos del carácter `#`. Puede usar la contraseña predeterminada o establecer una personalizada.

### 4. Configuración de Internet

Configure su Mudi 7 con uno de los métodos de conexión a Internet compatibles: Cellular, Ethernet, Repeater, Tethering y USB Ethernet. Si desea utilizar la función [Multi-WAN](../../interface_guide/multi-wan.md), configure más de una conexión a Internet.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}

    Mudi 7 incorpora una **eSIM integrada** y **doble ranura Nano-SIM**. Puede conectarse a Internet comprando un paquete eSIM (sin necesidad de tarjeta SIM física) o insertando sus tarjetas Nano-SIM para acceder a la red móvil 5G.

    - eSIM: en la pantalla táctil, vaya a **Cellular** -> **Active SIM Card**, active eSIM y después cargue su perfil eSIM a través del panel de administración web, o cómprelo en eSIM Profile Store.

    - Nano-SIM: retire la tapa trasera de Mudi 7, saque la batería, inserte la tarjeta Nano-SIM en la ranura y vuelva a instalar la batería.

    Cuando la conexión a Internet se establezca correctamente, las barras de señal y el estado de la conexión celular aparecerán en la esquina superior derecha de la pantalla táctil. También puede comprobar los detalles de la conexión en el panel de administración web.

    Consulte [Conectarse a Internet mediante conexión celular](../../interface_guide/internet_cellular.md) para ver instrucciones detalladas.

    !!! note

        1. La eSIM integrada y SIM 2 son mutuamente excluyentes y no pueden activarse al mismo tiempo. La eSIM está desactivada por defecto. Si activa la eSIM, SIM 2 no funcionará aunque haya una tarjeta SIM insertada.
        2. Como Mudi 7 incorpora una eSIM integrada, una tarjeta física eSIM SIMPoYo se reconocerá como una tarjeta SIM normal sin funcionalidad eSIM en Mudi 7.

=== "Ethernet"

    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Conecte el puerto Ethernet de Mudi 7 a una fuente de red aguas arriba (por ejemplo, un módem del ISP, un switch de red o una toma Ethernet de pared) mediante un cable Ethernet.
    2. En la pantalla táctil o en el panel de administración web, vaya a **Network** -> **Ethernet Ports**, establezca la función del puerto en **WAN** y haga clic en **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Cuando la conexión a Internet se establezca correctamente, aparecerá un icono de puerto Ethernet en la esquina superior derecha de la pantalla táctil. También puede comprobar los detalles de la conexión en el panel de administración web.

    Consulte [Conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md) para ver instrucciones detalladas.

=== "Repeater"

    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. En la pantalla táctil o en el panel de administración web, vaya a **Internet** -> **Repeater** y haga clic en **Connect**. Mudi 7 empezará a buscar redes Wi-Fi disponibles.
    2. Seleccione la red Wi-Fi que desea ampliar con Mudi 7.
    3. Introduzca la contraseña y haga clic en **Apply**.
    4. Cuando la conexión a Internet se establezca correctamente, aparecerá un icono Wi-Fi en la esquina superior derecha de la pantalla táctil. También puede comprobar los detalles de la conexión en el panel de administración web.

    Consulte [Conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md) para ver instrucciones detalladas.

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Conecte su dispositivo móvil, por ejemplo un smartphone o un dongle USB, al puerto USB-C de Mudi 7 mediante un cable USB.
    2. En su dispositivo móvil, vaya a Settings y active **USB Tethering**. Si usa iPhone, pulse **Trust This Device** si se lo solicita.
    3. Mudi 7 se conectará automáticamente a su dispositivo. Si no se conecta, repita los pasos anteriores o inicie sesión en el panel de administración web y compruebe la conexión Tethering en la página INTERNET.
    4. Cuando la conexión a Internet se establezca correctamente, aparecerá un icono de cadena en la esquina superior derecha de la pantalla táctil. También puede comprobar los detalles de la conexión en el panel de administración web.

    Consulte [Conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md) para ver instrucciones detalladas.

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 está equipado con un puerto USB-C **compatible con OTG**, que le permite añadir un segundo puerto Ethernet para Dual-Ethernet WAN. Para ello se necesita un **adaptador USB-C a Ethernet vendido por separado**.

    <small>*USB OTG (On-The-Go) es un estándar USB que permite que dispositivos compatibles, como los routers, alternen entre los roles de host y periférico, permitiendo transmisión directa de datos e interacción de alimentación sin un dispositivo host independiente.</small>

    1. Conecte una fuente de red aguas arriba (por ejemplo, un módem del ISP, un switch de red o una toma Ethernet de pared) al puerto USB-C de Mudi 7 mediante un adaptador USB-C a Ethernet.
    2. En la pantalla táctil o en el panel de administración web, vaya a **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, establezca la función del puerto en **WAN** y haga clic en **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 se conectará automáticamente a su dispositivo. Si no se conecta, repita los pasos anteriores o inicie sesión en el panel de administración web y compruebe la conexión USB Ethernet en la página INTERNET.
    4. Cuando la conexión a Internet se establezca correctamente, aparecerán un icono USB y un icono de puerto Ethernet en la esquina superior derecha de la pantalla táctil. También puede comprobar los detalles de la conexión en el panel de administración web.

## Reparación y restablecimiento

Puede restaurar la conectividad de red o restablecer Mudi 7 a los valores de fábrica mediante el botón físico de reinicio.

**Nota**: antes de realizar un restablecimiento, asegúrese de que Mudi 7 haya terminado completamente el arranque. NO pulse el botón de reinicio inmediatamente después de encenderlo, ya que esto puede activar el modo U-Boot failsafe.

Retire la tapa trasera y encontrará el botón de reinicio como se muestra a continuación.

![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

!!! note "Network Repair"

    Mantenga pulsado el botón de reinicio durante **4 segundos** y suéltelo para reparar la red. Mientras mantiene pulsado el botón, preste atención a las indicaciones en pantalla y siga las instrucciones.

    Esto reiniciará la interfaz de red, conservando los ajustes de Wi-Fi, las configuraciones VPN (desactivadas), los ajustes del sistema, etc.

    **Nota**:

    1. Si el Wi-Fi se ha desactivado, un reinicio suave restaurará el Wi-Fi a su estado predeterminado activado.
    2. Un reinicio suave también puede utilizarse para cambiar rápidamente el dispositivo del modo no-router al modo router.

!!! note "Device Reset"

    Mantenga pulsado el botón de reinicio durante **10 segundos** y suéltelo para realizar un reinicio completo. Mientras mantiene pulsado el botón, preste atención a las indicaciones en pantalla y siga las instrucciones.

    Esto borrará toda su configuración. Proceda con precaución.

## Iniciar sesión en el panel de administración web

Puede iniciar sesión en el panel de administración web de Mudi 7 para configurar o comprobar más ajustes.

Primero, conecte un dispositivo, por ejemplo un ordenador, un portátil o un smartphone, a Mudi 7 mediante Wi-Fi, un cable Ethernet o un cable USB.

- **Wi-Fi**

    - <u>QR code</u>: use su dispositivo para escanear el código QR en la pantalla de Mudi 7. Después pulse "Join" en su dispositivo para conectarse.
    - <u>Manual Connect</u>: en su dispositivo, vaya a Settings -> WLAN, localice el nombre de la red Wi-Fi de Mudi 7 en la lista de redes disponibles e introduzca la contraseña para unirse a la red. (Puede encontrar el nombre de red y la contraseña predeterminados impresos en la etiqueta).

- **Ethernet**

    Conecte su dispositivo al puerto Ethernet (LAN por defecto) de Mudi 7 mediante un cable Ethernet.

- **USB**

    Conecte su dispositivo al puerto USB-C de Mudi 7 mediante un cable USB. El puerto USB-C compatible con OTG le permite acceder a la WebGUI de Mudi 7 en el siguiente paso.

Después, abra un navegador web e introduzca `192.168.8.1` en la barra de direcciones para acceder a la página de inicio de sesión. Seleccione su idioma, establezca la contraseña de administrador y haga clic en **Apply**.

Después iniciará sesión en el panel de administración web de Mudi 7.

A continuación se ofrece una visión general de las funciones del panel de administración web de Mudi 7.

## Wireless

La página Wireless le permite configurar ajustes para las redes Wi-Fi de 6 GHz, 5 GHz y 2,4 GHz, incluyendo activar el Wi-Fi, ajustar la potencia TX, definir el nombre de la red Wi-Fi (SSID), activar el BSSID aleatorio, seleccionar el modo de seguridad Wi-Fi y la contraseña, configurar la visibilidad del SSID y elegir el modo Wi-Fi, el ancho de banda y el canal.

Para configurar Wireless, consulte [Wireless](../../interface_guide/wireless.md).

**Nota**: existen algunas diferencias en los ajustes inalámbricos de Mudi 7 en comparación con otros routers GL.iNet Wi-Fi 7.

1. Debido a limitaciones del hardware del chipset, el Wi-Fi de 5 GHz y el de 6 GHz no pueden activarse simultáneamente.
2. Cuando Repeater está activado, Guest Network se desactiva automáticamente.
3. Tal y como exigen las normativas, cambie el Wi-Fi al modo Outdoor cuando lo utilice en exteriores. Esto puede reducir el alcance de cobertura. Puede cambiar Usage Environment (Indoor o Outdoor) en la parte superior de la página Wireless.

## Clients

La página Clients muestra información sobre los dispositivos conectados. Para cada cliente, se muestra el nombre, las direcciones IP y MAC, las velocidades de descarga y subida, el tráfico total y la posibilidad de bloquear el cliente o realizar otras acciones.

Para configurar Clients, consulte [Clients](../../interface_guide/clients.md).

## Servicios en la nube

=== "GoodCloud"

    El servicio de gestión en la nube GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} proporciona una forma sencilla de acceder de forma remota a los routers GL.iNet y gestionarlos.

    Para configurar GoodCloud, consulte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp es una plataforma de red avanzada diseñada para ofrecer redes remotas y gestión remota de dispositivos sin interrupciones. Creada específicamente para integrarse con routers GL.iNet, AstroWarp admite una gestión integral de dispositivos en redes completas, lo que permite controlar tanto los dispositivos superiores como los inferiores. Con un enfoque centrado en la gestión de toda la red y compatibilidad futura con control a nivel de hardware, AstroWarp ofrece una solución más sólida y fiable para gestionar dispositivos y mantener redes seguras y estables.

    Para configurar AstroWarp, consulte [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN (red privada virtual) crea tráfico seguro y cifrado entre su dispositivo y el servidor VPN. Proporciona una capa adicional de privacidad y seguridad cuando se usa como cliente VPN y permite acceder a una red remota cuando se usa como servidor VPN. Mudi 7 es compatible con OpenVPN y WireGuard.

=== "OpenVPN"

    Mudi 7, al igual que otros routers GL.iNet, es compatible con el protocolo OpenVPN, que ofrece una gran seguridad. Para configurar OpenVPN, siga estos tutoriales:

    * [Cómo configurar un cliente OpenVPN](../../interface_guide/openvpn_client.md)
    * [Cómo configurar un servidor OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mudi 7, al igual que otros routers GL.iNet, es compatible con el protocolo WireGuard, que ofrece gran velocidad y comodidad de uso. Para configurar WireGuard, siga estos tutoriales:

    * [Cómo configurar un cliente WireGuard](../../interface_guide/wireguard_client.md)
    * [Cómo configurar un servidor WireGuard](../../interface_guide/wireguard_server.md)

## Network

=== "Multi-WAN"

    Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo ethernet, repeater, tethering, cellular y USB ethernet, al mismo tiempo. Si falla la conexión a Internet actual, el router cambiará automáticamente a otra conexión. Esto garantiza un acceso a Internet fluido e ininterrumpido.

    Para configurar Multi-WAN, consulte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, es una red que conecta ordenadores y dispositivos dentro de un área geográfica limitada, como una vivienda u oficina. Permite transferencias de datos de alta velocidad y compartir recursos, lo que hace posible que los dispositivos se comuniquen entre sí de forma eficiente.

    Para configurar LAN, consulte [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Le permite establecer una subred dentro de los rangos de direcciones privadas IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, especificar las direcciones IP de puerta de enlace y máscara de red, y configurar ajustes de seguridad como el aislamiento AP para la red de invitados.

    Para configurar Guest Network, consulte [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La página DNS le permite establecer servidores DNS personalizados, activar la protección frente a ataques de DNS rebinding y sobrescribir los ajustes DNS de todos los clientes, permitir que el DNS personalizado reemplace al DNS de la VPN, y configurar el modo de ajustes del servidor DNS como automático o especificar manualmente servidores DNS desde la conexión Ethernet.

    Para configurar DNS, consulte [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La página Ethernet Port le permite establecer la función del puerto Ethernet (es decir, usarlo como WAN o LAN), cambiar el modo MAC y la dirección MAC de la interfaz WAN, y mostrar la velocidad negociada del puerto.

    Mudi 7 dispone de un único puerto Ethernet, configurado por defecto como LAN. Puede cambiarlo a WAN desde la pantalla táctil o desde el panel de administración web si es necesario.

    Para gestionar los puertos Ethernet, consulte [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, abreviatura de Internet Protocol version 6, es la versión más reciente del protocolo de Internet diseñada para sustituir a IPv4. Proporciona un espacio de direcciones muchísimo mayor, lo que permite un número prácticamente ilimitado de direcciones IP únicas, algo esencial para dar cabida al creciente número de dispositivos conectados a Internet.

    Para configurar IPv6, consulte [IPv6](../../interface_guide/ipv6.md).

---

=== "IGMP Snooping"

    IGMP Snooping es una técnica de optimización de red utilizada en switches Ethernet para gestionar y controlar el tráfico multicast.

    Para configurar IGMP Snooping, consulte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network mode se refiere a la configuración que determina cómo un dispositivo se conecta a una red y se comunica con otros dispositivos.

    Para configurar Network Mode, consulte [Network Mode](../../interface_guide/network_mode.md).

    **Nota**: Mudi 7 es compatible con Router, Access Point y Extender. No es compatible con el modo WDS.

=== "Drop-in gateway"

    Drop-in gateway amplía la funcionalidad del router principal, incluyendo AdGuard Home, DNS cifrado y cliente VPN.

    Para configurar drop-in gateway, consulte estos enlaces:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration puede reducir la carga de la CPU y acelerar el reenvío de paquetes de tráfico.

    Para configurar Network Acceleration, consulte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "Parental Control"

    Parental Control está diseñado para ayudarle a gestionar y controlar los dispositivos de sus hijos. Incluye la limitación del tiempo de pantalla y la restricción del acceso a determinados contenidos.

    Para configurar el control parental, consulte [Parental Control](../../interface_guide/parental_control.md).

## Security

=== "Port Forwarding"

    Port forwarding permite que servidores remotos y dispositivos de Internet accedan a dispositivos de una red privada.

    Para configurar Port Forwarding, consulte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Management Control le permite configurar varios ajustes de seguridad para proteger la red y el router frente a accesos no autorizados. Esta página incluye las siguientes opciones:

    * Local Access Control: gestionar y restringir el acceso a la interfaz del router desde dispositivos conectados a la red local.
    * Remote Access Control: configurar y restringir el acceso a la interfaz del router desde ubicaciones remotas a través de Internet, reforzando la seguridad frente a amenazas externas.
    * Open Ports on Router: controlar qué puertos están abiertos en el router, limitando posibles vulnerabilidades y accesos no autorizados.

    Estos ajustes le ayudan a mantener un entorno de red seguro, protegiendo tanto el router como los dispositivos conectados.

    Consulte [Security](../../interface_guide/security.md) para ver instrucciones detalladas.

=== "NAT Mode"

    La página NAT Mode le permite activar o desactivar la funcionalidad Full Cone NAT y SIP ALG.

    Para configurar los ajustes NAT, consulte [NAT Mode](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Un plug-in es un componente de software que añade funciones o capacidades específicas a un programa existente, permitiendo personalizarlo y ampliar sus capacidades.

    Para configurar los plug-ins, consulte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) detecta y actualiza automáticamente en tiempo real la dirección IP asociada a un dominio. Resulta especialmente útil para los usuarios que necesitan una dirección IP estática para acceder a una red remota.

    Para configurar Dynamic DNS, consulte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage se refiere a una solución de almacenamiento de datos centralizada que permite que varios usuarios y dispositivos accedan a archivos y los compartan a través de una red.

    Para configurar Network Storage, consulte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home es una solución de bloqueo de anuncios y rastreadores para toda la red que actúa como servidor DNS para filtrar contenido no deseado en todos los dispositivos conectados a una red doméstica.

    Para configurar AdGuard Home, consulte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier es una solución de red definida por software que permite a los usuarios crear redes virtuales seguras a través de Internet, conectando dispositivos como si estuvieran en la misma red local.

    Para configurar ZeroTier, consulte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale es un servicio VPN que le permite acceder a sus dispositivos y aplicaciones desde cualquier lugar.

    Para configurar Tailscale, consulte [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, abreviatura de The Onion Router, es una red centrada en la privacidad que permite la comunicación anónima a través de Internet. Enruta el tráfico de Internet a través de una serie de servidores operados por voluntarios (nodos) para ocultar la ubicación y el uso del usuario, lo que dificulta el rastreo de la actividad en línea.

    Para configurar Tor, consulte [Tor](../../interface_guide/tor.md).

## System

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

    La página Admin Password le permite establecer o cambiar la contraseña de la interfaz de administración del router.

    La contraseña de administrador debe cumplir los siguientes requisitos:

    * Mínimo 10 caracteres y máximo 63 caracteres.
    * Se permiten letras (distinguiendo mayúsculas y minúsculas), números y símbolos `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Se requieren al menos dos de los siguientes grupos: letras mayúsculas, letras minúsculas, números y símbolos.

=== "Upgrade"

    La página Upgrade se utiliza para actualizar el firmware del router a la versión más reciente, garantizando mejor rendimiento, seguridad y nuevas funciones. Esta página ofrece dos opciones de actualización:

    * Firmware Online Upgrade: comprueba automáticamente si hay una nueva versión de firmware y la instala directamente desde el servidor del fabricante, simplificando el proceso.
    * Firmware Local Upgrade: permite cargar manualmente un archivo de firmware desde el ordenador para actualizar el router, lo que le da control sobre la versión y el momento de la actualización.

    Estas opciones le permiten mantener el router actualizado con las mejoras y correcciones más recientes.

    Consulte [Upgrade](../../interface_guide/upgrade.md) para ver instrucciones detalladas.

---

=== "Scheduled Tasks"

    La página Scheduled Tasks le permite configurar reinicios automáticos del router en intervalos específicos, ayudando a mantener un rendimiento y una estabilidad óptimos.

    Consulte [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) para ver instrucciones detalladas.

    **Nota**: Mudi 7 no es compatible con la programación de visualización LED ni con la programación del estado del Wi-Fi.

=== "Display Management"

    La página Display Management le permite gestionar la pantalla táctil y sus ajustes relacionados.

    - Wallpaper: personalice el fondo de pantalla y el estilo de activación.
    - Brightness: ajuste el brillo de la pantalla táctil. Use el control deslizante o introduzca un porcentaje para adaptarlo a distintas condiciones de iluminación.
    - Personalised Signature: añada un texto personalizado a la pantalla táctil para mostrar su estilo o para una identificación rápida.
    - Auto Lock: establezca el tiempo de espera para que la pantalla se bloquee automáticamente cuando no haya actividad. El rango va de 15 segundos a 5 minutos.
    - Passcode: establezca un código para la pantalla táctil como capa adicional de seguridad.

    Consulte [Display Management](../../interface_guide/display_management.md) para ver instrucciones detalladas.

=== "USB & Power"

    La página USB & Power le permite configurar ajustes relacionados con el USB y la gestión de energía del router, como protocolo USB, dirección de alimentación, tiempos de espera por inactividad y comportamiento en espera.

    Consulte [USB & Power](../../interface_guide/usb_power.md) para ver instrucciones detalladas.

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

