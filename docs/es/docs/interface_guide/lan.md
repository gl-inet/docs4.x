# LAN

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **LAN**.

La LAN es la red a la que está conectado su dispositivo cuando se conecta mediante la Wi-Fi principal o mediante un cable Ethernet.

Incluye ajustes básicos, ajustes del servidor DHCP y reserva de direcciones.

## Ajustes básicos

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

  Esta es la dirección que introduciría en la barra de direcciones del navegador para acceder a la página de administración del router.

  De forma predeterminada es **192.168.8.1**. Puede cambiarla si entra en conflicto con su red.

- **Netmask**

  El valor predeterminado es **255.255.255.0**. También puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **AP Isolation**

  Puede aislar los dispositivos cliente en un segmento de red independiente. Estos dispositivos no podrán comunicarse con otros dispositivos de la misma red.

## Servidor DHCP

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, tendrá que configurar manualmente los ajustes de red de los dispositivos cliente. Haga clic [aquí](../tutorials/manually_configure_static_ip.md) para aprender a configurar manualmente una IP estática.

Puede cambiar las direcciones IP inicial y final según sus necesidades, por ejemplo, si su red se amplía o se reduce, si se producen conflictos de direcciones IP o si se modifica el rango de la máscara de subred.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Haga clic en **Advanced** para una configuración adicional si es necesario.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: El periodo durante el cual una dirección IP asignada por DHCP sigue siendo válida para un dispositivo.

- **Gateway**: El dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1**: El servidor principal que traduce nombres de dominio en direcciones IP.

- **DNS Server 2**: El servidor secundario utilizado para la resolución de nombres de dominio si el servidor DNS principal no está disponible.

- **LPR Server**: (Line Printer Remote Server) Un servicio que gestiona trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

## Reserva de direcciones

Cuando especifica una dirección IP reservada para un cliente dentro de la LAN, el cliente siempre recibe la misma dirección IP cada vez que accede al servidor DHCP del router. Puede asignar direcciones IP reservadas a ordenadores o servidores que requieran ajustes IP permanentes.

**Nota:** Los clientes configurados tienen que volver a conectarse al router para activarse.

Haga clic en **Add** para reservar una IP.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

Verá una ventana emergente.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Seleccione la **MAC** en la lista desplegable y la **IP** correspondiente a la MAC seleccionada se rellenará automáticamente. Asigne un nombre descriptivo y, a continuación, haga clic en **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

Después de añadir una nueva reserva de dirección IP, verá la página como se muestra a continuación, lo que significa que la configuración se ha realizado correctamente.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
