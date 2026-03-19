# GL.iNet GoodCloud

## Contenido

- [Introducción](#introduccion)
- [Vincular dispositivos a GoodCloud](#vincular-dispositivos-a-goodcloud)
  - [Para firmware v4.6 o anterior](#para-firmware-v46-o-anterior)
    - [Habilitar GoodCloud](#habilitar-goodcloud)
    - [Registrar una cuenta](#registrar-una-cuenta)
    - [Añadir dispositivos](#anadir-dispositivos)
    - [Detalles de la vinculación](#detalles-de-la-vinculacion)
    - [Desvincular dispositivo](#desvincular-dispositivo)
  - [Para firmware v4.7 o posterior](#para-firmware-v47-o-posterior)
    - [Habilitar Cloud Service](#habilitar-cloud-service)
    - [Detalles de la vinculación](#detalles-de-la-vinculacion-1)
    - [Desvincular dispositivo](#desvincular-dispositivo-1)
- [Gestionar dispositivos](#gestionar-dispositivos)
  - [Información del sistema y acciones](#informacion-del-sistema-y-acciones)
  - [Detalles del dispositivo](#detalles-del-dispositivo)
    - [Información básica](#informacion-basica)
    - [Estadísticas](#estadisticas)
    - [Configuración de red](#configuracion-de-red)
    - [Lista de clientes](#lista-de-clientes)
- [Acceso remoto](#acceso-remoto)
  - [GUI remota](#gui-remota)
  - [SSH remoto](#ssh-remoto)
- [Modificar ajustes](#modificar-ajustes)
- [Alarma por correo electrónico](#alarma-por-correo-electronico)
- [Site to Site](#site-to-site)
- [GoodCloud y VPN](#goodcloud-y-vpn)
- [Ver registros](#ver-registros)
- [Deshabilitar la nube](#deshabilitar-la-nube)
- [Eliminar cuenta](#eliminar-cuenta)

## Introducción

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} es una plataforma diseñada para simplificar el despliegue y la gestión remotos de dispositivos conectados. Proporciona una forma sencilla de acceder y gestionar routers GL.iNet a distancia. Al centralizar los dispositivos de red en la nube, los usuarios pueden realizar de forma eficiente tareas de gestión por lotes, como desplegar configuraciones de red y realizar actualizaciones de software. También pueden acceder de forma remota al panel de administración web del router o conectarse al terminal del router por SSH, logrando una gestión de dispositivos de red entre regiones y de extremo a extremo.

Con GoodCloud, puede:

1. Comprobar el estado del router en tiempo real
   - Supervisar el estado en línea y fuera de línea
   - Ver el uso de RAM y la carga media en tiempo real
   - Recibir alertas por correo electrónico sobre cambios de estado en línea y fuera de línea

2. Configurar routers de forma remota
   - Configurar ajustes del router, por ejemplo, SSID y contraseña
   - Acceso remoto por SSH
   - Acceso remoto a la WebUI
   - Compartir el acceso al router con otras personas

3. Supervisar remotamente los clientes conectados
   - Ver los dispositivos conectados a su red
   - Supervisar el tráfico en tiempo real y bloquear clientes
   - Recibir alertas por correo electrónico sobre nuevas conexiones y eventos de bloqueo

4. Realizar operaciones por lotes
   - Reinicio por lotes
   - Actualización de firmware por lotes

5. Establecer conectividad Site-to-Site
   - Oficina virtual: ampliar la red de su oficina a otras sucursales
   - Viajes de negocios: acceder remotamente a los sistemas de oficina, por ejemplo, OA, CRM o MySQL
   - Hogar inteligente: acceder remotamente a dispositivos domésticos, por ejemplo, cámaras IP o NAS

Si necesita gestionar varios dispositivos y desbloquear funciones avanzadas como operaciones masivas, gestión de múltiples cuentas y soluciones personalizadas, elija nuestros planes de valor añadido. Haga clic [aquí](https://www.gl-inet.com/solutions/goodcloud/){target="\_blank"} para ver más detalles y no dude en escribir a [support@glinet.biz](mailto:support@glinet.biz).

## Vincular dispositivos a GoodCloud

Para conectar correctamente los dispositivos a la plataforma en la nube, siga los procedimientos de vinculación correspondientes a su versión de firmware.

### Para firmware v4.6 o anterior

#### Habilitar GoodCloud

Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **GoodCloud**. Active el interruptor para habilitar GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

Habilite **Remote SSH** y **Remote Web Access** según sea necesario, seleccione el servidor más cercano, lea y acepte los **Terms of Service & Privacy Policy** y, a continuación, haga clic en **Apply**.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH**: para acceder remotamente al terminal del router a través de GoodCloud.

- **Remote Web Access**: para acceder remotamente al panel de administración web del router a través de GoodCloud.

- **Data Server**: elija el servidor más cercano a la ubicación de su dispositivo. Hay tres opciones: Asia Pacific, Japón, America, Oregon, y Europe, Ireland.

#### Registrar una cuenta

Visite el [sitio web de GoodCloud](https://www.goodcloud.xyz){target="\_blank"} para registrar una cuenta e iniciar sesión.

Si no recibe el correo de verificación, revise la carpeta de spam o espere unos minutos e inténtelo de nuevo. Si tiene dificultades durante el registro, escriba a [support@glinet.biz](mailto:support@glinet.biz) para obtener ayuda.

#### Añadir dispositivos

En la plataforma Cloud, vaya a **Devices** -> **Bound Devices** -> **Add Devices**.

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

Hay tres métodos para vincular un dispositivo a su cuenta de GoodCloud: Auto Discover, Manually Add y Bulk Import.

??? "Auto Discover"

    Puede probar **Auto discover** si su router y el dispositivo usado para acceder al sitio web de GoodCloud están en la misma red.

    Seleccione su dispositivo en la lista desplegable e introduzca **DDNS / Device ID**, que puede encontrarse en la parte inferior del router o en la página GoodCloud del panel de administración web.

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Consulte [este enlace](../faq/where_to_find_the_device_id_mac_sn.md) para encontrar el Device ID.

??? "Manually Add"

    Si su dispositivo no aparece en la lista, haga clic en **Manually add** e introduzca los datos del router. Toda la información solicitada puede encontrarse en la parte inferior del router o en la página GoodCloud del panel de administración web.

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** está pensado para usuarios que gestionan un gran número de dispositivos. Puede importar varios dispositivos mediante un archivo de Microsoft Excel.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### Detalles de la vinculación

Después de vincular el dispositivo correctamente, vuelva a iniciar sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **GoodCloud**. Actualice esta página y verá el nombre de usuario de GoodCloud vinculado y la fecha.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Desvincular dispositivo

Si desea desvincular su router, inicie sesión en el panel de administración web del router, vaya a **APPLICATION** -> **GoodCloud** y haga clic en **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

Como alternativa, puede eliminar el dispositivo correspondiente de la Bound Devices List en la plataforma GoodCloud. El panel de administración web del router se sincronizará entonces para reflejar el estado más reciente de vinculación del dispositivo.

Si tiene cualquier dificultad, escriba a [support@glinet.biz](mailto:support@glinet.biz) para obtener ayuda.

### Para firmware v4.7 o posterior

#### Habilitar Cloud Service

Inicie sesión en el panel de administración web del router y vaya a **CLOUD SERVICE** -> **GoodCloud**.

Haga clic en el botón **Get Started** y aparecerá una ventana emergente de Cloud Service en la esquina superior derecha. Haga clic en **Enable** para usar Cloud Service.

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

Inicie sesión en su cuenta de GoodCloud.

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

Si no tiene cuenta, registre una e inicie sesión. Una vez completado el registro, el router se vinculará automáticamente a esta cuenta.

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

Si no recibe el correo de verificación, revise la carpeta de spam o espere unos minutos e inténtelo de nuevo. Si tiene dificultades durante el registro, escriba a [support@glinet.biz](mailto:support@glinet.biz) para obtener ayuda.

#### Detalles de la vinculación

Después de vincular el dispositivo correctamente, vuelva a iniciar sesión en el panel de administración web del router, haga clic en el icono de la nube en la esquina superior derecha y verá los detalles de la vinculación, incluidos el nombre de usuario de GoodCloud vinculado y la fecha, el Device ID, el Device MAC y el Device S/N.

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

En el panel de administración web, vaya a **CLOUD SERVICES** -> **GoodCloud**, donde podrá habilitar o deshabilitar el acceso remoto a su router.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH**: para acceder remotamente al terminal del router a través de GoodCloud.

- **Remote Web Access**: para acceder remotamente al panel de administración web del router a través de GoodCloud.

- **View Logs**: mostrará los registros de llamadas API realizadas por GoodCloud.

#### Desvincular dispositivo

Si desea desvincular su router, inicie sesión en el panel de administración web del router. Haga clic en el icono de la nube en la esquina superior derecha y luego en **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

Como alternativa, puede eliminar el dispositivo correspondiente de la Bound Devices List en la plataforma GoodCloud. El panel de administración web del router se sincronizará entonces para reflejar el estado más reciente de vinculación del dispositivo.

Si tiene cualquier dificultad, escriba a [support@glinet.biz](mailto:support@glinet.biz) para obtener ayuda.

## Gestionar dispositivos

### Información del sistema y acciones

En [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} -> **Bound Devices**, puede ver la información del sistema, por ejemplo, modelo, versión, dirección MAC o dirección IP, y el estado, por ejemplo, en línea o fuera de línea, de todos los dispositivos vinculados a su cuenta.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Seleccione un dispositivo y podrá realizar acciones en la esquina superior derecha, como modificar ajustes, actualizar el firmware, acceder remotamente al dispositivo, reiniciarlo o restablecerlo.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Haga clic en el icono de engranaje situado en el extremo derecho de la cabecera de la lista para personalizar las columnas visibles y su orden, de modo que pueda centrarse en la información del dispositivo que más le interese.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Detalles del dispositivo

En [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} -> **Bound Devices**, haga clic en el nombre de un dispositivo y será redirigido a la página de detalles del dispositivo, donde se muestra la información básica del router, datos estadísticos, ajustes de red, lista de clientes, etc.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Información básica

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Estadísticas

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Configuración de red

Esta página muestra las configuraciones de red y los ajustes Wi-Fi de su router.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Lista de clientes

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Acceso remoto

En [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} -> **Bound Devices**, haga clic en el nombre del dispositivo al que desea acceder para entrar en la página de detalles, donde verá acciones remotas en la esquina superior derecha.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### GUI remota

Haga clic en **Remote GUI** para acceder remotamente al panel de administración web de su router.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Si esta opción aparece atenuada o no disponible, es probable que esta función esté deshabilitada. Habilítela primero en el panel de administración web del router antes de acceder a ella mediante GoodCloud.

Si esta opción se puede pulsar, pero no responde, pruebe a usar el modo incógnito o inPrivate del navegador.

### SSH remoto

Haga clic en **Remote SSH** para acceder remotamente al terminal del router mediante SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Si esta opción aparece atenuada o no disponible, es probable que esta función esté deshabilitada. Habilítela primero en el panel de administración web del router antes de acceder a ella mediante GoodCloud.

Si esta opción se puede pulsar, pero no responde, pruebe a usar el modo incógnito o inPrivate del navegador.

## Modificar ajustes

Puede configurar múltiples parámetros para un solo dispositivo o para varios dispositivos.

En [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} -> **Bound Devices**, seleccione el dispositivo que desea configurar y, en la esquina superior derecha, haga clic en **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Aquí puede consultar y modificar los ajustes de red del router, incluidos los de wireless, Ethernet, seguridad, port forwarding, LAN y sistema.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Alarma por correo electrónico

Puede configurar una alarma por correo electrónico cuando cambie el estado del dispositivo, en línea o fuera de línea, o cuando se conecten nuevos clientes.

En [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} -> **Notifications**, haga clic en el botón **Add Rule** en la esquina superior derecha.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Seleccione el dispositivo que desea supervisar y haga clic en **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Seleccione el evento desencadenante, por ejemplo, el estado en línea o fuera de línea del dispositivo, y haga clic en **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Revise la configuración de la regla y haga clic en **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

En la lista Notifications, puede ver las reglas de alerta que ha creado. Los usuarios individuales están limitados a crear una sola regla de alerta. Si necesita gestión masiva de dispositivos, no dude en contactarnos para ampliar su plan.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site

Consulte [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud y VPN

Si habilita **GoodCloud** y **VPN client** al mismo tiempo en su router, la conexión entre el router y el servidor GoodCloud no pasará por la VPN de forma predeterminada. Esto garantiza una conexión más estable con los servicios de GoodCloud.

Sin embargo, si desea que la conexión de GoodCloud pase por la VPN, puede cambiar este ajuste en el panel de administración web del router. Vaya a VPN -> VPN Dashboard -> VPN Client -> Options y habilite la opción "Services from GL.iNet Use VPN".

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Tenga en cuenta que enrutar GoodCloud a través de la VPN puede afectar a la estabilidad de la conexión en la nube, especialmente si:

- La conexión VPN es inestable
- El proveedor de VPN filtra o bloquea el tráfico de GoodCloud
- La VPN añade una latencia significativa a la conexión

En general, se recomienda mantener la configuración predeterminada en la que GoodCloud evita la VPN para lograr un rendimiento y una fiabilidad óptimos.

## Ver registros

Puede ver los registros de GoodCloud cuando lo necesite, incluidos Activity Logs, Device Logs, Upgrade Logs, Alert Logs y Device Settings Logs.

En [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} -> **Logs**, seleccione los registros que desea ver en la lista desplegable.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Deshabilitar la nube

Si ya no desea que su dispositivo esté conectado a la plataforma en la nube, puede deshabilitar el servicio cloud en el panel de administración web del router.

??? "Para firmware v4.6 o anterior"

    Inicie sesión en el panel de administración web del router, vaya a **APPLICATIONS** -> **GoodCloud**, desactive el interruptor de GoodCloud y haga clic en **Apply**

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Una vez deshabilitado, la interfaz se mostrará de la siguiente manera.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Para firmware v4.7 o posterior"

    Inicie sesión en el panel de administración web del router y haga clic en el icono de la nube en la esquina superior derecha.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Una vez deshabilitado, la interfaz se mostrará de la siguiente manera.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Eliminar cuenta

Por razones de seguridad, puede eliminar su cuenta si ya no está en uso.

En la plataforma [GoodCloud](https://www.goodcloud.xyz){target="\_blank"}, haga clic en el nombre de usuario en la esquina superior derecha y seleccione **Personal Center**. Desplácese hasta la parte inferior de la página y haga clic en **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    La eliminación borrará permanentemente todos los servicios relacionados, datos e información personal, sin posibilidad de recuperación.

    Si su cuenta pertenece a alguna organización, abandone primero todas las organizaciones antes de eliminar la cuenta.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
