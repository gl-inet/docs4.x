# VPN Dashboard (Firmware v4.9)

En el lado izquierdo del panel de administración web, vaya a **VPN** -> **VPN Dashboard**.

VPN Dashboard muestra detalles de la conexión VPN, como reglas de enrutamiento, servidor conectado, estadísticas de tráfico, IP virtual del cliente y registro de conexión, y permite configurar ajustes avanzados como el Kill Switch de la VPN, el enmascaramiento de IP y el MTU.

En comparación con el firmware v4.8, la versión v4.9 incluye las siguientes mejoras en VPN Dashboard:

1. **Permite seleccionar varios perfiles dentro de un grupo de túneles y definir su prioridad**. El túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión.

2. **Cada grupo de túneles funciona de forma independiente y no realiza conmutación por error entre grupos**. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y del túnel **All Other Traffic**.

## Primeros pasos

### Cargar perfil VPN

Cuando entre en esta página por primera vez, si no se ha creado ningún túnel, la página se mostrará como en la imagen siguiente. Haga clic en **Add VPN Tunnel** para empezar.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

Se le dirigirá a la página **VPN Client Profile**. Seleccione un proveedor VPN e inicie sesión.

Los proveedores VPN que aparecen en la lista están integrados en el panel de administración web del router GL.iNet. Con una suscripción activa, solo tiene que introducir sus credenciales para iniciar sesión al instante y obtener los archivos de configuración de las conexiones VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

Si está suscrito a otros proveedores VPN, o si quiere subir sus propias configuraciones VPN, haga clic en **Add Manually** y suba sus configuraciones.

Tomemos **PureVPN** como ejemplo. Haga clic en PureVPN e inicie sesión con credenciales válidas.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Obtendrá una lista de perfiles VPN. En algunos proveedores VPN, es posible que deba seleccionar antes un protocolo VPN o los servidores/ciudades preferidos para que aparezca la lista de perfiles.

Después, haga clic en **Go to Dashboard** en la parte inferior. Se le dirigirá a VPN Dashboard para añadir su túnel VPN y configurar la política VPN.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

### Configurar la política VPN

!!! note "¿Qué es una política VPN?"

    Una política VPN define cómo se enruta el tráfico de red a través de los túneles VPN y determina qué tráfico va a los destinos objetivo a través de la VPN y cuál accede a Internet directamente mediante la WAN local.

    Permite que todos los clientes o dispositivos concretos accedan a sitios web específicos o a todo Internet a través de una conexión VPN, lo que facilita una gestión de red flexible y segura.

En VPN Dashboard, siga el asistente de configuración para definir su política VPN, incluida la selección del perfil VPN, el origen del tráfico y el destino del tráfico.

1. **Seleccione el perfil VPN.**

    Si ya ha iniciado sesión con credenciales de algún servicio VPN integrado o ha subido un archivo de configuración, los perfiles disponibles aparecerán aquí. En caso contrario, vaya a **VPN Client Profile** para iniciar sesión con sus credenciales o subir manualmente un archivo de configuración.

    Tome [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} como ejemplo. Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y de la política [All Other Traffic](#all-other-traffic).

2. **Seleccione el origen del cliente.**

    Hay cuatro opciones:

    - **All Clients**: si se selecciona, el tráfico de todos los dispositivos coincidirá con esta regla.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: si se selecciona, el tráfico de los tipos de conexión especificados (por ejemplo, subred LAN, Drop-in Gateway o Guest Network) coincidirá con esta regla.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: si se selecciona, el tráfico de los dispositivos especificados (identificados por su dirección MAC) coincidirá con esta regla.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: si se selecciona, el tráfico de los dispositivos especificados (identificados por su dirección MAC) no coincidirá con esta regla.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

3. **Seleccione el destino del tráfico**.

    Hay tres opciones:

    - **All Targets**: si se selecciona, el tráfico que coincida con esta regla se enrutará a todos los destinos.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: si se selecciona, el tráfico que coincida con esta regla se enrutará a los dominios o direcciones IP especificados. Debe introducirlos manualmente.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: si se selecciona, el tráfico que coincida con esta regla no se enrutará a los dominios o direcciones IP especificados. Debe introducirlos manualmente.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Kill Switch

!!! note "¿Qué es Kill Switch?"

    Kill Switch es una función de seguridad para conexiones VPN. Corta automáticamente todo el acceso a Internet de su red local si la conexión VPN se interrumpe de forma inesperada, evitando que se expongan su dirección IP real y sus datos en línea y garantizando la privacidad y la seguridad continuas. Esta función es especialmente útil para mantener un acceso a Internet seguro y anónimo, por ejemplo al usar redes públicas, procesar datos sensibles u ocultar su dirección IP real.

    Cuando está habilitado, bloquea cualquier tráfico de clientes que intente eludir el túnel VPN, deteniendo eficazmente las fugas de VPN causadas por problemas de configuración DNS, desconexiones inesperadas, solicitudes directas por IP y otros escenarios similares.

Desde el firmware v4.8, los routers GL.iNet admiten la configuración de un Kill Switch para cada túnel VPN individual, así como para la conexión VPN global.

- Para configurar el Kill Switch de cada túnel VPN individual, consulte [aquí](#tunnel-options).

- Para configurar el Kill Switch de la conexión VPN global, es decir, el Enhanced Kill Switch, consulte [aquí](#all-other-traffic).

## Escenarios de uso

Aquí tiene dos escenarios con instrucciones paso a paso como referencia.

### Escenario 1

**Objetivos**:

1. Solo determinados dispositivos conectados a este router acceden a Internet a través de la VPN. Todos los demás dispositivos accederán a Internet a través de la WAN local.

2. Los dispositivos seleccionados deben usar solo la conexión VPN. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet de estos dispositivos para evitar fugas de DNS y rastreo de IP.

**Siga estos pasos para configurar la política VPN.**

1. Seleccione el perfil VPN.

    Si ya ha iniciado sesión con credenciales de algún servicio VPN integrado o ha subido un archivo de configuración, los perfiles disponibles aparecerán aquí. En caso contrario, vaya a **VPN Client Profile** para iniciar sesión con sus credenciales o subir manualmente un archivo de configuración.

    Tome [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} como ejemplo. Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

    ![scenario 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y de la política [All Other Traffic](#all-other-traffic).

2. Seleccione el origen del cliente.

    Haga clic en la pestaña **Specified Devices**, seleccione los dispositivos que usarán la VPN y haga clic en **Apply**.

    ![scenario 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

3. Seleccione el destino del tráfico.

    Haga clic en la pestaña **All Targets**, establézcala como destino del tráfico y haga clic en **Apply**.

    ![scenario 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

4. Se le dirigirá a VPN Dashboard, donde se habrá añadido un túnel VPN.

    ![scenario 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

5. Asegúrese de que el **Kill Switch** de este túnel esté habilitado. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet del tráfico que coincida con este túnel para evitar fugas de DNS y rastreo de IP.

    ![scenario 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

    ![scenario 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

6. Asegúrese de que **Allow Non-VPN Traffic** esté habilitado. Esta opción está activada por defecto para garantizar que el tráfico que no coincida con el túnel VPN siga pudiendo acceder a Internet a través de la WAN local.

    ![scenario 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

7. Haga clic en el botón central para activar este túnel.

    ![scenario 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

8. Una vez conectado, la página mostrará los detalles de la conexión VPN, incluidos la política VPN, las estadísticas de tráfico, la dirección del servidor, el puerto de escucha y la dirección IP virtual.

    ![scenario 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

    Ahora, solo los dispositivos especificados acceden a Internet a través de la VPN. Si la VPN se desconecta inesperadamente, el acceso a Internet de estos dispositivos se bloqueará para evitar fugas de DNS y rastreo de IP. Todos los demás dispositivos accederán a Internet a través de la WAN local.

### Escenario 2

**Objetivos:**

1. Todos los dispositivos usan **VPN Tunnel 1** al acceder a dominios de determinadas redes sociales y servicios de streaming, y usan **VPN Tunnel 2** para el resto del acceso a Internet.

2. Si los túneles VPN se desconectan inesperadamente, el acceso a Internet de todos los dispositivos se bloqueará para evitar fugas de DNS y rastreo de IP.

**Siga estos pasos para configurar la política VPN.**

1. Seleccione el perfil VPN para Tunnel 1.

    Tome [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} como ejemplo. Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

    ![scenario 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y de la política [All Other Traffic](#all-other-traffic).

2. Seleccione el origen del cliente.

    Haga clic en la pestaña **All Clients**, establézcala como origen del cliente para Tunnel 1 y haga clic en **Apply**.

    ![scenario 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

3. Seleccione el destino del tráfico.

    Haga clic en la pestaña **Specified Domain / IP List**, introduzca dominios de algunos servicios comunes de redes sociales y streaming, como se muestra a continuación, y haga clic en **Apply**.

    ![scenario 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

4. Se le dirigirá a VPN Dashboard, donde se habrá añadido Tunnel 1.

    ![scenario 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

5. Asegúrese de que el **Kill Switch** de Tunnel 1 esté habilitado. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet del tráfico que coincida con este túnel para evitar fugas de DNS y rastreo de IP.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

6. Haga clic en **Add New Tunnel** para añadir Tunnel 2.

    ![scenario 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

7. Seleccione el perfil VPN para Tunnel 2.

    Tome [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} como ejemplo. Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

    ![scenario 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    **Nota**: Cuando se seleccionan varios perfiles, el túnel intentará conectarse usando cada perfil según el orden de prioridad hasta establecer correctamente la conexión. Si todos los perfiles de un mismo túnel no consiguen conectarse, el sistema decidirá si cambia a la WAN local según el estado del Kill Switch del túnel y de la política [All Other Traffic](#all-other-traffic).

8. Seleccione el origen del cliente.

    Haga clic en la pestaña **All Clients**, establézcala como origen del cliente para Tunnel 2 y haga clic en **Apply**.

    ![scenario 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. Seleccione el destino del tráfico.

    Haga clic en la pestaña **All Targets**, establézcala como destino del tráfico para Tunnel 2 y haga clic en **Apply**.

    ![scenario 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

10. Se le dirigirá a VPN Dashboard, donde se habrá añadido Tunnel 2.

    ![scenario 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

11. Asegúrese de que el **Kill Switch** de Tunnel 2 esté habilitado. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet del tráfico que coincida con este túnel para evitar fugas de DNS y rastreo de IP.

    ![tunnel 2 kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

    ![tunnel 2 kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

12. Haga clic en el icono de engranaje de la esquina superior derecha y habilite **Enhanced Kill Switch**. Esto garantiza que todo el tráfico deba acceder a Internet a través de la VPN.

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

13. Haga clic en el botón central para activar Tunnel 1 y Tunnel 2.

    ![scenario 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

14. Una vez conectado, la página mostrará los detalles de la conexión VPN, incluidos la política VPN, las estadísticas de tráfico, la dirección del servidor, el puerto de escucha y la dirección IP virtual.

    ![scenario 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

    Ahora, todos los dispositivos usarán **VPN Tunnel 1** al acceder a los dominios especificados y **VPN Tunnel 2** para el resto del acceso a Internet. Si los túneles VPN se desconectan inesperadamente, el acceso a Internet de todos los dispositivos se bloqueará para evitar fugas de DNS y rastreo de IP.

## All Other Traffic

Haga clic en el icono de engranaje de la esquina superior derecha para configurar la política del tráfico que no coincida con ningún túnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Esta política controla si el tráfico que no coincide con ninguno de sus grupos de túneles VPN puede acceder o no a Internet. Tiene dos opciones: **Allow Non-VPN Traffic** y **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: está habilitado por defecto para garantizar que el tráfico que no coincide con los túneles VPN pueda seguir accediendo a Internet a través de la WAN local.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: obliga a todos los dispositivos a acceder a Internet a través de una VPN. Se bloqueará cualquier tráfico que no coincida con un túnel VPN. Este ajuste global no anula el Kill Switch configurado para cada túnel VPN individual.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Prioridad de los túneles

Para ajustar la prioridad de los túneles, haga clic en el icono de engranaje de un grupo de túneles y seleccione **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Mantenga pulsado el icono de tres líneas situado a la derecha para reordenar los túneles y, a continuación, haga clic en **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Cuando hay varios túneles habilitados, el router enruta el tráfico según las siguientes reglas**:

1. El tráfico intentará primero coincidir con la regla del túnel de mayor prioridad. Si coincide, se enrutará a través de ese túnel; si no, probará con el siguiente túnel según el orden de prioridad, y así sucesivamente.

2. Cada grupo de túneles funciona de forma independiente. Una vez que el tráfico coincide con la regla de un túnel, se enrutará a través de ese túnel y no habrá conmutación por error entre grupos de túneles.

3. Se pueden seleccionar varios perfiles dentro de cada grupo de túneles para permitir la conmutación por error dentro del propio túnel. Cuando el perfil de mayor prioridad de un grupo de túneles deja de estar disponible, el túnel se conectará automáticamente usando el perfil con la segunda mayor prioridad, y así sucesivamente.

4. Si un túnel VPN se desconecta inesperadamente, el sistema decidirá si conmuta el tráfico por error al túnel **All Other Traffic** en función de si el **Kill Switch** de ese túnel está habilitado.

    - Si el Kill Switch está habilitado, el tráfico se bloqueará y no se desviará al túnel **All Other Traffic**.
    - Si el Kill Switch está deshabilitado, el tráfico se desviará al túnel **All Other Traffic**.

5. En el túnel **All Other Traffic**, distintos modos determinan si el tráfico que no coincide con ningún túnel VPN puede acceder a Internet.

    - **Allow Non-VPN Traffic**: está habilitado por defecto para garantizar que el tráfico que no coincide con los túneles VPN pueda seguir accediendo a Internet a través de la WAN local.

    - **Enhanced Kill Switch**: obliga a todos los dispositivos a acceder a Internet a través de una VPN. Se bloqueará cualquier tráfico que no coincida con un túnel VPN. Este ajuste global no anula el Kill Switch configurado para cada túnel VPN individual. En resumen, refuerza el Kill Switch y bloquea el acceso normal a Internet para evitar fugas de IP.

## Opciones del túnel

Puede configurar ajustes avanzados para cada túnel VPN, como el Kill Switch de la VPN, el enmascaramiento de IP y el MTU.

Haga clic en el icono de engranaje de un grupo de túneles y seleccione **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: si está habilitado, el tráfico que coincida con este túnel VPN se bloqueará si la conexión VPN falla inesperadamente. Si está deshabilitado, ese tráfico se desviará al túnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: si está habilitado, los servicios GoodCloud, DDNS y rtty transmitirán paquetes a través de los túneles VPN. Esta opción está deshabilitada por defecto, ya que esos servicios suelen necesitar la IP real del dispositivo para funcionar correctamente.

- **Allow Remote Access to the LAN Subnet**: si está habilitado, se permitirá el acceso remoto a este router y a sus dispositivos LAN a través de la VPN. Requiere que el servidor VPN anuncie una ruta de vuelta a su subred LAN.

- **IP Masquerading**: si está habilitado, las direcciones IP de origen de los clientes LAN se reescribirán con la IP del túnel VPN del router. Deshabilite esta opción solo en configuraciones site-to-site en las que el peer remoto conozca sus subredes LAN.

- **MTU**: el valor MTU que defina para el túnel anulará la configuración MTU del archivo de configuración.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
