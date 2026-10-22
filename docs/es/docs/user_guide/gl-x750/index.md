# Guía de usuario de Spitz (GL-X750) {#spitz-gl-x750-user-guide}

## Descripción general del producto {#product-overview}

Spitz es un router inalámbrico de doble banda 3G/4G, ampliamente utilizado en el ámbito del hogar inteligente y el IoT. Ejecuta OpenWrt OS, por lo que puede compilar su propio firmware para adaptarlo a diferentes escenarios de uso. Incorpora un módulo mini PCIe 3G/4G para admitir distintos operadores y puede utilizarse en todo el mundo.

Spitz V2 (GL-X750V2) es la versión avanzada de Spitz (GL-X750). Incluye una PCBA rediseñada y antenas optimizadas para mejorar el rendimiento 4G.

![gl-x750 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/x750v2_interface.jpg){class="glboxshadow"}

## Especificaciones {#specifications}

[Especificaciones del GL-X750](https://www.gl-inet.com/products/gl-x750/#specs){target="_blank"}

---

## Configuración inicial {#first-time-setup}

Todos los routers GL.iNet tienen un proceso de configuración similar. [Haga clic aquí para conocer la configuración inicial](../../faq/first_time_setup.md).

---

## INTERNET {#internet}

Inicie sesión en el panel de administración web del router y vaya a **INTERNET** desde el menú lateral izquierdo.

Esta página le permite seleccionar el tipo de conexión a Internet, como Ethernet, Repeater, Tethering y Cellular.

### Ethernet {#ethernet}

Conecte el router a un módem activo o a un dispositivo de red activo mediante un cable Ethernet para acceder a Internet. Este método suele ofrecer la conexión a Internet más rápida y fiable.

[Haga clic aquí para aprender a conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Configure el router como repetidor para ampliar la cobertura Wi-Fi de una red Wi-Fi existente. Como repetidor, recibe y retransmite señales inalámbricas dentro de su alcance, ampliando así la cobertura. Este método resulta útil cuando un solo router no puede cubrir toda el área de uso.

[Haga clic aquí para aprender a conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Conecte el puerto USB del router a un smartphone con datos móviles activos mediante un cable USB para acceder a Internet. Este método permite que varios dispositivos conectados al router accedan a Internet usando los datos móviles del smartphone.

[Haga clic aquí para aprender a conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Inserte una tarjeta SIM en la ranura SIM del router para conectarlo a Internet. Este método es útil para compartir el acceso a Internet de una única tarjeta SIM con todos los dispositivos conectados.

[Haga clic aquí para aprender a conectarse a Internet mediante Cellular](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN es una función de red que le permite configurar el router con varias conexiones a Internet, por ejemplo Ethernet, Repeater y Cellular, al mismo tiempo. Si falla la conexión a Internet con mayor prioridad, el router cambiará automáticamente a otra conexión. Esto también se denomina Failover y garantiza un acceso a Internet fluido e ininterrumpido.

Vaya a [Multi-WAN](../../interface_guide/multi-wan.md) para establecer la prioridad de cada conexión a Internet.

Como alternativa, puede cambiar el modo Multi-WAN de Failover a Load Balance, lo que le permite usar varias interfaces de red al mismo tiempo para aumentar el ancho de banda total del router.

---

## WIRELESS {#wireless}

La configuración inalámbrica permite gestionar la seguridad de red del Wi-Fi principal y del Guest Wi-Fi. Puede acceder a ella desde **WIRELESS** en el menú lateral.

[Haga clic aquí para obtener más información sobre la configuración inalámbrica](../../interface_guide/wireless.md)

---

## CLIENTS {#clients}

Los clientes son los dispositivos conectados al router. Puede bloquear clientes o limitar su velocidad de red. La interfaz está disponible haciendo clic en **CLIENTS** en el menú lateral del panel de administración del router.

[Haga clic aquí para obtener más información sobre la gestión de los dispositivos cliente.](../../interface_guide/clients.md)

---

## VPN {#vpn}

Los routers GL.iNet vienen preinstalados con OpenVPN y WireGuard®, compatibles con más de 30 servicios VPN. Cuando el cliente VPN está habilitado, el router puede cifrar el tráfico de los dispositivos de la red, incluidos los que no pueden ejecutar aplicaciones VPN, según la configuración de sus políticas VPN. Nuestros routers también pueden actuar como servidores VPN, redirigiendo el tráfico de dispositivos cliente ubicados en lugares remotos al servidor VPN a través de un túnel VPN antes de acceder a Internet pública.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Consulte los siguientes enlaces para ver una guía de configuración paso a paso:

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Consulte los siguientes enlaces para ver una guía de configuración paso a paso:

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS {#applications}

Los routers GL.iNet incluyen una amplia variedad de funciones adicionales que simplifican la gestión del dispositivo, mejoran la experiencia de Internet del usuario, automatizan las actualizaciones de firmware y mucho más.

### Plug-ins {#plug-ins}

Visite el tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Visite el tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Visite el tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### Parental Control {#parental-control}

Visite el tutorial [**Parental Control**](../../interface_guide/parental_control.md).

---

## NETWORK {#network}

### Firewall {#firewall}

Los routers GL.iNet incluyen varias funciones de firewall para garantizar una conexión segura y un control completo por parte de los usuarios. Permiten configurar reglas de firewall, incluidas Port Forwarding, Open Ports y DMZ.

[Haga clic aquí para obtener más información sobre el firewall de los routers GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Visite el tutorial [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Visite el tutorial [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Visite el tutorial [**DNS**](../../interface_guide/dns.md).

### Network Mode {#network-mode}

Visite el tutorial [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Visite el tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

La página Mac Address se llamaba anteriormente Mac Clone y pasó a llamarse Mac Address a partir de la versión 4.2.

Visite el tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Visite el tutorial [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Visite el tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Visite el tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet proporciona actualizaciones periódicas del firmware de sus routers para mejorar el rendimiento, resolver errores y corregir vulnerabilidades.

Visite el tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks {#scheduled-tasks}

Visite el tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Esta función se trasladó a [**Security**](../../interface_guide/security.md) a partir de la versión 4.5.

Visite el tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Visite el tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Log {#log}

Visite el tutorial [**Log**](../../interface_guide/log.md).

### Security {#security}

Esta función está disponible a partir de la versión 4.5.

Visite el tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Visite el tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Visite el tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
