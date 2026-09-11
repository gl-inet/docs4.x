# Firmware v4.9

Esta versión se centra en un control de red más preciso, una mejor gestión del tráfico, mayor seguridad de red y una interfaz de usuario renovada, todo ello diseñado para ofrecer una mejor experiencia general.

Obtenga el firmware más reciente en el [Centro de descarga de firmware](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control

Flow Control es un módulo central de gestión de red que permite identificar, supervisar, regular y filtrar el tráfico de red con precisión. Optimiza la asignación de recursos de red, elimina la congestión del ancho de banda y normaliza el comportamiento de acceso a la red para ofrecer una experiencia más fluida, segura y controlable. En el firmware v4.9, este módulo integra varias funciones prácticas para gestionar el tráfico de forma integral.

El módulo Flow Control incluye DPI Engine, Data Statistics, Content Filter, QoS, SQM y Parental Control.

### DPI Engine

A diferencia de los routers tradicionales, que solo identifican las direcciones de origen y destino, DPI (Deep Packet Inspection) analiza en profundidad la carga útil de los paquetes. Mediante una biblioteca de coincidencia de características, identifica con precisión aplicaciones y sitios web, lo que permite clasificar y controlar el tráfico de forma detallada.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics

Data Statistics ofrece un panel de tráfico intuitivo que identifica el uso de la red por aplicación y protocolo. Permite consultar tendencias históricas de 1 hora, 1 día y 7 días, muestra clasificaciones de uso, supervisa el tráfico de cada dispositivo y permite bloquear aplicaciones no deseadas con un solo clic.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter

Content Filter es una función inteligente de seguridad en línea basada en la clasificación DPI. Bloquea automáticamente sitios web dañinos y maliciosos para mantener la red limpia y segura. También admite reglas personalizadas para bloquear aplicaciones, dominios o direcciones IP específicos.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS

QoS (Quality of Service) optimiza la asignación del ancho de banda al dar prioridad a actividades importantes, como videollamadas o juegos, cuando la red está congestionada. De este modo, reduce la latencia y mejora el rendimiento general de la red.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM (Smart Queue Management) gestiona de forma inteligente el tráfico de red del router para minimizar la latencia y el «bufferbloat», lo que garantiza una experiencia más fluida en juegos y llamadas de voz.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control

Esta función, que antes se encontraba en el menú **Applications**, se ha trasladado al menú **Flow Control** en el firmware v4.9. Utiliza el DPI Engine actualizado para identificar y bloquear con precisión aplicaciones y contenido de red inadecuados, lo que permite aplicar restricciones de acceso basadas en el tráfico de manera más profesional y precisa.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

El firmware v4.9 mejora de forma integral la lógica de enrutamiento subyacente y la interfaz interactiva del módulo VPN. Corrige posibles conflictos de enrutamiento, simplifica la lógica de configuración y hace que el uso sea más intuitivo.

Los principales ajustes se describen a continuación.

### Túnel VPN aislado

Cada túnel VPN funciona como un grupo independiente, sin conmutación por error entre grupos. Una vez que el tráfico de red coincide con un grupo VPN específico, no cambia automáticamente a otros grupos VPN aunque falle el túnel actual, lo que garantiza un enrutamiento estable y predecible.

**Nota**: La política tradicional «Not Use VPN» se ha eliminado en el firmware v4.9. De este modo, se eliminan configuraciones redundantes y se evitan conflictos de enrutamiento provocados por varias reglas de túnel complejas.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### Conmutación por error de perfiles VPN

Un solo grupo de túneles VPN puede contener varios perfiles de configuración. Los usuarios pueden personalizar la prioridad de cada perfil dentro del mismo grupo, lo que permite una conmutación por error interna automática para mantener la conectividad VPN cuando falla un perfil.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Panel rediseñado

El VPN Dashboard se ha rediseñado por completo con una disposición más intuitiva. El estado de los túneles, los detalles de conexión y las entradas de configuración se presentan con mayor claridad, lo que mejora considerablemente la operación y la gestión diarias. Además, en la nueva arquitectura Kill Switch está habilitado de forma predeterminada para todos los túneles VPN, de modo que el tráfico permanezca protegido en todo momento.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

El firmware v4.9 introduce oficialmente el protocolo AmneziaWG 2.0, equipado con varios parámetros nuevos de ofuscación de tráfico. El protocolo actualizado evita eficazmente la detección por DPI y otros sistemas de identificación de tráfico, lo que mejora de forma significativa la ocultación de la conexión y la resistencia a interferencias. Esto permite establecer conexiones VPN estables y fiables en regiones con restricciones de red y en entornos de red complejos.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## Red IoT

En el firmware v4.9 puede crear una red Wi-Fi dedicada e independiente para dispositivos IoT inteligentes. Al estar aislada física y lógicamente de la red principal, evita la ocupación de recursos y los riesgos de seguridad derivados del acceso de los dispositivos IoT a la red principal. Esta optimización ofrece una compatibilidad más amplia con distintos clientes IoT inteligentes y mejora en conjunto la seguridad de la red doméstica.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL, abreviatura de Access Control List, es una función central de gestión de seguridad de red que permite crear reglas de acceso personalizadas para gestionar el tráfico interno y externo según los protocolos de conexión, las direcciones IP de los dispositivos y los puertos. Admite un control preciso de permisos para permitir o bloquear accesos específicos a la red. Cuando varias reglas ACL entran en conflicto, el sistema ejecuta automáticamente la regla de mayor prioridad para garantizar la aplicación correcta de la política.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL se diferencia de Port Forwarding en su objetivo principal: ACL se centra en la gestión de la seguridad de red mediante el control de los permisos de acceso de dispositivos y tráfico, mientras que Port Forwarding se utiliza para redirigir recursos de red. Para ello, reenvía el tráfico externo a dispositivos locales específicos y permite el acceso remoto a servicios de la red local.

## Interfaz Wireless

La interfaz Wireless se ha rediseñado por completo con una disposición más clara y un estilo visual unificado. Esto reduce la complejidad de uso y mejora considerablemente la sencillez y facilidad de uso de la interfaz.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## DNS cifrado

El DNS cifrado se ha ampliado para admitir más protocolos de cifrado, incluidos DoH, DoT y DoQ. Además, se han integrado más proveedores oficiales de DNS y se ha añadido la configuración manual de servidores DNS cifrados personalizados para satisfacer distintas necesidades de resolución segura de dominios.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node

Los routers GL.iNet ahora pueden funcionar como Tailscale Exit Node. Todo el tráfico saliente de Internet de los dispositivos del Tailnet puede enrutarse a través de la dirección IP pública del router, lo que permite gestionar de forma unificada y segura la salida de toda la red Tailscale. Consulte los detalles [aquí](../interface_guide/tailscale.md#run-exit-node).

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
