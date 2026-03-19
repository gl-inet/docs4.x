# Cómo acceder a la interfaz LuCI mediante GoodCloud

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} supera las limitaciones geográficas y ofrece una forma cómoda de administrar routers de forma remota. A través de GoodCloud, puede acceder a la interfaz LuCI del router en cualquier momento y desde cualquier lugar, realizar distintos ajustes en el router y administrar la red con facilidad.

## Preparación

- Equipo de hardware: un router GL.iNet configurado con acceso a Internet y funcionando con normalidad.
- Entorno de red: la red a la que está conectado el router es estable y puede acceder a Internet con normalidad.
- Vinculación del dispositivo: necesita [vincular su router GL.iNet a su cuenta de GoodCloud](../interface_guide/cloud.md/#setup-your-goodcloud-account). Si no tiene una cuenta de GoodCloud, puede [registrarse](https://www.goodcloud.xyz/){target="_blank"}.

## Pasos para acceder a la interfaz LuCI mediante GoodCloud

### Para firmware versión 4.7 o superior

Desde la versión 4.7, los usuarios pueden acceder directamente a la página LuCI desde la plataforma GoodCloud sin pasar por el panel de administración web del router.

1. Inicie sesión en su cuenta de GoodCloud [aquí](https://www.goodcloud.xyz/){target="_blank"}.
2. En el lado izquierdo, vaya a **Devices** -> **Bound Devices**. Haga clic en el nombre del dispositivo al que desea acceder y verá los iconos de acceso web remoto.
    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}
    La ventana emergente muestra el puerto 80. Cámbielo a **8080** y haga clic en Apply.
    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}
3. Será redirigido a la página de inicio de sesión de LuCI. Introduzca su contraseña de administrador para iniciar sesión.
    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}
4. Ya ha iniciado sesión en LuCI correctamente.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### Para firmware versión 4.6 o inferior

1. Inicie sesión en su cuenta de GoodCloud [aquí](https://www.goodcloud.xyz/){target="_blank"}.
2. En el lado izquierdo, vaya a **Devices** -> **Bound Devices**. Haga clic en el nombre del dispositivo al que desea acceder y verá los iconos de acceso web remoto.
    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}
    La ventana emergente muestra el puerto 80. Haga clic en Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}
3. A continuación, será redirigido a la página de inicio de sesión del panel de administración de GL.iNet. Introduzca su contraseña de administrador para iniciar sesión.
    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}
4. Después de iniciar sesión, en el lado izquierdo vaya a SYSTEM -> Advanced Settings y haga clic en el hipervínculo para ir a la interfaz LuCI.
    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}
    Será redirigido a la página de inicio de sesión de LuCI. Introduzca la misma contraseña de administrador para iniciar sesión.
    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}
5. Ya ha iniciado sesión en LuCI correctamente.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
