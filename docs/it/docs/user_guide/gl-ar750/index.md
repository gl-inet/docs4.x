# Guida utente di Creta (GL-AR750)

## Panoramica del prodotto

Creta (GL-AR750) e un router da viaggio AC dual-band. Il dual-band simultaneo supporta una velocita di trasmissione wireless fino a 733 Mbps (2,4 GHz: 300 Mbps + 5 GHz: 433 Mbps). Creta puo convertire una rete pubblica in una rete Wi-Fi privata per una navigazione sicura. L'archiviazione esterna supporta schede MicroSD fino a 128 GB. OpenWrt/LEDE e OpenVPN sono preinstallati. Per questo motivo, Creta offre agli utenti attenti alla privacy una VPN veloce e semplice che utilizza crittografia all'avanguardia.

![ar750 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/product_info/ar750_overview.png){class="glboxshadow"}

### Specifiche

[Specifiche GL-AR750](https://www.gl-inet.com/products/gl-ar750/#specs){target="_blank"}

## Come configurare Creta

Per configurare Creta, puoi usare uno dei quattro metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Guarda questo video di configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Questo video utilizza un router GL.iNet diverso per mostrare la configurazione, ma i passaggi sono gli stessi per Creta e per gli altri modelli di router.)</small>

### 1. Accendi Creta

Collega il cavo di alimentazione Micro USB alla porta di alimentazione del router. Assicurati di usare un alimentatore standard da 5V/2A.

!!! Note

    L'hot plugging della scheda TF non e supportato. Se desideri usare una scheda TF, inseriscila prima di accendere il router.

### 2. Collega il dispositivo a Creta

Collega il computer o il dispositivo mobile al router tramite Wi-Fi o Ethernet.

=== "Wi-Fi"

    Sul dispositivo, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password. Il nome della rete e la password predefiniti sono stampati sull'etichetta del router.

=== "Ethernet"

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

### 3. Collega Creta a Internet

**Note:** Le istruzioni seguenti sono state scritte per chi collega il router a Internet tramite il pannello di amministrazione web. Se desideri usare l'app GL.iNet invece del pannello di amministrazione web, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni mostrate sullo schermo.

#### 1. Accedi al pannello di amministrazione web del router

Nella barra degli indirizzi di un browser web, inserisci `192.168.8.1`. Scegli la lingua, quindi fai clic su **Next**. Imposta la password di amministrazione, quindi fai clic su **Apply**.

#### 2. Configura il metodo o i metodi di connessione Internet

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/ethernet.png){class="glboxshadow"}
    
    Collega un cavo Ethernet alla porta WAN del router e a un dispositivo upstream, ad esempio un modem. Se la connessione a Internet va a buon fine, accanto a "Ethernet" compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/repeater.png){class="glboxshadow"}

    1. Nella schermata principale del pannello di amministrazione web, individua la sezione "Repeater", quindi fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi.
    3. Inserisci la password della rete, quindi fai clic su **Apply**.
    
    Se la connessione a Internet va a buon fine, compare un punto verde accanto al nome della rete Wi-Fi.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/tethering.png){class="glboxshadow"}

    1. Collega lo smartphone al router tramite un cavo USB e abilita la condivisione della rete nelle impostazioni dell'hotspot personale.
    2. Nella schermata principale del pannello di amministrazione web, individua la sezione "Tethering", quindi fai clic su **Connect**.
    3. Se la connessione a Internet va a buon fine, compare un punto verde accanto a "Tethering".

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/usb_modem.png){class="glboxshadow"}

    1. Inserisci un modem USB con supporto cellulare nella porta USB del router.
    2. Nella schermata principale del pannello di amministrazione web, individua la sezione "Cellular", quindi fai clic su **Connect**.
    3. Se la connessione a Internet va a buon fine, compare un punto verde accanto a "Cellular".

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite un modem USB](../../interface_guide/internet_cellular.md).

**Note:** Se desideri usare la funzione Multi-WAN, devi configurare piu di un metodo di connessione Internet.

---

## Come configurare una VPN

Una VPN (rete privata virtuale) crea traffico sicuro e crittografato tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza come client VPN e consente di accedere a una rete remota come server VPN. Creta, come gli altri router GL.iNet, supporta OpenVPN e WireGuard.

=== "OpenVPN"

    Creta, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Creta, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocita e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

---

## Altre applicazioni

=== "Plug-ins"

    I plug-in sono funzionalita aggiuntive che ampliano le capacita del router. Per configurarli, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva automaticamente e aggiorna in tempo reale l'indirizzo IP associato a un dominio. E particolarmente utile per gli utenti che hanno bisogno di un indirizzo IP statico per accedere a una rete remota. Per configurarlo, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Il servizio di gestione cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet. Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

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

=== "IPv6"

    La pagina IPv6 consente di configurare le impostazioni IPv6 della rete, offrendo supporto per il piu recente protocollo Internet. In questa pagina puoi abilitare IPv6 e scegliere tra quattro modalita diverse in base alle esigenze della rete:

    * Native: ottiene un indirizzo IPv6 direttamente dal provider Internet, consentendo una connettivita IPv6 nativa semplice ed efficiente.
    * Passthrough: permette al traffico IPv6 di attraversare il router fino ai dispositivi della rete, facendo di fatto da ponte senza che il router gestisca direttamente l'instradamento IPv6.
    * NAT6: utilizza il Network Address Translation per IPv6 (NAT6) per tradurre tra indirizzi IPv6 interni ed esterni, in modo simile a quanto avviene con NAT per IPv4.
    * Static IPv6: consente di configurare manualmente un indirizzo IPv6 statico per il router, offrendo un indirizzo fisso per una connettivita costante e una gestione piu semplice dei servizi di rete.

    Queste impostazioni aiutano a sfruttare i vantaggi di IPv6, tra cui uno spazio di indirizzamento maggiore, funzionalita di sicurezza migliorate e prestazioni migliori.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [IPv6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    La pagina MAC Address consente di visualizzare e gestire gli indirizzi Media Access Control (MAC) associati al router. Le funzioni principali disponibili in questa pagina includono:

    * Factory Default: mostra gli indirizzi MAC predefiniti del router per le modalita Ethernet e Repeater, fornendo un riferimento per le impostazioni hardware originali.
    * Clone: clona l'indirizzo MAC di uno specifico dispositivo client. Questa funzione e particolarmente utile negli scenari in cui l'accesso alla rete e limitato a determinati dispositivi.
    * Manual: consente di specificare manualmente un indirizzo MAC personalizzato per il router. Inoltre, puoi usare il pulsante Random per generare un indirizzo MAC casuale, offrendo maggiore flessibilita e privacy.

    Queste funzioni consentono di gestire in modo efficace gli indirizzi MAC del router, garantendo compatibilita e flessibilita in diversi ambienti di rete.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalita del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN. Per configurarlo, fai riferimento a [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    La pagina IGMP Snooping consente di configurare impostazioni che ottimizzano la gestione del traffico multicast nella rete. IGMP Snooping ascolta ed estrae informazioni dai pacchetti del protocollo IGMP, creando e mantenendo tabelle di inoltro multicast di livello 2. In questo modo, i dati dei gruppi multicast vengono inoltrati solo agli host che hanno aderito al gruppo multicast, evitando che traffico multicast indesiderato raggiunga altri host.

    Queste impostazioni contribuiscono a ottimizzare prestazioni ed efficienza della rete, in particolare in ambienti con molto traffico multicast, ad esempio streaming video o giochi online.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Impostazioni di sistema

=== "Overview"

    La pagina Overview fornisce una panoramica completa dello stato attuale del router e delle relative metriche di prestazione. In questa pagina puoi visualizzare:

    * CPU Average Load: monitora il carico medio della CPU del router per valutare le prestazioni e individuare eventuali colli di bottiglia.
    * Memory Usage: controlla quanta memoria del router e in uso, facilitando la gestione delle risorse.
    * Flash Usage: visualizza l'utilizzo della memoria flash del router, assicurandoti che ci sia spazio sufficiente per firmware e dati di configurazione.
    * LED Control: attiva o disattiva i LED del router, personalizzando gli indicatori visivi del dispositivo.
    * System Info: accedi a informazioni dettagliate sul sistema del router, tra cui versione del firmware, uptime e stato della rete.
    
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

=== "Admin Password"

    La pagina Admin Password consente di impostare o modificare la password dell'interfaccia di amministrazione del router, assicurando che solo gli utenti autorizzati possano accedere e modificare le impostazioni del router. Questa password e fondamentale per mantenere la sicurezza e l'integrita della rete, proteggendola da accessi non autorizzati e modifiche di configurazione.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attivita pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La pagina Toggle Button Settings consente di configurare il pulsante fisico del router, permettendo di assegnargli funzioni specifiche per un accesso e un controllo rapidi. Questa funzione offre scorciatoie pratiche per attivita e impostazioni comuni, migliorando l'esperienza d'uso e semplificando la gestione del router.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    La pagina Log offre accesso a vari registri che memorizzano attivita ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati relativi a eventi e attivita a livello di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attivita legate ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se usato dal router, che riportano traffico web e operazioni del server.
    
    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione e molto utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporta il router alle impostazioni di default della versione firmware corrente. Puo essere utile per risolvere problemi persistenti o per ricominciare da zero con la configurazione predefinita del firmware attuale.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La pagina Advanced Settings offre accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in modo dettagliato impostazioni e funzioni del router oltre a quelle disponibili nell'interfaccia di base. Include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate e ulteriori informazioni, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
