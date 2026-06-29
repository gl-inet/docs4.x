# AstroMesh

> Questa funzione è introdotta nel firmware v4.10.

AstroMesh è la tecnologia mesh globale proprietaria di GL.iNet basata su EasyMesh. A differenza dei sistemi mesh wireless tradizionali che funzionano solo in una rete locale, AstroMesh elimina i limiti geografici e permette di collegarsi alla rete domestica ovunque.

A casa, il router da viaggio agisce come un normale Mesh Node per estendere la copertura Wi-Fi con roaming fluido. Quando sei fuori, può passare automaticamente alla modalità Astro Node e sincronizzare tramite cloud le impostazioni Wi-Fi di casa, consentendo l’accesso remoto ai dispositivi LAN e instradando il traffico attraverso l’uscita della rete domestica. Plug-and-play e senza configurazioni complicate, AstroMesh offre un’esperienza Internet fluida sia a casa sia in viaggio.

## Configurazione rapida

In questo esempio utilizziamo Flint 3 (GL-BE9300) e Slate 7 (GL-BE3600) per creare una rete AstroMesh.

- **Flint 3**: funge da Main Router, si connette a Internet e gestisce tutti i Mesh Nodes. Inoltre agisce come uscita di rete per tutti gli Astro Nodes remoti.
- **Slate 7**: funziona come Mesh Node che estende localmente la copertura Wi-Fi del Main Router oppure estende la rete domestica a siti remoti.

Segui i passaggi seguenti per completare la configurazione.

### Configurare il Main Router

1. Accedi al Web Admin Panel di Flint 3 e vai su **INTERNET**. Connettilo a Internet tramite uno dei tipi di connessione supportati: Ethernet, Repeater, Tethering o Cellular.

2. Vai su **ASTROMESH** e fai clic su **Main Router**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

### Configurare il Mesh Node

Accedi al Web Admin Panel di Slate 7. Vai su **ASTROMESH** e fai clic su **Mesh/Astro Node**.

![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

### Associazione

Aggiungi Mesh Nodes alla rete AstroMesh tramite **Wi-Fi Scan** o **Pairing Code**.

![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

Consulta le istruzioni corrispondenti di seguito.

??? note "Wi-Fi Scan"

    Prima della scansione, assicurati che:

    1. Il Mesh Node sia acceso e vicino al Main Router.
    2. Il Mesh Node abbia AstroMesh abilitato e funzioni in modalità **Mesh Node**.
     ---

    Accedi al Web Admin Panel di Flint 3 e vai su **ASTROMESH**. Fai clic su **Add nodes via Wi-Fi Scan**.

    ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

    Nella finestra pop-up, fai clic su **Scan**.

    ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

    Il router avvierà la scansione dei Mesh Nodes vicini tramite Wi-Fi.

    ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

    Seleziona un nodo e fai clic su **Add**.

    ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

    Il Mesh Node verrà aggiunto alla rete AstroMesh. Fai clic su **Finish**.

    ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

    **Nota**: quando un nodo entra nella rete AstroMesh, non sarà più accessibile tramite il suo indirizzo IP originale. Tutti i nodi possono essere gestiti dal Admin Panel del Main Router. Consulta [Gestire i Mesh Nodes](#manage-mesh-nodes) per i dettagli.

??? note "Pairing Code"

    Accedi al Web Admin Panel di Flint 3 e vai su **ASTROMESH**. Fai clic su **Add nodes via Pairing Code**.

    ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

    Il Main Router genererà un codice di associazione. Copia questo codice.

    ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

    Accedi al Web Admin Panel di Slate 7 e vai su **ASTROMESH**. Inserisci il codice di associazione copiato e fai clic su **Apply**.

    ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

    ***Nota**: il codice di associazione ha una validità limitata. Inseriscilo prima che scada.*

    Il Mesh Node inizierà a connettersi al Main Router. Fai clic su **Done**.

    ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

    **Nota**: quando un nodo entra nella rete AstroMesh, non sarà più accessibile tramite il suo indirizzo IP originale. Tutti i nodi possono essere gestiti dal Admin Panel del Main Router. Consulta [Gestire i Mesh Nodes](#manage-mesh-nodes) per i dettagli.

Dopo che i nodi sono stati aggiunti correttamente ad AstroMesh, nel Admin Panel del Main Router verrà visualizzata una topologia, come mostrato di seguito.

![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Gestire i Mesh Nodes {#manage-mesh-nodes}

Gestisci i Mesh Nodes dal Admin Panel del Main Router.

### Visualizzare le informazioni del nodo

Nel Admin Panel del Main Router, vai su **ASTROMESH** e fai clic su **Main Router** nella topologia AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Puoi visualizzare i dettagli del Main Router, inclusi modello, indirizzi IP e MAC, tempo di attività e client connessi.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Fai clic su **Mesh Node** nella topologia AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Puoi visualizzare i dettagli del Mesh Node, inclusi modello, indirizzi IP e MAC, versione firmware, tempo di attività e client connessi.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Modificare il Mesh Node

Nel Admin Panel del Main Router, vai su **ASTROMESH** e fai clic su **Mesh Node** nella topologia AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Per impostazione predefinita, ogni Mesh Node viene chiamato "Node" seguito dalle ultime quattro cifre del suo indirizzo MAC. Fai clic sull’icona di modifica per rinominare il Mesh Node.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Accedere al Mesh Node

Nel Admin Panel del Main Router, vai su **ASTROMESH** e fai clic su **Mesh Node** nella topologia AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Fai clic sull’icona a forma di ingranaggio in alto a destra e seleziona **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Verrai reindirizzato alla pagina di accesso del Mesh Node all’indirizzo IP assegnato dal Main Router. Inserisci la password amministratore per accedere.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

Dopo l’accesso, vai su **ASTROMESH** per visualizzare lo stato della connessione.

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### Aggiungere altri nodi

Per aggiungere altri nodi, fai clic su **Add** nell’angolo in alto a destra della topologia AstroMesh.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Gestire gli Astro Nodes

Quando sposti un Mesh Node fuori dalla rete domestica, passerà automaticamente alla modalità **Astro Node**.

Ad esempio, porta Slate 7 in un’altra posizione. Accendilo e seleziona la modalità **Mesh Node** sul touchscreen.

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

Rileverà l’ambiente di rete corrente, passerà automaticamente alla modalità **Astro Node** e avvierà la connessione.

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

Una volta connesso, mostrerà il suo indirizzo IP originale, che può essere utilizzato per accedere al suo Web Admin Panel.

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

Usa questo indirizzo IP per accedere al tuo Astro Node.

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

Dopo l’accesso, vai su **ASTROMESH** per visualizzare lo stato della connessione. La modalità di connessione predefinita è **Exit Node Mode**. Puoi passare a **Traffic Split Mode** secondo necessità.

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode**: in questa modalità, tutto il traffico dell’Astro Node viene instradato attraverso la rete domestica per accedere a Internet. L’IP pubblico dell’Astro Node corrisponderà all’indirizzo IP pubblico della rete domestica.

- **Traffic Split Mode**: in questa modalità, solo il traffico diretto alla rete domestica viene inoltrato al Main Router, mentre l’altro traffico Internet passa direttamente attraverso la WAN locale dell’Astro Node. Assicurati che l’Astro Node sia connesso a una rete Internet locale.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
