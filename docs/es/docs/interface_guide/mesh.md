# Mesh {#mesh}

**Nota**: Esta función se incorporó en el firmware v4.10.

Mango 2 (GL-MG1300) y Mudi 7 (GL-E5800) no admiten Mesh ni siquiera con el firmware v4.10 o posterior. Consulte [Modelos compatibles](#supported-models) para obtener más información.

---

En el menú lateral izquierdo del panel de administración web, vaya a **MESH**.

Mesh es una función basada en el estándar Wi-Fi EasyMesh™ que amplía la cobertura Wi-Fi en toda la vivienda y permite el roaming sin interrupciones. Si tiene varios routers GL.iNet, configure uno como router principal y el resto como nodos Mesh para disfrutar de roaming Wi-Fi continuo por toda la casa.

## Comparación de los modos Mesh, Extender y Access Point {#mesh-vs-extender-vs-access-point-mode}

Los tres modos pueden ampliar la cobertura Wi-Fi. Las principales diferencias son cómo se conectan al router principal y cómo se configuran y gestionan los dispositivos. El **backhaul** es la conexión entre el router principal y un extensor, un punto de acceso o un nodo Mesh.

Esta tabla compara los modos independientes Extender y Access Point de GL.iNet con su implementación Mesh.

| Función | Modo Extender | Modo Access Point | Modo Mesh |
|---|---|---|---|
| **Backhaul inalámbrico** | ✅ Compatible | ❌ No se utiliza | ✅ Compatible |
| **Backhaul Ethernet** | ❌ No se utiliza en este modo | ✅ Compatible | ✅ Compatible |
| **Backhaul dúplex completo** | ❌ Wi-Fi es semidúplex | ✅ Ethernet | ✅ Solo Ethernet; el backhaul inalámbrico sigue siendo semidúplex |
| **Backhaul inalámbrico de 2.4/5 GHz** | ⚠️ Las bandas disponibles dependen del modelo y el firmware | ❌ No aplicable | ⚠️ Las bandas disponibles dependen del modelo y el firmware |
| **Backhaul inalámbrico de 6 GHz** | ⚠️ Depende del modelo y el firmware | ❌ No aplicable | 🔜 Próximamente |
| **Roaming Wi-Fi** | ✅ Controlado por el cliente | ✅ Controlado por el cliente | ✅ Controlado por el cliente, con asistencia 802.11k/v |
| **Sincronización automática de la configuración Wi-Fi** | ❌ Configuración por separado | ❌ Configuración por separado | ✅ Desde el router principal |
| **Gestión centralizada de nodos** | ❌ Configuración por separado | ❌ Configuración por separado | ✅ A través del router principal |
| **Topología de red y vista general de clientes** | ❌ Sin vista general de toda la red Mesh | ❌ Sin vista general de toda la red Mesh | ✅ Disponible en el router principal |
| **Ampliación con gestión centralizada** | ❌ Extensores independientes | ❌ Puntos de acceso independientes | ✅ Un router principal y hasta ocho nodos |
| **Saltos inalámbricos con gestión centralizada** | ❌ Sin gestión Mesh | ❌ No aplicable | ✅ Hasta tres saltos inalámbricos |
| **Cambio automático entre backhaul cableado e inalámbrico** | ❌ Sin cambio gestionado por Mesh | ❌ Sin cambio gestionado por Mesh | ✅ Prioriza Ethernet |
| **Uso más adecuado** | Ampliación sencilla de la cobertura inalámbrica | Ampliación de cobertura donde hay Ethernet | Cobertura coordinada con conexiones cableadas, inalámbricas o mixtas |

✅ Compatible · ❌ No compatible o no aplicable en este modo · ⚠️ Depende del hardware, el firmware o la configuración · 🔜 Función prevista

Mesh sincroniza las configuraciones Wi-Fi compatibles de las redes principal, de invitados, IoT y MLO. También ofrece gestión centralizada de nodos, que incluye reiniciar, eliminar y actualizar los nodos GL.iNet compatibles. Se pueden añadir nodos mediante búsqueda Wi-Fi, conexión Ethernet o un botón Mesh/WPS, cuando esté disponible. La gestión del backhaul incluye prioridad de Ethernet, cambio entre conexión cableada e inalámbrica y prevención de bucles.

### Comprender las diferencias de rendimiento {#understanding-performance-differences}

#### Modo Extender {#extender-mode}

El dispositivo se conecta a una red Wi-Fi existente. La radio utilizada para la conexión ascendente sigue el canal del router principal. Los clientes que utilizan la misma radio también usan ese canal, por lo que el tráfico ascendente y el de los clientes comparten tiempo de transmisión.

En los modelos multibanda compatibles, las radios independientes pueden seguir atendiendo a clientes en otras bandas. Por ejemplo, un extensor puede conectarse al router principal por 2.4 GHz y atender a los clientes mediante su radio independiente de 5 GHz. Esas dos conexiones no compiten por el tiempo de transmisión del mismo canal. Las combinaciones disponibles dependen del modelo y el firmware; el modo Extender no está limitado de forma inherente al funcionamiento en una sola banda.

El mismo requisito de canal ascendente se aplica a la función de conexión Repeater de GL.iNet, aunque el funcionamiento de Repeater y el modo de red independiente Extender difieren en otros aspectos.

#### Mesh inalámbrico {#wireless-mesh}

En la configuración Mesh tribanda probada, el nodo utiliza **5 GHz para el backhaul inalámbrico**. El canal de 5 GHz del nodo sigue al router principal y no puede cambiarse de forma independiente, mientras que sus **canales independientes de 2.4 GHz y 6 GHz se pueden seguir configurando por separado**. Se trata de ajustes de canal, no de una indicación de las bandas a las que pueden conectarse los clientes. Cambiar un canal orientado a los clientes no modifica la banda del backhaul.

Por tanto, el efecto sobre el rendimiento depende de cómo se conecte el cliente:

- **Dispositivos conectados por 5 GHz:** si un teléfono, portátil u otro dispositivo se conecta al Wi-Fi de 5 GHz del nodo Mesh mientras esa misma radio transporta el backhaul inalámbrico, las conexiones comparten tiempo de transmisión. Que el canal de 5 GHz del nodo esté bloqueado no impide necesariamente que los clientes se conecten a esa banda.
- **Dispositivos conectados por 2.4 GHz o 6 GHz:** cuando estos clientes utilizan una radio distinta de la del backhaul inalámbrico de 5 GHz, los dos enlaces no sufren la penalización del reenvío en el mismo canal.

Esto describe la configuración probada, no todos los modelos Mesh compatibles. El reenvío mediante radios independientes no es exclusivo de Mesh, y cambiar de Extender a Mesh no mejora automáticamente el rendimiento.

#### Modo Access Point y Mesh cableado {#access-point-mode-and-wired-mesh}

Ambos utilizan Ethernet para conectarse al router principal. El backhaul Ethernet funciona en dúplex completo y evita transmitir tráfico de backhaul por Wi-Fi. Las conexiones Wi-Fi de los clientes siguen siendo semidúplex. Con hardware y condiciones comparables, el modo Access Point y Mesh cableado pueden ofrecer un rendimiento similar; Mesh añade configuración y gestión coordinadas.

Mesh prioriza el backhaul Ethernet y permite cambiar al inalámbrico cuando hay una conexión inalámbrica adecuada disponible. En la configuración probada, el canal de 5 GHz del nodo permanece alineado con el del router principal incluso cuando el backhaul Ethernet está activo. Esto no significa que el backhaul inalámbrico esté transportando el tráfico. Ethernet elimina el salto inalámbrico del backhaul de datos, pero los nodos y clientes cercanos que utilizan el mismo canal Wi-Fi pueden seguir compitiendo por el tiempo de transmisión.

!!! note "Backhaul Mesh de 6 GHz — Próximamente"

    El backhaul Mesh de 6 GHz requerirá hardware compatible con 6 GHz tanto en el router principal como en el nodo Mesh, junto con firmware que lo admita. No dé por hecho que todos los modelos compatibles con Mesh admitirán esta función.

    Esto es diferente de conectar un cliente a la red Wi-Fi de 6 GHz existente de un nodo. Con backhaul de 6 GHz, una radio independiente de 5 GHz podría atender a los clientes sin compartir el tiempo de transmisión del canal de backhaul. Una radio solo está dedicada al backhaul cuando se reserva para ese fin y no atiende también a clientes.

!!! important "Las radios independientes no convierten Wi-Fi en dúplex completo"

    Cada enlace Wi-Fi sigue siendo semidúplex. El reenvío mediante radios independientes evita compartir un canal entre los enlaces de backhaul y de clientes, pero no elimina otras interferencias, la contención ni las limitaciones de varios saltos. El rendimiento de extremo a extremo sigue limitado por el enlace más lento y las condiciones de la red.

## Modelos compatibles {#supported-models}

??? "Modelos compatibles"
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Modelos no compatibles"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)


## Configuración rápida {#quick-setup}

En el siguiente ejemplo se utilizan Flint 3 (GL‑BE9300) y Slate 7 (GL‑BE3600) para crear una red Mesh.

**Flint 3** es el router principal que se conecta a Internet y administra todos los nodos Mesh.

**Slate 7** es el nodo Mesh que amplía la cobertura Wi-Fi del router principal.

1. Encienda el nodo Mesh y colóquelo cerca del router principal.

    Durante la configuración inicial, mantenga el nodo Mesh junto al router principal para que pueda detectarlo rápidamente. Cuando finalice la configuración, puede colocarlo a medio camino entre el router principal y la zona sin cobertura Wi-Fi para ampliar la cobertura.

2. Inicie sesión en el panel de administración web del nodo Mesh, vaya a **MESH** y haga clic en **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    El nodo pasará a ser detectable y no tendrá conexión de red hasta que se añada a la red Mesh.

3. Inicie sesión en el panel de administración web del router principal y vaya a **INTERNET**. Conéctelo a Internet mediante cualquiera de los tipos de conexión compatibles: Ethernet, Repeater, Tethering o Cellular.

4. Después de configurar la conexión a Internet, vaya a **MESH** y haga clic en **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. La página muestra dos formas de añadir nodos Mesh: Wi-Fi Scan y Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Seleccione a continuación el tutorial correspondiente para añadir los nodos Mesh.

    ??? note "Wi-Fi Scan"

        Haga clic en **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        El router comenzará a buscar por Wi-Fi los nodos Mesh cercanos. Seleccione los dispositivos que desea añadir y haga clic en **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        El nodo Mesh se añadirá a la red Mesh. Haga clic en **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Conecte el puerto WAN del nodo Mesh al puerto LAN del router principal mediante un cable Ethernet. Se configurará automáticamente una red Ethernet Backhaul.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Cuando se haya añadido el nodo Mesh, la topología aparecerá en el panel de administración del router principal.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Administrar los nodos {#manage-nodes}

Una vez finalizada la configuración, ya no se podrá acceder al nodo Mesh mediante su dirección IP original. Puede administrar el router principal y todos los nodos Mesh desde el panel de administración del router principal.

### Ver los detalles de un nodo {#view-node-details}

En el panel de administración del router principal, vaya a **MESH** y haga clic en **Main Router** en la topología.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Puede consultar los detalles del router principal, incluidos el modelo, las direcciones IP y MAC, el tiempo de actividad y los clientes conectados.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Haga clic en **Mesh Node** en la topología.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Puede consultar los detalles del nodo Mesh, incluidos el modelo, las direcciones IP y MAC, la versión del firmware, el tiempo de actividad y los clientes conectados.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Editar un nodo Mesh {#edit-mesh-node}

En el panel de administración del router principal, vaya a **MESH** y haga clic en **Mesh Node** en la topología.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

De forma predeterminada, cada nodo Mesh recibe el nombre «Node» seguido de los cuatro últimos dígitos de su dirección MAC. Haga clic en el icono de edición para cambiar el nombre del nodo Mesh.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Acceder a un nodo Mesh {#access-mesh-node}

En el panel de administración del router principal, vaya a **MESH** y haga clic en **Mesh Node** en la topología.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Haga clic en el icono de engranaje de la esquina superior derecha y seleccione **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Se le redirigirá a la página de inicio de sesión del nodo Mesh en la dirección IP asignada por el router principal. Ahora puede iniciar sesión en el nodo Mesh.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Añadir más nodos {#add-more-nodes}

Si es necesario, haga clic en **Add** en la esquina superior derecha de la topología para añadir más nodos.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
