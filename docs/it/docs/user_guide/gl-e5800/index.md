# Guida utente di Mudi 7 (GL-E5800)

## Panoramica del prodotto

Mudi 7 e un router da viaggio 5G NR Wi-Fi 7 portatile progettato per chi viaggia spesso e per utenti business, offrendo reti private affidabili per proteggere i dati dalle minacce informatiche. Integra 5G ad alta velocita, doppia SIM con commutazione automatica in caso di failover e Wi-Fi 7 (canali da 320 MHz e 4K QAM) per una connettivita stabile e veloce, adatta a download rapidi, streaming 4K e videoconferenze fluide anche in ambienti affollati.

Dotato di touchscreen, Mudi 7 consente di monitorare in tempo reale l'utilizzo dei dati, la potenza del segnale, i dispositivi collegati e la velocita dei client, oltre a regolare le impostazioni con semplici tocchi per un controllo intuitivo e pratico.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Contenuto della confezione

- 1 x Mudi 7 (GL-E5800)
- 1 x Pacco batteria
- 1 x Cavo USB-C da 10 Gbps
- 1 x Custodia da viaggio
- 1 x Manuale utente

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Guarda qui sotto il video di unboxing di Mudi 7.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Come configurare Mudi 7

Guarda questo video di configurazione oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Installa la scheda SIM

Installa una o piu Nano-SIM su Mudi 7. Se preferisci usare eSIM, salta questo passaggio e passa al passaggio 2.

Per prima cosa, rimuovi il coperchio della batteria, quindi estrai la batteria di Mudi 7.

Successivamente, inserisci la o le Nano-SIM. Se usi una sola scheda, dai priorita alla SIM 1.

Infine, rimetti la batteria e richiudi il coperchio.

![install nano-sim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/install_nano-sim.png){class="glboxshadow"}

### 2. Accendi il dispositivo

Tieni premuto il pulsante di accensione per **3 secondi**, oppure collega un alimentatore.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power_on.png){class="glboxshadow"}

### 3. Impostazioni di base

Segui le istruzioni sullo schermo per configurare le impostazioni di base, inclusi **screen passcode**, **admin password**, **Wi-Fi name**, **Wi-Fi password** e **frequency bands**.

**Tip**: La password amministratore predefinita corrisponde agli ultimi 9 caratteri del numero di serie del dispositivo, seguiti dal carattere `#`. Puoi usare la password predefinita oppure impostarne una personalizzata.

### 4. Configurazione della connessione Internet

Configura Mudi 7 usando uno dei metodi di connessione Internet supportati: Cellular, Ethernet, Repeater, Tethering e USB Ethernet. Se desideri usare la funzione [Multi-WAN](../../interface_guide/multi-wan.md), configura piu di una connessione Internet.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}

    Mudi 7 dispone di **eSIM integrata** e di **doppi slot Nano-SIM**. Puoi collegarti a Internet acquistando un pacchetto eSIM, senza richiedere una scheda SIM fisica, oppure inserire le tue Nano-SIM per accedere alla rete mobile 5G.

    **Configurare l'eSIM**:

    1. Sul touchscreen, vai su **Cellular** -> **SIM Card Switch** e attiva l'interruttore per **abilitare eSIM**.

        ![enable esim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/lcd_enable_esim.png){class="glboxshadow" width="590"}

    2. Accedi al pannello di amministrazione web e vai su **INTERNET** -> **Cellular** -> **eSIM Management**.

        ![esim management](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/esim_management.png){class="glboxshadow" width="590"}

    3. Nella finestra popup, fai clic su **Add eSIM Profile** in basso.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile1.png){class="glboxshadow" width="590"}

        Carica il tuo profilo eSIM tramite codice QR o codice di attivazione, quindi fai clic su **Install**. Tieni presente che la maggior parte dei profili eSIM può essere scaricata e aggiunta una sola volta.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile2.png){class="glboxshadow"}

        **Suggerimento**: se non hai ancora acquistato un profilo eSIM, puoi comprarne uno nell'eSIM Profile Recommended Store.

        ![recommended store](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/recommended_store.png){class="glboxshadow" width="590"}

    4. Una volta caricato, vai su **Cellular** e fai clic su **SIM Card Switch**.

        ![sim card switch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/sim_card_switch.png){class="glboxshadow" width="590"}

        Nella finestra popup, seleziona **eSIM** come scheda SIM attiva, quindi fai clic su **Apply**.

        ![active sim card](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/active_sim_card.png){class="glboxshadow"}

    5. Il router inizierà a connettersi tramite questo profilo eSIM. Attendi e verifica che la connessione vada a buon fine.

    **Configurare la Nano-SIM**:

    1. Rimuovi il coperchio posteriore, estrai la batteria, inserisci la Nano-SIM nello slot, quindi reinstalla la batteria.

    2. Il router inizierà automaticamente a connettersi tramite questa Nano-SIM. Attendi e verifica che la connessione vada a buon fine.

    Quando la connessione a Internet va a buon fine, le barre del segnale e lo stato della rete cellulare compariranno nell'angolo superiore destro del touchscreen. Puoi anche controllare i dettagli della connessione nel pannello di amministrazione web.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md).

    !!! note

        1. L'eSIM integrata e la SIM 2 sono mutuamente esclusive e non possono essere attivate contemporaneamente. L'eSIM e disabilitata per impostazione predefinita. Se abiliti l'eSIM, la SIM 2 non funzionera anche se e inserita una scheda SIM.
        2. Poiche Mudi 7 dispone di eSIM integrata, una scheda eSIM fisica SIMPoYo verra riconosciuta come una normale scheda SIM senza funzionalita eSIM su Mudi 7.

=== "Ethernet"

    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Collega la porta Ethernet di Mudi 7 a una sorgente di rete upstream, ad esempio un modem ISP, uno switch di rete o una presa Ethernet a muro, tramite un cavo Ethernet.
    2. Sul touchscreen oppure nel pannello di amministrazione web, vai su **Network** -> **Ethernet Ports**, imposta il ruolo della porta su **WAN** e fai clic su **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Quando la connessione a Internet va a buon fine, un'icona della porta Ethernet comparira nell'angolo superiore destro del touchscreen. Puoi anche controllare i dettagli della connessione nel pannello di amministrazione web.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. Sul touchscreen oppure nel pannello di amministrazione web, vai su **Internet** -> **Repeater** e fai clic su **Connect**. Mudi 7 iniziera la scansione delle reti Wi-Fi disponibili.
    2. Seleziona la rete Wi-Fi che desideri estendere.
    3. Inserisci la password e fai clic su **Apply**.
    4. Quando la connessione a Internet va a buon fine, un'icona Wi-Fi comparira nell'angolo superiore destro del touchscreen. Puoi anche controllare i dettagli della connessione nel pannello di amministrazione web.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Collega il dispositivo mobile, ad esempio uno smartphone o un dongle USB, alla porta USB-C di Mudi 7 tramite un cavo USB.
    2. Sul dispositivo mobile, vai nelle impostazioni e abilita **USB Tethering**. Se usi un iPhone, tocca **Trust This Device** quando richiesto.
    3. Mudi 7 si colleghera quindi automaticamente al dispositivo. Se non si connette, ripeti i passaggi sopra oppure accedi al pannello di amministrazione web e controlla la connessione Tethering nella pagina INTERNET.
    4. Quando la connessione a Internet va a buon fine, un'icona a forma di catena comparira nell'angolo superiore destro del touchscreen. Puoi anche controllare i dettagli della connessione nel pannello di amministrazione web.

    Per istruzioni dettagliate, fai riferimento a [Collegarsi a Internet tramite USB tethering](../../interface_guide/internet_tethering.md).

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 e dotato di una porta USB-C con supporto **OTG**, che consente di aggiungere una seconda porta Ethernet per Dual-Ethernet WAN. Per usarla e necessario un **adattatore USB-C to Ethernet venduto separatamente**.

    <small>*USB OTG (On-The-Go) e uno standard USB che consente a dispositivi compatibili, come i router, di passare tra il ruolo di host e quello di periferica, permettendo trasmissione dati diretta e interazione di alimentazione senza un dispositivo host separato.*</small>

    1. Collega una sorgente di rete upstream, ad esempio un modem ISP, uno switch di rete o una presa Ethernet a muro, alla porta USB-C di Mudi 7 tramite un adattatore USB-C to Ethernet.
    2. Sul touchscreen oppure nel pannello di amministrazione web, vai su **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, imposta il ruolo della porta su **WAN** e fai clic su **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 si colleghera quindi automaticamente al dispositivo. Se non si connette, ripeti i passaggi sopra oppure accedi al pannello di amministrazione web e controlla la connessione USB Ethernet nella pagina INTERNET.
    4. Quando la connessione a Internet va a buon fine, un'icona USB e un'icona della porta Ethernet compariranno nell'angolo superiore destro del touchscreen. Puoi anche controllare i dettagli della connessione nel pannello di amministrazione web.

## Aggiornamento firmware

!!! note "Prima di eseguire l'aggiornamento, tieni presente quanto segue:"

    1. Per conservare le configurazioni di Mudi 7, seleziona **Keep Settings** nella pagina di aggiornamento.
    2. Non selezionare **Keep Settings** quando esegui il downgrade, poiché potrebbero verificarsi problemi di compatibilità.
    3. L'aggiornamento del firmware richiede un certo consumo di dati. Se il piano dati della SIM è limitato, si consiglia di collegare il router a Internet con altri metodi, ad esempio Repeater o USB Tethering, per evitare consumo dati aggiuntivo.

Puoi aggiornare il firmware di Mudi 7 tramite touchscreen o pannello di amministrazione web.

### Aggiornamento tramite touchscreen

1. Collega Mudi 7 a Internet.

2. Una volta connesso, il sistema verificherà automaticamente la disponibilità di aggiornamenti firmware. Se è disponibile un nuovo firmware, sullo schermo comparirà una notifica. Nella finestra popup, fai clic su **Go to Upgrade** per procedere.

    ![go to upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade1.png){class="glboxshadow" width="300"}

3. Se la finestra popup non compare, nella schermata principale fai clic su **More** -> **About Device** -> **Version & Upgrade** -> **Download & Upgrade**, quindi segui le istruzioni sullo schermo per aggiornare il firmware.

    ![download & upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade2.png){class="glboxshadow" width="300"}

### Aggiornamento via web

1. Aggiornamento online

    Accedi al pannello di amministrazione web e vai su **SYSTEM** -> **Upgrade** -> **Firmware Online Upgrade** per aggiornare il firmware del router.

    Per i dettagli, fai riferimento [qui](../../interface_guide/upgrade.md#online-upgrade).

2. Aggiornamento locale

    Accedi al pannello di amministrazione web e vai su **SYSTEM** -> **Upgrade** -> **Firmware Local Upgrade** per aggiornare il firmware del router.

    Per i dettagli, fai riferimento [qui](../../interface_guide/upgrade.md#local-upgrade).

## Ripristino e reset

Puoi ripristinare la connettivita di rete oppure riportare Mudi 7 alle impostazioni di fabbrica usando il pulsante fisico di reset.

**Note**: prima di eseguire il reset, assicurati che Mudi 7 abbia completato l'avvio. **NON** premere il pulsante di reset immediatamente dopo l'accensione, perche potresti attivare la modalita failsafe U-Boot.

Rimuovi il coperchio posteriore e troverai il pulsante di reset come mostrato di seguito.

![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

!!! note "Network Repair"

    Tieni premuto il pulsante di reset per **4 secondi**, quindi rilascialo per riparare la rete. Durante la pressione, presta attenzione ai prompt sullo schermo e procedi come indicato.

    Questa operazione riavviera l'interfaccia di rete, mantenendo impostazioni Wi-Fi, configurazioni VPN disabilitate, impostazioni di sistema e altro ancora.

    **Note**:

    1. Se il Wi-Fi e stato disabilitato, un soft reset ripristinera il Wi-Fi allo stato predefinito abilitato.
    2. Un soft reset puo essere usato anche per riportare rapidamente il dispositivo dalla modalita non-router alla modalita router.

!!! note "Device Reset"

    Tieni premuto il pulsante di reset per **10 secondi**, quindi rilascialo per eseguire un hard reset. Durante la pressione, presta attenzione ai prompt sullo schermo e procedi come indicato.

    Questa operazione cancellera tutte le impostazioni. Procedi con cautela.

## Accedi al pannello di amministrazione web

Puoi accedere al pannello di amministrazione web di Mudi 7 per configurare o controllare altre impostazioni.

Per prima cosa, collega un dispositivo, ad esempio un computer, un laptop o uno smartphone, a Mudi 7 tramite Wi-Fi, cavo Ethernet o cavo USB.

- **Wi-Fi**

    - <u>QR code</u>: usa il dispositivo per scansionare il codice QR sullo schermo di Mudi 7. Quindi fai clic su "Join" sul dispositivo per collegarti.
    - <u>Manual Connect</u>: sul dispositivo, vai in Settings -> WLAN, individua il nome della rete Wi-Fi di Mudi 7 nell'elenco delle reti disponibili e inserisci la password per collegarti. Le credenziali predefinite sono stampate sull'etichetta.

- **Ethernet**

    Collega il dispositivo alla porta Ethernet, che per impostazione predefinita e LAN, di Mudi 7 tramite un cavo Ethernet.

- **USB**

    Collega il dispositivo alla porta USB-C di Mudi 7 tramite un cavo USB. La porta USB-C con supporto OTG consente di accedere alla WebGUI di Mudi 7 nel passaggio successivo.

Apri quindi un browser web e inserisci `192.168.8.1` nella barra degli indirizzi per accedere alla pagina di login. Seleziona la lingua, imposta la password di amministrazione e fai clic su **Apply**.

Verrrai quindi autenticato nel pannello di amministrazione web di Mudi 7.

Di seguito trovi una panoramica delle funzioni presenti nel pannello di amministrazione web di Mudi 7.

## Wireless

La pagina Wireless consente di configurare le impostazioni delle reti Wi-Fi a 6 GHz, 5 GHz e 2,4 GHz, tra cui attivazione del Wi-Fi, potenza TX, nome della rete Wi-Fi (SSID), BSSID casuale, modalita di sicurezza Wi-Fi e password, visibilita dell'SSID, modalita Wi-Fi, larghezza di banda e canale.

Per configurarla, fai riferimento a [Wireless](../../interface_guide/wireless.md).

**Note**: ci sono alcune differenze tra le impostazioni wireless di Mudi 7 e quelle degli altri router GL.iNet Wi-Fi 7.

1. A causa dei vincoli hardware del chipset, il Wi-Fi a 5 GHz e quello a 6 GHz non possono essere abilitati contemporaneamente.
2. Quando il Repeater e abilitato, la Guest Network verra disabilitata automaticamente.
3. Come richiesto dalle normative, passa il Wi-Fi alla modalita Outdoor quando lo usi all'aperto. Questo puo ridurre l'area di copertura. Puoi cambiare Usage Environment, Indoor oppure Outdoor, nella parte superiore della pagina Wireless.

## Client

La pagina Clients mostra informazioni sui dispositivi collegati. Per ogni client visualizza nome, indirizzi IP e MAC, velocita di download e upload, traffico totale e offre la possibilita di bloccare il client o eseguire altre azioni.

Per configurarla, fai riferimento a [Clients](../../interface_guide/clients.md).

## Servizi cloud

=== "GoodCloud"

    Il servizio di gestione cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice e immediato per accedere da remoto e gestire i router GL.iNet.

    Per configurarlo, fai riferimento a [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp e una piattaforma di rete avanzata progettata per offrire networking remoto senza interruzioni e gestione remota dei dispositivi. Sviluppata specificamente per l'integrazione con i router GL.iNet, AstroWarp supporta una gestione completa dei dispositivi sull'intera rete, consentendo il controllo sia dei dispositivi a monte sia di quelli a valle. Con un focus sulla gestione dell'intera rete e sul futuro supporto al controllo a livello hardware, AstroWarp offre una soluzione piu robusta e affidabile per la gestione dei dispositivi e il mantenimento di reti sicure e stabili.

    Per configurarla, fai riferimento a [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Una VPN crea traffico sicuro e crittografato tra il dispositivo e il server VPN. Offre un ulteriore livello di privacy e sicurezza come client VPN e consente di accedere a una rete remota come server VPN. Mudi 7 supporta OpenVPN e WireGuard.

=== "OpenVPN"

    Mudi 7, come gli altri router GL.iNet, supporta il protocollo OpenVPN, che offre un elevato livello di sicurezza. Per configurare OpenVPN, segui questi tutorial:

    * [Come configurare un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Come configurare un server OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mudi 7, come gli altri router GL.iNet, supporta il protocollo WireGuard, che offre ottima velocita e praticita. Per configurare WireGuard, segui questi tutorial:

    * [Come configurare un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Come configurare un server WireGuard](../../interface_guide/wireguard_server.md)

## Rete

=== "Multi-WAN"

    Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet, ad esempio ethernet, repeater, tethering, cellular e USB ethernet, contemporaneamente. Se la connessione Internet attuale si interrompe, il router passera automaticamente a un'altra connessione Internet. In questo modo l'accesso a Internet rimane fluido e ininterrotto.

    Per configurarlo, fai riferimento a [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, o Local Area Network, e una rete che collega computer e dispositivi all'interno di un'area geografica limitata, ad esempio una casa o un ufficio. Consente trasferimento dati ad alta velocita e condivisione delle risorse, permettendo ai dispositivi di comunicare tra loro in modo efficiente.

    Per configurarla, fai riferimento a [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Consente di impostare una sottorete all'interno degli intervalli di indirizzi privati IPv4 192.168.0.0/16, 172.16.0.0/12 o 10.0.0.0/8, specificare gli indirizzi IP di gateway e netmask e configurare impostazioni di sicurezza come l'isolamento AP per la rete ospite.

    Per configurarla, fai riferimento a [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La pagina DNS consente di impostare server DNS personalizzati, abilitare la protezione dagli attacchi DNS rebinding e sovrascrivere le impostazioni DNS di tutti i client, consentire ai DNS personalizzati di sovrascrivere i DNS della VPN e configurare la modalita delle impostazioni del server DNS su automatica oppure specificare manualmente i server DNS dalla connessione Ethernet.

    Per configurarla, fai riferimento a [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La pagina Ethernet Port consente di impostare il ruolo della porta Ethernet, cioe usarla come WAN o LAN, cambiare la modalita MAC e l'indirizzo MAC per l'interfaccia WAN e visualizzare la velocita negoziata della porta.

    Mudi 7 dispone di una singola porta Ethernet, che per impostazione predefinita e LAN. Se necessario, puoi cambiarla in WAN dal touchscreen oppure dal pannello di amministrazione web.

    Per gestire le porte Ethernet, fai riferimento a [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, abbreviazione di Internet Protocol version 6, e la versione piu recente del protocollo Internet progettata per sostituire IPv4. Offre uno spazio di indirizzamento molto piu ampio, permettendo un numero virtualmente illimitato di indirizzi IP univoci, elemento essenziale per il crescente numero di dispositivi collegati a Internet.

    Per configurarlo, fai riferimento a [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping e una tecnica di ottimizzazione della rete usata negli switch Ethernet per gestire e controllare il traffico multicast.

    Per configurarlo, fai riferimento a [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Network mode indica la configurazione che determina come un dispositivo si connette a una rete e comunica con altri dispositivi.

    Per configurarlo, fai riferimento a [Network Mode](../../interface_guide/network_mode.md).

    **Note**: Mudi 7 supporta le modalita Router, Access Point ed Extender. Non supporta la modalita WDS.

=== "Drop-in gateway"

    Drop-in gateway estende le funzionalita del router principale, inclusi AdGuard Home, DNS crittografato e client VPN.

    Per configurarlo, fai riferimento ai seguenti link:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Come configurare Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network acceleration puo ridurre il carico della CPU e accelerare l'inoltro dei pacchetti di traffico.

    Per configurarla, fai riferimento a [Network Acceleration](../../interface_guide/network_acceleration.md).

## Controllo del traffico

=== "Parental Control"

    Parental Control e progettato per aiutarti a gestire e controllare i dispositivi dei tuoi figli. Include la limitazione del tempo di utilizzo dello schermo e la restrizione dell'accesso a determinati contenuti.

    Per configurarlo, fai riferimento a [Parental Control](../../interface_guide/parental_control.md).

## Sicurezza

=== "Port Forwarding"

    Il port forwarding consente a server remoti e dispositivi su Internet di accedere a dispositivi all'interno di una rete privata.

    Per configurarlo, fai riferimento a [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    La pagina Management Control consente di configurare varie impostazioni di sicurezza per proteggere la rete e il router da accessi non autorizzati. Questa pagina include le seguenti opzioni:

    * Local Access Control: gestire e limitare l'accesso all'interfaccia del router dai dispositivi collegati alla rete locale.
    * Remote Access Control: configurare e limitare l'accesso all'interfaccia del router da posizioni remote tramite Internet, migliorando la protezione dalle minacce esterne.
    * Open Ports on Router: controllare quali porte sono aperte sul router, limitando potenziali vulnerabilita e accessi non autorizzati.

    Queste impostazioni aiutano a mantenere un ambiente di rete sicuro, proteggendo sia il router sia i dispositivi collegati.

    Per istruzioni dettagliate, fai riferimento a [Security](../../interface_guide/security.md).

=== "NAT Mode"

    La pagina NAT Mode consente di abilitare o disabilitare le funzioni Full Cone NAT e SIP ALG.

    Per configurarla, fai riferimento a [NAT Mode](../../interface_guide/nat_settings.md).

## Applicazioni

=== "Plug-ins"

    Un plug-in e un componente software che aggiunge funzioni o funzionalita specifiche a un programma informatico esistente, consentendo personalizzazione e ampliamento delle sue capacita.

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

=== "ZeroTier"

    ZeroTier e una soluzione di rete software-defined che consente agli utenti di creare reti virtuali sicure su Internet, collegando i dispositivi come se fossero sulla stessa rete locale.

    Per configurarlo, fai riferimento a [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale e un servizio VPN che consente di accedere ai dispositivi e alle applicazioni ovunque.

    Per configurarlo, fai riferimento a [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, abbreviazione di The Onion Router, e una rete orientata alla privacy che consente comunicazioni anonime su Internet. Instrada il traffico Internet attraverso una serie di server gestiti da volontari per nascondere posizione e utilizzo dell'utente, rendendo difficile tracciare le attivita online.

    Per configurarlo, fai riferimento a [Tor](../../interface_guide/tor.md).

## Sistema

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

    La pagina Admin Password consente di impostare o modificare la password dell'interfaccia amministrativa del router.

    La password amministratore deve soddisfare i seguenti requisiti:

    * Minimo 10 caratteri e massimo 63 caratteri.
    * Sono consentiti lettere, con distinzione tra maiuscole e minuscole, numeri e simboli `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``.
    * Sono richiesti almeno due tra lettere maiuscole, lettere minuscole, numeri e simboli.

=== "Upgrade"

    La pagina Upgrade viene usata per aggiornare il firmware del router alla versione piu recente, garantendo prestazioni migliori, maggiore sicurezza e nuove funzioni. Questa pagina offre due opzioni di aggiornamento:

    * Firmware Online Upgrade: controlla e installa automaticamente la versione firmware piu recente direttamente dal server del produttore, semplificando il processo di aggiornamento.
    * Firmware Local Upgrade: consente di caricare manualmente un file firmware dal computer per aggiornare il router, offrendo controllo sulla versione e sul momento dell'aggiornamento.

    Queste opzioni permettono di mantenere il router aggiornato con gli ultimi miglioramenti e le ultime correzioni.

    Per istruzioni dettagliate, fai riferimento a [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La pagina Scheduled Tasks consente di configurare il riavvio automatico del router a intervalli specifici, contribuendo a mantenere prestazioni e stabilita ottimali.

    Per istruzioni dettagliate, fai riferimento a [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

    **Note**: Mudi 7 non supporta la pianificazione del display LED e la pianificazione dello stato Wi-Fi.

=== "Display Management"

    La pagina Display Management consente di gestire il touchscreen e le impostazioni correlate.

    - Wallpaper: personalizza lo sfondo e lo stile di attivazione del display.
    - Brightness: regola la luminosita del touchscreen. Usa il cursore oppure inserisci una percentuale per adattarla a diverse condizioni di luce.
    - Personalised Signature: aggiungi un testo personalizzato al touchscreen per mostrare il tuo stile o per un riconoscimento rapido.
    - Auto Lock: imposta il tempo di attesa per il blocco automatico dello schermo in assenza di attivita. L'intervallo va da 15 secondi a 5 minuti.
    - Passcode: imposta un codice per il touchscreen per un ulteriore livello di sicurezza.

    Per istruzioni dettagliate, fai riferimento a [Display Management](../../interface_guide/display_management.md).

=== "USB & Power"

    La pagina USB & Power consente di configurare le impostazioni legate alla USB e alla gestione energetica del router, ad esempio protocollo USB, direzione dell'alimentazione, timeout di inattivita e comportamento in standby.

    Per istruzioni dettagliate, fai riferimento a [USB & Power](../../interface_guide/usb_power.md).

---

=== "Time Zone"

    La pagina Time Zone consente di impostare il fuso orario corretto per il router, assicurando che tutte le attivita pianificate, i log e gli eventi di sistema riportino timestamp accurati in base all'ora locale. Questa impostazione e essenziale per mantenere registrazioni precise e per la corretta esecuzione delle configurazioni basate sull'orario.

    Per istruzioni dettagliate, fai riferimento a [Time Zone](../../interface_guide/time_zone.md).

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
