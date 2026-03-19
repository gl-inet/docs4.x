# ¿Cómo reservar una IP fija para un cliente OpenVPN en una conexión OpenVPN autoconstruida?

Este tutorial le mostrará cómo reservar una IP fija para su cliente OpenVPN que se conecta a su servidor. Antes de seguir los pasos siguientes, configure primero un router GL.iNet como servidor OpenVPN.

1. Inicie sesión en el panel de administración web de su servidor OpenVPN y, en la barra lateral izquierda, vaya a **VPN** -> **OpenVPN Server**.

   En la pestaña **Configuration**, anota la **subred IPv4** como referencia, por ejemplo `10.8.0.0/24`, como se muestra en la siguiente imagen, y cambia el Authentication Mode a **Username and Password Only**.

   ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Vaya a la pestaña **Users** y cree un nombre de usuario y una contraseña, como se muestra a continuación.

   ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Inicie sesión en el router por SSH y ejecute el siguiente comando para abrir el archivo de script de configuración del servidor OpenVPN:

   `vi /lib/netifd/proto/openserver.sh`

   En el archivo abierto, comprueba si existe en el script la línea `client-config-dir /etc/openvpn/ccd`.

   ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

   Si no existe, añádela manualmente y luego guarda el archivo y sal.

4. Vaya a `/etc/openvpn/` y cree una carpeta `ccd` con `mkdir ccd`.

   ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Añade un archivo llamado `GLsupport`, escribe `ifconfig-push 10.8.0.10 255.255.255.0` y luego guarda el archivo y sal.

   Verifica el contenido con `cat GLsupport`

   ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}
   - Cuando use `GLsupport` para conectarse a su servidor OpenVPN, se asignará la IP fija `10.8.0.10` a ese usuario `GLsupport`.

   - `255.255.255.0` es la máscara de subred y puede sustituirla por la máscara de subred de su servidor OpenVPN.

   **Nota**: Si quiere fijar direcciones IP para varios clientes OpenVPN, cree varios nombres de usuario y contraseñas en el paso 2 y, a continuación, repita el paso 5. Añada archivos a la carpeta `ccd` según el orden de los usuarios, por ejemplo `user_1`, `user_2`, `user_3`, seguidos del comando `ifconfig-push` y de su correspondiente IP fija y máscara de subred.

   Por ejemplo: `ifconfig-push 10.8.0.20 225.225.225.0`, `ifconfig-push 10.8.0.30 225.225.225.0`, `ifconfig-push 10.8.0.40 225.225.225.0`

6. Por último, realice una prueba con su cliente OVPN y compruebe si la **Client Virtual IP (IPv4)** es la reservada.

   Por ejemplo, si su cliente OpenVPN es un router GL.iNet, puede iniciar sesión en el panel de administración web del router cliente OpenVPN y entrar en **VPN Dashboard** para verificar la **Client Virtual IP (IPv4)**.

   ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
   <small>(VPN Dashboard en firmware v4.7 y anteriores)</small>

   ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
   <small>(VPN Dashboard en firmware v4.8)</small>

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
