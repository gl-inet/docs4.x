# Guida utente di Mango 2 (GL-MG1300)

## Panoramica del prodotto

Mango 2 (GL-MG1300) è il primo mini router da viaggio Wi-Fi 5 dual-band di GL.iNet, caratterizzato da un design ultrasottile e portatile. Offre velocità teoriche di 400 Mbps (2,4 GHz) e 866 Mbps (5 GHz), con configurazione MIMO 2×2. Inoltre, include OpenVPN e WireGuard preinstallati, supporta oltre 30 servizi VPN, crittografa automaticamente tutto il traffico di rete e consente la gestione remota tramite GoodCloud, coniugando prestazioni, praticità e sicurezza.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## Contenuto della confezione

- 1 x Mango 2 (GL-MG1300)
- 1 x Manuale utente
- 1 x Cavo di alimentazione da USB-C a USB-C
- 1 x Biglietto di ringraziamento

## Come configurare Mango 2

Per configurare Mango 2, utilizza uno dei quattro metodi di connessione Internet supportati: Ethernet, Repeater, Tethering o Cellular. Segui i passaggi riportati di seguito.

### 1. Accendi il router

Collega il cavo di alimentazione USB Type-C alla porta di alimentazione del router. Collega l'altra estremità a un alimentatore da 5 V/2 A (non incluso), quindi inseriscilo in una presa elettrica.

### 2. Collega un dispositivo

Collega un dispositivo (ad esempio computer, laptop o smartphone) al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, apri Settings -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password. Il nome e la password predefiniti sono riportati sull'etichetta nella parte inferiore del router.

### 3. Accedi al pannello di amministrazione web

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua, imposta la password amministratore, quindi fai clic su **Apply**.

Se modifichi le informazioni Wi-Fi, dovrai riconnettere il dispositivo alla rete Wi-Fi del router utilizzando le credenziali aggiornate.

### 4. Configurazione della connessione Internet

**Nota:** Le seguenti istruzioni si applicano agli utenti che configurano il router tramite il GL.iNet Web Admin Panel. Se preferisci utilizzare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni visualizzate.

Configura Mango 2 utilizzando uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering o Cellular. Per utilizzare [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Collega la porta WAN di Mango 2 a un dispositivo upstream, ad esempio un modem, tramite un cavo Ethernet.

    Quando la connessione a Internet va a buon fine, nella sezione Ethernet della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. Nella pagina INTERNET del pannello di amministrazione web, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password, quindi fai clic su **Apply**.

    Quando la connessione a Internet va a buon fine, nella sezione Repeater della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o un dongle USB, alla porta USB di Mango 2 tramite un cavo USB.
    2. Sul dispositivo mobile, apri Settings e abilita **USB Tethering** o **Personal Hotspot**. Su iPhone, tocca **Trust This Device** se richiesto.
    3. Nella pagina INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.

    Quando la connessione a Internet va a buon fine, nella sezione Tethering della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Con Mango 2 puoi collegare direttamente un modem USB-C oppure utilizzare un adattatore da USB-C a USB-A per collegare un modem USB-A.

    Inserisci un modem USB cellulare nella porta USB di Mango 2. Questo metodo e utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

    Quando la connessione a Internet va a buon fine, nella sezione Cellular della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

---

Di seguito è riportata una panoramica delle funzioni del pannello di amministrazione web di Mango 2.

## Wireless

La pagina Wireless consente di configurare Main Network, Guest Network e IoT Network. Per ogni tipo di rete Wi-Fi è possibile configurare separatamente le bande a 5 GHz e 2,4 GHz. È inoltre possibile abilitare e definire le impostazioni di base di ciascuna banda, tra cui SSID Wi-Fi, modalità di sicurezza, password e BSSID casuale.

Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

## Client

La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza nome, indirizzi IP e MAC, velocita di download e upload, traffico totale e offre la possibilita di bloccare il client o eseguire altre azioni.

Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GL.iNet Account"

    GL.iNet Account consente di collegare e gestire dispositivi e servizi cloud. Puoi accedere agevolmente sia a GoodCloud sia alla glinet App, gestendo la rete in modo sicuro e pratico ovunque e in qualsiasi momento.

    Per configurare GL.iNet Account, consulta [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} consente di accedere e gestire da remoto i router GL.iNet in modo semplice.

=== "GoodPAS"

    GoodPAS è una funzione di rete avanzata progettata per offrire accesso remoto e gestione dei dispositivi senza interruzioni. Sviluppato appositamente per l'integrazione con i router GL.iNet, GoodPAS utilizza il protocollo AmneziaWG con offuscamento del traffico integrato per garantire connessioni sicure e stabili. Estende in modo sicuro la rete domestica a livello globale, consentendo di accedere alle risorse di casa mentre tutto il traffico sembra provenire dall'indirizzo IP pubblico domestico.

## VPN

Una VPN (rete privata virtuale) crea una connessione sicura e crittografata tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza (client VPN) e consente di accedere a una rete remota (server VPN). Mango 2 supporta OpenVPN e WireGuard.

=== "OpenVPN"

    Mango 2, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocita e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet, ad esempio cellular, repeater ed ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Subnet centralizza la gestione di LAN, Guest Network, IoT Network e reti VLAN personalizzate, consentendo di creare e gestire più sottoreti per isolare diversi tipi di dispositivi o traffico.

    Per configurare questa funzione, consulta [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La pagina Ethernet Port consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare la modalita MAC e l'indirizzo MAC per l'interfaccia WAN e visualizzare la velocita negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione dagli attacchi DNS rebinding e sovrascrivere le impostazioni DNS di tutti i client, consentire ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalita delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS dalla connessione Ethernet.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, e la versione piu recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto piu ampio, permettendo un numero virtualmente illimitato di indirizzi IP univoci, elemento essenziale per il crescente numero di dispositivi collegati a Internet.

    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping e una tecnica di ottimizzazione della rete usata negli switch Ethernet per gestire e controllare il traffico multicast.

    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    La pagina Network Mode consente di configurare il ruolo operativo del router in base a diverse esigenze di distribuzione della rete. È possibile scegliere varie modalità, dalla copertura Wi-Fi domestica alle reti multi-link aziendali; ciascuna modalità abilita o disabilita funzioni specifiche del router per ottimizzare le prestazioni.

    Per configurare questa funzione, consulta [Network Mode](../../interface_guide/network_mode.md).

=== "Network Acceleration"

    Network acceleration puo ridurre il carico della CPU e accelerare l'inoltro dei pacchetti di traffico.

    Per configurarla, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del flusso

=== "Parental Control"

    Parental Control e progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental controls](../../interface_guide/parental_control.md).

## Sicurezza

=== "Port Forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere a dispositivi all'interno di una rete privata.

    Per configurarlo, fai riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Admin Access"

    Admin Access consente di configurare diverse impostazioni di sicurezza progettate per proteggere la rete e il router da accessi non autorizzati.

    Per configurare questa funzione, consulta [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La pagina NAT Settings consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG.

    Per configurarla, fai riferimento a [NAT Settings](../../interface_guide/nat_settings.md).

## Applicazioni

=== "Plug-ins"

    Un plug-in e un componente software che aggiunge funzioni o funzionalita specifiche a un programma informatico esistente, consentendo personalizzazione e ampliamento delle sue capacita.

    Per configurarli, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva automaticamente e aggiorna in tempo reale l'indirizzo IP associato a un dominio. E utile per gli utenti che hanno bisogno di un indirizzo IP statico per accedere a una rete remota.

    Per configurarlo, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage indica una soluzione centralizzata di archiviazione dati che consente a piu utenti e dispositivi di accedere e condividere file tramite una rete.

    Per configurarlo, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

=== "Tailscale"

    Tailscale e un servizio VPN che consente di accedere ai dispositivi e alle applicazioni ovunque.

    Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

## Sistema

=== "Overview"

    La pagina Overview fornisce una panoramica completa dello stato attuale del router e delle relative metriche di prestazione. In questa pagina puoi visualizzare:

    * CPU Average Load: monitora il carico medio della CPU del router per valutare le prestazioni e individuare eventuali colli di bottiglia.
    * Memory Usage: controlla quanta memoria del router e in uso, facilitando la gestione delle risorse.
    * LED Control: attiva o disattiva i LED del router, personalizzando gli indicatori visivi del dispositivo.
    * Flash: visualizza l'utilizzo della memoria flash del router, assicurandoti che ci sia spazio sufficiente per firmware e dati di configurazione.
    * Device Info: accedi a informazioni dettagliate sul sistema del router, tra cui uptime, hostname, modello, architettura, versione OpenWrt, versione del kernel, ID dispositivo, MAC del dispositivo e numero di serie.
    * External Storage: controlla lo stato di eventuali dispositivi di archiviazione esterni collegati al router, ad esempio unita USB o schede TF.

    Queste funzioni offrono informazioni e controlli essenziali per gestire e monitorare in modo efficace il funzionamento del router.

    Per istruzioni dettagliate, fai riferimento a [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La pagina Admin Password consente di impostare o modificare la password dell'interfaccia di amministrazione del router.

    La password amministratore deve soddisfare i seguenti requisiti:

    * Minimo 10 caratteri e massimo 63 caratteri.
    * Sono consentiti lettere (con distinzione tra maiuscole e minuscole), numeri e i simboli `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Sono richiesti almeno due tipi tra lettere maiuscole, lettere minuscole, numeri e simboli.

=== "Upgrade"

    La pagina Upgrade viene usata per aggiornare il firmware del router alla versione piu recente, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Firmware Online Upgrade: controlla e installa automaticamente la versione firmware piu recente direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Firmware Local Upgrade: consente di caricare manualmente un file firmware dal computer per aggiornare il router, offrendo controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni permettono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando praticita ed efficienza. Le funzioni principali di questa pagina includono:

    * LED Control: attiva o disattiva i LED del router, personalizzando gli indicatori visivi del dispositivo.
    * Schedule Reboot: configura il riavvio automatico del router a intervalli specifici per mantenere prestazioni e stabilita ottimali.
    * Wi-Fi Status Schedule: imposta una pianificazione per controllare la banda Wi-Fi a 5 GHz / 2,4 GHz , gestendo meglio disponibilita della rete e consumo energetico.

    Queste opzioni di pianificazione offrono maggiore controllo sul funzionamento del router, garantendo che soddisfi esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attivita pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La pagina Toggle Button Settings consente di configurare il pulsante fisico del router, permettendo di assegnargli funzioni specifiche per un accesso e un controllo rapidi. Questa funzione offre scorciatoie pratiche per attivita e impostazioni comuni, migliorando l'esperienza d'uso e semplificando la gestione del router.

    Per istruzioni dettagliate, fai riferimento a [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporta il router alle impostazioni di default della versione firmware corrente. Puo essere utile per risolvere problemi persistenti o per ricominciare da zero con la configurazione predefinita del firmware attuale.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La pagina Log offre accesso a vari registri che memorizzano attivita ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati relativi a eventi e attivita a livello di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attivita legate ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se usato dal router, che riportano traffico web e operazioni del server.

    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione e molto utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La pagina Advanced Settings offre accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in modo dettagliato impostazioni e funzioni del router oltre a quelle disponibili nell'interfaccia di base. Include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
