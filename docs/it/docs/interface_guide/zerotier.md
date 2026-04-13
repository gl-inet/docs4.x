# ZeroTier

ZeroTier e' una rete privata virtuale, VPN, software-based che consente comunicazioni sicure e crittografate tra dispositivi tramite Internet. Crea una rete privata virtuale che permette ai dispositivi di comunicare come se si trovassero sulla stessa rete locale, indipendentemente dalla loro posizione fisica o dalla topologia di rete. ZeroTier e' progettato per essere semplice da configurare e utilizzare e offre funzioni come crittografia end-to-end, segmentazione della rete e bridging.

La funzione ZeroTier sui router GL.iNet, disponibile dal firmware v4.2, consente al router di unirsi a una rete virtuale ZeroTier. Una volta connesso, puoi accedere al router da remoto, comprese le sue risorse WAN e LAN.

**Nota**:

1. Non e' consigliabile usare ZeroTier contemporaneamente a una delle seguenti funzioni o servizi, poiche' potrebbero verificarsi conflitti di routing: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale, AstroWarp.

2. Questa funzione e' attualmente in beta e potrebbe contenere alcuni bug.

## Modelli supportati

??? "Modelli supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
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
    - GL-X2000 (Spitz Plus)
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

## Configurare una rete ZeroTier

Sono disponibili due versioni di ZeroTier Central: New Central e Legacy Central.

- **New Central**: una versione piu' recente di ZeroTier Central, con migliore usabilita' e nuove funzioni. E' consigliata ai nuovi utenti per ottenere l'esperienza migliore e gli strumenti piu' recenti.

- **Legacy Central**: per gli account creati prima di novembre 2025. Legacy Central continua a supportare gli utenti esistenti nella gestione delle loro reti.

Entrambe le versioni possono essere usate in parallelo, ma al momento non esiste un percorso di migrazione diretto.

Seleziona la versione appropriata per proseguire.

### New Central

Di seguito trovi un esempio con GL-MT3600BE.

1. Visita il [sito ufficiale di ZeroTier](https://www.zerotier.com/){target="_blank"} ed effettua l'accesso con il tuo account.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Crea un'organizzazione.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Seleziona un piano. Qui scegliamo come esempio il piano Personal, che include 10 dispositivi, 1 amministratore di rete e 1 rete. Se devi creare piu' reti, aggiungere piu' dispositivi o aggiungere route personalizzate e DNS, scegli il piano Essential o Scale.

    ![select plan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Ora la tua rete ZeroTier e' stata creata. Prendi nota del **Network ID**, una combinazione alfanumerica di 16 caratteri in alto a destra, perche' ti servira' quando collegherai altri dispositivi in seguito.

    ![network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Abilita ZeroTier sul router GL.iNet.

    Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **ZeroTier**.

    Abilita ZeroTier, inserisci il Network ID nella stessa pagina e fai clic su **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    Dopo poco tempo, l'interfaccia indichera' che e' richiesta l'autorizzazione. Fai clic sul collegamento **ZeroTier Central** per essere reindirizzato a ZeroTier Central.

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Autorizza il tuo dispositivo su ZeroTier Central.

    In ZeroTier Central, individua il dispositivo Pending e autorizzalo.

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Una volta autorizzato, la pagina verra' mostrata come segue.

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Aggiungi un altro dispositivo, ad esempio un computer o uno smartphone, alla stessa rete ZeroTier seguendo [questa guida](https://docs.zerotier.com/platforms/){target="_blank"}.

    Di seguito trovi un esempio con un laptop Windows 10 Pro.

    1. Installa ZeroTier sul laptop da [qui](https://www.zerotier.com/download/){target="_blank"}.

    2. Avvia ZeroTier. L'icona di ZeroTier apparira' nell'area di notifica in basso a destra sul desktop.

    3. Fai clic con il pulsante destro sull'icona, seleziona **Join New Network** e inserisci il **Network ID** ottenuto al passaggio 4 nella finestra pop-up.

        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Poi vai su ZeroTier Central, individua il dispositivo Pending e autorizzalo.

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Una volta autorizzato, la pagina verra' mostrata come segue. Vedrai i dettagli dei dispositivi membri, come **Device ID**, **Name**, **Status**, **Managed IP** e **Public IP**.

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Suggerimento**: puoi fare clic sull'icona con tre puntini sulla destra per modificare le impostazioni del dispositivo membro, inclusi nome del dispositivo, Managed IP e impostazioni avanzate.

8. Fai clic sul **Managed IP** del router per copiarlo. Potrai quindi usare questo Managed IP per accedere al router dal tuo laptop che si trova nella stessa rete ZeroTier.

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Testa la connettivita'.

    Sul laptop connesso alla stessa rete ZeroTier, apri un browser web e inserisci il Managed IP del router ottenuto al passaggio precedente.

    Se riesci ad accedere al pannello di amministrazione web del router, la connessione ZeroTier e' riuscita.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Puoi anche eseguire `ping` verso il Managed IP del router dal tuo laptop per verificare la connettivita'. Se ricevi una risposta corretta, la connessione ZeroTier e' stata stabilita con successo.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central

Di seguito trovi un esempio con GL-MT2500.

1. Crea la tua prima rete ZeroTier.

    Fai riferimento alla [Getting Started Guide](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"} ufficiale di ZeroTier per creare un account ZeroTier e una rete. Ricorda di annotare il Network ID, una combinazione alfanumerica di 16 caratteri, perche' ti servira' quando collegherai altri dispositivi in seguito.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Abilita ZeroTier sul router GL.iNet.

    Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **ZeroTier**.

    Abilita ZeroTier, inserisci il Network ID nella stessa pagina e fai clic su **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    Dopo poco tempo, l'interfaccia indichera' che e' richiesta l'autorizzazione.

    Fai clic sul collegamento **ZeroTier Central** per essere reindirizzato a ZeroTier Central.

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

3. Autorizza il tuo dispositivo su ZeroTier Central.

    In ZeroTier Central, vai alla sezione **Members**. Individua il nuovo dispositivo e fai clic sulla casella **Auth** per autorizzarlo. Se lo desideri, puoi anche personalizzare il nome del dispositivo.

    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Dopo poco tempo, ZeroTier assegnera' al dispositivo un **Managed IP**. Prendi nota di questo indirizzo IP, perche' verra' usato nel passaggio di test.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

4. Aggiungi un altro dispositivo, ad esempio un computer o uno smartphone, alla stessa rete ZeroTier seguendo [questa guida](https://docs.zerotier.com/platforms/){target="_blank"}.

5. Testa la connettivita'.

    Su un altro dispositivo collegato alla stessa rete ZeroTier, apri un browser web e inserisci il ZeroTier Managed IP del router ottenuto al passaggio precedente.

    Potrai accedere al pannello di amministrazione web del router.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

    Puoi anche usare il comando `ping` per verificare la connettivita'. Fai riferimento alla [Quickstart Guide](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"} di ZeroTier.

## Allow Remote Access WAN

Se questa opzione e' abilitata, le risorse sul lato WAN del dispositivo possono essere raggiunte tramite la rete virtuale ZeroTier.

Ad esempio, come mostrato nella topologia seguente, se questa funzione e' abilitata puoi accedere a `GL-AXT1800` tramite il suo indirizzo IP (`192.168.29.1`) da `leo-phone`. Questo e' possibile perche' GL-AXT1800 e' il dispositivo di livello superiore di `GL-MT2500`, e quest'ultimo e' connesso alla stessa rete ZeroTier di leo-phone.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Nota**: questa funzione richiede l'aggiunta di regole di routing nella rete ZeroTier per avere effetto. In Legacy Central e' possibile aggiungere gratuitamente una custom route, mentre in New Central puoi configurare custom route solo con un piano Essential o superiore. Fai clic [qui](https://www.zerotier.com/pricing/) per i dettagli.

I passaggi seguenti usano come esempio Legacy Central.

1. Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **ZeroTier**.

    Abilita **Allow Remote Access WAN** e fai clic su **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    Ti verra' chiesto di configurare le regole di routing. Lascia aperta questa pagina web oppure annota i dettagli della route, Destination e Via, perche' ti serviranno nel passaggio successivo.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Vai su **ZeroTier Central** e individua la sezione **Advanced**.

    Inserisci i dettagli della route, Destination e Via, ottenuti al passaggio precedente, quindi fai clic su **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

    Una volta aggiunta la route, la sezione **Managed Routes** verra' mostrata come segue.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. Ora puoi accedere a `GL-AXT1800` tramite il suo indirizzo IP (`192.168.29.1`) da altri dispositivi. In pratica, puoi accedere a tutti i dispositivi della subnet `192.168.29.0/24`.

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN

Se questa opzione e' abilitata, le risorse sul lato LAN del dispositivo possono essere raggiunte tramite la rete virtuale ZeroTier.

Ad esempio, come mostrato nella topologia seguente, se questa funzione e' abilitata puoi accedere via SSH a `Ubuntu` tramite il suo indirizzo IP (`192.168.8.110`) da `leo-phone`. Questo e' possibile perche' `Ubuntu` e' il dispositivo di livello inferiore di `GL-MT2500`, e quest'ultimo e' connesso alla stessa rete ZeroTier di leo-phone.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Nota**: questa funzione richiede l'aggiunta di regole di routing nella rete ZeroTier per avere effetto. In Legacy Central e' possibile aggiungere gratuitamente una custom route, mentre in New Central puoi configurare custom route solo con un piano Essential o superiore. Fai clic [qui](https://www.zerotier.com/pricing/) per i dettagli.

I passaggi seguenti usano come esempio Legacy Central.

1. Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **ZeroTier**.

    Abilita **Allow Remote Access LAN** e fai clic su **Apply**.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    Ti verra' chiesto di configurare le regole di routing. Lascia aperta questa pagina web oppure annota i dettagli della route, Destination e Via, perche' ti serviranno nel passaggio successivo.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Vai su **ZeroTier Central** e individua la sezione **Advanced**.

    Inserisci i dettagli della route, Destination e Via, ottenuti al passaggio precedente, quindi fai clic su **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    Una volta aggiunta la route, la sezione **Managed Routes** verra' mostrata come segue.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. Ora puoi eseguire il ping o accedere via SSH a `Ubuntu` tramite il suo indirizzo IP (`192.168.8.110`) da altri dispositivi. In pratica, puoi accedere a tutti i dispositivi della subnet `192.168.8.0/24`.

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
