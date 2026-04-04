# Come configurare OpenVPN server tramite AstroRelay?

Questo tutorial presenta i passaggi per configurare un server OpenVPN tramite AstroRelay su un router GL.iNet, ideale per gli utenti che hanno bisogno di accesso remoto ai servizi locali di casa o ufficio ma non dispongono di un indirizzo IP pubblico dal proprio ISP.

[AstroRelay](https://www.astrorelay.com){target="_blank"} fornisce un tunnel reverse proxy sicuro, attraverso il quale puoi accedere in sicurezza alle risorse dietro NAT e firewall.

1. Segui [questa guida](../interface_guide/openvpn_server.md) per configurare un server OpenVPN sul router GL.iNet, anche se non hai un indirizzo IP pubblico.

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Poi esporta la configurazione OpenVPN. Qui sotto trovi un esempio di file di configurazione.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. Facoltativo: se hai bisogno di accedere da remoto alla LAN del server VPN, abilita **Allow Remote Access LAN**. Altrimenti, salta questo passaggio.

    ??? "Per firmware v4.7 e precedenti"

        1. Nella barra laterale sinistra, fai clic su **VPN** > **VPN Dashboard**.
        2. Fai clic sull'icona Options.
        3. Attiva l'interruttore per **Remote Access LAN**.
        4. Fai clic su **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "Per firmware v4.8 e successivi"

        1. Nella barra laterale sinistra, fai clic su **VPN** > **OpenVPN Server**.
        2. Fai clic su **Options** nell'angolo in alto a destra.
        3. Attiva l'interruttore per **Allow Remote Access the LAN Subnet**.
        4. Fai clic su **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3. Registra un account AstroRelay e segui questo [tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"} per completare la configurazione iniziale.

    Quando aggiungi un nuovo dominio, scegli il server piu' vicino al router.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Quando aggiungi un nuovo link, inserisci il **LAN IP address** del router nel campo **Destination Host IP** e inserisci **1194** nel campo **Destination Port**.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    Otterrai quindi un link, ad esempio **testforx3000.arlab1.cc:37202**. Fai clic su di esso per copiarlo.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4. Apri il file di configurazione OpenVPN e sostituisci il valore dopo **Remote** con il link ottenuto nel passaggio precedente. Nell'esempio seguente, `"42.200.00.00 1194"` viene sostituito con il link `"testforx3000.arlab1.cc:37202"`. Poi sostituisci i due punti `:` con uno spazio e applica le modifiche.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5. Installa la [app OpenVPN Connect](https://openvpn.net/client/){target="_blank"} sul dispositivo che vuoi usare come client OpenVPN. Poi carica nell'app il file di configurazione modificato e avvia la connessione. In alternativa, caricalo su un altro router GL.iNet per configurarlo come client OpenVPN.

    Una volta connesso, potrai accedere da remoto ai servizi locali di casa o ufficio.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
