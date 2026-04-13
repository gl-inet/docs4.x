# Guida utente di Marble (GL-B3000)

## Panoramica del prodotto

Il router Marble (GL-B3000) e un vero oggetto di design, concepito come una cornice fotografica per ospitare la tua opera preferita e valorizzare l'ambiente domestico. Oltre al suo aspetto elegante, Marble (GL-B3000) offre prestazioni di alto livello grazie al supporto Wi-Fi 6 e alle funzionalita VPN.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Contenuto della confezione

- 1 x Marble (GL-B3000)
- 1 x Manuale utente
- 1 x Biglietto di ringraziamento
- 1 x Cavo Ethernet
- 1 x Kit di montaggio a parete
- 1 x Pad adesivo
- 1 x Supporto per router
- 1 x Cornice fotografica (opzionale)
- 1 x Alimentatore
- 1 x Convertitore (in base al Paese di spedizione)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Come configurare Marble

Guarda questi video di installazione e configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Accendi il router

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il router si avviera automaticamente.

### 2. Collega un dispositivo

Collega un dispositivo, ad esempio un computer, un laptop o uno smartphone, al router tramite Wi-Fi o cavo Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, vai in Settings -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password. Il nome di rete e la password predefiniti sono stampati sull'etichetta del router.

### 3. Accedi al pannello di amministrazione web

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua e imposta la password di amministrazione, quindi fai clic su **Apply**.

### 4. Configurazione della connessione Internet

**Note:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci usare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni mostrate sullo schermo.

Configura Marble usando uno dei metodi di connessione Internet supportati: Ethernet e Repeater. Se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura due connessioni Internet.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}
    
    Collega un cavo Ethernet tra la porta WAN del router e un dispositivo upstream, ad esempio un modem.
    
    Quando la connessione a Internet va a buon fine, nella sezione Ethernet della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. Nella pagina INTERNET del pannello di amministrazione web, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password della rete, quindi fai clic su **Apply**.
    
    Quando la connessione a Internet va a buon fine, nella sezione Repeater della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

---

## Come configurare una VPN

Una VPN (rete privata virtuale) crea traffico sicuro e crittografato tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza come client VPN e consente di accedere a una rete remota come server VPN. Marble, come gli altri router GL.iNet, supporta OpenVPN e WireGuard. Inoltre supporta anche Tor.

=== "OpenVPN"

    Marble, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocita e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor e un servizio orientato alla privacy che consente di accedere a Internet in modo anonimo. Per configurare Tor, segui questo tutorial:

    * [Come configurare Tor](../../interface_guide/tor.md)

---

## Wireless e client

=== "Wireless"

    La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi a 5 GHz e 2,4 GHz, tra cui attivazione/disattivazione del Wi-Fi, potenza TX, nome della rete Wi-Fi (SSID), BSSID casuale, modalita di sicurezza Wi-Fi, password Wi-Fi, visibilita dell'SSID, modalita Wi-Fi, larghezza di banda e canale.

    Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza nome del dispositivo, tipo di connessione (cioe via Ethernet o Wi-Fi), indirizzi IP e MAC, velocita di download e upload, traffico totale e offre la possibilita di bloccare il client o eseguire altre azioni.

    Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    Il servizio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.
    
    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    Questa funzione e disponibile a partire dal firmware v4.7.

    AstroWarp e una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata specificamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi sull'intera rete, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Con un focus sulla gestione dell'intera rete e sul futuro supporto al controllo a livello hardware, AstroWarp offre una soluzione piu robusta e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.

## Applicazioni

=== "Plug-ins"

    I plug-in sono funzionalita aggiuntive che ampliano le capacita del router. Per configurarli, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva automaticamente e aggiorna in tempo reale l'indirizzo IP associato a un dominio. E particolarmente utile per gli utenti che hanno bisogno di un indirizzo IP statico per accedere a una rete remota. Per configurarlo, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

---

=== "AdGuard Home"

    AdGuard Home e uno strumento di terze parti che blocca annunci e tracciamento per migliorare la sicurezza della navigazione.
    
    Per imparare ad abilitarlo, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Il parental control e un insieme di impostazioni progettate per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti. Marble offre due opzioni di parental control: la versione locale sviluppata da GL.iNet e la versione integrata di Bark, un'app dedicata al controllo parentale.

    Per configurarlo, fai riferimento a [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Tailscale e un servizio VPN che consente di accedere ai dispositivi e alle applicazioni ovunque. Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier e un servizio VPN che consente di collegare i dispositivi a una rete virtuale. Per configurarlo, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

---

## Impostazioni di rete

=== "Firewall"

    La pagina Firewall offre miglioramenti essenziali alla sicurezza della rete. Include funzioni come Port Forwarding, Open Ports e DMZ. Questi strumenti consentono di gestire e personalizzare il flusso del traffico di rete e di aumentarne la sicurezza.

    * Port Forwarding: reindirizza traffico specifico da Internet verso dispositivi designati all'interno della rete, consentendo l'accesso a servizi come server di gioco o server web.
    * Open Ports: consente di monitorare e controllare quali porte del router sono aperte, aiutando a prevenire accessi non autorizzati e potenziali minacce alla sicurezza.
    * DMZ (Demilitarized Zone): colloca un dispositivo all'esterno del firewall principale, permettendogli di avere accesso illimitato a Internet mentre il resto della rete resta protetto da potenziali minacce.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet, ad esempio cellular, repeater ed ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La pagina LAN consente di gestire e configurare le impostazioni della rete locale del router. Le funzioni principali disponibili in questa pagina includono:

    * Indirizzo IP del router: modifica l'indirizzo IP del router per adattarlo meglio alla configurazione della rete.
    * Netmask: imposta la subnet mask della rete, che determina dimensioni e intervallo degli indirizzi IP.
    * DHCP: abilita o configura il protocollo Dynamic Host Configuration Protocol, che assegna automaticamente gli indirizzi IP ai dispositivi della rete.
    * Address Reservation: riserva indirizzi IP specifici per determinati dispositivi, garantendo che ricevano sempre lo stesso indirizzo IP dal server DHCP.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [LAN](../../interface_guide/lan.md).

---

=== "Guest Network"

    La pagina Guest Network consente di creare e gestire una rete separata per gli ospiti, fornendo accesso a Internet senza compromettere la sicurezza della rete principale. Le principali funzioni di questa pagina includono:

    * Gateway: imposta un intervallo di indirizzi IP specifico per la rete ospite, distinguendolo dalla rete principale.
    * DHCP: configura il Dynamic Host Configuration Protocol per la rete ospite, assegnando automaticamente indirizzi IP ai dispositivi che vi si collegano.

    Queste funzioni consentono agli ospiti di accedere a Internet mantenendo sicure prestazioni e protezione della rete principale.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La pagina DNS offre opzioni per personalizzare le impostazioni del Domain Name System del router, migliorando sia la sicurezza sia le prestazioni. Le funzioni principali disponibili in questa pagina includono:

    * Encrypted DNS: configura DNS crittografato per proteggere i dati di navigazione da monitoraggio o manomissioni, garantendo privacy e sicurezza.
    * Manual DNS: imposta manualmente i server DNS desiderati, ottenendo un controllo personalizzato sulle query DNS e, potenzialmente, tempi di risoluzione piu rapidi.
    * DNS Proxy: abilita il proxy DNS per instradare le richieste DNS dei dispositivi tramite un server DNS specificato, fornendo un ulteriore livello di controllo sul traffico DNS.

    Queste impostazioni consentono di ottimizzare le prestazioni e la sicurezza DNS della rete in base alle proprie esigenze.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    La pagina Network Mode consente di configurare il router per operare in diverse modalita, offrendo flessibilita per soddisfare varie esigenze di rete. Le modalita disponibili includono:

    * Router: funziona come router standard, gestendo il traffico tra la rete locale e Internet e fornendo funzionalita come NAT, firewall e DHCP.
    * Access Point: funziona come punto di accesso, estendendo la rete cablata esistente tramite connettivita wireless senza instradare il traffico.
    * Extender: funziona come range extender, ampliando il segnale della rete wireless esistente per coprire un'area piu ampia ed eliminare le zone d'ombra.
    * WDS (Wireless Distribution System): simile alla modalita Extender; scegli WDS se il router principale supporta la modalita WDS.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

---

=== "IPv6"

    La pagina IPv6 consente di configurare le impostazioni IPv6 della rete, offrendo supporto per il piu recente protocollo Internet. In questa pagina puoi abilitare IPv6 e scegliere tra quattro modalita diverse in base alle esigenze della rete:

    * Native: ottiene un indirizzo IPv6 direttamente dal provider Internet, consentendo una connettivita IPv6 nativa semplice ed efficiente.
    * Passthrough: permette al traffico IPv6 di attraversare il router fino ai dispositivi della rete, facendo di fatto da ponte senza che il router gestisca direttamente l'instradamento IPv6.
    * NAT6: utilizza il Network Address Translation per IPv6 (NAT6) per tradurre tra indirizzi IPv6 interni ed esterni, in modo simile a quanto avviene con NAT per IPv4.
    * Static IPv6: consente di configurare manualmente un indirizzo IPv6 statico per il router, offrendo un indirizzo fisso per una connettivita costante e una gestione piu semplice dei servizi di rete.

    Queste impostazioni aiutano a sfruttare i vantaggi di IPv6, tra cui uno spazio di indirizzamento maggiore, funzionalita di sicurezza migliorate e prestazioni migliori.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    La pagina MAC Address consente di visualizzare e gestire gli indirizzi Media Access Control (MAC) associati al router. Le funzioni principali disponibili in questa pagina includono:

    * Factory Default: mostra gli indirizzi MAC predefiniti del router per le modalita Ethernet e Repeater, fornendo un riferimento per le impostazioni hardware originali.
    * Clone: clona l'indirizzo MAC di uno specifico dispositivo client. Questa funzione e particolarmente utile negli scenari in cui l'accesso alla rete e limitato a determinati dispositivi.
    * Manual: consente di specificare manualmente un indirizzo MAC personalizzato per il router. Inoltre, puoi usare il pulsante Random per generare un indirizzo MAC casuale, offrendo maggiore flessibilita e privacy.

    Queste funzioni consentono di gestire in modo efficace gli indirizzi MAC del router, garantendo compatibilita e flessibilita in diversi ambienti di rete.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalita del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN. Per configurarlo, fai riferimento a [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    La pagina IGMP Snooping consente di configurare impostazioni che ottimizzano la gestione del traffico multicast nella rete. IGMP Snooping ascolta ed estrae informazioni dai pacchetti del protocollo IGMP, creando e mantenendo tabelle di inoltro multicast di livello 2. In questo modo, i dati dei gruppi multicast vengono inoltrati solo agli host che hanno aderito al gruppo multicast, evitando che traffico multicast indesiderato raggiunga altri host.

    Queste impostazioni contribuiscono a ottimizzare prestazioni ed efficienza della rete, in particolare in ambienti con molto traffico multicast, ad esempio streaming video o giochi online.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    La pagina Network Acceleration consente di abilitare funzioni che riducono il carico della CPU e accelerano l'inoltro dei pacchetti di traffico, migliorando le prestazioni complessive della rete. Tuttavia, l'abilitazione della network acceleration puo entrare in conflitto con alcune funzionalita.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La pagina NAT Settings consente di configurare opzioni di Network Address Translation (NAT) per ottimizzare applicazioni specifiche e migliorare le prestazioni di rete. Le principali impostazioni disponibili includono:

    * Enable Full Cone NAT: Full Cone NAT puo essere usato per ridurre la latenza nei giochi, offrendo un percorso piu diretto e meno restrittivo per il traffico di rete. Tuttavia, puo essere meno sicuro, poiche consente agli host esterni di avviare piu facilmente connessioni verso i dispositivi interni.
    * Enable SIP ALG: il Session Initiation Protocol Application Layer Gateway (SIP ALG) puo aiutare a mitigare i problemi causati da NAT multipli, che possono influire sui servizi VoIP. Tuttavia, nella maggior parte dei casi SIP ALG potrebbe non essere utile e puo causare problemi come audio unidirezionale, telefoni che non squillano, chiamate che cadono o che finiscono direttamente in segreteria.

    Queste impostazioni consentono di adattare il comportamento NAT del router alle esigenze della rete, bilanciando miglioramenti di prestazione con considerazioni su sicurezza e funzionalita.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [NAT Settins](../../interface_guide/nat_settings.md).

---

## Impostazioni di sistema

=== "Overview"

    La pagina Overview fornisce una panoramica completa dello stato attuale del router e delle relative metriche di prestazione. In questa pagina puoi visualizzare:

    * CPU Average Load: monitora il carico medio della CPU del router per valutare le prestazioni e individuare eventuali colli di bottiglia.
    * Memory Usage: controlla quanta memoria del router e in uso, facilitando la gestione delle risorse.
    * Flash Usage: visualizza l'utilizzo della memoria flash del router, assicurandoti che ci sia spazio sufficiente per firmware e dati di configurazione.
    * System Info: accedi a informazioni dettagliate sul sistema del router, tra cui versione del firmware, uptime e stato della rete.
    * LED Control: attiva o disattiva i LED del router, personalizzando gli indicatori visivi del dispositivo.

    Queste funzioni offrono informazioni e controlli essenziali per gestire e monitorare in modo efficace il funzionamento del router.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La pagina Upgrade viene usata per aggiornare il firmware del router alla versione piu recente, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Online Upgrade: controlla e installa automaticamente la versione firmware piu recente direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Local Upgrade: consente di caricare manualmente un file firmware dal computer per aggiornare il router, offrendo controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni permettono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando praticita ed efficienza. Le funzioni principali di questa pagina includono:

    * LED Display Schedule: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in determinati orari.
    * Schedule Reboot: configura il riavvio automatico del router a intervalli specifici per mantenere prestazioni e stabilita ottimali.
    * 5GHz Wi-Fi Status Schedule: crea una pianificazione per abilitare o disabilitare la banda Wi-Fi a 5 GHz in orari specifici, ottimizzando l'uso della rete e l'efficienza energetica.
    * 2.4GHz Wi-Fi Status Schedule: imposta una pianificazione per controllare la banda Wi-Fi a 2,4 GHz, gestendo meglio disponibilita della rete e consumo energetico.

    Queste opzioni di pianificazione offrono maggiore controllo sul funzionamento del router, garantendo che soddisfi esigenze e preferenze specifiche.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attivita pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    La pagina Log offre accesso a vari registri che memorizzano attivita ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati relativi a eventi e attivita a livello di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attivita legate ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se usato dal router, che riportano traffico web e operazioni del server.

    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione e molto utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Log](../../interface_guide/log.md).

=== "Security"

    La pagina Security consente di configurare varie impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include opzioni per:

    * Admin Password: impostare o modificare la password dell'interfaccia amministrativa del router per garantire che solo gli utenti autorizzati possano modificare le impostazioni.
    * Local Access Control: gestire e limitare l'accesso all'interfaccia del router dai dispositivi collegati alla rete locale.
    * Remote Access Control: configurare e limitare l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la protezione dalle minacce esterne.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporta il router alle impostazioni di default della versione firmware corrente. Puo essere utile per risolvere problemi persistenti o per ricominciare da zero con la configurazione predefinita del firmware attuale.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La pagina Advanced Settings offre accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in modo dettagliato impostazioni e funzioni del router oltre a quelle disponibili nell'interfaccia di base. Include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
