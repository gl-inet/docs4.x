# Usar WinSCP para acceder a sus archivos compartidos

Puede usar **WinSCP** para acceder a sus archivos compartidos mediante la función de uso compartido de archivos de los routers **GL.iNet**.

Primero configure sus enlaces de **WebDAV** en la pestaña de almacenamiento en red. Para ver la configuración detallada, consulte [WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav).

## Configurar enlaces en WinSCP

Después de configurar WebDAV, puede volver a la página **Share Folders** del almacenamiento en red.

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Haga clic con el botón derecho en el icono **"..."** y copie el enlace HTTPS.

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Abra WinSCP y seleccione WebDAV; seleccione también el cifrado TLS/SSL. Luego pegue el enlace en **Host name**; el número de puerto cambiará automáticamente a 6008.

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Introduzca su nombre de usuario y contraseña; luego haga clic en guardar e iniciar sesión. Se abrirá la carpeta compartida.

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
