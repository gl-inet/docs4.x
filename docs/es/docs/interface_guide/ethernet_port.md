# Puerto Ethernet

**Nota**: Esta página estuvo disponible como **Port Management** desde el firmware v4.7 y pasó a llamarse **Ethernet Port** en el firmware v4.8.3.

---

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Port Management** o **Ethernet Port**.

Esta página le permite gestionar las funciones de los puertos Ethernet, WAN o LAN, y ver detalles del puerto como la dirección MAC y la velocidad negociada.

## WAN

Esta sección muestra la función del puerto, WAN o LAN, la dirección MAC y la velocidad negociada.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

- **WAN/LAN**: El modo de funcionamiento actual del puerto WAN físico. Puede cambiarlo a LAN según sea necesario.

- **MAC Mode**: El valor predeterminado es Factory Mode. Puede cambiarlo a Clone Mode o Random Mode.

- **Mac Address**: La dirección MAC de la interfaz WAN.

- **Negotiated Network Port Rate**: La velocidad de enlace negociada de la interfaz WAN. Solo se muestra cuando se detecta un enlace válido.

## LAN

Esta sección muestra la velocidad negociada del puerto LAN. Solo se muestra cuando se detecta un enlace válido.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Algunos modelos admiten cambiar LAN 1 a un puerto WAN para escenarios de WAN dual por Ethernet. Haga clic en [Dual-Ethernet WAN](#dual-ethernet-wan) para obtener más información.

## Dual-Ethernet WAN

La función Dual-Ethernet WAN permite cambiar un puerto Ethernet LAN predeterminado a un puerto WAN secundario para acceder a Internet mediante Ethernet dual. Esto proporciona conectividad de respaldo fiable y, cuando es compatible, admite agregación de ancho de banda para cargas de trabajo que requieren mucho ancho de banda. También permite conectarse simultáneamente a dos redes independientes, por ejemplo una de trabajo y otra personal, lo que aporta mayor flexibilidad sin hardware adicional.

??? "Modelos compatibles"
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

    **Nota**: El GL-E5800 (Mudi 7) está equipado con un puerto Ethernet (LAN de forma predeterminada, que puede cambiarse a WAN) y con un **puerto USB-C compatible con OTG**. Para añadir un segundo puerto Ethernet para Dual-Ethernet WAN, conecte al puerto USB-C un adaptador USB-C a Ethernet vendido por separado.

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

Siga estos pasos para cambiar un puerto LAN a un puerto WAN.

1. En la página **Port Management** o **Ethernet Port**, haga clic en la pestaña **LAN**, cambie la función del puerto a WAN y, a continuación, haga clic en **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. En la ventana emergente, haga clic en **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. El puerto seleccionado funcionará ahora como puerto WAN. Puede continuar configurando Multi-WAN [aquí](multi-wan.md).

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
