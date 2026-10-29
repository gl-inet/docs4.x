# Mesh {#mesh}

**Nota**: questa funzione è stata introdotta nel firmware v4.10.

Mango 2 (GL-MG1300) e Mudi 7 (GL-E5800) non supportano Mesh, neppure con il firmware v4.10 o successivo. Per i dettagli, consultare [Modelli supportati](#supported-models).

---

Nel menu a sinistra del pannello di amministrazione web, andare su **MESH**.

Mesh è una funzione basata sullo standard Wi-Fi EasyMesh™ che estende la copertura Wi‑Fi in tutta la casa e consente il roaming senza interruzioni. Se si dispone di più router GL.iNet, impostarne uno come router principale e gli altri come nodi Mesh.

Non si è sicuri di quale modalità scegliere? Consultare [Confronto tra le modalità Mesh, Extender e Access Point](#mesh-vs-extender-vs-access-point-mode).

## Modelli supportati {#supported-models}

??? "Modelli supportati"
    - ※GL-BE14000 (Flint 4)
    - ※GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - ※GL-XE3000 (Puli AX)
    - ※GL-X3000 (Spitz AX)
    - GL-MT3000 (Beryl AX)

    **Nota**: i modelli contrassegnati con ※ supportano Mesh nel firmware Beta.

??? "Modelli non supportati"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
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

## Configurazione rapida {#quick-setup}

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

## Gestire i nodi {#manage-nodes}

Al termine della configurazione, il nodo Mesh non è più accessibile tramite il suo indirizzo IP originale. Il router principale e tutti i nodi possono essere gestiti dal pannello del router principale.

### Visualizzare i dettagli di un nodo {#view-node-details}

Nel pannello del router principale, andare su **MESH** e fare clic su **Main Router** nella topologia.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Vengono visualizzati modello, indirizzi IP e MAC, tempo di attività e client connessi.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Fare clic su **Mesh Node** nella topologia.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Vengono visualizzati modello, indirizzi IP e MAC, versione firmware, tempo di attività e client connessi del nodo.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Modificare un nodo Mesh {#edit-mesh-node}

Nel pannello del router principale, andare su **MESH** e fare clic su **Mesh Node** nella topologia.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Per impostazione predefinita, ogni nodo si chiama "Node" seguito dalle ultime quattro cifre dell'indirizzo MAC. Fare clic sull'icona di modifica per rinominarlo.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Accedere a un nodo Mesh {#access-mesh-node}

Nel pannello del router principale, andare su **MESH** e fare clic su **Mesh Node** nella topologia.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Fare clic sull'icona a forma di ingranaggio nell'angolo superiore destro e selezionare **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Si verrà reindirizzati alla pagina di accesso del nodo, all'indirizzo IP assegnato dal router principale.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Aggiungere altri nodi {#add-more-nodes}

Se necessario, fare clic su **Add** nell'angolo superiore destro della topologia.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

## Confronto tra le modalità Mesh, Extender e Access Point {#mesh-vs-extender-vs-access-point-mode}

Tutte e tre le modalità possono estendere la copertura Wi-Fi. Le differenze principali riguardano il collegamento al router principale e la configurazione e gestione dei dispositivi. Il **backhaul** è il collegamento tra il router principale e un extender, un access point o un nodo Mesh.

Questa tabella confronta le modalità autonome Extender e Access Point di GL.iNet con la sua implementazione Mesh.

| Funzionalità | Modalità Extender | Modalità Access Point | Modalità Mesh |
|---|---|---|---|
| **Backhaul wireless** | ✅ Supportato | ❌ Non applicabile | ✅ Supportato |
| **Backhaul Ethernet** | ❌ Non utilizzato in questa modalità | ✅ Supportato | ✅ Supportato |
| **Backhaul full-duplex** | ❌ Il Wi-Fi è half-duplex | ✅ Ethernet | ✅ Solo Ethernet; il backhaul wireless resta half-duplex |
| **Backhaul wireless a 2.4/5 GHz** | ⚠️ Le bande disponibili dipendono dal modello e dal firmware | ❌ Non applicabile | ⚠️ Le bande disponibili dipendono dal modello e dal firmware |
| **Backhaul wireless a 6 GHz** | ⚠️ Dipende dal modello e dal firmware | ❌ Non applicabile | 🔜 In arrivo |
| **Roaming Wi-Fi** | ✅ Controllato dal client | ✅ Controllato dal client | ✅ Controllato dal client, con assistenza 802.11k/v |
| **Sincronizzazione automatica delle impostazioni Wi-Fi** | ❌ Configurazione separata | ❌ Configurazione separata | ✅ Dal router principale |
| **Gestione centralizzata dei nodi** | ❌ Configurazione separata | ❌ Configurazione separata | ✅ Tramite il router principale |
| **Topologia di rete e panoramica dei client** | ❌ Nessuna panoramica dell’intera rete Mesh | ❌ Nessuna panoramica dell’intera rete Mesh | ✅ Disponibile sul router principale |
| **Espansione gestita centralmente** | ❌ Extender indipendenti | ❌ Access point indipendenti | ✅ Un router principale e fino a otto nodi |
| **Salti wireless gestiti centralmente** | ❌ Non gestiti da Mesh | ❌ Non applicabile | ✅ Fino a tre salti wireless |
| **Passaggio automatico tra backhaul cablato e wireless** | ❌ Nessuna commutazione gestita da Mesh | ❌ Nessuna commutazione gestita da Mesh | ✅ Priorità a Ethernet |
| **Ideale per** | Semplice estensione della copertura wireless | Estensione della copertura dove è disponibile Ethernet | Copertura coordinata con collegamenti cablati, wireless o misti |

✅ Supportato · ❌ Non supportato o non applicabile in questa modalità · ⚠️ Dipende da hardware, firmware o configurazione · 🔜 Funzionalità prevista

Mesh sincronizza le impostazioni Wi-Fi supportate delle reti principale, ospite, IoT e MLO. Offre inoltre la gestione centralizzata dei nodi, inclusi riavvio, rimozione e aggiornamento dei nodi GL.iNet supportati. I nodi possono essere aggiunti tramite scansione Wi-Fi, collegamento Ethernet o pulsante Mesh/WPS, ove supportato. La gestione del backhaul comprende la priorità a Ethernet, il passaggio tra collegamenti cablati e wireless e la prevenzione dei loop.

### Comprendere le differenze di prestazioni {#understanding-performance-differences}

#### Modalità Extender {#extender-mode}

Il dispositivo si connette a una rete Wi-Fi esistente. La radio usata per il collegamento a monte segue il canale del router principale. Anche i client che utilizzano la stessa radio usano quel canale, quindi il traffico a monte e quello dei client condividono il tempo di trasmissione.

Sui modelli multibanda supportati, radio separate possono comunque servire i client su altre bande. Ad esempio, un extender può collegarsi a monte tramite 2.4 GHz e servire i client con la propria radio separata a 5 GHz. Questi due collegamenti non competono per il tempo di trasmissione dello stesso canale. Le combinazioni disponibili dipendono dal modello e dal firmware; la modalità Extender non è intrinsecamente limitata al funzionamento su una sola banda.

Lo stesso requisito relativo al canale a monte si applica alla funzione di connessione Repeater di GL.iNet, sebbene il funzionamento Repeater e la modalità di rete autonoma Extender differiscano sotto altri aspetti.

#### Mesh wireless {#wireless-mesh}

Nella configurazione Mesh a tre bande testata, il nodo utilizza **5 GHz per il backhaul wireless**. Il canale a 5 GHz del nodo segue quello del router principale e non può essere modificato indipendentemente, mentre le **impostazioni dei canali separati a 2.4 GHz e 6 GHz restano configurabili indipendentemente**. Si tratta di impostazioni dei canali, non di un’indicazione delle bande a cui possono connettersi i client. Modificare un canale destinato ai client non cambia la banda del backhaul.

L’effetto sulle prestazioni dipende quindi dal modo in cui si connette il client:

- **Dispositivi connessi tramite 5 GHz:** se un telefono, un portatile o un altro dispositivo si connette al Wi-Fi a 5 GHz del nodo Mesh mentre la stessa radio trasporta il backhaul wireless, i collegamenti condividono il tempo di trasmissione. Il blocco del canale a 5 GHz del nodo non impedisce necessariamente ai client di connettersi su quella banda.
- **Dispositivi connessi tramite 2.4 GHz o 6 GHz:** quando questi client utilizzano una radio separata da quella del backhaul wireless a 5 GHz, i due collegamenti non subiscono la penalizzazione dovuta all’inoltro sullo stesso canale.

Questa descrizione riguarda la configurazione testata, non tutti i modelli Mesh supportati. L’inoltro tramite radio separate non è esclusivo di Mesh e il passaggio da Extender a Mesh non migliora automaticamente la velocità effettiva.

#### Modalità Access Point e Mesh cablato {#access-point-mode-and-wired-mesh}

Entrambi utilizzano Ethernet per il collegamento al router principale. Il backhaul Ethernet funziona in full-duplex ed evita di trasmettere il traffico di backhaul tramite Wi-Fi. Le connessioni Wi-Fi dei client restano half-duplex. A parità di hardware e condizioni, la modalità Access Point e Mesh cablato possono offrire velocità effettive simili; Mesh aggiunge configurazione e gestione coordinate.

Mesh dà priorità al backhaul Ethernet e supporta il passaggio al wireless quando è disponibile un collegamento wireless adatto. Nella configurazione testata, il canale a 5 GHz del nodo resta allineato a quello del router principale anche quando il backhaul Ethernet è attivo. Questo non significa che il backhaul wireless stia trasportando il traffico. Ethernet elimina il salto wireless del backhaul dati, ma nodi e client vicini che utilizzano lo stesso canale Wi-Fi possono comunque competere per il tempo di trasmissione.

!!! note "Backhaul Mesh a 6 GHz — In arrivo"

    Il backhaul Mesh a 6 GHz richiederà hardware compatibile con 6 GHz sia sul router principale sia sul nodo Mesh, insieme a firmware che lo supporti. Non presumere che tutti i modelli compatibili con Mesh supporteranno questa funzionalità.

    Questo è diverso dal connettere un client alla rete Wi-Fi a 6 GHz esistente di un nodo. Con il backhaul a 6 GHz, una radio separata a 5 GHz potrebbe servire i client senza condividere il tempo di trasmissione del canale di backhaul. Una radio è dedicata al backhaul solo quando è riservata a tale scopo anziché servire anche i client.

!!! important "Radio separate non rendono il Wi-Fi full-duplex"

    Ogni collegamento Wi-Fi resta half-duplex. L’inoltro tramite radio separate evita di condividere un canale tra i collegamenti di backhaul e dei client, ma non elimina altre interferenze, contese o limitazioni dovute a più salti. La velocità effettiva end-to-end resta limitata dal collegamento più lento e dalle condizioni di rete.

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
