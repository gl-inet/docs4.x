# ACL

> La función ACL se introdujo en el firmware v4.9.

ACL, abreviatura de Access Control List, le permite crear reglas para gestionar el tráfico de red según los protocolos de conexión, las direcciones de los dispositivos y los puertos. Controla si se permite o se bloquea el acceso a la red. Si varias reglas ACL entran en conflicto, el sistema aplica la que tenga mayor prioridad.

ACL funciona de forma distinta a Port Forwarding: ACL permite o bloquea principalmente el acceso a la red con fines de seguridad, mientras que Port Forwarding redirige tráfico externo a dispositivos concretos de su red local para habilitar el acceso remoto a servicios locales.

---

En el lado izquierdo del panel de administración web, vaya a **SECURITY** -> **ACL**.

Haga clic en el botón **Add Rule** situado a la derecha.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Cree la regla ACL en la ventana emergente y, a continuación, haga clic en **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: Introduzca un nombre personalizado para la regla.

- **Protocol**: Especifique qué tipo de tráfico de red cubre la regla. Seleccione un protocolo de conexión entre `Any`, `TCP`, `UDP`, `TCP+UDP` e `ICMP`.

- **IP Type**: Define el formato de dirección IP del tráfico de red. Seleccione el tipo entre `IPv4 & IPv6`, `IPv4` e `IPv6`.

- **Source Zone**: Seleccione la zona de red de donde proviene el tráfico. Opciones disponibles: `LAN`, `Guest`, `IoT` y `WAN`.

- **Source Address**: (Opcional) Limite la regla a dispositivos o direcciones IP de origen concretos. Puede seleccionar una dirección de origen en la lista desplegable.

- **Destination Zone**: Indica hacia dónde se dirige el tráfico de red. Seleccione la zona de red de destino. Opciones disponibles: `LAN`, `Guest`, `IoT` y `WAN`.

- **Destination Address**: (Opcional) Limite la regla a dispositivos o direcciones IP de destino concretos. Puede seleccionar una dirección de destino en la lista desplegable.

- **Action**: Elija si el tráfico que coincida con esta regla se debe `Accept` o `Block`.

- **Enable**: Active o desactive esta regla.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
