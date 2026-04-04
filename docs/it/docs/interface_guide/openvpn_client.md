# Configurare OpenVPN Client sui router GL.iNet {#setup-openvpn-client}

OpenVPN e' un protocollo VPN open-source che usa tecniche di rete privata virtuale per stabilire connessioni sicure site-to-site o point-to-point.

Per configurare OpenVPN client su un router GL.iNet, guarda questo video oppure segui i passaggi qui sotto.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Prima di iniziare, assicurati di avere un abbonamento attivo con un provider di servizi VPN che supporti la configurazione manuale di OpenVPN. Fai clic [qui](https://www.gl-inet.com/solutions/vpn/){target="_blank"} per verificare i provider OpenVPN compatibili con GL.iNet.

In generale, devi prima visitare il sito ufficiale del provider VPN a cui sei abbonato, ottenere il file di configurazione e caricarlo sul router per impostarlo come client OpenVPN. Se non sai come ottenere il file di configurazione, fai riferimento [a questo link](#get-configuration-files-from-openvpn-service-providers) oppure contatta il supporto del provider.

Puoi configurare un client OpenVPN tramite il pannello di amministrazione web oppure tramite la [mobile app](../faq/mobile_app.md). Di seguito trovi i passaggi per la configurazione tramite pannello di amministrazione web.

---

Nel pannello di amministrazione web, vai su **VPN** -> **OpenVPN Client**.

Se hai un abbonamento NordVPN, fai clic su **NordVPN** per effettuare il login; altrimenti fai clic su **Add Manually** per caricare i file di configurazione OpenVPN.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Configurare NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} e' un popolare servizio VPN online noto per velocita' e sicurezza.

La configurazione rapida di NordVPN e' integrata nel pannello di amministrazione dei router GL.iNet. Puoi ottenere online i file di configurazione per tutti i server NordVPN inserendo le credenziali del tuo account, ottenute dal NordVPN Dashboard, nel pannello di amministrazione web del router o nella mobile app, senza dover caricare manualmente i file.

1. Accedi al tuo account web NordVPN [qui](https://my.nordaccount.com/){target="_blank"}.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

    Dopo l'accesso, nel Nord Dashboard fai clic su **NordVPN**, quindi su **Set up NordVPN manually**.

    ![nord dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Troverai le **service credentials**. Copiale per usarle piu' tardi.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Accedi al pannello di amministrazione web del router, vai su VPN -> OpenVPN Client -> NordVPN. Inserisci le **service credentials** ottenute al passaggio 1 (nota: **NON** sono email/password dell'account di login), quindi fai clic su **Save and Continue**.

    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Seleziona protocollo, numero massimo di server per ciascuna localita' e localita', quindi fai clic su **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

    Verranno scaricati i file di configurazione.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Avvia una connessione.

    Seleziona un server preferito e fai clic sull'icona con i tre puntini a destra per avviare la connessione.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Inoltre, i dettagli della connessione VPN verranno mostrati nel **VPN Dashboard**.

    ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione causati da manutenzione o dismissione dei server.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Modifica le credenziali.

    Fai clic sull'icona dell'ingranaggio per modificare le credenziali di accesso.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Elimina tutti i file.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Configurare manualmente OpenVPN Client (per altri provider)

Se il tuo provider di servizi OpenVPN non e' integrato nel nostro pannello di amministrazione, visita prima il sito ufficiale del provider a cui sei abbonato per ottenere il file di configurazione. Poi caricalo sul router per configurare un client OpenVPN.

Nei passaggi seguenti useremo [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} come esempio.

1. Scarica un file di configurazione dal sito ufficiale di Private Internet Access.

2. Accedi al pannello di amministrazione web del router, vai su VPN -> OpenVPN Client e fai clic su **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. Verra' creato un gruppo nella barra laterale sinistra.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. Imposta un nome descrittivo per il gruppo, ad esempio private internet access.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. Carica il file di configurazione OpenVPN. Inserisci le credenziali se richiesto, quindi fai clic su **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}

    - Sono disponibili 4 tipi di credenziali per l'autenticazione:

        1. Nessuna autenticazione.

        2. Solo Username e Password.

        3. Solo Passphrase.

        4. Username, Password e Passphrase.

    A questo punto vedrai il file di configurazione caricato.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. Fai clic sull'icona con i tre puntini a destra per avviare una connessione.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

    Inoltre, i dettagli della connessione VPN verranno mostrati nel **VPN Dashboard**.

    ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## Configurare OpenVPN Server su un router GL.iNet

Se hai due router GL.iNet, puoi valutare di impostarne uno come OpenVPN server, e' richiesto un IP pubblico, e l'altro come OpenVPN client. In questo modo puoi creare la tua connessione VPN senza abbonarti a servizi VPN di terze parti.

Per configurare OpenVPN server, fai riferimento [qui](openvpn_server.md).

## Ottenere i file di configurazione dai provider OpenVPN {#get-configuration-files-from-openvpn-service-providers}

Abbiamo testato oltre 30 provider di servizi OpenVPN e documentato i passaggi per ottenere i file di configurazione. Se non sei sicuro di come ottenere il file di configurazione, fai riferimento ai passaggi qui sotto.

Se il provider a cui sei abbonato non e' elencato di seguito, contatta il relativo supporto per ulteriore assistenza.

??? "NordVPN"
    ### NordVPN

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Accedi al tuo account NordVPN**

        Accedi al [sito ufficiale](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}, vai al Nord Account Dashboard, dove troverai le service credentials.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        Dopo l'accesso al Nord dashboard, fai clic su NordVPN sul lato sinistro, quindi su **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Trova le **Service credentials**. Copiale nel caso ti servano per il caricamento della configurazione.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Scegli un server NordVPN e scarica il file di configurazione**

        Vai alla scheda **Server recommendation**. Ti verra' consigliato un server in base alla tua rete e ti verranno forniti i protocolli disponibili da scaricare. Fai clic su **Get setup configuration** per continuare.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        Nella finestra pop-up, seleziona il protocollo **OpenVPN** e scarica la configurazione UDP o TCP.

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Puoi scaricare le configurazioni di tutti i server [qui](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Suggerimenti: se il file zip e' troppo grande da caricare, puoi eliminare alcuni file `.ovpn` dallo zip oppure caricare un singolo file `.ovpn`.

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Puoi anche usare la [mobile app](../faq/mobile_app.md) per configurare NordVPN.

??? "AirVPN"
    ### AirVPN

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Accedi al tuo account AirVPN

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Scegli Config Generator sul lato sinistro e poi seleziona Linux come sistema operativo. Successivamente scegli il server preferito.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Potrai vedere la pagina di download del file di configurazione.

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Informazioni tratte dalle [istruzioni ufficiali Astrill](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Genera e scarica il file ZIP di configurazione OpenVPN di Astrill

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Inserisci una descrizione, ad esempio OPENVPN_GUI.

    3. Fai clic sul pulsante ADD to my certificates.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Una volta aggiunto il certificato OpenVPN, fai clic sul pulsante Download.

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

    Accedi al [Dashboard](https://users.bolehvpn.net/){target="_blank"}, scarica i file di configurazione e seleziona il formato [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Estrai i file zip dopo aver completato il download.

    Suggerimenti: se il file zip e' troppo grande da caricare, puoi eliminare alcuni file `.ovpn` dallo zip oppure caricare un singolo file `.ovpn`.

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Download](https://www.cactusvpn.com/downloads/){target="_blank"} diretto.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [Download](https://cryptostorm.is/configs/ecc/){target="_blank"} diretto.

??? "CyberGhost"
    ### CyberGhost

    [Official Website](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Informazioni tratte dalle [istruzioni ufficiali CyberGhost](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Accedi al tuo account online CyberGhost VPN.

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Seleziona "**VPN**" dal menu a sinistra, poi fai clic su "**Configure Device**" e crea la configurazione del server come descritto di seguito:

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Ora crea la configurazione del server come descritto di seguito:

        * **Protocol** : **OpenVPN**
        * **Country** : poiche' le connessioni con protocollo nativo possono essere usate solo con un singolo server, devi scegliere il paese da cui vuoi navigare; il server da usare in quel paese verra' scelto automaticamente da CyberGhost.
        * **Server group** : scegli il gruppo di server e il protocollo OpenVPN, UDP o TCP, che vuoi usare

        **OpenVPN UDP** consente velocita' maggiori rispetto alla versione TCP, ma in alcuni casi puo' causare download interrotti. Questa e' l'impostazione predefinita.

        **OpenVPN TCP** offre connessioni piu' stabili rispetto alla versione UDP, ma e' leggermente piu' lento. Scegli questa versione se hai problemi ricorrenti di connessione, come disconnessioni improvvise.

        Una volta scelti i parametri desiderati, salvali con **Save Configuration**

    4. Per visualizzare le credenziali **OpenVPN** generate per te nel dashboard di configurazione, premi **View Configuration**.

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Dopo aver configurato le preferenze di connessione, tieni presente quanto segue:

        * **Server Group** : e' l'indirizzo del paese, server, a cui vuoi collegarti, ad esempio `12345-1-ca.cg-dialup.net`. Questo indirizzo cambia per ogni paese scelto nel passaggio precedente. Il singolo server effettivo verra' scelto automaticamente da CyberGhost.
        * **Username** : e' un nome utente generato appositamente per questo protocollo. NON e' il normale nome utente dell'account CyberGhost; viene usato solo per autenticarsi con i server CyberGhost tramite configurazioni manuali. Ti servira' quando configurerai OpenVPN sui router GL.iNet.
        * **Password** : e' una password generata appositamente per l'uso di questo protocollo. NON e' la normale password dell'account CyberGhost; viene usata solo per autenticarsi con i server CyberGhost tramite configurazioni manuali. Ti servira' quando configurerai OpenVPN sui router GL.iNet.

        Una volta fatto, scarica il file di configurazione. Per farlo, fai clic su *Download Configuration* e scarica il file di configurazione sul computer.

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN

    [Official Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    Informazioni tratte dalle [istruzioni ufficiali ExpressVPN](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Vai sul sito [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} e accedi con le credenziali ExpressVPN.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Inserisci il codice di verifica** inviato alla tua email.

    2. Nella sezione "Set up your devices", fai clic su **More**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. Fai clic su **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. Vedrai **username**, **password** e un elenco di **OpenVPN configuration files**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Fai clic sulle localita' desiderate per scaricare i file `.ovpn`.

        **Tieni aperta questa finestra del browser**. Ti servira' piu' tardi durante la configurazione.

    [Refer link](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Scarica il file zip delle configurazioni FastestVPN per OpenVPN TCP e UDP [qui](https://support.fastestvpn.com/download/fastestvpn_ovpn/)

    Suggerimenti: se il file zip e' troppo grande da caricare, elimina alcuni file `.ovpn` dalla cartella zip oppure carica un singolo file `.ovpn`.

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. Accedi al tuo account FinchVPN.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Vai alla pagina Download e fai clic su Download sotto FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Scegli Linux.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Scegli il protocollo in base alle tue preferenze. In genere puoi selezionare il primo, **Port 8484 over UDP**.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Ricordati di selezionare la casella per includere username e password prima di scaricare il file.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. Accedi al tuo account HideIPVPN.

    2. Vai su Package sul lato sinistro, fai clic sul tuo pacchetto e assicurati che sia attivo.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. Nella scheda VPN sono presenti i dettagli di login VPN, username e password, usati per la connessione OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Scorri verso il basso per scaricare i file di configurazione OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Accedi al tuo account Hide.me e trova Server Locations sul lato sinistro.

    2. Scarica la configurazione OpenVPN per Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [Official Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Nota: i file di configurazione router di Hotspot Shield non sono piu' disponibili o supportati. I passaggi seguenti restano qui solo a scopo storico per chi li avesse ancora installati.**

    1. Vai su [https://www.hotspotshield.com/](https://www.hotspotshield.com/) e fai clic su Account. Effettua il login se richiesto.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Vai su [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router)

        Vai nel menu Select location e scegli la localita' virtuale che il router dovra' usare. Poi fai clic su "Download file". Il file di configurazione, `config.ovpn`, verra' scaricato sul computer. Username e password dovranno essere inseriti quando configurerai OpenVPN client sul router.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Refer link](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Puoi scaricare tutti i file di configurazione per tutti i server [qui](https://configs.ipvanish.com/configs/configs.zip). Il file contiene tutti i file di configurazione dei server `.ovpn` e un file certificato `.crt`. Il file `.zip` potrebbe essere un po' grande per alcuni modelli; elimina i file di configurazione `.ovpn` dei server che non userai.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Puoi anche scaricare i file di configurazione dei singoli server [qui](https://www.ipvanish.com/software/configs/), ma dovrai scaricare anche **ca.ipvanish.com.crt**. Prima di caricarli sul router, devi comprimere **ca.ipvanish.com.crt** e i file di configurazione `.ovpn` in un archivio `.zip`.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    Per configurare un client OpenVPN con Ivacy, ti servono:

    - Lo username per la configurazione manuale OpenVPN, mostrato nel prompt "Download Configuration"
      ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - La password, la stessa usata per accedere al tuo account Ivacy
    - Un file di configurazione OpenVPN

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Scarica i [file di configurazione OpenVPN](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Trova l'Account ID nella [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Quando trascini il file di configurazione su Add a New OpenVPN Configuration, ti verra' chiesto di inserire User Name e Password. User Name e' il tuo Account ID che inizia con le lettere **ivpn**. La password puo' essere qualsiasi cosa, ad esempio **ivpn**

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad"
    ### Mullvad

    [Official Website](https://mullvad.net/en){target="_blank"}

    1. Vai sul sito [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"} e accedi con le credenziali Mullvad.

    2. Scegli OpenVPN Configuration

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. Scegli **Linux** e seleziona la localita' del server.

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    Basta effettuare il login e potrai ottenere facilmente i file di configurazione OpenVPN facendo clic sul menu seguente.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Scegli il server e scarica.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    Username e password sono gli stessi usati per accedere a OVPN.

??? "OysterVPN"
    ### OysterVPN

    [Official Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Vai alla [pagina dell'elenco server OysterVPN](https://support.oystervpn.com/server-list/){target="_blank"} e fai clic su **Download .ovpn file** per scaricare il file di configurazione.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. Lo username e la password per la connessione OpenVPN sono gli stessi che usi per accedere a OysterVPN.

    Suggerimenti: se il file zip e' troppo grande da caricare, puoi eliminare alcuni file `.ovpn` dallo zip oppure caricare un singolo file `.ovpn`.

??? "PIA (Private Internet Access)"
    ### PIA

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Download](https://www.privateinternetaccess.com/openvpn/openvpn.zip) diretto.

    Suggerimenti: se il file zip e' troppo grande da caricare, puoi eliminare alcuni file `.ovpn` dallo zip oppure caricare un singolo file `.ovpn`.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Basta effettuare il login e potrai trovare facilmente **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

??? "PrivateVPN"
    ### PrivateVPN

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank"} diretto.

    [Qui](https://privatevpn.com/client/PrivateVPN-TUN.zip) trovi il link di download ufficiale. A causa di un bug riscontrato durante l'importazione nel router, il nome del file interno contiene caratteri speciali come 'Bogota'. Lo abbiamo rinominato e abbiamo fornito il link di download qui sopra. Correggeremo questo bug nelle versioni future.

    Suggerimenti: se il file zip e' troppo grande da caricare, puoi eliminare alcuni file `.ovpn` dallo zip oppure caricare un singolo file `.ovpn`.

??? "Proton VPN"
    ### Proton VPN

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN offre il servizio WireGuard; consigliamo di usare WireGuard, fai riferimento [qui](wireguard_client.md#wireguard-providers)**.

    1. Accedi al tuo account [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}.

    2. Fai clic su **Download** sul lato sinistro.

    3. Scegli la piattaforma Router, il protocollo ecc., trova il paese di destinazione e scarica il file di configurazione.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. Le credenziali per la connessione OpenVPN non sono quelle usate per accedere al dashboard del sito Proton. Puoi trovarle in **Account -> OpenVPN/IKEv2 username**

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Per configurare un client OpenVPN con PureVPN, ti serviranno username e password OpenVPN e un file di configurazione, che puoi trovare nel tuo account PureVPN.

    1. [Accedi al tuo account PureVPN.](https://my.purevpn.com/)
    2. Nella barra laterale sinistra, fai clic su **Subscriptions**.
    3. Scorri verso il basso per trovare username e password OpenVPN.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. Nella barra laterale sinistra, fai clic su **Manual Configuration**.
    5. Seleziona una localita' VPN e fai clic su **Download** per scaricare il file di configurazione.

    [Refer link](https://support.purevpn.com/openvpn-files)

    I router GL.iNet non supportano la funzione [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"} di PureVPN, perche' richiede PPTP.

??? "SaferVPN"
    ### SaferVPN

    [Official Website](https://safervpn.com/?a_aid=563){target="_blank"}

    Fai clic [qui](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup) per scaricare direttamente i file di configurazione.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN offre il servizio VPN con protocolli OpenVPN e WireGuard. Consigliamo WireGuard, poiche' di solito e' piu' veloce di OpenVPN. Fai riferimento [qui](wireguard_client.md#starvpn).

    Se preferisci usare OpenVPN, segui i passaggi qui sotto per scaricare il file di configurazione.

    1. **Registra un account StarVPN**

        Vai alla pagina delle [opzioni di piano tariffario](https://www.starvpn.com/#pricing){target="_blank"} e scegli il piano VPN piu' adatto alle tue esigenze. Puoi registrarti al checkout oppure direttamente [qui](https://www.starvpn.com/dashboard/register.php){target="_blank"}

    2. **Scarica la configurazione OpenVPN**

        Accedi all'area membri StarVPN [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. Nel Dashboard individua la sezione **VPN Configuration** e fai clic su **OpenVPN Config**. Copia username e password OVPN. Ti serviranno per l'autenticazione quando caricherai il file sul router GL.iNet.

        ![download starvpn ovpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/ovpnconfigdl.png){class="glboxshadow"}

        Seleziona UDP o TCP e scarica il file di configurazione.

        ![select udp or tcp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/udp_tcp.png){class="glboxshadow"}

    3. **Modifica il file di configurazione**

        Alcuni router GL.iNet non supportano IPv6. Per evitare problemi di compatibilita' e connettivita', apri il file di configurazione `.ovpn` e rimuovi il contenuto relativo a IPv6, come mostrato di seguito.

        ![remove ipv6](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/remove_ipv6.png){class="glboxshadow"}

??? "StreamVPN"
    ### StreamVPN

    [Official Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Accedi con il tuo account [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} e potrai vedere le informazioni sul tuo abbonamento. Fai clic su **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Fai clic su **VPN Router**: verra' scaricato un archivio `.zip` chiamato `StreamVPN.zip`.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Nota:** funzionano solo i file di configurazione il cui nome contiene "Primary".

??? "StrongVPN"
    ### StrongVPN

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Accedi con il tuo account [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} e vedrai il riepilogo degli account VPN. Fai clic su **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Trova la sezione Manual setup e segui i passaggi per ottenere la configurazione.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Trova i dettagli di login**

        Le service credentials di Surfshark sono diverse dalle credenziali del tuo account Surfshark, cioe' il tuo indirizzo email e la tua password. Ti serviranno le service credentials di Surfshark per collegarti alla VPN usando il metodo di configurazione manuale OpenVPN nel router.

        Accedi al [sito ufficiale](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, vai [a questa pagina](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, dove troverai tutti i dettagli necessari per una connessione manuale.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Scegli un server Surfshark**

        Seleziona la scheda **Locations**, dove vedrai tutti i server Surfshark.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        Ti verra' chiesto di scegliere TCP o UDP. Fai clic [qui](../faq/openvpn_tcp_udp.md) per vedere la differenza.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}

    Puoi scaricare tutte le configurazioni [qui](https://api.surfshark.com/v1/server/configurations) direttamente.

    Suggerimenti: se il file zip e' troppo grande da caricare, puoi eliminare alcuni file `.ovpn` dallo zip oppure caricare un singolo file `.ovpn`.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    I file di configurazione OpenVPN sono elencati sul [sito web VPN Gate](https://www.vpngate.net/en/) in base alla localita' del server.

    1. Fai clic su OpenVPN Config file nella colonna **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Vedrai la pagina di download.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Informazioni tratte dalle [istruzioni ufficiali VPN unlimited](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Inizia accedendo al tuo User Office, premi Manage per il servizio VPN Unlimited e segui alcuni semplici passaggi:

    1. Seleziona un dispositivo

        Scegli un dispositivo dall'elenco oppure creane uno nuovo. Se non hai piu' slot liberi, elimina un vecchio dispositivo oppure acquista slot aggiuntivi.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Scegli la localita' del server desiderata

        VPN Unlimited offre un'ampia varieta' di server, oltre 400 in piu' di 70 localita'. In questo caso, ad esempio, Germania.

    3. Seleziona il protocollo VPN

        seleziona il protocollo OpenVPN.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Crea una configurazione

        Premi Generate e otterrai tutti i dati necessari per configurare una connessione VPN.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPN offre i file OpenVPN qui: [Where can I find the OpenVPN files? - VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    Il file zip fornito contiene due cartelle con i file `.ovpn`: una chiamata OpenVPN160 e una chiamata OpenVPN256. Basta eliminare la cartella OpenVPN160 dal file zip e poi caricarlo normalmente sul router GL.iNet.

??? "Windscribe"
    ### Windscribe

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Accedi al tuo account Windscribe [qui](https://windscribe.com/login?auth_required){target="_blank"}, poi apri [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}.

    2. Seleziona la localita' del server, il protocollo UDP/TCP, la porta, ad esempio 1194, e la versione OpenVPN, preferibilmente quella piu' recente, quindi fai clic su **Download Config**. Verra' scaricato sul tuo dispositivo locale un file con estensione `.ovpn`.

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Fai clic sul pulsante **Get Credentials** nella stessa pagina. Riceverai le credenziali corrispondenti, che verranno poi usate nel pannello di amministrazione web del router quando caricherai il file di configurazione per l'autenticazione. Copia le credenziali oppure lascia questa pagina aperta.

    4. Poi segui [questa guida](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers) per continuare.

??? "ZoogVPN"
    ### ZoogVPN

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Accedi al [sito ufficiale](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}, poi apri la [pagina dei file di configurazione OpenVPN](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}, dove troverai tutti i server. Scarica il file di configurazione dalla colonna TCP oppure dalla colonna UDP.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Poi segui la [guida per configurare OpenVPN Client sul router GL.iNet](#setup-openvpn-client); username e password sono gli stessi usati per accedere al sito ZoogVPN.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
