# Crea il tuo server WireGuard domestico con due router GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Questo articolo spiega come configurare il router di casa come server VPN WireGuard e il router da viaggio come client VPN WireGuard, in modo da collegarli da remoto e poter usare l'indirizzo IP di casa tramite il router da viaggio ovunque ti trovi.

Guarda questo video oppure fai riferimento ai passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Questo video usa GL-MT5000 (Brume 3) e GL-MT3600BE (Beryl 7) per dimostrare la configurazione VPN.)</small>

Nei passaggi seguenti useremo come esempio GL-MT6000 (Flint 2) e GL-MT3000 (Beryl AX):

- GL-MT6000, router domestico, verrà configurato come server VPN WireGuard. Se non è necessaria la funzione wireless, puoi considerare anche il nostro security gateway GL-MT2500 o altri modelli.

- GL-MT3000, router da viaggio, verrà configurato come client VPN WireGuard per collegarsi da remoto al server VPN di casa.

## Perché creare il tuo server WireGuard domestico {#why-build-your-own-wireguard-home-server}

1. Usa l'indirizzo IP di casa come IP pubblico, così il traffico risulta provenire dalla tua rete domestica.
2. Evita i canoni mensili dei servizi VPN di terze parti.
3. Crittografa tutto il traffico Internet facendolo passare attraverso il tunnel verso la rete di casa per proteggere la tua privacy.
4. Accedi ai dispositivi di casa e ai servizi di streaming locali ovunque ti trovi.

## Preparazione {#preparations}

### Controlla se hai un IP pubblico {#check-if-you-have-a-public-ip}

Per prima cosa, assicurati che GL-MT6000 abbia un indirizzo IP pubblico sul lato WAN, in modo da poter essere raggiunto globalmente. In caso contrario, il router da viaggio non potrà stabilire una connessione VPN quando sei in viaggio.

Per verificare se hai un indirizzo IP pubblico, apri un browser web e digita [what is my ip](https://whatismyipaddress.com/){target="_blank"} nella barra degli indirizzi.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Verrà mostrato il tuo indirizzo IP pubblico. Se coincide con il WAN IP fornito dal tuo ISP a GL-MT6000, allora hai un IP pubblico.

Se non hai un IP pubblico, ecco alcuni metodi di riferimento.

1. Se hai un router principale, accedi a esso e controlla se riceve l'IP pubblico dal tuo ISP.
2. Chiedi al tuo ISP un indirizzo IP pubblico. Potrebbe essere previsto un costo aggiuntivo.
3. Se i due metodi precedenti non funzionano, ad esempio se la tua rete è dietro CGNAT, puoi provare la nostra soluzione SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

### Verifica se è necessario il Port Forwarding {#check-if-port-forwarding-is-required}

??? "GL.iNet come router principale"

    Se il router GL.iNet è collegato direttamente a un modem ISP tramite cavo Ethernet, allora il router GL.iNet è il router principale.

    **Come verificare se il router GL.iNet è collegato direttamente al modem ISP?**

    Accedi al pannello di amministrazione GL.iNet. Seleziona **INTERNET** nella barra laterale sinistra. Controlla la topologia e i dettagli della connessione.

    Se il router è collegato direttamente tramite Ethernet, vedrai la sezione **Ethernet** con dettagli come **Protocol**, **IP Address** e **Gateway**.

    Nell'immagine seguente, il campo **IP Address** evidenziato mostra l'indirizzo IP WAN assegnato dall'ISP al router GL.iNet.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    In questo esempio l'indirizzo IP WAN del router principale GL.iNet è pubblico, quindi **non è necessario configurare il port forwarding**.

    Configura il router GL.iNet come server WireGuard e il router da viaggio come client WireGuard. Quando il client si collega al server, si stabilisce un tunnel VPN tra i due router.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet come sub-router"

    Configura il **Port Forwarding** sul router principale per il router GL.iNet se quest'ultimo si trova dietro NAT.

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Esempio: un router TP-Link come router principale di casa.

    Collegati al Wi-Fi o alla LAN del router di casa. Poi accedi al pannello di amministrazione web. Controlla il WAN IP che riceve dal tuo ISP. Nell'immagine seguente puoi vedere che il tuo IP pubblico è **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Prima di configurare il port forwarding, consigliamo di riservare un indirizzo IP per il router GL.iNet sul router principale, così da assegnargli un IP fisso.** In caso contrario, al riavvio del router principale o del router GL.iNet, il router principale potrebbe assegnare un IP diverso al router GL.iNet, facendo fallire la regola di port forwarding.

    Poi configura il Port Forwarding sul router principale per il router GL.iNet.

    1. Vai su "Advanced", fai clic su "virtual Server", poi su "Add".

    2. Internal IP (Device IP): è l'indirizzo IP assegnato al router GL.iNet; puoi trovarlo nell'elenco client del TP-Link.

    3. External/Internal port: inserisci in entrambi i campi "51820".

    4. Protocol: puoi scegliere "All oppure UDP oppure TCP/UDP".

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Altri esempi di [Port Forward](how_to_set_up_port_forwarding.md)**

## Configurare il server WireGuard {#set-up-wireguard-server}

1. Accedi al pannello di amministrazione web e vai su **VPN** -> **WireGuard Server**. Fai clic su **Generate Configuration** (solo per la configurazione iniziale del server VPN).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Controlla la configurazione.

    La configurazione predefinita mostrata di seguito è adatta alla maggior parte dei casi.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address** indica l'indirizzo IP del tunnel del server WireGuard. Modificalo solo se è in conflitto con il gateway del router a monte.

        In tal caso, scegli un altro indirizzo, ad esempio **10.1.0.1/24**, quindi fai clic su **Apply**. Includi la notazione CIDR "/24" per evitare problemi di connettività.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Ad esempio, un router Xfinity a monte del router GL.iNet potrebbe usare l'indirizzo IP 10.0.0.1, che può entrare in conflitto con l'IP del tunnel di alcuni router GL.iNet configurati come server WireGuard. Se non c'è alcun conflitto, salta questo passaggio.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. IPv6 è disabilitato per impostazione predefinita sui router GL.iNet. Per usare un indirizzo IPv6, abilita [IPv6](../interface_guide/ipv6.md) sul router.

    - **Listen Port**. Per impostazione predefinita il server WireGuard è in ascolto sulla porta UDP `51820`. Se cambi la porta e usi il port forwarding, aggiorna la regola sul router a monte in modo che inoltri il traffico alla nuova porta di ascolto del server. Usa la porta esterna della regola di inoltro nel campo `Endpoint` di ogni profilo client. Se il server è raggiungibile direttamente, usa la sua porta di ascolto.

    - **Enable Obfuscation**. Se abiliti l'opzione, il server usa il protocollo di offuscamento AmneziaWG per mascherare il traffico VPN. Mantieni le impostazioni di offuscamento predefinite e modificale solo se conosci questi parametri. Consulta le guide seguenti.

        - [Offuscamento AmneziaWG sui router GL.iNet](../faq/amneziawg_obfuscation.md)
        - [Configurare l'offuscamento VPN sui router GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Aggiungi un profilo.

    Passa alla scheda **Profiles** e fai clic su **Add** per generare un profilo per il tuo dispositivo.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Assegna al profilo un nome descrittivo e fai clic su **Apply** per continuare.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Se devi modificare le impostazioni avanzate, fai clic su **Set More**. Poi fai clic su **Apply** per continuare.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Aggiungi regole di instradamento se necessario"

        Nella maggior parte dei casi non servono regole di instradamento.

        Se vuoi accedere dal server ai dispositivi nella LAN del client WireGuard, passa alla scheda **Route Rules** della pagina **WireGuard Server** e configura le regole di instradamento. Consulta [questa guida](../tutorials/wireguard_server_access_to_client_lan_side.md) per le istruzioni.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Se non ti serve accedere a questi dispositivi, passa al punto 4 per scaricare una configurazione client.

4. Scarica la configurazione.

    Dopo aver aggiunto il profilo e fatto clic su **Apply**, puoi ottenere la configurazione come codice QR, testo semplice o file scaricabile `.conf`.

    - **Codice QR**. Scansiona il codice nell'app WireGuard per importare un profilo WireGuard standard. Se hai abilitato l'offuscamento, usa l'app AmneziaWG o un altro client che supporti l'offuscamento AmneziaWG.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Testo semplice**. Puoi esaminare i dettagli della configurazione e copiarli per configurare manualmente l'app WireGuard o un router GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **File .conf**. Fai clic su **Download** per salvare il file .conf sul dispositivo. Puoi caricarlo direttamente nell'app WireGuard o su un router GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    A partire dal firmware v4.8 puoi scegliere, se necessario, l'indirizzo del server tra l'IP pubblico, il dominio DDNS e l'IP WAN corrente. Se cambi questa impostazione, il router aggiorna anche l'indirizzo del server nel file di configurazione.

    Ad esempio, se l'indirizzo IP pubblico della tua rete cambia spesso, abilita il [DDNS](../interface_guide/ddns.md) e usa il dominio DDNS come indirizzo del server.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Fai clic su **Start** nell'angolo superiore destro per avviare il server WireGuard. Lo stato della connessione compare nella stessa pagina.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Configurare il client WireGuard {#set-up-wireguard-client}

### Cambiare l'IP LAN {#change-the-lan-ip}

Poiché in questo tutorial usiamo GL-MT6000 e GL-MT3000 come esempio, e i loro IP LAN predefiniti sono entrambi **192.168.8.1**, dobbiamo cambiare uno dei due per evitare conflitti.

Ecco i passaggi per cambiare l'IP LAN di GL-MT3000, il client WireGuard.

Accedi al pannello di amministrazione web di GL-MT3000 e vai su **NETWORK** -> **LAN** per cambiare l'indirizzo IP LAN. Ad esempio, puoi passare dall'indirizzo predefinito 192.168.8.1 a `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Aggiungere la configurazione {#add-the-configuration}

Nel pannello di amministrazione web di GL-MT3000, vai su **VPN** -> **WireGuard Client** e fai clic su **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Crea un gruppo sulla sinistra e assegnagli un nome, poi seleziona il file di configurazione da caricare oppure trascinalo nella casella di caricamento sulla destra.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Dopo che il file ha superato la verifica, fai clic su **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Puoi anche fare clic su **Manually Add Configuration**, incollare il testo della configurazione e poi fare clic su **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Il file di configurazione verrà mostrato nella pagina WireGuard Client una volta caricato correttamente.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Avviare la connessione {#start-the-connection}

Fai clic sull'icona con tre puntini e poi su **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Attendi alcuni minuti. Una volta connesso correttamente, si accenderà un punto verde.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Vai su **VPN Dashboard** e vedrai che il client si sta collegando al server con l'IP pubblico di casa. La pagina può variare leggermente a seconda della versione firmware.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Accedi di nuovo al pannello di amministrazione web di GL-MT6000, il server WireGuard, vai su **VPN** -> **WireGuard Server** oppure su **VPN** -> **VPN Dashboard** se usi il firmware v4.7 o precedenti, e vedrai anche lo stato della connessione che indica che il client è connesso.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Pagina WireGuard Server nel firmware v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(Pagina VPN Dashboard nel firmware v4.7 e precedenti)</small>

## Prepararsi in anticipo alla risoluzione remota dei problemi VPN {#prep-for-remote-vpn-fixes-ahead}

Associa entrambi i router al tuo account GoodCloud prima del viaggio. Potrai così risolvere i problemi da remoto se la connessione VPN non funziona a causa della configurazione o di altri problemi di rete. L’accesso remoto funziona solo se i router rimangono accesi e connessi a Internet.

---

Articoli correlati

- [Configurare il server WireGuard sui router GL.iNet](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
