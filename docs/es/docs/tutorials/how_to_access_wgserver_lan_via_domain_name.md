# Cómo acceder desde el cliente a dispositivos LAN del servidor WireGuard mediante nombres de dominio

Este tutorial explica cómo acceder desde un cliente a dispositivos domésticos, como un NAS o una cámara IP, que están en la LAN del servidor WireGuard usando nombres de dominio.

## Topología

Como se muestra a continuación, puede acceder desde un PC de la LAN del cliente a dispositivos como un NAS o una cámara IP situados en la LAN del servidor WireGuard usando sus respectivos nombres de dominio.
![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Pasos de configuración

### 1. Editar Hosts en el servidor (opcional)

Este paso se aplica cuando el servidor VPN no puede resolver correctamente los nombres de dominio locales. Si no está seguro, omita este paso.
Inicie sesión en el panel de administración web del router que actúa como servidor VPN y vaya a **NETWORK** -> **DNS** -> **Edit Hosts**.
![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}
Introduzca la IP y el nombre de dominio de los dispositivos domésticos a los que desea acceder y luego haga clic en **Apply**.
![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Permitir acceso remoto a la LAN en el servidor

??? "Para routers servidor con firmware v4.8"

    En el panel de administración web del servidor, vaya a **VPN** -> **WireGuard Server**. Haga clic en **Options** en la esquina superior derecha.
    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}
    Habilite **Allow Remote Access the LAN Subnet** y haga clic en **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}
    **Cuando está habilitado, se puede acceder de forma remota a este router y a los dispositivos LAN mediante la VPN.**

??? "Para routers servidor con firmware v4.7 y anteriores"

    En el panel de administración web del servidor, vaya a **VPN** -> **VPN Dashboard** -> sección **VPN Server**. Haga clic en el icono de engranaje situado a la derecha del servidor WireGuard.
    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}
    Habilite **Remote Access LAN** y haga clic en **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}
    **Cuando está habilitado, se puede acceder de forma remota a este router y a los dispositivos LAN mediante la VPN.**

### 3. Exportar la configuración VPN

En el panel del servidor, vaya a **VPN** -> **WireGuard Server** -> pestaña **Profiles** y haga clic en **Add** para exportar un perfil de configuración.
![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}
Obtendrá un archivo **.conf**, como se muestra a continuación.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}
Abra este archivo. Asegúrese de que el campo DNS del archivo apunte a la IP del túnel del servidor, que se muestra en la pestaña **Configuration** de la página WireGuard Server, como se indica a continuación. Al mismo tiempo, elimine "64.6.64.6" del campo DNS, si aparece, para evitar fallos en la resolución DNS.
![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}
![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}
**Nota**: La IP del túnel del servidor WireGuard varía según la versión del firmware. Compruebe la IP del túnel de su servidor.

### 4. Habilitar el servidor VPN

En la página **WireGuard Server**, haga clic en el botón **Start** de la esquina superior derecha para iniciar el servidor.
![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Subir la configuración VPN

Inicie sesión en el panel de administración web del router cliente VPN, vaya a **VPN** -> **WireGuard Client** y haga clic en **Add Manually**.
![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}
Cree un nombre para este grupo y suba el archivo de configuración.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}
La carga se completará correctamente. Haga clic en **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}
Verá un archivo de configuración listado aquí.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Iniciar la conexión del cliente VPN

Haga clic en el icono de tres puntos para iniciar la conexión VPN.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}
Cuando el punto gris se vuelva verde, el cliente WireGuard se habrá conectado correctamente al servidor.
![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}
Ahora puede acceder desde el PC de la LAN del cliente a sus dispositivos domésticos, como un NAS, situados en la LAN del servidor usando sus nombres de dominio.
![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
