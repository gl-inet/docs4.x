# Guida utente di Brume 2 (GL-MT2500/GL-MT2500A) {#brume-2-gl-mt2500gl-mt2500a-user-guide}

## Panoramica del prodotto {#product-overview}

Brume 2 (GL-MT2500/GL-MT2500A) e un gateway VPN leggero e potente basato su sistema operativo OpenWrt v21.02. Ha un design compatto ed e ideale per ospitare un server VPN a casa oppure per eseguire SD-WAN, Site-to-Site, in piccole e medie imprese. È disponibile in due varianti: GL-MT2500 con chassis in plastica e GL-MT2500A con chassis in alluminio.

![gl-mt2500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

## Contenuto della confezione {#package-contents}

- 1 x Brume 2 (GL-MT2500/GL-MT2500A)
- 1 x Manuale utente
- 1 x Cavo Ethernet
- 1 x Biglietto di ringraziamento
- 1 x Scheda di garanzia
- 1 x Alimentatore
- 1 x Convertitore (in base al Paese di spedizione)

La figura seguente mostra il modello GL-MT2500A come esempio.

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

## Come configurare Brume 2 {#how-to-set-up-brume-2}

Per configurare Brume 2, puoi usare uno dei metodi di connessione Internet supportati: Ethernet, Tethering e Cellular. Repeater non e supportato perché Brume 2 non dispone di un modulo Wi-Fi. Guarda questo video di configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rpi_loOwUQM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Accendi il router {#1-power-on}

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il router si avviera automaticamente.

### 2. Collega un dispositivo {#2-connect-device}

Collega il dispositivo, ad esempio un computer o un laptop, alla porta LAN del router tramite un cavo Ethernet.

### 3. Accedi al pannello di amministrazione web {#3-log-in-to-web-admin-panel}

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua e imposta la password di amministrazione, quindi fai clic su **Apply**.

### 4. Configurazione della connessione Internet {#4-internet-setup}

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}

    Collega un cavo Ethernet tra la porta WAN del router e un dispositivo upstream, ad esempio un modem.

    Quando la connessione a Internet va a buon fine, nella sezione Ethernet della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o un dongle USB, alla porta USB del router tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita USB Tethering.
    3. Nella pagina INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.

    Quando la connessione a Internet va a buon fine, nella sezione Tethering della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

    Inserisci un modem USB cellulare nella porta USB del router. Questo metodo e utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

    Quando la connessione a Internet va a buon fine, nella sezione Cellular della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

**Note:** se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di un metodo di connessione Internet.

---

## Client {#clients}

La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza il nome del dispositivo, indirizzi IP e MAC, velocità di download e upload, traffico totale e offre la possibilità di riservare un IP, bloccare il client o eseguire altre azioni.

Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud {#cloud-services}

=== "GoodCloud"

    Il servizio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.

    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp e una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata specificamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi sull'intera rete, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Con un focus sulla gestione dell'intera rete e sul futuro supporto al controllo a livello hardware, AstroWarp offre una soluzione più robusta e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.

    Per configurarla, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Una VPN crea traffico sicuro e crittografato tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza come client VPN e consente di accedere a una rete remota come server VPN. Brume 2, come gli altri router GL.iNet, supporta OpenVPN e WireGuard. Inoltre supporta anche Tor.

=== "OpenVPN"

    Brume 2, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 2, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocità e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abbreviazione di The Onion Router, e una rete orientata alla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server gestiti da volontari per nascondere posizione e utilizzo dell'utente, rendendo difficile tracciare le attività online.

    * [Come configurare Tor](../../interface_guide/tor.md).

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

=== "AdGuard Home"

    AdGuard Home e una soluzione di blocco di annunci e tracker a livello di rete che agisce come server DNS per filtrare contenuti indesiderati su tutti i dispositivi collegati alla rete domestica.

    Per configurarlo, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Parental Control"

    Parental control e un insieme di impostazioni progettate per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier e una soluzione di rete software-defined che consente agli utenti di creare reti virtuali sicure su Internet, collegando i dispositivi come se fossero sulla stessa rete locale.

    Per configurarlo, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale e un servizio VPN che consente di accedere ai dispositivi e alle applicazioni ovunque.

    Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

## Rete {#network}

=== "Port forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere a dispositivi all'interno di una rete privata. Per configurarlo, fai riferimento a [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con più connessioni Internet, ad esempio Ethernet, Tethering e Cellular, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, e una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimento dati ad alta velocità e condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.

    Per configurarla, fai riferimento a [LAN](../../interface_guide/lan.md).

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione dagli attacchi DNS rebinding e sovrascrivere le impostazioni DNS di tutti i client, consentire ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalità delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS dalla connessione Ethernet.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

---

=== "Port Management"

    La pagina Port Management consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare modalità MAC e indirizzo MAC per l'interfaccia WAN e visualizzare la velocità negoziata della porta di rete.

=== "Network Mode"

    Network mode indica le impostazioni di configurazione che determinano come un dispositivo si connette a una rete e comunica con altri dispositivi.

    Per configurarlo, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, e la versione più recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto più ampio, permettendo un numero virtualmente illimitato di indirizzi IP univoci, elemento essenziale per il crescente numero di dispositivi collegati a Internet.

    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN.

    Per configurarlo, fai riferimento a [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP snooping e una tecnica di ottimizzazione della rete usata negli switch Ethernet per gestire e controllare il traffico multicast.

    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Hardware acceleration indica l'uso di componenti hardware specializzati per eseguire compiti specifici in modo più efficiente rispetto alle CPU generiche.

    Per configurare l’accelerazione di rete, fai riferimento a questo tutorial [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La pagina NAT Settings consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG.

    Per configurarla, fai riferimento a [NAT Settings](../../interface_guide/nat_settings.md).

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

=== "Upgrade"

    La pagina Upgrade viene usata per aggiornare il firmware del router alla versione più recente, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Firmware Online Upgrade: verifica automaticamente sul server del produttore la disponibilità della versione firmware più recente. Se disponibile online, è possibile installarla.
    * Firmware Local Upgrade: consente di caricare manualmente un file firmware dal computer per aggiornare il router, offrendo controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni permettono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare le funzioni del router in base a una pianificazione predefinita, migliorando praticita ed efficienza. Le funzioni principali di questa pagina includono:

    * LED Display Schedule: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in determinati orari.
    * Schedule Reboot: configura il riavvio automatico del router a intervalli specifici per mantenere prestazioni e stabilità ottimali.

    Queste opzioni di pianificazione offrono maggiore controllo sul funzionamento del router, garantendo che soddisfi esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attività pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

---

=== "Log"

    La pagina Log offre accesso a vari registri che memorizzano attività ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati relativi a eventi e attività a livello di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attività legate ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se usato dal router, che riportano traffico web e operazioni del server.

    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione e molto utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md).

=== "Security"

    La pagina Security consente di configurare varie impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include opzioni per:

    * Admin Password: impostare o modificare la password dell'interfaccia amministrativa del router per garantire che solo gli utenti autorizzati possano modificare le impostazioni.
    * Local Access Control: gestire e limitare l'accesso all'interfaccia del router dai dispositivi collegati alla rete locale.
    * Remote Access Control: configurare e limitare l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la protezione dalle minacce esterne.
    * Open Ports on Router: controllare quali porte sono aperte sul router, limitando potenziali vulnerabilita e accessi non autorizzati.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate, fai riferimento a [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporta il router alle impostazioni di default della versione firmware corrente. Può essere utile per risolvere problemi persistenti o per ricominciare da zero con la configurazione predefinita del firmware attuale.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La pagina Advanced Settings offre accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in modo dettagliato impostazioni e funzioni del router oltre a quelle disponibili nell'interfaccia di base. Include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
