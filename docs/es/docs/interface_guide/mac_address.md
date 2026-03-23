# Dirección MAC

Esta guía se aplica al firmware v4.5 y anteriores.

La página **MAC Address** se llamaba anteriormente **MAC Clone** y pasó a llamarse **MAC Address** desde la versión v4.2.

Desde la versión v4.6, la configuración de dirección MAC para las interfaces Ethernet y Repeater se ha trasladado respectivamente a las páginas [Ethernet Port](ethernet_port.md) y [Repeater](internet_repeater.md).

---

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **MAC Address**.

En esta página, puede encontrar la dirección MAC predeterminada del router, clonar la dirección MAC de un cliente, introducir una dirección MAC manualmente o generar una dirección MAC aleatoria.

Si el dispositivo admite configurar varios puertos Ethernet para usarlos como puertos WAN, puede establecer la dirección MAC de cada puerto por separado. Tenga en cuenta que la configuración de la dirección MAC solo es válida cuando el puerto Ethernet se usa como puerto WAN.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

- La dirección MAC predeterminada de fábrica.

  ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

- Clonar la dirección MAC de un cliente.

  ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

  **Nota:** Muchos dispositivos nuevos usan ahora una dirección MAC aleatoria distinta para conectarse a diferentes redes Wi-Fi, por lo que la dirección MAC mostrada aquí puede no ser la dirección MAC real del dispositivo del usuario. La MAC aleatoria también puede denominarse Private Wi-Fi Address o random hardware address en diferentes dispositivos.

- Introducir manualmente o generar una dirección MAC aleatoria.

  ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Escenarios de uso

Cuando se conecte a un hotspot público, use una dirección MAC aleatoria si no desea que el hotspot conozca su dirección MAC real o limite su acceso a Internet en función de ella. Lea esta guía: [Connect to a Hotspot with a Captive Portal](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
