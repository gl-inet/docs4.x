# LAN {#lan}

**Nota**. Esta página se aplica al firmware v4.11 y versiones posteriores. Si su dispositivo utiliza otra versión del firmware, seleccione la guía correspondiente en la lista siguiente.

<div class="gl-link-select" data-label="Versión del firmware" data-placeholder="Firmware v4.11 y posteriores" markdown="1">

- [Firmware v4.9 y anteriores](lan.md)

</div>

---

En el menú de la izquierda del panel web de administración, vaya a **NETWORK** -> **LAN**.

En esta página puede configurar y administrar la red principal (**Main Network**), la red de invitados (**Guest Network**), la red IoT (**IoT Network**) y las redes VLAN personalizadas (**VLAN Networks**). Puede crear y administrar varias subredes para aislar distintos tipos de dispositivos o de tráfico.

## Red principal {#main-network}

Su dispositivo se conecta a la red principal mediante la red Wi-Fi principal o un cable Ethernet.

En la red principal puede consultar el estado de todas las interfaces, el ID de VLAN, la dirección IP del router y el rango DHCP.

![Red principal 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para configurar la red principal.

![Red principal 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

La página de configuración incluye los ajustes básicos, los ajustes del servidor DHCP y la reserva de direcciones.

### Ajustes básicos {#basic-settings}

Puede configurar la subred dentro de los rangos de direcciones IPv4 privadas `192.168.0.0/16`, `172.16.0.0/12` y `10.0.0.0/8`.

![Ajustes básicos de la red principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Introduzca esta dirección en la barra de direcciones del navegador para acceder a la página de administración del router.

    La dirección predeterminada es **192.168.8.1**. Puede cambiarla si entra en conflicto con su red.

- **Netmask**

    La máscara de subred predeterminada es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred con más direcciones IP.

- **VLAN ID**

    El ID de VLAN predeterminado de la red principal es **1** y es fijo.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red aparte. Los clientes aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**. El aislamiento de AP se aplica únicamente a los dispositivos cliente conectados por Wi-Fi.

### Servidor DHCP {#dhcp-server}

El servidor DHCP (**DHCP Server**) está habilitado de forma predeterminada. Asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte [cómo configurar una dirección IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final del rango DHCP si cambia el tamaño de su red, si se producen conflictos entre direcciones IP o si se modifica el rango que abarca la máscara de subred.

![Ajustes básicos del servidor DHCP de la red principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Si necesita configurar más opciones, haga clic en **Advanced**.

![Ajustes avanzados del servidor DHCP de la red principal 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Ajustes avanzados del servidor DHCP de la red principal 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica el periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway** indica qué dispositivo enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1** indica qué servidor principal traduce los nombres de dominio a direcciones IP.

- **DNS Server 2** indica qué servidor secundario resuelve los nombres de dominio si el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server) es un servicio que gestiona los trabajos de impresión y permite a los dispositivos de la red enviar solicitudes de impresión a impresoras remotas. Puede configurar varios puertos de impresión LPR.

### Reserva de direcciones {#address-reservation}

Si reserva una dirección IP para un cliente de la LAN, ese cliente recibirá siempre la misma dirección IP cuando acceda al servidor DHCP del router. Puede reservar direcciones IP para equipos o servidores que necesiten una configuración IP permanente.

**Nota**. Para que se aplique la reserva, vuelva a conectar al router los dispositivos cliente configurados.

Haga clic en **Add** para reservar una dirección IP.

![Reserva de direcciones de la red principal 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Se abrirá una ventana emergente.

![Reserva de direcciones de la red principal 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Seleccione la dirección **MAC** en la lista desplegable. El campo **IP** se rellenará automáticamente con la dirección IP disponible correspondiente. Si lo desea, introduzca un nombre de host (**hostname**) y un nombre personalizado (**name**) para facilitar la identificación. A continuación, haga clic en **Submit**.

![Reserva de direcciones de la red principal 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Si se ha guardado correctamente, la nueva reserva de dirección IP aparecerá en la página como se muestra a continuación.

![Reserva de direcciones de la red principal 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Red de invitados {#guest-network}

La red de invitados ofrece una conexión Wi-Fi específica para visitantes con acceso a Internet. Está aislada de la red principal para mejorar la seguridad.

**Nota**. Algunos modelos, como GL-MT5000 y GL-MT2500/GL-MT2500A, carecen de Wi-Fi, por lo que su panel web de administración no ofrece los ajustes de la red de invitados.

En la red de invitados puede consultar el estado de la interfaz, el ID de VLAN, la puerta de enlace y el rango DHCP.

![Red de invitados 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para abrir el panel de configuración de la red de invitados a la derecha de la página.

![Red de invitados 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

La página de configuración incluye los ajustes básicos y los ajustes del servidor DHCP.

### Ajustes básicos {#guest-network-basic-settings}

Puede configurar la subred dentro de los rangos de direcciones IPv4 privadas `192.168.0.0/16`, `172.16.0.0/12` y `10.0.0.0/8`.

![Ajustes básicos de la red de invitados](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    La **puerta de enlace predeterminada** de la red de invitados es **192.168.9.1**. Si entra en conflicto con su red local, cambie la dirección.

- **Netmask**

    La máscara de subred predeterminada es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred con más direcciones IP.

- **VLAN ID**

    El ID de VLAN predeterminado de la red de invitados es **9**. Puede cambiarlo si es necesario.

- **Associated LAN Ports**

    Seleccione los puertos LAN que desea asignar a esta subred. Los dispositivos conectados por cable a esos puertos se incorporarán a la red.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red aparte. Los clientes aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**. El aislamiento de AP se aplica únicamente a los dispositivos cliente conectados por Wi-Fi.

- **WAN Access Control**

    Esta opción controla el acceso de la subred local a las redes del lado WAN, incluidas Internet y otras subredes WAN.

    Hay tres modos de control de acceso WAN.

    - **Unrestricted** permite a esta subred acceder sin restricciones a Internet y a otras subredes del lado WAN.

    - **Block WAN Subnet** bloquea el acceso a otras subredes del lado WAN y mantiene disponible el acceso a Internet.

    - **Block Internet Access** bloquea todo el acceso saliente, tanto a Internet como a las subredes del lado WAN.

### Servidor DHCP {#guest-network-dhcp-server}

El servidor DHCP (**DHCP Server**) está habilitado de forma predeterminada. Asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte [cómo configurar una dirección IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final del rango DHCP si cambia el tamaño de su red, si se producen conflictos entre direcciones IP o si se modifica el rango que abarca la máscara de subred.

![Ajustes básicos del servidor DHCP de la red de invitados](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Si necesita configurar más opciones, haga clic en **Advanced**.

![Ajustes avanzados del servidor DHCP de la red de invitados 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Ajustes avanzados del servidor DHCP de la red de invitados 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica el periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway** indica qué dispositivo enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1** indica qué servidor principal traduce los nombres de dominio a direcciones IP.

- **DNS Server 2** indica qué servidor secundario resuelve los nombres de dominio si el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server) es un servicio que gestiona los trabajos de impresión y permite a los dispositivos de la red enviar solicitudes de impresión a impresoras remotas. Puede configurar varios puertos de impresión LPR.

## Red IoT {#iot-network}

La red IoT ofrece una conexión Wi-Fi específica para dispositivos IoT. Está aislada de la red principal y ofrece mayor compatibilidad y seguridad.

**Nota**. Algunos modelos, como GL-MT5000 y GL-MT2500/GL-MT2500A, carecen de Wi-Fi, por lo que su panel web de administración no ofrece los ajustes de la red IoT.

En la red IoT puede consultar el estado de la interfaz, el ID de VLAN, la puerta de enlace y el rango DHCP.

![Red IoT 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para abrir el panel de configuración de la red IoT a la derecha de la página. Desde ese panel puede cambiar los ajustes básicos y los del servidor DHCP.

![Red IoT 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Ajustes básicos {#iot-network-basic-settings}

Puede configurar la subred dentro de los rangos de direcciones IPv4 privadas `192.168.0.0/16`, `172.16.0.0/12` y `10.0.0.0/8`.

![Ajustes básicos de la red IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    La **puerta de enlace predeterminada** de la red IoT es **192.168.10.1**. Si entra en conflicto con su red local, cambie la dirección.

- **Netmask**

    La máscara de subred predeterminada es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred con más direcciones IP.

- **VLAN ID**

    El ID de VLAN predeterminado de la red IoT es **10**. Puede cambiarlo si es necesario.

- **Associated LAN Ports**

    Seleccione los puertos LAN que desea asignar a esta subred. Los dispositivos conectados por cable a esos puertos se incorporarán a la red.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red aparte. Los clientes aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**. El aislamiento de AP se aplica únicamente a los dispositivos cliente conectados por Wi-Fi.

- **WAN Access Control**

    Esta opción controla el acceso de la subred local a las redes del lado WAN, incluidas Internet y otras subredes WAN.

    Hay tres modos de control de acceso WAN.

    - **Unrestricted** permite a esta subred acceder sin restricciones a Internet y a otras subredes del lado WAN.

    - **Block WAN Subnet** bloquea el acceso a otras subredes del lado WAN y mantiene disponible el acceso a Internet.

    - **Block Internet Access** bloquea todo el acceso saliente, tanto a Internet como a las subredes del lado WAN.

### Servidor DHCP {#iot-network-dhcp-server}

El servidor DHCP (**DHCP Server**) está habilitado de forma predeterminada. Asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte [cómo configurar una dirección IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final del rango DHCP si cambia el tamaño de su red, si se producen conflictos entre direcciones IP o si se modifica el rango que abarca la máscara de subred.

![Ajustes básicos del servidor DHCP de la red IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Si necesita configurar más opciones, haga clic en **Advanced**.

![Ajustes avanzados del servidor DHCP de la red IoT 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Ajustes avanzados del servidor DHCP de la red IoT 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica el periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway** indica qué dispositivo enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1** indica qué servidor principal traduce los nombres de dominio a direcciones IP.

- **DNS Server 2** indica qué servidor secundario resuelve los nombres de dominio si el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server) es un servicio que gestiona los trabajos de impresión y permite a los dispositivos de la red enviar solicitudes de impresión a impresoras remotas. Puede configurar varios puertos de impresión LPR.

## Redes VLAN {#vlan-networks}

En la parte superior de la página principal puede crear **redes VLAN** adicionales para aislar distintos tipos de dispositivos o el tráfico de visitantes.

![Redes VLAN 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Haga clic en el botón **+ Add** a la derecha de la página para configurar una nueva red.

![Redes VLAN 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Ajustes básicos {#vlan-networks-basic-settings}

En esta página puede configurar los ajustes básicos de las redes VLAN.

![Ajustes básicos de las redes VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Introduzca un nombre que permita identificar la nueva subred.

- **Gateway**

    Configure manualmente la puerta de enlace de la nueva subred. Si entra en conflicto con su segmento LAN actual, cambie la dirección.

- **Netmask**

    La máscara de subred predeterminada es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred con más direcciones IP.

- **VLAN ID**

    Al crear una subred, debe asignarle un ID de VLAN entre **9** y **4000**. Para evitar conflictos de red, utilice un ID de VLAN que esté libre.

- **Associated LAN Ports**

    Seleccione los puertos LAN que desea asignar a esta subred. Los dispositivos conectados por cable a esos puertos se incorporarán a la red.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red aparte. Los clientes aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**. El aislamiento de AP se aplica únicamente a los dispositivos cliente conectados por Wi-Fi.

- **WAN Access Control**

    Esta opción controla el acceso de la subred local a las redes del lado WAN, incluidas Internet y otras subredes WAN.

    Hay tres modos de control de acceso WAN.

    - **Unrestricted** permite a esta subred acceder sin restricciones a Internet y a otras subredes del lado WAN.

    - **Block WAN Subnet** bloquea el acceso a otras subredes del lado WAN y mantiene disponible el acceso a Internet.

    - **Block Internet Access** bloquea todo el acceso saliente, tanto a Internet como a las subredes del lado WAN.

### Servidor DHCP {#vlan-networks-dhcp-server}

El servidor DHCP (**DHCP Server**) está habilitado de forma predeterminada. Asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte [cómo configurar una dirección IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final del rango DHCP si cambia el tamaño de su red, si se producen conflictos entre direcciones IP o si se modifica el rango que abarca la máscara de subred.

![Ajustes básicos del servidor DHCP de las redes VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Si necesita configurar más opciones, haga clic en **Advanced**.

![Ajustes avanzados del servidor DHCP de las redes VLAN 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![Ajustes avanzados del servidor DHCP de las redes VLAN 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica el periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway** indica qué dispositivo enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1** indica qué servidor principal traduce los nombres de dominio a direcciones IP.

- **DNS Server 2** indica qué servidor secundario resuelve los nombres de dominio si el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server) es un servicio que gestiona los trabajos de impresión y permite a los dispositivos de la red enviar solicitudes de impresión a impresoras remotas. Puede configurar varios puertos de impresión LPR.

Una vez configurada, la nueva red VLAN aparecerá en esta página con la información de la subred.

---

¿Tiene alguna pregunta? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
