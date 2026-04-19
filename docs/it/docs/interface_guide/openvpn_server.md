# Configurare OpenVPN Server sui router GL.iNet

OpenVPN e' un protocollo VPN open-source che usa tecniche di rete privata virtuale per stabilire connessioni sicure site-to-site o point-to-point.

Per configurare OpenVPN server su un router GL.iNet, guarda questo video oppure segui i passaggi qui sotto.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Assicurati di avere un indirizzo IP pubblico {#make-sure-you-have-a-public-ip-address}

Fai clic [qui](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) per verificare se il tuo Internet Service Provider ti assegna un indirizzo IP pubblico.

**In caso contrario, il router non puo' essere impostato come OpenVPN Server.**

Metodi alternativi:

1. Se hai un router principale, accedi e verifica se riceve un IP pubblico dal tuo ISP.
2. Chiedi al tuo ISP un indirizzo IP pubblico. Potrebbe comportare un costo aggiuntivo.
3. Se i due metodi sopra non funzionano, ad esempio se la tua rete e' dietro CGNAT, puoi provare la nostra soluzione SD-WAN [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Verifica se e' necessario il Port Forwarding {#confirm-if-port-forwarding-is-required}

**Topologia di rete**

??? "GL.iNet e' il router principale"

    * Se il router GL.iNet e' il router principale della tua rete, non e' necessario alcun port forwarding. Passa al [passaggio successivo](#set-up-openvpn-server).

??? " GL.iNet e' il router secondario"

    * Se e' gia' in uso un router principale e il router GL.iNet e' configurato come router secondario, dovrai configurare il [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) sul router principale.

    * Se e' gia' in uso un router principale e il router GL.iNet si trova a piu' livelli sotto il router principale, configura il [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) su ogni livello intermedio.

## Configurare OpenVPN Server {#set-up-openvpn-server}

Accedi al pannello di amministrazione web e vai su **VPN** -> **OpenVPN Server**.

1. Fai clic su **Generate Configuration** solo per la configurazione iniziale del server VPN.

    ![ovpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_generate_config.png){class="glboxshadow"}

2. Applica la configurazione.

    La configurazione predefinita funziona nella maggior parte dei casi.

    Se non hai bisogno di modificarla, fai clic su **Export Client Configuration** in basso e passa al passaggio 3.

    Se hai modificato la configurazione, fai clic su **Apply** prima di esportare la configurazione client.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S oppure Tun. Fai clic [qui](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md/#tap-s2s-vs-tun-mode) per vedere le differenze.

    * **Protocol:** UDP oppure TCP. Fai clic [qui](../faq/openvpn_tcp_udp.md) per vedere le differenze.

    * **Authentication Mode:** determina il metodo di autenticazione usato quando il client si collega al server. Sono disponibili tre opzioni.

        - **Certificate Only**: se selezionato, il router generera' automaticamente le chiavi del certificato server e client e le incorporera' nel file di configurazione client. Quando carichi la configurazione sul client, non saranno necessarie credenziali aggiuntive.

        - **Username/Password Only**: se selezionato, il router generera' una configurazione client senza chiavi di certificato. Devi prima aggiungere username e password nella scheda Users prima di esportare la configurazione client. Quando carichi la configurazione sul client, dovrai inserire queste credenziali per l'autenticazione.

        - **Username/Password and Certificate**: se selezionato, devi prima aggiungere username e password nella scheda Users prima di esportare la configurazione client; inoltre, il router generera' automaticamente le chiavi del certificato server e client e le incorporera' nel file di configurazione. Quando carichi la configurazione sul client, verra' prima verificato il certificato, seguito dall'autenticazione username/password per una sicurezza a due fattori.

        Ecco un esempio di creazione di un utente.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: se necessario, puoi modificare ulteriori impostazioni del server.

        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Esporta la configurazione client.

    Fai clic su **Export Client Configuration** in fondo alla scheda Configuration, oppure applica prima la configurazione modificata, quindi comparira' una finestra come mostrato di seguito.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_export_configuration.png){class="glboxshadow"}

    - Se l'IP pubblico della tua rete cambia spesso, puoi abilitare [DDNS](ddns.md) per usare il dominio DDNS come indirizzo del server.

    - Dal firmware v4.8 puoi specificare l'indirizzo del server scegliendo tra IP pubblico, dominio DDNS e IP WAN corrente. Una volta modificato, l'indirizzo del server nel file di configurazione verra' aggiornato contemporaneamente.

    Poi fai clic su **Download** per esportare la configurazione.

4. Avvia OpenVPN server.

    Fai clic sul pulsante **Start** nell'angolo superiore destro della pagina OpenVPN Server per avviare il server. Poi vai alla pagina VPN Dashboard per verificarne lo stato e le altre impostazioni.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Verificare se OpenVPN Server funziona correttamente

### Verificare lo stato del server

Dal firmware v4.8 puoi controllare lo stato della connessione server nella pagina **OpenVPN Server**.

Se vengono mostrate le statistiche di traffico upload/download, significa che OpenVPN server e' in esecuzione.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

Per il firmware v4.7 e precedenti, controlla lo stato della connessione server nella pagina **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

### Verificare l'IP del client

Per verificare che la connessione al server sia riuscita: importa la configurazione OpenVPN precedentemente esportata su un dispositivo che si trovi in una rete diversa, non la stessa rete locale del server. Poi apri un browser web e cerca il tuo indirizzo IP e la tua posizione. Se corrispondono all'IP del server VPN, anziche' a quello del provider Internet, e alla sua posizione, allora la connessione VPN e' riuscita.

Il metodo piu' semplice e' usare uno smartphone con l'[app OpenVPN ufficiale](https://openvpn.net/vpn-client/){target="_blank"} installata. Per prima cosa, disattiva il Wi-Fi dello smartphone e collega il telefono a Internet solo tramite dati cellulari, 4G o 5G. Poi apri l'app OpenVPN, importa il file di configurazione e avvia la connessione. Verifica se lo smartphone puo' accedere a Internet e se il suo indirizzo IP corrisponde a quello di OpenVPN Server.

Quando importi il file di configurazione nell'app OpenVPN, potrebbe comparire un promemoria come mostrato di seguito. Fai clic su **CONTINUE** per procedere, poiche' il certificato e' gia' incorporato nel file di configurazione.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Se la connessione non riesce, esistono diverse cause comuni:

* Il provider Internet non ti assegna un indirizzo IP pubblico. Verifica [qui](#make-sure-you-have-a-public-ip-address).
* Potrebbe essere necessario configurare il port forwarding. Verifica [qui](#confirm-if-port-forwarding-is-required).
* La porta usata per OpenVPN Server e' bloccata dal tuo provider Internet. Cambia porta oppure contatta il provider per ulteriore assistenza.
* Alcuni paesi o regioni potrebbero bloccare la connessione VPN.

## Accesso client-to-client

**Topologia di rete**

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Abilita l'opzione client to client ed esporta una nuova configurazione verso i client; in questo modo i client potranno accedere l'uno all'altro.

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## Installazione dell'app OpenVPN

Scarica l'app OpenVPN dal [sito ufficiale OpenVPN](https://openvpn.net/vpn-client/){target="_blank"}.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
