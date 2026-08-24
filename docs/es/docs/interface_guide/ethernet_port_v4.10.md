# Puerto Ethernet (firmware v4.10)

**Nota**: El contenido de esta página está disponible actualmente en Flint 4 (GL-BE14000) y se incorporará a otros modelos con el firmware v4.10.

Si el dispositivo utiliza otra versión del firmware, use el selector siguiente para cambiar a la guía correspondiente.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [Firmware v4.9 y anteriores](ethernet_port.md)

</div>

---

En el menú lateral izquierdo del panel de administración web, vaya a **NETWORK** -> **Ethernet Port**.

Esta página muestra todas las interfaces del router. Puede consultar el estado de conexión de cada interfaz, administrar la función de los puertos Ethernet (WAN o LAN) y ver detalles como la dirección MAC, la velocidad negociada y el estado actual del enlace. Además, puede asignar interfaces físicas a cualquiera de las subredes que haya creado.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: Cuando el icono del puerto aparece resaltado en azul, el enlace físico está activo.

- **Link Down**: Cuando el icono del puerto aparece en gris, el enlace físico está inactivo.

- **Speed**: Velocidad de transmisión negociada del puerto Ethernet.

- **MAC**: Dirección MAC del puerto.

- **VLAN Mode**: El modo de funcionamiento de los puertos LAN se puede establecer en Standard o Multiple VLANs.

- **Native Network**: Subred sin etiquetar asignada de forma predeterminada al puerto LAN.

- **Allowed VLANs**: Especifica las VLAN etiquetadas que pueden pasar por este puerto en el modo Multiple VLANs.

- **Settings**: Haga clic para acceder a la página de configuración de cada puerto.

## WAN

Esta sección muestra el modo del puerto (WAN o LAN), la dirección MAC y la velocidad negociada.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: Modo de funcionamiento actual del puerto WAN físico. Puede establecerlo en LAN cuando sea necesario.

- **MAC Mode**: El valor predeterminado es Factory Mode. Puede cambiarlo a Clone Mode o Random Mode.

- **MAC Address**: Dirección MAC de la interfaz WAN.

- **Negotiated Network Port Rate**: Velocidad de enlace negociada de la interfaz WAN. Solo se muestra cuando se detecta un enlace válido.

## LAN

Esta sección muestra la configuración de los puertos LAN. Puede establecer Ethernet Mode en **Standard** o **Multiple VLANs**, según sus necesidades.

### Modo Standard

El modo Standard solo permite una VLAN (Untagged) y se utiliza para conectar dispositivos finales.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: Velocidad de enlace negociada de la interfaz LAN. Solo se muestra cuando se detecta un enlace válido.

- **Ethernet Mode**: El valor predeterminado es Standard Mode.

- **Access Network**: Access Network permite aislar redes mediante la asignación de los puertos LAN a subredes diferentes.

Una vez configurado, puede volver a la página Ethernet Port para comprobar los ajustes.

### Modo Multiple VLANs

El modo Multiple VLANs permite varias VLAN (Tagged) en un mismo puerto y suele utilizarse para conectar puntos de acceso u otros switches.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: Velocidad de enlace negociada de la interfaz LAN. Solo se muestra cuando se detecta un enlace válido.

- **VLAN Mode**: Para cambiar al modo Multiple VLANs, haga clic en la pestaña Multiple VLANs.

- **Untagged Traffic Handling**: Configure cómo procesa el puerto los paquetes sin etiquetar. Puede descartarlos directamente o reenviarlos a otra subred como red PVID nativa.

- **Allowed Tagged Networks**: Especifica las VLAN que pueden pasar por este puerto en modo etiquetado. Puede seleccionar redes VLAN de la lista; solo se reenviará el tráfico coincidente.

Una vez configurado, puede volver a la página Ethernet Port para comprobar los ajustes.

Algunos modelos permiten convertir LAN 1 en un puerto WAN para utilizar una configuración WAN Ethernet doble. Consulte [WAN Ethernet doble](#dual-ethernet-wan) para obtener más información.

## Dual-Ethernet WAN

La función WAN Ethernet doble permite convertir un puerto Ethernet LAN predeterminado en un puerto WAN secundario para disponer de dos conexiones a Internet por Ethernet. Proporciona una conexión de respaldo fiable y admite la agregación de ancho de banda, cuando sea compatible, para tareas que requieren mucho ancho de banda. También permite conectarse simultáneamente a dos redes independientes, por ejemplo, una de trabajo y otra personal, lo que aporta mayor flexibilidad sin hardware adicional.

??? "Modelos compatibles"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Nota**: GL-E5800 (Mudi 7) dispone de un puerto Ethernet (LAN de forma predeterminada, que puede convertirse en WAN) y un **puerto USB-C compatible con OTG**. Para añadir un segundo puerto Ethernet para WAN Ethernet doble, conecte al puerto USB-C un adaptador USB-C a Ethernet que se vende por separado.

??? "Modelos no compatibles"

    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Siga estos pasos para convertir un puerto LAN en un puerto WAN. En este ejemplo se utiliza Flint 3 (GL-BE9300).

1. En la página **Ethernet Port**, haga clic en la configuración de **LAN1** para acceder a la página de configuración. A continuación, cambie la función del puerto a WAN y haga clic en **Apply**.

    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Vuelva a la página Ethernet Port para comprobar que la función del puerto ha cambiado a WAN.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. El puerto seleccionado funcionará ahora como puerto WAN. A continuación, puede configurar Multi-WAN [aquí](multi-wan.md).

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
