# VPN Dashboard (Firmware v4.7 y versiones anteriores)

Inicie sesión en el panel de administración web y vaya a **VPN** -> **VPN Dashboard**.

La página VPN Dashboard muestra detalles de la conexión VPN, como la dirección del servidor, las estadísticas de tráfico, la IP virtual del cliente y el registro de conexión. También permite configurar ajustes avanzados, como el Kill Switch de VPN, la política VPN, el enmascaramiento de IP, el MTU y VPN Cascading.

Esta página se divide en dos secciones: [VPN Client](#vpn-client) y [VPN Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN Client

Cuando entre en esta página por primera vez, si no hay ningún archivo de configuración disponible para OpenVPN y WireGuard, la página se mostrará como se indica a continuación. Haga clic en **Set Up Now** y se le redirigirá a la página [OpenVPN Client](openvpn_client.md) o [WireGuard Client](wireguard_client.md) para cargar su archivo de configuración VPN.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_setup.png){class="glboxshadow"}

Una vez cargada, su configuración aparecerá en la columna **Configuration File**. Si ha cargado varios archivos de configuración, puede cambiar de archivo haciendo clic en el cuadro.

![configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_config.png){class="glboxshadow"}

### Opciones del cliente

Haga clic en el icono de engranaje de la derecha para acceder a las opciones del cliente OpenVPN o WireGuard.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options.png){class="glboxshadow"}

Las opciones de OpenVPN Client se muestran a continuación.

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_ovpn.png){class="glboxshadow"}

Las opciones de WireGuard Client se muestran a continuación.

![wg client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: Si está habilitado, se permitirá el acceso remoto a este router y a sus dispositivos LAN a través de la VPN. El servidor VPN debe anunciar una ruta hacia la subred LAN de este router.

    Por ejemplo, como se muestra en el diagrama siguiente, el router GL.iNet funciona como cliente VPN y se conecta a un servidor VPN a través del túnel VPN. Cuando esta opción está habilitada, tanto el router GL.iNet como sus dispositivos del lado LAN pueden ser accedidos por dispositivos del lado del servidor VPN (por ejemplo, un NAS). Para ello, debe añadir una regla de enrutamiento en el servidor VPN para llegar a la subred LAN del router GL.iNet.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: Si está habilitado, las direcciones IP de origen de los clientes LAN se reescribirán con la IP del túnel VPN del router. Deshabilite esta opción solo en configuraciones site-to-site donde el par remoto conozca sus subredes LAN.

- **MTU**: Abreviatura de Maximum Transmission Unit. Esta opción le permite personalizar el MTU del túnel VPN, sobrescribiendo el valor definido en el archivo de configuración.

### Modo proxy

El modo proxy predeterminado para la conexión VPN es **Global Proxy**. Puede hacer clic en el cuadro de la esquina superior derecha para cambiar a otros modos proxy.

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_proxy.png){class="glboxshadow"}

Hay tres modos proxy disponibles: **Global Proxy**, **Policy Mode** y **Route Mode**.

1. Global Proxy

    En este modo, todo el tráfico se enruta a través de la VPN. Solo se puede activar una instancia de cliente VPN.

2. Policy Mode

    Este modo puede dividirse a su vez en tres políticas.

    - Basado en el dominio o la IP de destino.

        En este modo, solo el tráfico de determinados sitios web identificados por dirección IP o nombre de dominio se enrutará a través de la VPN. Solo se puede activar una instancia de cliente VPN.

    - Basado en el dispositivo cliente.

        En este modo, solo el tráfico de determinados dispositivos LAN identificados por direcciones MAC se enrutará a través de la VPN. Solo se puede activar una instancia de cliente VPN.

    - Basado en la VLAN.

        En este modo, solo el tráfico de determinadas VLAN se enrutará a través de la VPN. Solo se puede activar una instancia de cliente VPN.

3. Route Mode

    - Detección automática

        Se utilizarán las reglas de enrutamiento definidas en cada archivo de configuración del cliente VPN o emitidas por el servidor VPN.

    - Personalizar reglas de enrutamiento

        Puede configurar manualmente las reglas de enrutamiento para cada instancia de cliente VPN.

### Opciones globales

Haga clic en **Global Options** en la esquina superior derecha para configurar ajustes avanzados para su cliente VPN.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: Si está habilitado, todo el tráfico de Internet se obliga a pasar exclusivamente por el túnel VPN y no puede enrutarse a través de otras interfaces, como la WAN local del ISP. Si la conexión VPN se cae de forma inesperada, todo el tráfico de Internet se bloquea por completo para evitar que vuelva a la WAN normal. Esto evita fugas de VPN causadas por fallos de la VPN, configuraciones DNS incorrectas en el cliente y problemas similares.

    Esta función también se conoce como [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Evita que los datos del usuario queden expuestos en línea. Un Kill Switch típico corta automáticamente el acceso a Internet cuando falla la conexión VPN. La función Block Non-VPN Traffic de los routers GL.iNet ofrece una protección más amplia frente a fugas y cubre los siguientes escenarios:

    1. Fuga DNS

    2. Fuga de IPv6

    3. Fuga de WebRTC

    4. Caída de la conexión VPN

    5. Aplicaciones iniciadas antes de establecer la VPN

    6. Fugas de tráfico por aplicación

- **Allow Access WAN**: Si está habilitado, los dispositivos cliente locales seguirán pudiendo acceder a los servicios del lado WAN (por ejemplo, impresoras, NAS y otros dispositivos de la subred superior) mientras la VPN esté activa.

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Como se muestra en el diagrama anterior, al habilitar esta función, sus dispositivos locales podrán acceder a hosts de la subred superior, como impresoras y NAS.

    Esta opción está diseñada principalmente para permitir que los clientes accedan a dispositivos dentro de la subred superior. Sin embargo, el router no puede distinguir el tráfico de la subred superior del tráfico normal de Internet. Si los dispositivos cliente acceden a recursos directamente mediante IP públicas, existe un riesgo potencial de fuga de tráfico. Por este motivo, **Allow Access WAN** y **Block Non-VPN Traffic** son mutuamente excluyentes y no pueden habilitarse al mismo tiempo.

- **Services From GL.iNet Use VPN**: Si está habilitado, los servicios GoodCloud, DDNS y rtty transmitirán paquetes a través de los túneles VPN. Esta opción está deshabilitada de forma predeterminada, ya que estos servicios normalmente requieren la dirección IP real del dispositivo para funcionar correctamente.

## VPN Server

Si el router nunca se ha configurado como servidor OpenVPN o WireGuard, la página se mostrará como se indica a continuación. Haga clic en **Set Up Now** y se le redirigirá a la página **OpenVPN Server** o **WireGuard Server** para inicializar su servidor VPN.

![vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_setup.png){class="glboxshadow"}

Una vez habilitado OpenVPN Server o WireGuard Server, la página mostrará el estado del servidor como se indica a continuación.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_connected.png){class="glboxshadow"}

### Opciones del servidor

Haga clic en el icono de engranaje de la derecha para acceder a las opciones del servidor OpenVPN o WireGuard.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options.png){class="glboxshadow"}

Las opciones de OpenVPN Server se muestran a continuación.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_ovpn.png){class="glboxshadow"}

Las opciones de WireGuard Server se muestran a continuación.

![wg server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: Si está habilitado, se podrá acceder a los recursos de la subred LAN del servidor a través del túnel VPN.

* **IP Masquerading**: Si está habilitado, las direcciones IP de origen de los clientes LAN se reescribirán con la IP del túnel VPN del router. Deshabilite esta opción solo en configuraciones site-to-site donde el par remoto conozca sus subredes LAN.

* **MTU**: Abreviatura de Maximum Transmission Unit. El valor MTU que establezca para el túnel sobrescribirá los ajustes MTU del archivo de configuración.

* **Client to Client**: Si está habilitado, los clientes VPN conectados a este servidor podrán acceder entre sí a través de sus IP del túnel VPN. Si también desea permitir que los clientes accedan a las subredes LAN de los demás, el servidor VPN debe anunciar las rutas correspondientes hacia esas subredes LAN remotas.

* **Client to Client**: Si está habilitado, los clientes VPN conectados a este servidor podrán acceder entre sí a través de sus IP del túnel VPN. Si también desea permitir que los clientes accedan a las subredes LAN de los demás, deberá añadir reglas de enrutamiento en el servidor VPN para anunciar rutas hacia esas subredes LAN remotas.

### Regla de ruta del servidor

Haga clic en el icono de ruta de la derecha para personalizar las reglas de ruta de OpenVPN o WireGuard según sea necesario.

![server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule.png){class="glboxshadow"}

La regla de ruta de OpenVPN Server se muestra a continuación. Haga clic en **Add Route Rule**, introduzca **Target Address** y **Gateway** y, a continuación, haga clic en el icono de verificación verde para aplicar.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

La regla de ruta de WireGuard Server se muestra a continuación. Haga clic en **Add Route Rule**, introduzca **Target Address** y **Gateway** y, a continuación, haga clic en el icono de verificación verde para aplicar.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Nota**: En el modo customize routes, el cliente VPN ignorará el archivo de configuración y la configuración de enrutamiento emitida por el servidor. Que se use o no el túnel VPN cifrado al acceder a cualquier segmento de red vendrá determinado por las reglas de enrutamiento que establezca manualmente.

### Opciones globales

Haga clic en **Global Options** en la esquina superior derecha para configurar ajustes avanzados para su servidor VPN.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: Si está habilitado, cuando este router actúa simultáneamente como servidor VPN y cliente VPN, el tráfico de los clientes VPN remotos conectados al servidor VPN de este router se enrutará a través del túnel VPN ascendente que este router está usando como cliente VPN. [Más información sobre VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
