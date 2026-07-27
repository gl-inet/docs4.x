# Guida utente di Fortify (GL-MT6000)

## Panoramica del prodotto

Fortify (GL-MT6000) e' un router Wi-Fi 6 co-branded rilasciato congiuntamente da GL.iNet ed ExpressVPN. Ogni unita' include un abbonamento ExpressVPN gratuito di un anno. Gli utenti possono riscattare l'abbonamento e associare l'account direttamente dal pannello di amministrazione web del router. Dopo l'attivazione, tutto il traffico che passa attraverso il router utilizza la rete ad alta velocita' e la crittografia robusta di ExpressVPN per proteggere l'intera connessione di rete e la privacy online.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Come configurare Fortify

### 1. Accensione

Assembla l'adattatore di alimentazione in due parti. Collegalo al router Fortify e inseriscilo in una presa. Il router si avvia automaticamente.

### 2. Collegare un dispositivo

Collega un dispositivo, ad esempio computer, laptop o smartphone, al router tramite Wi-Fi o Ethernet.

- Ethernet

    Collega il dispositivo alla porta LAN del router con un cavo Ethernet.

- Wi-Fi

    Sul dispositivo, vai su Settings -> WLAN, individua il nome della rete Wi-Fi del router nell'elenco delle reti disponibili e inserisci la password. Il nome e la password predefiniti sono stampati sull'etichetta del router.

### 3. Accedere al pannello di amministrazione web

Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi e accedi. Scegli la lingua nell'angolo in alto a destra, imposta la password amministratore e fai clic su **Next**. La password deve essere lunga da 10 a 63 caratteri e contenere almeno due tra lettere maiuscole, lettere minuscole, numeri e simboli speciali.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Configura il Wi-Fi. Se modifichi le informazioni Wi-Fi, dovrai riconnettere il dispositivo al Wi-Fi del router usando le nuove credenziali.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Configurazione Internet

**Note:** Le istruzioni seguenti si applicano agli utenti che configurano il router tramite il pannello di amministrazione web GL.iNet. Se preferisci l'[app GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, scaricala e segui le istruzioni sullo schermo.

Configura Fortify con uno dei metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Se vuoi usare [Multi-WAN](../../interface_guide/multi-wan.md), configura piu' di una connessione Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Collega un cavo Ethernet tra la porta WAN del router Fortify e un dispositivo upstream, ad esempio un modem.

    Quando la connessione Internet e' stabilita correttamente, il LED del router diventa bianco fisso.

    Consulta [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) per istruzioni dettagliate.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Nel pannello di amministrazione web, vai alla sezione INTERNET -> Repeater e fai clic su **Connect**.
    2. Seleziona una rete Wi-Fi dall'elenco delle reti disponibili.
    3. Inserisci la password e fai clic su **Apply**.

    Quando la connessione Internet e' stabilita correttamente, il LED del router diventa bianco fisso.

    Consulta [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) per istruzioni dettagliate.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Collega lo smartphone alla porta USB del router con un cavo USB.
    2. Sullo smartphone, vai su Settings e abilita USB Tethering. Su iPhone, autorizza il dispositivo e abilita Personal Hotspot.
    3. Nel pannello di amministrazione web, vai alla sezione INTERNET -> Tethering e fai clic su **Connect**.

    Quando la connessione Internet e' stabilita correttamente, il LED del router diventa bianco fisso.

    Consulta [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) per istruzioni dettagliate.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Collega un modem USB cellulare alla porta USB del router per condividere la connessione Internet del modem con tutti i dispositivi connessi.

    Quando la connessione Internet e' stabilita correttamente, il LED del router diventa bianco fisso.

    Consulta [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) per istruzioni dettagliate.

---

Di seguito trovi una panoramica delle funzioni nel pannello di amministrazione web di Fortify.

## Wireless

La pagina Wireless consente di configurare le reti Wi-Fi di Fortify, incluse Main Network, Guest Network e IoT Network. Ogni rete supporta le bande 2,4 GHz e 5 GHz.

Per configurare Wireless, consulta [Wireless](../../interface_guide/wireless_v4.9.md).

## Clients

La pagina Clients mostra informazioni sui dispositivi connessi, tra cui nome dispositivo, tipo di connessione, indirizzi IP e MAC, velocita' di download e upload, traffico, e consente di bloccare client specifici con un clic o eseguire altre azioni.

Consulta [Clients](../../interface_guide/clients.md) per i dettagli.

## Servizi cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un modo semplice per accedere e gestire da remoto i router GL.iNet.

    Consulta [GoodCloud](../../interface_guide/cloud.md) per i dettagli.

=== "AstroWarp"

    AstroWarp e' pensato per reti remote fluide sui router GL.iNet. Usa il protocollo AmneziaWG con offuscamento del traffico integrato per fornire accesso remoto stabile e sicuro.

    Consulta [AstroWarp](../../interface_guide/astrowarp.md) per i dettagli.

## VPN

Una VPN (virtual private network) stabilisce tunnel di traffico sicuri e crittografati tra il dispositivo locale e il server VPN. Aggiunge privacy e sicurezza al client VPN e consente l'accesso alla rete remota del server VPN.

Fortify si integra con [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, consentendo di attivare una connessione ExpressVPN in pochi minuti. Ogni dispositivo Fortify include un abbonamento ExpressVPN gratuito di un anno, riscattabile e associabile dal pannello di amministrazione web.

Per riscattare l'abbonamento gratuito e configurare un tunnel VPN, consulta [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md).

Per configurare un server OpenVPN, consulta [OpenVPN Server](../../interface_guide/openvpn_server.md).

Per configurare un server WireGuard, consulta [WireGuard Server](../../interface_guide/wireguard_server.md).

## Rete

=== "Multi-WAN"

    Multi-WAN consente di usare piu' connessioni Internet contemporaneamente, ad esempio cellular, repeater ed ethernet. Se la connessione corrente non funziona, il router passa automaticamente a un'altra connessione.

    Consulta [Multi-WAN](../../interface_guide/multi-wan.md) per i dettagli.

=== "LAN"

    LAN e' la rete locale a cui il dispositivo si collega tramite Wi-Fi principale o cavo Ethernet. La pagina LAN include Basic Settings, DHCP Server Settings e Address Reservation.

    Consulta [LAN](../../interface_guide/lan.md) per i dettagli.

=== "Guest Network"

    Guest Network crea una rete Wi-Fi dedicata ai visitatori. E' isolata dalla rete principale e consente di impostare una sottorete ospite nei range IPv4 privati `192.168.0.0/16`, `172.16.0.0/12` o `10.0.0.0/8`.

    Consulta [Guest Network](../../interface_guide/guest_network.md) per i dettagli.

=== "IoT Network"

    IoT Network consente di creare una rete Wi-Fi dedicata ai dispositivi IoT, isolata dalla rete principale per migliorare compatibilita' e sicurezza.

    Consulta [IoT Network](../../interface_guide/iot_network.md) per i dettagli.

<br>

=== "DNS"

    Le impostazioni DNS controllano la traduzione dei nomi di dominio in indirizzi IP. Puoi usare server DNS ottenuti automaticamente, impostare server personalizzati e configurare le priorita' DNS.

    Consulta [DNS](../../interface_guide/dns.md) per i dettagli.

=== "Ethernet Port"

    Ethernet Port consente di gestire i ruoli delle porte WAN/LAN e visualizzare dettagli come indirizzo MAC e velocita' negoziata.

    Consulta [Ethernet Port](../../interface_guide/ethernet_port.md) per i dettagli.

=== "IPv6"

    IPv6 e' la versione piu' recente del protocollo Internet e fornisce uno spazio di indirizzi molto piu' ampio rispetto a IPv4.

    Consulta [IPV6](../../interface_guide/network_mode.md) per i dettagli.

=== "IGMP Snooping"

    IGMP Snooping e' una tecnica di ottimizzazione usata negli switch Ethernet per gestire e controllare il traffico multicast.

    Consulta [IGMP Snooping](../../interface_guide/igmp_snooping.md) per i dettagli.

<br>

=== "Network Mode"

    Network Mode definisce come un dispositivo si connette a una rete e comunica con altri dispositivi.

    Per configurarlo, consulta [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway estende le funzioni del router principale con AdGuard Home, DNS crittografato e VPN.

    Per configurarlo, consulta [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    Network Acceleration puo' ridurre il carico della CPU e accelerare l'inoltro dei pacchetti.

    Per configurarlo, consulta [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) analizza il contenuto dei pacchetti per identificare applicazioni e siti web con maggiore precisione tramite una libreria di firme. La funzione DPI di GL.iNet si integra con [Netify](https://www.netify.ai/){target="_blank"}.

    Consulta [DPI Engine](../../interface_guide/dpi_engine.md) per i dettagli.

=== "Data Statistics"

    Data Statistics categorizza e visualizza l'utilizzo della rete per applicazione, aiutando a monitorare traffico in tempo reale e storico.

    Consulta [Data Statistics](../../interface_guide/data_statistics.md) per i dettagli.

=== "Content Filter"

    Content Filter usa una classificazione basata su DPI per bloccare automaticamente siti web dannosi o malevoli.

    Consulta [Content Filter](../../interface_guide/content_filter.md) per i dettagli.

<br>

=== "QoS"

    QoS dà priorita' alle attivita' critiche, come videochiamate o gaming, durante la congestione di rete. Si applica al traffico dei client locali e ai tunnel VPN Client, ma non al traffico ricevuto quando il router funziona come VPN Server.

    Consulta [QoS](../../interface_guide/qos.md) per i dettagli.

=== "SQM"

    SQM (Smart Queue Management) gestisce il traffico di rete per ridurre latenza e bufferbloat.

    Consulta [SQM](../../interface_guide/sqm.md) per i dettagli.

=== "Parental Control"

    Parental Control aiuta a gestire i dispositivi dei figli, limitare il tempo di utilizzo e restringere l'accesso a determinati contenuti.

    Consulta [Parental Control](../../interface_guide/parental_control_v4.9.md) per i dettagli.

## Sicurezza

=== "Port forwarding"

    Port forwarding consente a server e dispositivi remoti su Internet di accedere ai dispositivi in una rete privata.

    Consulta [Port Forwarding](../../interface_guide/port_forwarding.md) per i dettagli.

=== "ACL"

    ACL (Access Control List) consente di creare regole per gestire il traffico di rete in base a protocolli, indirizzi dei dispositivi e porte. Se piu' regole sono in conflitto, il sistema applica quella con priorita' piu' alta.

    Consulta [ACL](../../interface_guide/acl.md) per i dettagli.

=== "Admin Access"

    Admin Access include impostazioni di sicurezza per proteggere rete e router da accessi non autorizzati, tra cui Access Control, Remote Access Control e Open Ports on Router.

    Consulta [Admin Access](../../interface_guide/admin_access.md) per i dettagli.

=== "NAT Mode"

    NAT Mode consente di abilitare o disabilitare Full Cone NAT e SIP ALG.

    Consulta [NAT Mode](../../interface_guide/nat_settings.md) per i dettagli.

## Applicazioni

=== "Plug-ins"

    Un plug-in aggiunge funzioni specifiche a un programma o sistema esistente.

    Consulta [Plug-ins](../../interface_guide/plugins.md) per i dettagli.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) rileva e aggiorna automaticamente in tempo reale l'indirizzo IP associato a un dominio.

    Consulta [Dynamic DNS](../../interface_guide/ddns.md) per i dettagli.

=== "Network Storage"

    Network Storage fornisce archiviazione centralizzata accessibile da piu' utenti e dispositivi sulla rete.

    Consulta [Network Storage](../../interface_guide/network_storage.md) per i dettagli.

=== "AdGuard Home"

    AdGuard Home blocca annunci e tracker a livello di rete agendo come server DNS per filtrare contenuti indesiderati.

    Consulta [AdGuard Home](../../interface_guide/adguardhome.md) per i dettagli.

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} puo' aiutare a proteggere l'ambiente digitale dei bambini. Nell'ambito della partnership tra GL.iNet e Bark, Fortify (GL-MT6000) offre gratuitamente il piano Bark Home.

    Consulta [Bark](../../interface_guide/bark.md) per i dettagli.

=== "Tailscale"

    Tailscale consente di accedere in modo sicuro ai propri dispositivi e applicazioni ovunque. Fortify (GL-MT6000) puo' unirsi a una rete virtuale Tailscale per l'accesso remoto alle risorse WAN e LAN.

    Consulta [Tailscale](../../interface_guide/tailscale.md) per i dettagli.

=== "ZeroTier"

    ZeroTier crea reti virtuali sicure via Internet, collegando dispositivi come se fossero nella stessa rete locale.

    Consulta [ZeroTier](../../interface_guide/zerotier.md) per i dettagli.

=== "Tor"

    Tor e' software libero e open source per comunicazioni anonime e navigazione piu' privata.

    Consulta [Tor](../../interface_guide/tor.md) per i dettagli.

## Sistema

=== "Overview"

    Overview mostra lo stato attuale e le metriche del router, tra cui CPU Average Load, Memory Usage, LED Control, Flash Usage, Device Info ed External Storage.

    Consulta [Overview](../../interface_guide/system_overview.md) per i dettagli.

=== "Admin Password"

    Admin Password consente di impostare o modificare la password dell'interfaccia amministrativa del router.

    Consulta [Admin Password](../../interface_guide/admin_password.md) per i dettagli.

=== "Upgrade"

    Upgrade viene usato per aggiornare il firmware del router. Include Firmware Online Upgrade e Firmware Local Upgrade.

    Consulta [Upgrade](../../interface_guide/upgrade.md) per i dettagli.

=== "Scheduled Tasks"

    Scheduled Tasks automatizza le funzioni del router secondo una pianificazione, tra cui LED Display Schedule, Schedule Reboot e 5GHz / 2.4GHz Wi-Fi Status Schedule.

    Consulta [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) per i dettagli.

<br>

=== "Time Zone"

    Time Zone imposta il fuso orario corretto per attivita' pianificate, log ed eventi di sistema.

    Consulta [Time Zone](../../interface_guide/time_zone.md) per i dettagli.

=== "Reset Firmware"

    Reset Firmware ripristina il firmware corrente alle impostazioni predefinite e cancella le configurazioni personalizzate.

    Consulta [Reset Firmware](../../interface_guide/reset_firmware.md) per i dettagli.

=== "Log"

    Log consente di accedere a System Log, Kernel Log, Crash Log, Cloud Log e Nginx Log. Il pulsante Export Log esporta i log raccolti per l'analisi del supporto tecnico.

    Consulta [Log](../../interface_guide/log.md) per i dettagli.

=== "Advanced Settings"

    Advanced Settings apre l'interfaccia OpenWrt LuCI per configurazioni avanzate.

    Consulta [Advanced Settings](../../interface_guide/advanced_settings.md) per i dettagli.
