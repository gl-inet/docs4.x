# No se detecta el hotspot 5G de Android

Conectar el router GL.iNet como repetidor al hotspot 5G de un teléfono Android es una de las formas habituales de acceder a Internet.

Sin embargo, si no puede detectar el hotspot 5G de su teléfono Android, el problema puede estar relacionado con el código de país de Wi-Fi.

Algunos teléfonos Android configuran su hotspot 5G en un canal de EE. UU. de forma predeterminada. Si su router GL.iNet no se compró originalmente en EE. UU., es posible que experimente este problema.

Puede cambiar el código de país del Wi-Fi de su router GL.iNet en la página LuCI siguiendo los pasos que se indican a continuación.

## Paso 1. Inicie sesión en LuCI

Inicie sesión en su router GL.iNet y, en la barra lateral izquierda, elija **SYSTEM -> Advanced Settings -> Go to LuCI**. Inicie sesión en LuCI con la misma contraseña de administrador.

## Paso 2. Edite la configuración de Wi-Fi

Vaya a **Network -> Wireless**, seleccione el Wi-Fi de 5 GHz y edítelo. Si está usando un GL-MT3000, vaya a **Network -> MTK Wi-Fi**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

![mtkwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/mtkwifi.jpg){class="glboxshadow"}

## Paso 3. Seleccione US como código de país

En **Device Configuration -> Advanced Settings**, seleccione US (United States) como código de país para su Wi-Fi de 5 GHz.

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

Haga clic en **Save & Apply** antes de salir.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

Después, intente detectar de nuevo el hotspot 5G de su teléfono Android.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
