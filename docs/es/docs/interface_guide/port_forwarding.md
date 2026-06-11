# Reenvío de puertos

> Esta guía se aplica al firmware v4.6 y versiones posteriores. Para versiones anteriores, consulte [Firewall](firewall.md).

En el lado izquierdo del Panel de administración web, vaya a **NETWORK** -> **Port Forwarding**, o a **SECURITY** -> **Port Forwarding** (para firmware v4.9 y versiones posteriores).

Esta página le permite configurar reglas de firewall, incluidas **DMZ** y **Port Forwarding**.

Nota: Para abrir puertos del router, vaya a SYSTEM -> [Security](security.md), o a SECURITY -> [Admin Access](admin_access.md) (para firmware v4.9 y versiones posteriores).

## DMZ

La DMZ le permite exponer un equipo a Internet, por lo que todos los paquetes entrantes se redirigirán a ese equipo.

Active **Enable DMZ**. Seleccione la dirección IP interna del dispositivo host que va a recibir todos los paquetes entrantes.

Puede establecer la prioridad de la DMZ. Si la prioridad de la DMZ es superior a la de las reglas de reenvío de puertos, todas las reglas de reenvío de puertos quedarán invalidadas. En caso contrario, las solicitudes solo se reenviarán al dispositivo DMZ Host si el puerto al que se accede no tiene una regla de reenvío de puertos correspondiente.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding

El reenvío de puertos permite que equipos remotos se conecten a un equipo local o a un servidor situado detrás del firewall del router en la LAN, como servidores web, servidores FTP, etc.

Para configurar el reenvío de puertos, haga clic en **Add** en la sección Port Forwarding.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

En la ventana emergente, añada una nueva regla de reenvío de puertos y haga clic en **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

- **Protocol:** Elija `TCP`, `UDP` o `TCP and UDP` para esta regla.

- **External Zone:** Las opciones de la zona externa son `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN` y `Guest`.

- **External Port:** Los números de los puertos externos. Puede introducir aquí un número de puerto concreto. El rango de puertos va de 1 a 65535. Puede configurar un único puerto o un rango uniendo el primero y el último con el símbolo `-`, por ejemplo `501-510`.

- **Internal Zone:** Las opciones de la zona interna son `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server` y `WAN`.

- **Internal IP:** La dirección IP que el router asigna al dispositivo al que se necesita acceder de forma remota. Si configura un único puerto en **External Port**, debe configurar aquí ese único puerto. Si configura un rango de puertos en **External Port**, debe configurar aquí el rango de puertos correspondiente.

- **Internal Port:** El número de puerto interno del dispositivo. Puede introducir un número de puerto concreto. Déjelo en blanco si es el mismo que el puerto externo.

- **Description:** Defina un nombre personalizado o añada una descripción para esta regla (opcional).

- **Enable:** Activa o desactiva esta regla.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
