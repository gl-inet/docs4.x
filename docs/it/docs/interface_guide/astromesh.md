# AstroMesh

> Questa funzione è introdotta nel firmware v4.10.

AstroMesh è la tecnologia mesh globale proprietaria di GL.iNet, che combina EasyMesh e AstroWarp. A differenza dei sistemi mesh wireless tradizionali che funzionano solo in una rete locale, AstroMesh elimina i limiti geografici e permette di collegarsi alla rete domestica ovunque.

A casa, il router da viaggio agisce come un normale Mesh Node per estendere la copertura Wi-Fi con roaming fluido. Quando sei fuori, può passare automaticamente alla modalità Astro Node e sincronizzare tramite cloud le impostazioni Wi-Fi di casa, consentendo l’accesso remoto ai dispositivi LAN e instradando il traffico attraverso l’uscita della rete domestica. Plug-and-play e senza configurazioni complicate, AstroMesh offre un’esperienza Internet fluida sia a casa sia in viaggio.

## Configurazione rapida

In questo esempio vengono utilizzati Flint 3 (GL-BE9300) e Slate 7 (GL-BE3600) per creare una rete AstroMesh.

- **Flint 3**: Main Node, gateway Internet, gestore dei Mesh Nodes e uscita di rete per Astro Nodes remoti.
- **Slate 7**: Mesh Node per estendere la copertura locale con EasyMesh o la rete remota tramite AstroWarp.

Segui i passaggi riportati di seguito per completare la configurazione.

1. Accedi al Web Admin Panel di Flint 3 e vai su **INTERNET**. Collegalo a Internet tramite Ethernet, Repeater, Tethering o Cellular.
2. Vai su **ASTROMESH** e fai clic su **Main Node**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Aggiungi nodi tramite **Wi-Fi Scan** o **Pairing Code**.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    ??? note "Wi-Fi Scan"

        Prima della scansione, assicurati che:

        1. Il router da aggiungere sia acceso e vicino al router principale.
        2. Il router da aggiungere abbia AstroMesh abilitato e funzioni in modalità **Mesh Node**.
        ---

        Fai clic su **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        Nella finestra pop-up, fai clic su **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        Il router cerca i Mesh Nodes vicini tramite Wi-Fi.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Seleziona un nodo e fai clic su **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Il Mesh Node viene aggiunto ad AstroMesh. Fai clic su **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Nota**: una volta connesso, questo Mesh Node non sarà più accessibile tramite il suo indirizzo IP originale. Usa il nuovo indirizzo IP assegnato dal Main Node e gestisci tutti i nodi dall’Admin Panel del Main Node. Vedi [qui](#manage-nodes).

    ??? note "Pairing Code"

        Fai clic su **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Copia il codice di associazione generato dal Main Node.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Accedi al Web Admin Panel di Slate 7, vai su **AstroMesh** e fai clic su **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Inserisci il codice di associazione e fai clic su **Apply**.

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Il Mesh Node inizia a connettersi al Main Node. Fai clic su **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Nota**: una volta connesso, questo Mesh Node non sarà più accessibile tramite il suo indirizzo IP originale. Usa il nuovo indirizzo IP assegnato dal Main Node e gestisci tutti i nodi dall’Admin Panel del Main Node. Vedi [qui](#manage-nodes).

4. Una volta aggiunto il nodo alla rete AstroMesh, l’Admin Panel del Main Node mostra la topologia di rete, come illustrato di seguito.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    Anche l’Admin Panel del Mesh Node mostra lo stato della connessione, come illustrato di seguito.

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **Nota**: una volta aggiunto alla rete AstroMesh, il Mesh Node non sarà più accessibile tramite il suo indirizzo IP originale. Per accedervi di nuovo, usa il nuovo indirizzo IP assegnato dal Main Node. Gestisci tutti i nodi dall’Admin Panel del Main Node. Vedi [qui](#manage-nodes).

5. Quando porti il Mesh Node fuori casa, passa automaticamente alla modalità Astro Node.

## Gestire i nodi {#manage-nodes}

Gestisci AstroMesh dall’Admin Panel del Main Node.

### Visualizzare le informazioni del nodo

Fai clic su **Main Node** nella topologia AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Puoi visualizzare i dettagli del Main Node, inclusi modello, indirizzi IP e MAC, tempo di attività e client connessi.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Fai clic su **Mesh Node** nella topologia AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Puoi visualizzare i dettagli del Mesh Node, inclusi modello, indirizzi IP e MAC, versione firmware, tempo di attività e client connessi.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Modificare il Mesh Node

Fai clic su **Mesh Node** nella topologia AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Per impostazione predefinita, ogni Mesh Node viene chiamato "Node" seguito dalle ultime quattro cifre del suo indirizzo MAC. Fai clic sull’icona di modifica per rinominarlo.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Accedere al Mesh Node

Fai clic su **Mesh Node** nella topologia AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Fai clic sull’icona a forma di ingranaggio in alto a destra e seleziona **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Verrai reindirizzato alla pagina di accesso del Mesh Node. Inserisci la password amministratore per accedere al suo Admin Panel tramite l’indirizzo IP assegnato dal Main Node.

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
