# Collegare i router GL.iNet a una rete EAP {#connect-glinet-routers-to-an-eap-network}

Alcuni router GL.iNet supportano la connessione a reti Wi-Fi EAP (Extensible Authentication Protocol) come ripetitori.

EAP è un framework di autenticazione comunemente usato con **autenticazione 802.1X** per reti **WPA2-Enterprise / WPA3-Enterprise**. Un esempio tipico è **eduroam**, un servizio globale di roaming Wi-Fi per istruzione e ricerca basato su 802.1X ed EAP.

Questo framework prevede diversi metodi di autenticazione EAP, tra cui EAP-PEAP, EAP-TLS, EAP-TTLS ed EAP-FAST. Non tutti i metodi EAP sono supportati da tutte le interfacce e da tutti i modelli di router.

Questa guida presenta due modi per collegare i router GL.iNet a una rete Wi-Fi EAP: tramite il pannello di amministrazione web GL.iNet e tramite LuCI. I due modi offrono metodi di autenticazione EAP diversi: il primo offre solo **EAP-PEAP**, mentre il secondo offre **EAP-TLS**, **EAP-TTLS**, **EAP-PEAP** ed **EAP-FAST**.

Alcuni router GL.iNet supportano la funzione di ripetitore EAP solo tramite uno di questi due modi. Consulta i modelli supportati di seguito.

### Modelli supportati {#supported-models}

??? "Modelli supportati"
    - <u>GL-MG1300 (Mango 2)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-AX1800 (Flint)</u><sup>1</sup>
    - <u>GL-AXT1800 (Slate AX)</u><sup>1</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - <u>GL-E750/GL-E750V2 (Mudi)</u><sup>1</sup>
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

    ---

    **Nota:**

    1. GL-MG1300 (Mango 2), GL-AX1800 (Flint), GL-AXT1800 (Slate AX) e GL-E750/GL-E750V2 (Mudi) possono connettersi come ripetitori a reti EAP-PEAP tramite il pannello di amministrazione web GL.iNet e a reti EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST tramite LuCI.

    2. GL-MT6000 (Flint 2) e GL-MT3000 (Beryl AX) non supportano la connessione a reti EAP come ripetitori con il firmware predefinito. Tuttavia, GL.iNet fornisce firmware OpenWrt con supporto EAP per questi modelli. Dopo aver installato questo firmware, puoi impostare il router in modalità ripetitore e connetterlo a reti EAP-PEAP tramite il pannello di amministrazione web GL.iNet oppure a reti EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST tramite LuCI.

        Cerca il tuo modello nel [Download Center](https://dl.gl-inet.com/){target="_blank"} e seleziona la scheda OpenWrt per scaricarlo se necessario.

    3. GL-SFT1200 (Opal) supporta la connessione a reti EAP come ripetitore a partire dal firmware v4.8, sia tramite il pannello di amministrazione web GL.iNet (EAP-PEAP) sia tramite LuCI (EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST).

    4. Tutti gli altri modelli sopra elencati supportano la connessione a reti EAP-PEAP come ripetitori solo tramite il pannello di amministrazione web GL.iNet. Altri metodi EAP (EAP-TLS, EAP-TTLS, EAP-FAST, ecc.) non sono supportati.

??? "Modelli non supportati"
    - GL-MT6000 (Fortify)
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Connessione tramite pannello di amministrazione web {#connect-via-web-admin-panel}

Tramite il pannello di amministrazione web GL.iNet puoi collegare il router a reti EAP-PEAP come ripetitore.

1. Accedi al pannello di amministrazione web, vai su **INTERNET** -> sezione **Repeater**, quindi fai clic su **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    Verrà eseguita una scansione delle reti disponibili. Trova e seleziona l'SSID EAP a cui connetterti.

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Oppure fai clic su **Join Other Network** in alto a destra per unirti manualmente alla rete EAP.

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Inserisci l'**SSID**.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Seleziona **Security** come WPA/WPA2/WPA3 Enterprise.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Inserisci **Username** e **Password**, quindi fai clic su **Apply** per connetterti.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Connessione tramite LuCI {#connect-via-luci}

Tramite LuCI puoi collegare il router a una rete EAP-TLS, EAP-TTLS, EAP-PEAP o EAP-FAST come ripetitore.

I passaggi seguenti sono solo di riferimento. Consulta la pagina LuCI effettiva del tuo dispositivo.

1. Accedi al pannello di amministrazione web, vai su **SYSTEM** -> **Advanced Settings**. Installa LuCI e fai clic su **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Accedi all'interfaccia LuCI con la stessa password amministratore e vai su Network -> Wireless.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Fai clic su **Scan** nella sezione 2.4G o 5G.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Unisciti alla rete desiderata.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Risoluzione dei problemi {#troubleshooting}

Se la rete EAP di destinazione richiede parametri aggiuntivi, come tipo EAP, ad esempio PEAP o TTLS, domain suffix match, identity, anonymous identity e così via, la connessione EAP tramite pannello di amministrazione web potrebbe fallire.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

Segui i passaggi seguenti per collegare il router GL.iNet a reti EAP che richiedono impostazioni avanzate tramite interfaccia LuCI.

1. Ottieni le configurazioni.

    Ottieni in anticipo i parametri di configurazione per la rete EAP di destinazione. Ad esempio:

    - Tipo EAP, ad esempio PEAP, TTLS, TLS
    - Suffix del dominio di autenticazione, ad esempio @company.com
    - Identity, di solito il nome utente completo
    - Anonymous Identity, opzionale
    - Tipo di autenticazione interna, ad esempio MSCHAPv2, PAP
    - Certificato CA, se richiesto, prepara un file in formato .crt

    Questo è un esempio di rete Wi-Fi Xfinity Mobile come riferimento.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Accedi a LuCI.

    Accedi al pannello di amministrazione web del router. Dopo il login, se in precedenza avevi provato a collegarti alla rete EAP di destinazione tramite WebGUI ma senza successo, interrompi la connessione.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    Poi vai su **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Accedi a LuCI con la stessa password amministratore.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Configura Repeater in LuCI.

    Nell'interfaccia LuCI, vai su Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    Fai clic sul pulsante **Scan** nella sezione 5G o 2.4G per cercare le reti Wi-Fi disponibili.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    Trova la rete EAP di destinazione nei risultati della scansione e fai clic su **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    Nella pagina "Joining Network", inserisci la **WPA passphrase** e fai clic su **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    Verrai reindirizzato alla configurazione Wireless Client.

4. Individua **Interface Configuration** -> **Wireless Security**.

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    Seleziona o inserisci i parametri di configurazione corretti in base alla rete EAP di destinazione, come mostrato di seguito. **Non fare ancora clic su Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. Passa alla scheda **Advanced Settings**, specifica un nome interfaccia, ad esempio **wlan0**. Poi fai clic su **Save** nell'angolo in basso a destra.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. Tornerai alla pagina Wireless, che mostrerà le modifiche in sospeso. Fai clic sul pulsante **Save & Apply** nell'angolo in basso a destra.

    ![save and apply](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    Il router verrà collegato correttamente alla rete EAP di destinazione.

7. Verifica la connessione.

    ??? "Controlla la connessione nella WebGUI"

        Una volta che il router si connette correttamente alla rete EAP di destinazione, un'icona repeater si accenderà nella WebGUI, come mostrato di seguito.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Nota**: poiché la configurazione in LuCI non viene sincronizzata con quella della WebGUI, i dettagli dell'interfaccia repeater, ad esempio IP connesso, gateway e così via, non appariranno nella WebGUI.

        Come mostrato nell'immagine, la sezione repeater in basso è vuota. Tuttavia, il router è già collegato alla rete EAP di destinazione come repeater, perché l'icona repeater in alto è accesa.

    ??? "Controlla la connessione tramite SSH"

        1. Accedi al router tramite [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"}.

        2. Inserisci **ifconfig** e premi Invio.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            Potrai controllare lo stato dell'interfaccia **wlan0**.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
