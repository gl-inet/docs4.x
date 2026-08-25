# Multi-WAN

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **Multi-WAN**.

Puede configurar el router con varios métodos de acceso a Internet, de modo que cuando un tipo de acceso a Internet no esté disponible, pueda cambiar automáticamente a otro tipo en poco tiempo. También puede usar varios métodos de acceso a Internet al mismo tiempo, asignando la conexión de red a diferentes métodos de conexión en una determinada proporción.

Los routers GL.iNet pueden conectarse a Internet de varias maneras, como [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md) y [Cellular](internet_cellular.md).

!!! Note

    1. Los modelos sin funcionalidad Wi-Fi, por ejemplo GL-MT2500/GL-MT2500A, solo admiten acceso a la red mediante Ethernet, Tethering y Cellular.

    2. Los modelos sin puerto USB, por ejemplo GL-B3000, solo admiten acceso a la red mediante Ethernet y Repeater.

    3. Algunos modelos admiten [Dual-Ethernet WAN](ethernet_port.md#dual-ethernet-wan), lo que añadirá una interfaz Ethernet adicional en la interfaz de usuario.

## Seguimiento del estado de la interfaz

Los routers GL.iNet admiten hasta 5 interfaces de red virtuales, aunque el número exacto puede variar según el modelo. Por ejemplo, el GL-MT6000 tiene **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** y **Cellular**, cada una con funciones de red distintas en configuraciones definidas por software.

Los routers utilizan el comando **ping** o **httping** solo para v4.3 y anteriores para rastrear el estado de la conexión con la IP de destino y determinar si la interfaz está disponible.

Si la interfaz está disponible, se mostrará un punto verde en el lado izquierdo; de lo contrario, será gris.

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Ajustes de seguimiento del estado

Haga clic en el icono de engranaje para acceder a los ajustes de seguimiento del estado de cada interfaz de red.

Por ejemplo, esta es la configuración de seguimiento del estado para la interfaz Ethernet, y lo mismo se aplica a otras interfaces.

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: Está habilitado de forma predeterminada. Puede deshabilitar el seguimiento del estado de la interfaz y, como resultado, el router determinará el estado de la interfaz según el estado físico, por ejemplo, si el cable de red está conectado o no.

- **Detection Mode**: Esta función se introdujo como **Low Data Mode** en v4.5 y pasó a llamarse **Detection Mode** en v4.7. Hay tres modos disponibles: **Normal Mode**, **Low Data Mode** y **Strict Mode**.

  El modo normal se utiliza de forma predeterminada, el modo de bajo consumo de datos solo rastrea cuando se produce un error de red en una interfaz, y el modo estricto determina el estado de la interfaz solo en función de los resultados de un comando de detección desde una IP pública.

  Puede usar **Low Data Mode** cuando tenga un plan de datos limitado. Sin embargo, una desventaja es que la reconexión tras una desconexión de red puede ser ligeramente más lenta en comparación con el modo normal, y solo la interfaz celular se activará de forma predeterminada.

- **Track Command**: El comando ping se usa para rastrear el estado de la conexión con la IP de destino y determinar si la interfaz está disponible. Para firmware v4.3 y anteriores, también está disponible el comando httping.

- **IPv4 Track IP**: Aquí puede personalizar la IP de seguimiento IPv4.

!!! Note

    Algunos firmware antiguos, como v4.3, proporcionan ajustes como **Track Interval**, **Change to Failure Condition** y **Change to Available Condition**. Estos ajustes se eliminaron desde v4.5 y se sustituyeron por **Detection Mode** y **Sensitivity Options**.

### Opciones de sensibilidad

Esta función está disponible desde v4.5.

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

Esta sensibilidad determina el intervalo de tiempo para la detección del estado de Internet.

- Si la red es estable y se usa en escenarios como ver videos o transmisiones en directo o jugar, se recomienda usar alta sensibilidad para un cambio rápido en caso de desconexión de red.
- Si la red es inestable y está descargando archivos en caché, se recomienda usar baja sensibilidad para evitar cambios constantes de red y detectar conexiones fallidas.

**Consejo**: Cambiar a alta sensibilidad puede provocar desconexiones de red. Ajústelo con precaución.

## Modo Multi-WAN

Multi-WAN dispone de dos modos: **Failover** y **Load Balance**. Son mutuamente excluyentes y solo se puede utilizar uno a la vez.

### Failover

Failover es el modo predeterminado cuando existen varias conexiones WAN. Si falla el enlace activo, el router cambiará automáticamente a otra interfaz de red para acceder a Internet.

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

Puede establecer la prioridad de cada interfaz. Si falla la interfaz en uso, el router cambia a la siguiente interfaz disponible con la prioridad más alta. Cuando se restablece una conexión con mayor prioridad, el router vuelve automáticamente a ella.

### Load Balance

Load Balance permite utilizar varios enlaces de red al mismo tiempo, lo que aumenta el ancho de banda y mejora el rendimiento total.

**Load Ratio** determina cómo se distribuye el tráfico entre las interfaces. El sistema asigna las conexiones nuevas a cada interfaz de acuerdo con la proporción configurada.

Se pueden configurar las dos proporciones de carga siguientes:

- **Default Load Ratio**

    Si el router está conectado simultáneamente a cuatro redes (Ethernet, Repeater, Tethering y Cellular) y las cuatro interfaces pueden acceder a Internet, la configuración 1:1:1:1 hace que el sistema distribuya las conexiones nuevas uniformemente entre las cuatro interfaces según dicha proporción.

- **Customize Load Ratio**

    Si el ancho de banda de Ethernet es de 200 Mbps, el de la conexión Wi-Fi Repeater es de 100 Mbps y no hay conexiones Tethering ni Cellular activas, puede establecer la proporción en 2 para Ethernet, 1 para Repeater y 0 para Tethering/Cellular. El sistema asignará las conexiones nuevas según la proporción 2:1, de modo que Ethernet procesará aproximadamente el doble de conexiones que Repeater. En comparación con el modo Failover, esto mejora el rendimiento total al equilibrar la carga entre las interfaces disponibles.

**Nota:** No se garantiza que las conexiones activas o el tráfico coincidan exactamente con la proporción de carga. Se aproximará más a esa proporción si se utiliza durante más tiempo.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

## Escenarios de uso

- El sistema de caja de una tienda usa una conexión cableada a Internet, mientras que Repeater hacia una red Wi-Fi de tiendas cercanas, o insertar una tarjeta SIM para habilitar la red celular, se usa como método de acceso a Internet de respaldo para evitar que los pagos móviles fallen cuando el cable de red no esté disponible.

- El router se conecta mediante Repeater a una Wi-Fi pública, pero la velocidad de red no es lo suficientemente alta, por lo que puede usar Mobile Tethering para hacer balanceo de carga al mismo tiempo y mejorar el ancho de banda total.

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
