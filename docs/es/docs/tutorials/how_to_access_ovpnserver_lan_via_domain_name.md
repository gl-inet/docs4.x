# Cómo acceder desde el cliente a dispositivos LAN del servidor OpenVPN mediante nombres de dominio

Este tutorial explica cómo acceder desde un cliente a dispositivos domésticos, como un NAS o una cámara IP, que están en la LAN del servidor OpenVPN usando nombres de dominio.

## Topología

Como se muestra a continuación, puede acceder desde un PC de la LAN del cliente a dispositivos como un NAS o una cámara IP situados en la LAN del servidor OpenVPN usando sus respectivos nombres de dominio.
![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Pasos de configuración

### 1. Editar Hosts en el servidor (opcional)

Este paso se aplica cuando el servidor VPN no puede resolver correctamente los nombres de dominio locales. Si no está seguro, omita este paso.
Inicie sesión en el panel de administración web del router que actúa como servidor VPN y vaya a **NETWORK** -> **DNS** -> **Edit Hosts**.
![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}
Introduzca la IP y el nombre de dominio de los dispositivos domésticos a los que desea acceder y luego haga clic en **Apply**.
![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Permitir acceso remoto a la LAN en el servidor

En el panel de administración web del servidor, vaya a **VPN** -> **OpenVPN Server**. Haga clic en **Options** en la esquina superior derecha.
![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}
Habilite **Allow Remote Access the LAN Subnet** y haga clic en **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}
Cuando está habilitado, se puede acceder de forma remota al router y a los dispositivos LAN mediante la VPN.

### 3. Exportar la configuración VPN

En el panel del servidor, vaya a **VPN** -> **OpenVPN Server** -> pestaña **Configuration** y haga clic en **Export Client Configuration** en la parte inferior.
![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}
En la ventana emergente, haga clic en **Export**.

**Nota**: Si la dirección IP pública de su servidor es dinámica y cambia con el tiempo, vaya a **APPLICATIONS** -> **Dynamic DNS** para habilitar **DDNS** antes de exportar la configuración del cliente.
![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}
A continuación obtendrá un archivo **.ovpn**, como se muestra a continuación.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}
Si su router servidor usa firmware v4.8 o posterior, no es necesario editar el archivo de configuración; continúe con el paso siguiente.
Si su router servidor usa firmware v4.7 o anterior, abra este archivo, añada la siguiente línea para configurar el servidor DNS con la IP del túnel de su servidor OpenVPN y guarde los cambios.
`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}
Sugerencia: la subred IPv4 del túnel del servidor OpenVPN puede encontrarse en la pestaña **Configuration** de la página OpenVPN Server, como se muestra a continuación. Varía según la versión del firmware. Compruebe la IP del túnel de su servidor OpenVPN.
![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Habilitar el servidor VPN

En la página **OpenVPN Server**, haga clic en el botón **Start** de la esquina superior derecha para iniciar el servidor.
![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Subir la configuración VPN

Inicie sesión en el panel de administración web del router cliente VPN, vaya a **VPN** -> **OpenVPN Client** y haga clic en **Add Manually**.
![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}
Cree un nombre para este grupo y suba el archivo de configuración.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}
La carga se completará correctamente. Haga clic en **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}
Verá un archivo de configuración listado aquí.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Iniciar la conexión del cliente VPN

Haga clic en el icono de tres puntos para iniciar la conexión VPN.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}
Cuando el punto gris se vuelva verde, el cliente OpenVPN se habrá conectado correctamente al servidor.
![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}
Ahora puede acceder desde el PC de la LAN del cliente a sus dispositivos domésticos, como un NAS, situados en la LAN del servidor usando sus nombres de dominio.
![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
