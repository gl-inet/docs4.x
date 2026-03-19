# ¿Cómo configurar un servidor WireGuard mediante AstroRelay?

Escenario: quiere configurar un servidor WireGuard en un router GL.iNet en casa o en la oficina para acceder de forma remota a su servicio local, pero su ISP no le proporciona una dirección IP pública.

[AstroRelay](https://www.astrorelay.com){target="\_blank"} proporciona un túnel seguro de proxy inverso, mediante el cual puede acceder de forma segura a recursos situados detrás de NAT y firewalls.

1. Siga la guía [aquí](../interface_guide/wireguard_server.md) para configurar un servidor WireGuard incluso si no tiene una dirección IP pública. Active **Allow Access Local Network**.

   ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

   Luego exporte una configuración de WireGuard. La imagen de abajo muestra un ejemplo.

   ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. Registre una cuenta en AstroRelay y siga este [tutorial](https://www.astrorelay.com/tutorial.html){target="\_blank"} para completar la configuración inicial.

   Al añadir un nuevo dominio, elija el servidor más cercano a su router.

   ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

   Al añadir un nuevo enlace, introduzca la **dirección IP LAN** de su router en el cuadro **Destination Host IP**. Introduzca **51820** en el cuadro **Destination Port**.

   ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

   Después obtendrá un enlace, por ejemplo **wg_server_test.arlab1.cc:33331**. Haga clic en él para copiarlo.

   ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

3. Abra la configuración de WireGuard y reemplace los datos después de **Endpoint** por el enlace que obtuvo en el paso anterior. Después podrá usar la configuración modificada en la aplicación cliente de WireGuard.

   ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

4. Cuando no esté en casa o en la oficina, puede cargar el archivo de configuración modificado en la aplicación cliente de WireGuard para acceder a su servicio local de casa u oficina como si estuviera allí.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
