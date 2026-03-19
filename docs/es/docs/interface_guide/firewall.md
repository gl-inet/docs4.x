# Firewall

Esta guía se aplica al firmware v4.5 y anteriores.

Desde la versión v4.6, la página Firewall se ha dividido. Las funciones Port Forwarding y DMZ se trasladaron a [Port Forwarding](port_forwarding.md). La función Open Ports se trasladó a [Security](security.md).

---

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Firewall**.

La página Firewall le permite configurar reglas como **Port Forwarding**, **Open Ports on Router** y **DMZ**.

## Reenvío de puertos

Port Forwarding permite que equipos remotos se conecten a un ordenador local o a un servidor situado detrás del firewall del router en la LAN, por ejemplo servidores web o FTP.

Para configurar el reenvío de puertos, haga clic en la pestaña **Port Forwards** y luego en **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

En la ventana emergente, agregue una nueva regla de reenvío de puertos y haga clic en **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** El nombre de la regla.

**Protocol:** El protocolo utilizado. Puede elegir TCP, UDP o ambos, TCP y UDP.

**External Zone:** Las opciones de zona externa son `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** Los números de puerto externos. Puede introducir aquí un número de puerto específico.

**Internal Zone:** Las opciones de zona interna son `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** La dirección IP asignada por el router al dispositivo al que se necesita acceder de forma remota.

**Internal Port:** El número de puerto interno del dispositivo. Puede introducir un número de puerto específico. Déjelo en blanco si es el mismo que el puerto externo.

**Enable:** Habilita o deshabilita la regla.

## Abrir puertos en el router

Los servicios del router, como web y FTP, requieren que sus puertos correspondientes estén abiertos en el router para ser accesibles públicamente.

Para abrir un puerto, cambie a la pestaña **Open Ports on Router** y haga clic en **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

En la ventana emergente, abra un nuevo puerto y haga clic en **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** El nombre de la regla, que puede ser definido por el usuario.

**Protocol:** El protocolo utilizado. Puede elegir TCP, UDP o ambos, TCP y UDP.

**Port:** El número de puerto que desea abrir.

**Enable:** Habilita o deshabilita la regla.

## DMZ

DMZ le permite exponer un equipo a Internet, por lo que todos los paquetes entrantes se redirigirán a ese ordenador.

Active **Enable DMZ**. Seleccione la dirección IP interna del dispositivo host que va a recibir todos los paquetes entrantes.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
