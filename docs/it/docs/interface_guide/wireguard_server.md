# Configurare WireGuard Server sui router GL.iNet

WireGuard® e' una VPN estremamente semplice, veloce e moderna che utilizza crittografia all'avanguardia. Punta a essere piu' veloce, piu' semplice, piu' leggera e piu' utile di IPSec, evitando al tempo stesso una complessita' eccessiva. In generale offre prestazioni nettamente migliori rispetto a OpenVPN.

Per configurare WireGuard server su un router GL.iNet, guarda questo video oppure segui i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Assicurati di avere un indirizzo IP pubblico {#make-sure-you-have-a-public-ip-address}

Fai clic [qui](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) per verificare se il tuo Internet Service Provider ti assegna un indirizzo IP pubblico.

**In caso contrario, il router non puo' essere configurato come WireGuard Server.**

Metodi alternativi:

1. Se hai un router principale, accedi ad esso e verifica se riceve un IP pubblico dal tuo ISP.
2. Chiedi al tuo ISP un indirizzo IP pubblico. Potrebbe essere previsto un costo aggiuntivo.
3. Se i due metodi precedenti non funzionano, ad esempio se la rete e' dietro CGNAT, puoi provare la nostra soluzione SD-WAN [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Verifica se e' necessario il Port Forwarding {#confirm-if-port-forwarding-is-required}

**Topologia di rete**

??? "GL.iNet e' il router principale"

    * Se il router GL.iNet e' il router principale della tua rete, non e' necessario configurare il port forwarding. Passa al [passaggio successivo](#set-up-wireguard-server).

??? "GL.iNet e' il router secondario"

    * Se e' gia' presente un router principale e il router GL.iNet e' configurato come router secondario, dovrai configurare il [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) sul router principale.

    * Se e' gia' presente un router principale e il router GL.iNet si trova diversi livelli sotto il router principale, configura il [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) su ciascun livello intermedio.

## Configurare WireGuard Server {#set-up-wireguard-server}

Accedi al pannello di amministrazione web e vai su **VPN** -> **WireGuard Server**.

1. Fai clic su **Generate Configuration** (solo per la configurazione iniziale del server VPN).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Controlla la configurazione.

    La configurazione predefinita funziona nella maggior parte dei casi, come mostrato di seguito. Non e' necessario modificare l'indirizzo IPv4 se non entra in conflitto con il gateway del router a monte.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    (IPv6 su GL.iNet e' disabilitato per impostazione predefinita. Se vuoi usare un indirizzo IPv6, abilita IPv6 sul router.)

    Se noti che l'indirizzo IPv4 entra in conflitto con il gateway del router a monte, modificalo con un altro, ad esempio **10.1.0.1/24**, quindi fai clic su **Apply**. Assicurati di includere la notazione CIDR "/24" per evitare problemi di connettivita'.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Ad esempio, se a monte di un router GL.iNet c'e' un router Xfinity, l'IP del router Xfinity potrebbe essere 10.0.0.1, entrando in conflitto con il Tunnel IP del WireGuard Server quando il router GL.iNet viene configurato come server WireGuard; in tal caso occorre apportare la modifica sopra indicata.

    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Aggiungi un profilo.

    Passa alla scheda **Profiles** e fai clic sul pulsante **Add** per generare un profilo per il tuo dispositivo.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    Imposta un nome descrittivo e fai clic su **Apply** per continuare.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Se devi impostare configurazioni avanzate, fai clic su **Set More**. Poi fai clic su **Apply** per continuare.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Aggiungi regole di route se necessario"

        Nella maggior parte dei casi non e' necessario aggiungere regole di route.

        Se vuoi accedere dal server ai dispositivi LAN del client WireGuard, passa alla scheda **Route Rules** nella pagina **WireGuard Server** per configurare le regole di route. Fai clic [qui](../tutorials/wireguard_server_access_to_client_lan_side.md) per ulteriori istruzioni.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        In caso contrario, passa al passaggio 4 per scaricare una configurazione client.

4. Scarica la configurazione.

    Dopo aver aggiunto un profilo e aver fatto clic su Apply, verra' generato un file di configurazione in tre formati: codice QR, testo semplice e file `.conf`. Scegli il metodo che preferisci per ottenere il file di configurazione.

    - **QR code**: adatto ai dispositivi terminali, ad esempio smartphone, tablet e laptop, con l'app WireGuard installata. Se vuoi configurare un determinato dispositivo come client WireGuard, apri semplicemente l'app WireGuard, scansiona il codice QR e la configurazione verra' importata automaticamente.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: nel formato testo semplice puoi controllare i dettagli della configurazione e copiarli/incollarli comodamente altrove per la configurazione manuale, ad esempio nell'app WireGuard o su un router GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: fai clic sul pulsante **Download** per salvare il file `.conf` sul tuo dispositivo locale. E' altrettanto pratico e puo' essere caricato direttamente nell'app WireGuard o in un router GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    Se necessario, puoi specificare l'indirizzo del server scegliendo tra IP pubblico, dominio DDNS e WAN IP corrente. Questa funzione e' disponibile dal firmware v4.8. Una volta modificata, anche l'indirizzo del server nel file di configurazione verra' aggiornato.

    Ad esempio, si consiglia di abilitare [DDNS](ddns.md) e usare il dominio DDNS come indirizzo del server se l'IP pubblico della tua rete cambia frequentemente.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Avvia WireGuard server.

    Fai clic sul pulsante **Start** in alto a destra per avviare WireGuard server.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    Lo stato della connessione verra' mostrato nella stessa pagina.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Verificare che WireGuard Server funzioni correttamente

### Verificare lo stato del server

Dal firmware v4.8 puoi controllare lo stato della connessione server nella pagina **WireGuard Server**.

Se vengono mostrate statistiche del traffico upload/download e dispositivi connessi online, significa che il server WireGuard e' in esecuzione e che ci sono client WireGuard collegati.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

Se vengono mostrati 0 traffico e 0 client, significa che non c'e' alcun client WireGuard connesso.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

Per il firmware v4.7 e precedenti, controlla lo stato della connessione server nella pagina **VPN Dashboard**.

### Verificare l'IP del client

Per verificare una connessione riuscita al server, importa la configurazione WireGuard precedentemente esportata su un dispositivo che si trovi in una rete diversa da quella locale del server. Poi apri un browser web e cerca il tuo indirizzo IP e la tua posizione. Se corrispondono all'IP del server VPN, invece che all'IP del tuo provider Internet, e alla relativa posizione, la connessione VPN e' riuscita.

Il metodo piu' semplice e' usare uno smartphone con l'[app WireGuard](https://www.wireguard.com/install){target="_blank"} ufficiale installata. Per prima cosa disattiva il Wi-Fi dello smartphone e collegati a Internet esclusivamente tramite rete cellulare 4G/5G. Poi apri l'app WireGuard, importa il file di configurazione e avvia la connessione. Verifica se lo smartphone riesce ad accedere a Internet e se il suo indirizzo IP corrisponde a quello del WireGuard Server.

Se la connessione fallisce, le cause piu' comuni sono:

* Il provider Internet non ti assegna un indirizzo IP pubblico. Controlla [qui](#make-sure-you-have-a-public-ip-address).
* Potrebbe essere necessario configurare il port forwarding. Controlla [qui](#confirm-if-port-forwarding-is-required).
* La porta usata da WireGuard Server e' bloccata dal tuo provider Internet. Cambia porta oppure contatta il provider per ulteriore assistenza.
* In alcuni paesi o regioni la connessione VPN potrebbe essere bloccata.

## Installazione dell'app WireGuard

Scarica l'app WireGuard dal [sito ufficiale di WireGuard](https://www.wireguard.com/install){target="_blank"}.

---

WireGuard® e' un marchio registrato di Jason A.Donenfeld.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
