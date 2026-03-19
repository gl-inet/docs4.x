# Acceder al router GL.iNet y a AdGuard Home mediante HTTPS

Si desea usar HTTPS para acceder al router GL.iNet y a AdGuard Home, siga los pasos que se indican a continuación.

## 1. Actualizar el certificado y la clave en el router GL.iNet

Primero, solicite un certificado SSL o use un certificado SSL autofirmado.

Luego acceda por SSH a su router GL.iNet o use WinSCP para cargar el certificado y la clave actualizados en su router GL.iNet. Las rutas son las siguientes:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Habilitar AdGuard Home

Inicie sesión en el panel de administración web de GL.iNet -> APPLICATIONS -> AdGuard Home y habilite AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Luego haga clic en **Settings Page** en la parte superior de esta página y será redirigido a la página de configuración de AdGuard Home.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Editar la configuración de Encryption

En la página de configuración de AdGuard Home, vaya a Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Marque la casilla Enable Encryption en la parte superior izquierda e introduzca `3001` en el puerto HTTPS.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Añada las rutas de su certificado y clave actualizados y haga clic en Save.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Después podrá usar HTTPS para acceder a **192.168.8.1** o **192.168.8.1:3001**.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
