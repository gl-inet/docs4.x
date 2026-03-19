# Cómo usar WinSCP para modificar archivos en routers GL.iNet

WinSCP es una herramienta sencilla para editar, copiar y descargar archivos o directorios en el router. Puede copiar archivos entre un ordenador local y su router usando los protocolos de transferencia de archivos FTP, SCP, SFTP, WebDAV o S3. Se aplica al sistema operativo Windows.

---

1. Descargue WinSCP desde [aquí](https://winscp.net/eng/download.php){target="\_blank"} e instálelo en Windows.

2. Conéctese al router y luego ejecute WinSCP.

   ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}
   - File protocol: elija `SCP` como protocolo.
   - Host name: introduzca la IP del router. Si no cambió la IP de su router, debería ser `192.168.8.1`
   - Port number: `22`
   - Username & Password: introduzca `root` como nombre de usuario y escriba su contraseña.

   Luego haga clic en el botón `Login`.

3. Después de iniciar sesión, tendrá control total del router.

   Puede seleccionar, ver, editar o transferir archivos o directorios desde o hacia el router.

   ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

   Por ejemplo, si quiere editar la configuración del firewall, puede ir a /etc/config, buscar el archivo firewall, hacer clic con el botón derecho sobre él y luego elegir **Edit**.

   ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

   Ahora puede editar libremente el contenido del archivo. Tenga cuidado de no alterar la configuración por error.

   ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
