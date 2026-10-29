# UPnP {#upnp}

**Nota**: Esta función se introdujo en el firmware v4.11.

---

En el lado izquierdo del panel de administración web, vaya a **SECURITY** -> **UPnP**.

UPnP (Universal Plug and Play) permite que los dispositivos LAN y aplicaciones compatibles soliciten automáticamente asignaciones de puertos en los routers GL.iNet. Estas asignaciones reenvían el tráfico WAN entrante a direcciones IP y puertos LAN específicos, permitiendo que clientes externos se conecten a servicios locales sin reglas de reenvío de puertos configuradas manualmente.

UPnP se diferencia del [reenvío de puertos](./port_forwarding.md) y de [DMZ](./port_forwarding.md#dmz): UPnP crea asignaciones automáticamente a petición de los dispositivos. El reenvío de puertos expone puertos seleccionados, mientras que DMZ expone todos los puertos de un equipo LAN; ambos requieren configuración manual. Antes de habilitar cualquiera de estas funciones, asegúrese de comprender su funcionamiento y los riesgos de seguridad asociados.

**Nota**: 

1. Cuando UPnP está habilitado, los dispositivos LAN y aplicaciones compatibles pueden solicitar asignaciones de puertos sin aprobación individual de cada solicitud.

2. Un dispositivo comprometido o una aplicación maliciosa puede usar UPnP para exponer servicios locales a Internet. Habilite UPnP solo en redes de confianza y deshabilítelo cuando no lo necesite.

3. UPnP requiere una IP pública en la interfaz WAN del router para aceptar conexiones entrantes desde Internet. No funcionará si su proveedor de Internet utiliza CGNAT.

Los usos habituales de UPnP incluyen:

- **Juegos en línea**: Los juegos y consolas compatibles (p. ej., juegos multijugador de Steam, Xbox Series X|S, PlayStation 5, Nintendo Switch) pueden crear asignaciones de puertos automáticamente para ayudar a establecer conexiones con otros jugadores.

- **Intercambio de archivos entre pares**: Los clientes BitTorrent y otras aplicaciones P2P compatibles pueden asignar automáticamente puertos de escucha para aceptar conexiones entrantes de otros pares.

- **Acceso remoto**: Los dispositivos y aplicaciones que admiten asignaciones de puertos UPnP, como determinados dispositivos NAS, cámaras IP y servidores multimedia, pueden configurar automáticamente asignaciones para acceder desde fuera de la red local.

## Configuración rápida {#quick-setup}

Active el interruptor para habilitar UPnP. Los dispositivos y aplicaciones compatibles podrán solicitar asignaciones de puertos según sea necesario, como se muestra en el ejemplo siguiente.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- **Client / Application**: Descripción del cliente o aplicación y dirección IP LAN del dispositivo solicitante.

- **Protocol**: Protocolo de transporte de la asignación, p. ej., `TCP` o `UDP`.

- **External Port**: Puerto WAN para las conexiones entrantes.

- **Internal Target**: Dirección IP LAN y puerto de destino.

- **Lease**: Tiempo restante antes de que caduque la asignación. La duración predeterminada de la concesión es de 7 días.

- **Action**: Haga clic en el icono de papelera para eliminar la asignación. El cliente o aplicación puede volver a solicitarla si sigue en ejecución.

Las asignaciones de puertos activas se eliminan cuando el cliente las libera o caducan sus concesiones. Haga clic en **Refresh** para ver las asignaciones de puertos más recientes.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contacte con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
