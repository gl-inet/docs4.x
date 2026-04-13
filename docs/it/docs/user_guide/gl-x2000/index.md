# Guida utente di Spitz Plus (GL-X2000)

## Panoramica del prodotto

Spitz Plus (GL-X2000) è un gateway cellulare 4G LTE Wi-Fi 6 dual-SIM progettato per fornire connessioni rapide e affidabili, soprattutto nelle aree remote e durante i viaggi su strada. Grazie alla 3-Carrier Aggregation, il router trasmette dati simultaneamente su tre bande dell'operatore, offrendo una larghezza di banda disponibile fino a 3 volte superiore per evitare la congestione. Offre quattro metodi di accesso a Internet: Cellular (schede SIM), Ethernet, Repeater e Tethering. Supporta Multi-WAN (failover e bilanciamento del carico), VPN (OpenVPN e WireGuard), controllo genitori, AdGuard Home, port forwarding, Tailscale e altro ancora.

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## Contenuto della confezione

- 1 x Spitz Plus (GL-X2000)
- 1 x Manuale utente
- 4 x Antenne esterne
- 1 x Biglietto di ringraziamento
- 1 x Cavo Ethernet
- 1 x Kit di montaggio a parete
- 1 x Pad adesivo
- 4 x Viti
- 1 x Alimentatore
- 1 x Adattatore (in base al Paese di spedizione)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_unboxing.jpg){class="glboxshadow"}

## Indicatori LED

| Stato della condizione                                                      | Alimentazione                        | Internet                    | 2.4GHz                      | 5GHz                        | Cellular |
| --------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | -------- |
| Normale (connesso a Internet)                                               | Verde                                | Verde                       | Verde                       | Verde                       | Verde    |
| Non connesso a Internet                                                     | Verde                                | Spento                      | Verde                       | Verde                       | Verde    |
| Aggiornamento firmware                                                      | Verde                                | Verde lampeggiante (ogni 0,5 s) | Verde lampeggiante (ogni 0,5 s) | Verde lampeggiante (ogni 0,5 s) | Verde    |
| Reimpostazione router (tieni premuto il pulsante "reset" per > 3 s)       | Verde lampeggiante (ogni 1 s)        | Verde                       | Verde                       | Verde                       | Verde    |
| Ripristino del router alle impostazioni di fabbrica (tieni premuto "reset" per 10 s) | Verde lampeggiante veloce (ogni 0,25 s) | Verde                   | Verde                       | Verde                       | Verde    |

## Come configurare Spitz Plus

Per configurare Spitz Plus puoi usare uno dei quattro metodi di connessione Internet supportati: Cellular (SIM richiesta), Ethernet, Repeater e Tethering. Guarda questo video di configurazione oppure segui i passaggi riportati qui sotto.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Questo video mostra la configurazione Cellular di Spitz Plus. Se devi configurare Spitz Plus con altri metodi di connessione Internet, fai riferimento ai passaggi qui sotto.)</small>

!!! note "Prima di iniziare, segui questi passaggi (se ti connetti tramite metodo cellulare):"

    Per connetterti a Internet tramite il metodo cellulare è necessaria almeno una nano SIM. Se hai già la nano SIM o le nano SIM pronte, segui questi passaggi:
    
    1. Attiva la SIM, se richiesto dall'operatore.
    2. Spegni il router.
    3. Inserisci la SIM negli slot per schede SIM. (**Nota:** solo una SIM è attiva alla volta. L'altra funziona solo come backup.)

### 1. Accensione

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il dispositivo si avvierà automaticamente.

### 2. Collegare un dispositivo

Collega un dispositivo, ad esempio un computer, un portatile o uno smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, vai su Impostazioni -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password. Il nome di rete e la password predefiniti sono stampati sull'etichetta del router.

### 3. Accedere al pannello di amministrazione web

Avvia un browser web, inserisci `192.168.8.1` nella barra degli indirizzi e accederai al pannello di amministrazione web GL.iNet. Scegli una lingua, imposta la password di amministrazione e fai clic su **Apply**.

### 4. Configurazione di Internet

**Nota:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci utilizzare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni visualizzate sullo schermo.

Configura Spitz Plus utilizzando uno dei metodi di connessione Internet supportati: Cellular, Ethernet, Repeater e Tethering. Se vuoi utilizzare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    Se hai inserito la SIM nel router, la connessione Internet dovrebbe stabilirsi automaticamente. Dovresti vedere il nome dell'operatore della SIM e un punto verde comparire nella sezione Cellular.
    
    In caso contrario, spegni il router, reinserisci la SIM e riaccendilo.
    
    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models).

    **Nota**: La funzionalita eSIM di Spitz Plus e disponibile nel firmware v4.7 e successivi. Scopri come usare la scheda eSIM fisica sui router GL.iNet [qui](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    Se riscontri problemi, consulta la [Guida alla risoluzione dei problemi della rete cellulare](../../faq/cellular_network_troubleshooting_guide.md).

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}
    
    Collega la porta WAN di Spitz Plus a un dispositivo a monte, ad esempio un modem, tramite un cavo Ethernet.
    
    Una volta stabilita correttamente la connessione a Internet, nella sezione Ethernet della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. Nella pagina INTERNET del pannello di amministrazione, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password, quindi fai clic su **Apply**.
    
    Una volta stabilita correttamente la connessione a Internet, nella sezione Repeater della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o una chiavetta USB, alla porta USB del router tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita il tethering USB.
    3. Nella schermata INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.
    
    Una volta stabilita correttamente la connessione a Internet, nella sezione Tethering della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite tethering USB](../../interface_guide/internet_tethering.md).

---

Di seguito trovi una panoramica delle funzioni disponibili nel pannello di amministrazione web di Spitz Plus.

## Wi-Fi

La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi sia a 5 GHz sia a 2,4 GHz, inclusi attivazione/disattivazione del Wi-Fi, impostazione della potenza TX, definizione del nome della rete Wi-Fi (SSID), attivazione/disattivazione del BSSID casuale, selezione della modalità di sicurezza Wi-Fi, impostazione della password Wi-Fi, configurazione della visibilità dell'SSID, scelta della modalità Wi-Fi, della larghezza di banda e del canale.

Per configurare Wireless, fai riferimento a [Wireless](../../interface_guide/wireless.md).

## Client

La pagina Client mostra le informazioni sui dispositivi connessi. Per ogni client visualizza il nome del dispositivo, il tipo di connessione, ossia tramite Ethernet o Wi-Fi, gli indirizzi IP e MAC, le velocità di download e upload, il traffico totale e offre la possibilità di riservare un IP, bloccare il client o eseguire altre azioni.

Per configurare i client, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e pratico per accedere da remoto ai router GL.iNet e gestirli.
    
    Per configurare GoodCloud, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp è una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata appositamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi in intere reti, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Grazie all'attenzione alla gestione dell'intera rete e al futuro supporto per il controllo a livello hardware, AstroWarp offre una soluzione più solida e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.
    
    Per configurare AstroWarp, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

    **Nota**: aggiorna Spitz Plus al firmware v4.8 o superiore per utilizzare AstroWarp.

## VPN

Una VPN (rete privata virtuale) crea un traffico sicuro e crittografato tra il tuo dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza (client VPN) e consente di accedere a una rete remota (server VPN). Spitz Plus supporta OpenVPN e WireGuard.

=== "OpenVPN"
    
    Spitz Plus, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui queste guide:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Spitz Plus, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottime velocità e praticità. Per configurare WireGuard, segui queste guide:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Applicazioni

=== "Plug-in"

    Un plug-in è un componente software che aggiunge funzionalità specifiche a un programma esistente, consentendo la personalizzazione e l'ampliamento delle sue capacità.
    
    Per configurare i plug-in, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva e aggiorna automaticamente in tempo reale l'indirizzo IP associato a un dominio. È utile per gli utenti che necessitano di un indirizzo IP statico per accedere a una rete remota.
    
    Per configurare Dynamic DNS, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Archiviazione di rete"

    L'archiviazione di rete è una soluzione di archiviazione dati centralizzata che consente a più utenti e dispositivi di accedere ai file e condividerli tramite una rete.
    
    Per configurare l'archiviazione di rete, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home è uno strumento di terze parti che blocca annunci e tracciamento per offrirti maggiore protezione. Per sapere come abilitare AdGuard Home, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Controllo genitori"

    Il controllo genitori è un insieme di impostazioni progettate per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti. Spitz Plus offre due opzioni di controllo genitori: la versione locale sviluppata da GL.iNet e la versione integrata di Bark, un'app per il controllo genitori.

    Per configurare il controllo genitori, fai riferimento a [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Spitz Plus supporta Tailscale con firmware v4.7 e versioni successive.
    
    Tailscale è un servizio VPN che consente di accedere ai propri dispositivi e applicazioni ovunque.
    
    Per configurare Tailscale, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM"

    Spitz Plus supporta la funzionalità eSIM con firmware v4.7 e versioni successive.
    
    Per sapere come configurare e gestire la eSIM sul dispositivo, fai riferimento a [questa guida](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
## Rete

=== "Port forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere ai dispositivi presenti su una rete privata. Per configurare il port forwarding, fai riferimento a [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN è una funzione di rete che consente di configurare il router con più connessioni Internet contemporaneamente, ad esempio rete cellulare, repeater ed Ethernet. Se la connessione Internet corrente si interrompe, il router passerà automaticamente a un'altra connessione Internet. Questo garantisce un accesso a Internet fluido e senza interruzioni.

    Per configurare Multi-WAN, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La LAN, o Local Area Network, è una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimenti dati ad alta velocità e la condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.
    
    Per configurare la LAN, fai riferimento a [LAN](../../interface_guide/lan.md).

---

=== "Rete ospite"

    Consente di impostare una sottorete all'interno degli intervalli di indirizzi privati IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, specificare gli indirizzi IP di gateway e netmask e configurare impostazioni di sicurezza come l'isolamento AP per la rete ospite.

    Per configurare la rete ospite, fai riferimento a [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione contro gli attacchi di DNS rebinding, sovrascrivere le impostazioni DNS di tutti i client, consentire ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalità delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS della connessione Ethernet.

    Per configurare il DNS, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "Gestione porte"

    La pagina Gestione porte consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare la modalità MAC e l'indirizzo MAC per l'interfaccia WAN e mostrare la velocità negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Modalità di rete"

    La modalità di rete si riferisce alle impostazioni di configurazione che determinano come un dispositivo si connette a una rete e comunica con altri dispositivi.
    
    Per configurare la modalità di rete, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Internet Protocol versione 6, è la versione più recente del protocollo Internet, progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, consentendo un numero virtualmente illimitato di indirizzi IP univoci, indispensabile per supportare il numero crescente di dispositivi connessi a Internet.
    
    Per configurare IPv6, fai riferimento a [IPv6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN. Per configurare Drop-in Gateway, fai riferimento a [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    L'IGMP Snooping è una tecnica di ottimizzazione della rete utilizzata negli switch Ethernet per gestire e controllare il traffico multicast.
    
    Per configurare IGMP Snooping, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Accelerazione di rete"

    L'accelerazione hardware si riferisce all'uso di componenti hardware specializzati per eseguire attività specifiche in modo più efficiente rispetto alle CPU generiche.
    
    Per configurare l'accelerazione di rete, fai riferimento alla guida [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "Impostazioni NAT"

    La pagina Impostazioni NAT consente di abilitare o disabilitare le funzionalità Full Cone NAT e SIP ALG (Application Layer Gateway).

    Per configurare le impostazioni NAT, fai riferimento a [NAT Settings](../../interface_guide/nat_settings.md).

## Sistema

=== "Panoramica"

    La pagina Panoramica fornisce un quadro completo dello stato attuale del router e delle sue metriche di prestazione. In questa pagina puoi visualizzare:

    * Carico medio CPU: monitora il carico medio sulla CPU del router, aiutandoti a valutare le prestazioni e a individuare eventuali colli di bottiglia.
    * Utilizzo memoria: verifica quanta memoria del router è in uso, per aiutarti nella gestione delle risorse.
    * Controllo LED: attiva o disattiva i LED del router, consentendo di personalizzare gli indicatori visivi del dispositivo.
    * Utilizzo flash: visualizza l'utilizzo della memoria flash del router, assicurando spazio sufficiente per firmware e dati di configurazione.
    * Informazioni sul dispositivo: accedi alle informazioni dettagliate del sistema del router, inclusi uptime, hostname, modello, architettura, versione OpenWrt, versione del kernel, ID dispositivo, MAC del dispositivo e numero di serie.
    * Archiviazione esterna: verifica lo stato di eventuali dispositivi di archiviazione esterni collegati al router, come unità USB o schede TF.
    
    Queste funzioni forniscono informazioni e controlli essenziali, aiutandoti a gestire e monitorare in modo efficace il funzionamento del router.

    Per istruzioni dettagliate, fai riferimento a [Overview](../../interface_guide/system_overview.md){target="_blank"}.

=== "Upgrade"

    La pagina Upgrade viene utilizzata per aggiornare il firmware del router all'ultima versione, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre quattro opzioni di aggiornamento:

    * Aggiornamento firmware online: controlla automaticamente e installa l'ultima versione del firmware direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Aggiornamento firmware locale: carica manualmente un file firmware dal computer per aggiornare il router, offrendo maggiore controllo sulla versione e sul momento dell'aggiornamento.
    * Aggiornamento modulo online: controlla automaticamente e installa l'ultima versione del modulo 4G/5G direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Aggiornamento modulo locale: carica manualmente un file del modulo dal computer per aggiornare il modulo 4G/5G.

    Queste opzioni ti consentono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md){target="_blank"}.

=== "Attività pianificate"

    La pagina Attività pianificate consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando comodità ed efficienza. Le principali funzioni di questa pagina includono:

    * Pianificazione LED: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in orari specifici.
    * Riavvio pianificato: configura il router affinché si riavvii automaticamente a intervalli specifici, contribuendo a mantenere prestazioni e stabilità ottimali.
    * Pianificazione stato Wi-Fi: imposta una pianificazione per controllare la banda Wi-Fi a 5 GHz / 2,4 GHz, consentendo una migliore gestione della disponibilità di rete e del consumo energetico.
    
    Queste opzioni di pianificazione ti offrono un maggiore controllo sul funzionamento del router, assicurando che risponda alle tue esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

---

=== "Fuso orario"

    La pagina Fuso orario consente di impostare il fuso orario corretto del router, garantendo che tutte le attività pianificate, i log e gli eventi di sistema vengano registrati correttamente in base all'ora locale. Questa impostazione è fondamentale per mantenere registrazioni precise e per il corretto funzionamento delle configurazioni basate sul tempo.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Log"

    La pagina Log fornisce accesso a vari registri che documentano attività ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * Log di sistema: registri dettagliati di eventi e attività a livello di sistema.
    * Log del kernel: registri relativi alle operazioni e agli eventi del kernel.
    * Log di crash: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Log cloud: registri delle interazioni e delle attività relative ai servizi GoodCloud integrati nel router.
    * Log Nginx: registri del server web Nginx, se utilizzato dal router, che descrivono il traffico web e le operazioni del server.
    
    Inoltre, la pagina include un pulsante Export Log che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione è preziosa per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md){target="_blank"}.

=== "Sicurezza"

    La pagina Sicurezza consente di configurare diverse impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include opzioni per:

    * Password amministratore: imposta o modifica la password dell'interfaccia amministrativa del router per garantire che solo gli utenti autorizzati possano modificare le impostazioni.
    * Controllo accesso locale: gestisce e limita l'accesso all'interfaccia del router da parte dei dispositivi collegati alla rete locale.
    * Controllo accesso remoto: configura e limita l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la sicurezza contro le minacce esterne.
    * Porte aperte sul router: controlla quali porte sono aperte sul router, limitando possibili vulnerabilità e accessi non autorizzati.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate, fai riferimento a [Security](../../interface_guide/security.md).

---

=== "Ripristino firmware"

    La pagina Ripristino firmware consente di reimpostare il firmware attualmente installato alle impostazioni predefinite, cancellando tutte le configurazioni personalizzate. Questo processo ripristina il router alle impostazioni predefinite della versione firmware attualmente installata. Può essere utile per risolvere problemi persistenti o per ripartire da una configurazione pulita con le impostazioni predefinite del firmware corrente.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"}.

=== "Impostazioni avanzate"

    La pagina Impostazioni avanzate fornisce accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in dettaglio le impostazioni e le funzionalità del router oltre le opzioni di base dell'interfaccia. Ciò include configurazioni di rete dettagliate, impostazioni del firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}.
