# Come aggiornare o eseguire il downgrade manuale del firmware del router, da v4.x a v4.x?

Questo tutorial mostra **come aggiornare o eseguire manualmente il downgrade del firmware del router, da v4.x a v4.x**. I passaggi per l'aggiornamento manuale e per il downgrade del firmware del router sono gli stessi.

!!! Note "Informazioni su upgrade e downgrade del firmware del router"

    **Upgrade:** i router GL.iNet con firmware versione 4.x non offrono la funzione di aggiornamento automatico.

    Quando e' disponibile una nuova versione firmware, dopo il login nel pannello di amministrazione del router vedrai il prompt "Upgrade Reminder". Puoi fare clic sul pulsante **Upgrade** per installare l'ultima versione firmware elencata. Se vuoi passare a una specifica versione firmware, segui i passaggi riportati di seguito per aggiornare manualmente il router.

    **Downgrade:** puoi eseguire il downgrade del firmware del router per risolvere alcuni problemi.

## 1. Verifica se il router esegue l'ultima versione firmware, solo per upgrade

1. In un browser web, inserisci l'URL del pannello di amministrazione del router, ad esempio 192.168.8.1, ed effettua l'accesso.
2. Dalla barra laterale sinistra, seleziona **SYSTEM** > **Upgrade**.

## 2. Scarica il file firmware

1. Nella barra di ricerca del [firmware download center](https://dl.gl-inet.com/), cerca e seleziona il modello del tuo router.
2. Nella scheda **Stable** o in altre schede, seleziona **Download for common upgrade and uboot** accanto alla versione firmware che vuoi scaricare.

## 3. Carica il firmware

Le istruzioni seguenti sono state scritte per il caricamento del firmware tramite pannello di amministrazione del router. Per caricare il firmware tramite app mobile GL.iNet, [scarica l'app](https://www.gl-inet.com/app/) e configurala.

1. In un browser web, inserisci l'URL del pannello di amministrazione del router, ad esempio 192.168.8.1, ed effettua l'accesso.
2. Facoltativo: se vuoi eseguire il backup delle impostazioni correnti, segui i passaggi riportati di seguito.

    ??? "Esegui il backup delle impostazioni correnti"

        a. Dalla barra laterale sinistra, fai clic su **SYSTEM** > **Advanced Settings**.

        b. Fai clic sul collegamento oppure sul pulsante **Go To LuCI** per accedere alla pagina di login di LuCI.

        c. Inserisci la password amministratore, poi fai clic su **Log in**.

        d. Fai clic su **System** > **Backup / Flash Firmware**.

        e. In **Backup**, fai clic su **Generate archive**. Sul dispositivo verra' scaricato un file contenente le impostazioni correnti.

        **Tieni presente che questo file e' valido solo per la versione firmware al momento del backup e non per altre versioni firmware.**

3. Dalla barra laterale sinistra, fai clic su **SYSTEM** > **Upgrade**.
4. Fai clic su **Local Upgrade** e seleziona il file scaricato in precedenza.
5. Per mantenere le impostazioni correnti, ad esempio la password amministratore del router, attiva **Keep Settings**.
6. Fai clic su **Install**.

**Nota**: durante il processo di upgrade, non spegnere il router. Una volta completato l'upgrade, vedrai la schermata di login del router.

Se durante il processo di aggiornamento firmware hai perso le impostazioni del router, ripristinale.

Se il metodo sopra non funziona, prova ad aggiornare il firmware tramite [U-boot](../faq/debrick.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
