# ¿Cómo actualizar o degradar manualmente el firmware de su router (de v4.x a v4.x)?

Este tutorial le mostrará **cómo actualizar o degradar manualmente el firmware de su router (de v4.x a v4.x)**. Los pasos para actualizar y degradar manualmente el firmware del router son los mismos.

!!! Note "Acerca de la actualización y degradación del firmware del router"

    **Upgrade:** Los routers GL.iNet que ejecutan la versión 4.x del firmware no ofrecen la función de actualización automática.

    Cuando haya disponible una nueva versión de firmware, verá el aviso "Upgrade Reminder" después de iniciar sesión en el panel de administración del router. Puede hacer clic en el botón **Upgrade** para instalar la versión de firmware más reciente que aparece allí. Si quiere actualizar a una versión específica del firmware, siga los pasos siguientes para actualizar el router manualmente.

    **Downgrade:** Puede degradar el firmware de su router para resolver ciertos problemas.

## 1. Comprobar si su router está ejecutando la última versión de firmware (solo para actualización)

1. En un navegador web, introduzca la URL del panel de administración de su router, por ejemplo `192.168.8.1`, e inicie sesión.
2. En la barra lateral izquierda, selecciona **SYSTEM** > **Upgrade**.

## 2. Descargar el archivo de firmware

1. En la barra de búsqueda del [centro de descarga de firmware](https://dl.gl-inet.com/), busque y seleccione el modelo de su router.
2. En la pestaña **Stable** o en otra pestaña, seleccione **Download for common upgrade and uboot** junto a la versión de firmware que quiera descargar.

## 3. Cargar el firmware

Las siguientes instrucciones están escritas para cargar el firmware a través del panel de administración del router. Para cargar el firmware mediante la aplicación móvil GL.iNet, [descarga la aplicación](https://www.gl-inet.com/app/) y configúrala.

1.  En un navegador web, introduzca la URL del panel de administración de su router, por ejemplo `192.168.8.1`, e inicie sesión.
2.  Opcionalmente, si quiere hacer una copia de seguridad de su configuración actual, siga los pasos siguientes.

    ??? "Hacer una copia de seguridad de su configuración actual"

        a. En la barra lateral izquierda, haga clic en **SYSTEM** > **Advanced Settings**.

        b. Haga clic en el enlace o en el botón **Go To LuCI** para acceder a la página de inicio de sesión de LuCI.

        c. Introduzca la contraseña de administrador y haga clic en **Log in**.

        d. Haga clic en **System** > **Backup / Flash Firmware**.

        e. En **Backup**, haga clic en **Generate archive**. Se descargará en su dispositivo un archivo que contiene su configuración actual.

        **Ten en cuenta que este archivo solo es aplicable a la versión de firmware existente en el momento de la copia de seguridad y no a otras versiones de firmware.**

3.  En la barra lateral izquierda, haga clic en **SYSTEM** > **Upgrade**.
4.  Haga clic en **Local Upgrade** y seleccione el archivo que descargó anteriormente.
5.  Para conservar la configuración actual, por ejemplo la contraseña de administrador del router, active **Keep Settings**.
6.  Haga clic en **Install**.

**Nota:** Durante el proceso de actualización, no apagues el router. Cuando la actualización se complete, verás la pantalla de inicio de sesión del router.

Si perdió la configuración del router durante el proceso de actualización del firmware, restaure la configuración del router.

Si el método anterior no funciona, intente actualizar el firmware mediante [U-boot](../faq/debrick.md).

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
