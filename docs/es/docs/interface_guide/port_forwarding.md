# Reenvío de puertos

Esta página está disponible desde el firmware v4.6. Para versiones anteriores, consulte [Firewall](firewall.md).

---

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Port Forwarding**.

Esta página le permite configurar reglas de firewall como **DMZ** y **Port Forwarding**.

Para la configuración de **Open Ports on Router**, vaya a **SYSTEM** -> **Security**.

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

**Protocol:** El protocolo utilizado. Puede elegir TCP, UDP o ambos, TCP y UDP.

**External Zone:** Las opciones de zona externa son `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN`, `Guest`.

**External Port:** Los números de los puertos externos. Puede introducir aquí un número de puerto concreto. El rango de puertos va de 1 a 65535. Puede establecer un único puerto o un rango uniendo el primer y el último puerto con el símbolo `-`, por ejemplo `501-510`.

**Internal Zone:** Las opciones de zona interna son `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `WAN`.

**Internal IP:** La dirección IP que el router asigna al dispositivo al que se necesita acceder de forma remota.

**Internal Port:** El número de puerto interno del dispositivo. Puede introducir un número de puerto concreto. Déjelo en blanco si es el mismo que el puerto externo.

**Description:** Establezca un nombre o añada una descripción para la regla de reenvío de puertos, de forma opcional.

**Enable:** Habilita o deshabilita la regla.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
