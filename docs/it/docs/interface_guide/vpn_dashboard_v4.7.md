# VPN Dashboard (Firmware v4.7 e precedenti)

Accedi al pannello di amministrazione web e vai su **VPN** -> **VPN Dashboard**.

La pagina VPN Dashboard mostra lo stato della connessione VPN e le impostazioni. Sono presenti due sezioni: [VPN Client](#vpn-client) e [VPN Server](#vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

All'inizio non e' disponibile alcuna configurazione per OpenVPN e WireGuard. Fai clic su **Set Up Now** e verrai indirizzato rispettivamente alle pagine [OpenVPN Client](openvpn_client.md) e [WireGuard Client](wireguard_client.md).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

Una volta completata la configurazione, puoi selezionare il file di configurazione nella colonna Configuration file.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### Opzioni VPN Client

Fai clic sull'icona dell'ingranaggio di OpenVPN o WireGuard.

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

Opzioni del client OpenVPN.

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

Opzioni del client WireGuard.

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Se questa opzione e' abilitata, ai dispositivi collegati sotto il router e' consentito accedere alla LAN sul lato del VPN Server, il che richiede anche le impostazioni appropriate sul lato del VPN Server.

    Ad esempio, nell'immagine seguente, se questa opzione e' abilitata significa che *Your Device* puo' accedere al *NAS*, ma e' comunque necessario che il *VPN Server* ti consenta l'accesso al NAS all'interno della sua subnet.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* **IP Masquerading**

    Se questa opzione e' abilitata, quando i dispositivi client sulla LAN inviano i loro pacchetti IP, il router sostituisce l'indirizzo IP sorgente con il proprio indirizzo e poi lo inoltra nel tunnel VPN.

* **MTU**

    Significa maximum transmission unit. Il valore MTU impostato per l'istanza sovrascrivera' l'elemento MTU nel file di configurazione.

### Modalita' proxy

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

Come mostrato nella figura sopra, la modalita' proxy corrente e' Global Proxy. Fai clic su Global Proxy per passare alle altre modalita' proxy. Esistono 3 tipi: **Global Proxy**, **Policy Mode** e **Route Mode**.

1. Global Proxy

    Tutto il traffico passera' attraverso la VPN. Puo' essere attivata una sola istanza client VPN.

2. Policy Mode

    1. Basata sul dominio o IP di destinazione.

        In questa modalita', solo il traffico di determinati siti web definiti tramite indirizzo IP o nome di dominio passera' attraverso la VPN. Puo' essere attivata una sola istanza client VPN.

    2. Basata sul dispositivo client.

        In questa modalita', solo il traffico di determinati dispositivi client locali definiti tramite indirizzo MAC passera' attraverso la VPN. Puo' essere attivata una sola istanza client VPN.

    3. Basata sulla VLAN.

        In questa modalita', solo il traffico di determinate VLAN puo' passare attraverso la VPN. Puo' essere attivata una sola istanza client VPN.

3. Route Mode

    1. Auto detect

        Verranno usate le regole di instradamento definite in ciascun file di configurazione del client VPN oppure fornite dal server VPN.

    2. Customize routing rules

        Puoi configurare manualmente le regole di instradamento per ciascuna istanza client VPN.

### Opzioni globali di VPN Client

Facendo clic su **Global Options** comparira' una finestra di dialogo con le opzioni globali.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Block Non-VPN Traffic

    Se questa opzione e' abilitata, tutto il traffico dei dispositivi client che tenta di bypassare il tunnel VPN verra' bloccato, impedendo efficacemente perdite VPN causate da configurazioni DNS del client, cadute della connessione VPN, app client che richiedono direttamente per IP e cosi' via.

    Questa funzione e' nota anche come [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. E' progettata per impedire che i tuoi dati fuoriescano sul web. La maggior parte dei provider VPN offre una funzione Kill Switch che disconnette automaticamente computer, telefono o tablet da Internet se la connessione VPN cade. La funzione Block Non-VPN Traffic sui router GL.iNet copre ancora piu' scenari, inclusi i seguenti sei casi:

    1. DNS Leak
    2. IPv6 Leak
    3. WebRTC Leak
    4. Dropped VPN Connection
    5. Programs Started Before VPN
    6. Application Specific Leaks

2. Allow Access WAN

    Se questa opzione e' abilitata, mentre la VPN e' connessa, i dispositivi client potranno comunque accedere alla WAN, ad esempio per raggiungere stampanti, NAS e cosi' via nella subnet superiore.

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Come mostrato sopra, se questa funzione e' attiva, il tuo dispositivo potra' accedere ai dispositivi nella subnet a monte, come stampante e NAS.

    Lo scenario principale consiste nel consentire ai client l'accesso ai dispositivi nella subnet a monte, ma il router non ha modo di distinguere tra subnet a monte e Internet; quindi, se il traffico del dispositivo client viene raggiunto direttamente tramite IP, puo' esistere un rischio di perdita. Per questo motivo questa opzione e Block Non-VPN Traffic si escludono a vicenda.

3. Services From GL.iNet Use VPN

    Se questa opzione e' abilitata, i servizi sul router che normalmente richiedono l'uso di un IP reale useranno la VPN. Inclusi GoodCloud, DDNS e rtty. Rtty include **Remote SSH** e **Remote Web Access** nella [pagina GoodCloud](cloud.md#enable-goodcloud-on-router).

    Lo scopo principale e' usare VPN Client e [GoodCloud](cloud.md) / [DDNS](ddns.md) contemporaneamente. Si consiglia di disattivare questa opzione se vuoi usare GoodCloud, altrimenti la stabilita' di GoodCloud sara' influenzata dallo stato della VPN. Se vuoi usare DDNS, devi disattivare questa opzione, altrimenti DDNS puntera' all'indirizzo IP del VPN Server.

## VPN Server

All'inizio entrambi i VPN Server non sono ancora inizializzati. Fai clic su **Set Up Now** e verrai indirizzato rispettivamente alle pagine [OpenVPN Server](openvpn_server.md) e [WireGuard Server](wireguard_server.md).

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

Dopo l'avvio di OpenVPN Server e WireGuard Server.

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### Opzioni OpenVPN Server

Fai clic sull'icona dell'ingranaggio di OpenVPN server.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Se questa opzione e' abilitata, le risorse all'interno della subnet LAN possono essere accessibili tramite il tunnel VPN.

* **IP Masquerading**

    Se questa opzione e' abilitata, quando i dispositivi client sulla LAN inviano i loro pacchetti IP, il router sostituisce l'indirizzo IP sorgente con il proprio indirizzo e poi lo inoltra nel tunnel VPN.

* **MTU**

    Il valore MTU impostato per l'istanza sovrascrivera' l'elemento MTU nel file di configurazione.

### Regola di route di OpenVPN Server

Fai clic sull'icona di rete di OpenVPN server.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

In modalita' customize routes, il client VPN ignorera' il file di configurazione e la configurazione di instradamento fornita dal server. Se usare o meno il tunnel crittografato della VPN quando si accede a un determinato segmento di rete viene deciso dalle regole di routing impostate manualmente.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### Opzioni WireGuard Server

Fai clic sull'icona dell'ingranaggio di WireGuard server.

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Se questa opzione e' abilitata, le risorse all'interno della subnet LAN possono essere accessibili tramite il tunnel VPN.

* **IP Masquerading**

    Se questa opzione e' abilitata, quando i dispositivi client sulla LAN inviano i loro pacchetti IP, il router sostituisce l'indirizzo IP sorgente con il proprio indirizzo e poi lo inoltra nel tunnel VPN.

* **MTU**

    Il valore MTU impostato per l'istanza sovrascrivera' l'elemento MTU nel file di configurazione.

* **Client to Client**

    I client WireGuard possono accedere ai dati reciproci. Gli utenti possono accedere ai dispositivi della rete interna di casa o dell'ufficio da remoto e l'accesso ai dati tramite WireGuard server e' piu' sicuro del port forwarding grazie ai processi crittografati; inoltre, una volta connesso, il processo e' piu' stabile e veloce.

### Regola di route di WireGuard Server

Fai clic sull'icona di rete di WireGuard server.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

In modalita' customize routes, il client VPN ignorera' il file di configurazione e la configurazione di instradamento fornita dal server. Se usare o meno il tunnel crittografato della VPN quando si accede a un determinato segmento di rete viene deciso dalle regole di routing impostate manualmente.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### Opzioni globali di VPN Server

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPN Cascading**, se questa opzione e' abilitata, quando su questo router sono in esecuzione sia VPN server sia VPN Client, i client collegati al VPN server verranno ulteriormente instradati nel tunnel del VPN client. [Scopri di piu' su VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
