# Clients {#clients}

En el lado izquierdo del panel de administración web, vaya a **CLIENTS**.

La página Clients muestra información sobre los dispositivos conectados, incluidos el nombre del dispositivo, el tipo de conexión, la dirección IP, la dirección MAC, la velocidad y el tráfico, organizados de izquierda a derecha.

## Nombre del dispositivo {#device-name}

La primera columna muestra el nombre y el tipo de dispositivo, que dependen del hostname del equipo.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Para modificar el nombre y el tipo de dispositivo, haga clic en el icono de tres puntos de la columna Action y, en el menú desplegable, haga clic en **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Tipo de conexión {#connection-type}

El icono azul situado a la derecha del nombre del dispositivo representa el tipo o método de conexión del dispositivo.

Indica cómo está conectado a la red, ya sea por Wi-Fi o mediante un cable Ethernet.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## Dirección IP y MAC {#ip-and-mac-address}

La segunda columna muestra las direcciones IP y MAC del dispositivo conectado.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Muchos dispositivos usan direcciones MAC aleatorias. Si los dispositivos conectados usan direcciones MAC aleatorias, aparecerá el siguiente aviso.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Nota**: La regla utilizada aquí es que, si el segundo carácter de la dirección MAC es 2, 6, A o E, sin distinguir mayúsculas y minúsculas, se considera una dirección MAC aleatoria. Sin embargo, algunos dispositivos pueden usar una regla diferente para generar una MAC aleatoria, por lo que este método de detección puede no ser exacto.

## Velocidad {#speed}

La tercera columna muestra la velocidad de Internet del dispositivo conectado. Este dato representa la velocidad media de los últimos 3 minutos.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

**Nota**: El sistema empieza a calcular la velocidad media cuando se abre esta página. Por ejemplo, si la página lleva abierta 10 segundos, la velocidad media se basará solo en 10 segundos de datos.

## Tráfico {#traffic}

La cuarta columna muestra el tráfico de Internet del dispositivo conectado.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## IP reservada {#reserved-ip}

En la quinta columna, puede reservar una dirección IP para un dispositivo conectado con un solo clic. Esta función se introdujo en el firmware v4.8.

Cuando especifica una dirección IP reservada para un cliente dentro de la LAN, el cliente siempre recibe la misma dirección IP cada vez que accede al servidor DHCP del router.

Puede asignar direcciones IP reservadas a ordenadores o servidores que requieran una configuración IP permanente.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blocklist {#blocklist}

En la sexta columna, puede bloquear dispositivos conectados específicos con un solo clic.

La regla de control de acceso es Blocklist de forma predeterminada, y puede cambiarla a Allowlist desde la parte superior si lo necesita.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Los dispositivos con direcciones MAC incluidas en la lista de bloqueo no pueden conectarse a este router.

- **Allowlist**: Solo pueden conectarse los dispositivos con direcciones MAC específicas, una opción adecuada para dispositivos IoT y la gestión de redes empresariales.

Para crear una Blocklist, puede cargar una lista de bloqueo en formato Excel en **(1)** o introducir direcciones MAC manualmente en **(2)**.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Método 1. Importar clientes**

En la página Access Control, haga clic en **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Haga clic en **Download Import Template** y descargará una hoja XLS llamada `mac-template.csv`.

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Abra el archivo, importe las direcciones MAC y guárdelo.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Seleccione el archivo guardado o arrástrelo al área de carga.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow gl-80-desktop"}

Una vez que la carga se haya realizado correctamente, haga clic en **Import** para completar la importación por lotes de direcciones MAC.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Método 2. Introducir manualmente**

En la página Access Control, introduzca manualmente la dirección MAC de los dispositivos que desea bloquear y haga clic en **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Nota**: El bloqueo del cliente se basa en la dirección MAC del dispositivo. Si el dispositivo bloqueado usa una dirección MAC diferente la próxima vez, podrá seguir conectándose al router.

## Acción {#action}

### Ver detalles {#view-details}

Si necesita ver los detalles del dispositivo cliente, haga clic en el icono de tres puntos de la columna Action, situada más a la derecha, y luego haga clic en **View Details** en el menú desplegable.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Podrá ver toda la información del dispositivo cliente en la subpágina abierta, incluidas todas sus direcciones IPv6 si las hubiera.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modificar {#modify}

Haga clic en el icono de tres puntos de la columna Action y, en el menú desplegable, haga clic en **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Limitar velocidad {#limit-speed}

Haga clic en el icono de tres puntos de la columna Action y, en el menú desplegable, haga clic en **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed1.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Si a un cliente se le ha aplicado una limitación de velocidad, las flechas de subida y bajada de su velocidad se volverán amarillas.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed2.png){class="glboxshadow"}

Haga clic en el icono de tres puntos de la columna Action para desactivar el límite de velocidad.

### Usar túnel VPN {#use-vpn-tunnel}

**Nota**: Esta opción está disponible a partir del firmware v4.8 y solo aparecerá en el menú Action si se ha configurado una política basada en MAC.

Añada un cliente a la lista del túnel VPN con una política basada en MAC. Si necesita hacer ajustes detallados en los túneles, vaya a VPN Dashboard para gestionarlos.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Ordenar {#sort}

La regla de ordenación actual se muestra en la esquina superior derecha y puede cambiarla por otra.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.jpg){class="glboxshadow"}

El tipo de orden predeterminado es el siguiente:

- El propio dispositivo, es decir, el que utiliza para acceder al panel de administración, siempre aparece en la parte superior.
- En la sección Online Clients, los dispositivos que se conectaron antes aparecen más arriba.
- En la sección Offline Clients, los dispositivos que se desconectaron antes aparecen más arriba.

## Ajustes {#settings}

Haga clic en el botón **Settings** de la esquina superior derecha para realizar otras operaciones.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/settings.png){class="glboxshadow"}

- **Clear Traffic Statistics**: Borra con un solo clic las estadísticas de tráfico de todos los clientes en línea. Una vez aplicado, la columna de estadísticas de tráfico se restablecerá a cero y el recuento volverá a empezar.

    ![clear traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic_cleared.png){class="glboxshadow"}

- **Toggle Rate Unit**: Cambia la unidad de velocidad de la columna de velocidad entre **KB/s** y **Kbps**.

- **Auto Remove Offline Clients**: Esta función se introdujo en el firmware v4.9. Una vez activada, todos los clientes sin conexión se eliminarán inmediatamente y no se mostrarán en la sección Offline Clients.

    ![auto removal](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/auto_removal.png){class="glboxshadow"}

## Eliminar clientes {#remove-clients}

En la sección de clientes sin conexión, puede hacer clic en **Delete All** en la esquina superior derecha para eliminar todos los clientes sin conexión.

Si desea eliminar un cliente específico, haga clic en el icono de tres puntos de la columna Action y, en el menú desplegable, haga clic en **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
