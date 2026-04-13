# Come usare la eSIM Physical Card con i router GL.iNet?

Questa guida mostra come usare la eSIM Physical Card acquistata nello store online GL.iNet con i router GL.iNet.

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Caratteristiche

I punti principali della scheda eSIM fisica sono i seguenti:

- Supporta reti 4G e 5G per connessioni affidabili e veloci.
- Consente di gestire facilmente i profili eSIM aggiungendoli, rimuovendoli o abilitandoli.
- Permette di selezionare e acquistare in qualsiasi momento i pacchetti dati preferiti dalla maggior parte degli store eSIM nel mondo.
- Funziona con profili eSIM della maggior parte degli store eSIM globali.
- Consente di acquistare profili eSIM online senza fornire informazioni personali, riducendo il rischio di violazioni della privacy.
- Include un seed profile con 1 GB di dati gratuiti per Stati Uniti ed Europa, piu' 100 MB di dati globali, validi per 1 anno dalla data di attivazione.
- Compatibile con dispositivi GL.iNet selezionati.

## Modelli supportati

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | ※        |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**Per i modelli contrassegnati con ※**:

1. Il firmware stable attuale non supporta la eSIM. Per usare la funzione eSIM, devi installare il firmware con supporto eSIM. [Contattaci](https://www.gl-inet.com/contacts/){target="_blank"} per ulteriori istruzioni.

2. Se stai usando un modello contrassegnato con ※ con modulo EP06-A, la eSIM non e' supportata perche' il software Qualcomm non include il supporto per specifici comandi AT.

3. Se stai usando un modello contrassegnato con ※ con modulo EP06-E, fai riferimento a [questo link](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} per aggiornare il firmware del modulo e installare il firmware con supporto eSIM, cosi' da abilitare la funzionalita' eSIM.

**Per i modelli contrassegnati con X**:

1. GL-E750V2 vSIM non supporta la funzionalita' eSIM.

2. GL-E5800 (Mudi 7) include una eSIM integrata. Pertanto, su Mudi 7 la scheda eSIM fisica verra' riconosciuta come una normale scheda SIM, senza funzionalita' eSIM.

## Configurare la eSIM Physical Card

Se usi la eSIM Physical Card per la prima volta, guarda questo video di configurazione oppure segui i passaggi riportati di seguito per configurarla sul router GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Passaggio 1:** inserisci la eSIM Physical Card nel router. Fai riferimento alle immagini seguenti per una guida dettagliata.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Passaggio 2:** apri un browser e digita `192.168.8.1` nella barra degli indirizzi per accedere al GL.iNet Admin Panel.

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Passaggio 3:** collega il dispositivo a Internet.

Vai su **INTERNET** e fai clic su **Connect**, oppure **Auto Setup** nelle versioni firmware piu' basse, per connetterti a Internet tramite rete cellulare.

*Questa scheda eSIM fisica include un seed profile con 1 GB di dati gratuiti per Stati Uniti ed Europa, piu' 100 MB di dati globali, validi per 1 anno dalla data di attivazione. Tieni presente che questi dati servono solo per acquistare e scaricare profili eSIM e non sono destinati al normale accesso Internet.*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Se la connessione Internet va a buon fine, lo schermo apparira' come segue.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Gestire il profilo eSIM

**Passaggio 1:** assicurati che il dispositivo GL.iNet abbia installato il firmware piu' recente.

Assicurati che la Version sia 4.0 o superiore e che il numero Firmware Type sia 0319 o maggiore.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Se il firmware **non e' aggiornato**, puoi aggiornarlo automaticamente online oppure manualmente.

<u>Opzione 1</u>: aggiornamento firmware online

1. Assicurati che il dispositivo sia connesso a Internet.

2. Nel pannello di amministrazione web, vai su **SYSTEM** > **Upgrade** > **Online Upgrade** e fai clic sul pulsante **Install** per aggiornare automaticamente all'ultima versione firmware.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Opzione 2</u>: aggiornamento firmware manuale

1. Scarica da [qui](https://dl.gl-inet.com/){target="_blank"} il firmware del modello corrispondente che supporta la funzionalita' eSIM.

2. Nel pannello di amministrazione web, vai su **SYSTEM** > **Upgrade** > **Local Upgrade**. Seleziona il file firmware oppure trascinalo nell'area dedicata per aggiornare all'ultima versione.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Alcuni modelli, come Mudi (GL-E750), Puli (GL-XE300) e Spitz (GL-X750), non supportano la eSIM se equipaggiati con moduli Quectel EP06-A, a causa della mancanza di supporto per specifici comandi AT nel software Qualcomm.

    2. Se hanno installato moduli EP06-E, fai riferimento a [questo link](https://forum.gl-inet.com/t/48907){target="_blank"} per aggiornare il modulo all'ultima versione software per la funzionalita' eSIM.

**Passaggio 2:** vai a eSIM Management.

Dopo l'aggiornamento del firmware, attendi il riavvio del dispositivo e poi accedi al GL.iNet Admin Panel.

Vai su **APPLICATIONS** > **eSIM Management**. Qui puoi vedere lo stato attuale della tua eSIM.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Solo un profilo eSIM puo' essere attivo alla volta. Un punto verde indica che il profilo eSIM selezionato e' attualmente attivo.

## Guida a eSIM Management

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. Current eSIM Status:**

Questa sezione mostra le informazioni di base della eSIM e i dettagli del profilo attualmente attivo.

- **EID:** identificatore globale univoco della eUICC, il chip eSIM, usato per identificazione e controllo del profilo.
- **ICCID:** identificatore della scheda integrata del profilo eSIM attualmente attivo.
- **IMSI:** International Mobile Subscriber Identity del profilo eSIM attualmente attivo.
- **eSIM OS Version:** versione del sistema operativo della eUICC che ne definisce compatibilita' e capacita'.
- **eSIM Storage (remain/total):** capacita' disponibile e totale della eUICC per memorizzare i profili eSIM.
- **eSIM Profile Number:** numero di profili eSIM attualmente memorizzati sulla eUICC.

**B. Seed Profile:**

Questa sezione fornisce i dettagli del seed profile. Il seed profile e' precaricato con 1 GB di dati gratuiti per Stati Uniti ed Europa, piu' 100 MB di dati globali, validi per 1 anno dalla data di attivazione. Questi dati consentono di scaricare altri profili a livello globale. Puoi anche monitorarne l'uso, inclusi dati rimanenti, dati totali e data di scadenza.

**C. Normal Profile:**

Questa sezione mostra le informazioni sui profili normali. Se acquisti un profilo eSIM in uno store online e carichi il QR code tramite la funzione **Add eSIM Profile (QR Code Install)**, il profilo apparira' qui una volta completato il caricamento.

**D. Add eSIM Profile (QR Code Install):**

Questa e' la funzione principale per caricare e installare profili eSIM. Quando acquisti un profilo eSIM da uno store online, riceverai un QR code. Fai clic su questo pulsante per caricare il QR code, che scarichera' e installera' il profilo eSIM sul router.

**E. Export Log for Support:**

Questa sezione consente di visualizzare tutti i log relativi al funzionamento della eSIM. Se riscontri problemi e hai bisogno di supporto tecnico, puoi esportare questi log e condividerli con il nostro team di supporto via email all'indirizzo support@gl-inet.com.

**F. Top-up:**

Se esaurisci i dati omaggio e precaricati forniti da GL.iNet, oppure se i dati sono scaduti e vuoi continuare a usare il servizio, puoi fare clic sul pulsante **Top-up** per scansionare un QR code e acquistare dati aggiuntivi.

**G. Recommended eSIM Profile Stores:**

GL.iNet consiglia due store partner per la tua comodita': EIOTCLUB e Tuge. Puoi scansionare i QR code oppure fare clic sui link, [the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} oppure [the Tuge eSIM Store](https://esim_store.gl-inet.com/){target="_blank"}, per effettuare l'acquisto in base alle tue esigenze. Puoi anche scegliere di acquistare pacchetti eSIM da altri provider terzi di tua scelta.

**H. Actions:**

Questa sezione consente di gestire facilmente i profili eSIM, inclusa l'abilitazione, il cambio o l'eliminazione.

## Ricaricare il seed profile eSIM

Per la configurazione iniziale o per acquistare un profilo eSIM, GL.iNet fornisce dati precaricati: 100 MB per uso globale e 1 GB per Europa e Stati Uniti. Questi piani sono pensati per essere piu' costosi e sono destinati a situazioni in cui hai bisogno di scaricare un nuovo profilo eSIM una volta arrivato in un luogo senza accesso a Internet.

Per ricaricare il tuo seed profile eSIM, fai semplicemente clic sul pulsante **Top-up**, scansiona il QR code e segui le istruzioni.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## Acquistare e installare un profilo eSIM

Dopo aver configurato il router, segui i passaggi seguenti per acquistare e attivare il profilo eSIM.

**Passaggio 1:** acquista un profilo eSIM dagli eSIM store.

<u>Opzione 1</u>: acquista un profilo eSIM da uno dei nostri store consigliati, [the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} oppure [the Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}. Fai riferimento all'immagine seguente per i link diretti agli store.

*Tutti i pacchetti di profili eSIM acquistati da questi due store sono pienamente compatibili con i nostri router. Se hai domande, contatta il nostro team di supporto all'indirizzo support@gl-inet.com.*

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>Opzione 2</u>: fai riferimento a [questo link](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} per ottenere un elenco di store testati da GL.iNet. Tieni presente che non possiamo garantire che tutti i pacchetti di questi store siano pienamente compatibili con i router GL.iNet.

*Poiche' GL.iNet non ha partnership con questi store, non possiamo fornire assistenza post-vendita o rimborsi relativi a tali pacchetti.*

<u>Opzione 3</u>: acquista un profilo eSIM da altri provider terzi a tua scelta.

**Passaggio 2**: installa il tuo profilo eSIM

Dopo aver acquistato il profilo eSIM, riceverai un QR code. Salvalo sul tuo computer. Poi fai clic sul pulsante **Add eSIM Profile (QR Code Install)** per caricare e installare il profilo eSIM acquistato.

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**Nota**: come indicato dalla freccia verde nell'immagine sopra, un QR code correttamente formattato mostrera' un codice di attivazione che inizia con **LPA:**.

*Tuttavia, alcuni QR code non standard possono produrre solo un codice di attivazione grezzo senza il prefisso LPA.
Se cio' accade, aggiungi manualmente `LPA:` all'inizio del codice prima di fare clic sul pulsante Download & Install.*

**Passaggio 3:** abilita il nuovo profilo

Dopo aver caricato correttamente il QR code, vedrai il nuovo profilo eSIM elencato nella sezione **Normal Profile**. Fai clic su **Enable** per attivare il nuovo profilo eSIM.

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**Passaggio 4:** applica il nuovo profilo eSIM e collegati a Internet

Dopo aver abilitato il profilo eSIM, vai su **INTERNET** e fai clic su **Connect** per applicare il profilo eSIM e connetterti a Internet.

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

*Nota: alcuni profili eSIM potrebbero richiedere impostazioni aggiuntive, come APN, PIN o TTL. Se necessario, fai clic su **Manual Setup** oppure **SIM Card Settings** per configurarle. In alcuni casi potrebbe essere necessario riavviare il dispositivo per stabilire la connessione Internet.*

Una volta che il profilo eSIM e' stato configurato correttamente, lo schermo apparira' come segue:

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**Passaggio 5:** passa facilmente da un profilo eSIM all'altro oppure eliminalo

Puoi passare facilmente tra i profili eSIM facendo clic su **Enable** accanto al profilo che vuoi attivare. Per rimuovere un profilo eSIM, fai semplicemente clic su **Delete**.

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
