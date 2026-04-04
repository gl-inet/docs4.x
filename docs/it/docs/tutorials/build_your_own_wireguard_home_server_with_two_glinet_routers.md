# Crea il tuo server WireGuard domestico con due router GL.iNet

Questo articolo spiega come configurare il router di casa come server VPN WireGuard e il router da viaggio come client VPN WireGuard, in modo da collegarli da remoto e poter usare l'indirizzo IP di casa tramite il router da viaggio ovunque ti trovi.

Guarda questo video oppure fai riferimento ai passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Questo video usa GL-MT5000 (Brume 3) e GL-MT3600BE (Beryl 7) per dimostrare la configurazione VPN.)</small>

Nei passaggi seguenti useremo come esempio GL-MT6000 (Flint 2) e GL-MT3000 (Beryl AX):

- GL-MT6000, router domestico, verra' configurato come server VPN WireGuard. Se non e' necessaria la funzione wireless, puoi considerare anche il nostro security gateway GL-MT2500 o altri modelli.

- GL-MT3000, router da viaggio, verra' configurato come client VPN WireGuard per collegarsi da remoto al server VPN di casa.

## Perche' creare il tuo server WireGuard domestico

1. Usa l'indirizzo IP di casa come indirizzo Internet, come se fossi a casa.
2. Nessun canone mensile rispetto ai servizi VPN di terze parti.
3. Instrada tutto il traffico Internet verso la rete di casa tramite un tunnel VPN crittografato e proteggi la tua privacy.
4. Accesso semplice alle risorse interne e allo streaming locale.

## Preparazione

### Controlla se hai un IP pubblico

Per prima cosa, assicurati che GL-MT6000 abbia un indirizzo IP pubblico sul lato WAN, in modo da poter essere raggiunto globalmente. In caso contrario, il router da viaggio non potra' stabilire una connessione VPN quando sei in viaggio.

Per verificare se hai un indirizzo IP pubblico, apri un browser web e digita [what is my ip](https://whatismyipaddress.com/){target="_blank"} nella barra degli indirizzi.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Verrà mostrato il tuo indirizzo IP pubblico. Se coincide con il WAN IP fornito dal tuo ISP a GL-MT6000, allora hai un IP pubblico.

Se non hai un IP pubblico, ecco alcuni metodi di riferimento.

1. Se hai un router principale, accedi a esso e controlla se riceve l'IP pubblico dal tuo ISP.
2. Chiedi al tuo ISP un indirizzo IP pubblico. Potrebbe essere previsto un costo aggiuntivo.
3. Se i due metodi precedenti non funzionano, ad esempio se sei dietro CGNAT, puoi usare un metodo reverse proxy come [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md). In alternativa puoi provare una soluzione SD-WAN, [AstroWarp](https://www.astrowarp.net/).

### Verifica se e' necessario il Port Forwarding

??? "GL.iNet come router principale"

    Se il router GL.iNet e' collegato direttamente a un modem ISP tramite cavo Ethernet, allora il router GL.iNet e' il router principale.

    **Come verificare se il router GL.iNet e' collegato direttamente al modem ISP?**

    Passaggi:

    1. Accedi al pannello di amministrazione GL.iNet.

    2. Seleziona INTERNET nella barra laterale sinistra. Controlla topologia e dettagli della connessione:

        Se e' collegato direttamente tramite Ethernet, vedrai una sezione chiamata "Ethernet" con dettagli come Protocol, IP address, Gateway e cosi' via.

        Nell'immagine seguente, l'IP Address evidenziato e' il WAN IP fornito dall'ISP a questo router GL.iNet.

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Questo WAN IP e' un indirizzo IP pubblico, quindi questo router GL.iNet, che funge da router principale, ha un IP pubblico e **non e' necessario configurare il Port Forwarding**.

        Devi solo configurare questo router GL.iNet come server WireGuard e un router da viaggio come client WireGuard che si connetta al server. In questo modo verra' creato un tunnel VPN tra i due.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet come sub-router"

    Configura il **Port Forwarding** sul router principale per il router GL.iNet se quest'ultimo si trova dietro NAT.

    Topologia

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Esempio: un router TP-Link come router principale di casa.

    Collegati al Wi-Fi o alla LAN del router di casa. Poi accedi al pannello di amministrazione web. Controlla il WAN IP che riceve dal tuo ISP. Nell'immagine seguente puoi vedere che il tuo IP pubblico e' **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Prima di configurare il port forwarding, consigliamo di riservare un indirizzo IP per il router GL.iNet sul router principale, cosi' da assegnargli un IP fisso.** In caso contrario, al riavvio del router principale o del router GL.iNet, il router principale potrebbe assegnare un IP diverso al router GL.iNet, facendo fallire la regola di port forwarding.

    Poi configura il Port Forwarding sul router principale per il router GL.iNet.

    1. Vai su "Advanced", fai clic su "virtual Server", poi su "Add".

    2. Internal IP (Device IP): e' l'indirizzo IP assegnato al router GL.iNet; puoi trovarlo nell'elenco client del TP-Link.

    3. External/Internal port: inserisci in entrambi i campi "51820".

    4. Protocol: puoi scegliere "All oppure UDP oppure TCP/UDP".

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Altri esempi di [Port Forward](how_to_set_up_port_forwarding.md)**

## Configurare WireGuard server

### Abilitare DDNS (opzionale)

Abilita la funzione DDNS se non hai un IP pubblico statico ma solo un IP pubblico dinamico.

Accedi al pannello di amministrazione web di GL-MT6000 e vai su **APPLICATIONS** -> **Dynamic DNS**. Attiva l'interruttore **Enable DDNS**.

Seleziona la casella **Terms of Service & Privacy Policy** e fai clic su **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Poi vai su **WireGuard Server** -> scheda Configuration, assicurati che la Listen Port sia 51820, quindi fai clic su **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Generare la configurazione

Nella stessa pagina, fai clic sulla scheda **Profiles** accanto alla scheda Configuration, poi fai clic su **Add** (contrassegnato come 1 nell'immagine seguente).

Verra' generata automaticamente una configurazione client. Fai clic sull'**icona forward** (contrassegnata come 2).

Nella finestra pop-up, scorri per abilitare **DDNS Domain** (contrassegnato come 3; e' opzionale e va abilitato solo se hai un IP pubblico dinamico).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Puoi quindi scansionare il QR con l'[app mobile](https://www.wireguard.com/install/) WireGuard per testare il server. Per i dettagli fai clic [qui](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly).

In alternativa, puoi esportare una configurazione in formato testo per la connessione del client VPN.

Passa dalla configurazione QR code al formato testo facendo clic sulla scheda **Configuration File**.

Copia il testo per il client oppure fai clic sul pulsante Download e salvalo per usarlo in seguito.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Configurare WireGuard Client

### Cambiare l'IP LAN

Poiche' in questo tutorial usiamo GL-MT6000 e GL-MT3000 come esempio, e i loro IP LAN predefiniti sono entrambi **192.168.8.1**, dobbiamo cambiare uno dei due per evitare conflitti.

Ecco i passaggi per cambiare l'IP LAN di GL-MT3000, il client WireGuard.

Accedi al pannello di amministrazione web di GL-MT3000, poi vai su **NETWORK** nella barra laterale sinistra -> **LAN** per cambiare l'IP LAN. Ad esempio, puoi cambiare l'IP LAN dal valore predefinito 192.168.8.1 a `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Per maggiori dettagli sull'interfaccia LAN, fai clic [qui](../interface_guide/lan.md).

### Aggiungere la configurazione

Nel pannello di amministrazione web di GL-MT3000, vai su **VPN** -> **WireGuard Client** e fai clic su **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Crea un gruppo sulla sinistra e assegnagli un nome, poi seleziona il file di configurazione da caricare oppure trascinalo nella casella di caricamento sulla destra.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Dopo che il file ha superato la verifica, fai clic su **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Puoi anche fare clic su **Manually Add Configuration**, incollare il testo della configurazione e poi fare clic su **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Il file di configurazione verra' mostrato nella pagina WireGuard Client una volta caricato correttamente.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Avviare la connessione

Fai clic sull'icona con tre puntini e poi su **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Attendi alcuni minuti. Una volta connesso correttamente, si accendera' un punto verde.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Vai su **VPN Dashboard** e vedrai che il client si sta collegando al server con l'IP pubblico di casa. La pagina puo' variare leggermente a seconda della versione firmware.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Accedi di nuovo al pannello di amministrazione web di GL-MT6000, il server WireGuard, vai su **VPN** -> **WireGuard Server** oppure su **VPN** -> **VPN Dashboard** se usi il firmware v4.7 o precedenti, e vedrai anche lo stato della connessione che indica che il client e' connesso.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Pagina WireGuard Server nel firmware v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(Pagina VPN Dashboard nel firmware v4.7 e precedenti)</small>

## Prepararsi in anticipo alla risoluzione remota dei problemi VPN

In caso di problemi imprevisti durante il viaggio, associa in anticipo entrambi i router al tuo account GoodCloud per il troubleshooting remoto della VPN.

Talvolta il server puo' non essere disponibile a causa di un'interruzione di corrente o di altri motivi. Per mantenere accessibile il tuo server, collegalo a GL.iNet GoodCloud.

---

Articoli correlati

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
