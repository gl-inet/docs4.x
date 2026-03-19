# ¿Cómo enrutar las consultas DNS del cliente VPN al DNS ascendente del servidor VPN?

Este tutorial presenta los pasos para redirigir todas las consultas DNS de los clientes VPN a su servidor DNS autoalojado en el lado LAN de su router principal, aguas arriba del servidor VPN.

## Topología

En este tutorial, usamos **Flint 3 (GL-BE9300)** y **Slate 7 (GL-BE3600)** como ejemplos.

Flint 3 es el servidor VPN, que tiene un router principal en su red ascendente, y Slate 7 es el cliente VPN que se conecta a Flint 3.

Cuando se establece un túnel VPN entre el servidor VPN y el cliente, de forma predeterminada las consultas DNS del cliente VPN se envían primero al servidor VPN, luego se reenvían al router principal y, por último, son resueltas por los servidores DNS asignados por el ISP configurados en la WAN del router principal.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Sin embargo, si ha desplegado un servidor DNS autoalojado con dirección IP `192.168.1.13` en el router principal, se requieren configuraciones adicionales para enrutar las consultas DNS a ese servidor DNS autoalojado.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Configuración

1. Inicie sesión en el panel de administración web del Flint 3 y vaya a **NETWORK** -> **DNS**. Cambie el DNS Server Mode a **Manual DNS** e introduzca la dirección IP de su servidor DNS.

   ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Ve a **VPN** -> **WireGuard Server** -> pestaña **Configuration** y anota la dirección IPv4, que normalmente es `10.0.0.1/24` o `10.1.0.1/24`, según el modelo y la versión del firmware.

   ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Cambia a la pestaña **Profiles**, añade una configuración de cliente y exporta un perfil para Slate 7.

   ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Abre el perfil y asegúrate de que el DNS sea la dirección IP del servidor VPN que obtuviste en el paso 2.

   Para evitar fallos de resolución DNS, elimina `64.6.64.6` si aparece y guarda los cambios.

   ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. En el panel de administración web del Flint 3, haga clic en el botón **Start** en la parte superior de la página **WireGuard Server** para ejecutar el servidor.

   ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Inicie sesión en el panel de administración web del Slate 7 y vaya a **VPN** -> **WireGuard Client**.

   Haga clic en **Add Manually** y cargue el perfil editado.

   ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Haga clic en el icono de tres puntos para iniciar la conexión VPN. Si el indicador de estado se pone en verde, significa que la conexión VPN se ha establecido correctamente.

   ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Verificar la resolución DNS

Ejecute el siguiente comando para capturar el tráfico DNS en el cliente VPN. Mostrará que todo el tráfico DNS del cliente VPN va al servidor VPN, es decir, `10.0.0.1` en este ejemplo.

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Ejecute el siguiente comando para capturar el tráfico DNS en el servidor VPN. Mostrará que todo el tráfico DNS del cliente VPN termina yendo al servidor DNS autoalojado, es decir, `192.168.1.13` en este ejemplo.

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
