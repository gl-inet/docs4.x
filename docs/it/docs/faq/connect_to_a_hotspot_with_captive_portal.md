# Collegare un router GL.iNet agli hotspot pubblici con Captive Portal

## Che cos'è un captive portal?

Un captive portal è una pagina web in cui gli hotspot pubblici richiedono agli utenti di visualizzare e interagire con la pagina prima di concedere l'accesso a Internet.

## Perché usare un router con gli hotspot pubblici?

* Il Wi-Fi pubblico non è sicuro

    È difficile sopravvalutare i rischi del Wi-Fi pubblico. Collegando il router GL.iNet a una rete Wi-Fi pubblica, puoi accedere direttamente al tuo account VPN tramite il pannello di amministrazione del router. Il router crittograferà automaticamente tutti i dispositivi collegati alla rete locale, evitando di dover configurare una VPN su ogni singolo dispositivo.

* Usalo come repeater per consentire la connessione di più dispositivi

    Inoltre, alcune reti Wi-Fi pubbliche (ad esempio il Wi-Fi degli hotel) limitano l'accesso, per esempio, a due dispositivi. Quando si viaggia in gruppo, questo è poco pratico. In alternativa, puoi collegare un travel router al Wi-Fi dell'hotel e usarlo come repeater per trasmettere un segnale Wi-Fi a tutti i tuoi dispositivi, inclusi laptop, smartphone, tablet e così via. Il Wi-Fi dell'hotel riconoscerà il travel router come un singolo dispositivo, ma tu potrai collegare tutti i dispositivi che desideri alla rete Wi-Fi gratuita.

## Come collegare il router agli hotspot pubblici con captive portal?

Guarda questo video oppure segui i passaggi seguenti.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Collega uno smartphone o un computer al router.

    Accendi il router. Sullo smartphone o sul computer, cerca l'SSID del router e inserisci la password Wi-Fi. L'SSID e la password predefiniti sono stampati nella parte inferiore del router.

2. Accedi al pannello di amministrazione web del router.

    Sullo smartphone o sul computer, apri un browser web e inserisci nella barra degli indirizzi l'indirizzo IP del router (IP predefinito: `192.168.8.1`). Potrai accedere al pannello di amministrazione web del router.

    Se accedi per la prima volta, seleziona una lingua e crea una password di accesso per il pannello di amministrazione web del router.

3. Collega il router all'hotspot pubblico. Fai riferimento al tutorial [Repeater](../interface_guide/internet_repeater.md/).

## Risoluzione dei problemi

Se non riesci ad aprire il captive portal, il router potrebbe non riuscire ad accedere a Internet. Prova i seguenti metodi per la risoluzione dei problemi.

### Metodo 1: abilita Public Hotspot Login Mode & Camouflage

**Nota**: queste due funzioni sono disponibili solo nel firmware v4.6 e successivi.

Quando colleghi il router a un hotspot pubblico, nella pagina **Join Network**, abilitare le seguenti funzioni può aiutare ad aumentare il tasso di successo della connessione.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    Se questa opzione è abilitata, il router entrerà automaticamente in Login Mode for Public Hotspots quando si collega correttamente a un hotspot ma non a Internet. In questa modalità, alcuni servizi verranno sospesi mentre la modalità DNS passerà ad automatica, il che potrebbe esporre la tua attività di rete al provider dell'hotspot (ad esempio hotel o centri commerciali).

- Enable Camouflage

    Se abilitata, il router si maschererà come il dispositivo client che usi per accedere al pannello di amministrazione, emulando l'indirizzo MAC di quel dispositivo.

---

### Metodo 2: cambia le impostazioni del router

1. Accedi al pannello di amministrazione web e vai a NETWORK -> DNS. Assicurati che **DNS Rebinding Attack Protection** sia disabilitato e che **Mode** sia impostato su **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. Nel pannello di amministrazione web, vai a VPN -> VPN Dashboard. Assicurati che tutte le connessioni VPN siano disabilitate.

    **Per firmware v4.7 e precedenti**, la pagina viene visualizzata come segue.

    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}

    **Per firmware v4.8 e successivi**, la pagina viene visualizzata come segue.

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. Nel pannello di amministrazione web, vai a APPLICATIONS -> AdGuard Home. Assicurati che AdGuard Home sia disabilitato.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Apri un browser web, reinserisci o aggiorna la pagina del captive portal. Attendi un minuto e controlla se viene reindirizzato automaticamente alla pagina di autenticazione del captive portal.

    Se stai usando uno smartphone e il browser non reindirizza al captive portal, disattiva il Wi-Fi dello smartphone e poi riattivalo, quindi ricollegati al Wi-Fi del router. Il captive portal dovrebbe comparire direttamente dopo aver inserito la password Wi-Fi.

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Metodo 3：MAC Clone

Alcuni hotel limitano il numero di dispositivi che ogni cliente può collegare al Wi-Fi dell'hotel riconoscendone l'indirizzo MAC, e registrano il MAC del dispositivo al primo collegamento. In questo caso, puoi clonare sul router l'indirizzo MAC che il telefono usa per connettersi al Wi-Fi dell'hotel, permettendo al router di usare quel MAC per accedere al Wi-Fi dell'hotel.

1. Collega il telefono al Wi-Fi dell'hotel. Trova l'indirizzo MAC che il telefono usa per collegarsi al Wi-Fi dell'hotel.

    Ecco un esempio per iPhone (iOS 16.1.2): vai su Settings -> Wi-Fi -> seleziona il Wi-Fi dell'hotel e troverai il Wi-Fi Address. Annota questo indirizzo.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    Su alcuni modelli più vecchi, l'indirizzo MAC potrebbe non essere disponibile nelle impostazioni Wi-Fi. In questo caso, il dispositivo può usare il proprio MAC reale quando si collega al Wi-Fi pubblico, che puoi trovare in Settings > About (oppure "About Phone").

2. Collega il telefono o il computer al router. Accedi al pannello di amministrazione web del router, quindi clona o inserisci manualmente questo indirizzo MAC.

    **Per firmware v4.5 e precedenti**, seleziona NETWORK dal lato sinistro -> MAC Address.

    Seleziona Manual Mode, inserisci l'indirizzo MAC ottenuto nel passaggio 1 e fai clic su Apply.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **Per firmware v4.6 e successivi**, seleziona INTERNET dal lato sinistro -> sezione Repeater, quindi fai clic su Modify.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    Nella finestra popup, imposta **MAC Mode** su **Clone**, inserisci manualmente l'indirizzo MAC e fai clic su **Apply**.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. Potrebbe essere necessario riavviare il router affinché la modifica abbia effetto.

---

### Metodo 4：chiedi aiuto al personale dell'hotel

Alcuni hotel applicano politiche di verifica molto rigide per le proprie reti. Se nessuno dei metodi sopra funziona, prova a chiedere al personale dell'hotel di aggiungere direttamente l'indirizzo MAC del tuo router (usa il MAC di fabbrica, non quello casuale) alla whitelist della rete dell'hotel.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
