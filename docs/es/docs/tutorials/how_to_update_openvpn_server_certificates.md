# ¿Cómo actualizar los certificados del servidor OpenVPN?

Este tutorial explica cómo actualizar los certificados del servidor OpenVPN en sus routers GL.iNet.

**Nota**: Este proceso requiere actualizar el certificado Root CA, lo que invalidará todos los certificados de cliente existentes, integrados en los archivos de configuración. Debe volver a exportar todos los archivos de configuración para que sus clientes OpenVPN puedan reconectarse al servidor.

1. Inicie sesión en el panel de administración web de su router y vaya a **VPN** -> **OpenVPN Server**.

   Si su servidor OpenVPN está en ejecución, detenga el servicio.

2. En la pestaña Configuration, haga clic en **Advanced Configuration** para desplegar la configuración.

   ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Busque **Server Root Certificate** y elimine todo el contenido del cuadro de texto.

   ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

   El correspondiente **Server Certificate** y **Server Key** también se eliminarán automáticamente, como se muestra a continuación.

   ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Deje los tres cuadros en blanco y haga clic en **Apply** en la parte inferior. Se generarán automáticamente nuevos certificados y se rellenarán los cuadros.

   ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. Los certificados del servidor OpenVPN ya están actualizados. Haga clic en **Export Client Configuration** en la parte inferior para exportar nuevos archivos de configuración para que sus dispositivos se conecten.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
