# VPN Dashboard (Firmware v4.9)

**Nota**: questa guida si basa sul firmware v4.9. Per le versioni precedenti, fai riferimento [qui](vpn_dashboard.md).

---

Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **VPN Dashboard**.

Il VPN dashboard mostra dettagli della connessione VPN, come regole di instradamento, server connesso, statistiche del traffico, IP virtuale del client e log di connessione, e consente di configurare impostazioni avanzate come VPN Kill Switch, IP Masquerading e MTU.

Rispetto al firmware v4.8, v4.9 include i seguenti miglioramenti al VPN Dashboard:

1. **Consente agli utenti di selezionare piu' profili all'interno di un gruppo di tunnel e di impostarne la priorita'**. Il tunnel tentera' di connettersi usando ciascun profilo in ordine di priorita' fino a stabilire correttamente una connessione.

2. **Ogni gruppo di tunnel opera in modo indipendente e non esegue failover tra gruppi**. Se tutti i profili in un singolo tunnel non riescono a connettersi, il sistema determinera' se passare alla WAN locale in base allo stato del Tunnel Kill Switch e del tunnel All Other Traffic.

## Primi passi

Quando entri in questa pagina per la prima volta, se non e' stato creato alcun tunnel, la pagina apparira' come mostrato di seguito. Fai clic su **Add VPN Tunnel** per iniziare.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**Seleziona un provider VPN**. I provider VPN elencati sono integrati nel pannello di amministrazione web del router GL.iNet. Con un abbonamento attivo, gli utenti devono solo inserire le proprie credenziali per effettuare subito il login e ottenere i file di configurazione per le connessioni VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

Se hai sottoscritto altri provider VPN, oppure vuoi caricare configurazioni VPN personali, vai su **VPN Client Profile** per la configurazione manuale.

Ecco un esempio con **Hide.me**. Effettua il login con le credenziali Hide.me.

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**Seleziona un server VPN**. Questo e' il server a cui ti collegherai tramite questo tunnel VPN e il tuo indirizzo IP pubblico sembrera' provenire dalla posizione del server selezionato. Fai clic su **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

La connessione verra' avviata automaticamente. Fai clic su **Done**.

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

Verrai indirizzato al VPN Dashboard, dove VPN Tunnel 1 sara' stato abilitato e connesso.

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**In questo esempio, tutti i client connessi a questo router accederanno a Internet attraverso questo tunnel VPN.**

Se vuoi configurare la policy VPN, fai riferimento a [VPN Policy](#vpn-policy).

**All Other Traffic** e' un tunnel pre-abilitato mostrato nella parte inferiore del VPN Dashboard. Fai clic [qui](#all-other-traffic) per i dettagli.

## Dettagli del tunnel

Nel VPN Dashboard, ciascun tunnel VPN individuale viene mostrato come di seguito, con informazioni dettagliate sul tunnel VPN come regole di instradamento, server connesso, statistiche del traffico, indirizzo del server, porta di ascolto, IP virtuale del client e log di connessione. Puoi abilitare o disabilitare il tunnel VPN e configurare le impostazioni del tunnel nella parte superiore del gruppo tunnel.

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## VPN Policy

Una VPN policy definisce come il traffico di rete viene instradato attraverso i tunnel VPN, determinando quale traffico va verso le destinazioni di destinazione tramite VPN e quale accede direttamente a Internet tramite WAN locale.

Consente a tutti i client o a dispositivi specifici di accedere a siti web designati o all'intera Internet tramite una connessione VPN, permettendo una gestione di rete flessibile e sicura.

### Configurazione rapida

Nel VPN Dashboard, fai clic su **Add New Tunnel** oppure fai clic sull'area centrale di un tunnel VPN esistente.

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

Segui quindi la procedura guidata per configurare la VPN policy, inclusa la selezione del profilo VPN, dell'origine del traffico e della destinazione del traffico.

1. **Seleziona il profilo VPN.**

    Se hai effettuato il login con credenziali di servizi VPN integrati o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

    Prendiamo [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} come esempio. Effettua il login con le tue credenziali di servizio e vedrai un elenco di profili VPN. Seleziona uno o piu' profili e regola la priorita' sulla destra secondo necessita'.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Nota**: quando sono selezionati piu' profili, il tunnel tentera' di connettersi usando ciascun profilo in ordine di priorita' fino a stabilire correttamente una connessione. Se tutti i profili all'interno di un singolo tunnel non riescono a connettersi, il sistema determinera' se passare alla WAN locale in base allo stato del Tunnel Kill Switch e del tunnel [All Other Traffic](#all-other-traffic).

2. **Seleziona l'origine client.**

    Sono disponibili quattro opzioni:

    - **All Clients**: se selezionato, il traffico di tutti i dispositivi corrispondera' a questa regola.
      ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: se selezionato, il traffico dei tipi di connessione specificati, ad esempio LAN subnet, Drop-in Gateway e Guest Network, corrispondera' a questa regola.
      ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, corrispondera' a questa regola.
      ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, non corrispondera' a questa regola.
      ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **Seleziona la destinazione di destinazione**.

    Sono disponibili tre opzioni:

    - **All Targets**: se selezionato, il traffico che corrisponde a questa regola verra' instradato verso tutte le destinazioni.
      ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola verra' instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.
      ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola non verra' instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.
      ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Scenari di utilizzo

Di seguito trovi due scenari con istruzioni passo-passo di riferimento.

**Scenario 1**

**Obiettivi**:

1. Solo i dispositivi specifici collegati a questo router accedono a Internet tramite VPN. Tutti gli altri dispositivi accedono a Internet tramite WAN locale.

2. I dispositivi selezionati devono usare solo la connessione VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verra' bloccato per prevenire DNS leak e tracciamento IP.

**Segui i passaggi seguenti per configurare la VPN policy.**

1. Seleziona il profilo VPN.

    Se hai effettuato il login con credenziali di servizi VPN integrati o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

    Prendiamo [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} come esempio. Effettua il login con le tue credenziali di servizio e vedrai un elenco di profili VPN.

    ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

    Seleziona uno o piu' profili e regola la priorita' sulla destra secondo necessita'.

    ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

2. Seleziona **Specified Devices** come origine client, poi seleziona i dispositivi che useranno la VPN e fai clic su **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. Seleziona **All Targets** come destinazione, quindi fai clic su **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. Verrai reindirizzato al VPN Dashboard, dove sara' stato aggiunto un tunnel VPN.

    ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. Assicurati che il **Kill Switch** per questo tunnel sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verra' bloccato per prevenire DNS leak e tracciamento IP.

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}

6. Assicurati che **All Other Traffic** sia abilitato e che la modalita' sia impostata su **Allow Non-VPN Traffic**. Questo garantisce che il traffico che non corrisponde ai tunnel VPN sopra configurati possa comunque accedere a Internet tramite WAN locale.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. Attiva l'interruttore per avviare questo tunnel.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. Una volta connesso, la pagina mostrera' i dettagli della connessione VPN, inclusi VPN policy, statistiche del traffico, indirizzo del server, porta di ascolto e indirizzo IP virtuale.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

    Ora solo i due dispositivi specificati accederanno a Internet tramite VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verra' bloccato per prevenire DNS leak e tracciamento IP. Tutti gli altri dispositivi accederanno invece a Internet tramite WAN locale.

**Scenario 2**

**Obiettivi:**

1. Tutti i dispositivi usano **VPN Tunnel 1** quando accedono ai domini di specifici servizi social e di streaming e usano **VPN Tunnel 2** per tutto il resto dell'accesso a Internet.

2. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verra' bloccato per prevenire DNS leak e tracciamento IP.

**Segui i passaggi seguenti per configurare la VPN policy.**

1. Seleziona il profilo VPN per Tunnel 1.

    Se hai effettuato il login con credenziali di servizi VPN integrati o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

    Prendiamo [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} come esempio. Effettua il login con le tue credenziali di servizio e vedrai un elenco di profili VPN.

    ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}

    Seleziona uno o piu' profili e regola la priorita' sulla destra secondo necessita'.

    ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

2. Seleziona **All Clients** come origine client per Tunnel 1, poi fai clic su **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Seleziona **Specified Domain / IP List** come destinazione per Tunnel 1. Inserisci i domini di alcuni servizi social e di streaming comuni, come mostrato di seguito, poi fai clic su **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. Verrai reindirizzato al VPN Dashboard, dove sara' stato aggiunto Tunnel 1.

    ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Assicurati che il **Kill Switch** di Tunnel 1 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verra' bloccato per prevenire DNS leak e tracciamento IP.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}

6. Fai clic su **Add New Tunnel** per aggiungere Tunnel 2.

    ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Seleziona il profilo VPN per Tunnel 2.

    Se hai effettuato il login con credenziali di servizi VPN integrati o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

    Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Effettua il login con le tue credenziali di servizio e vedrai un elenco di profili VPN.

    ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}

    Seleziona uno o piu' profili e regola la priorita' sulla destra secondo necessita'.

    ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

8. Seleziona **All Clients** come origine client per Tunnel 2, poi fai clic su **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Seleziona **All Targets** come destinazione per Tunnel 2, quindi fai clic su **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. Verrai reindirizzato al VPN Dashboard, dove sara' stato aggiunto Tunnel 2.

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Assicurati che il **Kill Switch** di Tunnel 2 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verra' bloccato per prevenire DNS leak e tracciamento IP.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. Disabilita **All Other Traffic**. Assicurati che la modalita' sia impostata su **Enhanced Kill Switch**. Questo garantisce che tutto il traffico debba accedere a Internet tramite VPN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. Attiva l'interruttore per abilitare Tunnel 1 e Tunnel 2.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. Una volta connesso, la pagina mostrera' i dettagli della connessione VPN, inclusi VPN policy, statistiche del traffico, indirizzo del server, porta di ascolto e indirizzo IP virtuale.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    Ora tutti i dispositivi useranno **VPN Tunnel 1** quando accedono ai domini specificati e useranno **VPN Tunnel 2** per tutto il resto dell'accesso a Internet. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verra' bloccato per prevenire DNS leak e tracciamento IP.

## All Other Traffic

Questa opzione controlla se il traffico che non corrisponde a nessuno dei gruppi di tunnel VPN sopra puo' accedere a Internet. E' abilitata per impostazione predefinita per garantire il normale accesso a Internet al traffico non instradato tramite VPN.

Quando e' abilitata, il traffico non corrispondente puo' comunque accedere a Internet.

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

Quando e' disabilitata, solo il traffico instradato tramite VPN puo' accedere a Internet. Tutto il traffico non VPN e il traffico che effettua failover dalle connessioni VPN verra' bloccato. Questa opzione non sovrascrive il Kill Switch individuale di ciascun tunnel VPN.

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## Tunnel Priority

Per regolare la priorita' dei tunnel, fai clic sull'icona dell'ingranaggio in un gruppo tunnel e seleziona **Sort**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Fai clic e tieni premuta l'icona a tre linee sulla destra per riordinare i tunnel, poi fai clic su **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Quando sono abilitati piu' tunnel, il router instrada il traffico secondo le seguenti regole**:

1. Il traffico tentera' prima di corrispondere alla regola del tunnel con priorita' piu' alta. Se corrisponde, verra' instradato attraverso quel tunnel; altrimenti provera' il tunnel con priorita' successiva e cosi' via.

2. Ogni gruppo tunnel opera in modo indipendente. Una volta che il traffico corrisponde a una regola di tunnel, verra' instradato attraverso quel tunnel e non effettuera' failover tra gruppi tunnel.

3. All'interno di ciascun gruppo tunnel possono essere selezionati piu' profili per abilitare il failover intra-tunnel. Quando il profilo con priorita' piu' alta in un gruppo tunnel non e' disponibile, il tunnel si connettera' automaticamente usando il profilo con priorita' immediatamente successiva, e cosi' via.

4. Se un tunnel VPN si disconnette inaspettatamente, il sistema determinera' se fare failover del traffico verso il tunnel All Other Traffic in base al fatto che il **Kill Switch** di questo tunnel sia abilitato.

    - Se il Kill Switch e' abilitato, il traffico verra' bloccato e non fara' failover verso il tunnel All Other Traffic.
    - Se il Kill Switch e' disabilitato, il traffico fara' failover verso il tunnel All Other Traffic.

5. Il tunnel **All Other Traffic** e' abilitato per impostazione predefinita per garantire che il traffico che non corrisponde ai tunnel VPN possa comunque accedere a Internet.

    - Se abilitato, instrada il traffico non corrispondente o in failover tramite WAN locale.
    - Se disabilitato, rafforza il Kill Switch e blocca il normale accesso a Internet per prevenire perdite di IP.

## Tunnel Options

Puoi configurare impostazioni avanzate per ciascun tunnel VPN, come VPN Kill Switch, IP Masquerading e MTU.

Fai clic sull'icona dell'ingranaggio in un gruppo tunnel e seleziona **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, il traffico che corrisponde a questo tunnel VPN verra' bloccato se la connessione VPN fallisce inaspettatamente. Se disabilitato, tale traffico fara' failover verso il tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione e' disabilitata per impostazione predefinita, poiche' questi servizi richiedono normalmente il reale indirizzo IP del dispositivo per funzionare correttamente.

- **Allow Remote Access to the LAN Subnet**: se abilitato, sara' consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite la VPN. Richiede che il server VPN pubblichi una route di ritorno verso la propria subnet LAN.

- **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilitalo solo per configurazioni Site-to-Site in cui il peer remoto conosce gia' le tue subnet LAN.

- **MTU**: il valore MTU impostato per il tunnel sovrascrivera' le impostazioni MTU nel file di configurazione.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
