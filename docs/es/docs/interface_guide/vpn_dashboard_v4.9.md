# VPN Dashboard (Firmware v4.9)

**Nota**: Esta guía se basa en el firmware v4.9. Para versiones anteriores, consulte [aquí](vpn_dashboard.md).

---

En el lado izquierdo del panel de administración web, vaya a **VPN** -> **VPN Dashboard**.

La página VPN Dashboard muestra detalles de la conexión VPN, como reglas de enrutamiento, servidor conectado, estadísticas de tráfico, IP virtual del cliente y registro de conexión, y permite configurar ajustes avanzados como el Kill Switch de VPN, el enmascaramiento de IP y el MTU.

En comparación con el firmware v4.8, la versión v4.9 incluye las siguientes mejoras en VPN Dashboard:

1. **Permite seleccionar varios perfiles dentro de un grupo de túneles y definir su prioridad**. El túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión.

2. **Cada grupo de túneles funciona de forma independiente y no realiza conmutación por error entre grupos**. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y del túnel **All Other Traffic**.

## Primeros pasos

Cuando entre en esta página por primera vez, si no se ha creado ningún túnel, se mostrará como en la imagen siguiente. Haga clic en **Add VPN Tunnel** para empezar.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**Seleccione un proveedor VPN**. Los proveedores VPN que aparecen en la lista están integrados en el panel de administración web del router GL.iNet. Con una suscripción activa, solo tiene que introducir sus credenciales para iniciar sesión al instante y obtener los archivos de configuración de la conexión VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

Si está suscrito a otros proveedores VPN, o si quiere subir sus propias configuraciones VPN, vaya a **VPN Client Profile** para configurarlo manualmente.

Aquí se usa **Hide.me** como ejemplo. Inicie sesión con las credenciales de Hide.me.

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**Seleccione un servidor VPN**. Es el servidor al que se conectará mediante este túnel VPN, y su dirección IP pública aparecerá como si procediera de la ubicación del servidor seleccionado. Haga clic en **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

Se conectará automáticamente. Haga clic en **Done**.

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

Se le redirigirá a VPN Dashboard, donde **VPN Tunnel 1** ya estará habilitado y conectado.

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**En este ejemplo, todos los clientes conectados a este router accederán a Internet a través de este túnel VPN.**

Si quiere configurar una política VPN, consulte [Politica de VPN](#vpn-policy).

El túnel **All Other Traffic** aparece prehabilitado en la parte inferior de VPN Dashboard. Haga clic [aquí](#all-other-traffic) para obtener más información.

## Detalles del tunel

En VPN Dashboard, cada túnel VPN individual se muestra como en la imagen siguiente, con información detallada como reglas de enrutamiento, servidor conectado, estadísticas de tráfico, dirección del servidor, puerto de escucha, IP virtual del cliente y registro de conexión. Puede habilitar o deshabilitar el túnel VPN y configurar sus ajustes en la parte superior del grupo de túneles.

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

<a id="vpn-policy"></a>

## Politica de VPN

Una política VPN define cómo se enruta el tráfico de red a través de túneles VPN, determinando qué tráfico va a los destinos objetivo por la VPN y cuál accede a Internet directamente mediante la WAN local.

Permite que todos los clientes o dispositivos concretos accedan a sitios web designados o a Internet completo a través de una conexión VPN, lo que facilita una gestión de red flexible y segura.

### Configuracion rapida

En VPN Dashboard, haga clic en **Add New Tunnel** o en la zona central de un túnel VPN existente.

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

Después, siga el asistente de configuración para definir su política VPN, incluida la selección del perfil VPN, el origen del tráfico y el destino del tráfico.

1. **Seleccione el perfil VPN.**

   Si ha iniciado sesión con credenciales de un servicio VPN integrado o ha subido un archivo de configuración, los perfiles disponibles aparecerán aquí. En caso contrario, vaya a **VPN Client Profile** para iniciar sesión con sus credenciales o subir manualmente un archivo de configuración.

   Tome [Hide.me](https://hide.me/en/?friend=glinet){target="\_blank"} como ejemplo. Inicie sesión con las credenciales de su servicio y verá una lista de perfiles VPN. Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

   ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

   **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y del túnel [All Other Traffic](#all-other-traffic).

2. **Seleccione el origen del cliente.**

   Hay cuatro opciones:
   - **All Clients**: Si se selecciona, el tráfico de todos los dispositivos coincidirá con esta regla.
     ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

   - **Specified Connection Types**: Si se selecciona, el tráfico de los tipos de conexión especificados, por ejemplo la subred LAN, Drop-in Gateway o Guest Network, coincidirá con esta regla.
     ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

   - **Specified Devices**: Si se selecciona, el tráfico de los dispositivos especificados, identificados por dirección MAC, coincidirá con esta regla.
     ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

   - **Exclude Specified Devices**: Si se selecciona, el tráfico de los dispositivos especificados, identificados por dirección MAC, no coincidirá con esta regla.
     ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **Seleccione el destino objetivo.**

   Hay tres opciones:
   - **All Targets**: Si se selecciona, el tráfico que coincida con esta regla se enrutará a todos los destinos.
     ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

   - **Specified Domain / IP List**: Si se selecciona, el tráfico que coincida con esta regla se enrutará a los dominios o direcciones IP especificados. Debe introducirlos manualmente.
     ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

   - **Exclude specified Domain / IP List**: Si se selecciona, el tráfico que coincida con esta regla no se enrutará a los dominios o direcciones IP especificados. Debe introducirlos manualmente.
     ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Escenarios de uso

Aquí tiene dos escenarios con instrucciones paso a paso como referencia.

**Escenario 1**

**Objetivos**:

1. Solo determinados dispositivos conectados a este router accederán a Internet a través de la VPN. Todos los demás dispositivos accederán a Internet a través de la WAN local.

2. Los dispositivos seleccionados deben usar únicamente la conexión VPN. Si la VPN se desconecta de forma inesperada, se bloqueará el acceso a Internet de estos dispositivos para evitar fugas DNS y el rastreo de IP.

**Siga los pasos siguientes para configurar la política VPN.**

1. Seleccione el perfil VPN.

   Si ha iniciado sesión con credenciales de un servicio VPN integrado o ha subido un archivo de configuración, los perfiles disponibles aparecerán aquí. En caso contrario, vaya a **VPN Client Profile** para iniciar sesión con sus credenciales o subir manualmente un archivo de configuración.

   Tome [Hide.me](https://hide.me/en/?friend=glinet){target="\_blank"} como ejemplo. Inicie sesión con las credenciales de su servicio y verá una lista de perfiles VPN.

   ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

   Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

   ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

   **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y del túnel [All Other Traffic](#all-other-traffic).

2. Seleccione **Specified Devices** como origen del cliente, luego seleccione los dispositivos que usarán la VPN y haga clic en **Apply**.

   ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. Seleccione **All Targets** como destino objetivo y haga clic en **Apply**.

   ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. Se le redirigirá a VPN Dashboard, donde se habrá añadido un túnel VPN.

   ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. Asegúrese de que el **Kill Switch** de este túnel esté habilitado. Si la VPN se desconecta de forma inesperada, se bloqueará el acceso a Internet del tráfico que coincida con este túnel para evitar fugas DNS y el rastreo de IP.

   ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

   ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}

6. Asegúrese de que **All Other Traffic** esté habilitado y de que el modo esté configurado como **Allow Non-VPN Traffic**. Esto garantiza que el tráfico que no coincida con los túneles VPN anteriores siga pudiendo acceder a Internet a través de la WAN local.

   ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. Active el interruptor para habilitar este túnel.

   ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. Una vez conectado, la página mostrará los detalles de la conexión VPN, incluida la política VPN, las estadísticas de tráfico, la dirección del servidor, el puerto de escucha y la dirección IP virtual.

   ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

   Ahora, solo dos dispositivos especificados accederán a Internet mediante la VPN. Si la VPN se desconecta de forma inesperada, se bloqueará el acceso a Internet de esos dispositivos para evitar fugas DNS y el rastreo de IP. Todos los demás dispositivos accederán a Internet a través de la WAN local.

**Escenario 2**

**Objetivos:**

1. Todos los dispositivos usarán **VPN Tunnel 1** al acceder a dominios de determinados servicios de redes sociales y streaming, y usarán **VPN Tunnel 2** para cualquier otro acceso a Internet.

2. Si los túneles VPN se desconectan de forma inesperada, se bloqueará el acceso a Internet de todos los dispositivos para evitar fugas DNS y el rastreo de IP.

**Siga los pasos siguientes para configurar la política VPN.**

1. Seleccione el perfil VPN para el Túnel 1.

   Si ha iniciado sesión con credenciales de un servicio VPN integrado o ha subido un archivo de configuración, los perfiles disponibles aparecerán aquí. En caso contrario, vaya a **VPN Client Profile** para iniciar sesión con sus credenciales o subir manualmente un archivo de configuración.

   Tome [Hide.me](https://hide.me/en/?friend=glinet){target="\_blank"} como ejemplo. Inicie sesión con las credenciales de su servicio y verá una lista de perfiles VPN.

   ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}

   Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

   ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

   **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y del túnel [All Other Traffic](#all-other-traffic).

2. Seleccione **All Clients** como origen del cliente para el Túnel 1 y haga clic en **Apply**.

   ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Seleccione **Specified Domain / IP List** como destino objetivo para el Túnel 1. Introduzca los dominios de algunos servicios comunes de redes sociales y streaming, como se muestra a continuación, y haga clic en **Apply**.

   ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. Se le redirigirá a VPN Dashboard, donde se habrá añadido el Túnel 1.

   ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Asegúrese de que el **Kill Switch** del Túnel 1 esté habilitado. Si la VPN se desconecta de forma inesperada, se bloqueará el acceso a Internet del tráfico que coincida con este túnel para evitar fugas DNS y el rastreo de IP.

   ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

   ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}

6. Haga clic en **Add New Tunnel** para añadir el Túnel 2.

   ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Seleccione el perfil VPN para el Túnel 2.

   Si ha iniciado sesión con credenciales de un servicio VPN integrado o ha subido un archivo de configuración, los perfiles disponibles aparecerán aquí. En caso contrario, vaya a **VPN Client Profile** para iniciar sesión con sus credenciales o subir manualmente un archivo de configuración.

   Tome [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="\_blank"} como ejemplo. Inicie sesión con las credenciales de su servicio y verá una lista de perfiles VPN.

   ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}

   Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

   ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

   **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y del túnel [All Other Traffic](#all-other-traffic).

8. Seleccione **All Clients** como origen del cliente para el Túnel 2 y haga clic en **Apply**.

   ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Seleccione **All Targets** como destino objetivo para el Túnel 2 y haga clic en **Apply**.

   ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. Se le redirigirá a VPN Dashboard, donde se habrá añadido el Túnel 2.

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Asegúrese de que el **Kill Switch** del Túnel 2 esté habilitado. Si la VPN se desconecta de forma inesperada, se bloqueará el acceso a Internet del tráfico que coincida con este túnel para evitar fugas DNS y el rastreo de IP.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. Deshabilite **All Other Traffic**. Asegúrese de que el modo esté configurado como **Enhanced Kill Switch**. Esto garantiza que todo el tráfico deba acceder a Internet mediante la VPN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. Active el interruptor para habilitar el Túnel 1 y el Túnel 2.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. Una vez conectado, la página mostrará los detalles de la conexión VPN, incluida la política VPN, las estadísticas de tráfico, la dirección del servidor, el puerto de escucha y la dirección IP virtual.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    Ahora, todos los dispositivos usarán **VPN Tunnel 1** al acceder a dominios especificados y usarán **VPN Tunnel 2** para cualquier otro acceso a Internet. Si los túneles VPN se desconectan de forma inesperada, se bloqueará el acceso a Internet de todos los dispositivos para evitar fugas DNS y el rastreo de IP.

<a id="all-other-traffic"></a>

## All Other Traffic

Esta opción controla si el tráfico que no coincide con ninguno de los grupos de túneles VPN anteriores puede acceder a Internet. Está habilitada de forma predeterminada para garantizar el acceso normal a Internet del tráfico que no se enruta por la VPN.

Cuando está habilitada, el tráfico no coincidente puede seguir accediendo a Internet.

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

Cuando está deshabilitada, solo se permite acceder a Internet al tráfico enrutado por la VPN. Se bloqueará todo el tráfico no VPN y el tráfico que haga conmutación por error desde conexiones VPN. Esta opción no anula el Kill Switch individual de cada túnel VPN.

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## Prioridad de tuneles

Para ajustar la prioridad de los túneles, haga clic en el icono de engranaje de un grupo de túneles y seleccione **Sort**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Haga clic y mantenga pulsado el icono de tres líneas de la derecha para reordenar los túneles y, a continuación, haga clic en **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Cuando hay varios túneles habilitados, el router enruta el tráfico según las siguientes reglas**:

1. El tráfico intentará primero coincidir con la regla del túnel de mayor prioridad. Si coincide, se enrutará por ese túnel; en caso contrario, probará con el siguiente túnel por prioridad, y así sucesivamente.

2. Cada grupo de túneles funciona de forma independiente. Una vez que el tráfico coincide con una regla de túnel, se enruta por ese túnel y no realizará conmutación por error entre grupos de túneles.

3. Se pueden seleccionar varios perfiles dentro de cada grupo de túneles para habilitar la conmutación por error dentro del túnel. Cuando el perfil de mayor prioridad de un grupo de túneles deja de estar disponible, el túnel se conectará automáticamente usando el segundo perfil de mayor prioridad, y así sucesivamente.

4. Si un túnel VPN se desconecta de forma inesperada, el sistema decidirá si realiza la conmutación por error del tráfico al túnel **All Other Traffic** en función de si el **Kill Switch** de este túnel está habilitado.
   - Si el Kill Switch está habilitado, el tráfico se bloqueará y no hará conmutación por error hacia el túnel **All Other Traffic**.
   - Si el Kill Switch está deshabilitado, el tráfico hará conmutación por error hacia el túnel **All Other Traffic**.

5. El túnel **All Other Traffic** está habilitado de forma predeterminada para garantizar que el tráfico que no coincide con los túneles VPN siga pudiendo acceder a Internet.
   - Si está habilitado, enruta el tráfico no coincidente o conmutado por error a través de la WAN local.
   - Si está deshabilitado, refuerza el Kill Switch y bloquea el acceso normal a Internet para evitar fugas de IP.

## Opciones del tunel

Puede configurar ajustes avanzados para cada túnel VPN, como el Kill Switch de VPN, el enmascaramiento de IP y el MTU.

Haga clic en el icono de engranaje de un grupo de túneles y seleccione **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: Si está habilitado, el tráfico que coincida con este túnel VPN se bloqueará si la conexión VPN falla de forma inesperada. Si está deshabilitado, ese tráfico hará conmutación por error hacia el túnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: Si está habilitado, los servicios GoodCloud, DDNS y rtty transmitirán paquetes a través de los túneles VPN. Esta opción está deshabilitada de forma predeterminada, ya que estos servicios normalmente requieren la dirección IP real del dispositivo para funcionar correctamente.

- **Allow Remote Access to the LAN Subnet**: Si está habilitado, se permitirá el acceso remoto a este router y a sus dispositivos LAN a través de la VPN. Requiere que el servidor VPN anuncie una ruta de retorno hacia su subred LAN.

- **IP Masquerading**: Si está habilitado, las direcciones IP de origen de los clientes LAN se reescribirán con la IP del túnel VPN del router. Deshabilite esta opción solo en configuraciones site-to-site donde el par remoto conozca sus subredes LAN.

- **MTU**: El valor MTU que establezca para el túnel sobrescribirá los ajustes MTU del archivo de configuración.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
