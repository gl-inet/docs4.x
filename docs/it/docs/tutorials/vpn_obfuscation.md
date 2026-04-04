# Come configurare l'offuscamento VPN sui router GL.iNet

## Che cos'e l'offuscamento VPN

L'offuscamento VPN e una tecnica che maschera il traffico VPN facendolo sembrare normale traffico Internet. Questo aiuta gli utenti ad aggirare restrizioni di rete e censura, soprattutto in aree con politiche Internet rigide.

- Nasconde le caratteristiche della VPN per evitare il rilevamento da parte di ISP, firewall o Deep Packet Inspection, DPI.

- Fa apparire la connessione VPN come traffico web standard, migliorando stabilita della connessione e probabilita di successo in reti con restrizioni.

## Che cos'e AmneziaWG

AmneziaWG e un protocollo VPN basato su WireGuard, con offuscamento del traffico integrato. Mantiene i vantaggi principali di WireGuard, come alta velocita, design leggero e bassa latenza, aggiungendo al tempo stesso un modulo dedicato all'offuscamento. Questo modulo nasconde efficacemente i modelli di traffico VPN, consentendo sia agli utenti individuali sia alle aziende di proteggere la privacy online, aggirare restrizioni regionali ed evitare interruzioni della connessione causate da controlli di rete severi.

AmneziaWG e compatibile con un'ampia gamma di dispositivi, inclusi Windows, macOS, iOS, Android, Linux e router, offrendo connessioni VPN offuscate affidabili in ogni scenario.

Attualmente, diversi router GL.iNet, ad esempio **Brume 3**, **Flint 3**, **Flint 2** e **Beryl AX**, supportano il protocollo AmneziaWG in alcune versioni firmware selezionate. Il supporto ufficiale completo sara disponibile nel firmware ver.4.9 e verra gradualmente esteso ad altri modelli.

## Configurazione rapida

Di seguito trovi due scenari tipici per configurare l'offuscamento VPN AmneziaWG sui router GL.iNet.

### Scenario 1. Usare due router GL.iNet

Questo scenario usa due router GL.iNet per stabilire una connessione VPN offuscata tramite il protocollo AmneziaWG.

- **Brume 3 (GL-MT5000)**: agisce come server VPN per l'uso domestico.
- **Beryl AX (GL-MT3000)**: agisce come client VPN portatile per l'uso in viaggio.

#### Configurare il server VPN

1. Accedi al pannello di amministrazione web di Brume 3.

    Collega un dispositivo, ad esempio il tuo laptop o PC, alla porta LAN di Brume 3 tramite cavo Ethernet. Apri un browser e inserisci l'indirizzo di amministrazione predefinito, di solito `192.168.8.1`, quindi accedi con la tua password amministratore.

2. Completa la configurazione iniziale di Brume 3 per l'accesso a Internet.

    Se Brume 3 viene usato come router principale, collega la sua porta WAN alla rete upstream, ad esempio un modem ISP.

    Se non e il router principale, vale a dire se esiste un altro dispositivo upstream, come un router ISP, che agisce come router principale, e necessaria una configurazione di **port forwarding** sul router principale. Fai riferimento a [questo link](how_to_set_up_port_forwarding.md).

3. Abilita DDNS, facoltativo.

    Abilita la funzione DDNS se il tuo IP pubblico non e statico ma dinamico.

    Dalla barra laterale sinistra, vai su **APPLICATIONS** -> **Dynamic DNS**. Attiva **Enable DDNS**, accetta **Terms of Service & Privacy Policy**, quindi fai clic su **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. Abilita l'offuscamento VPN.

    Dalla barra laterale sinistra, vai su **VPN** > **WireGuard Server** -> scheda **Configurations**, attiva **Enable Obfuscation**, quindi fai clic su **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    Puoi personalizzare i parametri di offuscamento secondo le tue esigenze. Ti consigliamo di mantenere le impostazioni predefinite.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Esporta il file di configurazione.

    Nella pagina **WireGuard Server**, passa alla scheda **Profiles** e fai clic sul pulsante **Add** per creare un file di configurazione con cui Beryl AX potra collegarsi.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Imposta un nome descrittivo, ad esempio Travel Router, quindi fai clic su **Apply**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    Nella finestra pop-up, fai clic su **Export** per scaricare la configurazione in locale, che verra usata successivamente.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Avvia il server VPN.

    Nella parte superiore della pagina **WireGuard Server**, fai clic sul pulsante **Start** per avviare il server.

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    A questo punto il server VPN con offuscamento AmneziaWG e abilitato. Ora puoi collegarti a questo server VPN Brume 3 tramite l'app AmneziaWG oppure con un router GL.iNet che esegue un firmware che supporta l'offuscamento AmneziaWG.

    **Nota: i client che non supportano l'offuscamento AmneziaWG non riusciranno a collegarsi.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### Configurare il client VPN

1. Accedi al pannello di amministrazione web di Beryl AX.

    Collega un dispositivo, ad esempio il tuo laptop o PC, al Wi-Fi o alla porta LAN di Beryl AX tramite cavo Ethernet. Apri un browser e inserisci l'indirizzo di amministrazione predefinito, di solito `192.168.8.1`, quindi accedi con la tua password amministratore.

2. Completa la configurazione iniziale di Beryl AX per l'accesso a Internet.

    **Suggerimento**: collega Beryl AX a una rete diversa da quella di Brume 3. Ad esempio, puoi abilitare un hotspot mobile a cui collegare Beryl AX.

3. Carica il file di configurazione.

    Dalla barra laterale sinistra, vai su **VPN** > **WireGuard Client**. Aggiungi un nuovo gruppo e imposta un nome descrittivo, ad esempio Home Router.

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Carica sul lato destro il file di configurazione esportato in precedenza.

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    Dopo aver caricato il file di configurazione e aver superato la verifica, fai clic su **Apply**.

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    La pagina verra aggiornata e vedrai un file di configurazione nell'elenco.

4. Avvia la connessione VPN.

    Fai clic sull'icona con i tre puntini e poi seleziona **Start**.

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Attendi circa 1 minuto. Se l'indicatore di stato diventa verde, significa che la connessione VPN e riuscita.

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Vai su **VPN Dashboard** e vedrai che Beryl AX e connesso al router domestico Brume 3.

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Doppio controllo, facoltativo.

    Accedi al pannello di amministrazione web di Brume 3 e vai su **VPN** -> **WireGuard Server**. Vedrai anche un client online, cioe Beryl AX, attualmente connesso a questo server VPN Brume 3.

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    La connessione VPN e completa. Tutti i dispositivi collegati a Beryl AX ora accedono a Internet tramite il gateway di Brume 3, ottenendo cosi una connessione VPN offuscata.

### Scenario 2. Usare un singolo router GL.iNet

Questo scenario usa un singolo router GL.iNet **Brume 3 (GL-MT5000)** come client VPN per collegarsi a un server AmneziaVPN.

In questo caso non e necessario distribuire un server personale. Basta scaricare un file di configurazione AmneziaWG dal [sito ufficiale di Amnezia](https://amnezia.org/){target="_blank"} o da qualsiasi provider VPN che integri AmneziaWG, quindi caricare il file sul router GL.iNet. Potrai cosi stabilire una connessione VPN con offuscamento abilitato.

#### Scaricare la configurazione

<u>Opzione 1</u>: scarica una configurazione da Amnezia Official, e richiesto un abbonamento Premium.

1. Accedi alla [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} con la tua Subscription Key.

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Nella dashboard di Amnezia, vai su **Connection Assets** -> **Configuration Files**, seleziona un Paese e scarica un file di configurazione in locale per usarlo successivamente.

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Opzione 2</u>: scarica una configurazione da un altro provider VPN che integri AmneziaWG.

Prendiamo come esempio StarVPN.

1. Vai ai [piani tariffari](https://www.starvpn.com/#pricing){target="_blank"} di StarVPN e scegli il piano VPN piu adatto alle tue esigenze. Puoi registrare un account StarVPN durante il checkout oppure direttamente [qui](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

2. Accedi alla [StarVPN Dashboard](https://www.starvpn.com/dashboard){target="_blank"}, individua **VPN Configuration** e fai clic su **AmneziaWG Config** per scaricare il file di configurazione.

    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. La configurazione puo contenere un indirizzo IPv6. Per evitare problemi di compatibilita e connettivita, apri il file `.conf` e rimuovi l'indirizzo IPv6, come mostrato sotto.

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Poi segui i passaggi sotto per configurare il client VPN.

#### Configurare il client VPN

1. Accedi al pannello di amministrazione web di Brume 3.

    Collega un dispositivo, ad esempio il tuo laptop o PC, alla porta LAN di Brume 3 tramite cavo Ethernet. Apri un browser e inserisci l'indirizzo di amministrazione predefinito, di solito `192.168.8.1`, quindi accedi con la tua password amministratore.

2. Completa la configurazione iniziale di Brume 3 per l'accesso a Internet.

3. Carica il file di configurazione.

    Dalla barra laterale sinistra, vai su **VPN** > **WireGuard Client**. Aggiungi un nuovo gruppo e imposta un nome descrittivo, ad esempio AmneziaVPN.

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Carica sul lato destro il file di configurazione AmneziaVPN esportato in precedenza.

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    Dopo aver caricato il file di configurazione e aver superato la verifica, fai clic su **Apply**.

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    La pagina verra aggiornata e vedrai un file di configurazione nell'elenco.

4. Avvia la connessione VPN.

    Fai clic sull'icona con i tre puntini e poi seleziona **Start**.

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Attendi circa 1 minuto. Se l'indicatore di stato diventa verde, significa che la connessione VPN e riuscita.

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Vai su **VPN Dashboard** e vedrai che Brume 3 e connesso a un server AmneziaVPN.

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

    La connessione VPN e completa. Tutti i dispositivi collegati a Brume 3 ora accedono a Internet tramite il server AmneziaVPN, ottenendo cosi una connessione VPN offuscata.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
