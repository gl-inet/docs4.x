# Guida utente di Flint 2 (GL-MT6000) {#flint-2-gl-mt6000-user-guide}

## Panoramica del prodotto {#product-overview}

Flint 2 (GL-MT6000) è un router Wi-Fi 6 per casa e ufficio, ideale per trasmissioni dati intensive, connessioni simultanee di molti dispositivi o ambienti di gaming a bassissima latenza. Flint 2 offre velocità VPN WireGuard estremamente elevate, fino a 900 Mbps. Inoltre supporta funzionalità di ridondanza di rete avanzate, tra cui Multi-WAN, failover e load balance, per garantire una rete senza interruzioni.

![gl-mt6000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/hardware_info/gl-mt6000_interface.jpg){class="glboxshadow"}

## Contenuto della confezione {#package-contents}

- 1 x Flint 2 (GL-MT6000)
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 1 x Cavo Ethernet
- 1 x Alimentatore
- 1 x Adattatore (in base al Paese di spedizione)

![gl-mt6000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/first_time_setup/gl-mt6000_unboxing.jpg){class="glboxshadow"}

Guarda qui sotto il video di unboxing di Flint 2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ru1O-zxKgKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Come configurare Flint 2 {#how-to-set-up-flint-2}

Guarda questo video di configurazione oppure segui i passaggi qui sotto.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In questo video viene utilizzato un router GL.iNet diverso per mostrare la configurazione, ma i passaggi sono gli stessi per Flint 2 e per gli altri modelli di router.)</small>

### 1. Accensione {#1-power-on}

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il dispositivo si avvierà automaticamente.

### 2. Collegare un dispositivo {#2-connect-device}

Collega un dispositivo, ad esempio un computer, un portatile o uno smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, vai su Impostazioni -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password per connetterti. Il nome di rete e la password predefiniti sono stampati sull'etichetta del router.

### 3. Accedere al pannello di amministrazione web {#3-log-in-to-web-admin-panel}

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua, imposta la password di amministrazione, quindi fai clic su **Apply**.

Quando confermi i dettagli del Wi-Fi, tieni presente che se modifichi le informazioni Wi-Fi dovrai ricollegare il dispositivo alla rete Wi-Fi del router utilizzando le credenziali aggiornate.

### 4. Configurazione di Internet {#4-internet-setup}

**Nota:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci utilizzare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni visualizzate sullo schermo.

Configura Flint 2 utilizzando uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Se vuoi utilizzare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_ethernet.png){class="glboxshadow"}

    Collega un cavo Ethernet tra la porta WAN del router e un dispositivo a monte, ad esempio un modem.
    
    Una volta stabilità correttamente la connessione a Internet, nella sezione Ethernet della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_repeater.png){class="glboxshadow"}

    1. Nella pagina INTERNET del pannello di amministrazione web, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password, quindi fai clic su **Apply**.
    
    Una volta stabilità correttamente la connessione a Internet, nella sezione Repeater della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_tethering.png){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o una chiavetta USB, alla porta USB del router tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita il tethering USB.
    3. Nella pagina INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.
    
    Una volta stabilità correttamente la connessione a Internet, nella sezione Tethering della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite tethering USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_cellular.png){class="glboxshadow"}

    Collega un modem USB cellulare alla porta USB del router. Questo metodo è utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

    Una volta stabilità correttamente la connessione a Internet, nella sezione Cellular della pagina INTERNET comparirà un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Connessione a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

---

## DNS {#dns}

Le impostazioni DNS del router controllano la risoluzione dei nomi di dominio in indirizzi IP. Questa pagina consente di utilizzare i server DNS ottenuti automaticamente dai dispositivi a monte o di impostarne di personalizzati. Puoi anche configurare le opzioni DNS e modificare le regole degli host statici.

Per ulteriori informazioni, consulta [DNS](../../interface_guide/dns_v4.11.md).

## Wireless {#wireless}

La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi sia a 5 GHz sia a 2,4 GHz, inclusi attivazione/disattivazione del Wi-Fi, impostazione della potenza TX, definizione del nome della rete Wi-Fi (SSID), attivazione/disattivazione del BSSID casuale, selezione della modalità di sicurezza Wi-Fi, impostazione della password Wi-Fi, configurazione della visibilità dell'SSID, scelta della modalità Wi-Fi, della larghezza di banda e del canale.

Per configurare Wireless, fai riferimento a [Wireless](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh è una funzionalità basata sullo standard Wi-Fi EasyMesh™ che estende la copertura Wi-Fi a tutta la casa e consente il roaming senza interruzioni. Se disponi di più router GL.iNet, configurane uno come router principale e gli altri come nodi mesh per il roaming Wi-Fi senza interruzioni in tutta la casa.

Per ulteriori informazioni, consulta [Mesh](../../interface_guide/mesh.md).

## Client {#clients}

La pagina Client mostra le informazioni sui dispositivi connessi. Per ogni client visualizza il nome del dispositivo, il tipo di connessione, ossia tramite Ethernet o Wi-Fi, gli indirizzi IP e MAC, le velocità di download e upload, il traffico totale e offre la possibilità di riservare un IP, bloccare il client o eseguire altre azioni.

Per configurare i client, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account consente di collegare e gestire dispositivi e servizi cloud. Puoi accedere agevolmente sia a GoodCloud sia alla glinet App, gestendo la rete in modo sicuro e pratico ovunque e in qualsiasi momento.

    Per configurare GL.iNet Account, consulta [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    Il servizio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e pratico per accedere da remoto ai router GL.iNet e gestirli.
    
    Per configurare GoodCloud, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS è una funzione di rete avanzata progettata per offrire accesso remoto e gestione dei dispositivi senza interruzioni. Sviluppato appositamente per l'integrazione con i router GL.iNet, GoodPAS utilizza il protocollo AmneziaWG con offuscamento del traffico integrato per garantire connessioni sicure e stabili. GoodPAS consente di accedere da remoto alla rete domestica. Quando il router di casa funge da nodo di uscita GoodPAS, il traffico Internet inviato tramite GoodPAS utilizza l’indirizzo IP pubblico WAN di quel router.

    Per configurare GoodPAS, consulta [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

Una VPN (rete privata virtuale) crea traffico sicuro e crittografato tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza come client VPN e consente di accedere a una rete remota come server VPN. Flint 2, come gli altri router GL.iNet, supporta OpenVPN e WireGuard.

=== "OpenVPN"

    Flint 2, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui queste guide:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 2, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottime velocità e praticità. Per configurare WireGuard, segui queste guide:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete {#network}

=== "Multi-WAN"

    Multi-WAN è una funzione di rete che consente di configurare il router con più connessioni Internet contemporaneamente, ad esempio rete cellulare, repeater ed Ethernet. Se la connessione Internet corrente si interrompe, il router passerà automaticamente a un'altra connessione Internet. Questo garantisce un accesso a Internet fluido e senza interruzioni.

    Per configurare Multi-WAN, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La pagina LAN centralizza la configurazione e la gestione della rete principale, della rete ospite, della rete IoT e delle reti VLAN personalizzate. Puoi creare e gestire più sottoreti per isolare diversi tipi di dispositivi o traffico.

=== "Porte Ethernet"

    La pagina Porte Ethernet consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare la modalità MAC e l'indirizzo MAC per l'interfaccia WAN e mostrare la velocità negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

=== "IPv6"

    IPv6, o Internet Protocol versione 6, è la versione più recente del protocollo Internet, progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, consentendo un numero virtualmente illimitato di indirizzi IP univoci, indispensabile per supportare il numero crescente di dispositivi connessi a Internet.
    
    Per configurare IPv6, fai riferimento a [IPv6](../../interface_guide/ipv6.md).

<br>

=== "IGMP Snooping"

    L'IGMP Snooping è una tecnica di ottimizzazione della rete utilizzata negli switch Ethernet per gestire e controllare il traffico multicast.
    
    Per configurare IGMP Snooping, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Modalità di rete"

    La pagina Network Mode consente di configurare il ruolo operativo del router in base a diverse esigenze di distribuzione della rete. È possibile scegliere varie modalità, dalla copertura Wi-Fi domestica alle reti multi-link aziendali; ciascuna modalità abilita o disabilita funzioni specifiche del router per ottimizzare le prestazioni.

    Per configurare questa funzione, consulta [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN client.

    Per configurarlo, fai riferimento ai seguenti link:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Accelerazione di rete"

    L'accelerazione di rete può ridurre il carico della CPU e velocizzare l'inoltro dei pacchetti di traffico.
    
    Per configurare l'accelerazione di rete, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del traffico {#flow-control}

=== "Network Quality"

    La dashboard Network Quality monitora la qualità della connessione Internet in tempo reale. Valuta la reattività, la latenza e le prestazioni DNS, rilevando interruzioni della connessione e perdite di pacchetti. Queste metriche aiutano a identificare instabilità della rete e problemi di connettività che i soli test della larghezza di banda potrebbero non rilevare.

    Per ulteriori informazioni, consulta [Network Quality](../../interface_guide/network_quality.md).

=== "Data Statistics"

    Data Statistics offre un pannello intelligente di analisi del traffico che classifica e visualizza l'utilizzo della rete per applicazione, consentendo di monitorare il traffico in tempo reale e quello storico.

    Per maggiori dettagli, consultare [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter offre una protezione online intelligente basata sulla classificazione DPI e blocca automaticamente i siti web dannosi o malevoli per mantenere la rete sicura.

    Per maggiori dettagli, consultare [Content Filter](../../interface_guide/content_filter.md).

<br>

=== "QoS"

    QoS (Quality of Service) ottimizza l'assegnazione della larghezza di banda dando priorità alle attività critiche, come videochiamate e giochi, durante la congestione della rete. Riduce la latenza e migliora le prestazioni complessive. Si applica al traffico dei client locali e dei tunnel del client VPN, ma non al traffico ricevuto quando il router funziona come server VPN.

    Per maggiori dettagli, consultare [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", rendendo più fluidi i giochi e le chiamate vocali.

    Per maggiori dettagli, consultare [SQM](../../interface_guide/sqm.md).

=== "Controllo genitori"

    Controllo genitori è progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Sicurezza {#security}

=== "Security Scan"

    Security Scan esegue un controllo di sicurezza del router. Valuta le impostazioni di sicurezza e genera un punteggio di sicurezza, insieme ad avvisi sui rischi e suggerimenti di ottimizzazione. Puoi modificare la configurazione in base ai risultati della scansione per migliorare la sicurezza del router.

    Per ulteriori informazioni, consulta [Security Scan](../../interface_guide/security_scan.md).

=== "ACL"

    ACL, acronimo di Access Control List, consente di creare regole per gestire il traffico di rete in base a protocolli di connessione, indirizzi dei dispositivi e porte. Le regole stabiliscono se consentire o bloccare l'accesso alla rete. In caso di conflitto tra più regole ACL, il sistema applica quella con priorità più alta.

    Per maggiori dettagli, consultare [ACL](../../interface_guide/acl.md).

=== "Port Forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere ai dispositivi presenti su una rete privata.

    Per configurare il port forwarding, fai riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md).

<br>

=== "UPnP"

    UPnP (Universal Plug and Play) consente ai dispositivi e alle applicazioni LAN compatibili di richiedere automaticamente mappature delle porte sui router GL.iNet. Queste mappature inoltrano il traffico WAN in ingresso a indirizzi IP e porte LAN specifici, consentendo ai client esterni di connettersi ai servizi locali senza configurare manualmente regole di port forwarding.

    Per ulteriori informazioni, consulta [UPnP](../../interface_guide/upnp.md).

=== "Admin Access"

    Admin Access consente di configurare diverse impostazioni di sicurezza per proteggere la rete e il router dagli accessi non autorizzati. La pagina include le opzioni seguenti:

    * Controllo accesso locale: gestisce e limita l'accesso all'interfaccia del router da parte dei dispositivi collegati alla rete locale.
    * Controllo accesso remoto: configura e limita l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la sicurezza contro le minacce esterne.
    * Porte aperte sul router: controlla quali porte sono aperte sul router, limitando possibili vulnerabilità e accessi non autorizzati.

    Per maggiori dettagli, consultare [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La pagina NAT Mode consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG.

    Per configurarla, fai riferimento a [NAT Mode](../../interface_guide/nat_settings.md).

## Applicazioni {#applications}

=== "Plug-in"

    Un plug-in è un componente software che aggiunge funzionalità specifiche a un programma esistente, consentendo la personalizzazione e l'ampliamento delle sue capacità.
    
    Per configurare i plug-in, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva e aggiorna automaticamente in tempo reale l'indirizzo IP associato a un dominio. Collega un nome di dominio all'indirizzo IP pubblico dinamico del router, consentendo l'accesso remoto alla rete senza un indirizzo IP statico.
    
    Per configurare Dynamic DNS, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Archiviazione di rete"

    L'archiviazione di rete è una soluzione di archiviazione dati centralizzata che consente a più utenti e dispositivi di accedere ai file e condividerli tramite una rete.
    
    Per configurare l'archiviazione di rete, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

<br>

=== "AdGuard Home"

    AdGuard Home è una soluzione di blocco degli annunci e dei tracker a livello di rete che funziona come server DNS per filtrare i contenuti indesiderati su tutti i dispositivi collegati alla rete domestica.
    
    Per configurare AdGuard Home, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale è un servizio VPN che consente di accedere ai propri dispositivi e applicazioni ovunque.
    
    Per configurare Tailscale, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier è una soluzione di rete definita dal software che consente agli utenti di creare reti virtuali sicure su Internet, collegando i dispositivi come se si trovassero sulla stessa rete locale.
    
    Per configurare ZeroTier, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abbreviazione di The Onion Router, è una rete incentrata sulla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server volontari, chiamati nodi, per oscurare la posizione e l'utilizzo dell'utente, rendendo difficile tracciare le attività online.

    Per maggiori dettagli, consultare [Tor](../../interface_guide/tor.md).

## Sistema {#system}

=== "Panoramica"

    La pagina Panoramica fornisce un quadro completo dello stato attuale del router e delle sue metriche di prestazione. In questa pagina puoi visualizzare:

    * Carico medio CPU: monitora il carico medio sulla CPU del router, aiutandoti a valutare le prestazioni e a individuare eventuali colli di bottiglia.
    * Utilizzo memoria: verifica quanta memoria del router è in uso, per aiutarti nella gestione delle risorse.
    * Controllo LED: attiva o disattiva i LED del router, consentendo di personalizzare gli indicatori visivi del dispositivo.
    * Utilizzo flash: visualizza l'utilizzo della memoria flash del router, assicurando spazio sufficiente per firmware e dati di configurazione.
    * Informazioni sul dispositivo: accedi alle informazioni dettagliate del sistema del router, inclusi uptime, hostname, modello, architettura, versione OpenWrt, versione del kernel, ID dispositivo, MAC del dispositivo e numero di serie.
    * Archiviazione esterna: verifica lo stato di eventuali dispositivi di archiviazione esterni collegati al router, come unità USB o schede TF.
    
    Queste funzioni forniscono informazioni e controlli essenziali, aiutandoti a gestire e monitorare in modo efficace il funzionamento del router.

    Per istruzioni dettagliate, fai riferimento a [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La pagina Admin Password consente di gestire la password dell'interfaccia di amministrazione, in modo che solo gli utenti autorizzati possano modificare le impostazioni.

    Per maggiori dettagli, consultare [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    La pagina Upgrade viene utilizzata per aggiornare il firmware del router all'ultima versione, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Aggiornamento firmware online: verifica automaticamente sul server del produttore la disponibilità della versione firmware più recente. Se disponibile online, è possibile installarla.
    * Aggiornamento firmware locale: carica manualmente un file firmware dal computer per aggiornare il router, offrendo maggiore controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni ti consentono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

=== "Attività pianificate"

    La pagina Attività pianificate consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando comodità ed efficienza. Le principali funzioni di questa pagina includono:

    * Pianificazione LED: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in orari specifici.
    * Riavvio pianificato: configura il router affinché si riavvii automaticamente a intervalli specifici, contribuendo a mantenere prestazioni e stabilità ottimali.
    * Pianificazione stato Wi-Fi 5 GHz / 2,4 GHz: imposta una pianificazione per controllare le bande Wi-Fi a 5 GHz e 2,4 GHz, consentendo una migliore gestione della disponibilità di rete e del consumo energetico.
    
    Queste opzioni di pianificazione ti offrono un maggiore controllo sul funzionamento del router, assicurando che risponda alle tue esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Fuso orario"

    La pagina Fuso orario consente di impostare il fuso orario corretto del router, garantendo che tutte le attività pianificate, i log e gli eventi di sistema vengano registrati correttamente in base all'ora locale. Questa impostazione è fondamentale per mantenere registrazioni precise e per il corretto funzionamento delle configurazioni basate sul tempo.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

=== "Ripristino firmware"

    La pagina Ripristino firmware consente di reimpostare il firmware attualmente installato alle impostazioni predefinite, cancellando tutte le configurazioni personalizzate. Questo processo ripristina il router alle impostazioni predefinite della versione firmware attualmente installata. Può essere utile per risolvere problemi persistenti o per ripartire da una configurazione pulita con le impostazioni predefinite del firmware corrente.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

<br>

=== "Log"

    La pagina Log fornisce accesso a vari registri che documentano attività ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * Log di sistema: registri dettagliati di eventi e attività a livello di sistema.
    * Log del kernel: registri relativi alle operazioni e agli eventi del kernel.
    * Log di crash: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Log cloud: registri delle interazioni e delle attività relative ai servizi GoodCloud integrati nel router.
    * Log Nginx: registri del server web Nginx, se utilizzato dal router, che descrivono il traffico web e le operazioni del server.
    
    Inoltre, la pagina include un pulsante Export Log che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione è preziosa per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md).

=== "Impostazioni avanzate"

    La pagina Impostazioni avanzate fornisce accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in dettaglio le impostazioni e le funzionalità del router oltre le opzioni di base dell'interfaccia. Ciò include configurazioni di rete dettagliate, impostazioni del firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
