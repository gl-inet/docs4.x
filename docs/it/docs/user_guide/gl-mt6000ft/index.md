# Guida per l'utente Fortify (GL-MT6000)

## Panoramica del prodotto

Fortify (GL-MT6000) è un router Wi-Fi 6 in co-branding rilasciato congiuntamente da GL.iNet ed ExpressVPN. Ogni unità viene fornita con un abbonamento ExpressVPN gratuito di un anno. Gli utenti possono riscattare l'abbonamento e connettere i propri account direttamente sul pannello di amministrazione web del router. Una volta attivato, tutto il traffico che passa attraverso il router sfrutterà la rete ad alta velocità di ExpressVPN e la solida crittografia per proteggere l'intera connessione di rete e la privacy online.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Come impostare Fortify

### 1. Accendere

Metti insieme l'alimentatore in due pezzi. Collegalo al router Fortify e collegalo a una presa. Si avvierà automaticamente.

### 2. Connetti il dispositivo

Collega un dispositivo (ad esempio un computer, un portatile o uno smartphone) al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il tuo dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul tuo dispositivo, vai su Impostazioni -> WLAN, individua il nome della rete Wi-Fi del tuo router nell'elenco delle reti disponibili e inserisci la password per accedere alla rete. È possibile trovare il nome di rete e la password predefiniti stampati sull'etichetta del router.

### 3. Accedi al pannello di amministrazione web

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua nell'angolo in alto a destra, imposta la password dell'amministratore, quindi fai clic su **Next**. La password deve contenere da 10 a 63 caratteri e contenere almeno due dei seguenti elementi: lettere maiuscole, lettere minuscole, numeri e simboli speciali.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Configura la tua connessione Wi-Fi. Tieni presente che se modifichi le informazioni Wi‑Fi, dovrai riconnettere il tuo dispositivo al Wi‑Fi del router utilizzando le credenziali aggiornate.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Configurazione di Internet

**Nota:** Le seguenti istruzioni si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci l'[app GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, scaricala e segui le istruzioni visualizzate sullo schermo.

Configura il tuo Fortify utilizzando uno dei metodi di connessione Internet supportati: Ethernet, Ripetitore, Tethering e Cellulare. Se desideri utilizzare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura più di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Collega un cavo Ethernet tra la porta WAN del router Fortify e un dispositivo upstream come un modem.

    Una volta connesso correttamente a Internet, il LED del router diventa bianco fisso.

    Fare riferimento a [Connessione a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md) per istruzioni dettagliate.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Nel pannello di amministrazione web, vai su INTERNET -> sezione Ripetitore e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra le reti disponibili.
    3. Immettere la password, quindi fare clic su **Apply**.

    Una volta connesso correttamente a Internet, il LED del router diventa bianco fisso.

    Fare riferimento a [Connessione a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md) per istruzioni dettagliate.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Collega il tuo smartphone alla porta USB del router utilizzando un cavo USB.
    2. Sul tuo smartphone, vai su Impostazioni e attiva Tethering USB. Per iPhone, fidati di questo dispositivo e abilita l'Hotspot personale.
    3. Nel pannello di amministrazione web, vai su INTERNET -> sezione Tethering e fai clic su **Connect**.

    Una volta connesso correttamente a Internet, il LED del router diventa bianco fisso.

    Fare riferimento a [Connessione a Internet tramite tethering USB](../../interface_guide/internet_tethering.md) per istruzioni dettagliate.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Collega un modem USB cellulare alla porta USB del router. Ciò è utile per condividere Internet da un modem USB a tutti i dispositivi collegati.

    Una volta connesso correttamente a Internet, il LED del router diventa bianco fisso.

    Fare riferimento a [Connessione a Internet tramite cellulare](../../interface_guide/internet_cellular.md) per istruzioni dettagliate.

---

Di seguito è riportata una panoramica delle funzionalità del pannello di amministrazione web di Fortify.

## Senza fili

La pagina Wireless ti consente di configurare le reti Wi-Fi di Fortify, tra cui Rete principale, Rete ospite e Rete IoT. Ciascuna rete supporta entrambe le bande da 2,4 GHz e 5 GHz.

Per impostare la modalità wireless, fare riferimento a [Wireless](../../interface_guide/wireless.md).

## Clienti

La pagina Client visualizza informazioni sui dispositivi connessi, inclusi nome del dispositivo, tipo di connessione, indirizzi IP e MAC, velocità di download e upload, traffico e offre la possibilità di bloccare client specifici con un clic o eseguire altre azioni.

Per i dettagli fare riferimento a [Clienti](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} fornisce un modo facile e semplice per accedere e gestire in remoto i router GL.iNet.

    Per i dettagli fare riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp è una funzionalità creata per la rete remota senza interruzioni sui router GL.iNet. Adotta il protocollo AmneziaWG con offuscamento del traffico integrato, offrendo un accesso remoto stabile e sicuro sempre e ovunque.

    Fare riferimento a [AstroWarp](../../interface_guide/astrowarp.md) per i dettagli.

## VPN

Una VPN (virtual private network) stabilisce tunnel di traffico sicuri e crittografati tra il tuo dispositivo locale e il server VPN. Aggiunge un ulteriore livello di privacy e sicurezza al client VPN e consente l'accesso alla rete di server VPN remota.

Fortify si integra con [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, consentendoti di attivare una connessione ExpressVPN in pochi minuti. Ogni dispositivo Fortify viene fornito con un abbonamento ExpressVPN gratuito di un anno. Puoi riscattare l'abbonamento e connettere il tuo account ExpressVPN direttamente sul pannello di amministrazione web del router. Una volta abilitata la connessione VPN, tutto il traffico instradato attraverso il router utilizzerà i server ad alta velocità di ExpressVPN e la solida crittografia per proteggere l'intera rete e la privacy online.

Per riscattare l'abbonamento gratuito e configurare il tunnel VPN, fare riferimento alla [Guida all'attivazione di ExpressVPN](../../interface_guide/expressvpn_activation_guide.md).

Per configurare un server OpenVPN, fare riferimento a [Server OpenVPN](../../interface_guide/openvpn_server.md).

Per configurare un server WireGuard, fare riferimento a [WireGuard Server](../../interface_guide/wireguard_server.md).

## Rete

=== "Multi-WAN"

    Multi-WAN è una funzionalità di rete che consente di configurare il router con più connessioni Internet (ad esempio cellulare, ripetitore ed Ethernet) contemporaneamente. Se la tua attuale connessione Internet non funziona, il router passerà automaticamente a un'altra connessione Internet. Ciò garantisce un accesso a Internet fluido e ininterrotto.

    Per i dettagli fare riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Una LAN, o Local Area Network, è una rete che collega computer e dispositivi all'interno di un'area geografica limitata, come una casa o un ufficio. Questa è la rete locale a cui si collega il dispositivo quando è connesso alla rete Wi-Fi principale o tramite un cavo Ethernet. La pagina LAN copre le Impostazioni di base, le Impostazioni del server DHCP e la Prenotazione degli indirizzi.

    Fare riferimento a [LAN](../../interface_guide/lan.md) per i dettagli.

=== "Guest Network"

    La pagina Rete ospite ti consente di creare una rete Wi-Fi dedicata per i visitatori. Isolato dalla rete primaria, migliora la sicurezza fornendo al contempo un comodo accesso a Internet. È possibile impostare una sottorete ospite all'interno degli intervalli di indirizzi privati ​​IPv4 `192.168.0.0/16`, `172.16.0.0/12` o `10.0.0.0/8`, specificare il gateway e gli indirizzi IP della maschera di rete.

    Per i dettagli fare riferimento a [Rete ospite](../../interface_guide/guest_network.md).

=== "IoT Network"

    La pagina Rete IoT consente di creare una rete Wi-Fi dedicata per i dispositivi IoT. Isolato dalla rete primaria, offre migliore compatibilità e maggiore sicurezza.

    Per i dettagli fare riferimento a [Rete IoT](../../interface_guide/iot_network.md).

<br>

=== "DNS"

    Le impostazioni DNS sul router controllano il modo in cui i nomi di dominio vengono tradotti in indirizzi IP. Questa pagina consente di utilizzare il server DNS(s) ottenuto automaticamente dai dispositivi upstream o di impostarne di personalizzati e di configurare le priorità DNS.

    Per i dettagli fare riferimento a [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La pagina Porta Ethernet consente di gestire i ruoli della porta Ethernet (WAN/LAN) e visualizzare i dettagli della porta come l'indirizzo MAC e la velocità negoziata.

    Fare riferimento a [Porta Ethernet](../../interface_guide/ethernet_port.md) per i dettagli.

=== "IPv6"

    IPv6, o Protocollo Internet versione 6, è la versione più recente del Protocollo Internet progettata per sostituire IPv4. Fornisce uno spazio di indirizzi molto più ampio, consentendo un numero virtualmente illimitato di indirizzi IP univoci, essenziale per accogliere il numero crescente di dispositivi connessi a Internet.

    Per i dettagli fare riferimento a [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    Lo snooping IGMP è una tecnica di ottimizzazione della rete utilizzata negli switch Ethernet per gestire e controllare il traffico multicast.

    Fare riferimento a [Snooping IGMP](../../interface_guide/igmp_snooping.md) per i dettagli.

<br>

=== "Network Mode"

    La modalità di rete si riferisce alle impostazioni di configurazione che determinano il modo in cui un dispositivo si connette a una rete e comunica con altri dispositivi.

    Per impostare la modalità di rete, fare riferimento a [Modalità di rete](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzionalità del tuo router principale con funzionalità che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN.

    Per impostare il gateway drop-in, fare riferimento a [Come impostare il gateway drop-in](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    L'accelerazione della rete può ridurre il carico della CPU e accelerare l'inoltro dei pacchetti di traffico.

    Per impostare l'accelerazione di rete, fare riferimento a [Accelerazione di rete](../../interface_guide/network_acceleration.md).

## Controllo del flusso

=== "DPI Engine"

    DPI (Deep Packet Inspection) è una funzionalità fondamentale della gestione della rete intelligente. Può superare le limitazioni dei router tradizionali (che identificano solo gli indirizzi di origine o destinazione), analizzare in profondità i carichi utili dei pacchetti di dati e identificare con precisione le applicazioni e i siti Web a cui hanno avuto accesso gli utenti attraverso il confronto delle librerie di funzionalità, consentendo una classificazione e un controllo raffinati del traffico.

    Integrata con [Netify](https://www.netify.ai/){target="_blank"}, la funzionalità GL.iNet DPI adotta un plug-in incorporato leggero per un'implementazione efficiente. Con il database delle firme aggiornato online Netify, consente una gestione affidabile, rendendo il controllo della rete più accurato ed efficiente.

    Fare riferimento a [Motore DPI](../../interface_guide/dpi_engine.md) per i dettagli.

=== "Data Statistics"

    Data Statistics offre un dashboard intelligente per le informazioni sul traffico che classifica e visualizza l'utilizzo della rete da parte delle applicazioni, aiutandoti a monitorare il traffico storico e in tempo reale per una migliore consapevolezza e controllo della rete.

    Per i dettagli fare riferimento a [Statistiche dei dati](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Il filtro contenuti fornisce una sicurezza online intelligente basata sulla classificazione basata su DPI, bloccando automaticamente i siti Web dannosi per mantenere la rete pulita e sicura.

    Per i dettagli fare riferimento a [Filtro contenuti](../../interface_guide/content_filter.md).

<br>

=== "QoS"

    QoS (Quality of Service) ottimizza l'allocazione della larghezza di banda dando priorità alle attività critiche (ad esempio videochiamate e giochi) durante la congestione della rete, riducendo la latenza e migliorando le prestazioni complessive della rete. Tieni presente che ciò si applica al traffico del client locale e al traffico del tunnel del client VPN, ma non al traffico ricevuto quando il router funziona come server VPN.

    Per i dettagli fare riferimento a [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", garantendo giochi e chiamate vocali più fluidi.

    Per i dettagli fare riferimento a [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control è progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di visualizzazione e la restrizione dell'accesso a determinati contenuti.

    Per i dettagli fare riferimento a [Controllo genitoriale](../../interface_guide/parental_control_v4.9.md).

## Sicurezza

=== "Port forwarding"

    Il port forwarding consente ai server e ai dispositivi remoti su Internet di accedere ai dispositivi su una rete privata.

    Fare riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md) per i dettagli.

=== "ACL"

    ACL, abbreviazione di Access Control List, consente di creare regole per gestire il traffico di rete in base a protocolli di connessione, indirizzi di dispositivi e porte. Controlla se consentire o bloccare l'accesso alla rete. Se più regole ACL sono in conflitto, il sistema applica quella con priorità più alta.

    Per i dettagli fare riferimento a [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    L'accesso amministratore consente di configurare varie impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include le seguenti opzioni:

    * Controllo dell'accesso: gestisci e limita l'accesso all'interfaccia del router dai dispositivi collegati alla rete locale.
    * Controllo dell'accesso remoto: configura e limita l'accesso all'interfaccia del router da postazioni remote su Internet, migliorando la sicurezza contro le minacce esterne.
    * Porte aperte sul router: controlla quali porte sono aperte sul router, limitando potenziali vulnerabilità e accessi non autorizzati.

    Fare riferimento a [Accesso amministratore](../../interface_guide/admin_access.md) per i dettagli.

=== "NAT Mode"

    La pagina Modalità NAT consente di abilitare o disabilitare la funzionalità Full Cone NAT e SIP ALG (Application Layer Gateway).

    Fare riferimento a [Modalità NAT](../../interface_guide/nat_settings.md) per i dettagli.

## Applicazioni

=== "Plug-ins"

    Un plug-in è un componente software che aggiunge caratteristiche o funzionalità specifiche a un programma per computer esistente, consentendo la personalizzazione e il miglioramento delle sue capacità.

    Fare riferimento a [Plug-in](../../interface_guide/plugins.md) per i dettagli.

=== "Dynamic DNS"

    Il DNS dinamico (DDNS) rileva e aggiorna automaticamente l'indirizzo IP associato a un dominio in tempo reale. È utile per gli utenti che necessitano di un indirizzo IP statico per accedere a una rete remota.

    Per i dettagli fare riferimento a [DNS dinamico](../../interface_guide/ddns.md).

=== "Network Storage"

    L'archiviazione di rete si riferisce a una soluzione di archiviazione dati centralizzata che consente a più utenti e dispositivi di accedere e condividere file su una rete.

    Fare riferimento a [Archiviazione di rete](../../interface_guide/network_storage.md) per i dettagli.

=== "AdGuard Home"

    AdGuard Home è una soluzione di blocco di annunci e tracker su tutta la rete che funge da server DNS per filtrare i contenuti indesiderati su tutti i dispositivi collegati a una rete domestica.

    Per i dettagli fare riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

<br>

=== "Bark"

    Il servizio [Bark](https://www.bark.us/){target="_blank"} può aiutare a proteggere il mondo digitale di tuo figlio e fornire una protezione online completa. In genere richiede un abbonamento a pagamento. Tuttavia, come parte della partnership GL.iNet con Bark, offriamo gratuitamente il piano Bark Home su Fortify (GL-MT6000), fornendo monitoraggio avanzato e avvisi senza costi aggiuntivi.

    Fare riferimento a [Bark](../../interface_guide/bark.md) per i dettagli.

=== "Tailscale"

    Tailscale è un servizio VPN che rende i dispositivi e le applicazioni che possiedi accessibili ovunque nel mondo, in modo sicuro e semplice.

    Fortify (GL-MT6000) si integra con Tailscale, consentendoti di unire il router a una rete virtuale Tailscale. Una volta connesso, puoi accedervi da remoto, comprese le sue risorse WAN e LAN.

    Fare riferimento a [Tailscale](../../interface_guide/tailscale.md) per i dettagli.

=== "ZeroTier"

    ZeroTier è una soluzione di rete definita dal software che consente agli utenti di creare reti virtuali sicure su Internet, connettendo i dispositivi come se fossero sulla stessa rete locale.

    Per i dettagli fare riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor (derivato da The Onion Router) è un software gratuito e open source per consentire la comunicazione anonima. Aiuta gli utenti a esplorare Internet con privacy.

    Fare riferimento a [Tor](../../interface_guide/tor.md) per i dettagli.

## Sistema

=== "Overview"

    La pagina Panoramica fornisce un'istantanea completa dello stato attuale del router e dei parametri delle prestazioni. In questa pagina è possibile visualizzare:

    * Carico medio della CPU: monitora il carico medio sulla CPU del router, aiutandoti a valutare le prestazioni e identificare potenziali colli di bottiglia.
    * Utilizzo della memoria: controlla quanta memoria del router è in uso, aiutando nella gestione delle risorse.
    * Controllo LED: attiva o disattiva le luci LED del router, consentendo la personalizzazione degli indicatori visivi del dispositivo.
    * Utilizzo flash: visualizza l'utilizzo della memoria flash del router, assicurando che ci sia spazio sufficiente per firmware e dati di configurazione.
    * Informazioni sul dispositivo: accedi a informazioni dettagliate sul sistema del tuo router, inclusi tempo di attività, nome host, modello, architettura, versione OpenWrt, versione del kernel, ID dispositivo, MAC dispositivo e S/N dispositivo.
    * Archiviazione esterna: controlla lo stato di eventuali dispositivi di archiviazione esterni collegati al router, come unità USB o schede TF.

    Queste funzionalità forniscono informazioni e controlli essenziali, aiutandoti a gestire e monitorare in modo efficace il funzionamento del router.

    Per i dettagli fare riferimento a [Panoramica](../../interface_guide/system_overview.md).

=== "Admin Password"

    La pagina Password amministratore consente di impostare o modificare la password per l'interfaccia amministrativa del router.

    Fare riferimento a [Password amministratore](../../interface_guide/admin_password.md) per i dettagli.

=== "Upgrade"

    La pagina Aggiornamento viene utilizzata per aggiornare il firmware del router alla versione più recente, garantendo prestazioni migliorate, sicurezza e nuove funzionalità. Questa pagina offre due opzioni:

    * Aggiornamento online del firmware: controlla e installa automaticamente la versione più recente del firmware direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Aggiornamento locale del firmware: carica manualmente un file firmware dal tuo computer per aggiornare il router, fornendo il controllo sulla versione e sui tempi di aggiornamento.

    Fare riferimento a [Aggiornamento](../../interface_guide/upgrade.md) per i dettagli.

=== "Scheduled Tasks"

    La pagina Attività pianificate consente di automatizzare varie funzioni del router in base a una pianificazione predefinita, migliorando praticità ed efficienza. Le funzionalità principali di questa pagina includono:

    * Programmazione display LED: imposta una programmazione per accendere o spegnere automaticamente le luci LED del router, riducendo l'inquinamento luminoso in orari specifici.
    * Pianifica riavvio: configura il router in modo che si riavvii automaticamente a intervalli specificati, contribuendo a mantenere prestazioni e stabilità ottimali.
    * Pianificazione stato Wi-Fi 5GHz/2,4GHz: imposta una pianificazione per controllare la banda Wi-Fi 5GHz/2,4GHz, consentendo una migliore gestione della disponibilità della rete e del consumo energetico.

    Queste opzioni di pianificazione ti offrono un maggiore controllo sulle operazioni del router, garantendo che soddisfi le tue esigenze e preferenze specifiche.

    Per i dettagli fare riferimento a [Attività pianificate](../../interface_guide/scheduled_tasks.md).

<br>

=== "Time Zone"

    La pagina Fuso orario ti consente di impostare il fuso orario corretto per il tuo router, assicurando che tutte le attività pianificate, i registri e gli eventi di sistema abbiano un timestamp accurato in base all'ora locale. Questa impostazione è fondamentale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sul tempo.

    Per i dettagli fare riferimento a [Fuso orario](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    La pagina Ripristina firmware consente di ripristinare la versione corrente del firmware del router alle impostazioni predefinite, cancellando tutte le configurazioni personalizzate. Questo processo ripristinerà il router alle impostazioni predefinite della versione del firmware attualmente installata. Ciò può essere utile per risolvere problemi persistenti o ricominciare da capo con la configurazione predefinita del firmware corrente.

    Fare riferimento a [Ripristina firmware](../../interface_guide/reset_firmware.md) per i dettagli.

=== "Log"

    La pagina Log fornisce l'accesso a vari log che registrano le attività e gli eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * Registro di sistema: registri dettagliati di eventi e attività a livello di sistema.
    * Registro del kernel: registri relativi alle operazioni e agli eventi del kernel.
    * Registro arresti anomali: registrazioni di arresti anomali ed errori del sistema, utili per diagnosticare problemi critici.
    * Cloud Log: registri di interazioni e attività relative ai servizi GoodCloud integrati con il router.
    * Registro Nginx: registri dal server Web Nginx, se utilizzato dal router, che descrivono in dettaglio il traffico Web e le operazioni del server.

    Inoltre, la pagina presenta un pulsante Esporta registro, che consente di esportare tutti i registri raccolti per l'analisi del supporto tecnico. Questa funzione è preziosa per diagnosticare problemi complessi e ottenere assistenza professionale.

    Fare riferimento a [Log](../../interface_guide/log.md) per i dettagli.

=== "Advanced Settings"

    La pagina Impostazioni avanzate fornisce l'accesso alle opzioni di configurazione avanzate tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di ottimizzare le impostazioni e le funzionalità del proprio router oltre le opzioni dell'interfaccia di base. Ciò include configurazioni di rete dettagliate, impostazioni del firewall e altre personalizzazioni avanzate del sistema.

    Per i dettagli fare riferimento a [Impostazioni avanzate](../../interface_guide/advanced_settings.md).
