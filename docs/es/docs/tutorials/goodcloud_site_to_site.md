# Site to Site de GoodCloud

## Introducción

GoodCloud Site to Site permite que oficinas ubicadas en distintos lugares establezcan conexiones seguras entre sí a través de Internet. Amplía la red de la empresa y hace que los recursos informáticos de una ubicación estén disponibles para los empleados de otras ubicaciones a través de la red.
![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}
**Escenario 1**: Decenas de sucursales de una misma empresa necesitan integrarse en una red privada unificada para compartir recursos sin fricciones entre todas las ubicaciones.
**Escenario 2**: Cuando dos empresas con una colaboración estrecha necesitan trabajar juntas, Site to Site facilita esa colaboración en un entorno de red compartido y seguro.
**Escenario 3**: Para familias con cámaras IP, Site to Site permite acceder remotamente al dispositivo cuando los miembros están fuera de casa y supervisarlo con facilidad desde cualquier lugar.

## Condiciones

1. Se requieren al menos dos routers GL.iNet para crear una red Site to Site.

2. Al menos uno de los routers debe tener una dirección IP pública para poder configurarse como nodo principal. [Compruebe si su ISP le asigna una dirección IP pública](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    Se recomienda elegir como nodo principal un router con buen rendimiento y la mejor velocidad de red.

3. **NO** se recomienda ejecutar Site to Site mientras los subnodos también estén usando un cliente VPN / Tailscale / ZeroTier / AstroWarp, ya que esto puede hacer que la configuración de red sea especialmente compleja.

## Crear una red Site to Site

1. Vincule sus routers a su cuenta de GoodCloud. [Cómo hacerlo](../interface_guide/cloud.md/#setup-your-goodcloud-account)?

2. Inicie sesión en [GoodCloud](https://www.goodcloud.xyz/#/login), vaya a **Site to Site** en la barra lateral izquierda y haga clic en **Create Network** en la esquina superior derecha.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Marque la casilla de la izquierda para seleccionar al menos dos dispositivos.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

    Los dispositivos seleccionados se mostrarán en la parte inferior de la página.

    El puerto predeterminado de Site to Site es **51830**. Si desea usar otro puerto, haga clic en **Advanced** en la esquina inferior izquierda para modificarlo. Luego haga clic en **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Una red Site to Site puede tener hasta 10 dispositivos para garantizar un rendimiento estable.

4. Asigne un nombre a la red y haga clic en **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing comenzará a comprobar si alguno de los dispositivos puede configurarse como Main Node.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Si ninguno de sus dispositivos puede usarse como Main Node, asegúrese de que:

    - Al menos un router tenga una IP pública, ya sea estática o dinámica.
    - El puerto esté abierto. El puerto predeterminado para Site to Site es 51830. También puede cambiar el puerto y volver a intentarlo.
    - Si el router que desea establecer como Main Node está detrás de NAT, es posible que necesite configurar el reenvío de puertos.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Si hay más de un dispositivo que puede establecerse como Main Node, elija uno para continuar. Sugerimos seleccionar como Main Node el router con mejor rendimiento y velocidad de red.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Si solo hay un dispositivo que puede establecerse como Main Node, se abrirá directamente la página de detalles de Site to Site.

6. La red está deshabilitada de forma predeterminada. Asegúrese de que las direcciones IP LAN de todos los nodos no entren en conflicto entre sí. Haga clic en el icono de engranaje para cambiar la IP LAN si es necesario y después haga clic en **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Espere unos minutos. Cuando la línea discontinua pase a ser continua, significará que la red Site to Site se ha establecido correctamente.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Probar la conexión Site to Site

1. Conecte su PC o smartphone a uno de los nodos de esta red Site to Site.

2. Abra un navegador web para acceder a la IP LAN de otro nodo. Si puede acceder a la página de inicio de sesión, la conexión entre esos dos nodos funciona correctamente.

## Rutas y otras opciones

De forma predeterminada, cada nodo puede acceder a la LAN de los demás nodos. Por motivos de seguridad, recomendamos abrir solo las direcciones IP de servicios concretos.

Por ejemplo, hay un Servidor A (172.30.97.100) en la subred del Nodo 1. Si desea que los demás nodos solo accedan al Servicio A del Nodo 1, puede configurarlo de la siguiente manera:
![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}
Puede añadir también las rutas principales del nodo.

Cada subnodo crea una red de túnel cifrado hacia el nodo principal. Si desea cambiar la IP de la subred del túnel, haga clic en **IP Address Range** para modificarla.
Aplicar el cambio del rango de direcciones IP provocará una desconexión de la red durante unos minutos.
![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
