# Guida utente di Slate AX (GL-AXT1800)

## Panoramica del prodotto

Slate AX (GL-AXT1800) e un router Wi-Fi 6 dual-band con velocita di connessione fino a 600 Mbps (2,4 GHz) + 1200 Mbps (5 GHz). Esegue OpenWrt 23.05. La velocita di crittografia VPN arriva fino a 667 Mbps e il dispositivo puo essere usato per ospitare server VPN. Slate AX e ideale per trasmissioni dati intensive, collegamento simultaneo di molti dispositivi o gaming a latenza ultra ridotta.

![gl-axt1800 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/hardware_info/gl-axt1800_interface.jpg){class="glboxshadow"}

## Contenuto della confezione

- 1 x Slate AX (GL-AXT1800)
- 1 x Manuale utente
- 1 x Cavo Ethernet
- 1 x Biglietto di ringraziamento
- 1 x Scheda di garanzia
- 1 x Alimentatore
- 1 x Convertitore (in base al Paese di spedizione)

![gl-ax1800 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/first_time_setup/axt1800_unboxing.jpg){class="glboxshadow"}

## Come configurare Slate AX

Guarda questo video di configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f7DYULL6ZSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Questo video utilizza un router GL.iNet diverso per mostrare la configurazione, ma i passaggi sono gli stessi per Slate AX e per gli altri modelli di router.)</small>

### 1. Accendi il router

Assembla l'alimentatore in due parti. Collegalo al router e inseriscilo in una presa di corrente. Il router si avviera automaticamente.

### 2. Collega un dispositivo

Collega un dispositivo, ad esempio un computer, un laptop o uno smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router utilizzando un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, vai in Settings -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password. Il nome di rete e la password predefiniti sono stampati sull'etichetta nella parte inferiore del router.

### 3. Accedi al pannello di amministrazione web

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso. Scegli la lingua e imposta la password di amministrazione, quindi fai clic su **Apply**.

Quando confermi i dettagli del Wi-Fi, tieni presente che se modifichi le informazioni del Wi-Fi dovrai ricollegare il dispositivo alla rete Wi-Fi del router usando le credenziali aggiornate.

### 4. Configurazione della connessione Internet

**Note:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci usare l'app GL.iNet, [scarica l'app](https://www.gl-inet.com/app/){target="_blank"} e segui le istruzioni mostrate sullo schermo.

Configura Slate AX usando uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura piu di una connessione Internet.

=== "Ethernet"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_ethernet.png){class="glboxshadow"}

    Collega un cavo Ethernet tra la porta WAN del router e un dispositivo upstream, ad esempio un modem.
    
    Quando la connessione a Internet va a buon fine, nella sezione Ethernet della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_repeater.png){class="glboxshadow"}

    1. Nella pagina INTERNET del pannello di amministrazione web, individua la sezione Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi tra quelle disponibili.
    3. Inserisci la password, quindi fai clic su **Apply**.
    
    Quando la connessione a Internet va a buon fine, nella sezione Repeater della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_tethering.png){class="glboxshadow"}

    1. Collega il dispositivo mobile alla porta USB del router tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita USB Tethering.
    3. Nella pagina INTERNET del pannello di amministrazione web, fai clic su **Connect** nella sezione Tethering.
    
    Quando la connessione a Internet va a buon fine, nella sezione Tethering della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-axt1800/internet/axt1800_cellular.png){class="glboxshadow"}

    Inserisci un modem USB cellulare nella porta USB del router. Questo metodo e utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

    Quando la connessione a Internet va a buon fine, nella sezione Cellular della pagina INTERNET compare un punto verde.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

## Come configurare una VPN

Una VPN (rete privata virtuale) crea traffico sicuro e crittografato tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza come client VPN e consente di accedere a una rete remota come server VPN. Slate AX supporta OpenVPN, WireGuard e Tor.

=== "OpenVPN"

    Slate AX, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate AX, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocita e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abbreviazione di The Onion Router, e una rete orientata alla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server gestiti da volontari (nodi) per nascondere posizione e utilizzo dell'utente, rendendo difficile tracciare le attivita online.
    
    * [Come configurare Tor](../../interface_guide/tor.md).

## Wireless e client

=== "Wireless"

    La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi a 5 GHz e 2,4 GHz, inclusi attivazione del Wi-Fi, potenza TX, nome della rete Wi-Fi (SSID), BSSID casuale, modalita di sicurezza Wi-Fi e password, visibilita dell'SSID, modalita Wi-Fi, larghezza di banda e canale.

    Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza nome, indirizzi IP e MAC, velocita di download e upload, traffico totale e offre la possibilita di bloccare il client o eseguire altre azioni.

    Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    Il servizio GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.
    
    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp e una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata specificamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi sull'intera rete, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Con un focus sulla gestione dell'intera rete e sul futuro supporto al controllo a livello hardware, AstroWarp offre una soluzione piu robusta e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.

    Per configurarla, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

## Applicazioni

=== "Plug-ins"

    Un plug-in e un componente software che aggiunge funzioni o funzionalita specifiche a un programma informatico esistente, consentendo di personalizzarne e ampliarne le capacita.
    
    Per configurarli, fai riferimento a [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva automaticamente e aggiorna in tempo reale l'indirizzo IP associato a un dominio. E particolarmente utile per gli utenti che hanno bisogno di un indirizzo IP statico per accedere a una rete remota.
    
    Per configurarlo, fai riferimento a [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network storage indica una soluzione centralizzata di archiviazione dati che consente a piu utenti e dispositivi di accedere e condividere file tramite una rete.
    
    Per configurarlo, fai riferimento a [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home e una soluzione di blocco di annunci e tracker a livello di rete che agisce come server DNS per filtrare contenuti indesiderati su tutti i dispositivi collegati alla rete domestica.
    
    Per configurarlo, fai riferimento a [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control e progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier e una soluzione di rete software-defined che consente agli utenti di creare reti virtuali sicure su Internet, collegando i dispositivi come se fossero sulla stessa rete locale.
    
    Per configurarlo, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale e un servizio VPN che consente di accedere ai dispositivi e alle applicazioni ovunque.
    
    Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

## Impostazioni di rete

=== "Port forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere a dispositivi all'interno di una rete privata.
    
    Per configurarlo, fai riferimento a [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet, ad esempio cellular, repeater ed ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, e una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimento dati ad alta velocita e condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.
    
    Per configurarla, fai riferimento a [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Consente di impostare una sottorete all'interno degli intervalli di indirizzi privati IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, specificare gli indirizzi IP di gateway e netmask e configurare impostazioni di sicurezza come l'isolamento AP per la rete ospite.

    Per configurarla, fai riferimento a [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione dagli attacchi DNS rebinding e sovrascrivere le impostazioni DNS di tutti i client, consentire ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalita delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS dalla connessione Ethernet.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "Port Management"

    La pagina Port Management consente di configurare le porte WAN e LAN, impostare l'interfaccia WAN/LAN su Ethernet, specificare modalita MAC e indirizzo MAC per l'interfaccia WAN e visualizzare la velocita negoziata della porta di rete.

    Per gestire le porte Ethernet, fai riferimento a [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Network mode indica le impostazioni di configurazione che determinano come un dispositivo si connette a una rete e comunica con altri dispositivi.
    
    Per configurarlo, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, o Internet Protocol version 6, e la versione piu recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto piu ampio, permettendo un numero virtualmente illimitato di indirizzi IP univoci, elemento essenziale per il crescente numero di dispositivi collegati a Internet.
    
    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in Gateway estende le funzionalita del router principale con caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN.
    
    Per configurarlo, fai riferimento ai seguenti link:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP snooping e una tecnica di ottimizzazione della rete usata negli switch Ethernet per gestire e controllare il traffico multicast.
    
    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    La pagina NAT Settings consente di abilitare o disabilitare le funzionalita Full Cone NAT e SIP ALG (Application Layer Gateway).

    Per configurarla, fai riferimento a [NAT Settings](../../interface_guide/nat_settings.md).

## Impostazioni di sistema

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

    La pagina Upgrade viene usata per aggiornare il firmware del router alla versione piu recente, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Firmware Online Upgrade: controlla e installa automaticamente la versione firmware piu recente direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Firmware Local Upgrade: consente di caricare manualmente un file firmware dal computer per aggiornare il router, offrendo controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni permettono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di automatizzare diverse funzioni del router in base a una pianificazione predefinita, migliorando praticita ed efficienza. Le funzioni principali di questa pagina includono:

    * LED Display Schedule: imposta una pianificazione per accendere o spegnere automaticamente i LED del router, riducendo l'inquinamento luminoso in determinati orari.
    * Schedule Reboot: configura il riavvio automatico del router a intervalli specifici per mantenere prestazioni e stabilita ottimali.
    * 5GHz Wi-Fi Status Schedule: imposta una pianificazione per controllare la banda Wi-Fi a 5 GHz, gestendo meglio disponibilita della rete e consumo energetico.
    * 2.4GHz Wi-Fi Status Schedule: imposta una pianificazione per controllare la banda Wi-Fi a 2,4 GHz, gestendo meglio disponibilita della rete e consumo energetico.
    
    Queste opzioni di pianificazione offrono maggiore controllo sul funzionamento del router, garantendo che soddisfi esigenze e preferenze specifiche.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attivita pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La pagina Toggle Button Settings consente di configurare il pulsante fisico del router, permettendo di assegnargli funzioni specifiche per un accesso e un controllo rapidi. Questa funzione offre scorciatoie pratiche per attivita e impostazioni comuni, migliorando l'esperienza d'uso e semplificando la gestione del router.

    Per istruzioni dettagliate, fai riferimento a [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    La pagina Log offre accesso a vari registri che memorizzano attivita ed eventi del router, aiutando nella risoluzione dei problemi e nel monitoraggio delle prestazioni. Questa pagina include:

    * System Log: log dettagliati relativi a eventi e attivita a livello di sistema.
    * Kernel Log: log relativi alle operazioni e agli eventi del kernel.
    * Crash Log: registrazioni di arresti anomali ed errori di sistema, utili per diagnosticare problemi critici.
    * Cloud Log: log delle interazioni e delle attivita legate ai servizi GoodCloud integrati nel router.
    * Nginx Log: log del server web Nginx, se usato dal router, che riportano traffico web e operazioni del server.
    
    Inoltre, la pagina include il pulsante Export Log, che consente di esportare tutti i log raccolti per l'analisi da parte del supporto tecnico. Questa funzione e molto utile per diagnosticare problemi complessi e ottenere assistenza professionale.

    Per istruzioni dettagliate, fai riferimento a [Log](../../interface_guide/log.md).

---

=== "Security"

    La pagina Security consente di configurare varie impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include opzioni per:

    * Admin Password: impostare o modificare la password dell'interfaccia amministrativa del router per garantire che solo gli utenti autorizzati possano modificare le impostazioni.
    * Local Access Control: gestire e limitare l'accesso all'interfaccia del router dai dispositivi collegati alla rete locale.
    * Remote Access Control: configurare e limitare l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la protezione dalle minacce esterne.
    * Open Ports on Router: controllare quali porte sono aperte sul router, limitando potenziali vulnerabilita e accessi non autorizzati.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate, fai riferimento a [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    La pagina Reset Firmware consente di ripristinare le impostazioni predefinite della versione firmware attualmente installata sul router, cancellando tutte le configurazioni personalizzate. Questo processo riporta il router alle impostazioni di default della versione firmware corrente. Puo essere utile per risolvere problemi persistenti o per ricominciare da zero con la configurazione predefinita del firmware attuale.

    Per istruzioni dettagliate, fai riferimento a [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La pagina Advanced Settings offre accesso a opzioni di configurazione avanzata tramite l'interfaccia OpenWrt LuCI, consentendo agli utenti esperti di regolare in modo dettagliato impostazioni e funzioni del router oltre a quelle disponibili nell'interfaccia di base. Include configurazioni di rete dettagliate, impostazioni firewall e altre personalizzazioni avanzate del sistema.

    Per istruzioni dettagliate, fai riferimento a [Advanced Settings](../../interface_guide/advanced_settings.md).
