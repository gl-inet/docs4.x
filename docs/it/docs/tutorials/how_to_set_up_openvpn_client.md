# Come configurare OpenVPN client sui router GL.iNet

Questo tutorial mostra come configurare un client OpenVPN sui router GL.iNet.

Guarda questo video oppure fai riferimento ai passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Prima di iniziare, assicurati di avere un abbonamento attivo con un provider di servizi VPN che supporti la configurazione manuale di OpenVPN. Fai clic [qui](https://www.gl-inet.com/solutions/vpn/){target="_blank"} per controllare i provider OpenVPN compatibili con GL.iNet.

Di seguito trovi i passaggi per configurare un client OpenVPN tramite il pannello di amministrazione web del router.

## 1. Accedi al router

Apri un browser web e accedi al pannello di amministrazione web del router, IP predefinito 192.168.8.1. Effettua il login con la password amministratore.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Configura il client VPN

Fai riferimento alla sezione corrispondente al provider di servizi VPN che stai usando.

??? "NordVPN"

    1. Nel pannello di amministrazione web del router, vai su **VPN** > **OpenVPN Client**.

    2. Fai clic su **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Inserisci le credenziali del servizio, poi fai clic su **Save and Continue**.

        Nota: NON si tratta dell'email/password dell'account di login, ma delle credenziali del servizio ottenute dal sito NordVPN -> Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. Nella finestra richiesta, seleziona le posizioni VPN a cui vuoi collegarti, poi fai clic su **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Seleziona il server VPN a cui vuoi collegarti, fai clic sull'icona con tre puntini e poi su **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Altri provider di servizi VPN, ad esempio Surfshark"

    1. Nel pannello di amministrazione web del router, vai su **VPN** > **OpenVPN Client**.

    2. Fai clic su **Add Manually**.

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Imposta un nome. Puoi inserire il nome del tuo provider di servizi VPN, poi fare clic sull'icona di conferma.

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Assicurati di aver scaricato il file di configurazione fornito dal provider di servizi VPN, e le eventuali credenziali del servizio.
    5. Carica il file di configurazione scaricato.

        Inserisci le credenziali del servizio se richiesto, poi fai clic su **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Accanto all'indirizzo del server VPN, fai clic sull'icona con tre puntini e poi su **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Verificare la connessione VPN

Apri un browser web e cerca il tuo indirizzo IP e la tua posizione. Se corrispondono all'IP e alla posizione del server VPN, invece che a quelli del tuo Internet service provider, allora la connessione VPN e' riuscita.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
