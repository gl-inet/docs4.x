# ¿Cómo configurar un servidor WireGuard mediante AstroRelay?

Este tutorial presenta los pasos para configurar un servidor WireGuard mediante AstroRelay en un router GL.iNet. Es ideal para quienes necesitan acceder de forma remota a servicios locales de su casa u oficina, pero no disponen de una dirección IP pública proporcionada por su ISP.

[AstroRelay](https://www.astrorelay.com){target="\_blank"} proporciona un túnel seguro de proxy inverso, mediante el cual puede acceder de forma segura a recursos situados detrás de NAT y firewalls.

1. Siga [esta guía](../interface_guide/wireguard_server.md) para configurar un servidor WireGuard en su router GL.iNet, aunque no tenga una dirección IP pública.

   ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

   Después haga clic en **Profiles** para exportar la configuración de WireGuard. A continuación se muestra un archivo de configuración de ejemplo.

   ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. (Opcional) Si necesita acceder de forma remota a la LAN del servidor VPN, habilite **Allow Remote Access LAN**. De lo contrario, omita este paso.

   ??? "Para firmware v4.7 y anteriores"

   En el panel de administración web del servidor, vaya a **VPN** -> **VPN Dashboard** -> sección **VPN Server**. Haga clic en el icono de engranaje situado a la derecha del servidor WireGuard.

   ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

   Active **Remote Access LAN** y haga clic en **Apply**.

   ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

   **Cuando esta opción está habilitada, se puede acceder de forma remota a este router y a los dispositivos de la LAN a través de la VPN.**

   ??? "Para firmware v4.8 y posteriores"

   En el panel de administración web del servidor, vaya a **VPN** -> **WireGuard Server**. Haga clic en **Options** en la esquina superior derecha.

   ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

   Active **Allow Remote Access the LAN Subnet** y haga clic en **Apply**.

   ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

   **Cuando esta opción está habilitada, se puede acceder de forma remota a este router y a los dispositivos de la LAN a través de la VPN.**

3. Registre una cuenta en AstroRelay y siga este [tutorial](https://www.astrorelay.com/tutorial.html){target="\_blank"} para completar la configuración inicial.

   Al añadir un nuevo dominio, elija el servidor más cercano a su router.

   ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

   Al añadir un nuevo enlace, introduzca la **dirección IP LAN** de su router en el campo **Destination Host IP** e introduzca **51820** en el campo **Destination Port**.

   ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

   A continuación obtendrá un enlace, por ejemplo **wg_server_test.arlab1.cc:33331**. Haga clic en él para copiarlo.

   ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4. Abra el archivo de configuración de WireGuard, reemplace el valor que aparece después de **Endpoint** por el enlace obtenido en el paso anterior y aplique el cambio.

   ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5. Instale la [aplicación WireGuard](https://www.wireguard.com/install/){target="\_blank"} en el dispositivo que quiera usar como cliente WireGuard. Después cargue el archivo de configuración modificado en la aplicación e inicie la conexión. Como alternativa, también puede subirlo a otro router GL.iNet para configurarlo como cliente WireGuard.

   Una vez conectado, podrá acceder de forma remota a sus servicios locales de casa u oficina.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
