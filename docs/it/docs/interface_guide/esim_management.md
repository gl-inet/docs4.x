# Gestione eSIM

Nel pannello di amministrazione web, sul lato sinistro, vai su **APPLICATIONS** -> **eSIM Management**.

Questa pagina consente di controllare lo stato della eSIM Physical Card e di gestire i profili eSIM. E composta da due parti: **Current eSIM Status** e **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Modelli supportati

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | √         |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**Per i modelli contrassegnati con ※**:

1. Il firmware stabile attuale non supporta la eSIM. Per usare la funzione eSIM, devi installare un firmware con supporto eSIM. [Contattaci](https://www.gl-inet.com/contacts/){target="_blank"} per ulteriori istruzioni.

2. Per i modelli contrassegnati con ※ con modulo EP06-A, la eSIM non e supportata perche il software Qualcomm non include il supporto ai comandi AT richiesti.

3. Per GL-E750 (Mudi) e per i modelli contrassegnati con ※ con modulo EP06-E, fai riferimento a [questo link](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} per aggiornare prima il firmware del modulo e poi installare il firmware con supporto eSIM per abilitare la funzione.

**Per i modelli contrassegnati con X**:

1. GL-E750V2 vSIM non supporta la funzionalita eSIM.

2. GL-E5800 (Mudi 7) include una eSIM integrata. Di conseguenza, sul Mudi 7 la eSIM Physical Card verra riconosciuta come una normale scheda SIM, senza funzionalita eSIM.

## Current eSIM Status

Questa sezione mostra le informazioni di base e i dettagli del profilo eSIM attualmente attivo.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** identificatore univoco globale della eUICC (chip eSIM), usato per l'identificazione e la gestione dei profili.
- **ICCID:** Integrated Circuit Card Identifier del profilo eSIM attualmente attivo.
- **IMSI:** International Mobile Subscriber Identity del profilo eSIM attualmente attivo.
- **eSIM OS Version:** versione del sistema operativo della eUICC, che ne definisce compatibilita e capacita supportate.
- **eSIM Storage (remain/total):** capacita disponibile e totale della eUICC per memorizzare i profili eSIM.
- **eSIM Profile Number:** numero di profili eSIM attualmente memorizzati sulla eUICC. Tieni presente che i profili eSIM offerti da operatori diversi possono avere dimensioni differenti, quindi puo variare anche il numero di profili memorizzabili sulla eUICC.

## eSIM Profile List

Questa sezione mostra le informazioni relative al Seed Profile e ai profili normali.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: il Seed Profile e precaricato con 1 GB di dati gratuiti per Stati Uniti ed Europa, piu 100 MB di dati globali, validi per 1 anno dalla data di attivazione. Questi dati consentono di scaricare altri profili in tutto il mondo. Puoi anche monitorarne l'utilizzo, inclusi dati residui, volume totale e data di scadenza.

- **Normal Profile**: se acquisti un profilo eSIM e lo carichi tramite QR code o codice di attivazione, il profilo verra visualizzato qui.

### Ricaricare il Seed Profile

GL.iNet fornisce un Seed Profile precaricato con 100 MB di dati globali e 1 GB di dati validi in Europa e negli Stati Uniti per la configurazione iniziale e l'attivazione dei profili eSIM. Questo piano e pensato per scaricare nuovi profili eSIM quando arrivi a destinazione senza accesso a Internet.

Se hai gia consumato i dati gratuiti precaricati, oppure se sono scaduti e vuoi continuare a usare il servizio, puoi ricaricare il Seed Profile.

Nella sezione **Seed Profile**, fai clic sul pulsante **Top-up** a destra.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

Nella finestra pop-up, scansiona il QR code e segui le istruzioni per completare la ricarica.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Acquistare un profilo eSIM

Puoi acquistare profili eSIM nei nostri store consigliati, in store testati oppure da altri provider eSIM di terze parti.

??? note "Opzione 1: acquisto dai nostri store consigliati"

    Ci sono due store consigliati: [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} e [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    Nella sezione **Normal Profile**, fai clic su **eSIM Profile Recommended Store** a destra.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Scansiona il QR code oppure fai clic sui link per acquistare profili eSIM.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Nota**: tutti i pacchetti di profili eSIM acquistati da questi due store sono pienamente compatibili con i router GL.iNet. Se hai domande, contatta il nostro team di supporto all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Opzione 2: acquisto da store testati"

    Consulta [questo link](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} per visualizzare l'elenco degli store testati da GL.iNet.

    **Nota**: non possiamo garantire la piena compatibilita con i router GL.iNet per tutti i profili o pacchetti offerti da questi store. Poiche GL.iNet non ha partnership con essi, non possiamo fornire supporto post-vendita ne assistere per i rimborsi.

??? note "Opzione 3: acquisto da altri provider eSIM di terze parti"

    Puoi anche scegliere di acquistare profili eSIM da altri provider di tua scelta.

    Tuttavia, non possiamo garantire la piena compatibilita con i router GL.iNet per i profili eSIM acquistati da altri provider di terze parti. Acquista a tua discrezione. GL.iNet non e responsabile di eventuali problemi di incompatibilita.

    Per supporto post-vendita o rimborsi, contatta il provider eSIM corrispondente.

### Caricare un profilo eSIM

Dopo aver acquistato un profilo eSIM, di solito riceverai un QR code o un codice di attivazione. Salva il QR code in locale, quindi segui i passaggi riportati sotto per caricare il tuo profilo eSIM.

1. Nella sezione **Normal Profile**, fai clic su **Add eSIM Profile** in basso.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Carica il QR code eSIM oppure inserisci il codice di attivazione, quindi fai clic su **Install**. Il profilo verra scaricato e installato sul router.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Nota:**

    1. La maggior parte dei profili eSIM puo essere scaricata e installata una sola volta.

    2. Un QR code correttamente formattato mostrera un codice di attivazione che inizia con **LPA:**. Tuttavia, alcuni QR code non standard possono fornire solo un codice grezzo senza il prefisso LPA. In questo caso, aggiungi manualmente `LPA:` all'inizio del codice prima di fare clic su **Install**.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Se non hai ancora acquistato alcun profilo eSIM, puoi comprarne uno da **eSIM Profile Recommended Store**. Fai clic [qui](#acquistare-un-profilo-esim) per i dettagli.

3. Abilita il tuo profilo eSIM.

    Dopo il caricamento corretto, il nuovo profilo eSIM comparira nell'elenco **Normal Profile**. Fai clic su **Enable** per attivarlo.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Connettiti a Internet.

    Dopo aver abilitato il profilo eSIM, vai su **INTERNET** -> **Cellular**. Fai clic su **Connect** per stabilire una connessione Internet tramite il profilo eSIM.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Nota**: alcuni profili eSIM possono richiedere configurazioni aggiuntive, come impostazioni APN, PIN o TTL. Se necessario, fai clic su **Manual Setup** oppure **SIM Card Settings** per regolare questi parametri. In alcuni casi potrebbe essere necessario riavviare il dispositivo per stabilire la connessione Internet.*

5. Quando il router si connette correttamente tramite il profilo eSIM, la pagina verra visualizzata come segue:

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Esportare il log per il supporto

Fai clic su **Export Log for Support** per visualizzare tutti i log relativi alla eSIM. Se riscontri problemi e hai bisogno di assistenza tecnica, esporta i log eSIM e condividili con il nostro team di supporto via email all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Articoli correlati:

- [Come usare la eSIM Physical Card con i router GL.iNet?](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Come usare la eSIM Physical Card con i dispositivi Android?](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [Contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
