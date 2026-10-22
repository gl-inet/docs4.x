# Guía de usuario de Mudi V2 (GL-E750V2) {#mudi-v2-gl-e750v2-user-guide}

**Nota:** Mudi V2 (GL-E750V2) y Mudi (GL-E750) ejecutan el mismo firmware. Si está utilizando Mudi (GL-E750), [actualice el firmware](https://dl.gl-inet.com/?model=e750) para usar las funciones y capacidades más recientes.

## Descripción general del producto {#product-overview}

Mudi V2 (GL-E750V2) es un router de viaje 4G LTE portátil compatible con operadores globales. Funciona totalmente en código abierto sobre OpenWrt y el SDK 4.0 de GL.iNet, lo que proporciona capacidad de personalización y un conjunto completo de funciones. Mudi V2 (GL-E750V2) admite velocidades Wi-Fi de 300 Mbps (2.4 GHz) y 433 Mbps (5 GHz), además de tarjetas MicroSD de hasta 1 TB. Incorpora una batería integrada de 7000 mAh. También admite multi-WAN, tanto con conmutación por error como con balanceo de carga, para garantizar una conexión fluida para todos sus dispositivos.

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Botón {#button}

- Pulse el botón de encendido durante **3 segundos**: enciende el dispositivo.

- Pulse el botón de encendido durante **3 a 5 segundos**: entra en el modo de espera.

- Pulse el botón de encendido durante **más de 5 segundos**: apaga el dispositivo.

  (Al pulsarlo durante 3 segundos, la pantalla OLED mostrará primero “Standby Mode On”. SIGA PULSANDO el botón de encendido hasta que vea “Shut Down” debajo de “Standby Mode On”. Comenzará una cuenta atrás de 3 segundos y el dispositivo se apagará.)

## Modo de espera {#standby-mode}

En el modo de espera, Mudi V2 (GL-E750V2) desactiva el Wi-Fi y el 4G para ahorrar energía. No puede conectarse a Mudi V2 (GL-E750V2) en este modo.

Para activar o desactivar el modo de espera, pulse el botón de encendido durante 3 segundos. Verá “Standby Mode On” o “Standby Mode Off” en la pantalla OLED.

## Contenido del paquete {#package-contents}

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Router portátil 4G LTE Mudi V2 (GL-E750V2)
- 1 x Adaptador de corriente
- 4 x Adaptadores de enchufe (US, EU, UK y AU)
- 1 x Manual del usuario
- 1 x Tarjeta de garantía
- 1 x Cable Ethernet
- 1 x Replicador de puertos USB-C
- 1 x Cable USB-C a USB-C
- 1 x Cable USB-A a USB-C
- 1 x Bolsa de transporte
- 1 x Tarjeta de agradecimiento

---

## Configuración inicial {#first-time-setup}

Vea este video o siga los pasos para configurar Mudi V2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Inserte una tarjeta SIM {#1-insert-a-sim-card}

Inserte una tarjeta SIM y, opcionalmente, una tarjeta MicroSD en Mudi V2 (GL-E750V2).

Nota: si va a usar una tarjeta SIM, debe insertarla en el dispositivo antes de encenderlo.

1. Dé la vuelta a Mudi V2 (GL-E750V2).
2. Introduzca el dedo en el orificio situado cerca del borde de la tapa.
3. Deslícelo a lo largo del borde.
4. Cuando la tapa se eleve ligeramente, aproximadamente entre 25 y 30 grados, tire de ella para abrirla.
5. Inserte la tarjeta en la ranura como indica el símbolo situado cerca de la esquina.
6. Presione la tapa hacia abajo para cerrar la cubierta.

### 2. Encienda el dispositivo {#2-power-on}

Pulse el botón de encendido para encender el dispositivo.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_power-on.png){class="glboxshadow"}

Cuando Mudi V2 (GL-E750V2) está apagado, aún puede comprobar el estado de la batería pulsando el botón de encendido. La pantalla OLED mostrará el nivel de batería cuando pulse el botón.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_battery.png){class="glboxshadow"}

Asegúrese de usar un adaptador de corriente estándar de 5 V/2 A. De lo contrario, puede provocar un mal funcionamiento.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET {#internet}

Inicie sesión en el panel de administración web del router y vaya a **INTERNET** desde el menú lateral izquierdo.

Esta página le permite seleccionar el tipo de conexión a Internet, como Ethernet, Repeater, Tethering y Cellular.

### Ethernet {#ethernet}

Conecte el router a un módem activo o a un dispositivo de red activo mediante un cable Ethernet para acceder a Internet. Este método suele ofrecer la conexión a Internet más rápida y fiable.

[Haga clic aquí para aprender a conectarse a Internet mediante un cable Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Configure el router como repetidor para ampliar la cobertura Wi-Fi de una red Wi-Fi existente. Como repetidor, recibe y retransmite señales inalámbricas dentro de su alcance, ampliando así la cobertura. Este método resulta útil cuando un solo router no puede cubrir toda el área de uso.

[Haga clic aquí para aprender a conectarse a Internet mediante una red Wi-Fi existente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Conecte el puerto USB del router a un smartphone con datos móviles activos mediante un cable USB para acceder a Internet. Este método permite que varios dispositivos conectados al router accedan a Internet usando los datos móviles del smartphone.

[Haga clic aquí para aprender a conectarse a Internet mediante USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Retire la tapa trasera de Mudi V2 e inserte una tarjeta SIM en la ranura SIM para conectarse a Internet. Este método es útil para compartir el acceso a Internet de una única tarjeta SIM con todos los dispositivos conectados.

[Haga clic aquí para aprender a conectarse a Internet mediante Cellular](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_cellular.png){class="glboxshadow"}

Para usar una tarjeta física eSIM en su router GL.iNet, haga clic aquí: [¿Cómo usar la tarjeta física eSIM con routers GL.iNet?](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

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

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS {#applications}

Los routers GL.iNet incluyen una amplia variedad de funciones adicionales que simplifican la gestión del dispositivo, mejoran la experiencia de Internet del usuario, automatizan las actualizaciones de firmware y mucho más.

### Plug-ins {#plug-ins}

Visite el tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Visite el tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Visite el tutorial [**GoodCloud**](../../interface_guide/cloud.md).

---

## NETWORK {#network}

### Firewall {#firewall}

Los routers GL.iNet incluyen varias funciones de firewall para garantizar una conexión segura y un control completo por parte de los usuarios. Permiten configurar reglas de firewall, incluidas Port Forwarding, Open Ports y DMZ.

[Haga clic aquí para obtener más información sobre el firewall de los routers GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan}

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

### IGMP Snooping {#igmp-snooping}

Visite el tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Visite el tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet proporciona actualizaciones periódicas del firmware de sus routers para mejorar el rendimiento, resolver errores y corregir vulnerabilidades.

Visite el tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### OLED Screen Settings {#oled-screen-settings}

En esta página puede ajustar qué información se muestra en la pantalla OLED de su Mudi V2 (GL-E750V2).

### Scheduled Tasks {#scheduled-tasks}

Visite el tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Esta función se trasladó a [**Security**](../../interface_guide/security.md) a partir de la versión 4.5.

Visite el tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Visite el tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings {#toggle-button-settings}

Visite el tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log {#log}

Visite el tutorial [**Log**](../../interface_guide/log.md).

### Reset Firmware {#reset-firmware}

Visite el tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Visite el tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
