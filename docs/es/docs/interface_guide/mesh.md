# Mesh

**Nota**: Esta función se incorporó en el firmware v4.10.

Mango 2 (GL-MG1300) y Mudi 7 (GL-E5800) no admiten Mesh ni siquiera con el firmware v4.10 o posterior. Consulte [Modelos compatibles](#supported-models) para obtener más información.

---

En el menú lateral izquierdo del panel de administración web, vaya a **MESH**.

Mesh es una función basada en el estándar Wi-Fi EasyMesh™ que amplía la cobertura Wi-Fi en toda la vivienda y permite el roaming sin interrupciones. Si tiene varios routers GL.iNet, configure uno como router principal y el resto como nodos Mesh para disfrutar de roaming Wi-Fi continuo por toda la casa.

## Modelos compatibles {#supported-models}

??? "Modelos compatibles"
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Modelos no compatibles"
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
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)
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


## Configuración rápida

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

## Administrar los nodos

Una vez finalizada la configuración, ya no se podrá acceder al nodo Mesh mediante su dirección IP original. Puede administrar el router principal y todos los nodos Mesh desde el panel de administración del router principal.

### Ver los detalles de un nodo

En el panel de administración del router principal, vaya a **MESH** y haga clic en **Main Router** en la topología.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Puede consultar los detalles del router principal, incluidos el modelo, las direcciones IP y MAC, el tiempo de actividad y los clientes conectados.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Haga clic en **Mesh Node** en la topología.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Puede consultar los detalles del nodo Mesh, incluidos el modelo, las direcciones IP y MAC, la versión del firmware, el tiempo de actividad y los clientes conectados.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Editar un nodo Mesh

En el panel de administración del router principal, vaya a **MESH** y haga clic en **Mesh Node** en la topología.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

De forma predeterminada, cada nodo Mesh recibe el nombre «Node» seguido de los cuatro últimos dígitos de su dirección MAC. Haga clic en el icono de edición para cambiar el nombre del nodo Mesh.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Acceder a un nodo Mesh

En el panel de administración del router principal, vaya a **MESH** y haga clic en **Mesh Node** en la topología.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Haga clic en el icono de engranaje de la esquina superior derecha y seleccione **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Se le redirigirá a la página de inicio de sesión del nodo Mesh en la dirección IP asignada por el router principal. Ahora puede iniciar sesión en el nodo Mesh.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Añadir más nodos

Si es necesario, haga clic en **Add** en la esquina superior derecha de la topología para añadir más nodos.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
