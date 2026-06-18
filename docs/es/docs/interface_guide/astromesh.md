# AstroMesh

> Esta función se introdujo en el firmware v4.10.

AstroMesh es la tecnología mesh global propietaria de GL.iNet, que combina EasyMesh y AstroWarp. A diferencia de los sistemas mesh inalámbricos convencionales que solo funcionan dentro de una red local, AstroMesh elimina las restricciones geográficas para conectarle a su red doméstica desde cualquier lugar.

En casa, el router de viaje actúa como un Mesh Node normal para ampliar la cobertura Wi-Fi con itinerancia fluida. Al salir, puede cambiar automáticamente al modo Astro Node y sincronizar por la nube los ajustes Wi-Fi de casa, permitiendo acceder de forma remota a los dispositivos LAN y enrutar el tráfico por la salida de la red doméstica. Con funcionamiento plug-and-play y sin configuración complicada, AstroMesh ofrece una experiencia de Internet fluida tanto en casa como durante los viajes.

## Configuración rápida

En este ejemplo se utilizan Flint 3 (GL-BE9300) y Slate 7 (GL-BE3600) para crear una red AstroMesh.

- **Flint 3**: Main Node, puerta de enlace a Internet, gestor de Mesh Nodes y salida de red para Astro Nodes remotos.
- **Slate 7**: Mesh Node para ampliar la cobertura local con EasyMesh o extender la red de forma remota mediante AstroWarp.

Siga los pasos siguientes para completar la configuración.

1. Inicie sesión en el Web Admin Panel de Flint 3 y vaya a **INTERNET**. Conéctelo a Internet mediante Ethernet, Repeater, Tethering o Cellular.
2. Vaya a **ASTROMESH** y haga clic en **Main Node**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Añada nodos mediante **Wi-Fi Scan** o **Pairing Code**.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    ??? note "Wi-Fi Scan"

        Antes de escanear, asegúrese de que:

        1. El router que se va a añadir esté encendido y cerca del router principal.
        2. El router que se va a añadir tenga AstroMesh habilitado y funcione en modo **Mesh Node**.
        ---

        Haga clic en **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        En la ventana emergente, haga clic en **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        El router buscará Mesh Nodes cercanos mediante Wi-Fi.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Seleccione un nodo y haga clic en **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        El Mesh Node se añadirá a AstroMesh. Haga clic en **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Nota**: Una vez conectado, este Mesh Node ya no será accesible mediante su dirección IP original. Use la nueva dirección IP asignada por el Main Node y administre todos los nodos desde el Admin Panel del Main Node. Consulte [aquí](#manage-nodes).

    ??? note "Pairing Code"

        Haga clic en **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Copie el código de emparejamiento generado por el Main Node.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Inicie sesión en el Web Admin Panel de Slate 7, vaya a **AstroMesh** y haga clic en **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Introduzca el código de emparejamiento y haga clic en **Apply**.

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        El Mesh Node empezará a conectarse al Main Node. Haga clic en **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Nota**: Una vez conectado, este Mesh Node ya no será accesible mediante su dirección IP original. Use la nueva dirección IP asignada por el Main Node y administre todos los nodos desde el Admin Panel del Main Node. Consulte [aquí](#manage-nodes).

4. Una vez añadido el nodo a la red AstroMesh, el Admin Panel del Main Node mostrará la topología de red, como se muestra a continuación.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    El Admin Panel del Mesh Node también mostrará el estado de conexión, como se muestra a continuación.

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **Nota**: Una vez añadido a la red AstroMesh, el Mesh Node ya no será accesible mediante su dirección IP original. Para acceder a él de nuevo, utilice la nueva dirección IP que recibe del Main Node. Administre todos los nodos desde el Admin Panel del Main Node. Consulte [aquí](#manage-nodes).

5. Cuando lleve el Mesh Node fuera de casa, cambiará automáticamente al modo Astro Node.

## Administrar nodos {#manage-nodes}

Administre AstroMesh desde el Admin Panel del Main Node.

### Ver información del nodo

Haga clic en **Main Node** en la topología de AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Puede ver los detalles del Main Node, como modelo, direcciones IP y MAC, tiempo de actividad y clientes conectados.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Haga clic en **Mesh Node** en la topología de AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Puede ver los detalles del Mesh Node, como modelo, direcciones IP y MAC, versión de firmware, tiempo de actividad y clientes conectados.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Editar Mesh Node

Haga clic en **Mesh Node** en la topología de AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Cada Mesh Node se nombra de forma predeterminada como "Node" seguido de los últimos cuatro dígitos de su dirección MAC. Haga clic en el icono de edición para cambiarle el nombre.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Acceder al Mesh Node

Haga clic en **Mesh Node** en la topología de AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Haga clic en el icono de engranaje en la esquina superior derecha y seleccione **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Se le redirigirá a la página de inicio de sesión del Mesh Node. Introduzca la contraseña de administrador para acceder a su Admin Panel mediante la dirección IP asignada por el Main Node.

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
