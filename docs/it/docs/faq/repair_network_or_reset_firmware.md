# Come riparare la rete o ripristinare le impostazioni di fabbrica?

Tutti i router GL.iNet sono dotati di un meccanismo di reset fisico (pulsante reset o foro pinhole). Premere il pulsante o inserire un perno nel foro produce lo stesso effetto: ripristinare la connettività di rete oppure riportare il router alle impostazioni di fabbrica.

Per i modelli dotati di foro pinhole, usa uno spillo, una graffetta raddrizzata o uno strumento simile per eseguire l'operazione.

Assicurati che il router abbia completato l'avvio prima di eseguire un reset. **NON** premere il pulsante reset subito dopo l'accensione, perché potresti attivare la modalità failsafe U-Boot.

## Riparare la rete

Tieni premuto il pulsante reset per **4 secondi**, quindi rilascialo per eseguire un soft reset, che può riparare la rete.

Questa operazione riavvia l'interfaccia di rete e ripristina l'interfaccia Internet alle impostazioni predefinite, mantenendo però impostazioni Wi-Fi, impostazioni VPN, impostazioni di sistema e così via.

**Nota**:

1. Se il Wi-Fi è stato disabilitato, un soft reset lo ripristinerà allo stato abilitato predefinito.

2. Un soft reset può essere usato anche per passare rapidamente dalla modalità non-router alla modalità router.

## Ripristino di fabbrica

**Per i modelli senza touchscreen**, il firmware può essere ripristinato in due modi: tramite il pulsante reset oppure dal pannello di amministrazione web. Guarda questo video oppure segui i passaggi seguenti.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jguDqBWP-Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Usando il meccanismo di reset fisico (pulsante o foro pinhole).

    Tieni premuto il pulsante reset (oppure inserisci un perno nel foro pinhole) per **10 secondi**, quindi rilascialo per riportare il router alle impostazioni di fabbrica. Tutti i dati utente verranno cancellati.

    **Nota:** se il ripristino di fabbrica non funziona, potrebbe essere necessario seguire il [tutorial Uboot](debrick.md) per sbloccare il router.

2. Ripristino del firmware dal pannello di amministrazione web.

    Accedi al pannello di amministrazione web del router e vai su SYSTEM -> Reset Firmware. Fai clic sul pulsante per ripristinare il firmware.

    **Nota:** tutte le impostazioni e i dati attuali andranno persi. Il processo richiederà circa 2 minuti. **NON** spegnere il router durante il processo.

    ![glinet reset firmware](https://static.gl-inet.com/docs/router/en/4/tutorials/reset_firmware/reset_firmware_4.8.png){class="glboxshadow"}

**Per i modelli con touchscreen**, il firmware può essere ripristinato in tre modi: tramite touchscreen, pulsante reset o pannello di amministrazione web.

Il seguente video mostra questi metodi utilizzando il Mudi 7 (GL-E5800). Gli stessi passaggi si applicano a tutti i modelli con touchscreen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3Kx_StIFLqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
<small></small>

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
