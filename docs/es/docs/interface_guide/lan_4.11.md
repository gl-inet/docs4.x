# LAN {#lan}

**Nota**: Esta guía se refiere al firmware v4.11 y versiones posteriores. Si su dispositivo utiliza otra versión, seleccione la guía correspondiente en el menú inferior.

<div class="gl-link-select" data-label="Versión de firmware" data-placeholder="Firmware v4.11 y versiones posteriores" markdown="1">

- [Firmware v4.9 y versiones anteriores](lan.md)

</div>

---

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **LAN**.

Desde esta página puede configurar y gestionar **Main Network**, **Guest Network**, **IoT Network** y las **VLAN Networks** personalizadas. Puede crear y gestionar varias subredes para aislar distintos tipos de dispositivos o de tráfico.

## Red principal {#main-network}

**Main Network** es la red a la que se conecta su dispositivo por la Wi-Fi principal o mediante un cable Ethernet.

En **Main Network** puede consultar el estado de todas las interfaces, el ID de VLAN, la dirección IP del router y el rango DHCP.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para configurar la red principal.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

La página de configuración incluye los ajustes básicos, los del servidor DHCP y la reserva de direcciones.

### Ajustes básicos {#basic-settings}

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4 `192.168.0.0/16`, `172.16.0.0/12` y `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Introduzca esta dirección en la barra de direcciones del navegador para acceder al panel web de administración del router.

    El valor predeterminado es **192.168.8.1**. Puede cambiarlo si entra en conflicto con su red.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    El ID de VLAN de la red principal es **1** y no se puede modificar.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red independiente. Los dispositivos aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**: La opción **AP Isolation** solo se aplica a los clientes Wi-Fi.

### Servidor DHCP {#dhcp-server}

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte la guía para [configurar manualmente una IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final según sus necesidades. Por ejemplo, puede ajustarlas si su red se amplía o se reduce, si hay conflictos de direcciones IP o si cambia el rango de la máscara de subred.

![main network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Haga clic en **Advanced** si necesita acceder a más ajustes.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Tiempo durante el que una dirección IP asignada mediante DHCP sigue siendo válida para el dispositivo.

- **Gateway**. Dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1**. Servidor principal que traduce los nombres de dominio en direcciones IP.

- **DNS Server 2**. Servidor secundario que resuelve los nombres de dominio cuando el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server). Servicio que gestiona los trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

### Reserva de direcciones {#address-reservation}

Si reserva una dirección IP para un cliente de la LAN, el cliente recibirá siempre la misma dirección IP al acceder al servidor DHCP del router. Puede reservar direcciones IP para ordenadores o servidores que necesiten una configuración IP permanente.

**Nota**: Los clientes configurados deben volver a conectarse al router para que se aplique la reserva.

Haga clic en **Add** para reservar una dirección IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Se abrirá una ventana emergente.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Seleccione **MAC** en la lista desplegable. La **IP** disponible correspondiente se rellenará automáticamente. Si lo desea, introduzca un nombre de host en **hostname** y un nombre personalizado en **name** para facilitar la identificación. A continuación, haga clic en **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Cuando se añada correctamente la reserva de dirección IP, aparecerá la página que se muestra a continuación.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Red de invitados {#guest-network}

**Guest Network** ofrece una red Wi-Fi dedicada a los visitantes. Está aislada de la red principal, lo que mejora la seguridad y facilita el acceso a Internet.

**Nota**: Algunos modelos, como GL-MT5000 y GL-MT2500/GL-MT2500A, carecen de Wi-Fi. Su panel web de administración no ofrece los ajustes de la red de invitados.

En **Guest Network** puede consultar el estado de la interfaz, el ID de VLAN, la puerta de enlace y el rango DHCP.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para abrir el panel de configuración de la red de invitados a la derecha de la página.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

La página de configuración incluye los ajustes básicos y los del servidor DHCP.

### Ajustes básicos {#guest-network-basic-settings}

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4 `192.168.0.0/16`, `172.16.0.0/12` y `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    La **puerta de enlace predeterminada** de la red de invitados es **192.168.9.1**. Si entra en conflicto con su red local, cámbiela por otra.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    El ID de VLAN predeterminado de la red de invitados es **9**. Puede cambiarlo si es necesario.

- **Associated LAN Ports**

    Seleccione los puertos LAN que desea asignar a esta subred. Los dispositivos conectados por cable a estos puertos se incorporarán a la red.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red independiente. Los dispositivos aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**: La opción **AP Isolation** solo se aplica a los clientes Wi-Fi.

- **WAN Access Control**

    **WAN Access Control** regula el acceso desde la subred local a Internet y a otras subredes del lado WAN.

    Hay tres modos de control de acceso WAN disponibles.

    - **Unrestricted**. Permite el acceso desde esta subred a Internet y a otras subredes del lado WAN sin restricciones.

    - **Block WAN Subnet**. Bloquea el acceso a otras subredes del lado WAN. El acceso a Internet sigue disponible.

    - **Block Internet Access**. Bloquea todo el acceso saliente, incluido el acceso a Internet y a las subredes del lado WAN.

### Servidor DHCP {#guest-network-dhcp-server}

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte la guía para [configurar manualmente una IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final según sus necesidades. Por ejemplo, puede ajustarlas si su red se amplía o se reduce, si hay conflictos de direcciones IP o si cambia el rango de la máscara de subred.

![guest network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Haga clic en **Advanced** si necesita acceder a más ajustes.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Tiempo durante el que una dirección IP asignada mediante DHCP sigue siendo válida para el dispositivo.

- **Gateway**. Dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1**. Servidor principal que traduce los nombres de dominio en direcciones IP.

- **DNS Server 2**. Servidor secundario que resuelve los nombres de dominio cuando el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server). Servicio que gestiona los trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

## Red IoT {#iot-network}

**IoT Network** crea una red Wi-Fi dedicada a los dispositivos IoT. Está aislada de la red principal, lo que mejora la compatibilidad y la seguridad.

**Nota**: Algunos modelos, como GL-MT5000 y GL-MT2500/GL-MT2500A, carecen de Wi-Fi. Su panel web de administración no ofrece los ajustes de la red IoT.

En **IoT Network** puede consultar el estado de la interfaz, el ID de VLAN, la puerta de enlace y el rango DHCP.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para abrir el panel de configuración de la red IoT a la derecha de la página. En este panel puede modificar los ajustes básicos y los del servidor DHCP.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Ajustes básicos {#iot-network-basic-settings}

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4 `192.168.0.0/16`, `172.16.0.0/12` y `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    La **puerta de enlace predeterminada** de la red IoT es **192.168.10.1**. Si entra en conflicto con su red local, cámbiela por otra.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    El ID de VLAN predeterminado de la red IoT es **10**. Puede cambiarlo si es necesario.

- **Associated LAN Ports**

    Seleccione los puertos LAN que desea asignar a esta subred. Los dispositivos conectados por cable a estos puertos se incorporarán a la red.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red independiente. Los dispositivos aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**: La opción **AP Isolation** solo se aplica a los clientes Wi-Fi.

- **WAN Access Control**

    **WAN Access Control** regula el acceso desde la subred local a Internet y a otras subredes del lado WAN.

    Hay tres modos de control de acceso WAN disponibles.

    - **Unrestricted**. Permite el acceso desde esta subred a Internet y a otras subredes del lado WAN sin restricciones.

    - **Block WAN Subnet**. Bloquea el acceso a otras subredes del lado WAN. El acceso a Internet sigue disponible.

    - **Block Internet Access**. Bloquea todo el acceso saliente, incluido el acceso a Internet y a las subredes del lado WAN.

### Servidor DHCP {#iot-network-dhcp-server}

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte la guía para [configurar manualmente una IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final según sus necesidades. Por ejemplo, puede ajustarlas si su red se amplía o se reduce, si hay conflictos de direcciones IP o si cambia el rango de la máscara de subred.

![iot network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Haga clic en **Advanced** si necesita acceder a más ajustes.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Tiempo durante el que una dirección IP asignada mediante DHCP sigue siendo válida para el dispositivo.

- **Gateway**. Dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1**. Servidor principal que traduce los nombres de dominio en direcciones IP.

- **DNS Server 2**. Servidor secundario que resuelve los nombres de dominio cuando el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server). Servicio que gestiona los trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

## Redes VLAN {#vlan-networks}

En la parte superior de la página principal puede crear **redes VLAN** adicionales para aislar distintos tipos de dispositivos o el tráfico de los visitantes.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Haga clic en **+ Add** en el lado derecho de la página para configurar una nueva red.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Ajustes básicos {#vlan-networks-basic-settings}

En esta página puede configurar los ajustes básicos de **VLAN Networks**.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Asigne un nombre a la nueva subred para identificarla.

- **Gateway**

    Configure manualmente la puerta de enlace de la nueva subred. Cámbiela si entra en conflicto con el segmento LAN existente.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. Puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    Al crear una subred, debe asignar un ID de VLAN entre **9** y **4000**. Para evitar conflictos de red, utilice un ID de VLAN que esté libre.

- **Associated LAN Ports**

    Seleccione los puertos LAN que desea asignar a esta subred. Los dispositivos conectados por cable a estos puertos se incorporarán a la red.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red independiente. Los dispositivos aislados no podrán comunicarse con otros dispositivos de la misma red.

    **Nota**: La opción **AP Isolation** solo se aplica a los clientes Wi-Fi.

- **WAN Access Control**

    **WAN Access Control** regula el acceso desde la subred local a Internet y a otras subredes del lado WAN.

    Hay tres modos de control de acceso WAN disponibles.

    - **Unrestricted**. Permite el acceso desde esta subred a Internet y a otras subredes del lado WAN sin restricciones.

    - **Block WAN Subnet**. Bloquea el acceso a otras subredes del lado WAN. El acceso a Internet sigue disponible.

    - **Block Internet Access**. Bloquea todo el acceso saliente, incluido el acceso a Internet y a las subredes del lado WAN.

### Servidor DHCP {#vlan-networks-dhcp-server}

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, deberá configurar manualmente los ajustes de red de los dispositivos cliente. Consulte la guía para [configurar manualmente una IP estática](../tutorials/manually_configure_static_ip.md).

Puede cambiar las direcciones IP inicial y final según sus necesidades. Por ejemplo, puede ajustarlas si su red se amplía o se reduce, si hay conflictos de direcciones IP o si cambia el rango de la máscara de subred.

![vlan networks dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Haga clic en **Advanced** si necesita acceder a más ajustes.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Tiempo durante el que una dirección IP asignada mediante DHCP sigue siendo válida para el dispositivo.

- **Gateway**. Dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server 1**. Servidor principal que traduce los nombres de dominio en direcciones IP.

- **DNS Server 2**. Servidor secundario que resuelve los nombres de dominio cuando el servidor DNS principal no está disponible.

- **LPR Server** (Line Printer Remote Server). Servicio que gestiona los trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

Una vez configurada, la nueva red VLAN aparecerá en la página junto con la información de su subred.

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
