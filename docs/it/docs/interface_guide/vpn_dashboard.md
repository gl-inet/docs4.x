# VPN Dashboard {#vpn-dashboard}

Il contenuto di questa pagina si basa sulla versione firmware v4.9.x e successive. Se il dispositivo esegue una versione firmware diversa, usa il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Versione firmware" data-placeholder="Firmware v4.9 e successivi" markdown="1">

- [Firmware v4.7 e precedenti](vpn_dashboard_v4.7.md)
- [Firmware v4.8](vpn_dashboard_v4.8.md)

</div>

---

Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **VPN Dashboard**.

Il VPN Dashboard mostra i dettagli della connessione VPN, come regole di instradamento, server connesso, statistiche del traffico, IP virtuale del client e log di connessione, e consente di configurare impostazioni avanzate come il Kill Switch VPN, il mascheramento IP e l'MTU.

Rispetto al firmware v4.8, la v4.9 include i seguenti miglioramenti al VPN Dashboard:

1. **Consente di selezionare più profili all'interno di un gruppo di tunnel e di impostarne la priorità**. Il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità finché non viene stabilita correttamente una connessione.

2. **Ogni gruppo di tunnel opera in modo indipendente e non esegue il failover tra gruppi**. Se tutti i profili di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale in base allo stato del Kill Switch del tunnel e del tunnel All Other Traffic.

## Caricare un profilo VPN {#upload-vpn-profile}

Quando accedi a questa pagina per la prima volta, se non è stato creato alcun tunnel, la pagina appare come mostrato di seguito. Fai clic su **Add VPN Tunnel** per iniziare.

![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Verrai indirizzato alla pagina **VPN Client Profile**. Seleziona un provider VPN ed effettua il login.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. I provider VPN elencati nell'immagine precedente sono integrati nel pannello di amministrazione web del router GL.iNet. Con un abbonamento attivo, basta inserire le proprie credenziali per effettuare subito il login e ottenere i file di configurazione per le connessioni VPN.
    
    2. Se hai sottoscritto un abbonamento con altri provider VPN, oppure vuoi caricare configurazioni VPN personali, fai clic su **Add Manually** e carica le tue configurazioni.

Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Fai clic su PureVPN ed effettua il login con credenziali valide.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Otterrai un elenco di profili VPN. Per alcuni provider di servizi VPN, prima che venga mostrato l'elenco dei profili potrebbe essere necessario selezionare un protocollo VPN oppure server o città preferiti.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Fai clic su **Go to Dashboard** in basso. Verrai indirizzato al VPN Dashboard per aggiungere il tuo tunnel VPN e configurare i criteri VPN.

## Aggiungere un tunnel VPN {#add-vpn-tunnel}

### Procedura generale {#general-steps}

Segui i passaggi seguenti per aggiungere il tuo tunnel VPN e configurare i criteri VPN. Se necessario, consulta i [casi di riferimento](#case-reference).

1. Nel VPN Dashboard, fai clic su **Add VPN Tunnel**. Sulla destra si aprirà una procedura guidata di configurazione VPN.

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Seleziona il profilo VPN.

    Seleziona uno o più profili, regola la loro priorità sulla destra secondo necessità, quindi fai clic su **Next**.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Nota**: quando sono selezionati più profili, il tunnel tenterà di connettersi usando ciascun profilo in ordine di priorità finché non viene stabilita correttamente una connessione. Se tutti i profili di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla WAN locale del router in base allo stato del Kill Switch nelle impostazioni [Opzioni del tunnel](#tunnel-options) e [All Other Traffic](#all-other-traffic).

3. Seleziona l'origine client, quindi fai clic su **Next**.

    Sono disponibili quattro opzioni:

    - **All Clients**: se selezionato, il traffico di tutti i dispositivi corrisponderà a questa regola.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: se selezionato, il traffico dei tipi di connessione specificati (ad esempio subnet LAN, Drop-in Gateway, rete ospite) corrisponderà a questa regola.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: se selezionato, il traffico dei dispositivi specificati (identificati tramite indirizzo MAC) corrisponderà a questa regola.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: se selezionato, il traffico dei dispositivi specificati (identificati tramite indirizzo MAC) non corrisponderà a questa regola.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Seleziona la destinazione del traffico, quindi fai clic su **Apply**.

    Sono disponibili tre opzioni:

    - **All Targets**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso tutte le destinazioni.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso i domini o gli indirizzi IP specificati. Devi inserirli manualmente.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola non verrà instradato verso i domini o gli indirizzi IP specificati. Devi inserirli manualmente.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. Il tunnel VPN è stato aggiunto correttamente e verrai indirizzato al **VPN Dashboard**. Se necessario, aggiungi altri tunnel VPN.

    Per motivi di sicurezza, prima di attivare il tunnel VPN vai su [All Other Traffic](#all-other-traffic) e [Opzioni del tunnel](#tunnel-options) per verificare lo stato del **Kill Switch**.

### Casi di riferimento {#case-reference}

Di seguito trovi due casi tipici di configurazione dei criteri VPN, con istruzioni di configurazione passo passo.

??? note "Caso 1: instradare tramite VPN solo i dispositivi specificati."

    **Requisiti:**

    1. Solo dispositivi specifici collegati a questo router accedono a Internet tramite VPN. Tutti gli altri dispositivi accedono a Internet tramite la WAN locale.

    2. I dispositivi selezionati devono usare esclusivamente la connessione VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verrà bloccato per prevenire DNS leak e tracciamento dell'IP.

    **Passaggi di configurazione:**

    1. Seleziona il profilo VPN.

        Se hai effettuato il login con le credenziali di un servizio VPN integrato o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.

        Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili e regola la loro priorità sulla destra secondo necessità.

        ![case 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Seleziona l'origine client.

        Fai clic sulla scheda **Specified Devices**, seleziona i dispositivi che useranno la VPN, quindi fai clic su **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Seleziona la destinazione del traffico.

        Fai clic sulla scheda **All Targets**, impostala come destinazione del traffico, quindi fai clic su **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. Verrai indirizzato al VPN Dashboard. Il tunnel VPN è stato aggiunto correttamente, come mostrato di seguito.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Assicurati che il **Kill Switch** di questo tunnel sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verrà bloccato per prevenire DNS leak e tracciamento dell'IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}
        
    6. Assicurati che **Allow Non-VPN Traffic** sia abilitato. Questa opzione è abilitata per impostazione predefinita per garantire che il traffico che non corrisponde al tunnel VPN possa comunque accedere a Internet tramite la WAN locale.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Fai clic sul pulsante centrale per attivare questo tunnel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Una volta stabilita la connessione, la pagina mostrerà i dettagli della connessione VPN, inclusi criteri VPN, statistiche del traffico, indirizzo del server, porta di ascolto e indirizzo IP virtuale.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Ora solo i due dispositivi specificati accedono a Internet tramite VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verrà bloccato per prevenire DNS leak e tracciamento dell'IP. Tutti gli altri dispositivi accederanno invece a Internet tramite la WAN locale.

??? note "Caso 2: instradare tutti i dispositivi tramite la VPN 1 per siti web specifici e tutto il resto del traffico tramite la VPN 2."

    **Requisiti:**

    1. Tutti i dispositivi usano **VPN Tunnel 1** quando accedono ai domini di specifici servizi social e di streaming e usano **VPN Tunnel 2** per tutto il resto dell'accesso a Internet.

    2. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verrà bloccato per prevenire DNS leak e tracciamento dell'IP.

    **Passaggi di configurazione:**

    1. Seleziona il profilo VPN per il Tunnel 1.

        Se hai effettuato il login con le credenziali di un servizio VPN integrato o hai caricato un file di configurazione, i profili disponibili saranno elencati qui. Altrimenti, vai su **VPN Client Profile** per effettuare il login con le tue credenziali o caricare manualmente un file di configurazione.
        
        Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili, regola la loro priorità sulla destra secondo necessità, quindi fai clic su **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Seleziona l'origine client.

        Fai clic sulla scheda **All Clients**, impostala come origine client per il Tunnel 1, quindi fai clic su **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Seleziona la destinazione del traffico.

        Fai clic sulla scheda **Specified Domain / IP List**, inserisci i domini di alcuni servizi social e di streaming comuni, come mostrato di seguito, quindi fai clic su **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. Verrai indirizzato al VPN Dashboard. Il tunnel VPN 1 è stato aggiunto correttamente.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Assicurati che il **Kill Switch** del Tunnel 1 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verrà bloccato per prevenire DNS leak e tracciamento dell'IP.

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}
        
    6. Fai clic su **Add New Tunnel** per aggiungere il Tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Seleziona il profilo VPN per il Tunnel 2.

        Prendiamo [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} come esempio. Seleziona uno o più profili e regola la loro priorità sulla destra secondo necessità.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. Seleziona l'origine client.

        Fai clic sulla scheda **All Clients**, impostala come origine client per il Tunnel 2, quindi fai clic su **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. Seleziona la destinazione del traffico.

        Fai clic sulla scheda **All Targets**, impostala come destinazione del traffico per il Tunnel 2, quindi fai clic su **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. Verrai indirizzato al VPN Dashboard. Il tunnel VPN 2 è stato aggiunto correttamente.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Assicurati che il **Kill Switch** del Tunnel 2 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico che corrisponde a questo tunnel verrà bloccato per prevenire DNS leak e tracciamento dell'IP.

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Fai clic sull'icona dell'ingranaggio in alto a destra e abilita **Enhanced Kill Switch**. In questo modo tutto il traffico deve accedere a Internet tramite VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Fai clic sul pulsante centrale per attivare il Tunnel 1 e il Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Una volta stabilita la connessione, la pagina mostrerà i dettagli della connessione VPN, inclusi criteri VPN, statistiche del traffico, indirizzo del server, porta di ascolto e indirizzo IP virtuale.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Ora tutti i dispositivi useranno **VPN Tunnel 1** quando accedono ai domini specificati e **VPN Tunnel 2** per tutto il resto dell'accesso a Internet. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verrà bloccato per prevenire DNS leak e tracciamento dell'IP.

## Kill Switch {#kill-switch}

!!! Tip "Che cos'è il Kill Switch?"

    Il Kill Switch VPN aiuta a impedire che il traffico ricada su una connessione Internet non crittografata quando la connessione VPN si interrompe.

    Per un singolo tunnel, l'attivazione del **Kill Switch** blocca l'accesso a Internet del traffico assegnato a quel tunnel se la sua connessione si interrompe. Il resto del traffico segue le impostazioni di **All Other Traffic**.

    **Enhanced Kill Switch** blocca il traffico Internet che non corrisponde ad alcun tunnel VPN. Non sostituisce l'impostazione **Kill Switch** di ciascun tunnel.

Dalla versione firmware v4.8, i router GL.iNet consentono di configurare il Kill Switch per la connessione VPN globale e per ogni singolo tunnel VPN.

- Per configurare il Kill Switch per la connessione VPN globale (cioè l'Enhanced Kill Switch), consulta [All Other Traffic](#all-other-traffic).

- Per configurare il Kill Switch per ogni singolo tunnel VPN, consulta [Opzioni del tunnel](#tunnel-options).

## Tutto il resto del traffico {#all-other-traffic}

Fai clic sull'icona dell'ingranaggio in alto a destra per configurare i criteri per il traffico che non corrisponde ai tunnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Questi criteri controllano se il traffico che non corrisponde a nessuno dei gruppi di tunnel VPN può accedere o meno a Internet. Sono disponibili due opzioni: **Allow Non-VPN Traffic** ed **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: abilitato per impostazione predefinita per garantire il normale accesso a Internet al traffico non VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: obbliga tutti i dispositivi ad accedere a Internet tramite una VPN. Qualsiasi traffico che non corrisponde a un tunnel VPN verrà bloccato. Questa impostazione globale non sovrascrive il Kill Switch configurato per i singoli tunnel VPN.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Opzioni del tunnel {#tunnel-options}

Puoi configurare impostazioni avanzate per ciascun tunnel VPN, come il Kill Switch VPN, il mascheramento IP e l'MTU.

Fai clic sull'icona dell'ingranaggio in un gruppo di tunnel e seleziona **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, il traffico che corrisponde a questo tunnel VPN verrà bloccato se la connessione VPN si interrompe inaspettatamente. Se disabilitato, tale traffico passerà in failover al tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione è disabilitata per impostazione predefinita, poiché questi servizi richiedono normalmente l'indirizzo IP reale del dispositivo per funzionare correttamente.

- **Allow Remote Access to the LAN Subnet**: se abilitato, sarà consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite la VPN. Richiede che il server VPN annunci una route di ritorno verso la propria subnet LAN.

- **IP Masquerading**: se abilitato, gli indirizzi IP di origine dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni site-to-site in cui il peer remoto conosce le tue subnet LAN.

    Come mostrato di seguito, se il mascheramento IP è abilitato, quando il portatile (192.168.10.200) della LAN del router da viaggio invia traffico attraverso il tunnel al NAS di casa (192.168.8.100), il router da viaggio riscrive l'IP di origine da `192.168.10.200` all'indirizzo del tunnel del client VPN `10.1.0.2`, quindi il lato server vede il traffico come proveniente dal client anziché dalla LAN locale del client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/ip_masquerading.png){class="glboxshadow"}

- **MTU**: il valore MTU impostato per il tunnel sovrascriverà le impostazioni MTU del file di configurazione.

## Priorità dei tunnel {#tunnel-priority}

Per regolare la priorità dei tunnel, fai clic sull'icona dell'ingranaggio in un gruppo di tunnel e seleziona **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Fai clic e tieni premuta l'icona a tre linee sulla destra per riordinare i tunnel, quindi fai clic su **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Quando sono abilitati più tunnel, il router instrada il traffico secondo le seguenti regole**:

1. Il traffico tenterà prima di corrispondere alla regola del tunnel con priorità più alta. Se corrisponde, verrà instradato attraverso quel tunnel; altrimenti verrà verificato il tunnel con la priorità successiva, e così via.

2. Ogni gruppo di tunnel opera in modo indipendente. Una volta che il traffico corrisponde alla regola di un tunnel, verrà instradato attraverso quel tunnel e non passerà in failover tra gruppi di tunnel.

3. All'interno di ciascun gruppo di tunnel è possibile selezionare più profili per abilitare il failover all'interno del tunnel. Quando il profilo con priorità più alta di un gruppo di tunnel non è disponibile, il tunnel si connetterà automaticamente usando il profilo con la seconda priorità più alta, e così via.

4. Se un tunnel VPN si disconnette inaspettatamente, il sistema determinerà se far passare il traffico in failover al tunnel All Other Traffic in base al fatto che il **Kill Switch** di questo tunnel sia abilitato o meno.

    - Se il Kill Switch è abilitato, il traffico verrà bloccato e non passerà in failover al tunnel All Other Traffic.
    - Se il Kill Switch è disabilitato, il traffico passerà in failover al tunnel All Other Traffic.

5. Nel tunnel **All Other Traffic**, la modalità selezionata determina se il traffico che non corrisponde ai tunnel VPN può accedere a Internet.

    - **Allow Non-VPN Traffic**: è abilitato per impostazione predefinita per garantire che il traffico che non corrisponde ai tunnel VPN possa comunque accedere a Internet tramite la WAN locale.

    - **Enhanced Kill Switch**: obbliga tutti i dispositivi ad accedere a Internet tramite una VPN. Qualsiasi traffico che non corrisponde a un tunnel VPN verrà bloccato. Questa impostazione globale non sovrascrive il Kill Switch configurato per i singoli tunnel VPN. In breve, rafforza il Kill Switch e blocca il normale accesso a Internet per prevenire perdite dell'IP.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
