# Use WireGuard para proteger RDP desde una red externa

Es posible que necesite acceder de forma remota a su PC desde una red externa, o viceversa. La forma más segura es hacerlo mediante su propio túnel WireGuard. Esto ofrece más seguridad que usar redirección de puertos y acceder a través de su dirección IP pública. Después de configurar el túnel, puede usar la **Remote Desktop App** de Windows para acceder a su PC desde cualquier lugar.

## Topología

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Configure su propia red WireGuard

Debe configurar su propio servidor WireGuard y cliente WireGuard antes de poder usar el túnel WireGuard para RDP. Puede configurar el túnel con dos routers GL.iNet. Consulte [Construya su propio servidor doméstico WireGuard con dos routers GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Permita que el servidor acceda al lado LAN del cliente

Si quiere acceso mutuo entre el servidor y el cliente, primero debe permitir que su servidor acceda al lado LAN del cliente. Consulte [Acceso a la LAN del cliente desde el servidor](wireguard_server_access_to_client_lan_side.md).

## Permita que el cliente acceda al lado LAN del servidor

Después de eso, active “Allow Remote LAN Access” en ambos paneles VPN, tanto del servidor como del cliente. Para más detalles, en el lado del cliente haga clic [aquí](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options); en el lado del servidor haga clic [aquí](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Configure el PC del lado del servidor para que sea accesible

### PC del lado del servidor

Si quiere acceder al PC conectado al lado LAN de su servidor con la IP **192.168.29.123**, vaya a la configuración de Windows de ese PC y haga clic en **Remote Desktop**.

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Actívelo.

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Haga clic en **Confirm**.

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Inicie la aplicación remota en el portátil cliente

### Portátil del lado del cliente

Busque la **Remote Desktop Connection App**.

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Ábrala e introduzca en el cuadro la IP del PC del lado del servidor, **192.168.29.123**.

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Introduzca las credenciales del PC del lado del servidor.

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

Podrá controlar de inmediato el PC del lado del servidor de forma remota.

Si quiere hacerlo a la inversa, simplemente invierta los pasos entre el PC del servidor y el portátil del cliente.
