# Guía de usuario de Cirrus (GL-AP1300)

## Descripción general del producto

Cirrus (GL-AP1300) es un punto de acceso inalámbrico de techo de nivel empresarial con solución Wi-Fi MU-MIMO. Incorpora alimentación PoE y función Watchdog timer para cubrir la mayoría de los casos de uso de nivel empresarial. Gracias al bien desarrollado sistema de gestión GoodCloud, administrar el dispositivo es muy fácil y cómodo. Puede habilitar un acceso remoto y seguro dondequiera que esté y cuando lo necesite.

![gl-ap1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ap1300/hardware_info/ap1300_interface.jpg){class="glboxshadow"}

## Especificaciones

[Especificaciones del GL-AP1300](https://www.gl-inet.com/products/gl-ap1300/#specs){target="\_blank"}

---

## Configuración inicial

Todos los routers GL.iNet tienen un proceso de configuración similar. [Haga clic aquí para conocer la configuración inicial](../../faq/first_time_setup.md/).

---

## INTERNET

Inicie sesión en el panel de administración web del router y vaya a **INTERNET** desde el menú lateral izquierdo.

Esta página le permite seleccionar el tipo de conexión a Internet, como Ethernet, Repeater, Tethering y Cellular, según su modelo.

En el caso de Cirrus (GL-AP1300), admite dos tipos de conexión: Ethernet y Repeater.

### Ethernet

Conecte el router a un módem activo o a un dispositivo de red activo mediante un cable Ethernet para acceder a Internet. Este método suele ofrecer la conexión a Internet más rápida y fiable.

[Haga clic aquí para aprender a conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md)

### Repeater

Configure el router como repetidor para ampliar la cobertura Wi-Fi de una red Wi-Fi existente. Como repetidor, recibe y retransmite señales inalámbricas dentro de su alcance, ampliando así la cobertura. Este método resulta útil cuando un solo router no puede cubrir toda el área de uso.

[Haga clic aquí para aprender a conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md)

### Multi-WAN

Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo Ethernet y Repeater, al mismo tiempo. Si falla la conexión a Internet con mayor prioridad, el router cambiará automáticamente a otra conexión. Esto también se denomina Failover y garantiza un acceso a Internet fluido e ininterrumpido.

Vaya a [Multi-WAN](../../interface_guide/multi-wan.md) para establecer la prioridad de cada conexión a Internet.

Como alternativa, puede cambiar el modo Multi-WAN de Failover a Load Balance, lo que le permite usar varias interfaces de red al mismo tiempo para aumentar el ancho de banda total del router.

---

## WIRELESS

La configuración inalámbrica permite gestionar la seguridad de red del Wi-Fi principal y del Guest Wi-Fi. Puede acceder a ella desde **WIRELESS** en el menú lateral.

[Haga clic aquí para obtener más información sobre la configuración inalámbrica](../../interface_guide/wireless.md)

---

## CLIENTS

Los clientes son los dispositivos conectados al router. Puede bloquear clientes o limitar su velocidad de red. La interfaz está disponible haciendo clic en **CLIENTS** en el menú lateral del panel de administración del router.

[Haga clic aquí para obtener más información sobre la gestión de los dispositivos cliente.](../../interface_guide/clients.md)

---

## VPN

Los routers GL.iNet vienen preinstalados con OpenVPN y WireGuard®, compatibles con más de 30 servicios VPN. Cifran automáticamente todo el tráfico de red dentro de la red conectada, incluidos los dispositivos de invitados y los dispositivos cliente que no pueden ejecutar cifrado VPN por sí mismos. Nuestros routers también pueden actuar como servidores VPN, redirigiendo el tráfico de dispositivos cliente ubicados en lugares remotos al servidor VPN a través de un túnel VPN antes de acceder a Internet pública.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Consulte los siguientes enlaces para ver una guía de configuración paso a paso:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard

Consulte los siguientes enlaces para ver una guía de configuración paso a paso:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

Los routers GL.iNet incluyen una amplia variedad de funciones adicionales que simplifican la gestión del dispositivo, mejoran la experiencia de Internet del usuario, automatizan las actualizaciones de firmware y mucho más.

### Plug-ins

Visite el tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Visite el tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Visite el tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### AdGuard Home

Visite el tutorial [**AdGuard Home**](../../interface_guide/adguardhome.md).

---

## NETWORK

### Firewall

Los routers GL.iNet incluyen varias funciones de firewall para garantizar una conexión segura y un control completo por parte de los usuarios. Permiten configurar reglas de firewall, incluidas Port Forwarding, Open Ports y DMZ.

[Haga clic aquí para obtener más información sobre el firewall de los routers GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Visite el tutorial [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Visite el tutorial [**LAN**](../../interface_guide/lan.md).

### DNS

Visite el tutorial [**DNS**](../../interface_guide/dns.md).

### Network Mode

Visite el tutorial [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Visite el tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

La página Mac Address se llamaba anteriormente Mac Clone y pasó a llamarse Mac Address a partir de la versión 4.2.

Visite el tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Visite el tutorial [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Visite el tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Visite el tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet proporciona actualizaciones periódicas del firmware de sus routers para mejorar el rendimiento, resolver errores y corregir vulnerabilidades.

Visite el tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Visite el tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Esta función se trasladó a [**Security**](../../interface_guide/security.md) a partir de la versión 4.5.

Visite el tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Visite el tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Visite el tutorial [**Log**](../../interface_guide/log.md).

### Security

Esta función está disponible a partir de la versión 4.5.

Visite el tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware

Visite el tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Visite el tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
