# Guida utente di Brume 3 (GL-MT5000)

## Panoramica del prodotto

Brume 3 (GL-MT5000) è un gateway di sicurezza ad alte prestazioni basato su OpenWrt v21.02, dotato di CPU MediaTek Quad-core Cortex-A53, 1 GB di RAM e 8 GB di memoria eMMC per l'espansione tramite plug-in. Ha un design compatto, ideale per installazioni in spazi ridotti, e supporta hosting VPN domestico, SD-WAN site-to-site e oltre 30 servizi VPN per una connettività sicura tra sedi diverse. Inoltre, integra la funzionalità DPI di GL.iNet, insieme a Controllo genitori e AdGuard Home, per soddisfare le esigenze di appassionati di tecnologia e utenti aziendali.

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## Contenuto della confezione

- 1 x Brume 3 (GL-MT5000)
- 1 x Alimentatore
- 1 x Cavo Ethernet
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 1 x Adattatore (in base al Paese di spedizione)

Guarda qui sotto il video di unboxing di Brume 3.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Come configurare Brume 3

Guarda questo video di configurazione oppure segui i passaggi qui sotto.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwbdUy79WHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Accensione

Assembla l'alimentatore in due parti. Collegalo a Brume 3 e inseriscilo in una presa di corrente. Il dispositivo si avvierà automaticamente.

### 2. Collegare un dispositivo

Collega un dispositivo cablato, ad esempio un computer o un portatile, alla porta LAN di Brume 3 tramite un cavo Ethernet.

### 3. Accedere al pannello di amministrazione web

**Nota:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet.

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua, imposta la password di amministrazione e fai clic su **Apply**.

### 4. Configurazione di Internet

Configura Brume 3 utilizzando uno dei metodi di connessione Internet supportati: Ethernet, Tethering e Cellular (opzionale). Se vuoi utilizzare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Collega la porta WAN di Brume 3 a un dispositivo a monte, ad esempio un modem, tramite un cavo Ethernet.
    
    Quando Brume 3 è connesso correttamente a Internet, accanto a "Ethernet" nella pagina INTERNET del pannello di amministrazione web apparirà un punto verde e il LED fisico di Brume 3 diventerà bianco fisso.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. Collega il dispositivo mobile alla porta USB Type-C di Brume 3 tramite un cavo dati USB 3.0.
    2. Nelle impostazioni del dispositivo mobile, abilita il tethering USB.
    3. Nella pagina INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione "Tethering".
    
    Quando Brume 3 è connesso correttamente a Internet, accanto a "Tethering" nella pagina INTERNET del pannello di amministrazione web apparirà un punto verde e il LED fisico di Brume 3 diventerà bianco fisso.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite tethering USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    Per questo metodo di connessione è necessario un cavo adattatore aggiuntivo da USB-C a USB-A.
    
    Collega un modem USB cellulare alla porta USB Type-C di Brume 3 tramite un cavo adattatore aggiuntivo da USB-C a USB-A. Questo metodo è utile per condividere la connessione Internet di un modem USB con tutti i dispositivi client collegati.

    Quando Brume 3 è connesso correttamente a Internet, accanto a "Cellular" nella pagina INTERNET del pannello di amministrazione web apparirà un punto verde e il LED fisico di Brume 3 diventerà bianco fisso.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

---

Di seguito trovi una panoramica delle funzioni disponibili nel pannello di amministrazione web di Brume 3.

## Client

La pagina Client mostra le informazioni sui dispositivi connessi. Per ogni client vengono visualizzati nome, indirizzi IP e MAC, velocità di download e upload, traffico totale, oltre alla possibilità di bloccare il client o eseguire altre azioni.

Per configurare i client, fai riferimento a [Client](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    Il servizio di gestione cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e pratico per accedere da remoto ai router GL.iNet e gestirli.
    
    Per configurare GoodCloud, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp è una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata appositamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi in intere reti, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Grazie all'attenzione alla gestione dell'intera rete e al futuro supporto per il controllo a livello hardware, AstroWarp offre una soluzione più solida e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.
    
    Per configurare AstroWarp, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN (rete privata virtuale) crea un traffico sicuro e crittografato tra il tuo dispositivo e il server VPN. Fornisce un ulteriore livello di privacy e sicurezza (client VPN) e consente di accedere a una rete remota (server VPN). Brume 3 supporta OpenVPN e WireGuard.

=== "OpenVPN"
    
    Brume 3, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui queste guide:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Brume 3, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottime velocità e praticità. Per configurare WireGuard, segui queste guide:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete

=== "Multi-WAN"

    Multi-WAN è una funzione di rete che consente di configurare il router con più connessioni Internet contemporaneamente, ad esempio cellulare, repeater ed Ethernet. Se la connessione Internet corrente si interrompe, il router passerà automaticamente a un'altra connessione Internet. Questo garantisce un accesso a Internet fluido e senza interruzioni.

    Per configurare Multi-WAN, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La LAN, o Local Area Network, è una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimenti dati ad alta velocità e la condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.
    
    Per configurare la LAN, fai riferimento a [LAN](../../interface_guide/lan.md).

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione contro gli attacchi di DNS rebinding, sovrascrivere le impostazioni DNS di tutti i client, consentire ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalità delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS della connessione Ethernet.

    Per configurare il DNS, fai riferimento a [DNS](../../interface_guide/dns.md).

---

=== "Porte Ethernet"

    La pagina Porte Ethernet consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare la modalità MAC e l'indirizzo MAC per l'interfaccia WAN e mostrare la velocità negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, o Internet Protocol versione 6, è la versione più recente del protocollo Internet, progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, consentendo un numero virtualmente illimitato di indirizzi IP univoci, indispensabile per supportare il numero crescente di dispositivi connessi a Internet.
    
    Per configurare IPv6, fai riferimento a [IPv6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    L'IGMP Snooping è una tecnica di ottimizzazione della rete utilizzata negli switch Ethernet per gestire e controllare il traffico multicast.
    
    Per configurare IGMP Snooping, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Modalità di rete"

    La modalità di rete si riferisce alle impostazioni di configurazione che determinano come un dispositivo si connette a una rete e comunica con altri dispositivi.
    
    Per configurare la modalità di rete, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN.
    
    Per configurare Drop-in Gateway, fai riferimento a questi link:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Accelerazione di rete"

    L'accelerazione di rete può ridurre il carico della CPU e velocizzare l'inoltro dei pacchetti di traffico.
    
    Per configurare l'accelerazione di rete, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del traffico

=== "Licenza DPI"

    DPI (Deep Packet Inspection) è una funzionalità centrale della gestione intelligente della rete. Può superare i limiti dei router tradizionali, che identificano solo indirizzi di origine o destinazione, analizzare in profondità il payload dei pacchetti dati e identificare con precisione applicazioni e siti web visitati dagli utenti tramite il confronto con una libreria di firme, consentendo una classificazione e un controllo raffinati del traffico.
    
    Integrata con [Netify](https://www.netify.ai/){target="_blank"}, la funzione DPI di GL.iNet adotta un plug-in embedded leggero per una distribuzione efficiente. Grazie al database di firme aggiornato online da Netify, consente una gestione affidabile e rende il controllo della rete più preciso ed efficiente.

    Per istruzioni dettagliate, fai riferimento a [DPI License](../../interface_guide/dpi_license.md).

=== "Statistiche dati"

    Statistiche dati offre una dashboard intelligente di analisi del traffico che categorizza e visualizza l'utilizzo della rete per applicazione, aiutandoti a monitorare il traffico in tempo reale e storico per una migliore consapevolezza e un controllo più efficace della rete.

    Per istruzioni dettagliate, fai riferimento a [Data Statistics](../../interface_guide/data_statistics.md).

=== "Filtro dei contenuti"

    Filtro dei contenuti offre una protezione online intelligente basata sulla classificazione DPI, bloccando automaticamente siti web dannosi o malevoli per mantenere la rete pulita e sicura.

    Per istruzioni dettagliate, fai riferimento a [Content Filter](../../interface_guide/content_filter.md).

---

=== "Controllo genitori"

    Controllo genitori è progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurare il controllo genitori, fai riferimento a [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) ottimizza l'allocazione della larghezza di banda dando priorità alle attività critiche, ad esempio videochiamate e gaming, durante la congestione della rete, riducendo la latenza e migliorando le prestazioni complessive della rete. Tieni presente che questo vale per il traffico dei client locali e per il traffico del tunnel del client VPN, ma non per il traffico ricevuto quando il router funziona come server VPN.

    Per istruzioni dettagliate, fai riferimento a [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", garantendo sessioni di gioco e chiamate vocali più fluide.

    Per istruzioni dettagliate, fai riferimento a [SQM](../../interface_guide/sqm.md).

## Sicurezza

=== "Port Forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere ai dispositivi presenti su una rete privata.
    
    Per configurare il port forwarding, fai riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Controllo di gestione"

    Controllo di gestione consente di configurare diverse impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include le seguenti opzioni:

    * Controllo accesso locale: gestisce e limita l'accesso all'interfaccia del router da parte dei dispositivi collegati alla rete locale.
    * Controllo accesso remoto: configura e limita l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la sicurezza contro le minacce esterne.
    * Porte aperte sul router: controlla quali porte sono aperte sul router, limitando possibili vulnerabilità e accessi non autorizzati.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate, fai riferimento a [Security](../../interface_guide/security.md).

=== "Modalità NAT"

    La pagina Modalità NAT consente di abilitare o disabilitare le funzionalità Full Cone NAT e SIP ALG (Application Layer Gateway).

    Per configurare le impostazioni NAT, fai riferimento a [NAT Mode](../../interface_guide/nat_settings.md).

## Applicazioni

=== "Plug-in"

    Un plug-in è un componente software che aggiunge funzionalità specifiche a un programma esistente, consentendo la personalizzazione e l'ampliamento delle sue capacità.
    
    Per configurare i plug-in, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva e aggiorna automaticamente in tempo reale l'indirizzo IP associato a un dominio. È particolarmente utile per gli utenti che necessitano di un indirizzo IP statico per accedere a una rete remota.
    
    Per configurare Dynamic DNS, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Archiviazione di rete"

    L'archiviazione di rete è una soluzione di archiviazione dati centralizzata che consente a più utenti e dispositivi di accedere ai file e condividerli tramite una rete.
    
    Per configurare l'archiviazione di rete, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home è una soluzione di blocco degli annunci e dei tracker a livello di rete che funziona come server DNS per filtrare i contenuti indesiderati su tutti i dispositivi collegati alla rete domestica.
    
    Per configurare AdGuard Home, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier è una soluzione di rete definita dal software che consente agli utenti di creare reti virtuali sicure su Internet, collegando i dispositivi come se si trovassero sulla stessa rete locale.
    
    Per configurare ZeroTier, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale è un servizio VPN che consente di accedere ai propri dispositivi e applicazioni ovunque.
    
    Per configurare Tailscale, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, abbreviazione di The Onion Router, è una rete incentrata sulla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server volontari, chiamati nodi, per oscurare la posizione e l'utilizzo dell'utente, rendendo difficile tracciare le attività online.
    
    * [Come configurare Tor](../../interface_guide/tor.md)

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

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Overview](../../interface_guide/system_overview.md).

=== "Password amministratore"

    La pagina Password amministratore consente di impostare o modificare la password dell'interfaccia amministrativa del router, in modo che solo gli utenti autorizzati possano modificare le impostazioni.

    Per motivi di sicurezza, consigliamo di attivare **Prevent Weak Password**.

    Quando **Prevent Weak Password** è attivato, i requisiti per le nuove password sono i seguenti.

    * Minimo 5 caratteri e massimo 63 caratteri.
    * Sono consentiti lettere (distinzione tra maiuscole e minuscole), numeri e simboli `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Sono richieste almeno due tra lettere maiuscole, lettere minuscole, numeri e simboli.

=== "Upgrade"

    La pagina Upgrade viene utilizzata per aggiornare il firmware del router all'ultima versione, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Aggiornamento firmware online: controlla automaticamente e installa l'ultima versione del firmware direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Aggiornamento firmware locale: carica manualmente un file firmware dal computer per aggiornare il router, offrendo maggiore controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni ti consentono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

---

=== "Attività pianificate"

    La pagina Attività pianificate consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando comodità ed efficienza. Le principali funzioni di questa pagina includono:

    * Pianificazione LED: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in orari specifici.
    * Riavvio pianificato: configura il router affinché si riavvii automaticamente a intervalli specifici, contribuendo a mantenere prestazioni e stabilità ottimali.
    
    Queste opzioni di pianificazione ti offrono un maggiore controllo sul funzionamento del router, assicurando che risponda alle tue esigenze e preferenze specifiche.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Fuso orario"

    La pagina Fuso orario consente di impostare il fuso orario corretto del router, garantendo che tutte le attività pianificate, i log e gli eventi di sistema vengano registrati correttamente in base all'ora locale. Questa impostazione è fondamentale per mantenere registrazioni precise e per il corretto funzionamento delle configurazioni basate sul tempo.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    La pagina Log fornisce accesso a vari registri che documentano attività ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * Log di sistema: registri dettagliati di eventi e attività a livello di sistema.
    * Log del kernel: registri relativi alle operazioni e agli eventi del kernel.
    * Log di crash: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Log cloud: registri delle interazioni e delle attività relative ai servizi GoodCloud integrati nel router.
    * Log Nginx: registri del server web Nginx, se utilizzato dal router, che descrivono il traffico web e le operazioni del server.
    
    Inoltre, la pagina include un pulsante Export Log che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione è preziosa per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Log](../../interface_guide/log.md).

---

=== "Ripristino firmware"

    La pagina Ripristino firmware consente di reimpostare il firmware attualmente installato alle impostazioni predefinite, cancellando tutte le configurazioni personalizzate. Questo processo ripristina il router alle impostazioni predefinite della versione firmware attualmente installata. Può essere utile per risolvere problemi persistenti o per ripartire da una configurazione pulita con le impostazioni predefinite del firmware corrente.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Impostazioni avanzate"

    La pagina Impostazioni avanzate fornisce accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in dettaglio le impostazioni e le funzionalità del router oltre le opzioni di base dell'interfaccia. Ciò include configurazioni di rete dettagliate, impostazioni del firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
