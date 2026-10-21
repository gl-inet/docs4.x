# VPN Dashboard (Firmware v4.8) {#vpn-dashboard-firmware-v48}

Il contenuto di questa pagina si basa sulla versione firmware v4.8.x. Se il dispositivo esegue una versione firmware diversa, usa il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Versione firmware" data-placeholder="Firmware v4.8" markdown="1">

- [Firmware v4.7 e precedenti](vpn_dashboard_v4.7.md)
- [Firmware v4.9 e successivi](vpn_dashboard.md)

</div>

---
Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **VPN Dashboard**.

Il VPN dashboard mostra i dettagli della connessione VPN, come regole del tunnel, indirizzo del server, statistiche del traffico, IP virtuale del client e log di connessione, e consente di configurare impostazioni avanzate come VPN Kill Switch, IP Masquerading e MTU.

Puoi anche attivare più connessioni VPN per scenari multi-tunnel.

## Procedura guidata di configurazione {#setup-wizard}

Fai clic sull'icona del libro in alto a sinistra e segui VPN Setup Wizard per completare rapidamente la configurazione VPN.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Nota**: VPN Setup Wizard è disponibile solo per i servizi VPN integrati, inclusi AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA e Surfshark. Per altri servizi VPN, salta la procedura guidata e vai su [OpenVPN Client](openvpn_client.md){target="_blank"} oppure [WireGuard Client](wireguard_client.md){target="_blank"} per configurare manualmente la VPN.

Ecco un esempio con **Hide.me**. Effettua il login con le credenziali Hide.me.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Seleziona un server VPN e fai clic su **Apply**. Questo è il server a cui ti collegherai tramite questo tunnel VPN e il tuo indirizzo IP pubblico sembrerà provenire dalla posizione del server selezionato.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

La connessione verrà avviata automaticamente. Una volta connesso correttamente, vai al VPN Dashboard e vedrai che un VPN Tunnel è stato abilitato.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Vengono mostrati il protocollo VPN attualmente in uso, ad esempio WireGuard, il file di configurazione, l'indirizzo del server, la porta di ascolto del server, le statistiche del traffico e l'IP virtuale del client. Gli utenti possono visualizzare il log di connessione in basso a destra.

Tutti i client connessi accederanno a Internet tramite questo tunnel VPN.

Se vuoi configurare la policy VPN, fai riferimento a [Policy Mode](#policy-mode).

## Modalità VPN {#vpn-mode}

Nel VPN Dashboard, fai clic sul pulsante nell'angolo in alto a destra per cambiare modalità VPN.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Sono disponibili due modalità: **Global Mode** e **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Global Mode {#global-mode}

In questa modalità, tutto il traffico viene instradato attraverso il tunnel VPN e può essere attivata una sola istanza client VPN.

È ideale per gli scenari in cui tutto il traffico dei client deve passare attraverso un singolo server VPN, ad esempio per sicurezza di rete unificata o accesso a contenuti specifici per regione.

Nell'esempio seguente, il router si connette a un server australiano usando il protocollo WireGuard. Tutto il traffico dei client connessi verrà instradato attraverso questo tunnel VPN.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

#### Tunnel Options {#tunnel-options}

Puoi configurare impostazioni avanzate per il tunnel VPN, come VPN Kill Switch, IP Masquerading e MTU.

Fai clic sull'icona dell'ingranaggio nell'angolo in alto a destra.

![global mode options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options1.png){class="glboxshadow"}

![global mode options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, tutto il traffico instradato attraverso questo tunnel VPN verrà bloccato automaticamente se la connessione VPN fallisce. Se disabilitato, il traffico tornerà alla WAN locale e accederà a Internet senza passare attraverso il tunnel VPN.

- **Services from GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione è disabilitata per impostazione predefinita, poiché questi servizi di norma richiedono il reale indirizzo IP del dispositivo per funzionare correttamente.

- **Allow Remote Access the LAN Subnet**: se abilitato, sarà consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite VPN. Il server VPN deve pubblicizzare una route verso la subnet LAN di questo router.

- **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni Site-to-Site in cui il peer remoto conosce le tue subnet LAN.

- **MTU**: abbreviazione di Maximum Transmission Unit. Il valore MTU impostato per il tunnel sovrascriverà il valore definito nel file di configurazione.

### Policy Mode {#policy-mode}

In questa modalità, il router può connettersi a più server VPN e puoi personalizzare le regole di instradamento per diversi client o destinazioni del traffico.

È adatta ai casi d'uso che richiedono una gestione flessibile del traffico, ad esempio instradare traffici diversi verso destinazioni diverse attraverso più server VPN.

Passa la modalità VPN su Policy Mode e fai clic su **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Dopo il passaggio, se la VPN non è abilitata, la pagina viene mostrata come di seguito, con tre sezioni: Primary Tunnel, Add Tunnel e All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Fai clic sulla sezione corrispondente per saperne di più.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Primary Tunnel {#primary-tunnel}

Il primary tunnel è un tunnel <u>preimpostato</u> in Policy Mode. Ha la priorità più alta e puoi modificare la [tunnel priority](#tunnel-priority) se esiste più di un tunnel.

In questo tunnel puoi personalizzare la regola del tunnel impostando tre fattori:

1. **From**: si riferisce all'origine del traffico, cioè al traffico che deve essere instradato tramite questo tunnel.

    Fai clic sulla casella grigia per selezionare l'origine del traffico.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients**: se selezionato, il traffico di tutti i dispositivi corrisponderà a questa regola.

        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: se selezionato, il traffico dei tipi di connessione specificati, ad esempio LAN subnet, Drop-in Gateway, Guest Network, corrisponderà a questa regola.

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Se hai abilitato OpenVPN server o WireGuard server su questo router, ci saranno più opzioni sotto Specified Connection Types. Questo è utile per [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, corrisponderà a questa regola.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, **NON** corrisponderà a questa regola.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: si riferisce alle destinazioni del traffico.

    Fai clic sulla casella grigia per selezionare le destinazioni del traffico.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso tutte le destinazioni.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.

        Tieni presente che specificare un <u>dominio radice</u> includerà tutti i suoi sottodomini. Ad esempio, se vuoi specificare `archive.ubuntu.com`, `security.ubuntu.com` e `old-releases.ubuntu.com` in un tunnel, ti basta specificare il dominio radice `ubuntu.com`.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Oppure cambia **Input Mode** da Manual a Subscription URL e inserisci il link URL.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Specificare un dominio radice includerà tutti i suoi sottodomini.

            - Se selezioni Subscribe URL, il dominio o IP nell'URL viene aggiornato automaticamente ogni giorno.

            - Assicurati di inserire l'URL corretto. Il rilevamento URL verificherà la validità del dominio o dell'indirizzo IP. [Scopri di più](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola **NON** verrà instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.

        Tieni presente che specificare un <u>dominio radice</u> includerà tutti i suoi sottodomini. Ad esempio, se vuoi specificare `archive.ubuntu.com`, `security.ubuntu.com` e `old-releases.ubuntu.com` in un tunnel, ti basta specificare il dominio radice `ubuntu.com`.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Oppure cambia **Input Mode** da Manual a Subscription URL e inserisci il link URL.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Specificare un dominio radice includerà tutti i suoi sottodomini.

            - Se selezioni Subscribe URL, il dominio o IP nell'URL viene aggiornato automaticamente ogni giorno.

            - Assicurati di inserire l'URL corretto. Il rilevamento URL verificherà la validità del nome di dominio o dell'indirizzo IP. [Scopri di più](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: si riferisce al metodo di instradamento del traffico, cioè se usare o meno la VPN.

    Fai clic sulla casella grigia per selezionare il metodo di instradamento.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso le destinazioni selezionate tramite VPN.

        Per cominciare, devi configurare il router come VPN client. Usa [VPN Setup Wizard](#setup-wizard) per completare rapidamente la configurazione, oppure vai a OpenVPN Client / WireGuard Client nella barra laterale sinistra per configurarlo manualmente.

        Una volta impostato il router come VPN client, seleziona un file di configurazione VPN per questo tunnel e fai clic su **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: se selezionato, il traffico che corrisponde a questa regola verrà instradato verso le destinazioni selezionate tramite WAN locale invece che tramite VPN.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Dopo aver selezionato origine del traffico, destinazione e metodo di instradamento, la configurazione della regola del primary tunnel è completa.

Nell'esempio seguente, la regola del Primary Tunnel è: tutti i client usano la VPN per accedere a domini specificati. Il loro traffico viene instradato attraverso il server australiano ed esce verso i domini Internet selezionati tramite questo tunnel.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Nota**: per motivi di sicurezza, vai su [All Other Traffic](#all-other-traffic) e [Tunnel Options](#tunnel-options_1) per controllare altre impostazioni prima di abilitare i tunnel.

#### Add Tunnel {#add-tunnel}

Per creare tunnel aggiuntivi per più istanze VPN, fai clic su **Add Tunnel** sotto il Primary Tunnel e configura regole personalizzate.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Assegna un nome al tunnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Otterrai un tunnel in più sul VPN Dashboard.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Puoi aggiungere altri tunnel se necessario. È possibile creare fino a 5 tunnel, incluso il primary tunnel preimpostato.

Personalizza le regole del tunnel impostando origine del traffico, destinazioni e metodo di instradamento. Fai riferimento a [Primary Tunnel](#primary-tunnel).

**Nota**: per motivi di sicurezza, vai su [All Other Traffic](#all-other-traffic) e [Tunnel Options](#tunnel-options_1) per controllare altre impostazioni prima di abilitare i tunnel.

#### All Other Traffic {#all-other-traffic}

In Policy Mode, un tunnel <u>pre-abilitato</u> viene mostrato nella parte inferiore del VPN Dashboard.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Questo tunnel controlla se il traffico che non corrisponde a nessuno dei gruppi di tunnel VPN precedenti può accedere a Internet. È abilitato per impostazione predefinita per garantire il normale accesso a Internet al traffico non instradato tramite VPN.

- Quando è abilitato, il traffico non corrispondente può comunque accedere a Internet.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Quando è disabilitato, solo il traffico instradato tramite VPN può accedere a Internet. Tutto il traffico non VPN e il traffico che effettua failover dalle connessioni VPN verrà bloccato. Questa opzione non sovrascrive il Kill Switch individuale di ciascun tunnel VPN.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Tunnel Priority {#tunnel-priority}

Per impostazione predefinita, il Primary Tunnel preimpostato ha la priorità più alta, seguito dagli altri tunnel aggiunti manualmente, se presenti, e infine dal tunnel All Other Traffic per garantire la connettività della rete locale tramite WAN locale.

Per modificare la priorità dei tunnel, fai clic su **Modify Priority** nella barra informativa superiore, oppure fai clic sull'**etichetta di priorità** in alto a sinistra di qualsiasi tunnel, ad esempio Priority 1 o Priority 2.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Fai clic e tieni premuta l'icona a tre linee sulla destra per riordinare i tunnel, quindi fai clic su **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Quando sono abilitati più tunnel, il router instraderà il traffico nel seguente ordine**:

1. Il traffico tenterà prima di corrispondere alla regola del tunnel con priorità più alta. Se corrisponde, verrà instradato attraverso quel tunnel; altrimenti proverà il tunnel con priorità successiva, e così via, fino a raggiungere il tunnel "All Other Traffic".

2. Se un tunnel VPN si disconnette inaspettatamente, il sistema determinerà se eseguire il failover del traffico verso il tunnel con priorità successiva in base al fatto che il **Kill Switch** di quel tunnel sia abilitato.

    - Se il Kill Switch è abilitato, il traffico verrà bloccato e non effettuerà failover verso il tunnel successivo.
    - Se il Kill Switch è disabilitato, il traffico effettuerà failover verso il tunnel successivo e tenterà di corrispondere alle sue regole.

3. Il tunnel **All Other Traffic** è abilitato per impostazione predefinita per garantire che il traffico che non corrisponde ai tunnel VPN possa comunque accedere a Internet.

    - Se abilitato, instrada il traffico non corrispondente o in failover tramite WAN locale.
    - Se disabilitato, rafforza il Kill Switch e blocca il normale accesso a Internet per prevenire perdite di IP.

#### Tunnel Options {#tunnel-options_1}

Puoi configurare impostazioni avanzate per ciascun tunnel VPN, come VPN Kill Switch, IP Masquerading e MTU.

Fai clic sull'icona dell'ingranaggio accanto al nome del tunnel e seleziona **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, tutto il traffico instradato attraverso questo tunnel VPN verrà bloccato automaticamente se la connessione VPN fallisce. Se disabilitato, il traffico effettuerà failover verso il tunnel successivo in priorità oppure verso la WAN locale.

- **Services from GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione è disabilitata per impostazione predefinita, poiché questi servizi di norma richiedono il reale indirizzo IP del dispositivo per funzionare correttamente.

- **Allow Remote Access the LAN Subnet**: se abilitato, sarà consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite VPN. Il server VPN deve pubblicizzare una route verso la subnet LAN di questo router.

- **IP Masquerading**: se abilitato, gli indirizzi IP sorgente dei client LAN verranno riscritti con l'IP del tunnel VPN del router. Disabilita questa opzione solo per configurazioni Site-to-Site in cui il peer remoto conosce le tue subnet LAN.

- **MTU**: abbreviazione di Maximum Transmission Unit. Il valore MTU impostato per il tunnel sovrascriverà il valore definito nel file di configurazione.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
