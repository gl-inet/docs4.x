# Cómo conectarse a Surfshark con una IP dedicada en routers GL.iNet

Este artículo presenta los pasos para configurar una conexión de Surfshark con una IP dedicada en routers GL.iNet.

Usamos el GL-AXT1800 como ejemplo.

1. Inicie sesión en su cuenta de Surfshark y luego seleccione **Dedicated IP**.

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){calss="glboxshadow"}

2. En la sección Dedicated IP, haga clic en **Settings**.

    ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){calss="glboxshadow"}

3. Seleccione un protocolo (WireGuard u OpenVPN) y descargue los archivos de configuración para la conexión manual.

    ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){calss="glboxshadow"}

    Para la configuración de WireGuard, la página de descarga muestra la IP del servidor y la clave pública del servidor, como se muestra a continuación.

    ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){calss="glboxshadow"}

    Para la configuración de OpenVPN, la página de descarga muestra la IP del servidor y las credenciales (nombre de usuario y contraseña), como se muestra a continuación. Copie las credenciales para usarlas más adelante.

    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){calss="glboxshadow"}

4. Consulte los enlaces siguientes para cargar los archivos de configuración en su router GL.iNet. Introduzca las credenciales si es necesario.

    - [Subir configuración de WireGuard](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [Subir configuración de OpenVPN](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.