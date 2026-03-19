# ¿Cómo configurar un servidor OpenVPN mediante AstroRelay?

Escenario: quiere configurar un servidor OpenVPN en un router GL.iNet en casa o en la oficina para acceder de forma remota a su servicio local, pero su ISP no le proporciona una dirección IP pública.

[AstroRelay](https://www.astrorelay.com){target="\_blank"} proporciona un túnel seguro de proxy inverso, mediante el cual puede acceder de forma segura a recursos situados detrás de NAT y firewalls.

1. Siga la guía [aquí](../interface_guide/openvpn_server.md) para configurar un servidor OpenVPN incluso si no tiene una dirección IP pública. Active **Allow Access Local Network**.

   ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

   Luego exporte una configuración de OpenVPN. La imagen de abajo muestra un ejemplo.

   ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. Registre una cuenta en AstroRelay y siga este [tutorial](https://www.astrorelay.com/tutorial.html){target="\_blank"} para completar la configuración inicial.

   Al añadir un nuevo dominio, elija el servidor más cercano a su router.

   ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

   Al añadir un nuevo enlace, introduzca la **dirección IP LAN** de su router en el cuadro **Destination Host IP**. Introduzca **1194** en el cuadro **Destination Port**.

   ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

   Después obtendrá un enlace, por ejemplo **testforx3000.arlab1.cc:37202**. Haga clic en él para copiarlo.

   ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

3. Abra la configuración de OpenVPN y reemplace los datos después de **Remote** por el enlace que obtuvo en el paso anterior. En el ejemplo de abajo, sustituimos "42.200.00.00 1194" por el enlace "testforx3000.arlab1.cc:37202".

   Luego sustituya los dos puntos ":" por un espacio, por ejemplo: "testforx3000.arlab1.cc 37202".

   ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

   ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

   Después podrá usar el archivo de configuración modificado en la aplicación cliente de OpenVPN.

4. Cuando no esté en casa o en la oficina, puede cargar el archivo de configuración modificado en la aplicación cliente de OpenVPN para acceder a su servicio local de casa u oficina como si estuviera allí.

   ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
