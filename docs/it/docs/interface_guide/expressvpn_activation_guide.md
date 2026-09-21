# Guida all'attivazione di ExpressVPN

**Nota:** Questa guida si applica solo al router co-branded GL.iNet x ExpressVPN **Fortify (GL-MT6000)**.

---

[ExpressVPN](https://www.expressvpn.com/){target="_blank"} è uno dei servizi VPN premium leader a livello mondiale progettato per proteggere la tua privacy online, proteggere la tua connessione Internet e consentire lo streaming sicuro da qualsiasi luogo. Offre velocità elevatissime, crittografia di livello militare e accesso a server in oltre 100 paesi. Che tu voglia eseguire lo streaming, navigare in privato o proteggere i tuoi dati sul Wi-Fi pubblico, ExpressVPN ti offre un'esperienza veloce e sicura.

**Fortify (GL-MT6000)** è un router in co-branding rilasciato congiuntamente da GL.iNet ed ExpressVPN. Ogni unità viene fornita con un abbonamento ExpressVPN gratuito di un anno. Gli utenti possono riscattare l'abbonamento e connettere i propri account direttamente sul pannello di amministrazione web del router. Una volta attivato, tutto il traffico che passa attraverso il router sfrutterà la rete ad alta velocità di ExpressVPN e la solida crittografia per proteggere l'intera connessione di rete e la privacy online.

Questa guida ti guida attraverso il riscatto del piano ExpressVPN di 12 mesi nel pannello di amministrazione web del router. Copre anche la personalizzazione delle policy VPN in base ai tuoi scenari e requisiti di utilizzo, aiutandoti a usufruire senza sforzo di una connettività Internet crittografata, sicura e ad alta velocità.

## Riscatta il piano ExpressVPN

Accedi al pannello di amministrazione web di Fortify e vai a **VPN** -> **VPN Client Profile**.

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/vpn_client_profile.png){class="glboxshadow"}

Leggi e accetta **Terms of Service** e **Privacy Policy**, quindi fai clic su **Get Started**.

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/get_started.png){class="glboxshadow"}

Fare clic su **Claim 12-Month Plan**.

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/claim_plan.png){class="glboxshadow"}

Nella finestra pop-up, inserisci il tuo **Order ID**. Se hai acquistato questo router da GL.iNet Store, è inoltre richiesto **Order Email**. Quindi fare clic su **Continue to ExpressVPN**.

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/store_order_email.png){class="glboxshadow"}

Verrai indirizzato al pagamento di ExpressVPN. È stato applicato un codice di riscatto sul diritto di attivare l'abbonamento di 12 mesi senza costi aggiuntivi.

Inserisci il tuo indirizzo email in alto e aggiungi il metodo di pagamento per garantire un accesso VPN ininterrotto alla fine del periodo iniziale. Quindi fare clic su **Subscribe with Card**.

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout1.png){class="glboxshadow"}

Il tuo piano è stato attivato. Torna al pannello di amministrazione web del tuo router Fortify per accedere con il tuo account.

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout2.png){class="glboxshadow"}

## Accedi a ExpressVPN

Nel pannello di amministrazione web di Fortify, vai su **VPN** -> **VPN Client Profile**.

Fai clic su **Log in to ExpressVPN** e verrai indirizzato alla pagina di accesso sicuro di ExpressVPN.

![expressvpn login 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login1.png){class="glboxshadow"}

Inserisci la tua email e fai clic su **Send Code**. Un codice di verifica di 6 cifre verrà inviato alla tua email.

![expressvpn login 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login2.png){class="glboxshadow"}

Inserisci il codice di verifica e fai clic su **Continue**.

![expressvpn login 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login3.png){class="glboxshadow"}

Cambia la tua password per attivare il tuo account.

![expressvpn login 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login4.png){class="glboxshadow"}

Nel passaggio successivo, fai clic su **Yes** per autorizzare l'accesso a ExpressVPN sul tuo router.

![expressvpn login 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login5.png){class="glboxshadow"}

Accesso riuscito. Puoi chiudere questa finestra del browser e tornare al tuo dispositivo.

![expressvpn login 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login6.png){class="glboxshadow"}

Nel pannello di amministrazione web di Fortify, vai su **VPN** -> **VPN Client Profile**.

Hai effettuato l'accesso a ExpressVPN su questo router. Fare clic su **Go to ExpressVPN Dashboard**.

![expressvpn signed in](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_signed_in.png){class="glboxshadow"}

Ora puoi aggiungere tunnel VPN e configurare le policy VPN in base alle tue esigenze.

![expressvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_dashboard.png){class="glboxshadow"}

## Aggiungi tunnel VPN

### Passaggi generali

Segui i passaggi seguenti per aggiungere il tuo tunnel VPN e configurare i criteri VPN. Se necessario, vedere [Riferimento caso](#case-reference).

1. Nel pannello di amministrazione web di Fortify, vai su **VPN** -> **ExpressVPN Dashboard**. Fare clic su **Add VPN Tunnel**.

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. Seleziona il profilo VPN, quindi fai clic su **Next**.

    Otterrai un elenco di profili ExpressVPN. Seleziona uno o più profili e regola la loro priorità a destra secondo necessità.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        Quando vengono selezionati più profili, il tunnel tenterà di connettersi utilizzando ciascun profilo in ordine di priorità finché la connessione non verrà stabilita correttamente. Se tutti i profili all'interno di un singolo tunnel non riescono a connettersi, il sistema determinerà se passare alla rete locale del router (WAN) in base allo stato del Kill Switch nelle impostazioni [Opzioni tunnel](#tunnel-options) e [Tutto l'altro traffico](#all-other-traffic).

3. Selezionare l'origine client, quindi fare clic su **Next**.

    Ci sono quattro opzioni:

    - **All Clients**: se selezionato, il traffico proveniente da tutti i dispositivi corrisponderà a questa regola.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types**: se selezionato, il traffico proveniente dai tipi di connessione specificati (ad esempio sottorete LAN, Drop-in Gateway o rete ospite) corrisponderà a questa regola.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices**: se selezionato, il traffico proveniente dai dispositivi specificati (identificati dall'indirizzo MAC) corrisponderà a questa regola.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: se selezionato, il traffico proveniente dai dispositivi specificati (identificati dall'indirizzo MAC) non corrisponderà a questa regola.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. Selezionare la destinazione di destinazione, quindi fare clic su **Apply**.

    Ci sono tre opzioni:

    - **All Targets**: se selezionato, il traffico corrispondente a questa regola verrà instradato a tutti i target.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: se selezionato, il traffico corrispondente a questa regola verrà instradato ai domini o agli indirizzi IP specificati. È necessario inserirli manualmente.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: se selezionato, il traffico corrispondente a questa regola non verrà instradato ai domini o agli indirizzi IP specificati. È necessario inserirli manualmente.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. Un tunnel VPN è stato aggiunto correttamente. Verrai indirizzato allo **ExpressVPN Dashboard**. Aggiungi altri tunnel VPN se necessario.

### Riferimento al caso

Di seguito sono riportati due casi tipici di configurazione della policy VPN con istruzioni dettagliate per la configurazione come riferimento.

??? note "Caso 1: instradare tramite VPN solo i dispositivi specificati."

    **Requisiti:**

    1. Solo dispositivi specifici collegati a questo router accedono a Internet tramite la VPN. Tutti gli altri dispositivi accedono a Internet tramite la WAN locale.

    2. I dispositivi selezionati devono utilizzare solo la connessione VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verrà bloccato per prevenire perdite DNS e tracciamento IP.

    **Passaggi di configurazione:**

    1. Seleziona il profilo VPN.

        Seleziona uno o più profili e regola la loro priorità a destra secondo necessità, quindi fai clic su **Next**.

        ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

    2. Seleziona l'origine del cliente.

        Fai clic sulla scheda **Specified Devices**, seleziona i dispositivi su cui desideri utilizzare la VPN, quindi fai clic su **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

    3. Seleziona la destinazione di destinazione.

        Fare clic sulla scheda **All Targets**, impostarla come destinazione del traffico, quindi fare clic su **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

    4. Verrai indirizzato alla dashboard di ExpressVPN. Ora un tunnel VPN è stato aggiunto correttamente.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

    5. Assicurati che **Kill Switch** per questo tunnel sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico corrispondente a questo tunnel verrà bloccato per impedire perdite DNS e tracciamento IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}

    6. Assicurati che **Allow Non-VPN Traffic** sia abilitato. Questa opzione è abilitata per impostazione predefinita per garantire che il traffico che non corrisponde al tunnel VPN possa comunque accedere a Internet tramite la rete WAN locale.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

    7. Fare clic sul pulsante centrale per attivare questo tunnel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

    8. Una volta connesso, la pagina visualizzerà i dettagli della connessione VPN, inclusi criteri VPN, IP virtuale del client, indirizzo del server, porta di ascolto e statistiche sul traffico.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

        Ora solo due dispositivi specificati accedono a Internet tramite VPN. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per questi dispositivi verrà bloccato per prevenire perdite DNS e tracciamento IP. Tutti gli altri dispositivi accederanno invece a Internet tramite la rete WAN locale.

??? note "Caso 2: instradare tutti i dispositivi tramite VPN 1 per siti specifici e tutto il traffico rimanente tramite VPN 2."

    **Requisiti:**

    1. Tutti i dispositivi utilizzano VPN Tunnel 1 quando accedono a siti Web di specifici social media e servizi di streaming e utilizzano VPN Tunnel 2 per tutto il resto dell'accesso a Internet.

    2. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verrà bloccato per impedire perdite DNS e tracciamento IP.

    **Passaggi di configurazione:**

    1. Seleziona il profilo VPN per Tunnel 1.

        Seleziona uno o più profili e regola la loro priorità a destra secondo necessità, quindi fai clic su **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

    2. Seleziona l'origine del cliente.

        Fare clic sulla scheda **All Clients**, impostarla come origine client per Tunnel 1, quindi fare clic su **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    3. Seleziona la destinazione di destinazione.

        Fai clic sulla scheda **Specified Domain / IP List**, inserisci i domini di social media e servizi di streaming specifici, come mostrato di seguito, quindi fai clic su **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

    4. Verrai indirizzato alla dashboard di ExpressVPN. Ora il tunnel VPN 1 è stato aggiunto con successo.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

    5. Assicurati che **Kill Switch** per Tunnel 1 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico corrispondente a questo tunnel verrà bloccato per impedire perdite DNS e tracciamento IP.

        ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

        ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}

    6. Fare clic su **Add New Tunnel** per aggiungere Tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

    7. Seleziona il profilo VPN per Tunnel 2.

        Seleziona uno o più profili e regola la loro priorità a destra secondo necessità, quindi fai clic su **Next**.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

    8. Seleziona l'origine del cliente.

        Fare clic sulla scheda **All Clients**, impostarla come origine client per Tunnel 2, quindi fare clic su **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    9. Seleziona la destinazione di destinazione.

        Fai clic sulla scheda **All Targets**, impostala come destinazione del traffico per il Tunnel 2, quindi fai clic su **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

    10. Verrai indirizzato alla dashboard della VPN. Ora il tunnel VPN 2 è stato aggiunto con successo.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

    11. Assicurati che **Kill Switch** per Tunnel 2 sia abilitato. Se la VPN si disconnette inaspettatamente, l'accesso a Internet per il traffico corrispondente a questo tunnel verrà bloccato per impedire perdite DNS e tracciamento IP.

        ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

        ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

    12. Fai clic sull'icona a forma di ingranaggio in alto a destra, attiva **Enhanced Kill Switch**, quindi fai clic su **Apply**. Ciò garantisce che tutto il traffico possa raggiungere Internet solo tramite VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

        Una volta applicato, **Enhanced Kill Switch** apparirà nella parte superiore della pagina.

        ![enhanced killswitch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch3.png){class="glboxshadow"}

    13. Fare clic sul pulsante centrale per attivare Tunnel 1 e Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

    14. Una volta connesso, la pagina visualizzerà i dettagli della connessione VPN, inclusi criteri VPN, IP virtuale del client, indirizzo del server, porta di ascolto e statistiche sul traffico.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

        Ora tutti i dispositivi utilizzeranno **VPN Tunnel 1** quando accedono a domini specifici e utilizzeranno **VPN Tunnel 2** per tutti gli altri accessi a Internet. Se i tunnel VPN si disconnettono inaspettatamente, l'accesso a Internet per tutti i dispositivi verrà bloccato per impedire perdite DNS e tracciamento IP.

## Kill Switch

Kill Switch è una funzionalità di sicurezza per le connessioni VPN. Interrompe automaticamente tutti gli accessi a Internet per la tua rete locale se la connessione VPN si interrompe inaspettatamente, impedendo che il tuo indirizzo IP reale e i tuoi dati online vengano esposti e garantendo privacy e sicurezza continue. Questa funzionalità è particolarmente utile per mantenere un accesso Internet sicuro e anonimo, ad esempio quando si utilizzano reti pubbliche, si elaborano dati sensibili o si nasconde il proprio indirizzo IP reale.

Se abilitato, blocca qualsiasi traffico client che tenta di bypassare il tunnel VPN, bloccando in modo efficace le perdite VPN causate da problemi di configurazione DNS, disconnessioni impreviste, richieste IP dirette e altri scenari simili.

Fortify supporta la configurazione Kill Switch per la connessione VPN globale, nonché per ogni singolo tunnel VPN.

- Per impostare il Kill Switch per la connessione VPN globale (ovvero Enhanced Kill Switch), fare riferimento a [Tutto il resto del traffico](#all-other-traffic).

- Per impostare il Kill Switch per ogni singolo tunnel VPN, fare riferimento a [Opzioni tunnel](#tunnel-options).

## Tutto il resto del traffico

Fai clic sull'icona a forma di ingranaggio in alto a destra per impostare la policy per il traffico che non corrisponde al tunnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

Questa policy controlla se il traffico che non corrisponde a nessuno dei tuoi gruppi di tunnel VPN può accedere a Internet o meno. Due opzioni disponibili: **Allow Non-VPN Traffic** e **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: abilitato per impostazione predefinita per garantire il normale accesso a Internet per il traffico non VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: forza tutti i dispositivi ad accedere a Internet tramite una VPN. Tutto il traffico che non corrisponde a un tunnel VPN verrà bloccato. Questa impostazione globale non sovrascrive il Kill Switch configurato per i singoli tunnel VPN.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## Opzioni del tunnel

Puoi configurare impostazioni avanzate per ciascun tunnel VPN, come VPN Kill Switch, IP Masquerading e MTU.

Fare clic sull'icona a forma di ingranaggio in un gruppo di tunnel e selezionare **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, il traffico corrispondente a questo tunnel VPN verrà bloccato se la connessione VPN fallisce inaspettatamente. Se disabilitato, tale traffico eseguirà il failover sul tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: se abilitati, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso tunnel VPN. Questa opzione è disabilitata per impostazione predefinita, poiché questi servizi normalmente richiedono l'indirizzo IP reale del dispositivo per funzionare correttamente.

- **Allow Remote Access to the LAN Subnet**: se abilitato, sarà consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite VPN. Richiede al server VPN di pubblicizzare un percorso di ritorno alla sua sottorete LAN.

- **IP Masquerading**: se abilitato, gli indirizzi IP di origine dei client LAN verranno riscritti nell'IP del tunnel VPN del router. Disabilitalo solo per le configurazioni da sito a sito in cui il peer remoto conosce le tue sottoreti LAN.

- **MTU**: il valore MTU impostato per il tunnel sovrascriverà le impostazioni MTU nel file di configurazione.

## Priorità al tunnel

Per regolare la priorità del tunnel, fai clic sull'icona a forma di ingranaggio in un gruppo di tunnel e seleziona **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

Fare clic e tenere premuta l'icona a tre righe sulla destra per riordinare i tunnel, quindi fare clic su **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

**Quando sono abilitati più tunnel, il router instrada il traffico secondo le regole seguenti**:

1. Il traffico tenterà innanzitutto di soddisfare la regola del tunnel con la priorità più alta. Se abbinato, verrà instradato attraverso quel tunnel; altrimenti proverà con il tunnel con priorità successiva e così via.

2. Ogni gruppo di tunnel opera in modo indipendente. Una volta che il traffico corrisponde a una regola del tunnel, verrà instradato attraverso quel tunnel e non verrà eseguito il failover tra i gruppi di tunnel.

3. È possibile selezionare più profili all'interno di ciascun gruppo di tunnel per abilitare il failover intra-tunnel. Quando il profilo con la priorità più alta in un gruppo di tunnel viene interrotto, il tunnel si connetterà automaticamente utilizzando il secondo profilo con la priorità più alta e così via.

4. Se un tunnel VPN si disconnette inaspettatamente, il sistema determinerà se eseguire il failover del traffico verso il tunnel Tutto l'altro traffico a seconda che **Kill Switch** di questo tunnel sia abilitato.

    - Se il Kill Switch è abilitato, il traffico verrà bloccato e non verrà eseguito il failover sul tunnel Tutto il resto del traffico.
    - Se il Kill Switch è disabilitato, il traffico eseguirà il failover nel tunnel Tutto il resto del traffico.

5. Nel tunnel **All Other Traffic**, diverse modalità determinano se il traffico che non corrisponde al tunnel VPN può accedere a Internet.

    - **Allow Non-VPN Traffic**: è abilitato per impostazione predefinita per garantire che il traffico che non corrisponde ai tunnel VPN possa comunque accedere a Internet tramite WAN locale.

    - **Enhanced Kill Switch**: forza tutti i dispositivi ad accedere a Internet tramite una VPN. Tutto il traffico che non corrisponde a un tunnel VPN verrà bloccato. Questa impostazione globale non sovrascrive il Kill Switch configurato per i singoli tunnel VPN. In breve, rafforza il Kill Switch e blocca l’accesso regolare a Internet per prevenire perdite di IP.

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [Contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
