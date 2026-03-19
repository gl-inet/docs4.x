# Red de invitados

La configuración de la red de invitados se separó de [LAN](lan.md) a partir del firmware v4.5.

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Guest Network**.

Incluye la configuración básica de Guest Network y la configuración del servidor DHCP.

## Configuración básica

Puede configurar la subred dentro de estos rangos privados de direcciones IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

Puede crear una red separada y aislada para usuarios temporales, con acceso limitado y mayor seguridad al estar segregada de la red principal.

**Nota**: Algunos modelos, por ejemplo GL-MT5000 y GL-MT2500/GL-MT2500A, no admiten Wi-Fi, por lo que la configuración de Guest Network no está disponible en su panel de administración web.

- **Gateway**

  El **gateway predeterminado** de Guest Network es **192.168.9.1**. Si entra en conflicto con su red local, cámbielo por otro diferente.

- **Netmask**

  El valor predeterminado es **255.255.255.0**. También puede seleccionar **255.255.0.0** si necesita una subred más grande con más direcciones IP.

- **AP Isolation**

  Esta función está disponible desde el firmware v4.5.

  Permite aislar los dispositivos cliente en un segmento de red separado. Estos dispositivos no podrán comunicarse con otros dispositivos de la misma red.

- **Block WAN Subnets**

  Esta función está disponible desde el firmware v4.8.

  Cuando está habilitada, la red de invitados no puede acceder a la red upstream ni a su subred.

## Servidor DHCP

Si Guest Network está habilitada, el servidor DHCP se activará de forma predeterminada.

El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente conectado a Guest Network. Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Haga clic [aquí](../tutorials/manually_configure_static_ip.md) para aprender a configurar manualmente una IP estática.

Puede cambiar las direcciones IP inicial y final según sus necesidades. Por ejemplo, si la red se amplía o se reduce, si se producen conflictos de direcciones IP o si se modifica el rango de la máscara de subred.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Haga clic en **Advanced** si necesita una configuración adicional.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: El período durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway**: El dispositivo que enruta el tráfico entre la red de invitados y redes externas, como Internet.

- **DNS Server 1**: El servidor principal que traduce nombres de dominio en direcciones IP.

- **DNS Server 2**: El servidor secundario utilizado para la resolución de nombres de dominio si el servidor DNS principal no está disponible.

- **LPR Server**: (Line Printer Remote Server) Un servicio que gestiona trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

---

Artículos relacionados:

- [How to set up a guest Wi-Fi network on GL.iNet routers](../tutorials/how_to_set_up_a_guest_network.md)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
