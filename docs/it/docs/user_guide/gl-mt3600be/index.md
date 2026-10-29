# Guida utente di Beryl 7 (GL-MT3600BE) {#beryl-7-gl-mt3600be-user-guide}

## Panoramica del prodotto {#product-overview}

Beryl 7 (GL-MT3600BE) e un router da viaggio portatile Wi-Fi 7 dual-band, progettato specificamente per scenari mobili come viaggi di lavoro e vacanze. Come versione aggiornata di Beryl AX, supporta tecnologie Wi-Fi 7 come Multi-Link Operation (MLO) e 4K QAM, con velocità teoriche dual-band fino a 688 Mbps (2,4 GHz) + 2882 Mbps (5 GHz), sufficienti per esigenze ad alta velocità come streaming 8K e gaming mobile.

Basato su processore quad-core MediaTek e dotato di 512 MB di memoria NAND flash, garantisce stabilità nel multitasking e compatibilità con vari plug-in OpenWrt. E dotato di 2 porte Ethernet da 2,5G e 1 porta USB 3.0, soddisfacendo sia le esigenze di connessioni cablate ad alta velocità sia quelle di espansione dello storage. Grazie alla compatibilità PD, può essere alimentato con un normale cavo di ricarica per telefono, riducendo peso e ingombro nel bagaglio. Può supportare oltre 120 dispositivi collegati contemporaneamente e ha un design elegante e portatile, pensato per la mobilita.

![gl-mt3600be interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/hardware_info/mt3600be_interface.png){class="glboxshadow"}

## Contenuto della confezione {#package-contents}

- 1 x Beryl 7 (GL-MT3600BE)
- 1 x Alimentatore
- 1 x Cavo Ethernet
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 3 x Convertitori (spine EU, UK e AU)

Guarda qui sotto il video di unboxing di Beryl 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xZHmP3B8VlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Come configurare Beryl 7 {#how-to-set-up-beryl-7}

Guarda questo video di configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ey-Z3MEOPpw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Accendi il router {#1-power-on}

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il router si avviera automaticamente.

### 2. Collega un dispositivo {#2-connect-device}

Collega il computer o il dispositivo mobile al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router tramite un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, vai in Settings -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password per collegarti. Le credenziali predefinite sono stampate sull'etichetta.

### 3. Accedi al pannello di amministrazione web {#3-log-in-to-web-admin-panel}

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua e imposta la password di amministrazione, quindi fai clic su **Apply**.

### 4. Configurazione della connessione Internet {#4-internet-setup}

**Note:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci usare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni mostrate sullo schermo.

Configura Beryl 7 usando uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_ethernet.png){class="glboxshadow"}

    Collega la porta WAN di Beryl 7 a un dispositivo upstream, ad esempio un modem, tramite un cavo Ethernet.

    Quando la connessione a Internet va a buon fine, nella sezione Ethernet della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_repeater.png){class="glboxshadow"}

    1. Nella pagina INTERNET del pannello di amministrazione web, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password, quindi fai clic su **Apply**.

    Quando la connessione a Internet va a buon fine, nella sezione Repeater della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_tethering.png){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o un dongle USB, alla porta USB di Beryl 7 tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita USB Tethering.
    3. Nella pagina INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.

    Quando la connessione a Internet va a buon fine, nella sezione Tethering della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_cellular.png){class="glboxshadow"}

    Inserisci un modem USB cellulare nella porta USB di Beryl 7. Questo metodo e utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

    Quando la connessione a Internet va a buon fine, nella sezione Cellular della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

---

Di seguito trovi una panoramica delle funzioni presenti nel pannello di amministrazione web di Beryl 7.

## Wireless {#wireless}

La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi a 5 GHz e 2,4 GHz, tra cui attivazione del Wi-Fi, potenza TX, nome della rete Wi-Fi (SSID), BSSID casuale, modalità di sicurezza Wi-Fi e password, visibilità dell'SSID, modalità Wi-Fi, larghezza di banda e canale.

Inoltre, Beryl 7 supporta il Wi-Fi MLO, cioe Multi-Link Operation, che combina simultaneamente più reti wireless per ottenere maggiore larghezza di banda e connessioni più affidabili.

Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

## Client {#clients}

La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza nome, indirizzi IP e MAC, velocità di download e upload, traffico totale e offre la possibilità di bloccare il client o eseguire altre azioni.

Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.

    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp e una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata specificamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi sull'intera rete, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Con un focus sulla gestione dell'intera rete e sul futuro supporto al controllo a livello hardware, AstroWarp offre una soluzione più robusta e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.

    Per configurarla, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Una VPN (rete privata virtuale) crea un traffico sicuro e crittografato tra il tuo dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza (client VPN) e consente di accedere a una rete remota (server VPN). Beryl 7 supporta OpenVPN e WireGuard.

=== "OpenVPN"

    Beryl 7, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Beryl 7, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocità e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete {#network}

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con più connessioni Internet, ad esempio cellular, repeater ed ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, e una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimento dati ad alta velocità e condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.

    Per configurarla, fai riferimento a [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Consente di impostare una sottorete all'interno degli intervalli di indirizzi privati IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, specificare gli indirizzi IP di gateway e netmask e configurare impostazioni di sicurezza come l'isolamento AP per la rete ospite.

    Per configurarla, fai riferimento a [Guest Network](../../interface_guide/guest_network.md).

=== "IoT Network"

    Consente di creare una rete Wi-Fi dedicata ai dispositivi IoT. Isolata dalla rete principale, offre una migliore compatibilità e maggiore sicurezza.

    Per configurarla, fai riferimento a [IoT Network](../../interface_guide/iot_network.md).

---

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione dagli attacchi DNS rebinding, sovrascrivere le impostazioni DNS di tutti i client e consentire ai DNS personalizzati di sovrascrivere i DNS della VPN. Puoi utilizzare i server DNS ottenuti automaticamente dai dispositivi a monte oppure specificare manualmente server DNS personalizzati.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La pagina Ethernet Port consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare la modalità MAC e l'indirizzo MAC per l'interfaccia WAN e visualizzare la velocità negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, e la versione più recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, permettendo un numero virtualmente illimitato di indirizzi IP univoci, elemento essenziale per il crescente numero di dispositivi collegati a Internet.

    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping e una tecnica di ottimizzazione della rete usata negli switch Ethernet per gestire e controllare il traffico multicast.

    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Network mode indica le impostazioni di configurazione che determinano come un dispositivo si connette a una rete e comunica con altri dispositivi.

    Per configurarlo, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del router principale, inclusi AdGuard Home, DNS crittografato e client VPN.

    Per configurarlo, fai riferimento ai seguenti link:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration può ridurre il carico della CPU e accelerare l'inoltro dei pacchetti di traffico.

    Per configurarla, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del traffico {#flow-control}

=== "DPI Engine"

    DPI (Deep Packet Inspection) è una funzione fondamentale per la gestione intelligente della rete. Supera il limite dei router tradizionali, che identificano solo gli indirizzi di origine o destinazione, analizzando in profondità il payload dei pacchetti. Mediante il confronto con una libreria di firme, identifica con precisione applicazioni e siti web utilizzati e consente una classificazione e un controllo dettagliati del traffico.

    Integrata con [Netify](https://www.netify.ai/){target="_blank"}, la funzione DPI di GL.iNet utilizza un plug-in integrato leggero e facile da distribuire. Il database delle firme Netify aggiornato online rende la gestione affidabile e il controllo della rete più accurato ed efficiente.

    Per maggiori dettagli, consultare [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics offre un pannello intelligente di analisi del traffico che classifica e visualizza l'utilizzo della rete per applicazione, consentendo di monitorare il traffico in tempo reale e quello storico.

    Per maggiori dettagli, consultare [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter offre una protezione online intelligente basata sulla classificazione DPI e blocca automaticamente i siti web dannosi o malevoli per mantenere la rete sicura.

    Per maggiori dettagli, consultare [Content Filter](../../interface_guide/content_filter.md).

---

=== "QoS"

    QoS (Quality of Service) ottimizza l'assegnazione della larghezza di banda dando priorità alle attività critiche, come videochiamate e giochi, durante la congestione della rete. Riduce la latenza e migliora le prestazioni complessive. Si applica al traffico dei client locali e dei tunnel del client VPN, ma non al traffico ricevuto quando il router funziona come server VPN.

    Per maggiori dettagli, consultare [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", rendendo più fluidi i giochi e le chiamate vocali.

    Per maggiori dettagli, consultare [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control consente di gestire e controllare i dispositivi dei bambini, limitandone il tempo di utilizzo e l'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Sicurezza {#security}

=== "Port Forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere a dispositivi all'interno di una rete privata.

    Per configurarlo, fai riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, acronimo di Access Control List, consente di creare regole per gestire il traffico di rete in base a protocolli di connessione, indirizzi dei dispositivi e porte. Le regole stabiliscono se consentire o bloccare l'accesso alla rete. In caso di conflitto tra più regole ACL, il sistema applica quella con priorità più alta.

    Per maggiori dettagli, consultare [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access consente di configurare diverse impostazioni di sicurezza per proteggere la rete e il router dagli accessi non autorizzati. La pagina include le opzioni seguenti:

    * Local Access Control: gestire e limitare l'accesso all'interfaccia del router dai dispositivi collegati alla rete locale.
    * Remote Access Control: configurare e limitare l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la protezione dalle minacce esterne.
    * Open Ports on Router: controllare quali porte sono aperte sul router, limitando potenziali vulnerabilita e accessi non autorizzati.

    Per maggiori dettagli, consultare [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La pagina NAT Mode consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG.

    Per configurarla, fai riferimento a [NAT Mode](../../interface_guide/nat_settings.md).

## Applicazioni {#applications}

=== "Plug-ins"

    Un plug-in e un componente software che aggiunge funzioni o funzionalità specifiche a un programma informatico esistente, consentendo personalizzazione e ampliamento delle sue capacità.

    Per configurarli, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva automaticamente e aggiorna in tempo reale l'indirizzo IP associato a un dominio. Collega un nome di dominio all'indirizzo IP pubblico dinamico del router, consentendo l'accesso remoto alla rete senza un indirizzo IP statico.

    Per configurarlo, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage indica una soluzione centralizzata di archiviazione dati che consente a più utenti e dispositivi di accedere e condividere file tramite una rete.

    Per configurarlo, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home e una soluzione di blocco di annunci e tracker a livello di rete che agisce come server DNS per filtrare contenuti indesiderati su tutti i dispositivi collegati alla rete domestica.

    Per configurarlo, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale e un servizio VPN che consente di accedere ai dispositivi e alle applicazioni ovunque.

    Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier e una soluzione di rete software-defined che consente agli utenti di creare reti virtuali sicure su Internet, collegando i dispositivi come se fossero sulla stessa rete locale.

    Per configurarlo, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abbreviazione di The Onion Router, e una rete orientata alla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server gestiti da volontari per nascondere posizione e utilizzo dell'utente, rendendo difficile tracciare le attività online.

    * [Come configurare Tor](../../interface_guide/tor.md)

## Sistema {#system}

=== "Overview"

    La pagina Overview fornisce una panoramica completa dello stato attuale del router e delle relative metriche di prestazione. In questa pagina puoi visualizzare:

    * CPU Average Load: monitora il carico medio della CPU del router per valutare le prestazioni e individuare eventuali colli di bottiglia.
    * Memory Usage: controlla quanta memoria del router e in uso, facilitando la gestione delle risorse.
    * LED Control: attiva o disattiva i LED del router, personalizzando gli indicatori visivi del dispositivo.
    * Flash Usage: visualizza l'utilizzo della memoria flash del router, assicurandoti che ci sia spazio sufficiente per firmware e dati di configurazione.
    * Device Info: accedi a informazioni dettagliate sul sistema del router, tra cui uptime, hostname, modello, architettura, versione OpenWrt, versione del kernel, ID dispositivo, MAC del dispositivo e numero di serie.
    * External Storage: controlla lo stato di eventuali dispositivi di archiviazione esterni collegati al router, ad esempio unita USB o schede TF.

    Queste funzioni offrono informazioni e controlli essenziali per gestire e monitorare in modo efficace il funzionamento del router.

    Per istruzioni dettagliate, fai riferimento a [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La pagina Admin Password consente di gestire la password dell'interfaccia di amministrazione, in modo che solo gli utenti autorizzati possano modificare le impostazioni.

    Per maggiori dettagli, consultare [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    La pagina Upgrade viene usata per aggiornare il firmware del router alla versione più recente, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Firmware Online Upgrade: verifica automaticamente sul server del produttore la disponibilità della versione firmware più recente. Se disponibile online, è possibile installarla.
    * Firmware Local Upgrade: consente di caricare manualmente un file firmware dal computer per aggiornare il router, offrendo controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni permettono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando praticita ed efficienza. Le funzioni principali di questa pagina includono:

    * LED Display Schedule: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in determinati orari.
    * Schedule Reboot: configura il riavvio automatico del router a intervalli specifici per mantenere prestazioni e stabilità ottimali.
    * Wi-Fi Status Schedule: imposta una pianificazione per controllare la banda Wi-Fi a 5 GHz / 2,4 GHz / MLO, gestendo meglio disponibilità della rete e consumo energetico.

    Queste opzioni di pianificazione offrono maggiore controllo sul funzionamento del router, garantendo che soddisfi esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attività pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Toggle Button Settings"

    La pagina Toggle Button Settings consente di configurare il pulsante fisico del router, permettendo di assegnargli funzioni specifiche per un accesso e un controllo rapidi. Questa funzione offre scorciatoie pratiche per attività e impostazioni comuni, migliorando l'esperienza d'uso e semplificando la gestione del router.

    Per istruzioni dettagliate, fai riferimento a [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporta il router alle impostazioni di default della versione firmware corrente. Può essere utile per risolvere problemi persistenti o per ricominciare da zero con la configurazione predefinita del firmware attuale.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La pagina Log offre accesso a vari registri che memorizzano attività ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati relativi a eventi e attività a livello di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attività legate ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se usato dal router, che riportano traffico web e operazioni del server.

    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione e molto utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La pagina Advanced Settings offre accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in modo dettagliato impostazioni e funzioni del router oltre a quelle disponibili nell'interfaccia di base. Include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
