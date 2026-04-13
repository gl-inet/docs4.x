# Come configurare OpenVPN server sui router GL.iNet

Questo tutorial mostra come configurare un server OpenVPN sui router GL.iNet. Un server VPN consente di stabilire da remoto una connessione sicura alla rete di casa o dell'ufficio. Con un router GL.iNet, puoi configurare un server OpenVPN in pochi minuti.

!!! note "Prima di iniziare, assicurati di soddisfare i seguenti requisiti"

    **Indirizzo IP pubblico**

    La configurazione di un server OpenVPN richiede un indirizzo IP pubblico. Per verificare se ne hai uno, fai riferimento a [questo link](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Port forwarding**

    Se il router GL.iNet e' collegato dietro un router principale, [configura il port forwarding sul router principale](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/).

## 1. Accedi al router

Apri un browser web e accedi al pannello di amministrazione web del router, IP predefinito 192.168.8.1. Effettua il login con la password amministratore.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Abilita Dynamic DNS, opzionale

La configurazione di un server OpenVPN richiede in genere un **indirizzo IP pubblico statico**, che fornisce un endpoint fisso attraverso cui altri dispositivi possono accedere al server VPN.

Tuttavia, se non hai un indirizzo IP pubblico statico, ad esempio ne hai uno dinamico, potresti dover abilitare **Dynamic DNS (DDNS)** sul router GL.iNet. Questo consente una connettivita' persistente al server OpenVPN anche quando il tuo indirizzo IP pubblico cambia dinamicamente.

Segui i passaggi seguenti per abilitare Dynamic DNS.

1. Nel pannello di amministrazione web del router, vai su **APPLICATIONS** > **Dynamic DNS**.
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Attiva **Enable DDNS**, leggi e accetta i **Terms of Service & Privacy Policy**, poi fai clic su **Apply**.
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Scarica il file di configurazione

1. Nel pannello di amministrazione web del router, vai su **VPN** > **OpenVPN Server**.
2. Fai clic su **Generate Configuration**.
3. Mantieni le impostazioni predefinite senza modificarle, poi fai clic su **Export Client Configuration**.
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. Nella finestra pop-up, attiva l'interruttore **Use DDNS Domain** se hai configurato in precedenza **Dynamic DNS**.
5. Fai clic su **Download**, poi salva il file.
6. Nella parte superiore della pagina **OpenVPN Server**, fai clic su **Start**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Opzionale) Per accedere alla rete locale del server VPN, abilita queste impostazioni:"

    Per firmware v4.7 e precedenti:

    1. Nella barra laterale sinistra, fai clic su **VPN** > **VPN Dashboard**.
    2. Fai clic sull'icona Options.
    3. Attiva l'interruttore per **Remote Access LAN**.
    4. Fai clic su **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Per firmware v4.8 e successivi:

    1. Nella barra laterale sinistra, fai clic su **VPN** > **OpenVPN Server**.
    2. Fai clic su **Options** nell'angolo in alto a destra.
    3. Attiva l'interruttore per **Allow Remote Access the LAN Subnet**.
    4. Fai clic su **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

## 4. Connettiti al server OpenVPN

Per connetterti al server OpenVPN ti serve un client OpenVPN. Puoi configurarlo usando uno dei metodi seguenti:

??? "Metodo 1: app client OpenVPN di terze parti, usa questo metodo se non hai un router aggiuntivo che supporti la configurazione di un client OpenVPN"

    In questo tutorial useremo come esempio OpenVPN Connect, l'app ufficiale sviluppata da OpenVPN Inc.

    1. Su un altro dispositivo, collegati a una rete Wi-Fi diversa, oppure alla rete cellulare se stai usando un dispositivo mobile.
    2. Invia al dispositivo il file di configurazione scaricato in precedenza, ad esempio via email, poi scaricalo sul dispositivo.
    3. Scarica OpenVPN Connect per il sistema operativo del tuo dispositivo:
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. Nell'app, leggi termini e condizioni, poi seleziona **Agree**.
    5. Seleziona **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Seleziona **Browse**, poi seleziona il file di configurazione scaricato in precedenza.
    7. Seleziona **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Seleziona **Connect** > **OK** > **Allow**.

    Vedrai la parola "Connected" nella parte superiore del profilo VPN.
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Metodo 2: un router che supporta la configurazione di un client OpenVPN"

    Puoi usare qualsiasi router che supporti la configurazione manuale di un client OpenVPN. In questo tutorial useremo come esempio il router da viaggio GL.iNet [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/).

    1. Su un altro dispositivo, collegati a una rete Wi-Fi diversa, oppure alla rete cellulare se stai usando un dispositivo mobile.
    2. Nell'indirizzo del browser web, inserisci l'URL del pannello di amministrazione del router, ad esempio 192.168.8.1.
    3. Inserisci la password, poi fai clic su **Login**.
    4. Nella barra laterale sinistra, fai clic su **VPN** > **OpenVPN Client**.
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Fai clic su **Add Manually**.
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Inserisci un nome nel campo, poi fai clic sull'icona di conferma.
    7. Carica il file di configurazione scaricato in precedenza.
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Fai clic su **Apply**.
    9. Fai clic sull'icona con tre puntini, poi su **Start**.
    10. Collega un dispositivo al router che esegue il client OpenVPN.

## 5. Verificare la connessione VPN

Apri un browser web e cerca il tuo indirizzo IP e la tua posizione. Se corrispondono all'IP e alla posizione del server VPN, invece che a quelli del tuo Internet service provider, allora la connessione VPN e' riuscita.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
