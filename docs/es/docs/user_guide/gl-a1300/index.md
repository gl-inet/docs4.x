# Guía de usuario de Slate Plus (GL-A1300)

## Descripción general del producto

Slate Plus (GL-A1300) es un router de viaje de tamaño bolsillo con una CPU potente, optimizada para la estabilidad de la red y para procesar el cifrado VPN de forma eficiente. Incluye nuestras funciones de seguridad más recientes y ejecuta la última versión del sistema operativo OpenWrt. Está diseñado para viajeros frecuentes con una alta demanda de uso de redes VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Contenido del paquete

Tenga en cuenta que el adaptador incluido en el paquete depende del país de envío.

El paquete incluye:

- 1 manual de usuario
- 1 Slate Plus (GL-A1300)
- 1 cable Ethernet
- 1 tarjeta de garantía
- 1 adaptador de corriente, con el tipo de enchufe correspondiente

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Indicación LED

[LED Indication](../../faq/led.md#gl-a1300)

## Especificaciones

[Especificaciones del GL-A1300](https://www.gl-inet.com/products/gl-a1300/#specs){target="\_blank"}

## Configuración inicial

Todos los routers GL.iNet tienen un proceso de configuración sencillo y casi idéntico. [Haga clic aquí para conocer la configuración inicial](../../faq/first_time_setup.md/).

Para configurar Slate Plus, utilizará uno de los cuatro métodos de conexión a Internet compatibles: Ethernet, Repeater, Tethering y Cellular. Consulte este vídeo de configuración.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## INTERNET

La interfaz de configuración de Internet permite a los usuarios elegir el tipo de conexión a Internet compatible con el router.

Configure la red de Internet seleccionando **INTERNET** en el menú lateral del panel de administración web del router.

Admite cuatro formas de conectarse a Internet, como se indica a continuación:

### Ethernet

Transmite datos mediante un cable Ethernet, conectando el router a un módem activo o a un dispositivo de red activo. Este método suele ofrecer la conexión a Internet más rápida y fiable.

[Haga clic aquí para aprender a conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### Repeater

Amplía el área de cobertura Wi-Fi de una red Wi-Fi existente utilizando un router para recibir señales inalámbricas dentro de su alcance y reenviarlas a una distancia mayor. Este método resulta especialmente útil cuando un único router no tiene alcance suficiente para cubrir toda el área de uso.

[Haga clic aquí para aprender a conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### Tethering

Establece acceso a Internet para los dispositivos conectados compartiendo por cable los datos móviles de un smartphone con el router. Este método resulta especialmente útil cuando se desea usar los datos del teléfono para acceder a Internet.

[Haga clic aquí para aprender a conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### Cellular

Conecta el router a Internet insertando un módem USB con capacidad celular en el puerto USB del router. Este método resulta especialmente útil para compartir el acceso a Internet de un módem USB con todos los dispositivos conectados.

[Haga clic aquí para aprender a conectarse a Internet mediante un módem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### Prioridad y balanceo de carga

Vaya a [Multi-WAN](../../interface_guide/multi-wan.md) para establecer la prioridad de cada método de acceso a Internet o el balanceo de carga cuando se usan varios métodos al mismo tiempo.

---

## WIRELESS

La configuración inalámbrica permite a los usuarios gestionar la seguridad de red del Wi-Fi principal y del Guest Wi-Fi. Puede acceder a ella desde **WIRELESS** en el menú lateral.

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

---

## APPLICATIONS

Los routers GL.iNet incluyen una amplia variedad de funciones adicionales que simplifican la gestión del dispositivo, mejoran la experiencia de Internet del usuario, automatizan las actualizaciones de firmware y mucho más.

### Plug-ins

Visite el tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Visite el tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Visite el tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage

Visite el tutorial [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home

Visite el tutorial [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Parental Control

Visite el tutorial [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier

Visite el tutorial [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale

Visite el tutorial [**Tailscale**](../../interface_guide/tailscale.md).

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

Please visit the [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md) tutorial.

### Admin Password

This feature has been moved to [**Security**](../../interface_guide/security.md) since v4.5.

Please visit the [**Admin Password**](../../interface_guide/admin_password.md) tutorial.

### Time Zone

Please visit the [**Time Zone**](../../interface_guide/time_zone.md) tutorial.

### Toggle Button Settings

Please visit the [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md) tutorial.

### Log

Please visit the [**Log**](../../interface_guide/log.md) tutorial.

### Security

This feature is available since v4.5.

Please visit the [**Security**](../../interface_guide/security.md) tutorial.

### Reset Firmware

Please visit the [**Reset Firmware**](../../interface_guide/reset_firmware.md) tutorial.

### Advanced Settings

Please visit the [**Advanced Settings**](../../interface_guide/advanced_settings.md) tutorial.
