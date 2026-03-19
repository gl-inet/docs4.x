# VPN Dashboard, firmware v4.7 y anteriores

**Nota**: Esta guía se basa en el firmware v4.7 y anteriores. Para versiones más recientes, consulte [aquí](vpn_dashboard.md).

---

Inicie sesión en el panel de administración web y vaya a **VPN** -> **VPN Dashboard**.

La página VPN Dashboard sirve para consultar el estado y la configuración de la VPN. Hay dos secciones: [VPN Client](#vpn-client) y [VPN Server](#vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

Al principio, no habrá ninguna configuración disponible para OpenVPN ni WireGuard. Haga clic en **Set Up Now** para ir a las páginas [OpenVPN Client](openvpn_client.md) y [WireGuard Client](wireguard_client.md), respectivamente.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

Una vez completada la configuración, podrá seleccionar el archivo correspondiente en la columna Configuration file.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### Opciones de VPN Client

Haga clic en el icono de engranaje de OpenVPN o WireGuard.

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

Opciones del cliente OpenVPN.

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

Opciones del cliente WireGuard.

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

- Allow Remote Access LAN

  Si esta opción está habilitada, los dispositivos conectados al router podrán acceder a la LAN del lado del servidor VPN, lo que también requiere la configuración adecuada en el lado del servidor VPN.

  Por ejemplo, en la imagen siguiente, si esta opción está habilitada, significa que _Your Device_ puede acceder al _NAS_, pero el _VPN Server_ aún debe permitirle acceder al NAS dentro de su subred.

  ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

- IP Masquerading

  Si esta opción está habilitada, cuando los dispositivos cliente de la LAN envíen sus paquetes IP, el router sustituirá la dirección IP de origen por la suya propia y luego los reenviará al túnel VPN.

- MTU

  Significa maximum transmission unit. El MTU que establezca para esta instancia sobrescribirá el valor MTU del archivo de configuración.

### Modo proxy

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

Como se muestra en la figura anterior, el modo proxy actual es Global Proxy. Haga clic en Global Proxy para cambiar a otros modos proxy. Hay tres tipos: **Global Proxy**, **Policy Mode** y **Route Mode**.

1. Global Proxy

   Todo el tráfico pasará por la VPN. Solo se puede activar una instancia de cliente VPN.

2. Policy Mode
   1. Basado en el dominio o la IP de destino.

      En este modo, solo el tráfico de determinados sitios web definidos por dirección IP o nombre de dominio pasará por la VPN. Solo se puede activar una instancia de cliente VPN.

   2. Basado en el dispositivo cliente.

      En este modo, solo el tráfico de determinados dispositivos cliente locales definidos por dirección MAC pasará por la VPN. Solo se puede activar una instancia de cliente VPN.

   3. Basado en la VLAN.

      En este modo, solo el tráfico de determinadas VLAN puede pasar por la VPN. Solo se puede activar una instancia de cliente VPN.

3. Route Mode
   1. Auto detect

      Se utilizarán las reglas de enrutamiento definidas en cada archivo de configuración del cliente VPN o emitidas por el servidor VPN.

   2. Customize routing rules

      Puede configurar manualmente las reglas de enrutamiento para cada instancia de cliente VPN.

### Opciones globales de VPN Client

Al hacer clic en **Global Options**, aparecerá un cuadro de diálogo con las opciones globales.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Block Non-VPN Traffic

   Si esta opción está habilitada, se bloqueará todo el tráfico de los dispositivos cliente que intente eludir el túnel VPN, lo que evitará eficazmente fugas de VPN causadas por configuraciones DNS del cliente, caídas de conexiones VPN, aplicaciones cliente que realizan solicitudes por IP, etc.

   Esta función también se conoce como [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="\_blank"}. Está diseñada para evitar que sus datos se filtren a Internet. La mayoría de los proveedores de VPN ofrecen una función Kill Switch que desconecta automáticamente su ordenador, teléfono o tablet de Internet si la conexión VPN se cae. La función Block Non-VPN Traffic de los routers GL.iNet puede cubrir más vías de fuga, incluidos los seis escenarios siguientes:
   1. DNS Leak

   2. IPv6 Leak

   3. WebRTC Leak

   4. Dropped VPN Connection

   5. Programs Started Before VPN

   6. Application Specific Leaks

2. Allow Access WAN

   Si esta opción está habilitada, mientras la VPN esté conectada, los dispositivos cliente seguirán pudiendo acceder a la WAN, por ejemplo a su impresora, NAS u otros dispositivos en la subred superior.

   ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

   Como se muestra arriba, si esta función está habilitada, su dispositivo podrá acceder a los dispositivos de la subred ascendente, como la impresora y el NAS.

   El objetivo principal es dar a los clientes acceso a los dispositivos de la subred ascendente, pero el router no tiene forma de distinguir entre la subred ascendente y Internet. Por ello, si el tráfico del dispositivo cliente accede directamente mediante IP, puede existir riesgo de fuga, por lo que esta opción y Block Non-VPN Traffic son mutuamente excluyentes.

3. Services From GL.iNet Use VPN

   Si esta opción está habilitada, los servicios del router que normalmente requieren usar una IP real utilizarán la VPN, incluidos GoodCloud, DDNS y rtty. rtty incluye **Remote SSH** y **Remote Web Access** en la [página GoodCloud](cloud.md#enable-goodcloud-on-router).

   El propósito principal es poder usar al mismo tiempo VPN Client y [GoodCloud](cloud.md) o [DDNS](ddns.md). Se recomienda desactivar esta opción si desea usar GoodCloud, ya que, de lo contrario, la estabilidad de GoodCloud se verá afectada por el estado de la VPN. Si desea usar DDNS, debe desactivar esta opción; de lo contrario, DDNS apuntará a la dirección IP del servidor VPN.

## VPN Server

Al principio, ambos servidores VPN no estarán inicializados todavía. Haga clic en **Set Up Now** para ir a las páginas [OpenVPN Server](openvpn_server.md) y [WireGuard Server](wireguard_server.md), respectivamente.

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

Después de iniciar OpenVPN Server y WireGuard Server.

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### Opciones de OpenVPN Server

Haga clic en el icono de engranaje del servidor OpenVPN.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

- **Allow Remote Access LAN**

  Si esta opción está habilitada, se podrá acceder a los recursos de la subred LAN a través del túnel VPN.

- **IP Masquerading**

  Si esta opción está habilitada, cuando los dispositivos cliente de la LAN envíen sus paquetes IP, el router sustituirá la dirección IP de origen por la suya propia y luego los reenviará al túnel VPN.

- **MTU**

  El MTU que establezca para esta instancia sobrescribirá el valor MTU del archivo de configuración.

### Regla de ruta de OpenVPN Server

Haga clic en el icono de red del servidor OpenVPN.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

En el modo customize routes, el cliente VPN ignorará el archivo de configuración y la configuración de enrutamiento emitida por el servidor. El uso o no del túnel cifrado proporcionado por la VPN al acceder a cualquier segmento de red vendrá determinado por las reglas de enrutamiento que establezca manualmente.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### Opciones de WireGuard Server

Haga clic en el icono de engranaje del servidor WireGuard.

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

- **Allow Remote Access LAN**

  Si esta opción está habilitada, se podrá acceder a los recursos de la subred LAN a través del túnel VPN.

- **IP Masquerading**

  Si esta opción está habilitada, cuando los dispositivos cliente de la LAN envíen sus paquetes IP, el router sustituirá la dirección IP de origen por la suya propia y luego los reenviará al túnel VPN.

- **MTU**

  El MTU que establezca para esta instancia sobrescribirá el valor MTU del archivo de configuración.

- **Client to Client**

  Los clientes WireGuard pueden acceder a los datos entre sí. Los usuarios pueden acceder de forma remota a dispositivos de red internos en casa o en la oficina, y el acceso a los datos mediante el servidor WireGuard es más seguro que el reenvío de puertos gracias al cifrado. Además, una vez conectado, el proceso es más estable y rápido.

### Regla de ruta de WireGuard Server

Haga clic en el icono de red del servidor WireGuard.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

En el modo customize routes, el cliente VPN ignorará el archivo de configuración y la configuración de enrutamiento emitida por el servidor. El uso o no del túnel cifrado proporcionado por la VPN al acceder a cualquier segmento de red vendrá determinado por las reglas de enrutamiento que establezca manualmente.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### Opciones globales de VPN Server

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPN Cascading**: Si esta opción está habilitada, cuando tenga tanto el servidor VPN como el cliente VPN en funcionamiento en este router, los clientes conectados al servidor VPN se enrutarán además al túnel del cliente VPN. [Más información sobre VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
