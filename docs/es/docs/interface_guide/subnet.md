# Subred

**Nota**: Esta página está disponible actualmente en Flint 4 (GL-BE14000) y se implementará en otros modelos con el firmware v4.10.

---

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **Subnet**.

La página consolida la configuración de **LAN**, **Guest Network**, **IoT Network** y las **VLAN Networks** personalizadas en una vista unificada. Proporciona una interfaz centralizada para todos los ajustes relacionados con subredes, lo que permite crear y administrar varias subredes para aislar distintos tipos de dispositivos o tráfico.

## Red principal

**Main Network** es la red a la que está conectado el dispositivo mediante la Wi-Fi principal o mediante un cable Ethernet.

En Main Network puede ver directamente todos los estados de interfaz, el VLAN ID, la dirección IP del router y el rango DHCP.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha para configurar Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

La página de configuración incluye ajustes básicos, ajustes del servidor DHCP y reserva de direcciones.

### Ajustes básicos

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Esta es la dirección que introduciría en la barra de direcciones del navegador para acceder a la página de administración del router.

    De forma predeterminada es **192.168.8.1**. Puede cambiarla si entra en conflicto con su red.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. También puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    El VLAN ID predeterminado de Main Network es **1** y no se puede modificar.

- **AP Isolation**

    Puede aislar los dispositivos cliente en un segmento de red independiente. Estos dispositivos no podrán comunicarse con otros dispositivos de la misma red.

### Servidor DHCP

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, tendrá que configurar manualmente los ajustes de red de los dispositivos cliente. Haga clic [aquí](../tutorials/manually_configure_static_ip.md) para aprender a configurar manualmente una IP estática.

Puede cambiar las direcciones IP inicial y final según sus necesidades, por ejemplo, si su red se amplía o se reduce, si se producen conflictos de direcciones IP o si se modifica el rango de la máscara de subred.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Haga clic en **Advanced** para una configuración adicional si es necesario.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: El periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway**: El dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server**: Hay dos campos de servidor DNS para configurar el resolver principal y el secundario.

    **Nota**: El DNS principal se introduce en el campo superior y el secundario en el campo inferior. Si el servidor principal no está disponible, los dispositivos cliente harán failover automáticamente al resolver secundario, lo que mantiene la continuidad de la resolución de nombres de dominio.

- **LPR Server** (Line Printer Remote Server): Un servicio que gestiona trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

### Reserva de direcciones

Cuando especifica una dirección IP reservada para un cliente dentro de la LAN, el cliente siempre recibe la misma dirección IP cada vez que accede al servidor DHCP del router. Puede asignar direcciones IP reservadas a ordenadores o servidores que requieran ajustes IP permanentes.

**Nota:** Los clientes configurados tienen que volver a conectarse al router para activarse.

Haga clic en **Add** para reservar una IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

Verá una ventana emergente.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Seleccione **MAC** en la lista desplegable. La **IP** disponible correspondiente se rellenará automáticamente. También puede introducir un **hostname** y un **name** personalizado para identificarlo fácilmente. A continuación, haga clic en **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

Después de añadir una nueva reserva de dirección IP, verá la página como se muestra a continuación, lo que significa que la configuración se ha realizado correctamente.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Red de invitados

**Guest Network** proporciona una red Wi-Fi dedicada para visitantes. Aislada de la red principal, mejora la seguridad mientras proporciona un acceso cómodo a Internet.

**Nota**: Algunos modelos, por ejemplo GL-MT5000 y GL-MT2500/GL-MT2500A, no tienen función Wi-Fi, por lo que los ajustes de Guest Network no están disponibles en su panel web de administración.

En Guest Network puede ver directamente el estado de la interfaz, el VLAN ID, el gateway y el rango DHCP.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha; el panel de configuración de Guest Network se abrirá en el lado derecho de la página.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

La página de configuración incluye ajustes básicos y ajustes del servidor DHCP.

### Ajustes básicos

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    El **gateway predeterminado** de Guest Network es **192.168.9.1**. Si entra en conflicto con su red local, cámbielo por otro diferente.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. También puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    El VLAN ID predeterminado de Guest Network es **9** y se puede modificar según sea necesario.

- **AP Isolation**

    Esta función está disponible desde el firmware v4.5.

    Puede aislar los dispositivos cliente en un segmento de red independiente. Estos dispositivos no podrán comunicarse con otros dispositivos de la misma red.

- **WAN Access Control**

    WAN Access Control gestiona el acceso de la subred local a redes del lado WAN, incluido Internet y otras subredes WAN.

    Hay tres modos de control de acceso WAN disponibles:

    - **Unrestricted**: Permite que esta subred acceda a Internet y a otras subredes del lado WAN sin restricciones.

    - **Block WAN Subnet**: Bloquea el acceso a otras subredes del lado WAN. El acceso a Internet sigue estando disponible.

    - **Block Internet Access**: Bloquea todo el acceso saliente, incluido Internet y las subredes del lado WAN.

### Servidor DHCP

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, tendrá que configurar manualmente los ajustes de red de los dispositivos cliente. Haga clic [aquí](../tutorials/manually_configure_static_ip.md) para aprender a configurar manualmente una IP estática.

Puede cambiar las direcciones IP inicial y final según sus necesidades, por ejemplo, si su red se amplía o se reduce, si se producen conflictos de direcciones IP o si se modifica el rango de la máscara de subred.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Haga clic en **Advanced** para una configuración adicional si es necesario.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: El periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway**: El dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server**: Hay dos campos de servidor DNS para configurar el resolver principal y el secundario.

    **Nota**: El DNS principal se introduce en el campo superior y el secundario en el campo inferior. Si el servidor principal no está disponible, los dispositivos cliente harán failover automáticamente al resolver secundario, lo que mantiene la continuidad de la resolución de nombres de dominio.

- **LPR Server** (Line Printer Remote Server): Un servicio que gestiona trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

## IoT Network

IoT Network crea una red Wi-Fi dedicada para dispositivos IoT. Aislada de la red principal, ofrece mejor compatibilidad y mayor seguridad.

**Nota**: Algunos modelos, por ejemplo GL-MT5000 y GL-MT2500/GL-MT2500A, no tienen función Wi-Fi, por lo que los ajustes de IoT Network no están disponibles en su panel web de administración.

En IoT Network puede ver directamente el estado de la interfaz, el VLAN ID, el gateway y el rango DHCP.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Haga clic en **Edit** en la esquina inferior derecha; el panel de configuración de IoT Network se abrirá en el lado derecho de la página. Puede configurar Basic Settings y DHCP Server Settings en este panel.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Ajustes básicos

Puede configurar la subred dentro de los rangos de direcciones privadas IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    El **gateway predeterminado** de IoT Network es **192.168.10.1**. Si entra en conflicto con su red local, cámbielo por otro diferente.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. También puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    El VLAN ID predeterminado de IoT Network es **10** y se puede modificar según sea necesario.

- **AP Isolation**

    Esta función está disponible desde el firmware v4.5.

    Puede aislar los dispositivos cliente en un segmento de red independiente. Estos dispositivos no podrán comunicarse con otros dispositivos de la misma red.

- **WAN Access Control**

    WAN Access Control gestiona el acceso de la subred local a redes del lado WAN, incluido Internet y otras subredes WAN.

    Hay tres modos de control de acceso WAN disponibles:

    - **Unrestricted**: Permite que esta subred acceda a Internet y a otras subredes del lado WAN sin restricciones.

    - **Block WAN Subnet**: Bloquea el acceso a otras subredes del lado WAN. El acceso a Internet sigue estando disponible.

    - **Block Internet Access**: Bloquea todo el acceso saliente, incluido Internet y las subredes del lado WAN.

### Servidor DHCP

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, tendrá que configurar manualmente los ajustes de red de los dispositivos cliente. Haga clic [aquí](../tutorials/manually_configure_static_ip.md) para aprender a configurar manualmente una IP estática.

Puede cambiar las direcciones IP inicial y final según sus necesidades, por ejemplo, si su red se amplía o se reduce, si se producen conflictos de direcciones IP o si se modifica el rango de la máscara de subred.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Haga clic en **Advanced** para una configuración adicional si es necesario.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: El periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway**: El dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server**: Hay dos campos de servidor DNS para configurar el resolver principal y el secundario.

    **Nota**: El DNS principal se introduce en el campo superior y el secundario en el campo inferior. Si el servidor principal no está disponible, los dispositivos cliente harán failover automáticamente al resolver secundario, lo que mantiene la continuidad de la resolución de nombres de dominio.

- **LPR Server** (Line Printer Remote Server): Un servicio que gestiona trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

## Redes VLAN

En la parte superior de la página principal, puede crear **VLAN networks** adicionales según sea necesario para aislar distintos tipos de dispositivos o tráfico de visitantes.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Haga clic en el botón **+ Add** del lado derecho de la página para configurar una nueva red.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Ajustes básicos

Puede configurar la información básica de **VLAN Networks** en esta página.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Personalice un nombre para la subred recién creada para identificarla.

- **Gateway**

    Configure manualmente el gateway de la nueva subred. Sustituya este gateway si entra en conflicto con su segmento LAN existente.

- **Netmask**

    El valor predeterminado es **255.255.255.0**. También puede seleccionar **255.255.0.0** si necesita una subred mayor con más direcciones IP.

- **VLAN ID**

    Al crear una subred, debe asignar un VLAN ID entre **9** y **4000**. Evite usar un VLAN ID que ya esté ocupado para prevenir conflictos de red.

- **AP Isolation**

    Esta función está disponible desde el firmware v4.5.

    Puede aislar los dispositivos cliente en un segmento de red independiente. Estos dispositivos no podrán comunicarse con otros dispositivos de la misma red.

- **WAN Access Control**

    WAN Access Control gestiona el acceso de la subred local a redes del lado WAN, incluido Internet y otras subredes WAN.

    Hay tres modos de control de acceso WAN disponibles:

    - **Unrestricted**: Permite que esta subred acceda a Internet y a otras subredes del lado WAN sin restricciones.

    - **Block WAN Subnet**: Bloquea el acceso a otras subredes del lado WAN. El acceso a Internet sigue estando disponible.

    - **Block Internet Access**: Bloquea todo el acceso saliente, incluido Internet y las subredes del lado WAN.

### Servidor DHCP

El **DHCP Server** está habilitado de forma predeterminada. El servidor DHCP asigna automáticamente direcciones IP y otros parámetros de comunicación a cada dispositivo cliente.

Si el servidor DHCP está deshabilitado, tendrá que configurar manualmente los ajustes de red de los dispositivos cliente. Haga clic [aquí](../tutorials/manually_configure_static_ip.md) para aprender a configurar manualmente una IP estática.

Puede cambiar las direcciones IP inicial y final según sus necesidades, por ejemplo, si su red se amplía o se reduce, si se producen conflictos de direcciones IP o si se modifica el rango de la máscara de subred.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Haga clic en **Advanced** para una configuración adicional si es necesario.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: El periodo durante el cual una dirección IP asignada por DHCP es válida para un dispositivo.

- **Gateway**: El dispositivo que enruta el tráfico entre la red local y redes externas como Internet.

- **DNS Server**: Hay dos campos de servidor DNS para configurar el resolver principal y el secundario.

    **Nota**: El DNS principal se introduce en el campo superior y el secundario en el campo inferior. Si el servidor principal no está disponible, los dispositivos cliente harán failover automáticamente al resolver secundario, lo que mantiene la continuidad de la resolución de nombres de dominio.

- **LPR Server** (Line Printer Remote Server): Un servicio que gestiona trabajos de impresión y permite que los dispositivos de red envíen solicitudes de impresión a impresoras remotas. Se pueden configurar varios puertos de impresora LPR.

Una vez configurada, la nueva red VLAN aparecerá en la página actual y mostrará la información de la subred.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.

