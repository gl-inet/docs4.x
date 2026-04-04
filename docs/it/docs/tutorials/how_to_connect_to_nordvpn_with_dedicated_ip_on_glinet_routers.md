# Come connettersi a NordVPN con un IP dedicato sui router GL.iNet?

Questo articolo illustra i passaggi per configurare una connessione NordVPN con IP dedicato sui router GL.iNet.

Usiamo GL-AXT1800 come esempio.

1. Accedi al tuo account Nord e controlla i dettagli dell'IP dedicato. Come mostrato di seguito, l'IP assegnato e' **193.32.211.142** e il server e' **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Vai su [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) e trova il file di configurazione per **United Kingdom #1625**. Scarica il file di configurazione UDP o TCP.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Torna alla pagina del tuo account Nord, vai su **Manual Setup** e fai clic su **Set up NordVPN Manually** per ottenere le credenziali del servizio.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Accedi al pannello di amministrazione web del router e vai su **VPN** > **OpenVPN Client**. Crea un nuovo gruppo per caricare il file di configurazione scaricato al passaggio 2. Poi inserisci le credenziali del servizio ottenute al passaggio 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    E' stato rilevato 1 file di configurazione valido. Inserisci nome utente e password. Se queste configurazioni usano password diverse, dovrai inserire la password corrispondente per ciascun file di configurazione.

5. Fai clic sull'icona con tre puntini a destra per connetterti. In alternativa puoi andare su **VPN Dashboard**, selezionare il file di configurazione e fare clic su **Apply** per stabilire la connessione.

6. Una volta connesso, controlla il tuo IP pubblico [qui](https://whatismyipaddress.com/) e verifica che corrisponda al tuo IP dedicato NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
