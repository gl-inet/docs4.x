# Configurar el cliente WireGuard en routers GL.iNet, firmware v4.6 y anteriores

**Nota**: Esta guía se aplica al firmware v4.6 y anteriores. Para versiones más recientes, consulte [aquí](wireguard_client.md).

---

WireGuard® es una VPN extremadamente simple, rápida y moderna que utiliza criptografía de última generación. Está diseñada para ser más rápida, más sencilla, más ligera y más útil que IPsec, evitando al mismo tiempo su gran complejidad. Su rendimiento previsto es considerablemente superior al de OpenVPN.

Si ya ha contratado un servicio WireGuard con un proveedor, pero no sabe cómo obtener los archivos de configuración, consulte [cómo obtener archivos de configuración de proveedores de servicios WireGuard](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) o contacte con su soporte.

Puede configurar WireGuard Client a través del panel de administración web o la [aplicación móvil](../faq/mobile_app.md).

- La aplicación móvil se integra con varios proveedores de servicios WireGuard, como AzireVPN, Mullvad, OVPN, StrongVPN y PIA VPN.

- El panel de administración web es compatible con menos proveedores de servicios WireGuard, por ejemplo AzireVPN y Mullvad, pero ofrece páginas más intuitivas y detalladas.

A continuación se indican los pasos para configurarlo a través del panel de administración web.

---

Inicie sesión en el panel de administración web y vaya a **VPN** -> **WireGuard Client**.

Si tiene una suscripción a **AzireVPN** o **Mullvad**, puede iniciar sesión directamente con sus credenciales. Alternativamente, haga clic en **Add Manually** para subir manualmente los perfiles de WireGuard.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Configurar AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="\_blank"} es un servicio VPN orientado a la privacidad que proporciona túneles seguros, modernos y robustos, como WireGuard.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Introduzca **Username** y **Password** y haga clic en **Save Credentials & Get Servers**. Se generarán archivos de configuración para cada servidor.

   ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Vaya a VPN Dashboard para habilitar la conexión.

   ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

   Una vez conectado, debería ver su dirección IP de usuario y la cantidad de bytes enviados y recibidos.

   ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Actualizar servidores

   AzireVPN puede poner en mantenimiento o apagar algunos servidores, lo que puede hacer que la conexión falle. Puede usar **Update Servers** para obtener la lista más reciente de servidores disponibles.

   ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Editar credenciales

   Haga clic en el icono de engranaje para editar las credenciales.

   ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Configurar Mullvad

[Mullvad](https://mullvad.net/){target="\_blank"} es un servicio VPN que ayuda a mantener privadas su actividad en línea, su identidad y su ubicación.

El firmware 4.x integra el servicio Mullvad WireGuard.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Introduzca **Account** y haga clic en **Save Credentials & Get Servers**.

   El número de cuenta de Mullvad es un número decimal de 16 dígitos en el rango de "1000 0000 0000 0000" a "9999 9999 9999 9999".

   Aparecerá un cuadro de diálogo para seleccionar una ubicación.

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

   A continuación, se generarán los archivos de configuración del servidor de la ubicación seleccionada.

   La **Public Key** es la clave pública de WireGuard que debe enviarse al servidor de Mullvad. Puede tener hasta cinco claves al mismo tiempo y gestionar las claves de WireGuard en la [página de Mullvad](https://mullvad.net/en/account/#/ports){target="\_blank"}.

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Vaya a VPN Dashboard para habilitar la conexión.

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

   Una vez conectado, debería ver su dirección IP de usuario y la cantidad de bytes enviados y recibidos.

   ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Actualizar servidores

   Mullvad puede poner en mantenimiento o apagar algunos servidores, lo que puede hacer que la conexión falle. Puede usar **Update Servers** para obtener la lista más reciente de servidores disponibles.

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Editar credenciales

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Eliminar la información de la cuenta

   Si hace clic en **Delete**, se eliminarán las credenciales de la cuenta, la clave privada, la clave pública y los archivos de configuración **del router**.

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Eliminar

   Permite eliminar todos los archivos de configuración con un solo clic y muestra una opción para eliminar también la clave privada y la clave pública.

   ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Configurar WireGuard Client

Desde el firmware 4.0, se introdujo la agrupación para gestionar perfiles de WireGuard.

1. Haga clic en **Add Manually**.

   ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Se creará un grupo.

   ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Dé al grupo un nombre descriptivo, por ejemplo azirevpn. Luego puede optar por subir archivos de configuración o añadir la configuración manualmente.

   ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}
   1. **Upload configuration files**

      Suba su archivo de configuración de WireGuard y haga clic en **Apply**.

      ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

      ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

   2. **Manually Add Configuration**: se utiliza si quiere pegar la configuración de WireGuard o completar cada campo manualmente.

      ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

      Asigne un nombre descriptivo y pegue la configuración. Haga clic en **Apply** para continuar.

      ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

      O bien puede añadir la configuración rellenando cada campo. Haga clic en **Item Mode**.

      ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

      ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Haga clic en el icono de tres puntos para iniciar, editar o eliminar el perfil.

   ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Compruebe el estado de la conexión yendo a la página [VPN Dashboard](vpn_dashboard_v4.7.md).

   ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® es una marca registrada de Jason A.Donenfeld.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
