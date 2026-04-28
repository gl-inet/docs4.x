# Configurare WireGuard Client sui router GL.iNet

**Nota**: questa guida si applica al firmware v4.7 e successivi. Per le versioni precedenti, fai riferimento [qui](wireguard_client_v4.6.md).

---

WireGuard® e' una VPN estremamente semplice, veloce e moderna che utilizza crittografia all'avanguardia. Punta a essere piu' veloce, piu' semplice, piu' leggera e piu' utile di IPsec, evitando al tempo stesso una complessita' eccessiva. In generale offre prestazioni nettamente migliori rispetto a OpenVPN.

Per configurare WireGuard client su un router GL.iNet, guarda questo video oppure fai riferimento ai passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Prima di iniziare, assicurati di avere un abbonamento attivo con un provider di servizi VPN che supporti la configurazione manuale di WireGuard. Fai clic [qui](https://www.gl-inet.com/solutions/vpn/){target="_blank"} per controllare i provider WireGuard compatibili con GL.iNet.

In generale, devi prima visitare il sito ufficiale del provider VPN a cui sei abbonato, ottenere il file di configurazione e caricarlo sul router per impostarlo come client WireGuard. Se non sai come ottenere il file di configurazione, fai riferimento a [questo link](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oppure contatta il relativo supporto.

Puoi configurare un client WireGuard tramite il pannello di amministrazione web oppure tramite [app mobile](../faq/mobile_app.md).

- **L'app mobile** integra alcuni provider di servizi WireGuard, come AzireVPN, Mullvad VPN, OVPN, StrongVPN, PIA VPN e altri, quindi puoi configurarlo facilmente inserendo semplicemente le credenziali del servizio WireGuard a cui sei abbonato. Apri l'app e segui le istruzioni mostrate sullo schermo.

- **Il pannello di amministrazione web** non solo integra alcuni provider di servizi WireGuard, ma offre anche una voce per la configurazione manuale. Puoi inserire le credenziali del tuo servizio WireGuard per una configurazione rapida oppure caricare manualmente un file di configurazione per completare la procedura.

Di seguito trovi i passaggi per la configurazione tramite pannello di amministrazione web. Seleziona il provider di servizi WireGuard corrispondente qui sotto per individuare rapidamente le istruzioni passo-passo.

* [Set Up AzireVPN](#set-up-azirevpn)
* [Set Up Hide.me](#set-up-hideme)
* [Set Up IPVanish](#set-up-ipvanish)
* [Set Up Mullvad](#set-up-mullvad)
* [Set Up NordVPN](#set-up-nordvpn)
* [Set Up PIA (Private Internet Access)](#set-up-pia-private-internet-access)
* [Set up PureVPN](#set-up-purevpn)
* [Set Up Surfshark](#set-up-surfshark)
* [Set Up WireGuard Client Manually (for other providers)](#set-up-wireguard-client-manually-for-other-providers)

## Set Up AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} e' un servizio VPN orientato alla privacy che offre tunnel sicuri, moderni e robusti come WireGuard.

Guarda questo video per configurare AzireVPN sui router GL.iNet tramite pannello di amministrazione web o app mobile.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Oppure segui i passaggi seguenti per configurare AzireVPN tramite pannello di amministrazione web.

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Vai a rinnovare.

    Se fai clic su **Go Renew**, verrai reindirizzato al sito ufficiale per rinnovare l'abbonamento.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Set Up Hide.me {#set-up-hideme}

[Official Website](https://www.hideipvpn.com/){target="_blank"}

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Set Up IPVanish {#set-up-ipvanish}

[Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Seleziona i server.

    Seleziona il server o i server a cui vuoi connetterti, quindi fai clic su **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Set Up Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} e' un servizio VPN che aiuta a mantenere private la tua attivita' online, la tua identita' e la tua posizione.

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Inserisci **Account**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Seleziona i server.

    Seleziona il server o i server a cui vuoi connetterti, quindi fai clic su **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Vai a rinnovare.

    Se fai clic su **Go Renew**, verrai reindirizzato al sito ufficiale per rinnovare l'abbonamento.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Set Up NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} e' un servizio VPN online che combina velocita' e sicurezza.

1. Fai clic [qui](https://my.nordaccount.com/){target="_blank"} per accedere con il tuo account web NordVPN.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}

    Dopo aver effettuato l'accesso alla dashboard Nord, fai clic su **NordVPN** nel menu a sinistra, individua la sezione **Access Token**, quindi fai clic su **Get Access token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token1.png){class="glboxshadow"}

    Nella pagina successiva, fai clic su **Generate new token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token2.png){class="glboxshadow"}

    Nella finestra pop-up, seleziona la data di scadenza del token, quindi fai clic su **Generate token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token3.png){class="glboxshadow"}

    A questo punto verra' mostrato il token di accesso. Copialo per usarlo piu' tardi.

    **Nota**: il token di accesso viene mostrato una sola volta. Assicurati di copiarlo e usarlo subito. Dopo aver chiuso questa finestra, il token non sara' piu' visibile. Se non lo salvi, dovrai generarne uno nuovo.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token4.png){class="glboxshadow"}

2. Accedi al pannello di amministrazione web del router, vai su **VPN** -> **WireGuard Client** -> **NordVPN**.

    Inserisci **Token**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Seleziona i server.

    Seleziona il server o i server a cui vuoi connetterti, quindi fai clic su **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Set Up PIA (Private Internet Access) {#set-up-pia-private-internet-access}

[Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **PIA**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Seleziona i server.

    Seleziona il server o i server a cui vuoi connetterti, quindi fai clic su **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Set Up PureVPN {#set-up-purevpn}

[Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **PureVPN**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    Verranno generati tutti i file di configurazione disponibili.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

4. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Set Up Surfshark {#set-up-surfshark}

[Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Seleziona i server.

    Seleziona il server o i server a cui vuoi connetterti, quindi fai clic su **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Refresh.

    Puoi fare clic su **Refresh** per aggiornare la chiave pubblica quando il server VPN non puo' essere raggiunto.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Set Up Windscribe {#set-up-windscribe}

[Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**. Verranno generati i file di configurazione per ciascun server.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Seleziona i server.

    Seleziona il server o i server a cui vuoi connetterti, quindi fai clic su **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Riceverai poi un elenco di file di configurazione corrispondenti ai server selezionati.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Avvia una connessione.

    Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Una volta connesso, comparira' un punto verde accanto al file di configurazione.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    I dettagli della connessione VPN verranno mostrati anche nel **VPN Dashboard**.

    ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. Aggiorna i server.

    Puoi fare clic su **Update Servers** per ottenere l'elenco piu' recente dei server disponibili, evitando errori di connessione dovuti a manutenzione o dismissione dei server.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Modifica le credenziali o esegui il logout.

    Fai clic sull'icona a ingranaggio per modificare le credenziali di accesso oppure per uscire.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Refresh.

    Puoi fare clic su **Refresh** per aggiornare la chiave pubblica quando il server VPN non puo' essere raggiunto.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Delete All.

    Puoi fare clic su **Delete All** per eliminare tutti i file di configurazione con un solo clic e scegliere se eliminare contemporaneamente anche le chiavi privata e pubblica.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Set Up WireGuard Client Manually (for other providers) {#set-up-wireguard-client-manually-for-other-providers}

Se usi un altro provider di servizi WireGuard, puoi scaricare i file di configurazione WireGuard e seguire i passaggi seguenti per configurare WireGuard Client. Se non sai come scaricare i file di configurazione, fai riferimento a [questa guida](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oppure contatta il relativo supporto.

Nel pannello di amministrazione web, vai su **VPN** -> **WireGuard Client**.

1. Fai clic su **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. Verra' creato un gruppo nella barra laterale sinistra.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Imposta un nome descrittivo per il gruppo, ad esempio azirevpn. Poi carica un file di configurazione, formati supportati: zip, tar, gz, conf, txt, oppure aggiungi manualmente i dettagli della configurazione, in formato testo.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Upload a configuration file**.

        Fai clic sull'area di caricamento per caricare il file di configurazione WireGuard, quindi fai clic su **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Manually add configuration**.

        Fai clic su **Manually Add Configuration** nella parte inferiore dell'area di caricamento.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Imposta un nome descrittivo e incolla la configurazione nella casella di testo. Poi fai clic su **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        Se vuoi verificare ogni voce, puoi passare alla Item mode e controllare i dettagli della configurazione. Poi fai clic su **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. Una volta connesso, puoi controllare lo stato della connessione nella pagina **VPN Dashboard**.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Configurare WireGuard Server su router GL.iNet

Non vuoi abbonarti a servizi VPN di terze parti? Puoi acquistare due router GL.iNet: impostarne uno come WireGuard server e l'altro come WireGuard server.

Questo scenario e' particolarmente adatto quando il tuo ISP domestico fornisce un IP pubblico e vuoi collegarti alla rete di casa tramite VPN quando sei fuori casa, per garantire sicurezza e accesso alle risorse della rete interna. In questo modo elimini costi e complicazioni dovuti ad abbonamenti continui a servizi VPN commerciali.

Per la configurazione di WireGuard server, consulta [qui](wireguard_server.md).

---

WireGuard® e' un marchio registrato di Jason A.Donenfeld.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
