# Cómo conectarse a la IP dedicada de NordVPN en routers GL.iNet

Este artículo presenta los pasos para configurar la IP dedicada de NordVPN.

Aquí usamos GL-AXT1800 como ejemplo.

1. Inicie sesión en su cuenta de Nord y consulte la información de la IP dedicada. Como se muestra en la siguiente imagen, la IP asignada es **193.32.211.142** y la información del servidor es **United Kingdom #1625**.
    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}
2. Vaya a este enlace: [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) y busque el archivo de configuración de **United Kingdom #1625**. Descargue el archivo de configuración UDP o TCP según prefiera.
    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}
3. Vuelva a la página de la cuenta de Nord, vaya a Manual setup y haga clic en **Set up NordVPN Manually** para obtener las credenciales del servicio.
    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}
    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}
4. Inicie sesión en el panel de administración web de su router, vaya a **VPN** > **OpenVPN Client**, cree un grupo nuevo y cargue el archivo de configuración descargado en el paso 2. Luego introduzca las credenciales del servicio que obtuvo en el paso 3.
    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}
5. Vaya a **VPN Dashboard**, seleccione el archivo de configuración y haga clic en **Apply** para conectarse.
    ![connect nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/connect_nordvpn_on_glinet_router.png){class="glboxshadow"}
6. Cuando esté conectado, puede comprobar su IP pública aquí: [https://whatismyipaddress.com/](https://whatismyipaddress.com/) y confirmar si coincide con la IP dedicada de NordVPN.
    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
