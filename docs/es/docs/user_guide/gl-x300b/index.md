# Guía de usuario de Collie (GL-X300B)

## Descripción general del producto

Collie (GL-X300B) es una pasarela celular industrial diseñada para funcionar a altas temperaturas y en escenarios con posibles riesgos físicos. Existen tres versiones de Collie, diseñadas para operar en instalaciones interiores fijas (GL-X300B-RS485 / GL-X300B-BLE) o en vehículos de transporte (GL-X300B-GPS). Collie es ideal para comunicaciones máquina a máquina entre dispositivos eléctricos en entornos con alto ruido eléctrico.

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

**¿Cuál es la diferencia?**

![gl-x300b series](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b_series.png){class="glboxshadow"}

![gl-x300b comparison](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/model_comparison.png){class="glboxshadow"}

- **GL-X300B-GPS** está equipado con cinco antenas externas, incluidas dos antenas Wi-Fi de 2.4 GHz, dos antenas 4G LTE y una antena GPS. Las antenas cableadas extensibles son perfectas para disponer de varios puntos de recepción dentro de un vehículo, lo que minimiza las zonas sin cobertura al circular por ciudades con alta densidad de red.

- **GL-X300B-BLE** está equipado con tres antenas omnidireccionales externas para comunicación Wi-Fi de 2.4 GHz, 4G LTE y BLE, capaces de recibir señales desde todas las direcciones y ofrecer gran flexibilidad de instalación en un entorno industrial.

- **GL-X300B-RS485** incorpora un chip RS485 con interfaz RS485. El módulo admite transmisión bidireccional de datos de varios dispositivos en el ámbito de la automatización industrial y el IoT, lo que permite funciones de adquisición de datos, control y supervisión.

!!! Note

    Las versiones BLE y GPS están disponibles con una cantidad mínima de pedido.

## Contenido del paquete

Tenga en cuenta que el adaptador incluido en el paquete depende del país de envío.

El paquete incluye:

- 1 x Manual del usuario
- 1 x Collie (GL-X300B)
- 1 x Cable Ethernet
- 1 x Tarjeta de agradecimiento
- 1 x Tarjeta de garantía
- 1 x Adaptador de corriente (tipo de enchufe seleccionado)

**Nota**: La imagen siguiente es un ejemplo del GL-X300B-GPS; algunos modelos pueden variar ligeramente.

![gl-x300b unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/first_time_setup/x300b-gps_unboxing.jpg){class="glboxshadow"}

## Especificaciones

[Especificaciones del GL-X300B](https://www.gl-inet.com/products/gl-x300b/#specs){target="\_blank"}

## Configuración inicial

Todos los routers GL.iNet tienen un proceso de configuración similar. [Haga clic aquí para conocer la configuración inicial](../../faq/first_time_setup.md/).

## INTERNET

Inicie sesión en el panel de administración web del router y vaya a **INTERNET** desde el menú lateral izquierdo.

Esta página le permite seleccionar el tipo de conexión a Internet, como Ethernet, Repeater, Tethering y Cellular, según su modelo.

En el caso de Collie (GL-X300B), admite tres tipos de conexión: Ethernet, Repeater y Cellular.

### Ethernet

Conecte el router a un módem activo o a un dispositivo de red activo mediante un cable Ethernet para acceder a Internet. Este método suele ofrecer la conexión a Internet más rápida y fiable.

[Haga clic aquí para aprender a conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### Repeater

Configure el router como repetidor para ampliar la cobertura Wi-Fi de una red Wi-Fi existente. Como repetidor, recibe y retransmite señales inalámbricas dentro de su alcance, ampliando así la cobertura. Este método resulta útil cuando un solo router no puede cubrir toda el área de uso.

[Haga clic aquí para aprender a conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### Cellular

Inserte una tarjeta SIM en la ranura SIM del router para conectarlo a Internet. Este método es útil para compartir el acceso a Internet de una única tarjeta SIM con todos los dispositivos conectados.

[Haga clic aquí para aprender a conectarse a Internet mediante Cellular](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo Ethernet, Repeater y Cellular, al mismo tiempo. Si falla la conexión a Internet con mayor prioridad, el router cambiará automáticamente a otra conexión. Esto también se denomina Failover y garantiza un acceso a Internet fluido e ininterrumpido.

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

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Consulte los siguientes enlaces para ver una guía de configuración paso a paso:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard

Consulte los siguientes enlaces para ver una guía de configuración paso a paso:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

Los routers GL.iNet incluyen una amplia variedad de funciones adicionales que simplifican la gestión del dispositivo, mejoran la experiencia de Internet del usuario, automatizan las actualizaciones de firmware y mucho más.

### Plug-ins

Visite el tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Visite el tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Visite el tutorial [**GoodCloud**](../../interface_guide/cloud.md).

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
