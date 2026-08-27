# Guida utente di Flint 4 (GL-BE14000)

## Panoramica del prodotto

Flint 4 (GL‑BE14000) ridefinisce le possibilità di un router domestico. È dotato di Wi‑Fi 7 tri-band con MLO e raggiunge velocità di picco di 688 Mbps (2.4 GHz) + 4323 Mbps (5 GHz) + 8646 Mbps (6 GHz). Per le connessioni cablate offre una dorsale multi-gigabit completa, con una porta 10G SFP+ WAN/LAN, una porta 10GE WAN/LAN, una porta 2.5GE WAN/LAN, tre porte 2.5GE LAN e quattro porte 1GE LAN. Per le VPN ad alte prestazioni raggiunge un throughput fino a 1.5 Gbps sia con WireGuard® sia con OpenVPN DCO. Integra inoltre un display touchscreen da 2.4 pollici per monitorare in tempo reale lo stato della rete e visualizzare direttamente sul dispositivo i principali parametri di rete.

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## Contenuto della confezione

- 1 x Flint 4 (GL-BE14000)
- 1 x Alimentatore
- 1 x Cavo Ethernet
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 1 x Adattatore (in base al paese di spedizione)

Di seguito è disponibile il video di unboxing di Flint 4.

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configurare Flint 4

Guardare il video di configurazione oppure seguire i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Accensione

Assemblare le due parti dell'alimentatore. Collegarlo al router e a una presa di corrente. Il router si avvierà automaticamente.

### 2. Collegamento di un dispositivo

Collegare un dispositivo, ad esempio un computer, un portatile o uno smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collegare il dispositivo a una porta LAN del router con un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, individuare il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e immettere la password. Il nome di rete (SSID) e la password predefiniti sono stampati sull'etichetta del router.

### 3. Accesso al pannello di amministrazione web

Aprire un browser web, immettere `192.168.8.1` nella barra degli indirizzi e accedere. Impostare la password di amministrazione e i dati Wi-Fi, quindi fare clic su **Apply**.

### 4. Configurazione di Internet

Configurare Flint 4 mediante uno dei metodi di connessione supportati: Ethernet (SFP+), Ethernet (RJ45), Repeater, Tethering e Cellular. Per utilizzare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configurare più di una connessione Internet.

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}
    
    Flint 4 dispone di una porta 10G SFP+ WAN/LAN, progettata per uplink in fibra, backhaul di switch ad alta velocità ed espansione di rete ad alte prestazioni. Per impostazione predefinita la porta è configurata come WAN, ma può essere commutata su LAN.

    Nell'esempio seguente, la porta 10G SFP+ di Flint 4 viene collegata all'uplink in fibra dell'ISP tramite un ricetrasmettitore ottico e un cavo in fibra. Per altre soluzioni, consultare [Collegare la porta 10G SFP+ di Flint 4](../../faq/connecting_10g_sfp_plus_port_on_flint4.md).

    1. Inserire un ricetrasmettitore 10G SFP+ compatibile nella porta SFP+ di Flint 4, quindi collegarlo all'uplink in fibra dell'ISP.  
    2. Flint 4 tenta di ottenere automaticamente tramite DHCP i parametri di rete (indirizzo IP, gateway e DNS). Se l'ISP richiede PPPoE o un indirizzo IP statico, modificare le impostazioni della connessione WAN nel pannello di amministrazione web.
    3. Una volta stabilita la connessione a Internet, la sezione Ethernet nella pagina iniziale del touchscreen diventa blu (attiva). Toccare Ethernet sul touchscreen oppure accedere al pannello di amministrazione web per visualizzare i dettagli della connessione.

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}
    
    1. Collegare la porta WAN di Flint 4 a un dispositivo a monte, ad esempio un modem ISP, uno switch di rete o una presa Ethernet a muro, utilizzando un cavo Ethernet.
    2. Flint 4 tenta di ottenere automaticamente tramite DHCP i parametri di rete (indirizzo IP, gateway e DNS). Se l'ISP richiede PPPoE o un indirizzo IP statico, modificare le impostazioni della connessione WAN nel pannello di amministrazione web.
    3. Una volta stabilita la connessione a Internet, la sezione Ethernet nella pagina iniziale del touchscreen diventa blu (attiva). Toccare Ethernet sul touchscreen oppure accedere al pannello di amministrazione web per visualizzare i dettagli della connessione.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. Toccare **Repeater** sul touchscreen. Il router inizierà a cercare le reti Wi-Fi disponibili.
    2. Selezionare la rete Wi-Fi che Flint 4 deve estendere.
    3. Immettere la password e toccare **Apply**.
    4. Una volta stabilita la connessione a Internet, la sezione Repeater nella pagina iniziale del touchscreen diventa blu (attiva). Toccare Repeater sul touchscreen oppure accedere al pannello di amministrazione web per visualizzare i dettagli della connessione.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. Collegare un dispositivo mobile, ad esempio uno smartphone, alla porta USB di Flint 4 con un cavo USB.
    2. Sul dispositivo mobile, aprire Settings e abilitare **USB Tethering** o **Personal Hotspot**. Su iPhone, toccare **Trust This Device** se richiesto.
    3. Sul touchscreen di Flint 4, selezionare **Tethering** e toccare **Connect**. Il router si collegherà al dispositivo.
    4. Una volta stabilita la connessione a Internet, la sezione Tethering nella pagina iniziale del touchscreen diventa blu (attiva). Toccare Tethering sul touchscreen oppure accedere al pannello di amministrazione web per visualizzare i dettagli della connessione.

    **Nota**: se la connessione non riesce, verificare che l'alimentatore fornisca 12V 4A, perché una potenza insufficiente può impedire l'alimentazione della porta USB. Ripetere i passaggi oppure accedere al pannello di amministrazione web per verificare lo stato della connessione Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. Inserire un modem cellulare o un dongle USB nella porta USB di Flint 4. In questo modo è possibile condividere la connessione Internet del modem USB con tutti i dispositivi connessi.
    2. Una volta stabilita la connessione a Internet, la sezione Cellular nella pagina iniziale del touchscreen diventa blu (attiva). Toccare Cellular sul touchscreen oppure accedere al pannello di amministrazione web per visualizzare i dettagli della connessione.

---

Di seguito viene fornita una panoramica delle funzioni disponibili nel pannello di amministrazione web di Flint 4.

## Wireless

La pagina Wireless consente di configurare le diverse reti Wi-Fi di Flint 4, tra cui MLO Wi-Fi, Main Network, Guest Network e IoT Network.

Per maggiori dettagli, consultare [Wireless](../../interface_guide/wireless.md).

## Client

La pagina Clients mostra le informazioni sui dispositivi connessi. Per ogni client sono disponibili nome, indirizzi IP e MAC, velocità di download e upload, traffico totale e le azioni per bloccarlo o gestirlo.

Per maggiori dettagli, consultare [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice per accedere e gestire da remoto i router GL.iNet.
    
    Per maggiori dettagli, consultare [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp è una funzione di rete avanzata integrata nei router GL.iNet. Consente di accedere da remoto alla rete domestica senza registrazione o login. Il protocollo AmneziaWG con offuscamento del traffico integrato mantiene la connessione stabile e sicura, offrendo un accesso remoto affidabile ovunque. È possibile configurare una rete AstroWarp direttamente nel pannello di amministrazione del router GL.iNet. Basta associare i router mediante un codice di accesso per collegare in modo sicuro il router da viaggio alla rete domestica in pochi secondi.
    
    Per maggiori dettagli, consultare [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN (rete privata virtuale) crea un canale di traffico sicuro e crittografato tra il dispositivo e il server VPN. Aggiunge un livello di privacy e sicurezza (client VPN) e consente l'accesso a una rete remota (server VPN). Flint 4 supporta i protocolli OpenVPN e WireGuard.

=== "OpenVPN"
    
    Flint 4 e gli altri router GL.iNet supportano il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurarlo, consultare le guide seguenti:

    * [Configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4 e gli altri router GL.iNet supportano il protocollo WireGuard, che offre velocità elevate e praticità. Per configurarlo, consultare le guide seguenti:

    * [Configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete

=== "Multi-WAN"

    Multi-WAN consente di configurare contemporaneamente più connessioni Internet sul router, ad esempio cellulare, repeater ed Ethernet. Se la connessione corrente si interrompe, il router passa automaticamente a un'altra connessione, garantendo un accesso a Internet continuo.

    Per maggiori dettagli, consultare [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    La pagina Subnet centralizza la gestione di LAN, Guest Network, IoT Network e reti VLAN personalizzate, consentendo di creare e gestire più sottoreti per isolare diversi tipi di dispositivi o traffico.

    Per maggiori dettagli, consultare [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La pagina Ethernet Port consente di gestire il ruolo delle porte Ethernet (WAN/LAN) e la segmentazione VLAN, oltre a visualizzare dettagli quali indirizzo MAC e velocità negoziata.

    Per maggiori dettagli, consultare [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione contro gli attacchi DNS rebinding, sostituire le impostazioni DNS di tutti i client, permettere al DNS personalizzato di sostituire il DNS della VPN e configurare automaticamente o manualmente i server DNS della connessione Ethernet.

    Per maggiori dettagli, consultare [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, o Internet Protocol versione 6, è la versione più recente del protocollo Internet e sostituisce IPv4. Offre uno spazio di indirizzi molto più ampio e un numero praticamente illimitato di indirizzi IP univoci, necessario per il crescente numero di dispositivi connessi a Internet.
    
    Per maggiori dettagli, consultare [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping è una tecnica di ottimizzazione utilizzata negli switch Ethernet per gestire e controllare il traffico multicast.
    
    Per maggiori dettagli, consultare [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Network Mode indica i diversi ruoli e le funzioni operative che un router può assumere per soddisfare le esigenze di implementazione della rete. Le modalità comuni includono Router Mode, Extender Mode e Access Point Mode.
    
    Per maggiori dettagli, consultare [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway consente di ampliare le funzionalità di un router principale esistente senza sostituirlo o riconfigurarlo. Impostando un router GL.iNet come Drop-in Gateway, è possibile aggiungere alla rete esistente funzioni avanzate quali AdGuard Home, VPN e DNS crittografato.

    Per configurare Drop-in Gateway, consultare i link seguenti.
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network Acceleration riduce il carico della CPU e velocizza l'inoltro dei pacchetti di traffico.
    
    Per maggiori dettagli, consultare [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del traffico

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

    Per maggiori dettagli, consultare [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Sicurezza

=== "Port Forwarding"

    Port Forwarding consente a server e dispositivi remoti su Internet di accedere ai dispositivi di una rete privata.
    
    Per maggiori dettagli, consultare [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, acronimo di Access Control List, consente di creare regole per gestire il traffico di rete in base a protocolli di connessione, indirizzi dei dispositivi e porte. Le regole stabiliscono se consentire o bloccare l'accesso alla rete. In caso di conflitto tra più regole ACL, il sistema applica quella con priorità più alta.

    Per maggiori dettagli, consultare [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access consente di configurare diverse impostazioni di sicurezza per proteggere la rete e il router dagli accessi non autorizzati. La pagina include le opzioni seguenti:

    * Local Access Control: gestisce e limita l'accesso all'interfaccia del router dai dispositivi connessi alla rete locale.
    * Remote Access Control: configura e limita l'accesso all'interfaccia del router da posizioni remote tramite Internet, aumentando la protezione dalle minacce esterne.
    * Open Ports on Router: controlla quali porte sono aperte sul router, limitando potenziali vulnerabilità e accessi non autorizzati.

    Per maggiori dettagli, consultare [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La pagina NAT Mode consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG (Application Layer Gateway).

    Per maggiori dettagli, consultare [NAT Mode](../../interface_guide/nat_settings.md).

## Applicazioni

=== "Plug-ins"

    Un plug-in è un componente software che aggiunge funzioni specifiche a un programma esistente, consentendone la personalizzazione e l'estensione.
    
    Per maggiori dettagli, consultare [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva e aggiorna automaticamente in tempo reale l'indirizzo IP associato a un dominio. È particolarmente utile per chi necessita di un indirizzo IP statico per accedere a una rete remota.
    
    Per maggiori dettagli, consultare [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage è una soluzione centralizzata per l'archiviazione dei dati che consente a più utenti e dispositivi di accedere e condividere file tramite una rete.
    
    Per maggiori dettagli, consultare [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home è una soluzione per il blocco di annunci pubblicitari e tracker a livello di rete. Funziona come server DNS e filtra i contenuti indesiderati su tutti i dispositivi connessi alla rete domestica.
    
    Per maggiori dettagli, consultare [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    Il servizio Bark integrato in Flint 4 aiuta a proteggere l'ambiente digitale dei bambini e offre una protezione online completa. In genere richiede un abbonamento a pagamento. Tuttavia, grazie alla partnership con Bark, GL.iNet offre gratuitamente il piano Bark Home su alcuni modelli di router, incluso Flint 4, fornendo monitoraggio avanzato e avvisi senza costi aggiuntivi.

    Per maggiori dettagli, consultare [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale è un servizio VPN che consente di accedere ovunque ai propri dispositivi e applicazioni.
    
    Per maggiori dettagli, consultare [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier è una soluzione di rete definita dal software che permette di creare reti virtuali sicure tramite Internet, collegando i dispositivi come se si trovassero sulla stessa rete locale.
    
    Per maggiori dettagli, consultare [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abbreviazione di The Onion Router, è una rete orientata alla privacy che consente comunicazioni anonime tramite Internet. Instrada il traffico attraverso una serie di server (nodi) gestiti da volontari per nascondere la posizione e l'utilizzo dell'utente, rendendo difficile tracciare le attività online.
    
    Per maggiori dettagli, consultare [Tor](../../interface_guide/tor.md).

## Sistema

=== "Overview"

    La pagina Overview fornisce un quadro completo dello stato corrente e delle metriche delle prestazioni del router. È possibile visualizzare:

    * CPU Average Load: carico medio della CPU del router, utile per valutare le prestazioni e individuare eventuali colli di bottiglia.
    * Memory Usage: quantità di memoria utilizzata dal router, utile per la gestione delle risorse.
    * Flash Usage: utilizzo della memoria flash del router, per verificare che vi sia spazio sufficiente per firmware e dati di configurazione.
    * Device Info: informazioni dettagliate sul sistema, tra cui tempo di attività, nome host, modello, architettura, versione OpenWrt, versione del kernel, ID dispositivo, MAC del dispositivo e numero di serie.
    * External Storage: stato dei dispositivi di archiviazione esterni collegati al router, ad esempio unità USB o schede TF.
    
    Queste funzioni forniscono informazioni e controlli essenziali per gestire e monitorare efficacemente il funzionamento del router.

    Per maggiori dettagli, consultare [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La pagina Admin Password consente di gestire la password dell'interfaccia di amministrazione, in modo che solo gli utenti autorizzati possano modificare le impostazioni.

    Per maggiori dettagli, consultare [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    La pagina Upgrade consente di aggiornare il firmware del router alla versione più recente, ottenendo miglioramenti delle prestazioni e della sicurezza e nuove funzioni. Sono disponibili due opzioni:

    * Firmware Online Upgrade: verifica automaticamente sul server del produttore la disponibilità della versione firmware più recente, che può essere installata quando è disponibile online.
    * Firmware Local Upgrade: consente di caricare manualmente dal computer un file firmware, scegliendo la versione e il momento dell'aggiornamento.

    Per maggiori dettagli, consultare [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita. Le principali funzioni includono:

    * LCD Display Schedule: imposta gli orari di accensione e spegnimento automatici del display LCD, riducendo l'illuminazione indesiderata in determinati periodi.
    * Schedule Reboot: riavvia automaticamente il router agli intervalli specificati, contribuendo a mantenere prestazioni e stabilità ottimali.
    * Wi-Fi Status Schedule: imposta una pianificazione per controllare le bande Wi-Fi 6GHz / 5GHz / 2.4GHz / MLO, gestendo la disponibilità della rete e riducendo il consumo energetico.
    
    Queste opzioni offrono un maggiore controllo sul funzionamento del router e consentono di adattarlo alle esigenze specifiche.

    Per maggiori dettagli, consultare [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).
    
=== "Display Management"

    La pagina Display Management offre una serie completa di funzioni per gestire il touchscreen e le relative impostazioni.

    ‒ Wallpaper: personalizza lo sfondo e lo stile di riattivazione del display.
    ‒ Brightness: regola la luminosità del touchscreen mediante il cursore o immettendo una percentuale specifica in base alle condizioni di illuminazione.
    ‒ Auto Lock: imposta il ritardo prima del blocco automatico dello schermo in assenza di attività, da 1 a 30 minuti.
    ‒ Screen Always On: stabilisce se il touchscreen deve rimanere sempre acceso o spegnersi dopo un periodo di inattività.
    ‒ Enable Screen Passcode: imposta un codice di accesso per aggiungere un ulteriore livello di sicurezza al touchscreen.

    Per maggiori dettagli, consultare [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto del router, affinché attività pianificate, registri ed eventi di sistema riportino l'ora locale esatta. L'impostazione è essenziale per registrazioni precise e per l'esecuzione corretta delle configurazioni basate sull'ora.

    Per maggiori dettagli, consultare [Time Zone](../../interface_guide/time_zone.md).

---

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware corrente, eliminando tutte le configurazioni personalizzate. Può essere utile per risolvere problemi persistenti o ricominciare dalla configurazione predefinita del firmware installato.

    Per maggiori dettagli, consultare [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La pagina Log consente di accedere a diversi registri delle attività e degli eventi del router, utili per la risoluzione dei problemi e il monitoraggio delle prestazioni. Include:

    * System Log: registro dettagliato degli eventi e delle attività a livello di sistema.
    * Kernel Log: registro delle operazioni e degli eventi del kernel.
    * Crash Log: record degli arresti anomali e degli errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: registro delle interazioni e delle attività relative ai servizi GoodCloud integrati nel router.
    * Nginx Log: registro del server web Nginx, se utilizzato dal router, con i dettagli del traffico web e delle operazioni del server.
    
    La pagina include inoltre il pulsante Export Log, che consente di esportare tutti i registri raccolti per l'analisi da parte dell'assistenza tecnica. Questa funzione è utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per maggiori dettagli, consultare [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La pagina Advanced Settings consente di accedere alle opzioni di configurazione avanzate tramite l'interfaccia OpenWrt LuCI. Gli utenti esperti possono così regolare le impostazioni e le funzioni del router oltre le opzioni dell'interfaccia di base, incluse configurazioni di rete dettagliate, impostazioni del firewall e altre personalizzazioni avanzate del sistema.

    Per maggiori dettagli, consultare [Advanced Settings](../../interface_guide/advanced_settings.md).

## Dichiarazione di conformità

GL TECHNOLOGIES (HONG KONG) LIMITED dichiara che il tipo di apparecchiatura radio [BE14000 Wi-Fi 7 Router, GL-BE14000] è conforme ai requisiti essenziali e alle altre disposizioni pertinenti della Direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile all'indirizzo [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.

Per l'UE:<br>
Potenza massima in uscita:<br>
CE: ≤20dBm EIRP (2.412GHz~2.472GHz); ≤23dBm EIRP (5.15GHz~5.35GHz); ≤30dBm EIRP (5.47GHz~5.725GHz); ≤13.98dBm (5.725GHz~5.85GHz); ≤23dBm EIRP (5.925GHz~6.425 GHz)
