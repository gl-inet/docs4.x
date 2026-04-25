# Configurar el cliente WireGuard en routers GL.iNet

**Nota**: Esta guía se aplica al firmware v4.7 y posteriores. Para versiones anteriores, consulte [aquí](wireguard_client_v4.6.md).

---

WireGuard® es una VPN extremadamente simple, pero a la vez rápida y moderna, que utiliza criptografía de vanguardia. Su objetivo es ser más rápida, simple, ligera y útil que IPsec, evitando al mismo tiempo su gran complejidad. También pretende ofrecer un rendimiento considerablemente superior al de OpenVPN.

Para configurar un cliente WireGuard en un router GL.iNet, vea este video o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Antes de comenzar, asegúrese de tener una suscripción activa con un proveedor de servicios VPN que admita la configuración manual de WireGuard. Haga clic [aquí](https://www.gl-inet.com/solutions/vpn/){target="\_blank"} para consultar los proveedores de WireGuard compatibles con GL.iNet.

Por lo general, primero debe visitar el sitio web oficial del proveedor del servicio VPN al que está suscrito, obtener el archivo de configuración y subirlo al router para configurarlo como cliente WireGuard. Si no sabe cómo obtener el archivo de configuración, consulte [este enlace](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) o contacte con el soporte del proveedor.

Puede configurar un cliente WireGuard mediante el panel de administración web o la [app móvil](../faq/mobile_app.md).

- **La app móvil** integra algunos proveedores de servicios WireGuard, como AzireVPN, Mullvad VPN, OVPN, StrongVPN, PIA VPN, etc., lo que significa que puede configurarlo fácilmente con solo introducir las credenciales de inicio de sesión del servicio WireGuard al que está suscrito. Abra la app y siga las instrucciones en pantalla para completar la configuración.

- **El panel de administración web** no solo integra algunos proveedores de servicios WireGuard, sino que también ofrece una entrada para la configuración manual. Puede introducir las credenciales de su servicio WireGuard para una configuración rápida o subir manualmente un archivo de configuración para completar el proceso.

A continuación se indican los pasos para configurarlo mediante el panel de administración web. Seleccione el proveedor de servicios WireGuard correspondiente para localizar rápidamente las instrucciones paso a paso.

- [Configurar AzireVPN](#configurar-azirevpn)
- [Configurar Hide.me](#configurar-hideme)
- [Configurar IPVanish](#configurar-ipvanish)
- [Configurar Mullvad](#configurar-mullvad)
- [Configurar NordVPN](#configurar-nordvpn)
- [Configurar PIA (Private Internet Access)](#configurar-pia-private-internet-access)
- [Configurar PureVPN](#configurar-purevpn)
- [Configurar Surfshark](#configurar-surfshark)
- [Configurar el cliente WireGuard manualmente (para otros proveedores)](#configurar-el-cliente-wireguard-manualmente-para-otros-proveedores)

## Configurar AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="\_blank"} es un servicio VPN orientado a la privacidad que ofrece túneles seguros, modernos y robustos como WireGuard.

Vea este video para configurar AzireVPN en routers GL.iNet mediante el panel de administración web o la app móvil.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

O siga los pasos a continuación para configurar AzireVPN mediante el panel de administración web.

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Renueve la suscripción.

   Si hace clic en **Go Renew**, será redirigido al sitio web oficial para renovar su suscripción.

   ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Configurar Hide.me {#set-up-hideme}

[Sitio web oficial](https://www.hideipvpn.com/){target="\_blank"}

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Configurar IPVanish {#set-up-ipvanish}

[Sitio web oficial](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="\_blank"}

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Seleccione servidores.

   Seleccione el o los servidores a los que desea conectarse y haga clic en **Apply**.

   ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Configurar Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="\_blank"} es un servicio VPN que ayuda a mantener privadas su actividad en línea, identidad y ubicación.

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Introduzca **Account**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Seleccione servidores.

   Seleccione el o los servidores a los que desea conectarse y haga clic en **Apply**.

   ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Renueve la suscripción.

   Si hace clic en **Go Renew**, será redirigido al sitio web oficial para renovar su suscripción.

   ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Configurar NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="\_blank"} es un servicio VPN en línea que combina velocidad y seguridad.

1. Haga clic [aquí](https://my.nordaccount.com/){target="\_blank"} para iniciar sesión con su cuenta web de NordVPN.

   ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}

   Después de iniciar sesión en el panel de Nord, haga clic en **NordVPN** en el menú izquierdo, busque la sección **Access Token** y luego haga clic en **Get Access token**.

   ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token1.png){class="glboxshadow"}

   En la página siguiente, haga clic en **Generate new token**.

   ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token2.png){class="glboxshadow"}

   En la ventana emergente, seleccione la fecha de caducidad del token y luego haga clic en **Generate token**.

   ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token3.png){class="glboxshadow"}

   A continuación se mostrará el token de acceso. Cópielo para usarlo más adelante.

   **Nota**: El token de acceso solo se muestra una vez. Asegúrese de copiarlo y usarlo ahora. Después de cerrar esta ventana, el token dejará de ser visible. Si no lo guarda, tendrá que generar uno nuevo.

   ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token4.png){class="glboxshadow"}

2. Inicie sesión en el panel de administración web del router y vaya a **VPN** -> **WireGuard Client** -> **NordVPN**.

   Introduzca **Token** y, a continuación, haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Seleccione servidores.

   Seleccione el o los servidores a los que desea conectarse y haga clic en **Apply**.

   ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Configurar PIA (Private Internet Access) {#set-up-pia-private-internet-access}

[Sitio web oficial](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="\_blank"}

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **PIA**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Seleccione servidores.

   Seleccione el o los servidores a los que desea conectarse y haga clic en **Apply**.

   ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Configurar PureVPN {#set-up-purevpn}

[Sitio web oficial](https://billing.purevpn.com/aff.php?aff=35535){target="\_blank"}

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **PureVPN**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**.

   ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

   Se generarán todos los archivos de configuración disponibles.

   ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

3. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

4. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

5. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Configurar Surfshark {#set-up-surfshark}

[Sitio web oficial](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="\_blank"}

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Seleccione servidores.

   Seleccione el o los servidores a los que desea conectarse y haga clic en **Apply**.

   ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Actualice la clave pública.

   Puede hacer clic en **Refresh** para actualizar la clave pública cuando no se pueda conectar al servidor VPN.

   ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Configurar Windscribe {#set-up-windscribe}

[Sitio web oficial](https://windscribe.com/yo/1u2h9ndl){target="\_blank"}

En el panel de administración web, vaya a **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Introduzca **Username** y **Password**, luego haga clic en **Save and Continue**. Se generarán archivos de configuración para cada servidor.

   ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Seleccione servidores.

   Seleccione el o los servidores a los que desea conectarse y haga clic en **Apply**.

   ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

   A continuación, obtendrá una lista de archivos de configuración correspondientes al servidor seleccionado.

   ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Inicie una conexión.

   Seleccione el servidor de su preferencia y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

   Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. Actualice los servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión provocados por mantenimiento o cierre de servidores.

   ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Edite las credenciales o cierre sesión.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión o cerrar sesión.

   ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Actualice la clave pública.

   Puede hacer clic en **Refresh** para actualizar la clave pública cuando no se pueda conectar al servidor VPN.

   ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Elimine todo.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic y elegir si desea eliminar también las claves privada y pública.

   ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Configurar el cliente WireGuard manualmente (para otros proveedores) {#set-up-wireguard-client-manually-for-other-providers}

Si utiliza otro proveedor de servicios WireGuard, puede descargar los archivos de configuración de WireGuard y seguir los pasos a continuación para configurar el cliente WireGuard. Si no sabe cómo descargar los archivos de configuración, consulte [esta guía](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) o contacte con el soporte del proveedor.

En el panel de administración web, vaya a **VPN** -> **WireGuard Client**.

1. Haga clic en **Add Manually**.

   ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. Se creará un grupo en la barra lateral izquierda.

   ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Establezca un nombre descriptivo para el grupo, por ejemplo, azirevpn. Luego suba un archivo de configuración (formatos compatibles: zip, tar, gz, conf, txt) o añada manualmente los detalles de configuración en formato de texto.

   ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}
   1. **Subir un archivo de configuración**.

      Haga clic en el área de carga para subir su archivo de configuración de WireGuard y, a continuación, haga clic en **Apply**.

      ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

      ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

   2. **Añadir configuración manualmente**.

      Haga clic en **Manually Add Configuration** en la parte inferior del área de carga.

      ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

      Establezca un nombre descriptivo y pegue la configuración en el cuadro de texto. Luego haga clic en **Apply**.

      ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
      <small>(Text Mode)</small>

      Si desea verificar cada elemento, puede cambiar al modo Item y revisar los detalles de configuración. Luego haga clic en **Apply**.

      ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
      <small>(Item Mode)</small>

4. Haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. Una vez conectado, puede comprobar el estado de la conexión en la página **VPN Dashboard**.

   ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Configurar el servidor WireGuard en un router GL.iNet

¿No desea suscribirse a servicios VPN de terceros? Puede adquirir dos routers GL.iNet: configure uno como servidor WireGuard y el otro como cliente WireGuard.

Esto es especialmente adecuado para escenarios en los que el ISP de su red doméstica proporciona una IP pública y desea conectarse a su red doméstica mediante VPN cuando está fuera de casa, para garantizar la seguridad y el acceso a los recursos de la red interna. Así evitará el coste y la molestia de suscribirse continuamente a servicios VPN comerciales.

Para la configuración del servidor WireGuard, consulte [aquí](wireguard_server.md).

---

WireGuard® es una marca registrada de Jason A.Donenfeld.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
