# ¿Cómo puedo encontrar todas las direcciones MAC de mi dispositivo?

## Escenario de uso

Las direcciones MAC de un dispositivo GL.iNet son únicas para cada interfaz de red, como WAN 1, WAN 2, puertos LAN, Wi-Fi de 2.4G y Wi-Fi de 5G.

Cuando se conecta en algunos hoteles, zonas de acampada o campus, el administrador de red puede pedirle la dirección MAC de su dispositivo para registrarla en la lista blanca antes de obtener acceso a Internet.

Puede consultar la dirección o direcciones MAC exactas de su dispositivo mediante los siguientes métodos.

## Método 1. Mediante la etiqueta del producto, solo para la MAC WAN

Busque la **dirección MAC WAN** en la etiqueta inferior.

Por ejemplo, la MAC WAN es E4:95:6E:40:DB:A9 en la imagen siguiente.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

## Método 2. Mediante SSH

Consulte [aquí](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) cómo usar SSH.

Introduzca **ifconfig** en SSH y obtendrá una salida de datos que mostrará interfaces como br-lan, ethx, wlanx, etc., en secuencia.

### Encontrar la MAC de los puertos Ethernet

Tome como ejemplo la siguiente imagen.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwan.jpg){class="glboxshadow"}

- **eth0** es el puerto WAN, con la dirección MAC **94:83:C4:19:19:08**.

  Si hay un puerto WAN adicional, por ejemplo, GL-MT6000, habrá una dirección MAC WAN más.

- **eth1**, **eth2**, etc., son los puertos LAN, con la dirección MAC **94:83:C4:19:19:09**.

  Solo habrá una dirección MAC aunque exista más de un puerto LAN.

### Encontrar la MAC de los puertos inalámbricos

Tome como ejemplo la siguiente imagen.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** es el Wi-Fi de 2.4G, con la dirección MAC **96:83:C4:19:19:0B**.

- **wlan1** es el Wi-Fi de 5G, con la dirección MAC **94:83:C4:19:19:0A**.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
