# Upgrade {#upgrade}

Sul lato sinistro del pannello di amministrazione web, vai su **SYSTEM** -> **Upgrade** per aggiornare il firmware del router.

Per alcuni modelli cellulari, se necessario puoi anche aggiornare la versione del modulo.

!!! Warning

    Mantieni l'alimentazione attiva durante l'aggiornamento. **NON** spegnere il router. Il dispositivo si riavvierà automaticamente dopo l'upgrade e l'operazione potrebbe richiedere alcuni minuti.

## Aggiornamento firmware {#firmware-upgrade}

### Aggiornamento online {#online-upgrade}

Online Upgrade verifica automaticamente via Internet la disponibilità del firmware ufficiale più recente e ne completa il download e il flashing direttamente sul router: è un modo pratico per aggiornare il firmware ufficiale con un clic, a condizione che il router sia connesso a Internet.

Puoi trovare la versione firmware corrente in **Firmware Online Upgrade**.

![upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/online_upgrade.png){class="glboxshadow"}

- **Accept Preview Plan**

    Se abilitata, questa opzione consente di provare nuove funzioni prima del rilascio della versione definitiva e inviare un feedback. Questi aggiornamenti potrebbero non essere stabili.

**Nota**: se durante un aggiornamento online compare **Download Failed**, vai su System -> Time Zone e correggi l'errore del fuso orario, sincronizzazione con il browser.

![online download failed](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/online_download_failed.jpg){class="glboxshadow" width="360"}

![time zone](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/time_zone.png){class="glboxshadow"}

### Aggiornamento locale {#local-upgrade}

Local Upgrade consente di caricare manualmente un file firmware per il flashing, permettendo di eseguire l'upgrade, il downgrade o l'installazione di firmware beta di versioni specifiche per provare le nuove funzioni.

Scarica prima il file firmware dal nostro [download center](https://dl.gl-inet.com){target="_blank"}, quindi vai su **Firmware Local Upgrade**.

![local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/local_upgrade.png){class="glboxshadow"}

Seleziona il file oppure trascinalo nell'area di caricamento. Il sistema verificherà il firmware.

![local upgrade uploaded](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/local_upgrade_uploaded.png){class="glboxshadow"}

- **Keep Settings:** se questa opzione è abilitata, le impostazioni correnti verranno mantenute e ti verrà chiesto di reinstallare eventuali pacchetti installati dall'utente dopo il completamento dell'upgrade. NON selezionare questa opzione quando esegui un downgrade del firmware.

Fai clic su **Install** per eseguire l'upgrade.

## Aggiornamento modem {#modem-upgrade}

I router cellulari GL.iNet consentono agli utenti di aggiornare il firmware del modem cellulare tramite il pannello di amministrazione web.

Puoi provare un aggiornamento del modulo cellulare quando la rete cellulare non funziona o mostra instabilità. Prima di eseguire l'upgrade del modem, consigliamo di contattare il supporto tecnico per il troubleshooting.

### Aggiornamento online {#online-upgrade_1}

Qui puoi trovare la versione corrente del modem cellulare. Se il router è connesso a Internet, controllerà automaticamente l'ultima versione del modem cellulare dal server del produttore, semplificando il processo di aggiornamento.

![modem online upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_online_upgrade.png){class="glboxshadow"}

### Aggiornamento locale {#local-upgrade_1}

Carica manualmente dal computer un file firmware del modem per aggiornare il modem cellulare, se necessario.

![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

## Aggiornamento online DPI {#dpi-online-upgrade}

L'aggiornamento online DPI controlla e aggiorna il motore DPI e il relativo database delle firme, garantendo un'identificazione accurata del traffico per Statistiche dati, Filtro contenuti e altre funzioni basate su DPI.

**Nota**: questa funzione è stata introdotta nel firmware v4.11.

![dpi online upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/dpi_online_upgrade.png){class="glboxshadow" width=700}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
