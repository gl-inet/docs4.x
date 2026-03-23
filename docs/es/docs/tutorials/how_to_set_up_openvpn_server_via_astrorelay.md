# ¿Cómo configurar un servidor OpenVPN mediante AstroRelay?

Este tutorial presenta los pasos para configurar un servidor OpenVPN mediante AstroRelay en un router GL.iNet. Es ideal para quienes necesitan acceder de forma remota a servicios locales de su casa u oficina, pero no disponen de una dirección IP pública proporcionada por su ISP.

[AstroRelay](https://www.astrorelay.com){target="\_blank"} proporciona un túnel seguro de proxy inverso, mediante el cual puede acceder de forma segura a recursos situados detrás de NAT y firewalls.

1. Siga [esta guía](../interface_guide/openvpn_server.md) para configurar un servidor OpenVPN en su router GL.iNet, aunque no tenga una dirección IP pública.

   ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

   Después exporte la configuración de OpenVPN. A continuación se muestra un archivo de configuración de ejemplo.

   ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. (Opcional) Si necesita acceder de forma remota a la LAN del servidor VPN, habilite **Allow Remote Access LAN**. De lo contrario, omita este paso.

   ??? "Para firmware v4.7 y anteriores"
   1. En la barra lateral izquierda, haga clic en **VPN** > **VPN Dashboard**.
   2. Haga clic en el icono de opciones.
   3. Active el interruptor de **Remote Access LAN**.
   4. Haga clic en **Apply**.

      ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

   ??? "Para firmware v4.8 y posteriores"
   1. En la barra lateral izquierda, haga clic en **VPN** > **OpenVPN Server**.
   2. Haga clic en **Options** en la parte superior derecha.
   3. Active el interruptor de **Allow Remote Access the LAN Subnet**.
   4. Haga clic en **Apply**.

      ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3. Registre una cuenta en AstroRelay y siga este [tutorial](https://www.astrorelay.com/tutorial.html){target="\_blank"} para completar la configuración inicial.

   Al añadir un nuevo dominio, elija el servidor más cercano a su router.

   ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

   Al añadir un nuevo enlace, introduzca la **dirección IP LAN** de su router en el campo **Destination Host IP** e introduzca **1194** en el campo **Destination Port**.

   ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

   A continuación obtendrá un enlace, por ejemplo **testforx3000.arlab1.cc:37202**. Haga clic en él para copiarlo.

   ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4. Abra el archivo de configuración de OpenVPN y reemplace el valor que aparece después de **Remote** por el enlace obtenido en el paso anterior. En el ejemplo de abajo, "42.200.00.00 1194" se sustituye por "testforx3000.arlab1.cc:37202". Después sustituya los dos puntos ":" por un espacio y aplique el cambio.

   ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

   ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5. Instale la [aplicación OpenVPN Connect](https://openvpn.net/client/){target="\_blank"} en el dispositivo que quiera usar como cliente OpenVPN. Después cargue el archivo de configuración modificado en la aplicación e inicie la conexión. Como alternativa, también puede subirlo a otro router GL.iNet para configurarlo como cliente OpenVPN.

   Una vez conectado, podrá acceder de forma remota a sus servicios locales de casa u oficina.

   ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
