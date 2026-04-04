# VPN Dashboard

**Nota**: questa guida si basa sul firmware v4.8. Per le versioni precedenti, fai riferimento [qui](vpn_dashboard_v4.7.md).

---

Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **VPN Dashboard**.

Il VPN dashboard mostra i dettagli della connessione VPN, come regole del tunnel, indirizzo del server, statistiche del traffico, IP virtuale del client e log di connessione, e consente di configurare impostazioni avanzate come VPN Kill Switch, IP Masquerading e MTU.

Puoi anche attivare piu' connessioni VPN per scenari multi-tunnel.

## Procedura guidata di configurazione

Fai clic sull'icona del libro in alto a sinistra e segui VPN Setup Wizard per completare rapidamente la configurazione VPN.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Nota**: VPN Setup Wizard e' disponibile solo per i servizi VPN integrati, inclusi AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA e Surfshark. Per altri servizi VPN, salta la procedura guidata e vai su [OpenVPN Client](openvpn_client.md){target="_blank"} oppure [WireGuard Client](wireguard_client.md){target="_blank"} per configurare manualmente la VPN.

Ecco un esempio con **Hide.me**. Effettua il login con le credenziali Hide.me.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Seleziona un server VPN e fai clic su **Apply**. Questo e' il server a cui ti collegherai tramite questo tunnel VPN e il tuo indirizzo IP pubblico sembrera' provenire dalla posizione del server selezionato.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

La connessione verra' avviata automaticamente. Una volta connesso correttamente, vai al VPN Dashboard e vedrai che un VPN Tunnel e' stato abilitato.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Vengono mostrati il protocollo VPN attualmente in uso, ad esempio WireGuard, il file di configurazione, l'indirizzo del server, la porta di ascolto del server, le statistiche del traffico e l'IP virtuale del client. Gli utenti possono visualizzare il log di connessione in basso a destra.

Tutti i client connessi accederanno a Internet tramite questo tunnel VPN.

Se vuoi configurare la policy VPN, fai riferimento a [Policy Mode](#policy-mode).

## Modalita' VPN

Nel VPN Dashboard, fai clic sul pulsante nell'angolo in alto a destra per cambiare modalita' VPN.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Sono disponibili due modalita': **Global Mode** e **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Global Mode

In questa modalita', tutto il traffico viene instradato attraverso il tunnel VPN e puo' essere attivata una sola istanza client VPN.

E' ideale per gli scenari in cui tutto il traffico dei client deve passare attraverso un singolo server VPN, ad esempio per sicurezza di rete unificata o accesso a contenuti specifici per regione.

Nell'esempio seguente, il router si connette a un server australiano usando il protocollo WireGuard. Tutto il traffico dei client connessi verra' instradato attraverso questo tunnel VPN.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### Policy Mode

In questa modalita', il router puo' connettersi a piu' server VPN e puoi personalizzare le regole di instradamento per diversi client o destinazioni del traffico.

E' adatta ai casi d'uso che richiedono una gestione flessibile del traffico, ad esempio instradare traffici diversi verso destinazioni diverse attraverso piu' server VPN.

Passa la modalita' VPN su Policy Mode e fai clic su **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Dopo il passaggio, se la VPN non e' abilitata, la pagina viene mostrata come di seguito, con tre sezioni: Primary Tunnel, Add Tunnel e All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Fai clic sulla sezione corrispondente per saperne di piu'.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Primary Tunnel

Il primary tunnel e' un tunnel <u>preimpostato</u> in Policy Mode. Ha la priorita' piu' alta e puoi modificare la [tunnel priority](#tunnel-priority) se esiste piu' di un tunnel.

In questo tunnel puoi personalizzare la regola del tunnel impostando tre fattori:

1. **From**: si riferisce all'origine del traffico, cioe' al traffico che deve essere instradato tramite questo tunnel.

    Fai clic sulla casella grigia per selezionare l'origine del traffico.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients**: se selezionato, il traffico di tutti i dispositivi corrispondera' a questa regola.

        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: se selezionato, il traffico dei tipi di connessione specificati, ad esempio LAN subnet, Drop-in Gateway, Guest Network, corrispondera' a questa regola.

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Se hai abilitato OpenVPN server o WireGuard server su questo router, ci saranno piu' opzioni sotto Specified Connection Types. Questo e' utile per [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, corrispondera' a questa regola.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: se selezionato, il traffico dei dispositivi specificati, identificati tramite indirizzo MAC, **NON** corrispondera' a questa regola.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: si riferisce alle destinazioni del traffico.

    Fai clic sulla casella grigia per selezionare le destinazioni del traffico.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: se selezionato, il traffico che corrisponde a questa regola verra' instradato verso tutte le destinazioni.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola verra' instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Oppure cambia **Input Mode** da Manual a Subscription URL e inserisci il link URL.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Se selezioni Subscribe URL, il dominio o IP nell'URL viene aggiornato automaticamente ogni giorno.

            - Assicurati di inserire l'URL corretto. Il rilevamento URL verifichera' la validita' del dominio o dell'indirizzo IP. [Scopri di piu'](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: se selezionato, il traffico che corrisponde a questa regola **NON** verra' instradato verso domini o indirizzi IP specificati. Devi inserirli manualmente.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Oppure cambia **Input Mode** da Manual a Subscription URL e inserisci il link URL.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

3. **Via**: si riferisce al metodo di instradamento del traffico, cioe' se usare o meno la VPN.

    Fai clic sulla casella grigia per selezionare il metodo di instradamento.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: se selezionato, il traffico che corrisponde a questa regola verra' instradato verso le destinazioni selezionate tramite VPN.

        Per cominciare, devi configurare il router come VPN client. Usa [VPN Setup Wizard](#setup-wizard) per completare rapidamente la configurazione, oppure vai a OpenVPN Client / WireGuard Client nella barra laterale sinistra per configurarlo manualmente.

        Una volta impostato il router come VPN client, seleziona un file di configurazione VPN per questo tunnel e fai clic su **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: se selezionato, il traffico che corrisponde a questa regola verra' instradato verso le destinazioni selezionate tramite WAN locale invece che tramite VPN.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Dopo aver selezionato origine del traffico, destinazione e metodo di instradamento, la configurazione della regola del primary tunnel e' completa.

Nell'esempio seguente, la regola del Primary Tunnel e': tutti i client usano la VPN per accedere a domini specificati. Il loro traffico viene instradato attraverso il server australiano ed esce verso i domini Internet selezionati tramite questo tunnel.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Nota**: per motivi di sicurezza, vai su [All Other Traffic](#all-other-traffic) e [Tunnel Options](#tunnel-options) per controllare altre impostazioni prima di abilitare i tunnel.

#### Add Tunnel

Per creare tunnel aggiuntivi per piu' istanze VPN, fai clic su **Add Tunnel** sotto il Primary Tunnel e configura regole personalizzate.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Assegna un nome al tunnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Otterrai un tunnel in piu' sul VPN Dashboard.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Puoi aggiungere altri tunnel se necessario. E' possibile creare fino a 5 tunnel, incluso il primary tunnel preimpostato.

Personalizza le regole del tunnel impostando origine del traffico, destinazioni e metodo di instradamento. Fai riferimento a [Primary Tunnel](#primary-tunnel).

**Nota**: per motivi di sicurezza, vai su [All Other Traffic](#all-other-traffic) e [Tunnel Options](#tunnel-options) per controllare altre impostazioni prima di abilitare i tunnel.

#### All Other Traffic

In Policy Mode, un tunnel <u>pre-abilitato</u> viene mostrato nella parte inferiore del VPN Dashboard.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Questo tunnel controlla se il traffico che non corrisponde a nessuno dei gruppi di tunnel VPN precedenti puo' accedere a Internet. E' abilitato per impostazione predefinita per garantire il normale accesso a Internet al traffico non instradato tramite VPN.

- Quando e' abilitato, il traffico non corrispondente puo' comunque accedere a Internet.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Quando e' disabilitato, solo il traffico instradato tramite VPN puo' accedere a Internet. Tutto il traffico non VPN e il traffico che effettua failover dalle connessioni VPN verra' bloccato. Questa opzione non sovrascrive il Kill Switch individuale di ciascun tunnel VPN.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Tunnel Priority

Per impostazione predefinita, il Primary Tunnel preimpostato ha la priorita' piu' alta, seguito dagli altri tunnel aggiunti manualmente, se presenti, e infine dal tunnel All Other Traffic per garantire la connettivita' della rete locale tramite WAN locale.

Per modificare la priorita' dei tunnel, fai clic su **Modify Priority** nella barra informativa superiore, oppure fai clic sull'**etichetta di priorita'** in alto a sinistra di qualsiasi tunnel, ad esempio Priority 1 o Priority 2.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Fai clic e tieni premuta l'icona a tre linee sulla destra per riordinare i tunnel, quindi fai clic su **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Quando sono abilitati piu' tunnel, il router instradera' il traffico nel seguente ordine**:

1. Il traffico tentera' prima di corrispondere alla regola del tunnel con priorita' piu' alta. Se corrisponde, verra' instradato attraverso quel tunnel; altrimenti provera' il tunnel con priorita' successiva, e cosi' via, fino a raggiungere il tunnel "All Other Traffic".

2. Se un tunnel VPN si disconnette inaspettatamente, il sistema determinera' se eseguire il failover del traffico verso il tunnel con priorita' successiva in base al fatto che il **Kill Switch** di quel tunnel sia abilitato.

    - Se il Kill Switch e' abilitato, il traffico verra' bloccato e non effettuera' failover verso il tunnel successivo.
    - Se il Kill Switch e' disabilitato, il traffico effettuera' failover verso il tunnel successivo e tentera' di corrispondere alle sue regole.

3. Il tunnel **All Other Traffic** e' abilitato per impostazione predefinita per garantire che il traffico che non corrisponde ai tunnel VPN possa comunque accedere a Internet.

    - Se abilitato, instrada il traffico non corrispondente o in failover tramite WAN locale.
    - Se disabilitato, rafforza il Kill Switch e blocca il normale accesso a Internet per prevenire perdite di IP.

#### Tunnel Options

Puoi configurare impostazioni avanzate per ciascun tunnel VPN, come VPN Kill Switch, IP Masquerading e MTU.

Fai clic sull'icona dell'ingranaggio accanto al nome del tunnel e seleziona **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: se abilitato, il traffico che corrisponde a questo tunnel VPN verra' bloccato se la connessione VPN fallisce inaspettatamente. Se disabilitato, tale traffico effettuera' failover verso il tunnel successivo in priorita' o verso la WAN locale.

- **Services from GL.iNet Use VPN**: se abilitato, i servizi GoodCloud, DDNS e rtty trasmetteranno i pacchetti attraverso i tunnel VPN. Questa opzione e' disabilitata per impostazione predefinita, poiche' questi servizi di norma richiedono il reale indirizzo IP del dispositivo per funzionare correttamente.

- **Allow Remote Access the LAN Subnet**: se abilitato, sara' consentito l'accesso remoto a questo router e ai suoi dispositivi LAN tramite la VPN. Richiede che il server VPN pubblichi una route di ritorno verso la propria subnet LAN.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
