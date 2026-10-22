# GL.iNet GoodCloud {#glinet-goodcloud}

## Introduzione {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} è una piattaforma progettata per semplificare l'implementazione e la gestione remota dei dispositivi connessi. Offre un modo semplice per accedere ai router GL.iNet e gestirli da remoto. Centralizzando i dispositivi di rete nel cloud, gli utenti possono eseguire in modo efficiente attività di gestione in blocco, come la distribuzione di configurazioni di rete e l'aggiornamento del software. Possono inoltre accedere da remoto al pannello di amministrazione web del router o connettersi al terminale del router tramite SSH, ottenendo una gestione end-to-end dei dispositivi di rete anche tra regioni diverse.

Con GoodCloud puoi:

1. Controllare lo stato del router in tempo reale
    - Monitorare lo stato online/offline
    - Visualizzare in tempo reale l'utilizzo della RAM e il carico medio
    - Ricevere avvisi via e-mail sulle modifiche dello stato online/offline

2. Configurare i router da remoto
    - Configurare le impostazioni del router (ad esempio SSID e password)
    - Accesso SSH remoto
    - Accesso remoto alla WebUI
    - Condividere l'accesso al router con altri utenti

3. Monitorare da remoto i client connessi
    - Visualizzare i dispositivi connessi alla rete
    - Monitorare il traffico in tempo reale e bloccare i client
    - Ricevere avvisi via e-mail per nuove connessioni ed eventi di blocco

4. Eseguire operazioni in blocco
    - Riavvio in blocco
    - Aggiornamento firmware in blocco

5. Stabilire la connettività da sito a sito
    - Ufficio virtuale: estendere la rete dell'ufficio ad altre filiali
    - Viaggi di lavoro: accedere da remoto ai sistemi dell'ufficio (ad esempio OA, CRM, MySQL)
    - Smart home: accedere da remoto ai dispositivi domestici (ad esempio telecamere IP, NAS)

Se hai bisogno di gestire più dispositivi e di sbloccare funzionalità avanzate come operazioni in blocco, gestione di più account e soluzioni personalizzate, scegli i nostri piani a valore aggiunto. Fai clic [qui](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} per i dettagli e non esitare a contattare [support@gl-inet.com](mailto:support@gl-inet.com).

## Associare i dispositivi al cloud {#bind-devices-to-cloud}

Seleziona la sezione corrispondente alla versione firmware del tuo dispositivo per i passaggi di associazione.

### Per firmware v4.10 e versioni successive {#for-firmware-v410-and-above}

1. Abilita GoodCloud.

    Accedi al pannello di amministrazione web del router, vai a **CLOUD SERVICE** -> **GoodCloud** e fai clic su **Get Started**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    Verrai indirizzato alla pagina **GL.iNet Account**. Fai clic su **Bind GL.iNet Account via URL**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    Nella finestra pop-up, fai clic su **Continue**. Verrai reindirizzato al sito web di GoodCloud per completare l'associazione.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Accedi per associare il dispositivo.

    Accedi al tuo account GL.iNet. Se non hai un account, creane uno ed effettua l'accesso.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Dopo aver effettuato l'accesso, verifica le informazioni dell'account e del dispositivo, inclusi ID dispositivo, modello e indirizzo MAC. Assegna un nome personalizzato al dispositivo e fai clic su **Bind**: il router verrà associato al tuo account.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Se non ricevi l'e-mail di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Per ulteriore assistenza, invia un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com).

3. Dettagli dell'associazione.

    Dopo aver completato l'associazione, torna al pannello di amministrazione web del router e vai a **CLOUD SERVICES** -> **GoodCloud**. Questa pagina mostra un collegamento di reindirizzamento alla piattaforma GoodCloud, i dati identificativi del dispositivo e i log cloud recenti.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Accesso remoto.

    Nel firmware v4.10, l'accesso remoto al pannello di amministrazione web e al terminale del router viene abilitato per impostazione predefinita una volta che il router è associato a GoodCloud.

5. Dissocia il dispositivo.

    Se desideri dissociare il router, accedi al pannello di amministrazione web del router e vai a **CLOUD SERVICES** -> **GL.iNet Account**. Fai clic su **Unbind**.

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    In alternativa, puoi rimuovere il dispositivo dall'elenco Bound Devices sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzerà per mostrare lo stato di associazione più recente.

    In caso di difficoltà, invia un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ricevere assistenza.

### Per firmware da v4.7 a v4.9 {#for-firmware-v47-to-v49}

1. Abilita GoodCloud.

    Accedi al pannello di amministrazione web del router e vai a **CLOUD SERVICE** -> **GoodCloud**.

    Fai clic sul pulsante **Get Started**: nell'angolo in alto a destra verrà visualizzata la finestra pop-up Cloud Service. Fai clic su **Enable**.

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

2. Accedi per associare il dispositivo.

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Se non hai un account, creane uno ed effettua l'accesso. Una volta completata la registrazione, il router verrà associato automaticamente al tuo account.

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Se non ricevi l'e-mail di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Per ulteriore assistenza, invia un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com).

3. Dettagli dell'associazione.

    Dopo aver completato l'associazione, torna al pannello di amministrazione web del router e fai clic sull'icona del cloud nell'angolo in alto a destra: verranno visualizzati i dettagli dell'associazione, tra cui nome utente, ora di associazione, Device ID, Device MAC e Device S/N.

    ![binding details](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/binding_details.png){class="glboxshadow"}

4. Abilita l'accesso remoto.

    Nel pannello di amministrazione web, vai a **CLOUD SERVICES** -> **GoodCloud**, dove puoi abilitare l'accesso remoto al router.

    ![enable remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_remote_access.png){class="glboxshadow"}

    - **Remote SSH**: consente di accedere da remoto al terminale del router tramite SSH dalla piattaforma GoodCloud.

    - **Remote Web Access**: consente di accedere da remoto al pannello di amministrazione web del router tramite HTTP/HTTPS dalla piattaforma GoodCloud.

    - **View Logs**: mostra i log delle chiamate API effettuate da GoodCloud.

5. Dissocia il dispositivo.

    Se desideri dissociare il router, accedi al pannello di amministrazione web del router. Fai clic sull'icona del cloud nell'angolo in alto a destra, quindi su **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    In alternativa, puoi rimuovere il dispositivo dall'elenco Bound Devices sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzerà per mostrare lo stato di associazione più recente.

    In caso di difficoltà, invia un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ricevere assistenza.

### Per firmware v4.6 o precedente {#for-firmware-v46-or-earlier}

1. Abilita GoodCloud.

    Accedi al pannello di amministrazione web del router e vai a **APPLICATIONS** -> **GoodCloud**. Attiva l'interruttore per abilitare GoodCloud.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    Abilita **Remote SSH** e **Remote Web Access** se necessario, seleziona il server più vicino, leggi e accetta **Terms of Service & Privacy Policy**, quindi fai clic su **Apply**.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: consente di accedere da remoto al terminale del router tramite SSH dalla piattaforma GoodCloud.

    - **Remote Web Access**: consente di accedere da remoto al pannello di amministrazione web del router tramite HTTP/HTTPS dalla piattaforma GoodCloud.

    - **Data Server**: scegli il server più vicino alla posizione del dispositivo. Sono disponibili tre opzioni: Asia Pacifico (Giappone), America (Oregon) ed Europa (Irlanda).

2. Registra un account.

    Visita [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, registrati ed effettua l'accesso.

    Se non ricevi l'e-mail di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Per ulteriore assistenza, invia un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com).

3. Aggiungi i dispositivi.

    Sulla piattaforma cloud, vai a **Devices** -> **Bound Devices** -> **Add Devices**.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Esistono tre metodi per associare un dispositivo al tuo account GoodCloud: Auto Discover, Manually Add e Bulk Import.

    ??? "Auto Discover"

        Puoi provare **Auto discover** se il router e il dispositivo utilizzato per accedere al sito web di GoodCloud si trovano sulla stessa rete.

        Seleziona il dispositivo dall'elenco a discesa e inserisci il **DDNS / Device ID**, che si trova sul fondo del router oppure nella pagina GoodCloud del pannello di amministrazione web.

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Consulta [questo link](../faq/where_to_find_the_device_id_mac_sn.md) per trovare il Device ID.

    ??? "Manually Add"

        Se il dispositivo non è presente nell'elenco, fai clic su **Manually add** e inserisci i dati del router. Tutte le informazioni richieste si trovano sul fondo del router oppure nella pagina GoodCloud del pannello di amministrazione web.

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** è pensato per gli utenti che gestiscono un gran numero di dispositivi. Puoi importare più dispositivi tramite un file Microsoft Excel.

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Dettagli dell'associazione.

    Dopo aver completato l'associazione, torna al pannello di amministrazione web del router e vai a **APPLICATIONS** -> **GoodCloud**. Questa pagina mostra i dettagli dell'associazione, inclusi nome utente e ora di associazione.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info.png){class="glboxshadow"}

5. Dissocia il dispositivo.

    Se desideri dissociare il router, accedi al pannello di amministrazione web del router, vai a **APPLICATION** -> **GoodCloud** e fai clic su **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    In alternativa, puoi rimuovere il dispositivo dall'elenco Bound Devices sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzerà per mostrare lo stato di associazione più recente.

    In caso di difficoltà, invia un'e-mail a [support@gl-inet.com](mailto:support@gl-inet.com) per ricevere assistenza.

## Gestire i dispositivi {#manage-devices}

### Informazioni di sistema e azioni {#system-info-and-actions}

Su [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** puoi visualizzare le informazioni di sistema (ad esempio modello, versione, indirizzo MAC, indirizzo IP) e lo stato (ad esempio online, offline) di tutti i dispositivi associati al tuo account.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Seleziona un dispositivo: nell'angolo in alto a destra puoi eseguire azioni come modificare le impostazioni, aggiornare il firmware, accedere da remoto al dispositivo, riavviarlo o ripristinarlo.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Fai clic sull'icona a forma di ingranaggio all'estrema destra dell'intestazione dell'elenco per personalizzare la visualizzazione delle colonne e il loro ordine, in modo da concentrarti sulle informazioni del dispositivo più importanti.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Dettagli del dispositivo {#device-details}

Su [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, fai clic sul nome di un dispositivo: verrai reindirizzato alla pagina dei dettagli del dispositivo, che mostra le informazioni di base del router, i dati statistici, le impostazioni di rete, l'elenco dei client e altro ancora.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Informazioni di base {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistiche {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Impostazioni di rete {#network-settings}

Questa pagina mostra le configurazioni di rete e le impostazioni Wi-Fi del router.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Elenco dei client {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Accesso remoto {#remote-access}

Su [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, fai clic sul nome del dispositivo a cui desideri accedere per aprire la pagina dei dettagli: le azioni remote sono disponibili nell'angolo in alto a destra.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

Fai clic su **Remote GUI** per accedere da remoto al pannello di amministrazione web del router.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Se questa opzione è disattivata (in grigio) o non disponibile, è probabile che la funzione sia disabilitata. Abilitala prima nel pannello di amministrazione web del router, quindi accedi tramite GoodCloud.

Se l'opzione è selezionabile ma non risponde, prova a utilizzare la modalità di navigazione in incognito/InPrivate del browser.

### Remote SSH {#remote-ssh}

Fai clic su **Remote SSH** per accedere da remoto al terminale del router tramite SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Se questa opzione è disattivata (in grigio) o non disponibile, è probabile che la funzione sia disabilitata. Abilitala prima nel pannello di amministrazione web del router, quindi accedi tramite GoodCloud.

Se l'opzione è selezionabile ma non risponde, prova a utilizzare la modalità di navigazione in incognito/InPrivate del browser.

## Modificare le impostazioni {#modify-settings}

Puoi configurare più parametri per un singolo dispositivo o per più dispositivi.

Su [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, seleziona il dispositivo da configurare e, nell'angolo in alto a destra, fai clic su **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Qui puoi controllare e modificare le impostazioni di rete del router, incluse le impostazioni wireless, Ethernet, di sicurezza, di port forwarding, LAN e di sistema.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Avvisi via e-mail {#email-alarm}

Puoi configurare un avviso via e-mail quando cambia lo stato del dispositivo (online/offline) o quando si connettono nuovi client.

Su [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications**, fai clic sul pulsante **Add Rule** nell'angolo in alto a destra.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Seleziona il dispositivo da monitorare e fai clic su **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Seleziona l'evento di attivazione, ad esempio lo stato online/offline del dispositivo, e fai clic su **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Verifica le impostazioni della regola e fai clic su **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Nell'elenco Notifications puoi visualizzare le regole di avviso create. Gli utenti individuali possono creare una sola regola di avviso. Se hai bisogno di gestire dispositivi in blocco, contattaci per aggiornare il tuo piano.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Da sito a sito {#site-to-site}

Consulta [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud e VPN {#goodcloud-and-vpn}

Se sul router abiliti contemporaneamente **GoodCloud** e il **client VPN**, per impostazione predefinita la connessione tra il router e il server GoodCloud non passa attraverso la VPN. In questo modo la connessione ai servizi GoodCloud è più stabile.

Tuttavia, se desideri che la connessione a GoodCloud passi attraverso la VPN, puoi modificare questa impostazione nel pannello di amministrazione web del router. Vai a VPN -> VPN Dashboard -> VPN Client -> Options e abilita l'opzione "Services from GL.iNet Use VPN".

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Tieni presente che instradare GoodCloud attraverso la VPN può compromettere la stabilità della connessione al cloud, soprattutto se:

* La connessione VPN è instabile
* Il provider VPN filtra o blocca il traffico GoodCloud
* La VPN aggiunge una latenza significativa alla connessione

In generale, si consiglia di mantenere le impostazioni predefinite, in cui GoodCloud non passa attraverso la VPN, per ottenere prestazioni e affidabilità ottimali.

## Visualizzare i log {#view-logs}

Puoi visualizzare i log di GoodCloud in base alle tue esigenze, inclusi Activity Logs, Device Logs, Upgrade Logs, Alert Logs e Device Settings Logs.

Su [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs**, seleziona dall'elenco a discesa i log che desideri visualizzare.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Disabilitare il cloud {#disable-cloud}

Se non desideri più che il dispositivo sia connesso alla piattaforma cloud, puoi disabilitare il servizio cloud nel pannello di amministrazione web del router.

??? "Per firmware v4.6 o precedente"

    Accedi al pannello di amministrazione web del router, vai a **APPLICATIONS** -> **GoodCloud**, disattiva l'interruttore per disabilitare GoodCloud e fai clic su **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Una volta disabilitato, l'interfaccia verrà visualizzata come segue.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Per firmware v4.7 o successivo"

    Accedi al pannello di amministrazione web del router e fai clic sull'icona del cloud nell'angolo in alto a destra. Nella finestra pop-up **Cloud Service**, fai clic sull'icona a forma di ingranaggio e seleziona **Disable**.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Una volta disabilitato, l'interfaccia verrà visualizzata come segue.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Eliminare l'account {#delete-account}

Per motivi di sicurezza, puoi eliminare il tuo account se non lo utilizzi più.

Sulla piattaforma [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, fai clic sul nome utente nell'angolo in alto a destra e seleziona **Personal Center**. Scorri fino in fondo alla pagina e fai clic su **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    L'eliminazione cancellerà in modo permanente tutti i servizi, i dati e le informazioni personali associati, senza possibilità di recupero.

    Se il tuo account appartiene a una o più organizzazioni, abbandona tutte le organizzazioni prima di eliminare l'account.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
