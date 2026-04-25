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

Qui puoi visualizzare lo stato della tua eSIM e gestire i profili eSIM.

Solo un profilo eSIM può essere attivo alla volta. Un punto verde indica che il profilo eSIM selezionato è attualmente attivo.

---

Articolo correlato:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
