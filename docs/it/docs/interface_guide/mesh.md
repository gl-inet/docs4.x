# Mesh

**Nota**: questa funzione è stata introdotta nel firmware v4.10.

Mango 2 (GL-MG1300) e Mudi 7 (GL-E5800) non supportano Mesh, neppure con il firmware v4.10 o successivo. Per i dettagli, consultare [Modelli supportati](#supported-models).

---

Nel menu a sinistra del pannello di amministrazione web, andare su **MESH**.

Mesh è una funzione basata sullo standard Wi-Fi EasyMesh™ che estende la copertura Wi‑Fi in tutta la casa e consente il roaming senza interruzioni. Se si dispone di più router GL.iNet, impostarne uno come router principale e gli altri come nodi Mesh.

## Modelli supportati {#supported-models}

??? "Modelli supportati"
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Modelli non supportati"
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

## Configurazione rapida

Nell'esempio seguente Flint 3 (GL‑BE9300) e Slate 7 (GL‑BE3600) vengono utilizzati per creare una rete Mesh.

**Flint 3** è il router principale, connesso a Internet, che gestisce tutti i nodi Mesh.

**Slate 7** è il nodo Mesh che estende la copertura Wi-Fi del router principale.

1. Accendere il nodo Mesh e posizionarlo vicino al router principale.

    Durante la prima configurazione, tenere il nodo accanto al router principale per velocizzare la scansione. Al termine, è possibile spostarlo a metà strada tra il router principale e la zona senza copertura Wi-Fi.

2. Accedere al pannello di amministrazione web del nodo Mesh, andare su **MESH** e fare clic su **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Il nodo diventa rilevabile e, prima di essere aggiunto alla rete Mesh, non dispone di una connessione di rete.

3. Accedere al pannello del router principale e andare su **INTERNET**. Connetterlo a Internet tramite Ethernet, Repeater, Tethering o Cellular.

4. Dopo aver configurato Internet, andare su **MESH** e fare clic su **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. La pagina mostra due metodi per aggiungere nodi Mesh: scansione Wi-Fi e backhaul Ethernet.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Selezionare la procedura corrispondente.

    ??? note "Wi-Fi Scan"

        Fare clic su **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Il router cerca tramite Wi-Fi i nodi Mesh nelle vicinanze. Selezionare i dispositivi da aggiungere e fare clic su **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Il nodo viene aggiunto alla rete Mesh. Fare clic su **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Collegare la porta WAN del nodo Mesh alla porta LAN del router principale con un cavo Ethernet. La rete di backhaul Ethernet verrà configurata automaticamente.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Dopo l'aggiunta del nodo, la topologia viene visualizzata nel pannello del router principale.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Gestire i nodi

Al termine della configurazione, il nodo Mesh non è più accessibile tramite il suo indirizzo IP originale. Il router principale e tutti i nodi possono essere gestiti dal pannello del router principale.

### Visualizzare i dettagli di un nodo

Nel pannello del router principale, andare su **MESH** e fare clic su **Main Router** nella topologia.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Vengono visualizzati modello, indirizzi IP e MAC, tempo di attività e client connessi.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Fare clic su **Mesh Node** nella topologia.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Vengono visualizzati modello, indirizzi IP e MAC, versione firmware, tempo di attività e client connessi del nodo.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Modificare un nodo Mesh

Nel pannello del router principale, andare su **MESH** e fare clic su **Mesh Node** nella topologia.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Per impostazione predefinita, ogni nodo si chiama "Node" seguito dalle ultime quattro cifre dell'indirizzo MAC. Fare clic sull'icona di modifica per rinominarlo.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Accedere a un nodo Mesh

Nel pannello del router principale, andare su **MESH** e fare clic su **Mesh Node** nella topologia.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Fare clic sull'icona a forma di ingranaggio nell'angolo superiore destro e selezionare **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Si verrà reindirizzati alla pagina di accesso del nodo, all'indirizzo IP assegnato dal router principale.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Aggiungere altri nodi

Se necessario, fare clic su **Add** nell'angolo superiore destro della topologia.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
