# Come ottenere i file di configurazione dai provider di servizi WireGuard

??? "AzireVPN"
    ### AzireVPN

    [Sito ufficiale](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Accedi al [sito ufficiale di AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} ed effettua il login, poi apri il [generatore di configurazione WireGuard](https://www.azirevpn.com/cfg/wireguard){target="_blank"}.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. Nell'opzione IP, seleziona **IPv4**. Poi fai clic su **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-azirevpn).

    4. Puoi anche usare la [app mobile](../faq/mobile_app.md) per configurare AzireVPN.

??? "Hide.me VPN"
    ### Hide.me VPN

    [Sito ufficiale](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN offre un modo semplice per usare il suo servizio WireGuard su un router GL.iNet.

    1. Collegati al router tramite [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}.

    2. Copia l'URL di installazione riportato sotto, incollalo nel terminale e premi Invio. Il clic destro del mouse incollera' il testo.

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. L'installazione verra' avviata e poi verranno richiesti nome utente e password. Quando digiti o incolli la password, nel terminale non verra' mostrato alcun cambiamento; premi semplicemente Invio dopo averla digitata.

    4. Al termine, vai nel pannello di amministrazione web e vedrai che e' stato creato un gruppo hide.me VPN con i file di configurazione gia' presenti. Ti basta connetterti come faresti con qualsiasi altro file di configurazione.

    **Nota**: la chiave nel file di configurazione Hide.me VPN viene rigenerata prima di ogni connessione e diventa non valida dopo la disconnessione, quindi copiare questo file di configurazione su altri dispositivi non permettera' di connettersi correttamente.

    [Link di riferimento](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [Sito ufficiale](https://mullvad.net/){target="_blank"}

    1. Accedi al [sito ufficiale di Mullvad](https://mullvad.net/){target="_blank"} ed effettua il login, poi apri il [generatore di file di configurazione WireGuard](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}.

    2. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md/#set-up-mullvad).

    3. Puoi anche usare la [app mobile](../faq/mobile_app.md) per configurare Mullvad.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [Sito ufficiale](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Non e' possibile scaricare le configurazioni WireGuard dal sito web; usa la [app mobile](../faq/mobile_app.md) per configurare PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [Sito ufficiale](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Se usi [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, effettua il login e poi vai a [questa pagina](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, fai clic su **Router** e seleziona **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. Nella finestra successiva, seleziona **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Seleziona **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Una volta generata la chiave, seleziona **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Infine, scegli la posizione che vuoi configurare e premi il pulsante **download** accanto alla posizione. Potrai scaricare i file di configurazione.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-surfshark).

    [Link di riferimento](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [Sito ufficiale](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Se usi [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, accedi al sito, vai a [Client Area](https://airvpn.org/client/){target="_blank"} e fai clic su [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Nella pagina Config Generator, seleziona WireGuard nella sezione Protocols.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Seleziona un server, scorri fino in fondo e fai clic su **Generate**. Il file di configurazione verra' scaricato.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Astrill"
    ### Astrill

    [Sito ufficiale](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Se usi [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, effettua il login e poi apri [questa pagina](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} per generare le configurazioni WireGuard.

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "IVPN"
    ### IVPN

    [Sito ufficiale](https://www.ivpn.net/){target="_blank"}

    Se usi [IVPN](https://www.ivpn.net/){target="_blank"}, devi generare manualmente la configurazione WireGuard. Segui la guida in base al tuo sistema operativo.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "NVPN"
    ### NVPN

    [Sito ufficiale](https://www.nvpn.net/){target="_blank"}

    Segui la guida [qui](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} per creare la configurazione.

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "OVPN"
    ### OVPN

    [Sito ufficiale](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Accedi a [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} e trova il menu seguente per ottenere i file di configurazione WireGuard.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Fai clic su **Generate WireGuard keys**, scegli il server desiderato e poi scarica la configurazione.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Apri la configurazione con un editor di testo e copia il contenuto.

        La configurazione puo' contenere contenuti IPv6; poiche' i router GL.iNet non supportano IPv6 in modo sufficientemente completo, elimina il contenuto IPv6. Nell'esempio seguente, la parte evidenziata e' il contenuto IPv6.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    5. Puoi anche usare la [app mobile](../faq/mobile_app.md) per configurare OVPN.

??? "PrivateVPN"
    ### PrivateVPN

    [Sito ufficiale](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Effettua il login e poi apri il [Control panel](https://privatevpn.com/control-panel){target="_blank"}.

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. Seleziona un server.

        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. Fai clic su **GENERATE CONFIG**, poi copia la configurazione.

        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PrivadoVPN"
    ### PrivadoVPN

    [Sito ufficiale](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Accedi al sito di PrivadoVPN ed effettua il login.

    Nella dashboard, trova la sezione Manual Configuration e fai clic su WireGuard. Seleziona il server a cui vuoi connetterti, poi fai clic su Download Configration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Proton VPN"
    ### Proton VPN

    [Sito ufficiale](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Se usi [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, segui la guida [qui](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} per generare il file di configurazione WireGuard.

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PureVPN"
    ### PureVPN

    [Sito ufficiale](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Fai riferimento a [questa guida](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} oppure ai passaggi seguenti per ottenere manualmente il file di configurazione WireGuard.

    1. Accedi alla tua [Member Area](https://my.puremember.com/){target="_blank"} e fai clic su **Manual Configuration**.

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn1.png){class="glboxshadow"}

    2. Vai nella Member Area e scarica da li' il file di configurazione WireGuard.

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn2.png){class="glboxshadow"}

    **Nota**: assicurati di copiare il file e attivare la connessione entro 30 minuti dal download del profilo; in caso contrario la configurazione scadra' e dovrai scaricare un nuovo file di configurazione.

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    [Link di riferimento](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [Sito ufficiale](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Accedi a [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) e trova la sezione per ottenere la configurazione VPN. Segui i passaggi per ottenerla.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Scarica la configurazione VPN.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "StarVPN"
    ### StarVPN

    [Sito ufficiale](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Registra un account StarVPN**

        Vai alle opzioni del [piano tariffario](https://www.starvpn.com/#pricing){target="_blank"} e scegli il piano VPN piu' adatto alle tue esigenze. Puoi registrarti durante il checkout oppure direttamente [qui](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Scarica la configurazione WireGuard**

        Accedi alla [dashboard](https://www.starvpn.com/dashboard){target="_blank"} dell'area membri StarVPN. Fai clic su **Wireguard Config** per scaricare il file di configurazione. Ogni slot conterrà un file di configurazione WireGuard univoco.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Suggerimento**: se vuoi usare l'offuscamento AmneziaWG, fai clic su **AmneziaWG Config** per scaricare il file di configurazione. Ogni slot conterrà un file di configurazione AmneziaWG univoco.

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Modifica il file di configurazione, opzionale**

        La configurazione puo' contenere un indirizzo IPv6. Per evitare problemi di compatibilita' e connettivita', apri il file `.conf` e rimuovi l'indirizzo IPv6, come mostrato di seguito.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) per caricare il file di configurazione sul router GL.iNet.

    Riferimenti:

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [Sito ufficiale](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Se usi [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, accedi a [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}.

    2. Seleziona una posizione dal menu a discesa, fai clic su **GENERATE** e apri il file di testo scaricato.

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    4. Puoi anche usare la [app mobile](../faq/mobile_app.md) per configurare StrongVPN.

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [Sito ufficiale](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Accedi a [https://trust.zone/setup](https://trust.zone/setup) ed effettua il login.

    2. Scorri fino alla sezione WireGuard, scegli la porta che desideri e poi scarica una configurazione per un server specifico oppure un file zip con tutte le configurazioni.

    3. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN.AC"
    ### VPN.AC

    [Sito ufficiale](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Se usi [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, devi accedere al pannello di controllo e trovare WireGuard Manager nel menu "Services".

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. Crea la configurazione e scaricala.

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Sito ufficiale](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Se usi [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, accedi al tuo [User Office](https://my.keepsolid.com/){target="_blank"} > seleziona l'applicazione VPN Unlimited® > fai clic su **Manage**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}

    2. Premi il campo sotto **Device** e fai clic su **Manually create a new device…** > imposta un nome personalizzato, ad esempio WireGuard > scegli la posizione appropriata del **Server** > seleziona il protocollo **WireGuard**® dal menu a discesa > fai clic su **Generate**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}

    3. I parametri di configurazione appariranno quindi sotto in formato testo.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        Combina la configurazione come segue.

        <p>
        [Interface]</br>
        PrivateKey = <i>incolla la PrivateKey dal tuo User Office</i></br>
        ListenPort = <i>incolla i dettagli di ListenPort</i></br>
        Address = <i>incolla le informazioni di Address</i></br>
        DNS = <i>incolla i dettagli DNS dal User Office</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>incolla la PublicKey dal tuo User Office</i></br>
        PresharedKey = <i>incolla i dettagli di PresharedKey</i></br>
        AllowedIPs = <i>incolla i dettagli di AllowedIPs</i></br>
        Endpoint = <i>incolla le informazioni di Endpoint</i></br>
        </p>

    4. Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    [Link di riferimento 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Link di riferimento 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [Sito ufficiale](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Accedi al tuo account Windscribe [qui](https://windscribe.com/login?auth_required){target="_blank"}, poi apri il [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.

    2. Seleziona la posizione del server e la porta che vuoi usare, poi fai clic su **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "12VPX"
    ### 12VPX

    [Sito ufficiale](https://12vpx.com/?aff=1174){target="_blank"}

    Se usi [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, accedi e apri [questa pagina](https://12vpx.com/setup/wireguard){target="_blank"}; vedrai le configurazioni di tutti i server.

    Poi continua seguendo [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
