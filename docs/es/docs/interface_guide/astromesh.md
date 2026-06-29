# AstroMesh

> Esta función se introdujo en el firmware v4.10.

AstroMesh es la tecnología mesh global propietaria de GL.iNet basada en EasyMesh. A diferencia de los sistemas mesh inalámbricos convencionales que solo funcionan dentro de una red local, AstroMesh elimina las restricciones geográficas para conectarle a su red doméstica desde cualquier lugar.

En casa, el router de viaje actúa como un Mesh Node normal para ampliar la cobertura Wi-Fi con itinerancia fluida. Al salir, puede cambiar automáticamente al modo Astro Node y sincronizar por la nube los ajustes Wi-Fi de casa, permitiendo acceder de forma remota a los dispositivos LAN y enrutar el tráfico por la salida de la red doméstica. Con funcionamiento plug-and-play y sin configuración complicada, AstroMesh ofrece una experiencia de Internet fluida tanto en casa como durante los viajes.

## Configuración rápida

En este ejemplo se utilizan Flint 3 (GL-BE9300) y Slate 7 (GL-BE3600) para crear una red AstroMesh.

- **Flint 3**: actúa como Main Router, se conecta a Internet y administra todos los Mesh Nodes. También funciona como salida de red para todos los Astro Nodes remotos.
- **Slate 7**: funciona como Mesh Node que amplía localmente la cobertura Wi-Fi del Main Router o extiende la red doméstica a ubicaciones remotas.

Siga los pasos siguientes para completar la configuración.

### Configurar el Main Router

1. Inicie sesión en el Web Admin Panel de Flint 3 y vaya a **INTERNET**. Conéctelo a Internet mediante cualquier tipo de conexión compatible: Ethernet, Repeater, Tethering o Cellular.

2. Vaya a **ASTROMESH** y haga clic en **Main Router**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

### Configurar el Mesh Node

Inicie sesión en el Web Admin Panel de Slate 7. Vaya a **ASTROMESH** y haga clic en **Mesh/Astro Node**.

![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

### Emparejamiento

Añada Mesh Nodes a su red AstroMesh mediante **Wi-Fi Scan** o **Pairing Code**.

![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

Consulte las instrucciones correspondientes a continuación.

??? note "Wi-Fi Scan"

    Antes de escanear, asegúrese de que:

    1. El Mesh Node esté encendido y cerca del router principal.
    2. El Mesh Node tenga AstroMesh habilitado y funcione en modo **Mesh Node**.
     ---

    Inicie sesión en el Web Admin Panel de Flint 3 y vaya a **ASTROMESH**. Haga clic en **Add nodes via Wi-Fi Scan**.

    ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

    En la ventana emergente, haga clic en **Scan**.

    ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

    El router buscará Mesh Nodes cercanos mediante Wi-Fi.

    ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

    Seleccione un nodo y haga clic en **Add**.

    ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

    El Mesh Node se añadirá a la red AstroMesh. Haga clic en **Finish**.

    ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

    **Nota**: Cuando un nodo se une a la red AstroMesh, ya no será accesible mediante su dirección IP original. Todos los nodos pueden administrarse desde el Admin Panel del Main Router. Consulte [Administrar Mesh Nodes](#manage-mesh-nodes) para obtener más detalles.

??? note "Pairing Code"

    Inicie sesión en el Web Admin Panel de Flint 3 y vaya a **ASTROMESH**. Haga clic en **Add nodes via Pairing Code**.

    ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

    El Main Router generará un código de emparejamiento. Copie este código.

    ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

    Inicie sesión en el Web Admin Panel de Slate 7 y vaya a **ASTROMESH**. Introduzca el código de emparejamiento copiado y haga clic en **Apply**.

    ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

    ***Nota**: El código de emparejamiento tiene tiempo limitado. Introdúzcalo antes de que caduque.*

    El Mesh Node empezará a conectarse al Main Router. Haga clic en **Done**.

    ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

    **Nota**: Cuando un nodo se une a la red AstroMesh, ya no será accesible mediante su dirección IP original. Todos los nodos pueden administrarse desde el Admin Panel del Main Router. Consulte [Administrar Mesh Nodes](#manage-mesh-nodes) para obtener más detalles.

Una vez que los nodos se hayan añadido correctamente a AstroMesh, aparecerá una topología en el Admin Panel del Main Router, como se muestra a continuación.

![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Administrar Mesh Nodes {#manage-mesh-nodes}

Administre sus Mesh Nodes desde el Admin Panel del Main Router.

### Ver información del nodo

En el Admin Panel del Main Router, vaya a **ASTROMESH** y haga clic en **Main Router** en la topología de AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Puede ver los detalles del Main Router, como modelo, direcciones IP y MAC, tiempo de actividad y clientes conectados.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Haga clic en **Mesh Node** en la topología de AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Puede ver los detalles del Mesh Node, como modelo, direcciones IP y MAC, versión de firmware, tiempo de actividad y clientes conectados.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Editar Mesh Node

En el Admin Panel del Main Router, vaya a **ASTROMESH** y haga clic en **Mesh Node** en la topología de AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Cada Mesh Node se nombra de forma predeterminada como "Node" seguido de los últimos cuatro dígitos de su dirección MAC. Haga clic en el icono de edición para cambiarle el nombre.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Acceder al Mesh Node

En el Admin Panel del Main Router, vaya a **ASTROMESH** y haga clic en **Mesh Node** en la topología de AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Haga clic en el icono de engranaje en la esquina superior derecha y seleccione **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Se le redirigirá a la página de inicio de sesión del Mesh Node en la dirección IP asignada por el Main Router. Introduzca su contraseña de administrador para iniciar sesión.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

Después de iniciar sesión, vaya a **ASTROMESH** para ver el estado de conexión.

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### Añadir más nodos

Para añadir más nodos, haga clic en **Add** en la esquina superior derecha de la topología de AstroMesh.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Administrar Astro Nodes

Cuando mueva un Mesh Node fuera de su red doméstica, cambiará automáticamente al modo **Astro Node**.

Por ejemplo, lleve el Slate 7 a otra ubicación. Enciéndalo y seleccione el modo **Mesh Node** en la pantalla táctil.

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

Detectará el entorno de red actual, cambiará automáticamente al modo **Astro Node** e iniciará la conexión.

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

Una vez conectado, mostrará su dirección IP original, que puede usarse para acceder a su Web Admin Panel.

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

Use esta dirección IP para iniciar sesión en su Astro Node.

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

Después de iniciar sesión, vaya a **ASTROMESH** para ver el estado de conexión. El modo de conexión predeterminado es **Exit Node Mode**. Puede cambiar a **Traffic Split Mode** según sea necesario.

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode**: En este modo, todo el tráfico del Astro Node se enruta a través de su red doméstica para acceder a Internet. La IP pública del Astro Node coincidirá con la dirección IP pública de su red doméstica.

- **Traffic Split Mode**: En este modo, solo el tráfico dirigido a su red doméstica se reenvía al Main Router, mientras que el resto del tráfico de Internet pasa directamente por la WAN local del Astro Node. Asegúrese de que el Astro Node esté conectado a una red local con Internet.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
