# Guida utente di Slate 7 Pro (GL-BE10000)

## Panoramica del prodotto

Slate 7 Pro (GL-BE10000) è un router da viaggio portatile tri-band Wi-Fi 7. Come versione aggiornata di Slate 7 (GL-BE3600), integra un touchscreen più grande nella parte superiore ed è dotato di 1 GB di RAM DDR4 e 8 GB di memoria flash eMMC per prestazioni stabili e compatibilità con i plug-in. Offre velocità VPN elevate, fino a 1.100 Mbps con WireGuard® e 1.000 Mbps con OpenVPN-DCO. Con 2 porte Ethernet da 2,5G (1 WAN + 1 LAN), 1 porta USB-C 3.0 e supporto all'alimentazione PD, garantisce connettività affidabile e praticità durante i viaggi e l'uso in mobilità.

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## Contenuto della confezione

La confezione include:

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 1 x Cavo Ethernet
- 1 x Cavo di alimentazione
- 1 x Alimentatore
- 4 x Adattatori (spine US, EU, UK e AU)

## Come configurare Slate 7 Pro

Per configurare Slate 7 Pro, puoi usare uno dei quattro metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Segui i passaggi riportati di seguito.

### 1. Accensione

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il dispositivo si avvierà automaticamente.

### 2. Touchscreen

Quando il router viene acceso, sullo schermo verrà visualizzato il logo GL.iNet, seguito dalla barra di avanzamento dell'avvio.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){class="glboxshadow" width="360"}

Una volta caricata completamente la barra di avanzamento, il dispositivo completa l'avvio ed entra nella schermata di benvenuto. Segui le indicazioni per impostare la password di amministrazione e la rete Wi-Fi.

![set admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){class="glboxshadow" width="360"}

![set WiFi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){class="glboxshadow" width="360"}

Entrerai quindi nella schermata principale. Sul lato sinistro vengono mostrate informazioni di sistema in tempo reale, tra cui ora di sistema e velocità di rete, oltre a riquadri rapidi per Wi-Fi, Client, VPN e altre funzioni. Sul lato destro sono presenti i riquadri rapidi per le quattro modalità di connessione: Ethernet, Repeater, Tethering e Cellular.

![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){class="glboxshadow" width="360"}

I diversi colori dei quattro riquadri rapidi indicano stati di rete differenti.

![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){class="glboxshadow" width="360"}

- **Blu**: attivo / connesso a Internet
- **Giallo**: connessione in corso / errore di rete
- **Bianco**: connessione inattiva

### 3. Collegare un dispositivo

Collega un dispositivo, ad esempio un computer, un portatile o uno smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router tramite un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password per connetterti. Il nome di rete predefinito (SSID) e la password sono stampati sull'etichetta del router.

### 4. Accedere al pannello di amministrazione web

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Seleziona la lingua e imposta la password di amministrazione, quindi fai clic su **Apply**.

### 5. Configurazione di Internet

Configura Slate 7 Pro usando uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}

    1. Collega la porta WAN di Slate 7 Pro a un dispositivo a monte, ad esempio un modem ISP, uno switch di rete o una presa Ethernet a muro, tramite un cavo Ethernet.
    2. Slate 7 Pro tenterà automaticamente di ottenere i parametri di rete, come indirizzo IP, gateway e server DNS, per stabilire la connessione Ethernet.
    3. Una volta connesso correttamente a Internet, la sezione Ethernet nella schermata principale del touchscreen diventerà blu (attiva). Puoi toccare Ethernet nella schermata principale del touchscreen oppure accedere al pannello di amministrazione web per verificare i dettagli della connessione.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. Tocca **Repeater** sul touchscreen. Il router inizierà a cercare le reti Wi-Fi disponibili.
    2. Seleziona la rete Wi-Fi che desideri estendere con Slate 7 Pro.
    3. Inserisci la password e tocca **Apply**.
    4. Una volta connesso correttamente a Internet, la sezione Repeater nella schermata principale del touchscreen diventerà blu (attiva). Puoi toccare Repeater nella schermata principale del touchscreen oppure accedere al pannello di amministrazione web per verificare i dettagli della connessione.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o un dongle USB, alla porta USB del router tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita **USB Tethering** o **Personal Hotspot**. Su iPhone, tocca **Trust This Device** se richiesto.
    3. Sul touchscreen, seleziona **Tethering** e tocca **Connect**. Il router si connetterà al dispositivo.
    4. Una volta connesso correttamente a Internet, la sezione Tethering nella schermata principale del touchscreen diventerà blu (attiva). Puoi toccare Tethering nella schermata principale del touchscreen oppure accedere al pannello di amministrazione web per verificare i dettagli della connessione.

    **Nota**: se la connessione non riesce, assicurati che la tensione di alimentazione sia superiore a 9V 3A, perché un'alimentazione insufficiente potrebbe impedire l'attivazione della porta USB. Ripeti i passaggi precedenti oppure accedi al pannello di amministrazione web per controllare lo stato della connessione Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. Collega un modem USB cellulare alla porta USB di Slate 7 Pro. Questo metodo è utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.
    2. Una volta connesso correttamente a Internet, la sezione Cellular nella schermata principale del touchscreen diventerà blu (attiva). Puoi toccare Cellular nella schermata principale del touchscreen oppure accedere al pannello di amministrazione web per verificare i dettagli della connessione.

---

Di seguito trovi una panoramica delle funzioni disponibili nel pannello di amministrazione web di Slate 7 Pro.

## Wireless

La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi a 6 GHz, 5 GHz e 2,4 GHz, inclusi attivazione del Wi-Fi, potenza TX, nome della rete Wi-Fi (SSID), attivazione del BSSID casuale, modalità di sicurezza Wi-Fi e password, visibilità dell'SSID, modalità Wi-Fi, larghezza di banda e canale.

Inoltre, Slate 7 Pro supporta il Wi-Fi MLO, cioè Multi-Link Operation, che combina simultaneamente più reti wireless per ottenere maggiore larghezza di banda e connessioni più affidabili.

Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

## Client

La pagina Client mostra le informazioni sui dispositivi connessi. Per ogni client vengono visualizzati nome, indirizzi IP e MAC, velocità di download e upload, traffico totale, oltre alla possibilità di bloccare il client o eseguire altre azioni.

Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.

    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp è una funzione di rete avanzata integrata nei router GL.iNet. Consente l'accesso remoto senza interruzioni alla rete domestica senza registrazione né accesso. Utilizzando il protocollo AmneziaWG con offuscamento del traffico integrato, mantiene la connessione stabile e sicura, risultando ideale per un accesso remoto affidabile ovunque ti trovi. Gli utenti possono configurare una rete AstroWarp direttamente dal pannello di amministrazione del router GL.iNet. Basta associare i router tramite un codice di accesso per collegare in modo sicuro il router da viaggio alla rete domestica in pochi secondi.

    Per configurarlo, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN (rete privata virtuale) crea traffico sicuro e crittografato tra il tuo dispositivo e il server VPN. Fornisce un ulteriore livello di privacy e sicurezza (client VPN) e consente di accedere a una rete remota (server VPN). Slate 7 Pro supporta i protocolli OpenVPN e WireGuard.

=== "OpenVPN"

    Slate 7 Pro, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 Pro, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottime velocità e praticità. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete

=== "Multi-WAN"

    Multi-WAN è una funzione di rete che consente di configurare il router con più connessioni Internet, ad esempio cellulare, repeater ed ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passerà automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarla, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, è una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimenti dati ad alta velocità e condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.

    Per configurarla, fai riferimento a [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Consente di impostare una subnet all'interno degli intervalli di indirizzi privati IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, specificare gateway e netmask e configurare impostazioni di sicurezza come l'isolamento AP per la rete ospite.

    Per configurarla, fai riferimento a [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione contro gli attacchi DNS rebinding e sovrascrivere le impostazioni DNS di tutti i client, permettere ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalità delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS della connessione Ethernet.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La pagina Ethernet Port consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare la modalità MAC e l'indirizzo MAC per l'interfaccia WAN e visualizzare la velocità negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, o Internet Protocol versione 6, è la versione più recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, consentendo un numero praticamente illimitato di indirizzi IP univoci, indispensabile per il crescente numero di dispositivi connessi a Internet.

    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping è una tecnica di ottimizzazione di rete usata negli switch Ethernet per gestire e controllare il traffico multicast.

    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network mode si riferisce alle impostazioni di configurazione che determinano come un dispositivo si collega a una rete e comunica con altri dispositivi.

    Per configurarla, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del router principale, tra cui AdGuard Home, DNS crittografato e client VPN.

    Per configurarlo, fai riferimento a questi link:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    L'accelerazione di rete può ridurre il carico della CPU e velocizzare l'inoltro dei pacchetti di traffico.

    Per configurarla, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del traffico

=== "DPI Engine"

    DPI (Deep Packet Inspection) è una funzionalità centrale della gestione intelligente della rete. Può superare i limiti dei router tradizionali, che identificano solo indirizzi di origine o destinazione, analizzare in profondità il payload dei pacchetti dati e identificare con precisione applicazioni e siti web visitati dagli utenti tramite il confronto con una libreria di firme, consentendo una classificazione e un controllo raffinati del traffico.

    Integrata con [Netify](https://www.netify.ai/){target="_blank"}, la funzione DPI di GL.iNet adotta un plug-in embedded leggero per una distribuzione efficiente. Grazie al database di firme aggiornato online da Netify, consente una gestione affidabile e rende il controllo della rete più preciso ed efficiente.

    Per istruzioni dettagliate, fai riferimento a [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics offre una dashboard intelligente di analisi del traffico che categorizza e visualizza l'utilizzo della rete per applicazione, aiutandoti a monitorare il traffico in tempo reale e storico per una migliore consapevolezza e un controllo più efficace della rete.

    Per istruzioni dettagliate, fai riferimento a [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter offre una protezione online intelligente basata sulla classificazione DPI, bloccando automaticamente siti web dannosi o malevoli per mantenere la rete pulita e sicura.

    Per istruzioni dettagliate, fai riferimento a [Content Filter](../../interface_guide/content_filter.md).

---

=== "Parental Control"

    Parental Control è progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) ottimizza l'allocazione della larghezza di banda dando priorità alle attività critiche, ad esempio videochiamate o gaming, durante la congestione della rete, riducendo la latenza e migliorando le prestazioni complessive. Tieni presente che si applica al traffico dei client locali e al traffico dei tunnel client VPN, ma non al traffico ricevuto quando il router funziona come server VPN.

    Per istruzioni dettagliate, fai riferimento a [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo latenza e "bufferbloat", garantendo giochi online e chiamate vocali più fluidi.

    Per istruzioni dettagliate, fai riferimento a [SQM](../../interface_guide/sqm.md).

## Sicurezza

=== "Port Forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere ai dispositivi presenti in una rete privata.

    Per configurarlo, fai riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Management Control consente di configurare diverse impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include le seguenti opzioni:

    * Local Access Control: gestisci e limita l'accesso all'interfaccia del router da parte dei dispositivi collegati alla rete locale.
    * Remote Access Control: configura e limita l'accesso all'interfaccia del router da posizioni remote via Internet, migliorando la protezione contro minacce esterne.
    * Open Ports on Router: controlla quali porte sono aperte sul router, limitando potenziali vulnerabilità e accessi non autorizzati.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate, fai riferimento a [Security](../../interface_guide/security.md).

=== "NAT Mode"

    La pagina NAT Mode consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG (Application Layer Gateway).

    Per configurare le impostazioni NAT, fai riferimento a [NAT Mode](../../interface_guide/nat_settings.md).

## Applicazioni

=== "Plug-ins"

    Un plug-in è un componente software che aggiunge funzionalità specifiche a un programma informatico esistente, consentendo personalizzazione ed espansione delle sue capacità.

    Per configurarli, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva e aggiorna automaticamente in tempo reale l'indirizzo IP associato a un dominio. È particolarmente utile per chi ha bisogno di un indirizzo IP statico per accedere a una rete remota.

    Per configurarlo, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage si riferisce a una soluzione di archiviazione dati centralizzata che consente a più utenti e dispositivi di accedere ai file e condividerli tramite una rete.

    Per configurarlo, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home è una soluzione di blocco di annunci e tracker a livello di rete che agisce come server DNS per filtrare contenuti indesiderati su tutti i dispositivi connessi alla rete domestica.

    Per configurarlo, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale è un servizio VPN che consente di accedere a dispositivi e applicazioni ovunque ti trovi.

    Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier è una soluzione di rete software-defined che consente di creare reti virtuali sicure su Internet, collegando i dispositivi come se si trovassero sulla stessa rete locale.

    Per configurarlo, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abbreviazione di The Onion Router, è una rete orientata alla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server volontari, chiamati nodi, per nascondere la posizione e l'utilizzo dell'utente, rendendo difficile tracciare le attività online.

    * [Come configurare Tor](../../interface_guide/tor.md)

## Sistema

=== "Overview"

    La pagina Overview fornisce una panoramica completa dello stato attuale del router e delle sue metriche di prestazione. In questa pagina puoi visualizzare:

    * CPU Average Load: monitora il carico medio della CPU del router per valutare le prestazioni e identificare eventuali colli di bottiglia.
    * Memory Usage: controlla quanta memoria del router è in uso, per gestire meglio le risorse.
    * LED Control: attiva o disattiva i LED del router, personalizzando gli indicatori visivi del dispositivo.
    * Flash Usage: visualizza l'utilizzo della memoria flash del router, per assicurarti che ci sia spazio sufficiente per firmware e dati di configurazione.
    * Device Info: accedi a informazioni dettagliate sul sistema del router, tra cui uptime, hostname, modello, architettura, versione di OpenWrt, versione del kernel, ID del dispositivo, MAC del dispositivo e S/N del dispositivo.
    * External Storage: controlla lo stato di eventuali dispositivi di archiviazione esterni collegati al router, come unità USB o schede TF.

    Queste funzioni forniscono informazioni e controlli essenziali per gestire e monitorare in modo efficace il funzionamento del router.

    Per istruzioni dettagliate, fai riferimento a [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La pagina Admin Password consente di impostare o modificare la password dell'interfaccia amministrativa del router, in modo che solo gli utenti autorizzati possano modificare le impostazioni.

    Per motivi di sicurezza, consigliamo di attivare **Prevent Weak Password**.

    Quando **Prevent Weak Password** è attivo, i requisiti per le nuove password sono i seguenti.

    * 5 caratteri e massimo 63 caratteri.
    * Sono consentiti lettere (con distinzione tra maiuscole e minuscole), numeri e simboli `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Sono richieste almeno due tra lettere maiuscole, lettere minuscole, numeri e simboli.

    Per istruzioni dettagliate, fai riferimento a [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    La pagina Upgrade viene usata per aggiornare il firmware del router all'ultima versione, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Firmware Online Upgrade: verifica e installa automaticamente l'ultima versione del firmware direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Firmware Local Upgrade: carica manualmente dal computer un file firmware per aggiornare il router, permettendo di controllare versione e tempistica dell'aggiornamento.

    Queste opzioni consentono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare varie funzioni del router in base a una pianificazione predefinita, migliorando comodità ed efficienza. Le funzioni principali di questa pagina includono:

    * LCD Display Schedule: imposta una pianificazione per accendere o spegnere automaticamente il display LCD del router, riducendo l'inquinamento luminoso in determinate fasce orarie.
    * Schedule Reboot: configura il riavvio automatico del router a intervalli specificati, contribuendo a mantenere prestazioni e stabilità ottimali.
    * Wi-Fi Status Schedule: imposta una pianificazione per controllare le bande Wi-Fi 6 GHz / 5 GHz / 2,4 GHz / MLO, migliorando la gestione della disponibilità della rete e dei consumi energetici.

    Queste opzioni di pianificazione ti offrono un maggiore controllo sul funzionamento del router, così da adattarlo alle tue esigenze e preferenze.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Display Management"

    La pagina Display Management offre una gamma completa di funzioni per gestire il touchscreen e le impostazioni correlate.

    ‒ Wallpaper: personalizza lo sfondo e lo stile di riattivazione del display.
    ‒ Brightness: regola la luminosità del touchscreen. Usa il cursore o inserisci una percentuale specifica per adattarla alle diverse condizioni di luce.
    ‒ Auto Lock: imposta il ritardo prima del blocco automatico dello schermo quando non c'è attività. L'intervallo va da 1 minuto a 30 minuti.
    ‒ Screen Always On: attiva o disattiva questa opzione per decidere se il touchscreen deve rimanere sempre acceso oppure spegnersi dopo un periodo di inattività.
    ‒ Enable Screen Passcode: imposta un codice per il touchscreen per un ulteriore livello di sicurezza.

    Per istruzioni dettagliate, fai riferimento a [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attività pianificate, i log e gli eventi di sistema abbiano timestamp accurati in base all'ora locale. Questa impostazione è fondamentale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sul tempo.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

---

=== "Toggle Button Settings"

    La pagina Toggle Button Settings consente di configurare il pulsante fisico a levetta del router, permettendoti di assegnargli funzioni specifiche per un accesso e un controllo rapidi. Questa funzione offre scorciatoie pratiche per attività e impostazioni comuni, migliorando l'esperienza d'uso e semplificando la gestione del router.

    Per istruzioni dettagliate, fai riferimento a [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare alle impostazioni predefinite la versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporterà il router alle impostazioni predefinite della versione firmware corrente. Può essere utile per risolvere problemi persistenti oppure per ripartire da una configurazione pulita del firmware attuale.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La pagina Log consente di accedere ai vari registri che tengono traccia delle attività e degli eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati degli eventi e delle attività di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di crash di sistema ed errori, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attività relative ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se utilizzato dal router, con dettagli sul traffico web e sulle operazioni del server.

    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione è preziosa per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La pagina Advanced Settings consente di accedere alle opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, permettendo agli utenti esperti di regolare con precisione impostazioni e funzionalità del router oltre le opzioni dell'interfaccia di base. Ciò include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
