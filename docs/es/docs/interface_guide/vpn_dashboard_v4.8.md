# VPN Dashboard (Firmware v4.8)

En el lado izquierdo del panel de administración web, vaya a **VPN** -> **VPN Dashboard**.

La página VPN Dashboard muestra detalles de la conexión VPN, como reglas de túnel, dirección del servidor, estadísticas de tráfico, IP virtual del cliente y registro de conexión, y permite configurar ajustes avanzados como el Kill Switch de la VPN, el enmascaramiento de IP y el MTU.

También puede activar varias conexiones VPN para escenarios con múltiples túneles.

<a id="vpn-setup-wizard"></a>

## Asistente de configuración

Haga clic en el icono del libro en la esquina superior izquierda y siga el asistente de configuración de VPN para completar rápidamente la configuración de la VPN.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Nota**: El asistente de configuración de VPN solo está disponible para los servicios VPN integrados, incluidos AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA y Surfshark. Para otros servicios VPN, omita el asistente y vaya a [OpenVPN Client](openvpn_client.md){target="\_blank"} o [WireGuard Client](wireguard_client.md){target="\_blank"} para configurar la VPN manualmente.

Aquí se usa **Hide.me** como ejemplo. Inicie sesión con las credenciales de Hide.me.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Seleccione un servidor VPN y haga clic en **Apply**. Es el servidor al que se conectará mediante este túnel VPN, y su dirección IP pública aparecerá como si procediera de la ubicación del servidor seleccionado.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

Se conectará automáticamente. Una vez establecida correctamente la conexión, vaya a VPN Dashboard y verá que se ha habilitado un túnel VPN.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Se muestran el protocolo VPN utilizado actualmente, por ejemplo WireGuard, el archivo de configuración, la dirección del servidor, el puerto de escucha del servidor, las estadísticas de tráfico y la IP virtual del cliente. Los usuarios pueden ver el registro de conexión en la parte inferior derecha.

Todos los clientes conectados accederán a Internet a través de este túnel VPN.

Si quiere configurar una política VPN, consulte [Modo de políticas](#policy-mode).

## Modo VPN

En VPN Dashboard, haga clic en el botón de la esquina superior derecha para cambiar entre modos VPN.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Hay dos modos disponibles: **Global Mode** y **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Modo global

En este modo, todo el tráfico se enruta a través del túnel VPN y solo puede activarse una instancia de cliente VPN.

Es ideal para escenarios en los que todo el tráfico de los clientes debe enrutarse a través de un único servidor VPN, como una seguridad de red unificada o el acceso a contenido específico por región.

En el ejemplo siguiente, el router se conecta a un servidor australiano mediante el protocolo WireGuard. Todo el tráfico de los clientes conectados se enrutará a través de este túnel VPN.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

<a id="policy-mode"></a>

### Modo de políticas

En este modo, el router puede conectarse a varios servidores VPN y usted puede personalizar reglas de enrutamiento para distintos clientes o destinos del tráfico.

Es adecuado para casos de uso que requieren una gestión flexible del tráfico, como enrutar distintos tipos de tráfico a diferentes destinos a través de varios servidores VPN.

Cambie el modo VPN a Policy Mode y haga clic en **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Después de cambiar, si la VPN no está habilitada, la página se mostrará como se ve a continuación, con tres secciones: Primary Tunnel, Add Tunnel y All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Haga clic en la sección correspondiente para obtener más información.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

<a id="primary-tunnel"></a>

#### Túnel principal

El túnel principal es un túnel <u>predefinido</u> en Policy Mode. Tiene la prioridad más alta, y puede modificar la [prioridad de los túneles](#tunnel-priority) si hay más de un túnel.

En este túnel, puede personalizar la regla del túnel estableciendo tres factores:

1.  **From**: Se refiere al origen del tráfico, es decir, el tráfico que debe enrutarse por este túnel.

    Haga clic en el cuadro atenuado para seleccionar el origen del tráfico.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}
    - **All Clients**: Si se selecciona, el tráfico de todos los dispositivos coincidirá con esta regla.

      ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: Si se selecciona, el tráfico de los tipos de conexión especificados, por ejemplo la subred LAN, Drop-in Gateway o Guest Network, coincidirá con esta regla.

      ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

      Si ha habilitado el servidor OpenVPN o WireGuard en este router, aparecerán más opciones dentro de Specified Connection Types. Esto resulta útil para [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

      ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: Si se selecciona, el tráfico de los dispositivos especificados, identificados por dirección MAC, coincidirá con esta regla.

      ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: Si se selecciona, el tráfico de los dispositivos especificados, identificados por dirección MAC, **NO** coincidirá con esta regla.

      ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2.  **To**: Se refiere a los destinos del tráfico.

    Haga clic en el cuadro atenuado para seleccionar los destinos del tráfico.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}
    - **All Targets**: Si se selecciona, el tráfico que coincida con esta regla se enrutará a todos los destinos.

      ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Si se selecciona, el tráfico que coincida con esta regla se enrutará a los dominios o direcciones IP especificados. Debe introducirlos manualmente.

      Tenga en cuenta que, si especifica un <u>dominio raíz</u>, se incluirán todos sus subdominios. Por ejemplo, si desea incluir `archive.ubuntu.com`, `security.ubuntu.com` y `old-releases.ubuntu.com` en un túnel, solo necesita especificar el dominio raíz `ubuntu.com`.

      ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

      O bien cambie **Input Mode** de Manual a Subscription URL e introduzca el enlace URL.

      ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

      !!! Note

            - Si especifica un dominio raíz, se incluirán todos sus subdominios.

            - Si selecciona Subscribe URL, el nombre de dominio o la IP de la URL se actualizarán automáticamente cada día.

            - Asegúrese de introducir la URL correcta. La detección de la URL verificará la validez del nombre de dominio o de la dirección IP. [Más información](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: Si se selecciona, el tráfico que coincida con esta regla **NO** se enrutará a los dominios o direcciones IP especificados. Debe introducirlos manualmente.

      Tenga en cuenta que, si especifica un <u>dominio raíz</u>, se incluirán todos sus subdominios. Por ejemplo, si desea incluir `archive.ubuntu.com`, `security.ubuntu.com` y `old-releases.ubuntu.com` en un túnel, solo necesita especificar el dominio raíz `ubuntu.com`.

      ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

      O bien cambie **Input Mode** de Manual a Subscription URL e introduzca el enlace URL.

      ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

      !!! Note

            - Si especifica un dominio raíz, se incluirán todos sus subdominios.

            - Si selecciona Subscribe URL, el nombre de dominio o la IP de la URL se actualizarán automáticamente cada día.

            - Asegúrese de introducir la URL correcta. La detección de la URL verificará la validez del nombre de dominio o de la dirección IP. [Más información](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3.  **Via**: Se refiere al método de enrutamiento del tráfico, es decir, si se usará o no la VPN.

    Haga clic en el cuadro atenuado para seleccionar el método de enrutamiento.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}
    - **Use VPN**: Si se selecciona, el tráfico que coincida con esta regla se enrutará a los destinos seleccionados a través de la VPN.

      Para empezar, debe configurar su router como cliente VPN. Use el [Asistente de configuracion](#vpn-setup-wizard) para completar rápidamente la configuración o vaya a OpenVPN Client / WireGuard Client en la barra lateral izquierda para configurarlo manualmente.

      Una vez configurado el router como cliente VPN, seleccione un archivo de configuración VPN para este túnel y haga clic en **Apply**.

      ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: Si se selecciona, el tráfico que coincida con esta regla se enrutará a los destinos seleccionados mediante la WAN local en lugar de la VPN.

      ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4.  Después de seleccionar el origen del tráfico, el destino y el método de enrutamiento, la configuración de la regla del túnel principal queda completada.

En el ejemplo siguiente, la regla de Primary Tunnel es: todos los clientes usan la VPN para acceder a dominios especificados. Su tráfico se enruta a través del servidor australiano y sale a los dominios de Internet seleccionados mediante este túnel.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Nota**: Por seguridad, vaya a [All Other Traffic](#all-other-traffic) y a [Opciones del tunel](#tunnel-options) para revisar otros ajustes antes de habilitar los túneles.

<a id="add-tunnel"></a>

#### Anadir tunel

Para crear túneles adicionales para varias instancias VPN, haga clic en **Add Tunnel** debajo de Primary Tunnel y configure reglas personalizadas.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Asigne un nombre al túnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Obtendrá un túnel más en VPN Dashboard.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Puede añadir más túneles si lo necesita. Se pueden crear hasta 5 túneles, incluido el túnel principal predefinido.

Personalice las reglas del túnel estableciendo el origen del tráfico, los destinos y el método de enrutamiento. Consulte [Tunel principal](#primary-tunnel).

**Nota**: Por seguridad, vaya a [All Other Traffic](#all-other-traffic) y a [Opciones del tunel](#tunnel-options) para revisar otros ajustes antes de habilitar los túneles.

<a id="all-other-traffic"></a>

#### All Other Traffic

En Policy Mode, en la parte inferior de VPN Dashboard aparece un túnel <u>prehabilitado</u>.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Este túnel controla si el tráfico que no coincide con ninguno de los grupos de túneles VPN anteriores puede acceder a Internet. Está habilitado de forma predeterminada para garantizar el acceso normal a Internet del tráfico que no se enruta por la VPN.

- Cuando está habilitado, el tráfico no coincidente puede seguir accediendo a Internet.

  ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Cuando está deshabilitado, solo se permite acceder a Internet al tráfico enrutado por la VPN. Se bloqueará todo el tráfico no VPN y el tráfico que haga conmutación por error desde conexiones VPN. Esta opción no anula el Kill Switch individual de cada túnel VPN.

  ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

<a id="tunnel-priority"></a>

#### Prioridad de tuneles

De forma predeterminada, el túnel Primary Tunnel predefinido tiene la máxima prioridad, seguido de otros túneles añadidos manualmente, si los hay, y después el túnel All Other Traffic para garantizar la conectividad de la red local mediante la WAN local.

Para modificar la prioridad de los túneles, haga clic en **Modify Priority** en la barra superior de información, o haga clic en la **etiqueta de prioridad** en la parte superior izquierda de cualquier túnel, por ejemplo Priority 1 o Priority 2.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Haga clic y mantenga pulsado el icono de tres líneas de la derecha para reordenar los túneles y haga clic en **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Cuando hay varios túneles habilitados, el router enruta el tráfico en el siguiente orden**:

1. El tráfico intentará primero coincidir con la regla del túnel de mayor prioridad. Si coincide, se enrutará por ese túnel; en caso contrario, probará con el siguiente túnel por prioridad, y así sucesivamente, hasta coincidir con el túnel "All Other Traffic".

2. Si un túnel VPN se desconecta de forma inesperada, el sistema decidirá si realiza la conmutación por error del tráfico hacia el siguiente túnel por prioridad en función de si el **Kill Switch** de ese túnel está habilitado.
   - Si el Kill Switch está habilitado, el tráfico se bloqueará y no hará conmutación por error hacia el siguiente túnel por prioridad.
   - Si el Kill Switch está deshabilitado, el tráfico hará conmutación por error hacia el siguiente túnel por prioridad e intentará coincidir con sus reglas de túnel.

3. El túnel **All Other Traffic** está habilitado de forma predeterminada para garantizar que el tráfico que no coincide con los túneles VPN siga pudiendo acceder a Internet.
   - Si está habilitado, enruta el tráfico no coincidente o conmutado por error a través de la WAN local.
   - Si está deshabilitado, refuerza el Kill Switch y bloquea el acceso normal a Internet para evitar fugas de IP.

<a id="tunnel-options"></a>

#### Opciones del tunel

Puede configurar ajustes avanzados para cada túnel VPN, como el Kill Switch de VPN, el enmascaramiento de IP y el MTU.

Haga clic en el icono de engranaje situado junto al nombre de un túnel y seleccione **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: Si está habilitado, el tráfico que coincida con este túnel VPN se bloqueará si la conexión VPN falla de forma inesperada. Si está deshabilitado, ese tráfico hará conmutación por error hacia el siguiente túnel por prioridad o hacia la WAN local.

- **Services from GL.iNet Use VPN**: Si está habilitado, los servicios GoodCloud, DDNS y rtty transmitirán paquetes a través de los túneles VPN. Esta opción está deshabilitada de forma predeterminada, ya que estos servicios normalmente requieren la dirección IP real del dispositivo para funcionar correctamente.

- **Allow Remote Access the LAN Subnet**: Si está habilitado, se permitirá el acceso remoto a este router y a sus dispositivos LAN a través de la VPN. Requiere que el servidor VPN anuncie una ruta de retorno hacia su subred LAN.

- **IP Masquerading**: Si está habilitado, las direcciones IP de origen de los clientes LAN se reescribirán con la IP del túnel VPN del router. Deshabilite esta opción solo en configuraciones site-to-site donde el par remoto conozca sus subredes LAN.

- **MTU**: El valor MTU que establezca para el túnel sobrescribirá los ajustes MTU del archivo de configuración.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
