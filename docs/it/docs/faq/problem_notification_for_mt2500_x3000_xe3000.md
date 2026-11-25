# Avviso relativo a GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Ultimo aggiornamento: 11 novembre 2026**

Questo problema noto riguarda solo alcuni lotti. I dispositivi ordinati a partire dal 1º luglio 2025 appartengono con tutta probabilità a un lotto più recente e non richiedono l’aggiornamento del bootloader U-Boot.

Se non sai a quale lotto appartiene il dispositivo, invia a [support@gl-inet.com](mailto:support@gl-inet.com) i dati seguenti prima di apportare modifiche:

- Modello del router e versione del firmware
- Indirizzo MAC del dispositivo
- Descrizione del problema (incluse le operazioni in corso quando si è verificato), eventuali messaggi di errore e passaggi di risoluzione già tentati

Confermeremo il lotto di produzione e ti forniremo istruzioni mirate.

---

L’avviso originale riportato di seguito è conservato come riferimento. Le procedure di aggiornamento si applicano solo ai lotti interessati. In caso di dubbi, contatta l’assistenza come indicato sopra prima di apportare modifiche.

**Pubblicazione: 26 marzo 2025**

Gentili clienti GL.iNet,

Questo annuncio riguarda il problema di mancato avvio e di ripristino del firmware tramite U-Boot sui dispositivi GL-MT2500/GL-X3000/GL-XE3000. Il problema è stato causato da un difetto software per cui alcuni parametri sono stati definiti in modo errato, causando un funzionamento anomalo dei router. Di conseguenza, abbiamo valutato che questo problema possa ridurre in una certa misura la vita utile dei router e ce ne scusiamo sinceramente.

Per risolvere completamente il problema, consigliamo vivamente a tutti gli utenti di GL-MT2500, GL-X3000 e GL-XE3000 di eseguire sia l'aggiornamento del bootloader U-Boot sia l'aggiornamento del firmware. Entrambe le procedure di aggiornamento sono essenziali e non devono essere omesse.

Anche se il dispositivo è già stato aggiornato all'ultima versione del firmware, l'aggiornamento del bootloader U-Boot rimane obbligatorio per prevenire possibili problemi. Dopo aver completato l'aggiornamento del bootloader U-Boot, se l'ultimo firmware è già installato, puoi saltare la reinstallazione del firmware.

Prova ad aggiornare usando Chrome o Microsoft Edge. **NON** usare Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Aggiorna il bootloader U-Boot.

    Scarica [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}, quindi [aggiorna il bootloader U-Boot](upgrade_uboot_version.md).

2. Aggiorna il firmware.

    Scarica [il firmware più recente per il router](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"}, quindi [aggiorna il firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Aggiorna il bootloader U-Boot.

    Scarica [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}, quindi [aggiorna il bootloader U-Boot](upgrade_uboot_version.md).

2. Aggiorna il firmware.

    Scarica [il firmware più recente per il router](https://dl.gl-inet.com/router/x3000/stable){target="_blank"}, quindi [aggiorna il firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-XE3000 {#gl-xe3000}

1. Aggiorna il bootloader U-Boot.

    Scarica [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}, quindi [aggiorna il bootloader U-Boot](upgrade_uboot_version.md).

2. Aggiorna il firmware.

    Scarica [il firmware più recente per il router](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"}, quindi [aggiorna il firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

<br>

Ci scusiamo sinceramente per qualsiasi inconveniente causato. In futuro ci impegneremo a migliorare i nostri prodotti e firmware con ancora maggiore attenzione e cura.

Per chi possiede attualmente questi router, estenderemo il periodo di garanzia di un anno senza alcun costo. Se dovessi riscontrare problemi, non esitare a contattare i nostri team di supporto.

Se il problema persiste nonostante l'aggiornamento, contatta i nostri team di supporto all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com) e ti forniremo una nuova unità sostitutiva gratuitamente.

La vostra fiducia e il vostro supporto significano moltissimo per noi e ve ne siamo profondamente grati.

<br>
Cordiali saluti,<br>
Il team GL.iNet<br>
26 marzo 2025
