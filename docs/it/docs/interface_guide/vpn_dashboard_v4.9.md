# VPN Dashboard (Firmware v4.9)

Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **VPN Dashboard**.

Il VPN dashboard mostra i dettagli della connessione VPN, come regole di instradamento, server connesso, statistiche del traffico, IP virtuale del client e log di connessione, e consente di configurare impostazioni avanzate come VPN Kill Switch, IP Masquerading e MTU.

Rispetto al firmware v4.8, v4.9 include i seguenti miglioramenti al VPN Dashboard:

1. **Consente agli utenti di selezionare più profili all'interno di un gruppo di tunnel e di impostarne la priorità**. Il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità fino a stabilire correttamente una connessione.

2. **Ogni gruppo di tunnel opera in modo indipendente e non esegue failover tra gruppi**. Se tutti i profili in un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale in base allo stato del Tunnel Kill Switch e del tunnel All Other Traffic.

## Primi passi

### Caricare un profilo VPN

Quando entri in questa pagina per la prima volta, se non è stato creato alcun tunnel, la pagina apparirà come mostrato di seguito. Fai clic su **Add VPN Tunnel** per iniziare.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

Verrai indirizzato alla pagina **VPN Client Profile**. Seleziona un provider VPN ed effettua il login.

I provider VPN elencati sono integrati nel pannello di amministrazione web del router GL.iNet. Con un abbonamento attivo, ti basta inserire le credenziali per effettuare subito il login e ottenere i file di configurazione per le connessioni VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

Se hai sottoscritto altri provider VPN, oppure vuoi caricare configurazioni VPN personali, fai clic su **Add Manually** e carica le tue configurazioni.

Prendiamo **PureVPN** come esempio. Fai clic su PureVPN ed effettua il login con credenziali valide.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Otterrai un elenco di profili VPN. Per alcuni provider di servizi VPN, prima che l'elenco dei profili venga mostrato potrebbe essere necessario selezionare un protocollo VPN oppure server o città preferiti.

Poi fai clic su **Go to Dashboard** in basso. Verrai indirizzato al VPN Dashboard per aggiungere il tuo tunnel VPN e configurare la VPN policy.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

### Configurare la VPN policy

!!! note "Che cos'è una VPN policy?"

    Una VPN policy definisce come il traffico di rete viene instradato attraverso i tunnel VPN, determinando quale traffico viene inviato alle destinazioni desiderate tramite VPN e quale accede direttamente a Internet tramite WAN locale.

    Consente a tutti i client o a dispositivi specifici di accedere a siti web designati o all'intera Internet tramite una connessione VPN, offrendo una gestione della rete flessibile e sicura.

Nel VPN Dashboard, segui la procedura guidata per configurare la VPN policy, inclusa la selezione del profilo VPN, dell'origine del traffico e della destinazione del traffico.

1. **Seleziona il profilo VPN.**

    Se hai effettuato in precedenza il login con credenziali di servizi VPN integrati oppure hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

    Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili e regola la priorità sulla destra secondo necessità.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Nota**: quando sono selezionati più profili, il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità fino a stabilire correttamente una connessione. Se tutti i profili all'interno di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale in base allo stato del Tunnel Kill Switch e della policy [All Other Traffic](#all-other-traffic).

2. **Seleziona l'origine client.**

    Sono disponibili quattro opzioni:

    - **All Clients**: se selezionato, il traffico di tutti i dispositivi corrisponderà a questa regola.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: se selezionato, il traffico dei tipi di connessione specificati, ad esempio LAN subnet, Drop-in Gateway o Guest Network, corrisponderà a questa regola.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, corrisponderà a questa regola.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, non corrisponderà a questa regola.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

3. **Seleziona la destinazione del traffico**.

    Sono disponibili tre opzioni:

    - **All Targets**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso tutte le destinazioni.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola non verrà instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Kill Switch

!!! note "Che cos'è il Kill Switch?"

    Il Kill Switch è una funzione di sicurezza per le connessioni VPN. Interrompe automaticamente tutto l'accesso a Internet della rete locale se la connessione VPN cade in modo imprevisto, evitando l'esposizione del tuo vero indirizzo IP e dei dati online e garantendo privacy e sicurezza continue. Questa funzione è particolarmente utile per mantenere un accesso a Internet sicuro e anonimo, ad esempio quando usi reti pubbliche, gestisci dati sensibili o vuoi nascondere il tuo indirizzo IP reale.

    Quando è abilitato, blocca qualsiasi traffico client che tenti di bypassare il tunnel VPN, impedendo efficacemente perdite VPN causate da problemi di configurazione DNS, disconnessioni impreviste, richieste IP dirette e scenari simili.

Dalla versione firmware v4.8, i router GL.iNet consentono di configurare un Kill Switch per ogni singolo tunnel VPN, oltre che per la connessione VPN globale.

- Per configurare il Kill Switch per ogni singolo tunnel VPN, fai riferimento [qui](#tunnel-options).

- Per configurare il Kill Switch per la connessione VPN globale (cioè Enhanced Kill Switch), fai riferimento [qui](#all-other-traffic).

## Scenari di utilizzo

Di seguito trovi due scenari con istruzioni passo passo.

### Scenario 1

**Obiettivi**:

1. Solo dispositivi specifici collegati a questo router accedono a Internet tramite VPN. Tutti gli altri dispositivi accedono a Internet tramite WAN locale.

2. I dispositivi selezionati devono usare solo la connessione VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verrà bloccato per prevenire DNS leak e tracciamento IP.

**Segui i passaggi seguenti per configurare la VPN policy.**

1. Seleziona il profilo VPN.

    Se hai effettuato il login con credenziali di servizi VPN integrati o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

    Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili e regola la priorità sulla destra secondo necessità.

    ![scenario 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    **Nota**: quando sono selezionati più profili, il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità fino a stabilire correttamente una connessione. Se tutti i profili all'interno di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale in base allo stato del Tunnel Kill Switch e della policy [All Other Traffic](#all-other-traffic).

2. Seleziona Client Source.

    Fai clic sulla scheda **Specified Devices**, seleziona i dispositivi che useranno la VPN, quindi fai clic su **Apply**.

    ![scenario 1 select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

3. Seleziona Target Destination.

    Fai clic sulla scheda **All Targets**, impostala come destinazione del traffico, quindi fai clic su **Apply**.

    ![scenario 1 select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

4. Verrai indirizzato al VPN Dashboard, dove sarà stato aggiunto un tunnel VPN.

    ![scenario 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

5. Assicurati che il **Kill Switch** per questo tunnel sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verrà bloccato per prevenire DNS leak e tracciamento IP.

    ![scenario 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

    ![scenario 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

6. Assicurati che **Allow Non-VPN Traffic** sia abilitato. È abilitato per impostazione predefinita per garantire che il traffico che non corrisponde al tunnel VPN possa comunque accedere a Internet tramite WAN locale.

    ![scenario 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

7. Fai clic sul pulsante centrale per attivare questo tunnel.

    ![scenario 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

8. Una volta connesso, la pagina mostrerà i dettagli della connessione VPN, inclusi VPN policy, statistiche del traffico, indirizzo del server, porta di ascolto e indirizzo IP virtuale.

    ![scenario 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

    Ora solo i dispositivi specificati accederanno a Internet tramite VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verrà bloccato per prevenire DNS leak e tracciamento IP. Tutti gli altri dispositivi accederanno invece a Internet tramite WAN locale.

### Scenario 2

**Obiettivi:**

1. Tutti i dispositivi usano **VPN Tunnel 1** quando accedono ai domini di specifici servizi social e di streaming e usano **VPN Tunnel 2** per tutto il resto dell'accesso a Internet.

2. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verrà bloccato per prevenire DNS leak e tracciamento IP.

**Segui i passaggi seguenti per configurare la VPN policy.**

1. Seleziona il profilo VPN per Tunnel 1.

    Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili e regola la priorità sulla destra secondo necessità.

    ![scenario 2 select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    **Nota**: quando sono selezionati più profili, il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità fino a stabilire correttamente una connessione. Se tutti i profili all'interno di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale in base allo stato del Tunnel Kill Switch e della policy [All Other Traffic](#all-other-traffic).

2. Seleziona Client Source.

    Fai clic sulla scheda **All Clients**, impostala come origine client per Tunnel 1, quindi fai clic su **Apply**.

    ![scenario 2 select source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

3. Seleziona Target Destination.

    Fai clic sulla scheda **Specified Domain / IP List**, inserisci i domini di alcuni servizi social e di streaming comuni, come mostrato di seguito, quindi fai clic su **Apply**.

    ![scenario 2 select target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

4. Verrai indirizzato al VPN Dashboard, dove Tunnel 1 sarà stato aggiunto.

    ![scenario 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

5. Assicurati che il **Kill Switch** di Tunnel 1 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verrà bloccato per prevenire DNS leak e tracciamento IP.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

6. Fai clic su **Add New Tunnel** per aggiungere Tunnel 2.

    ![scenario 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

7. Seleziona il profilo VPN per Tunnel 2.

    Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili e regola la priorità sulla destra secondo necessità.

    ![scenario 2 select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    **Nota**: quando sono selezionati più profili, il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità fino a stabilire correttamente una connessione. Se tutti i profili all'interno di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale in base allo stato del Tunnel Kill Switch e della policy [All Other Traffic](#all-other-traffic).

8. Seleziona Client Source.

    Fai clic sulla scheda **All Clients**, impostala come origine client per Tunnel 2, quindi fai clic su **Apply**.

    ![scenario 2 select source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. Seleziona Target Destination.

    Fai clic sulla scheda **All Targets**, impostala come destinazione del traffico per Tunnel 2, quindi fai clic su **Apply**.

    ![scenario 2 select target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

10. Verrai indirizzato al VPN Dashboard, dove Tunnel 2 sarà stato aggiunto.

    ![scenario 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

11. Assicurati che il **Kill Switch** di Tunnel 2 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verrà bloccato per prevenire DNS leak e tracciamento IP.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

12. Fai clic sull'icona dell'ingranaggio in alto a destra e abilita **Enhanced Kill Switch**. Questo garantisce che tutto il traffico debba accedere a Internet tramite VPN.

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

13. Fai clic sul pulsante centrale per attivare Tunnel 1 e Tunnel 2.

    ![scenario 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

14. Una volta connesso, la pagina mostrerà i dettagli della connessione VPN, inclusi VPN policy, statistiche del traffico, indirizzo del server, porta di ascolto e indirizzo IP virtuale.

    ![scenario 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

    Ora tutti i dispositivi useranno **VPN Tunnel 1** quando accedono ai domini specificati e useranno **VPN Tunnel 2** per tutto il resto dell'accesso a Internet. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verrà bloccato per prevenire DNS leak e tracciamento IP.

## All Other Traffic

Fai clic sull'icona dell'ingranaggio in alto a destra per configurare la policy del traffico che non corrisponde ai tunnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Questa policy controlla se il traffico che non corrisponde a nessuno dei gruppi di tunnel VPN può accedere a Internet oppure no. Ha due opzioni: **Allow Non-VPN Traffic** e **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: è abilitato per impostazione predefinita per garantire il normale accesso a Internet al traffico non VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: obbliga tutti i dispositivi ad accedere a Internet tramite VPN. Qualsiasi traffico che non corrisponde a un tunnel VPN verrà bloccato. Questa impostazione globale non sovrascrive il Kill Switch configurato per i singoli tunnel VPN.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel Priority

Per regolare la priorità dei tunnel, fai clic sull'icona dell'ingranaggio in un gruppo tunnel e seleziona **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Fai clic e tieni premuta l'icona a tre linee sulla destra per riordinare i tunnel, poi fai clic su **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Quando sono abilitati più tunnel, il router instrada il traffico secondo le seguenti regole**:

1. Il traffico tenterà prima di corrispondere alla regola del tunnel con priorità più alta. Se corrisponde, verrà instradato attraverso quel tunnel; altrimenti proverà il tunnel con priorità successiva e così via.

2. Ogni gruppo tunnel opera in modo indipendente. Una volta che il traffico corrisponde a una regola di tunnel, verrà instradato attraverso quel tunnel e non effettuerà failover tra gruppi tunnel.

3. All'interno di ciascun gruppo tunnel possono essere selezionati più profili per abilitare il failover intra-tunnel. Quando il profilo con priorità più alta in un gruppo tunnel non è disponibile, il tunnel si connetterà automaticamente usando il profilo con priorità immediatamente successiva, e così via.

4. Se un tunnel VPN si disconnette inaspettatamente, il sistema determinerà se fare failover del traffico verso il tunnel All Other Traffic in base al fatto che il **Kill Switch** di questo tunnel sia abilitato.

    - Se il Kill Switch è abilitato, il traffico verrà bloccato e non farà failover verso il tunnel All Other Traffic.
    - Se il Kill Switch è disabilitato, il traffico farà failover verso il tunnel All Other Traffic.

5. Nel tunnel **All Other Traffic**, modalità diverse determinano se il traffico che non corrisponde ai tunnel VPN può accedere a Internet.

    - **Allow Non-VPN Traffic**: è abilitato per impostazione predefinita per garantire che il traffico che non corrisponde ai tunnel VPN possa comunque accedere a Internet tramite WAN locale.

    - **Enhanced Kill Switch**: obbliga tutti i dispositivi ad accedere a Internet tramite VPN. Qualsiasi traffico che non corrisponde a un tunnel VPN verrà bloccato. Questa impostazione globale non sovrascrive il Kill Switch configurato per i singoli tunnel VPN. In breve, rafforza il Kill Switch e blocca il normale accesso a Internet per prevenire perdite di IP.

## Tunnel Options

Puoi configurare impostazioni avanzate per ciascun tunnel VPN, come VPN Kill Switch, IP Masquerading e MTU.

Fai clic sull'icona dell'ingranaggio in un gruppo tunnel e seleziona **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, il traffico che corrisponde a questo tunnel VPN verrà bloccato se la connessione VPN fallisce inaspettatamente. Se disabilitato, tale traffico farà failover verso il tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione è disabilitata per impostazione predefinita, poiché questi servizi richiedono normalmente il reale indirizzo IP del dispositivo per funzionare correttamente.

- **Allow Remote Access to the LAN Subnet**: se abilitato, sarà consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite la VPN. Richiede che il server VPN pubblichi una route di ritorno verso la propria subnet LAN.

- **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilitalo solo per configurazioni Site-to-Site in cui il peer remoto conosce già le tue subnet LAN.

- **MTU**: il valore MTU impostato per il tunnel sovrascriverà le impostazioni MTU nel file di configurazione.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
