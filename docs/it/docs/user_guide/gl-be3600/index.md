# Guida utente di Slate 7 (GL-BE3600) {#slate-7-gl-be3600-user-guide}

## Panoramica del prodotto {#product-overview}

Slate 7 (GL-BE3600) e il primo router da viaggio portatile Wi-Fi 7 dual-band di GL.iNet, realizzato con tecnologie Wi-Fi 7 di fascia alta come Multi-Link Operation e 4K QAM. Offre velocità teoriche dual-band di 688Mbps (2.4GHz) e 2882Mbps (5GHz), consentendo streaming 8K fluido ed esperienze di gioco mobile di alto livello. Il touchscreen permette di controllare a colpo d'occhio lo stato della rete ed eseguire operazioni di base in modo intuitivo.

Dotato di 2 porte Ethernet da 2,5G (1 WAN + 1 LAN) e 1 porta USB 3.0, il router soddisfa le esigenze di connessioni cablate ad alta velocità e di espansione flessibile dello storage. Supporta inoltre l'alimentazione Type-C PD (5V/3A, 9V/3A, 12V/2,5A) e presenta un design compatto e leggero, ideale da portare con sé. Preinstallato con AdGuard Home e compatibile con oltre 30 servizi VPN, offre una protezione robusta per la rete. Combinando praticita mobile e prestazioni di livello professionale, Slate 7 e la scelta ideale per il lavoro da remoto e la condivisione della rete in mobilita.

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

## Contenuto della confezione {#package-contents}

- 1 x Slate 7 (GL-BE3600)
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 1 x Cavo Ethernet
- 1 x Cavo di alimentazione
- 1 x Alimentatore US
- 3 x Convertitori (spine EU, UK e AU)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

Guarda qui sotto il video di unboxing di Slate 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bEuwGm0hQ5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Touchscreen {#touchscreen}

| Visualizzazione sullo schermo | Descrizione |
| :---------------------------- | :---------- |
| ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){width="400"} | Avvio in corso |
| ![network](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){width="400"} | Tipi di connessione di rete e stato<br>**Verde**: attiva / connessa<br>**Giallo**: connessione in corso / anomala<br>**Bianco**: connessione inattiva |
| ![wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wifi-details.png){width="400"} | Dettagli Wi-Fi, inclusi SSID, password, codice QR e pulsante di accensione/spegnimento |
| ![vpn](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/vpn_client.png){width="400"} | Stato VPN. Richiede la configurazione iniziale nel pannello di amministrazione web |
| ![adguard home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/adguard_home.png){width="400"} | AdGuard Home |
| ![tor](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/tor.png){width="400"} | Tor |
| ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/traffic_statistics.png){width="400"} | Statistiche del traffico<br>Si riferiscono alla velocità media di tutto il traffico che passa attraverso il router, calcolata ogni 3 secondi |
| ![system usage](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/overview.png){width="400"} | Utilizzo del sistema |
| ![time zone](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/time.png){width="400"} | Fuso orario |
| ![system menu](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/system_settings.png){width="400"} | Menu di sistema<br>Scorri dall'alto verso il basso per accedere al menu di sistema |
| ![unlock](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-unlock.png){width="400"} | Tocca lo schermo per riattivarlo e scorri da sinistra a destra per sbloccarlo |
| ![reboot](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-reboot.png){width="400"} | Dopo aver toccato "Reboot", scorri da sinistra a destra per confermare |

## Come configurare Slate 7 {#how-to-set-up-slate-7}

Guarda questo video di configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In questo video mostriamo la configurazione di Slate 7 in modalità Repeater. Se devi configurare Slate 7 con altri metodi di connessione Internet, fai riferimento ai passaggi sotto.)</small>

### 1. Accendi il router {#1-power-on}

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il router si avviera automaticamente.

### 2. Collega un dispositivo {#2-connect-device}

Collega un dispositivo, ad esempio un computer, un laptop o uno smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password per collegarti. Il nome di rete e la password predefiniti sono stampati sull'etichetta del router.

### 3. Accedi al pannello di amministrazione web {#3-log-in-to-web-admin-panel}

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli una lingua e imposta la password di amministrazione, quindi fai clic su **Apply**.

### 4. Configurazione della connessione Internet {#4-internet-setup}

**Note:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci usare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni mostrate sullo schermo.

Configura Slate 7 usando uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class="glboxshadow"}
    
    Collega la porta WAN di Slate 7 a un dispositivo upstream, ad esempio un modem, tramite un cavo Ethernet.
    
    Quando la connessione a Internet va a buon fine, nella sezione Ethernet della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class="glboxshadow"}

    1. Nella schermata INTERNET del pannello di amministrazione web, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password, quindi fai clic su **Apply**.
    
    Quando la connessione a Internet va a buon fine, nella sezione Repeater della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o un dongle USB, alla porta USB del router tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita USB Tethering.
    3. Nella schermata INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.
    
    Quando la connessione a Internet va a buon fine, nella sezione Tethering della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class="glboxshadow"}

    Inserisci un modem USB cellulare nella porta USB di Slate 7. Questo metodo e utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

    Quando la connessione a Internet va a buon fine, nella sezione Cellular della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

---

Di seguito trovi una panoramica delle funzioni presenti nel pannello di amministrazione web di Slate 7.

## Wireless {#wireless}

La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi a 5 GHz e 2.4 GHz, tra cui attivazione del Wi-Fi, potenza TX, nome della rete Wi-Fi (SSID), BSSID casuale, modalità di sicurezza Wi-Fi e password, visibilità dell'SSID, modalità Wi-Fi, larghezza di banda e canale.

Inoltre, Slate 7 supporta il Wi-Fi MLO, cioe Multi-Link Operation, che combina simultaneamente più reti wireless per ottenere maggiore larghezza di banda e connessioni più affidabili.

Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh è una funzionalità basata sullo standard Wi-Fi EasyMesh™ che estende la copertura Wi-Fi a tutta la casa e consente il roaming senza interruzioni. Se disponi di più router GL.iNet, configurane uno come router principale e gli altri come nodi mesh per il roaming Wi-Fi senza interruzioni in tutta la casa.

Per configurare Mesh, fai riferimento a [Mesh](../../interface_guide/mesh.md).

## Client {#clients}

La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza nome, indirizzi IP e MAC, velocità di download e upload, traffico totale e offre la possibilità di bloccare il client o eseguire altre azioni.

Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account consente di collegare e gestire dispositivi e servizi cloud. Puoi accedere agevolmente sia a GoodCloud sia alla glinet App, gestendo la rete in modo sicuro e pratico ovunque e in qualsiasi momento.

    Per configurare GL.iNet Account, consulta [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.
    
    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS è una funzione di rete avanzata progettata per offrire accesso remoto e gestione dei dispositivi senza interruzioni. Sviluppato appositamente per l'integrazione con i router GL.iNet, GoodPAS utilizza il protocollo AmneziaWG con offuscamento del traffico integrato per garantire connessioni sicure e stabili. GoodPAS consente di accedere da remoto alla rete domestica. Quando il router di casa funge da nodo di uscita GoodPAS, il traffico Internet inviato tramite GoodPAS utilizza l’indirizzo IP pubblico WAN di quel router.

    Per configurare GoodPAS, consulta [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

Una VPN (rete privata virtuale) crea un traffico sicuro e crittografato tra il tuo dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza (client VPN) e consente di accedere a una rete remota (server VPN). Slate 7 supporta OpenVPN e WireGuard.

=== "OpenVPN"

    Slate 7, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocità e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete {#network}

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con più connessioni Internet, ad esempio cellular, repeater ed ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Questa pagina consente di configurare e gestire in modo centralizzato **Main Network**, **Guest Network**, **IoT Network** e le **VLAN Networks** personalizzate. È possibile creare e gestire più sottoreti per isolare diversi tipi di dispositivi o traffico.

    Per configurare questa funzione, consulta [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La pagina Ethernet Port consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare modalità MAC e indirizzo MAC per l'interfaccia WAN e visualizzare la velocità negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione dagli attacchi DNS rebinding, sovrascrivere le impostazioni DNS di tutti i client e consentire ai DNS personalizzati di sovrascrivere i DNS della VPN. Puoi utilizzare i server DNS ottenuti automaticamente dai dispositivi a monte oppure specificare manualmente server DNS personalizzati.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, e la versione più recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, permettendo un numero virtualmente illimitato di indirizzi IP univoci, elemento essenziale per il crescente numero di dispositivi collegati a Internet.
    
    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping e una tecnica di ottimizzazione della rete usata negli switch Ethernet per gestire e controllare il traffico multicast.
    
    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    La pagina Network Mode consente di configurare il ruolo operativo del router in base a diverse esigenze di distribuzione della rete. È possibile scegliere varie modalità, dalla copertura Wi-Fi domestica alle reti multi-link aziendali; ciascuna modalità abilita o disabilita funzioni specifiche del router per ottimizzare le prestazioni.

    Per configurare questa funzione, consulta [Network Mode](../../interface_guide/network_mode.md).

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

    Un plugin e un componente software che aggiunge funzioni o funzionalità specifiche a un programma informatico esistente, consentendo personalizzazione e ampliamento delle sue capacità.
    
    Per configurarlo, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

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

    Tor, abbreviazione di The Onion Router, e una rete orientata alla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server gestiti da volontari (nodi) per nascondere posizione e utilizzo dell'utente, rendendo difficile tracciare le attività online.
    
    Per maggiori dettagli, consultare [Tor](../../interface_guide/tor.md).

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
    * Wi-Fi Status Schedule: imposta una pianificazione per controllare la banda Wi-Fi 5 GHz / 2.4 GHz / MLO, gestendo meglio disponibilità della rete e consumo energetico.
    
    Queste opzioni di pianificazione offrono maggiore controllo sul funzionamento del router, garantendo che soddisfi esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Display Management"

    La pagina Display Management offre una gamma completa di funzioni per gestire il touchscreen e le impostazioni correlate.
    
    - Function Management: gestisci le funzioni mostrate sul touchscreen, adattando la visualizzazione alle tue esigenze.
    - Lock Screen: personalizza le impostazioni della schermata di blocco. Puoi impostare lo sfondo e il risveglio del display.
    - Brightness: regola la luminosita del touchscreen. Usa il cursore oppure inserisci un livello specifico, da 1 a 10, per adattarlo a diverse condizioni di luce.
    - Auto Lock: imposta il ritardo di tempo per il blocco automatico dello schermo in assenza di attività. L'intervallo va da 1 a 30 minuti.
    - Screen Always On: attiva o disattiva questa opzione per decidere se il touchscreen deve restare sempre acceso oppure spegnersi dopo un periodo di inattivita.
    - Enable Screen Passcode: aggiungi un ulteriore livello di sicurezza abilitando un codice per il touchscreen.

    Per istruzioni dettagliate, fai riferimento a [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attività pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

---

=== "Toggle Button Settings"

    La pagina Toggle Button Settings consente di configurare il pulsante fisico del router, permettendo di assegnargli funzioni specifiche per un accesso e un controllo rapidi. Questa funzione offre scorciatoie pratiche per attività e impostazioni comuni, migliorando l'esperienza d'uso e semplificando la gestione del router.

    Per istruzioni dettagliate, fai riferimento a [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

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
