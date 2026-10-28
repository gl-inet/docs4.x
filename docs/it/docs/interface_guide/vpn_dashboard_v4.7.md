# VPN Dashboard (Firmware v4.7 e precedenti) {#vpn-dashboard-firmware-v47-and-earlier}

Il contenuto di questa pagina si basa sulle versioni firmware v4.7.x e precedenti. Se il dispositivo esegue una versione firmware diversa, usa il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Versione firmware" data-placeholder="Firmware v4.7 e precedenti" markdown="1">

- [Firmware v4.8](vpn_dashboard_v4.8.md)
- [Firmware v4.9 e successivi](vpn_dashboard.md)

</div>

---
Accedi al pannello di amministrazione web e vai su **VPN** -> **VPN Dashboard**.

La pagina VPN Dashboard mostra i dettagli della connessione VPN, come indirizzo del server, statistiche del traffico, IP virtuale del client e log di connessione. Consente inoltre di configurare impostazioni avanzate come VPN Kill Switch, criteri VPN, IP Masquerading, MTU e VPN Cascading.

Questa pagina è divisa in due sezioni: [VPN Client](#vpn-client) e [VPN Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN Client {#vpn-client}

Quando apri questa pagina per la prima volta, se non è disponibile alcun file di configurazione per OpenVPN e WireGuard, la pagina appare come segue. Fai clic su **Set Up Now** e verrai indirizzato alla pagina [OpenVPN Client](openvpn_client.md) oppure [WireGuard Client](wireguard_client.md) per caricare il file di configurazione VPN.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_setup.png){class="glboxshadow"}

Una volta caricato, il file di configurazione verrà mostrato nella colonna **Configuration File**. Se hai caricato più file di configurazione, puoi cambiarli facendo clic sulla casella.

![configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_config.png){class="glboxshadow"}

### Client Options {#client-options}

Fai clic sull'icona dell'ingranaggio sulla destra per accedere alle opzioni del client OpenVPN o WireGuard.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options.png){class="glboxshadow"}

Le opzioni del client OpenVPN vengono mostrate come segue.

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_ovpn.png){class="glboxshadow"}

Le opzioni del client WireGuard vengono mostrate come segue.

![wg client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: se abilitato, sarà consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite VPN. Il server VPN deve pubblicizzare una route verso la subnet LAN di questo router.

    Ad esempio, come mostrato nel diagramma seguente, il router GL.iNet funziona come client VPN e si collega a un server VPN tramite il tunnel VPN. Quando questa opzione è abilitata, sia il router GL.iNet sia i dispositivi sul lato LAN possono essere raggiunti dai dispositivi sul lato del server VPN, ad esempio un NAS. Per farlo, devi aggiungere una regola di instradamento sul server VPN per raggiungere la subnet LAN del router GL.iNet.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni Site-to-Site in cui il peer remoto conosce le tue subnet LAN.

    Come mostrato di seguito, se il mascheramento IP è abilitato, quando il portatile (192.168.10.200) della LAN del router da viaggio invia traffico attraverso il tunnel al NAS di casa (192.168.8.100), il router da viaggio riscrive l'IP sorgente da `192.168.10.200` all'indirizzo del tunnel del client VPN `10.1.0.2`, quindi il lato server vede il traffico come proveniente dal client anziché dalla LAN locale del client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/ip_masquerading.png){class="glboxshadow"}

- **MTU**: abbreviazione di Maximum Transmission Unit. Questa impostazione facoltativa consente di personalizzare l'MTU del tunnel VPN, sovrascrivendo il valore definito nel file di configurazione.

### Proxy Mode {#proxy-mode}

La modalità proxy predefinita per la connessione VPN è **Global Proxy**. Puoi fare clic sulla casella in alto a destra per passare ad altre modalità proxy.

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_proxy.png){class="glboxshadow"}

Sono disponibili tre modalità proxy: **Global Proxy**, **Policy Mode** e **Route Mode**.

1. Global Proxy

    In questa modalità, tutto il traffico verrà instradato attraverso la VPN. Può essere attivata una sola istanza di client VPN.

2. Policy Mode

    Questa modalità può essere ulteriormente suddivisa in tre criteri.

    - Basata sul dominio di destinazione o sull'IP.

        In questa modalità, solo il traffico di determinati siti web identificati tramite indirizzo IP o nome di dominio verrà instradato tramite VPN. Può essere attivata una sola istanza di client VPN.

    - Basata sul dispositivo client.

        In questa modalità, solo il traffico di determinati dispositivi LAN identificati tramite indirizzo MAC verrà instradato tramite VPN. Può essere attivata una sola istanza di client VPN.

    - Basata sulla VLAN.

        In questa modalità, solo il traffico di determinate VLAN verrà instradato tramite VPN. Può essere attivata una sola istanza di client VPN.

3. Route Mode

    - Auto Detect

        Verranno utilizzate le regole di instradamento definite in ogni file di configurazione del client VPN oppure fornite dal server VPN.

    - Customize Routing Rules

        Puoi configurare manualmente le regole di instradamento per ciascuna istanza di client VPN.

### Global Options {#global-options}

Fai clic su **Global Options** nell'angolo in alto a destra per configurare le impostazioni avanzate del client VPN.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: se abilitato, tutto il traffico Internet è obbligato a passare esclusivamente attraverso il tunnel VPN e non può essere instradato tramite altre interfacce come la WAN locale dell'ISP. Se la connessione VPN cade inaspettatamente, tutto il traffico Internet viene completamente bloccato per impedire il ritorno alla WAN normale. Questo evita perdite VPN causate da guasti della VPN, impostazioni DNS errate del client e problemi simili.

    Questa funzione è nota anche come [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Impedisce che i dati dell'utente vengano esposti online. Un tipico Kill Switch interrompe automaticamente l'accesso a Internet quando la connessione VPN fallisce. La funzione Block Non-VPN Traffic sui router GL.iNet offre una protezione più ampia contro le perdite e copre i seguenti scenari:

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applicazioni avviate prima della connessione VPN

    6. Perdite di traffico per singola applicazione

- **Allow Access WAN**: se abilitato, i dispositivi client locali possono continuare ad accedere ai servizi sul lato WAN, ad esempio stampanti, NAS e altri dispositivi nella subnet a monte, mentre la VPN è attiva.

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Come mostrato nel diagramma sopra, abilitando questa funzione i dispositivi locali possono raggiungere gli host della subnet a monte, come stampanti e NAS.

    Questa opzione è pensata principalmente per consentire ai client di accedere ai dispositivi nella subnet a monte. Tuttavia, il router non può distinguere il traffico della subnet a monte dal normale traffico Internet. Se i dispositivi client accedono direttamente a risorse tramite IP pubblici, esiste un potenziale rischio di perdita di traffico. Per questo motivo, **Allow Access WAN** e **Block Non-VPN Traffic** si escludono a vicenda e non possono essere abilitati contemporaneamente.

- **Services From GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione è disabilitata per impostazione predefinita, poiché questi servizi richiedono normalmente il reale indirizzo IP del dispositivo per funzionare correttamente.

## VPN Server {#vpn-server}

Se il router non è mai stato configurato come server OpenVPN o WireGuard, la pagina apparirà come mostrato di seguito. Fai clic su **Set Up Now** e verrai indirizzato alla pagina **OpenVPN Server** oppure **WireGuard Server** per inizializzare il server VPN.

![vpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_setup.png){class="glboxshadow"}

Dopo che OpenVPN Server o WireGuard Server sono stati abilitati, la pagina mostrerà lo stato del server come segue.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_connected.png){class="glboxshadow"}

### Server Options {#server-options}

Fai clic sull'icona dell'ingranaggio sulla destra per accedere alle opzioni del server OpenVPN o WireGuard.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options.png){class="glboxshadow"}

Le opzioni del server OpenVPN vengono mostrate come segue.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_ovpn.png){class="glboxshadow"}

Le opzioni del server WireGuard vengono mostrate come segue.

![wg server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: se abilitato, le risorse all'interno della subnet LAN del server possono essere raggiunte attraverso il tunnel VPN.

* **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni Site-to-Site in cui il peer remoto conosce le tue subnet LAN.

    Come mostrato di seguito, se il mascheramento IP è abilitato, quando il NAS (192.168.8.100) della LAN di casa invia traffico attraverso il tunnel al portatile (192.168.10.200) della LAN del router da viaggio, il router di casa riscrive l'IP sorgente da `192.168.8.100` all'indirizzo del tunnel del server VPN `10.1.0.1`, quindi il lato remoto vede il traffico come proveniente dal server anziché dalla LAN locale del server.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/ip_masquerading.png){class="glboxshadow"}

* **MTU**: abbreviazione di Maximum Transmission Unit. Il valore MTU impostato per il tunnel sovrascriverà le impostazioni MTU nel file di configurazione.

* **Client to Client**: se abilitato, i client VPN collegati a questo server possono accedere tra loro tramite i rispettivi IP del tunnel VPN. Per consentire ai client di accedere anche alle sottoreti LAN reciproche, aggiungere sul server VPN regole di instradamento che pubblicizzino tali sottoreti LAN remote.

### Server Route Rule {#server-route-rule}

Fai clic sull'icona della route sulla destra per personalizzare, se necessario, le regole di instradamento di OpenVPN o WireGuard.

![server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule.png){class="glboxshadow"}

La schermata OpenVPN Server Route Rule viene mostrata come segue. Fai clic su **Add Route Rule**, inserisci **Target Address** e **Gateway**, quindi fai clic sull'icona verde di conferma per applicare.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

La schermata WireGuard Server Route Rule viene mostrata come segue. Fai clic su **Add Route Rule**, inserisci **Target Address** e **Gateway**, quindi fai clic sull'icona verde di conferma per applicare.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Nota**: le regole di routing del server consentono di definire voci di routing personalizzate sul server VPN, specificando indirizzo di destinazione, gateway e altri parametri per ogni regola. Le voci configurate manualmente hanno la precedenza sulle impostazioni di routing predefinite nel file di configurazione VPN e determinano quale traffico dei client viene instradato attraverso il tunnel cifrato.

### Global Options {#global-options_1}

Fai clic su **Global Options** nell'angolo in alto a destra per configurare le impostazioni avanzate del server VPN.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: se abilitato, quando questo router funziona contemporaneamente come server VPN e client VPN, il traffico dei client VPN remoti collegati al server VPN di questo router verrà instradato attraverso il tunnel VPN a monte che questo router usa come client VPN. [Scopri di più su VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
