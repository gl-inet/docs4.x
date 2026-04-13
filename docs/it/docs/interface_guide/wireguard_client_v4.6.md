# Configurare WireGuard Client sui router GL.iNet (Firmware v4.6 e precedenti)

**Nota**: questa guida si applica al firmware v4.6 e precedenti. Per le versioni piu' recenti, fai riferimento [qui](wireguard_client.md).

---

WireGuard® e' una VPN estremamente semplice, veloce e moderna che utilizza crittografia all'avanguardia. Punta a essere piu' veloce, piu' semplice, piu' leggera e piu' utile di IPsec, evitando al tempo stesso una complessita' eccessiva. In generale offre prestazioni nettamente migliori rispetto a OpenVPN.

Se hai gia' acquistato un servizio WireGuard da un provider ma non sai come ottenere i file di configurazione, fai riferimento a [ottenere i file di configurazione dai provider di servizi WireGuard](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oppure contatta il loro supporto.

Puoi configurare WireGuard Client tramite il pannello di amministrazione web oppure tramite [app mobile](../faq/mobile_app.md).

- L'app mobile integra diversi provider di servizi WireGuard, come AzireVPN, Mullvad, OVPN, StrongVPN e PIA VPN.

- Il pannello di amministrazione web supporta meno provider WireGuard, ad esempio AzireVPN e Mullvad, ma offre pagine piu' intuitive e dettagliate.

Di seguito trovi i passaggi per la configurazione tramite il pannello di amministrazione web.

---

Accedi al pannello di amministrazione web e vai su **VPN** -> **WireGuard Client**.

Se hai un abbonamento **AzireVPN** o **Mullvad**, puoi effettuare direttamente il login con le relative credenziali. In alternativa, fai clic su **Add Manually** per caricare manualmente i profili WireGuard.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Configurare AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} e' un servizio VPN orientato alla privacy che offre tunnel sicuri, moderni e robusti come WireGuard.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Inserisci **Username** e **Password**, quindi fai clic su **Save Credentials & Get Servers**. Verranno generati i file di configurazione per ciascun server.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Vai al VPN Dashboard per abilitare la connessione.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Una volta connesso, vedrai il tuo indirizzo IP utente e il numero di byte inviati/ricevuti.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Aggiornare i server

    AzireVPN puo' mettere alcuni server in manutenzione o dismetterli, causando errori di connessione. Puoi usare **Update Servers** per ottenere l'elenco piu' recente dei server disponibili.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Modificare le credenziali

    Fai clic sull'icona a ingranaggio per modificare le credenziali.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Configurare Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} e' un servizio VPN che aiuta a mantenere private la tua attivita' online, la tua identita' e la tua posizione.

Il firmware 4.x integra il servizio Mullvad WireGuard.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Inserisci **Account**, quindi fai clic su **Save Credentials & Get Servers**.

    Il numero account Mullvad e' un valore decimale di 16 cifre compreso tra "1000 0000 0000 0000" e "9999 9999 9999 9999".

    Si aprira' una finestra di dialogo per selezionare una posizione.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Verranno quindi generati i file di configurazione per il server della posizione selezionata.

    La **Public Key** e' la chiave pubblica WireGuard inviata al server Mullvad. Puoi avere fino a cinque chiavi contemporaneamente e gestire le chiavi WireGuard nella [pagina di Mullvad](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Vai al VPN Dashboard per abilitare la connessione.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Una volta connesso, vedrai il tuo indirizzo IP utente e il numero di byte inviati/ricevuti.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Aggiornare i server

    Mullvad puo' mettere alcuni server in manutenzione o dismetterli, causando errori di connessione. Puoi usare **Update Servers** per ottenere l'elenco piu' recente dei server disponibili.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Modificare le credenziali

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Eliminare le informazioni dell'account

    Se fai clic su **Delete**, verranno eliminati **nel router** le credenziali dell'account, la chiave privata, la chiave pubblica e i file di configurazione.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Eliminare

    Consente di eliminare tutti i file di configurazione con un clic e mostra un prompt per eliminare anche la chiave privata e la chiave pubblica.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Configurare manualmente WireGuard Client

Dal firmware 4.0 e' stata introdotta la gestione dei profili WireGuard tramite gruppi.

1. Fai clic su **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Verra' creato un gruppo.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Assegna al gruppo un nome descrittivo, ad esempio azirevpn. Poi puoi scegliere se caricare i file di configurazione oppure aggiungere manualmente la configurazione.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Upload configuration files**

        Carica il file di configurazione WireGuard, poi fai clic su **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration**, da usare se vuoi incollare la configurazione WireGuard o compilare ciascun campo singolarmente.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Assegna un nome descrittivo, incolla la configurazione e fai clic su **Apply** per continuare.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Oppure puoi aggiungere la configurazione compilando ciascun campo; fai clic su **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Fai clic sull'icona con tre puntini per avviare / modificare / eliminare il profilo.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Controlla lo stato della connessione nella pagina [VPN Dashboard](vpn_dashboard_v4.7.md).

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® e' un marchio registrato di Jason A.Donenfeld.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
