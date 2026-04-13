# Impossibile accedere al pannello di amministrazione web

A volte potresti non riuscire ad accedere a [http://192.168.8.1](http://192.168.8.1) e quindi non riuscire ad accedere al pannello di amministrazione web. Le cause possibili possono essere diverse.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Possibili cause

* Il computer o il telefono cellulare non è collegato al router.
* `192.168.8.1` è l'indirizzo IP predefinito del router. Potresti aver modificato questo IP.
* La cache o un'estensione del browser possono rendere il pannello di amministrazione inaccessibile.
* Un software VPN o proxy gestisce il traffico, rendendo il pannello di amministrazione inaccessibile.
* Il router è bloccato.

## Controlla i passaggi generali per accedere al pannello di amministrazione web

1. Accendi il router senza collegarlo ad alcun dispositivo.
2. Collega il telefono o il laptop al Wi-Fi del router e inserisci la chiave Wi-Fi stampata sull'etichetta del router.
3. Se il passaggio 2 non riesce, disattiva il Wi-Fi sul computer/laptop. Collegalo invece alla porta LAN del router tramite un cavo Ethernet.
4. Apri un browser, digita `192.168.8.1` nella barra degli indirizzi e premi Invio. Dovresti riuscire a visitare il pannello di amministrazione web GL.iNet.

In alternativa, puoi usare [l'app](mobile_app.md) per accedere al router.

## Altri passaggi per risolvere il problema

1. [Controlla la connessione](#controlla-la-connessione)
2. [Controlla IP del router](#controlla-ip-del-router)
3. [Accedi tramite IP del router](#accedi-tramite-ip-del-router)

---

### Controlla la connessione

Se sei collegato tramite cavo Ethernet, assicurati che il collegamento WAN/LAN del router sia corretto:

- La porta WAN è collegata a una sorgente Internet, ad esempio un modem o un router principale.
- La porta LAN è collegata al dispositivo terminale, ad esempio il tuo laptop.

Se sei collegato tramite Wi-Fi, assicurati di aver selezionato sul dispositivo l'SSID corretto e di aver inserito la password corretta.

### Controlla IP del router

Segui i passaggi seguenti per controllare l'indirizzo IP del router.

=== "Windows 10 / Windows 11"

    Accedi al Pannello di controllo e assicurati che nell'angolo in alto a destra sia selezionata la visualizzazione con icone grandi o piccole.

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    Pannello di controllo -> Centro connessioni di rete e condivisione -> fai clic sulla connessione. Potresti avere più connessioni: scegli quella corrispondente al router che vuoi controllare.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    Si aprirà una finestra con lo stato della connessione. Fai clic sul pulsante dei dettagli.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    Si aprirà una finestra con i dettagli della connessione di rete: l'indirizzo IP del router corrisponde a **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Pannello di controllo -> Rete e Internet -> Centro connessioni di rete e condivisione -> Modifica impostazioni scheda

    Fai clic con il tasto destro sulla rete -> Stato -> Dettagli

    L'indirizzo IP del router corrisponde a **IPv4 Default Gateway**

    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. Preferenze di Sistema -> Rete

    2. Nella colonna di sinistra, fai clic sulla connessione di rete. Per una connessione Ethernet, verrà mostrato l'indirizzo IP del router.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Per una connessione Wi-Fi, fai clic sul pulsante "Advanced..." e poi sulla scheda "TCP/IP" nella parte superiore della finestra. Verrà mostrato l'indirizzo IP del router.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Impostazioni -> Wi-Fi
    2. Tocca l'icona delle informazioni (i blu in un cerchio) della rete Wi-Fi a cui sei attualmente connesso. Verrà mostrato l'indirizzo IP del router.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Questa procedura può variare a seconda del dispositivo Android.

    1. Impostazioni -> Rete e Internet
    2. Tocca Wi-Fi e trova la rete a cui sei connesso; fai clic sull'icona delle impostazioni per gestirne la configurazione
    3. Tocca il menu a discesa Advanced. Se ti propone le opzioni Static o Dynamic IPs, seleziona Static
    4. In ogni caso, dovresti vedere l'IP del router sotto Gateway.

### Accedi tramite IP del router

1. Usa Chrome/Edge/Safari per accedere al pannello di amministrazione del router, per una migliore compatibilità.

2. Per evitare problemi causati dalla cache e dalle estensioni del browser, apri una finestra in incognito e prova nuovamente ad accedere all'indirizzo IP del router.

3. Disabilita eventuali software VPN o proxy, inclusi Tailscale e ZeroTier.

4. Se stai usando un telefono cellulare, disattiva i dati mobili.

    Alcuni smartphone si disconnettono dal Wi-Fi del router e usano invece i dati mobili quando rilevano che il router non ha accesso a Internet. Tuttavia, la disconnessione dal router impedisce l'accesso al pannello di amministrazione web.

5. Se i passaggi sopra non hanno funzionato, prova a [ripristinare](repair_network_or_reset_firmware.md#reset-to-factory) il router alle impostazioni di fabbrica.

6. Se il ripristino non funziona, prova a [sbloccare tramite uboot](debrick.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
