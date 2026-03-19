# Cómo cambiar el tipo de NAT para juegos

La mayoría de los desarrolladores de juegos le pedirán que active UPnP en el router para obtener un mejor tipo de NAT; sin embargo, diversos estudios muestran que UPnP es un protocolo poco seguro.
Puede lograr el mismo objetivo de una forma más segura, ya sea mediante la función DMZ o mediante el reenvío de puertos.

## Compruebe la IP de su dispositivo de juego

Vaya a la lista de clientes y compruebe la IP asignada a su dispositivo de juego. Necesitará usar esa dirección IP en la configuración que se indica a continuación.
![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Método 1: DMZ

Vaya en la barra lateral a **Network > Port Forwarding** y habilite DMZ con la IP de su dispositivo de juego.
![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Método 2: Reenvío de puertos

Vaya en la barra lateral a **Network > Port Forwarding** y añada los puertos necesarios con la IP de su dispositivo de juego.
![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Ejemplo: puertos para PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Puertos para Xbox

UDP 88, 3074

TCP 3074

Es posible que algunos juegos necesiten que se reenvíen otros puertos. Puede consultar este sitio web para obtener más detalles.
[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT

Puede habilitar **Full Cone NAT** en **Network > NAT Settings** para mejorar la latencia.
![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}
* Esta función está disponible en el firmware 4.5 o superior.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
