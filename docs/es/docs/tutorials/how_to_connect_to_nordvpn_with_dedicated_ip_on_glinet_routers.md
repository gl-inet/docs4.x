# Cómo conectarse a NordVPN con una IP dedicada en routers GL.iNet

Este artículo presenta los pasos para configurar una conexión de NordVPN con una IP dedicada en routers GL.iNet.

Usamos el GL-AXT1800 como ejemplo.

1. Inicie sesión en su cuenta de Nord y revise los detalles de la IP dedicada. Como se muestra a continuación, la IP asignada es **193.32.211.142** y el servidor es **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Vaya a [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) y busque el archivo de configuración de **United Kingdom #1625**. Descargue el archivo de configuración UDP o TCP.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Vuelva a la página de su cuenta de Nord, vaya a **Manual Setup** y haga clic en **Set up NordVPN Manually** para obtener sus credenciales del servicio.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Inicie sesión en el panel de administración web de su router y vaya a **VPN** > **OpenVPN Client**. Cree un nuevo grupo para cargar el archivo de configuración descargado en el paso 2. Luego introduzca las credenciales del servicio obtenidas en el paso 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    Se ha detectado 1 archivo de configuración válido. Introduzca su nombre de usuario y contraseña. Si estas configuraciones usan contraseñas distintas, tendrá que introducir la contraseña correspondiente para cada archivo de configuración.

5. Haga clic en el icono de los tres puntos a la derecha para conectarse. También puede ir a **VPN Dashboard**, seleccionar el archivo de configuración y hacer clic en **Apply** para establecer la conexión.

6. Una vez conectado, compruebe su IP pública [aquí](https://whatismyipaddress.com/) y confirme que coincide con su IP dedicada de NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.