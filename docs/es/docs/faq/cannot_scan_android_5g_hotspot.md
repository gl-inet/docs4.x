# No se detecta el hotspot 5G de Android

Conectar el router GL.iNet como repetidor al hotspot 5G de un teléfono Android es una de las formas habituales de acceder a Internet.

Sin embargo, si no puede detectar el hotspot 5G de su teléfono Android, el problema puede estar relacionado con el canal Wi-Fi.

Algunos teléfonos Android configuran su hotspot 5G en un canal de EE. UU. de forma predeterminada. Si su router GL.iNet no se compró originalmente en EE. UU., es posible que experimente este problema.

Puede modificar el código de país del Wi-Fi de su router GL.iNet en la interfaz LuCI siguiendo los pasos que se indican a continuación.

1. Inicie sesión en su router GL.iNet y vaya a **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Inicie sesión en LuCI con la misma contraseña de administrador.

2. Edite la configuración de Wi-Fi.

    Vaya a **Network** -> **Wireless**, localice el Wi-Fi de 5 GHz y haga clic en **Edit** a la derecha.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. Seleccione US como código de país.

    En la página Wireless, haga clic en la pestaña **Advanced Settings** dentro de **Device Configuration**. Seleccione US (United States) como código de país para su Wi-Fi de 5 GHz.

    ![5gus](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. Haga clic en **Save & Apply** antes de salir.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    Después, intente detectar de nuevo el hotspot 5G de su teléfono Android.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
