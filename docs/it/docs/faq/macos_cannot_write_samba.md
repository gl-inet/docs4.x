# macOS non riesce a scrivere su una condivisione Samba

Quando si usa un dispositivo di archiviazione formattato exFAT per una condivisione Samba, alcuni dispositivi macOS possono mostrare uno dei seguenti errori quando provano a scrivere file nella condivisione.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Prova a risolvere il problema con i metodi seguenti.

1. **Controlla i permessi della condivisione Samba.**

    Assicurati che la condivisione Samba sia configurata con accesso in scrittura. Accedi al pannello di amministrazione web del router e verifica che la cartella condivisa abbia i permessi "Read/Write" abilitati per il tuo account utente.

2. **Usa il comando `cp -X file-name` per copiare il file.**

    Poiché Finder aggiunge automaticamente attributi estesi (ad esempio resource fork e metadati) durante i trasferimenti, che possono entrare in conflitto con la gestione Samba dell'archiviazione exFAT, prova a usare il comando **cp -X file-name** per copiare il file.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Oppure usa il comando **cp -rX folder-name** per copiare la cartella.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Riavvia il Mac.**

    Fai clic sul menu Apple e poi su Restart. Se il problema persiste, spegni il Mac, scollega tutti i dispositivi esterni, attendi 30 secondi e quindi riavvialo.

4. **Rinomina il file.**

    Fai clic con il tasto destro sul file e poi su Rename. Usa nomi semplici ed evita caratteri speciali come !@# o gli spazi.

5. **Ricollega il dispositivo di archiviazione.**

    Se stai usando un'unità esterna come una chiavetta USB, espellila prima di scollegarla, attendi 10 secondi, quindi ricollegala. Puoi anche provare una porta USB diversa.

6. **Ripara gli errori del disco con First Aid.**

    Dati corrotti sul disco possono causare errori di scrittura. Puoi usare Utility Disco di macOS per correggere il problema.

    1. Apri Finder -> Applications -> Utilities -> Disk Utility.
    2. Seleziona l'unità o il dispositivo di archiviazione (locale o esterno) nella barra laterale sinistra.
    3. Fai clic su First Aid -> Run. Attendi il completamento del processo.

7. **Regola il file system oppure formatta l'unità.**

    Se stai usando un'unità formattata exFAT, su macOS possono verificarsi problemi di compatibilità con Samba. Puoi provare i seguenti metodi.

    - **Formatta in FAT32** (per unità esterne, compatibilità multipiattaforma)

        1. Esegui prima il backup dei dati presenti sull'unità (la formattazione cancella tutti i file).
        2. Apri Disk Utility -> seleziona l'unità -> Erase.
        3. Scegli "MS-DOS (FAT)" (FAT32) come formato -> fai clic su Erase.

    - **Formatta in ext4**

        !!! Note

            ext4 è supportato principalmente dai sistemi Linux. Dopo la formattazione in ext4, il dispositivo di archiviazione potrebbe non essere compatibile con i sistemi operativi Windows, con possibili problemi come l'impossibilità di riconoscere o scrivere sull'unità da dispositivi Windows.

        1. Esegui il backup di tutti i dati presenti sull'unità, poiché la formattazione li cancellerà.
        2. Usa uno strumento come Disk Utility o un sistema Linux per formattare l'unità in ext4.

8. **Aggiorna macOS e svuota le cache.**

    Software obsoleto o cache corrotte possono causare conflitti. Vai su System Settings -> General -> Software Update e installa la versione più recente, quindi svuota le cache di sistema.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
