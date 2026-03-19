# Conectarse a Internet mediante un cable Ethernet

Conecte el router a una red de banda ancha mediante un cable Ethernet conectado al puerto WAN. Normalmente obtiene una dirección IP automáticamente mediante DHCP. Los usuarios también pueden configurar manualmente una IP estática o PPPoE. Este método ofrece gran estabilidad y alta velocidad, por lo que es ideal para entornos domésticos y de oficina con acceso fijo de banda ancha.

Siga los pasos siguientes para conectar su router a Internet mediante un cable Ethernet.

1. Conecte el puerto WAN del router al dispositivo ascendente, por ejemplo un módem del ISP, un router, un switch de red o una toma Ethernet, mediante un cable Ethernet.

2. Inicie sesión en el panel web de administración del router y vaya a la sección **INTERNET** -> **Ethernet**.

   Si la conexión se realiza correctamente, la sección **Ethernet** mostrará los detalles de la red, incluidos **Protocol**, **IP Address**, **Gateway** y **DNS Server**.

   ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Consejo**: Antes de conectar el cable Ethernet al puerto WAN del router, puede hacer clic en **Change to LAN** para [configurar el puerto WAN como puerto LAN](../faq/change_wan_to_lan.md). Esto resulta útil cuando utiliza el router como [repetidor](internet_repeater.md), ya que el puerto WAN físico queda libre. De este modo, puede reutilizar el puerto WAN no utilizado como puerto LAN y disponer de un puerto LAN adicional.

## Protocolo

Hay 3 tipos de protocolo: DHCP, Static y PPPoE. Haga clic en **Modify** para cambiarlo.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

- DHCP

  DHCP es el protocolo predeterminado y el más habitual. Asigna automáticamente direcciones IP y otros parámetros de comunicación a los dispositivos de red mediante una arquitectura cliente-servidor en redes IP.

  ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

- Static

  Static es necesario si su ISP proporciona una dirección IP fija, o si desea configurar manualmente la información de red, como la dirección IP, el Gateway y la Netmask.

  ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

- PPPoE

  PPPoE es un protocolo utilizado por la mayoría de los ISP. Normalmente proporcionan un módem y un nombre de usuario con contraseña, que son necesarios para configurar Internet.

  ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Configuración avanzada

Además de los ajustes esenciales, también hay algunos ajustes avanzados opcionales para los tres protocolos anteriores.

- **VLAN ID**: Este ajuste solo es necesario si el servidor del proveedor requiere que la interfaz use un VLAN ID etiquetado específico.

- **TTL**: TTL (Time To Live) define el tiempo máximo que los paquetes pueden permanecer en la red. De forma predeterminada, el router reduce en 1 el TTL de los paquetes entrantes desde los dispositivos cliente antes de reenviarlos. Si necesita sobrescribirlo, puede establecer aquí un valor fijo. La configuración de TTL solo es válida para IPv4.

- **HL**: En IPv6, el campo HL (Hop Limit) limita el número de saltos de transmisión de los paquetes de datos en la red y equivale al TTL en IPv4.

- **MTU**: El valor MTU predeterminado es de 1500 bytes.

## Puerto Ethernet

Haga clic en el icono de engranaje de la esquina superior derecha para acceder a [Ethernet Port](ethernet_port.md).

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

La página **WAN** muestra la función del puerto, es decir, si se usa como WAN o LAN, el modo MAC, la dirección MAC y la velocidad negociada del puerto de red.

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

La página **LAN** muestra la función del puerto y la velocidad negociada del puerto de red.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

Consulte este [enlace](ethernet_port.md) para más detalles.

## Solución de problemas

Si hay un cable Ethernet conectado al puerto WAN pero no hay acceso a Internet, se mostrará un mensaje amarillo como el siguiente.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Para solucionar este problema:

1. Compruebe si el dispositivo ascendente tiene acceso a Internet.

2. Vaya a la página [Multi-WAN](multi-wan.md) para comprobar el estado de la interfaz Ethernet.

---

Artículos relacionados

- [Página de Internet](internet.md)
- [¿Cómo establecer la prioridad de cada método de acceso a Internet?](multi-wan.md)
- [¿Cómo configurar el equilibrio de carga cuando se utilizan varios métodos de acceso a Internet al mismo tiempo?](multi-wan.md)

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
