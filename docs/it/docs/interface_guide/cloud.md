# GL.iNet GoodCloud

## Introduzione

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} è una piattaforma progettata per semplificare l'implementazione e la gestione remota dei dispositivi connessi. Fornisce un modo semplice per accedere e gestire in remoto i router GL.iNet. Centralizzando i dispositivi di rete sul cloud, gli utenti possono eseguire in modo efficiente attività di gestione batch, come la distribuzione di configurazioni di rete e l'esecuzione di aggiornamenti software. Possono anche accedere in remoto al pannello di amministrazione web del router o connettersi al terminale del router tramite SSH, ottenendo la gestione dei dispositivi di rete interregionali ed end-to-end.

Con GoodCloud puoi:

1. Controlla lo stato in tempo reale del router
    - Monitora lo stato online-offline
    - Visualizza l'utilizzo della RAM in tempo reale e il carico medio
    - Ricevi avvisi via email per le modifiche allo stato online-offline

2. Configura i router da remoto
    - configurare le impostazioni del router (ad esempio SSID e password)
    - Accesso SSH remoto
    - Accesso remoto alla WebUI
    - Condividi l'accesso al router con altri

3. Monitora i client connessi da remoto
    - Visualizza i dispositivi connessi alla tua rete
    - Monitora il traffico in tempo reale e blocca i client
    - Ricevi avvisi e-mail per nuove connessioni e blocca eventi

4. Eseguire operazioni batch
    - Riavvio batch
    - Aggiornamento firmware batch

5. Stabilire la connettività da sito a sito
    - Ufficio virtuale: estendi la tua rete aziendale ad altre filiali
    - Viaggi d'affari: accesso remoto ai sistemi per ufficio (ad esempio OA, CRM e MySQL)
    - Smart Home: accesso remoto ai dispositivi domestici (ad esempio telecamere IP e NAS)

Se hai bisogno di gestire più dispositivi e sbloccare funzionalità avanzate come operazioni in blocco, gestione di più account e soluzioni personalizzate, scegli i nostri piani a valore aggiunto. Fare clic su [here](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} per i dettagli e non esitate a contattare [support@gl-inet.com](mailto:support@gl-inet.com).

## Associa i dispositivi al cloud

Seleziona la sezione corrispondente per i passaggi di associazione del dispositivo in base alla versione firmware del tuo dispositivo.

### Per firmware v4.10 e versioni successive

1. Abilita GoodCloud.

    Accedi al pannello di amministrazione web del tuo router, vai a **CLOUD SERVICE** -> **GoodCloud** e fai clic su **Get Started**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    Verrai indirizzato alla pagina **GL.iNet Account**. Fare clic su **Bind GL.iNet Account via URL**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    Nella finestra pop-up, fare clic su **Continue**. Verrai reindirizzato al sito Web GoodCloud per completare l'associazione.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Accedi per associare il tuo dispositivo.

    Accedi al tuo account GL.iNet. Se non hai un account, creane uno ed effettua il login.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Dopo aver effettuato l'accesso, conferma il tuo account e le informazioni sul dispositivo, inclusi ID dispositivo, modello e indirizzo MAC. Personalizza il nome di un dispositivo e fai clic su **Bind**, quindi il router sarà associato al tuo account.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Se non ricevi l'email di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Si prega di inviare un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ulteriore assistenza.

3. Dettagli vincolanti.

    Dopo aver eseguito correttamente l'associazione, torna al pannello di amministrazione web del router e vai a **CLOUD SERVICES** -> **GoodCloud**. Questa pagina visualizza una voce di reindirizzamento alla piattaforma GoodCloud, i dettagli sull'identità del dispositivo e i registri cloud recenti.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Accesso remoto.

    Nel firmware v4.10, l'accesso remoto al pannello di amministrazione web e al terminale del router sarà abilitato per impostazione predefinita una volta che il router sarà collegato a GoodCloud.

5. Scollegare il dispositivo.

    Se desideri scollegare il router, accedi al pannello di amministrazione web del router e vai su **CLOUD SERVICES** -> **GL.iNet Account**. Fare clic su **Unbind**.

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    In alternativa, puoi rimuovere il dispositivo dall'elenco Dispositivi associati sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzerà per visualizzare l'ultimo stato di associazione.

    In caso di difficoltà, inviare un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ricevere assistenza.

### Per firmware da v4.7 a v4.9

1. Abilita GoodCloud.

    Accedi al pannello di amministrazione web del tuo router e vai a **CLOUD SERVICE** -> **GoodCloud**.

    Fare clic sul pulsante **Get Started** e nell'angolo in alto a destra verrà visualizzata una finestra pop-up del servizio cloud. Fare clic su **Enable**.

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

2. Accedi per associare il tuo dispositivo.

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Se non disponi di un account, creane uno ed effettua l'accesso. Una volta completata la registrazione, il router verrà automaticamente associato al tuo account.

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Se non ricevi l'email di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Si prega di inviare un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ulteriore assistenza.

3. Dettagli vincolanti.

    Dopo aver eseguito correttamente l'associazione, torna al pannello di amministrazione web del router, fai clic sull'icona Cloud nell'angolo in alto a destra e vedrai i dettagli dell'associazione, inclusi nome utente, tempo di associazione, ID dispositivo, MAC dispositivo e S/N dispositivo.

    ![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

4. Abilita l'accesso remoto.

    Nel pannello di amministrazione web, vai a **CLOUD SERVICES** -> **GoodCloud** e puoi abilitare l'accesso remoto per il tuo router.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

    - **Remote SSH**: per accedere in remoto al terminale del router tramite SSH dalla piattaforma GoodCloud.

    - **Remote Web Access**: per accedere da remoto al pannello di amministrazione web del router tramite HTTP/HTTPS dalla piattaforma GoodCloud.

    - **View Logs**: mostrerà i registri delle chiamate API di GoodCloud.

5. Scollegare il dispositivo.

    Se desideri scollegare il router, accedi al pannello di amministrazione web del router. Fare clic sull'icona della nuvola nell'angolo in alto a destra e fare clic su **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    In alternativa, puoi rimuovere il dispositivo dall'elenco Dispositivi associati sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzerà per visualizzare l'ultimo stato di associazione.

    In caso di difficoltà, inviare un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ricevere assistenza.

### Per firmware v4.6 o precedente

1. Abilita GoodCloud.

    Accedi al pannello di amministrazione web del tuo router e vai a **APPLICATIONS** -> **GoodCloud**. Attiva l'interruttore per abilitare GoodCloud.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    Abilita **Remote SSH** e **Remote Web Access** se necessario, seleziona il server più vicino, leggi e accetta **Terms of Service & Privacy Policy**, quindi fai clic su **Apply**.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: per accedere in remoto al terminale del router tramite SSH dalla piattaforma GoodCloud.

    - **Remote Web Access**: per accedere da remoto al pannello di amministrazione web del router tramite HTTP/HTTPS dalla piattaforma GoodCloud.

    - **Data Server**: Scegli il server più vicino alla posizione del tuo dispositivo. Sono disponibili tre opzioni: Asia Pacifico (Japan), America (Oregon) ed Europa (Ireland).

2. Registra un account.

    Visita [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, registrati e accedi.

    Se non ricevi l'email di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Si prega di inviare un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ulteriore assistenza.

3. Aggiungi dispositivi.

    Sulla piattaforma Cloud, accedere a **Devices** -> **Bound Devices** -> **Add Devices**.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Esistono tre metodi per associare il dispositivo al tuo account GoodCloud: rilevamento automatico, aggiunta manuale e importazione in blocco.

    ??? "Auto Discover"

        Puoi provare **Auto discover** se il router e il dispositivo utilizzato per accedere al sito Web GoodCloud si trovano sulla stessa rete.

        Seleziona il tuo dispositivo dall'elenco a discesa e inserisci **DDNS / Device ID**, che puoi trovare nella parte inferiore del router o nella pagina GoodCloud nel pannello di amministrazione web.

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Fare riferimento a [this link](../faq/where_to_find_the_device_id_mac_sn.md) per trovare l'ID dispositivo.

    ??? "Manually Add"

        Se il tuo dispositivo non è nell'elenco, fai clic su **Manually add** e inserisci i dettagli del tuo router. Tutte le informazioni richieste possono essere trovate nella parte inferiore del router o sulla pagina GoodCloud nel pannello di amministrazione web.

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** è progettato per gli utenti che gestiscono un gran numero di dispositivi. Puoi importare più dispositivi tramite un file Microsoft Excel.

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Dettagli vincolanti.

    Dopo aver eseguito correttamente l'associazione, torna al pannello di amministrazione web del router e vai a **APPLICATIONS** -> **GoodCloud**. Questa pagina visualizza i dettagli di associazione, inclusi nome utente e tempo di associazione.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

5. Scollegare il dispositivo.

    Se desideri scollegare il router, accedi al pannello di amministrazione web del router, vai a **APPLICATION** -> **GoodCloud** e fai clic su **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    In alternativa, puoi rimuovere il dispositivo dall'elenco Dispositivi associati sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzerà per visualizzare l'ultimo stato di associazione.

    In caso di difficoltà, inviare un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ricevere assistenza.
