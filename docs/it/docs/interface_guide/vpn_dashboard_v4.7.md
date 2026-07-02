# VPN Dashboard (Firmware v4.7 e precedenti)

Accedi al pannello di amministrazione web e vai su **VPN** -> **VPN Dashboard**.

La pagina VPN Dashboard mostra i dettagli della connessione VPN, come indirizzo del server, statistiche del traffico, IP virtuale del client e log di connessione. Consente inoltre di configurare impostazioni avanzate come VPN Kill Switch, criteri VPN, IP Masquerading, MTU e VPN Cascading.

Questa pagina e' divisa in due sezioni: [VPN Client](#vpn-client) e [VPN Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN Client

Quando apri questa pagina per la prima volta, se non e' disponibile alcun file di configurazione per OpenVPN e WireGuard, la pagina appare come segue. Fai clic su **Set Up Now** e verrai indirizzato alla pagina [OpenVPN Client](openvpn_client.md) oppure [WireGuard Client](wireguard_client.md) per caricare il file di configurazione VPN.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_setup.png){class="glboxshadow"}

Una volta caricato, il file di configurazione verra' mostrato nella colonna **Configuration File**. Se hai caricato piu' file di configurazione, puoi cambiarli facendo clic sulla casella.

![configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_config.png){class="glboxshadow"}

### Client Options

Fai clic sull'icona dell'ingranaggio sulla destra per accedere alle opzioni del client OpenVPN o WireGuard.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options.png){class="glboxshadow"}

Le opzioni del client OpenVPN vengono mostrate come segue.

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_ovpn.png){class="glboxshadow"}

Le opzioni del client WireGuard vengono mostrate come segue.

![wg client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: se abilitato, sara' consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite VPN. Il server VPN deve pubblicizzare una route verso la subnet LAN di questo router.

    Ad esempio, come mostrato nel diagramma seguente, il router GL.iNet funziona come client VPN e si collega a un server VPN tramite il tunnel VPN. Quando questa opzione e' abilitata, sia il router GL.iNet sia i dispositivi sul lato LAN possono essere raggiunti dai dispositivi sul lato del server VPN, ad esempio un NAS. Per farlo, devi aggiungere una regola di instradamento sul server VPN per raggiungere la subnet LAN del router GL.iNet.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni Site-to-Site in cui il peer remoto conosce le tue subnet LAN.

- **MTU**: abbreviazione di Maximum Transmission Unit. Questa impostazione facoltativa consente di personalizzare l'MTU del tunnel VPN, sovrascrivendo il valore definito nel file di configurazione.

### Proxy Mode

La modalita' proxy predefinita per la connessione VPN e' **Global Proxy**. Puoi fare clic sulla casella in alto a destra per passare ad altre modalita' proxy.

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_proxy.png){class="glboxshadow"}

Sono disponibili tre modalita' proxy: **Global Proxy**, **Policy Mode** e **Route Mode**.

1. Global Proxy

    In questa modalita', tutto il traffico verra' instradato attraverso la VPN. Puo' essere attivata una sola istanza di client VPN.

2. Policy Mode

    Questa modalita' puo' essere ulteriormente suddivisa in tre criteri.

    - Basata sul dominio di destinazione o sull'IP.

        In questa modalita', solo il traffico di determinati siti web identificati tramite indirizzo IP o nome di dominio verra' instradato tramite VPN. Puo' essere attivata una sola istanza di client VPN.

    - Basata sul dispositivo client.

        In questa modalita', solo il traffico di determinati dispositivi LAN identificati tramite indirizzo MAC verra' instradato tramite VPN. Puo' essere attivata una sola istanza di client VPN.

    - Basata sulla VLAN.

        In questa modalita', solo il traffico di determinate VLAN verra' instradato tramite VPN. Puo' essere attivata una sola istanza di client VPN.

3. Route Mode

    - Auto Detect

        Verranno utilizzate le regole di instradamento definite in ogni file di configurazione del client VPN oppure fornite dal server VPN.

    - Customize Routing Rules

        Puoi configurare manualmente le regole di instradamento per ciascuna istanza di client VPN.

### Global Options

Fai clic su **Global Options** nell'angolo in alto a destra per configurare le impostazioni avanzate del client VPN.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: se abilitato, tutto il traffico Internet e' obbligato a passare esclusivamente attraverso il tunnel VPN e non puo' essere instradato tramite altre interfacce come la WAN locale dell'ISP. Se la connessione VPN cade inaspettatamente, tutto il traffico Internet viene completamente bloccato per impedire il ritorno alla WAN normale. Questo evita perdite VPN causate da guasti della VPN, impostazioni DNS errate del client e problemi simili.

    Questa funzione e' nota anche come [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Impedisce che i dati dell'utente vengano esposti online. Un tipico Kill Switch interrompe automaticamente l'accesso a Internet quando la connessione VPN fallisce. La funzione Block Non-VPN Traffic sui router GL.iNet offre una protezione piu' ampia contro le perdite e copre i seguenti scenari:

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applicazioni avviate prima della connessione VPN

    6. Perdite di traffico per singola applicazione

- **Allow Access WAN**: se abilitato, i dispositivi client locali possono continuare ad accedere ai servizi sul lato WAN, ad esempio stampanti, NAS e altri dispositivi nella subnet a monte, mentre la VPN e' attiva.

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Come mostrato nel diagramma sopra, abilitando questa funzione i dispositivi locali possono raggiungere gli host della subnet a monte, come stampanti e NAS.

    Questa opzione e' pensata principalmente per consentire ai client di accedere ai dispositivi nella subnet a monte. Tuttavia, il router non puo' distinguere il traffico della subnet a monte dal normale traffico Internet. Se i dispositivi client accedono direttamente a risorse tramite IP pubblici, esiste un potenziale rischio di perdita di traffico. Per questo motivo, **Allow Access WAN** e **Block Non-VPN Traffic** si escludono a vicenda e non possono essere abilitati contemporaneamente.

- **Services From GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione e' disabilitata per impostazione predefinita, poiche' questi servizi richiedono normalmente il reale indirizzo IP del dispositivo per funzionare correttamente.

## VPN Server

Se il router non e' mai stato configurato come server OpenVPN o WireGuard, la pagina apparira' come mostrato di seguito. Fai clic su **Set Up Now** e verrai indirizzato alla pagina **OpenVPN Server** oppure **WireGuard Server** per inizializzare il server VPN.

![vpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_setup.png){class="glboxshadow"}

Dopo che OpenVPN Server o WireGuard Server sono stati abilitati, la pagina mostrera' lo stato del server come segue.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_connected.png){class="glboxshadow"}

### Server Options

Fai clic sull'icona dell'ingranaggio sulla destra per accedere alle opzioni del server OpenVPN o WireGuard.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options.png){class="glboxshadow"}

Le opzioni del server OpenVPN vengono mostrate come segue.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_ovpn.png){class="glboxshadow"}

Le opzioni del server WireGuard vengono mostrate come segue.

![wg server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: se abilitato, le risorse all'interno della subnet LAN del server possono essere raggiunte attraverso il tunnel VPN.

* **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni Site-to-Site in cui il peer remoto conosce le tue subnet LAN.

* **MTU**: abbreviazione di Maximum Transmission Unit. Il valore MTU impostato per il tunnel sovrascrivera' le impostazioni MTU nel file di configurazione.

* **Client to Client**: se abilitato, i client VPN collegati a questo server possono accedere tra loro tramite i rispettivi IP del tunnel VPN. Se vuoi consentire ai client di accedere anche alle subnet LAN reciproche, il server VPN deve pubblicizzare le relative route verso quelle subnet LAN remote.

### Server Route Rule

Fai clic sull'icona della route sulla destra per personalizzare, se necessario, le regole di instradamento di OpenVPN o WireGuard.

![server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule.png){class="glboxshadow"}

La schermata OpenVPN Server Route Rule viene mostrata come segue. Fai clic su **Add Route Rule**, inserisci **Target Address** e **Gateway**, quindi fai clic sull'icona verde di conferma per applicare.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

La schermata WireGuard Server Route Rule viene mostrata come segue. Fai clic su **Add Route Rule**, inserisci **Target Address** e **Gateway**, quindi fai clic sull'icona verde di conferma per applicare.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Nota**: in modalita' customize routes, il client VPN ignorera' il file di configurazione e la configurazione di instradamento fornita dal server. La scelta di usare o meno il tunnel VPN cifrato quando si accede a qualsiasi segmento di rete dipende dalle regole di instradamento impostate manualmente.

### Global Options

Fai clic su **Global Options** nell'angolo in alto a destra per configurare le impostazioni avanzate del server VPN.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: se abilitato, quando questo router funziona contemporaneamente come server VPN e client VPN, il traffico dei client VPN remoti collegati al server VPN di questo router verra' instradato attraverso il tunnel VPN a monte che questo router usa come client VPN. [Scopri di piu' su VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
