# Tailscale

Tailscale e' un servizio VPN che rende i dispositivi e le applicazioni di tua proprieta' accessibili ovunque nel mondo, in modo sicuro e semplice. Per maggiori informazioni su Tailscale, visita il [sito ufficiale Tailscale](https://tailscale.com/).

La funzione Tailscale sui router GL.iNet, disponibile dal firmware v4.2, consente al router di unirsi a una rete virtuale Tailscale. Una volta connesso, potrai accedere al router da remoto, incluse le sue risorse WAN e LAN.

**Nota**:

1. Poiche' Tailscale si basa su WireGuard, non e' consigliabile usare Tailscale contemporaneamente a una delle seguenti funzioni o servizi, perche' cio' potrebbe causare conflitti di routing: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, AstroWarp.

2. Questa funzione e' attualmente in beta e potrebbe contenere alcuni bug.

3. Alcuni modelli, pur eseguendo il firmware v4.2 o versioni successive, non supportano Tailscale a causa della memoria insufficiente.

## Modelli supportati

??? "Modelli supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Modelli non supportati"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Configurare la rete Tailscale

Di seguito un esempio con GL-MT2500.

1. Associa i tuoi dispositivi.

    Registra prima un account Tailscale, poi associa uno o due dispositivi, ad esempio smartphone o laptop, al tuo account Tailscale per fare dei test.

    Dopo l'associazione, potrai vedere i dispositivi e il relativo stato nella console Tailscale Admin.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Abilita Tailscale sul router GL.iNet.

    Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Attiva Tailscale e poi fai clic su **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Dopo poco tempo, l'interfaccia mostrera' un **Device Bind Link**. Fai clic sul Device Bind Link.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    Nella finestra pop-up verra' mostrato un link Tailscale. Fai clic sul link per essere reindirizzato al sito Tailscale ed effettuare il login.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Una volta effettuato il login, ti verra' chiesto di confermare il dispositivo che vuoi collegare. Fai clic su **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Quando la connessione riesce, verrai reindirizzato automaticamente alla console Tailscale Admin. Potrai vedere che l'indirizzo IP del GL-MT2500 e' `100.88.54.21`. Ora puoi usare questo IP per accedere al router.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Testa la connettivita'.

    Sui dispositivi collegati alla stessa rete Tailscale, puoi testare la connettivita' nei tre modi seguenti.

    * Usa il comando ping

        ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

    * Accedi al router tramite SSH

        ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

    * Accedi al pannello di amministrazione web

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Allow Remote Access WAN

Se questa opzione e' abilitata, le risorse sul lato WAN del dispositivo possono essere accessibili tramite la rete virtuale Tailscale.

Ad esempio, come mostrato nella topologia seguente, se questa funzione e' abilitata, puoi accedere al `GL-AXT1800` tramite il suo indirizzo IP, `192.168.29.1`, da `leo-phone`. Questo perche' GL-AXT1800 e' il dispositivo di livello superiore del `GL-MT2500` e quest'ultimo e' collegato alla stessa rete Tailscale di leo-phone.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

I passaggi operativi sono i seguenti.

1. Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **Tailscale**.

    Abilita **Allow Remote Access WAN** e fai clic su **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Vai alla console Tailscale Admin; verra' mostrato un avviso che indica che GL-MT2500 ha subnet.

    Fai clic sull'icona con i tre puntini a destra di GL-MT2500 e seleziona **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Abilita le subnet routes.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Ora puoi accedere a GL-AXT1800 tramite il suo indirizzo IP, `192.168.29.1`, da altri dispositivi. In realta', puoi accedere a tutti i dispositivi all'interno della subnet `192.168.29.0/24`.

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN

Se questa opzione e' abilitata, le risorse sul lato LAN del dispositivo possono essere accessibili tramite la rete virtuale Tailscale.

Ad esempio, come mostrato nella topologia seguente, se questa funzione e' abilitata, puoi accedere via SSH a `Ubuntu` tramite il suo indirizzo IP, `192.168.8.110`, da `leo-phone`. Questo perche' `Ubuntu` e' il dispositivo di livello inferiore del `GL-MT2500` e quest'ultimo e' collegato alla stessa rete Tailscale di leo-phone.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

I passaggi operativi sono i seguenti.

1. Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **Tailscale**.

    Abilita **Allow Remote Access LAN** e fai clic su **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Vai alla console Tailscale Admin; verra' mostrato un avviso che indica che GL-MT2500 ha subnet.

    Fai clic sull'icona con i tre puntini a destra di GL-MT2500 e seleziona **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Abilita le subnet routes.

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Ora puoi usare ping o accedere via SSH a Ubuntu tramite il suo indirizzo IP, `192.168.8.110`, da altri dispositivi. In realta', puoi accedere a tutti i dispositivi all'interno della subnet `192.168.8.0/24`.

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Custom Exit Nodes

Per impostazione predefinita, Tailscale agisce come rete overlay: instrada solo il traffico tra dispositivi che eseguono Tailscale e non elabora il traffico Internet pubblico, ad esempio quando navighi su siti come Google.

Tuttavia, potresti voler fare in modo che Tailscale instradi il traffico Internet pubblico. Ad esempio, quando sei fuori casa o in viaggio all'estero, se hai bisogno di accedere a servizi online, come il banking, disponibili solo nel tuo paese di origine, puoi impostare il tuo desktop di casa con IP pubblico come Exit node e configurare altri dispositivi nella stessa Tailnet, ad esempio GL-AXT1800 e GL-MT3000 mostrati nell'immagine seguente, in modo che inviino il loro traffico attraverso di esso. In questo modo tutto il traffico Internet pubblico verra' inoltrato tramite l'Exit Node.

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Quando tutto il traffico viene instradato tramite un Exit Node, di fatto stai usando le route predefinite, `0.0.0.0/0` e `::/0`, in modo simile a una normale connessione VPN.

In sintesi, un Exit node instrada il traffico Internet in uscita dei dispositivi della tua Tailnet, agendo di fatto come un server VPN. Quando sei connesso a un Exit node, tutto il tuo traffico Internet non Tailscale risulta provenire dalla sua posizione, aiutandoti ad accedere a contenuti con restrizioni geografiche e a migliorare la privacy online. Il dispositivo che si occupa di questo inoltro del traffico viene definito "exit node".

**Nota**: se il server DNS del router usa un indirizzo IP privato accessibile solo all'interno della rete locale, potresti perdere la connettivita' Internet quando usi un exit node. Per risolvere, accedi al router, vai su **NETWORK** -> **DNS** e imposta manualmente un server DNS pubblico come 8.8.8.8.

---

Nell'esempio seguente, un router GL.iNet **GL-MT2500** e **Leo-Desktop** si trovano nella stessa Tailnet. Di seguito i passaggi per impostare Leo-Desktop come Exit Node.

1. Abilita le subnet routes di GL-MT2500 nella console Tailscale Admin.

    Vai alla console Tailscale Admin, fai clic sull'icona con i tre puntini a destra di GL-MT2500 e seleziona **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    Nella finestra pop-up abilita le subnet routes.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Sul dispositivo che vuoi usare come exit node, ad esempio Leo-Desktop in questo esempio, seleziona **Run exit node**. Di seguito un esempio su Windows.

    ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Poi fai clic su **Yes**.

    ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. Nella console Tailscale Admin, imposta Leo-Desktop come Exit node.

    ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Accedi al pannello di amministrazione web di GL-MT2500, vai su **APPLICATIONS** -> **Tailscale** e abilita **Custom Exit Nodes**. Fai clic sul pulsante di aggiornamento, seleziona l'indirizzo IP di Leo-Desktop dal menu a discesa, quindi fai clic su **Apply**.

    ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    I dispositivi collegati al router instraderanno quindi il loro traffico tramite l'Exit Node per accedere a Internet e tutto il tuo traffico Internet sembrera' provenire dalla posizione dell'Exit Node.

Riferimenti: [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
