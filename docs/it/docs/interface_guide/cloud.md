# GL.iNet GoodCloud

## Indice

- [Introduzione](#introduction)
- [Collegare dispositivi a GoodCloud](#bind-devices-to-goodcloud)
    - [Per firmware v4.6 o precedenti](#for-firmware-v46-or-earlier)
        - [Abilitare GoodCloud](#enable-goodcloud)
        - [Registrare un account](#sign-up-an-account)
        - [Aggiungere dispositivi](#add-devices)
        - [Dettagli del collegamento](#binding-details)
        - [Scollegare un dispositivo](#unbind-device)
    - [Per firmware v4.7 o successivi](#for-firmware-v47-or-later)
        - [Abilitare Cloud Service](#enable-cloud-service)
        - [Dettagli del collegamento](#binding-details_1)
        - [Scollegare un dispositivo](#unbind-device_1)
- [Gestire i dispositivi](#manage-devices)
    - [Informazioni di sistema e azioni](#system-info-and-actions)
    - [Dettagli del dispositivo](#device-details)
        - [Informazioni di base](#basic-info)
        - [Statistiche](#statistics)
        - [Impostazioni di rete](#network-settings)
        - [Elenco client](#clients-list)
- [Accesso remoto](#remote-access)
    - [GUI remota](#remote-gui)
    - [SSH remoto](#remote-ssh)
- [Modificare le impostazioni](#modify-settings)
- [Avvisi e-mail](#email-alarm)
- [Site to Site](#site-to-site)
- [GoodCloud e VPN](#goodcloud-and-vpn)
- [Visualizzare i log](#view-logs)
- [Disabilitare il cloud](#disable-cloud)
- [Eliminare l'account](#delete-account)

## Introduzione {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} e' una piattaforma progettata per semplificare la distribuzione e la gestione remote dei dispositivi connessi. Offre un modo semplice per accedere e gestire da remoto i router GL.iNet. Centralizzando i dispositivi di rete nel cloud, gli utenti possono eseguire in modo efficiente operazioni di gestione in blocco, come distribuire configurazioni di rete ed effettuare aggiornamenti software. Possono inoltre accedere da remoto al pannello di amministrazione web del router o collegarsi al terminale del router tramite SSH, ottenendo una gestione dei dispositivi di rete end-to-end e tra diverse aree geografiche.

Con GoodCloud puoi:

1. Controllare lo stato del router in tempo reale
    - Monitorare lo stato online/offline
    - Visualizzare l'utilizzo della RAM e il carico medio in tempo reale
    - Ricevere avvisi e-mail per i cambiamenti di stato online/offline

2. Configurare i router da remoto
    - configurare le impostazioni del router (ad esempio SSID e password)
    - Accesso SSH remoto
    - Accesso remoto alla WebUI
    - Condividere l'accesso al router con altri

3. Monitorare da remoto i client connessi
    - Visualizzare i dispositivi connessi alla rete
    - Monitorare il traffico in tempo reale e bloccare i client
    - Ricevere avvisi e-mail per nuove connessioni ed eventi di blocco

4. Eseguire operazioni in blocco
    - Riavvio in blocco
    - Aggiornamento firmware in blocco

5. Stabilire una connettivita' Site-to-Site
    - Ufficio virtuale: estendere la rete dell'ufficio ad altre sedi
    - Viaggi di lavoro: accedere da remoto ai sistemi dell'ufficio (ad esempio OA, CRM, MySQL)
    - Smart Home: accedere da remoto ai dispositivi di casa (ad esempio telecamere IP, NAS)

Se hai bisogno di gestire piu' dispositivi e sbloccare funzionalita' avanzate come operazioni in blocco, gestione multi-account e soluzioni personalizzate, scegli i nostri piani a valore aggiunto. Fai clic [qui](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} per i dettagli e non esitare a contattare [support@glinet.biz](mailto:support@glinet.biz).

## Collegare dispositivi a GoodCloud {#bind-devices-to-goodcloud}

Per collegare correttamente i dispositivi alla piattaforma cloud, segui la procedura di collegamento corrispondente alla tua versione del firmware.

### Per firmware v4.6 o precedenti {#for-firmware-v46-or-earlier}

#### Abilitare GoodCloud {#enable-goodcloud}

Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **GoodCloud**. Attiva l'interruttore per abilitare GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

Abilita **Remote SSH** e **Remote Web Access** secondo necessita', seleziona il server piu' vicino, leggi e accetta i **Terms of Service & Privacy Policy**, quindi fai clic su **Apply**.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH**: per accedere da remoto al terminale del router tramite GoodCloud.

- **Remote Web Access**: per accedere da remoto al pannello di amministrazione web del router tramite GoodCloud.

- **Data Server**: scegli il server piu' vicino alla posizione del tuo dispositivo. Sono disponibili tre opzioni: Asia Pacific (Japan), America (Oregon) ed Europe (Ireland).

#### Registrare un account {#sign-up-an-account}

Visita il [sito web di GoodCloud](https://www.goodcloud.xyz){target="_blank"} per registrare un account ed effettuare l'accesso.

Se non ricevi l'e-mail di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Per qualsiasi difficolta' nella registrazione, invia un'e-mail a [support@glinet.biz](mailto:support@glinet.biz) per ricevere assistenza.

#### Aggiungere dispositivi {#add-devices}

Sulla piattaforma Cloud, vai su **Devices** -> **Bound Devices** -> **Add Devices**.

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

Ci sono tre metodi per collegare un dispositivo al tuo account GoodCloud: Auto Discover, Manually Add e Bulk Import.

??? "Auto Discover"

    Puoi provare **Auto discover** se il router e il dispositivo usato per accedere al sito GoodCloud si trovano sulla stessa rete.

    Seleziona il tuo dispositivo dal menu a discesa e inserisci **DDNS / Device ID**, che puoi trovare nella parte inferiore del router oppure nella pagina GoodCloud del pannello di amministrazione web.

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Per trovare il Device ID, fai riferimento [a questo link](../faq/where_to_find_the_device_id_mac_sn.md).

??? "Manually Add"

    Se il tuo dispositivo non e' presente nell'elenco, fai clic su **Manually add** e inserisci i dettagli del router. Tutte le informazioni richieste si trovano nella parte inferiore del router oppure nella pagina GoodCloud del pannello di amministrazione web.

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** e' pensato per gli utenti che gestiscono un gran numero di dispositivi. Puoi importare piu' dispositivi tramite un file Microsoft Excel.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### Dettagli del collegamento {#binding-details}

Dopo aver completato correttamente il collegamento, accedi nuovamente al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **GoodCloud**. Aggiorna questa pagina e verranno mostrati il nome utente GoodCloud associato e la data.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Scollegare un dispositivo {#unbind-device}

Se vuoi scollegare il router, accedi al pannello di amministrazione web del router, vai su **APPLICATION** -> **GoodCloud** e fai clic su **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

In alternativa, puoi rimuovere il dispositivo corrispondente dall'elenco Bound Devices sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzera' quindi per riflettere lo stato piu' recente del collegamento del dispositivo.

Per qualsiasi difficolta', invia un'e-mail a [support@glinet.biz](mailto:support@glinet.biz) per ricevere assistenza.

### Per firmware v4.7 o successivi {#for-firmware-v47-or-later}

#### Abilitare Cloud Service {#enable-cloud-service}

Accedi al pannello di amministrazione web del router e vai su **CLOUD SERVICE** -> **GoodCloud**.

Fai clic sul pulsante **Get Started** e apparira' una finestra pop-up Cloud Service nell'angolo superiore destro. Fai clic su **Enable** per usare Cloud Service.

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

Accedi al tuo account GoodCloud.

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

Se non hai un account, registrane uno ed effettua l'accesso. Una volta completata la registrazione, il router verra' associato automaticamente a questo account.

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

Se non ricevi l'e-mail di verifica, controlla la cartella spam oppure attendi qualche minuto e riprova. Per qualsiasi difficolta' nella registrazione, invia un'e-mail a [support@glinet.biz](mailto:support@glinet.biz) per ricevere assistenza.

#### Dettagli del collegamento {#binding-details_1}

Dopo aver completato correttamente il collegamento, accedi nuovamente al pannello di amministrazione web del router, fai clic sull'icona Cloud nell'angolo superiore destro e vedrai i dettagli del collegamento, inclusi il nome utente GoodCloud associato e la data, Device ID, Device MAC e Device S/N.

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

Nel pannello di amministrazione web, vai su **CLOUD SERVICES** -> **GoodCloud** e potrai abilitare o disabilitare l'accesso remoto per il router.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH**: per accedere da remoto al terminale del router tramite GoodCloud.

- **Remote Web Access**: per accedere da remoto al pannello di amministrazione web del router tramite GoodCloud.

- **View Logs**: mostra i log delle chiamate API effettuate da GoodCloud.

#### Scollegare un dispositivo {#unbind-device_1}

Se vuoi scollegare il router, accedi al pannello di amministrazione web del router. Fai clic sull'icona cloud nell'angolo superiore destro, quindi fai clic su **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

In alternativa, puoi rimuovere il dispositivo corrispondente dall'elenco Bound Devices sulla piattaforma GoodCloud. Il pannello di amministrazione web del router si sincronizzera' quindi per riflettere lo stato piu' recente del collegamento del dispositivo.

Per qualsiasi difficolta', invia un'e-mail a [support@glinet.biz](mailto:support@glinet.biz) per ricevere assistenza.

## Gestire i dispositivi {#manage-devices}

### Informazioni di sistema e azioni {#system-info-and-actions}

In [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** puoi visualizzare le informazioni di sistema (ad esempio modello, versione, indirizzo MAC, indirizzo IP) e lo stato (ad esempio online, offline) di tutti i dispositivi associati al tuo account.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Seleziona un dispositivo, quindi potrai eseguire azioni nell'angolo superiore destro, come modificare le impostazioni, aggiornare il firmware, accedere da remoto al dispositivo, riavviarlo o reimpostarlo.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Fai clic sull'icona a forma di ingranaggio all'estrema destra dell'intestazione dell'elenco per personalizzare la visualizzazione delle colonne e il loro ordine, cosi' da concentrarti sulle informazioni del dispositivo piu' importanti.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Dettagli del dispositivo {#device-details}

In [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, fai clic sul nome di un dispositivo per essere reindirizzato alla pagina dei dettagli del dispositivo, dove vengono mostrate le informazioni di base del router, i dati statistici, le impostazioni di rete, l'elenco dei client e cosi' via.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Informazioni di base {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistiche {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Impostazioni di rete {#network-settings}

Questa pagina mostra le configurazioni di rete del router e le impostazioni Wi-Fi.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Elenco client {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Accesso remoto {#remote-access}

In [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, fai clic sul nome del dispositivo a cui vuoi accedere per entrare nella pagina dei dettagli, dove vedrai le azioni remote nell'angolo superiore destro.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### GUI remota {#remote-gui}

Fai clic su **Remote GUI** per accedere da remoto al pannello di amministrazione web del router.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Se questa opzione e' grigia o non disponibile, e' probabile che la funzione sia disabilitata. Abilitala prima nel pannello di amministrazione web del router, quindi accedi tramite GoodCloud.

Se questa opzione e' cliccabile ma non risponde, prova a usare la modalita' incognito/inPrivate del browser.

### SSH remoto {#remote-ssh}

Fai clic su **Remote SSH** per accedere da remoto al terminale del router tramite SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Se questa opzione e' grigia o non disponibile, e' probabile che la funzione sia disabilitata. Abilitala prima nel pannello di amministrazione web del router, quindi accedi tramite GoodCloud.

Se questa opzione e' cliccabile ma non risponde, prova a usare la modalita' incognito/inPrivate del browser.

## Modificare le impostazioni {#modify-settings}

Puoi configurare piu' parametri per un singolo dispositivo o per piu' dispositivi.

In [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, seleziona il dispositivo che vuoi configurare e, nell'angolo superiore destro, fai clic su **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Qui puoi controllare e modificare le impostazioni di rete del router, incluse wireless, Ethernet, sicurezza, port forwarding, LAN e impostazioni di sistema.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Avvisi e-mail {#email-alarm}

Puoi configurare un avviso e-mail quando cambia lo stato del dispositivo (online/offline) o quando si connettono nuovi client.

In [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications**, fai clic sul pulsante **Add Rule** nell'angolo superiore destro.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Seleziona il dispositivo da monitorare e fai clic su **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Seleziona l'evento trigger, ad esempio lo stato online/offline del dispositivo, e fai clic su **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Controlla le impostazioni della regola e fai clic su **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Nell'elenco Notifications puoi vedere le regole di avviso che hai creato. I singoli utenti possono creare una sola regola di avviso. Se hai bisogno della gestione in blocco dei dispositivi, contattaci per effettuare l'upgrade del piano.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site {#site-to-site}

Fai riferimento a [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud e VPN {#goodcloud-and-vpn}

Se abiliti **GoodCloud** e **VPN client** contemporaneamente sul router, per impostazione predefinita la connessione tra il router e il server GoodCloud non passera' attraverso la VPN. Questo garantisce una connessione piu' stabile ai servizi GoodCloud.

Tuttavia, se vuoi che la connessione GoodCloud passi attraverso la VPN, puoi modificare questa impostazione nel pannello di amministrazione web del router. Vai su VPN -> VPN Dashboard -> VPN Client -> Options e abilita l'opzione "Services from GL.iNet Use VPN".

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Tieni presente che instradare GoodCloud attraverso la VPN puo' influire sulla stabilita' della connessione cloud, soprattutto se:

* La connessione VPN e' instabile
* Il provider VPN filtra o blocca il traffico GoodCloud
* La VPN aggiunge una latenza significativa alla connessione

In generale, e' consigliabile mantenere l'impostazione predefinita in cui GoodCloud bypassa la VPN per ottenere prestazioni e affidabilita' ottimali.

## Visualizzare i log {#view-logs}

Puoi visualizzare i log GoodCloud secondo necessita', inclusi Activity Logs, Device Logs, Upgrade Logs, Alert Logs e Device Settings Logs.

In [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs**, seleziona dal menu a discesa i log che vuoi visualizzare.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Disabilitare il cloud {#disable-cloud}

Se non desideri piu' che il tuo dispositivo sia connesso alla piattaforma cloud, puoi disabilitare il servizio cloud nel pannello di amministrazione web del router.

??? "Per firmware v4.6 o precedenti"

    Accedi al pannello di amministrazione web del router, vai su **APPLICATIONS** -> **GoodCloud**, disattiva l'interruttore per disabilitare GoodCloud e fai clic su **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Una volta disabilitato, l'interfaccia verra' visualizzata come segue.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Per firmware v4.7 o successivi"

    Accedi al pannello di amministrazione web del router e fai clic sull'icona cloud nell'angolo superiore destro.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Una volta disabilitato, l'interfaccia verra' visualizzata come segue.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Eliminare l'account {#delete-account}

Per motivi di sicurezza, puoi eliminare il tuo account se non e' piu' in uso.

Sulla piattaforma [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, fai clic sul nome utente nell'angolo superiore destro e seleziona **Personal Center**. Scorri fino in fondo alla pagina e fai clic su **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    L'eliminazione cancellera' definitivamente tutti i servizi correlati, i dati e le informazioni personali, senza possibilita' di ripristino.

    Se il tuo account appartiene a una qualsiasi organizzazione, esci prima da tutte le organizzazioni prima di eliminare l'account.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
