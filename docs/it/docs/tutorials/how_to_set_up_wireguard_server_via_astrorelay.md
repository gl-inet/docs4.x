# Come configurare WireGuard server tramite AstroRelay?

Questo tutorial presenta i passaggi per configurare un server WireGuard tramite AstroRelay su un router GL.iNet, ideale per gli utenti che hanno bisogno di accesso remoto ai servizi locali di casa o ufficio ma non dispongono di un indirizzo IP pubblico dal proprio ISP.

[AstroRelay](https://www.astrorelay.com){target="_blank"} fornisce un tunnel reverse proxy sicuro, attraverso il quale puoi accedere in sicurezza alle risorse dietro NAT e firewall.

1. Segui [questa guida](../interface_guide/wireguard_server.md) per configurare un server WireGuard sul router GL.iNet, anche se non hai un indirizzo IP pubblico.

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Poi fai clic su **Profiles** per esportare la configurazione WireGuard. Qui sotto trovi un esempio di file di configurazione.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. Facoltativo: se hai bisogno di accedere da remoto alla LAN del server VPN, abilita **Allow Remote Access LAN**. Altrimenti, salta questo passaggio.

    ??? "Per firmware v4.7 e precedenti"

        Nel pannello di amministrazione web del server, vai su **VPN** -> **VPN Dashboard** -> sezione **VPN Server**. Fai clic sull'icona a ingranaggio sul lato destro del server WireGuard.

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        Abilita **Remote Access LAN** e fai clic su **Apply**.

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **Quando e' abilitato, questo router e i dispositivi LAN possono essere raggiunti da remoto tramite VPN.**

    ??? "Per firmware v4.8 e successivi"

        Nel pannello di amministrazione web del server, vai su **VPN** -> **WireGuard Server**. Fai clic su **Options** nell'angolo in alto a destra.

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        Abilita **Allow Remote Access the LAN Subnet** e fai clic su **Apply**.

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **Quando e' abilitato, questo router e i dispositivi LAN possono essere raggiunti da remoto tramite VPN.**

3. Registra un account AstroRelay e segui questo [tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"} per completare la configurazione iniziale.

    Quando aggiungi un nuovo dominio, scegli il server piu' vicino al router.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Quando aggiungi un nuovo link, inserisci il **LAN IP address** del router nel campo **Destination Host IP** e inserisci **51820** nel campo **Destination Port**.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    Otterrai quindi un link, ad esempio **wg_server_test.arlab1.cc:33331**. Fai clic sul link per copiarlo.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4. Apri il file di configurazione WireGuard, sostituisci il valore dopo **Endpoint** con il link ottenuto nel passaggio precedente e applica le modifiche.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5. Installa la [app WireGuard](https://www.wireguard.com/install/){target="_blank"} sul dispositivo che vuoi usare come client WireGuard. Poi carica nell'app il file di configurazione modificato e avvia la connessione. In alternativa, caricalo su un altro router GL.iNet per configurarlo come client WireGuard.

    Una volta connesso, potrai accedere da remoto ai servizi locali di casa o ufficio.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
