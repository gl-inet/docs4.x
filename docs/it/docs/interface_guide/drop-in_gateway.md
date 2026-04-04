# Drop-in Gateway

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway e' una funzione di estensione che consente di ampliare le capacita' di un router principale esistente senza sostituirlo o riconfigurarlo. Collegando il router GL.iNet al router principale tramite un cavo Ethernet, gli utenti possono aggiungere funzioni di rete avanzate all'infrastruttura di rete esistente, ad esempio:

- Filtrare la pubblicita' tramite AdGuard Home
- Abilitare il client VPN
- Usare DNS crittografato

Si consiglia di usare un router o un security gateway con prestazioni piu' elevate e memoria sufficiente, ad esempio GL-MT2500 o GL-MT5000, e di installare strumenti aggiuntivi per l'inoltro e il controllo del traffico secondo necessita'.

## Topologia di rete

Drop-in Gateway funziona come un sistema di rete intermedio, instradando il traffico dati dei dispositivi client attraverso il router GL.iNet per l'elaborazione prima di trasmetterlo tramite il router principale. Durante questo processo non solo preserva le impostazioni di rete esistenti, ad esempio SSID e password, per garantire una connettivita' ininterrotta a tutti i dispositivi connessi, ma consente anche di gestire il traffico di rete per tutti o per specifici dispositivi client secondo necessita'.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

Il diagramma sopra e' composto da due tipi di linee: linee grigie e linee verdi contrassegnate da tre frecce, ciascuna etichettata con un numero corrispondente.

1. Le **linee grigie** illustrano la topologia di connessione fisica: i dispositivi client, ad esempio computer e laptop, si collegano al router principale e la porta LAN del router principale e' collegata tramite cavo Ethernet alla porta WAN del router GL.iNet, con Drop-in Gateway abilitato.

2. Le **linee verdi** mostrano il percorso sequenziale di trasmissione dei dati quando Drop-in Gateway e' attivo; le frecce numerate indicano l'ordine del flusso del traffico:

    1. Il traffico dei dispositivi client viene prima instradato verso il router principale;

    2. Il router principale inoltra il traffico al router GL.iNet per l'elaborazione, ad esempio filtraggio pubblicitario o crittografia VPN;

    3. Dopo l'elaborazione, il traffico viene rimandato al router principale, che quindi consegna i dati finali ai dispositivi client originali oppure li instrada verso Internet.

## Configurazione

Sono disponibili due modalita' di deployment per diversi scenari applicativi: tutti i dispositivi client sono collegati tramite Drop-in Gateway oppure solo specifici dispositivi client sono collegati tramite Drop-in Gateway.

Nell'esempio seguente, l'indirizzo gateway del router principale e' `192.168.1.1`.

### Tutti i dispositivi sono collegati tramite Drop-in Gateway {all-devices-managed-by-the-drop-in-gateway}

1. Collega la porta LAN del router principale alla porta WAN del router GL.iNet tramite un cavo Ethernet.

2. Accedi al pannello di amministrazione web del router GL.iNet, abilita Drop-in Gateway e il sistema generera' automaticamente i parametri di configurazione corrispondenti.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** si riferisce all'indirizzo IP WAN del router GL.iNet, assegnato dinamicamente dal router principale. Questo IP WAN puo' essere visualizzato nella sezione Ethernet della pagina [INTERNET](internet_ethernet.md).

    - I campi **Gateway** e **DNS Server 1** vengono compilati automaticamente con l'indirizzo IP del router principale per impostazione predefinita. Se questi parametri sono configurati in modo errato, puoi regolarli manualmente secondo necessita'.

    Annota questo indirizzo IP, perche' verra' usato nei passaggi successivi.

    Seleziona il primo metodo di configurazione e fai clic su **Apply**.

3. Accedi al pannello di amministrazione web del router principale.

    ??? "GL.iNet"

        Se il tuo router principale e' GL.iNet e usa firmware v4.2 o superiore, segui i passaggi sotto.

        Accedi al pannello di amministrazione web -> NETWORK -> LAN -> DHCP Server -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Inserisci nel campo DHCP Gateway l'indirizzo IP del passaggio 2, ad esempio `192.168.1.23`, quindi fai clic su **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Se il tuo router principale e' TP-Link, segui i passaggi sotto, usando TP-LINK Archer C3150 come esempio.

        Accedi alla pagina di amministrazione TP-Link, vai su **Advanced** -> **Network** -> **DHCP Server**, quindi disabilita **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Poi fai clic su **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Se il tuo router principale e' Linksys, segui i passaggi sotto, usando Linksys WHW01 come esempio.

        Accedi alla pagina di amministrazione Linksys, vai su **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Fai clic sulla scheda **Local Network**, disabilita **DHCP Server**, quindi fai clic su **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        Comparira' un avviso. Fai clic su **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        Accedi al pannello di amministrazione del router principale per disabilitare il relativo server DHCP. Puoi fare riferimento al manuale utente del produttore corrispondente oppure contattare il relativo supporto.

4. Torna al router GL.iNet e configura le funzioni necessarie, come [AdGuard Home](adguardhome.md), [DNS crittografato](dns.md), [WireGuard Client](wireguard_client.md) e [OpenVPN Client](openvpn_client.md).

### Dispositivi specifici sono collegati tramite Drop-in Gateway {some-devices-managed-by-the-drop-in-gateway}

1. Collega la porta LAN del router principale alla porta WAN del router GL.iNet tramite un cavo Ethernet.

2. Accedi al pannello di amministrazione web del router GL.iNet, abilita Drop-in Gateway e il sistema generera' automaticamente i parametri di configurazione corrispondenti.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** si riferisce all'indirizzo IP WAN del router GL.iNet, assegnato dinamicamente dal router principale. Questo IP WAN puo' essere visualizzato nella sezione Ethernet della pagina [INTERNET](internet_ethernet.md).

    - I campi **Gateway** e **DNS Server 1** vengono compilati automaticamente con l'indirizzo IP del router principale per impostazione predefinita. Se questi parametri sono configurati in modo errato, puoi regolarli manualmente secondo necessita'.

    Annota questo indirizzo IP, perche' verra' usato nei passaggi successivi.

    Seleziona il secondo metodo di configurazione e fai clic su **Apply**.

3. Imposta il gateway e il DNS sul dispositivo su cui vuoi usare la funzione Drop-in Gateway con lo stesso indirizzo IP mostrato nella pagina Drop-in Gateway.

    ??? "Windows"

        Questo e' un esempio per Windows 11; Windows 10 e' simile. Assicurati che il PC sia collegato al router principale. Qui si presume che il computer sia collegato al router principale tramite cavo di rete; la configurazione e' simile anche se ti colleghi via Wi-Fi.

        1. Apri Settings.

        2. Fai clic su **Network & Internet**.

        3. Fai clic sulla scheda **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Troverai l'indirizzo IP di questo PC. Nella sezione "IP assignment", fai clic sul pulsante **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Seleziona l'opzione **Manual**. Attiva l'interruttore **IPv4**.

        6. Imposta **IP address** con l'indirizzo IP visto al passaggio 4, **Subnet mask** con `255.255.255.0` e sia **Gateway** sia **Preferred DNS** con l'indirizzo IP indicato nella pagina Drop-in Gateway.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Fai clic sul pulsante **Save**.

    ??? "Android"

        Questo e' un esempio con Samsung S21. Assicurati che lo smartphone sia collegato al router principale.

        1. Apri Settings e fai clic su Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Fai clic su Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Fai clic sull'icona a forma di ingranaggio dell'SSID corrente.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Fai clic su **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Fai clic su **IP settings** e scegli **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Imposta **Gateway** e **DNS 1** con l'indirizzo IP mostrato nella pagina Drop-in Gateway, quindi fai clic su **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Questo e' un esempio di iOS 16.3 su iPhone 8. Assicurati che lo smartphone sia collegato al router principale.

        1. Apri Settings e fai clic su Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Fai clic sull'SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Scorri verso il basso e troverai **Configure IP** impostato su **Automatic**. Annota **IP Address** e **Subnet Mask** per il passaggio successivo.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Cambia **Configure IP** in **Manual**, imposta **IP Address** e **Subnet Mask** con gli stessi valori ottenuti nel passaggio precedente e imposta **Router** con l'indirizzo IP mostrato nella pagina Drop-in Gateway, quindi fai clic su **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Fai clic su **Configure DNS** e cambialo in **Manual**. Fai clic su **Add Server**, imposta l'indirizzo IP del server DNS con l'indirizzo IP mostrato nella pagina Drop-in Gateway, quindi fai clic su **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Torna al pannello di amministrazione web del router GL.iNet e configura le funzioni necessarie, come [AdGuard Home](adguardhome.md), [DNS crittografato](dns.md), [WireGuard Client](wireguard_client.md) e [OpenVPN Client](openvpn_client.md).

## Avvertenze

1. L'abilitazione di Drop-in Gateway aumenta la latenza di rete.

2. Quando Drop-in Gateway e' abilitato, anche la trasmissione dati tra i dispositivi LAN selezionati viene instradata tramite il drop-in gateway. La larghezza di banda tra il router principale e il drop-in gateway influisce quindi sulla larghezza di banda complessiva della LAN.

---

Articolo correlato:

- [Come configurare Drop-in Gateway su un router GL.iNet](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
