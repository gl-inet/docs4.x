# Guida alla risoluzione dei problemi della rete cellulare

Se non riesci a stabilire una connessione cellulare, controlla i seguenti possibili problemi.

??? "Controlla l'hardware del dispositivo"

    **1.1** Usa un alimentatore standard per il tuo dispositivo. Gli alimentatori non standard possono causare un'alimentazione insufficiente.

    **1.2** Assicurati che **Modem name**, **IMEI** e **SIM ICCID** siano visualizzati nel pannello di amministrazione web.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Per firmware ver.4.8 e successivi, fai clic su **View More Information** per trovare il SIM ICCID.

    Se non riesci a trovarli, riavvia il router. Se il modem name e l'IMEI continuano a non essere riconosciuti, contattaci all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).

    **1.3** Fai clic su **View More** per controllare **Cells Info** e confermare che il segnale sia stabile. Se il segnale è molto debole, assicurati che le antenne siano installate correttamente oppure sposta il router in un'area con un buon segnale e riprova.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}

    **1.4** Fai clic su **View More** per verificare se la banda di frequenza supportata dal dispositivo è compatibile con la tua area geografica.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Controlla le impostazioni software"

    **2.1** Accedi al pannello di amministrazione web e assicurati che il programma di connessione cellulare sia stato avviato. Puoi anche fare clic su **Abort** e poi su **Connect**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}

    **2.2** Alcuni operatori di rete potrebbero richiedere il **protocollo 3G** per stabilire la connessione. Passa al protocollo 3G e riprova.

    Per firmware ver.4.7 e precedenti, vai a **Manual Setup** -> **Protocol**, seleziona **3G**, quindi fai clic su **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    Per firmware ver.4.8 e successivi, vai a **SIM Card Settings** -> **Protocol**, seleziona **3G**, quindi fai clic su **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    Il dispositivo si ricollegherà automaticamente. Attendi qualche minuto per verificare se la connessione è riuscita.

    **2.3** Alcune schede SIM richiedono un APN specifico. Se la tua SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni. Se necessario, configura l'APN corretto sul router, quindi fai clic su **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}

    **2.4** Abilita **Band Masking** e riprova. Per firmware ver.4.7 e precedenti, fai riferimento a [questo link](../interface_guide/internet_cellular_v4.7.md/#band-masking). Per firmware ver.4.8 e successivi, fai riferimento a [questo link](../interface_guide/internet_cellular.md/#band-masking).

    **2.5** Blocca o sblocca una torre radio e riprova. Questa funzione è disponibile solo su GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) e GL-X2000 (Spitz Plus). Fai clic [qui](../interface_guide/internet_cellular.md/#lock-tower) per ulteriori istruzioni.

    Il blocco su una torre radio specifica consente al router di accedere a una risorsa di rete di alta qualità e di mantenere una connettività cellulare stabile.

    Tuttavia, una volta bloccata una torre, il router continuerà a provare a riconnettersi a quella torre dopo il riavvio, anche se viene spostato in una nuova posizione. Questo può impedire al router di connettersi automaticamente alla rete cellulare. In questo caso, puoi sbloccare la torre corrente dal pannello di amministrazione web del router oppure bloccarlo manualmente su una nuova torre.

    **Nota:** la torre bloccata deve corrispondere alle bande di frequenza supportate dal tuo operatore e dal dispositivo; in caso contrario, la connessione potrebbe non riuscire.

??? "Controlla la compatibilità della SIM"

    **3.1** Conferma il tipo di SIM. I router cellulari GL.iNet sono certificati come dispositivi IoT. In teoria, il dispositivo supporta solo schede SIM di tipo IoT. Se non sei sicuro del tipo di SIM, contatta il tuo operatore.

    I tipi di SIM più comuni includono: solo dati, solo dati + voce, IoT e hotspot. Ti consigliamo di usare schede SIM IoT o hotspot. Il funzionamento delle SIM solo dati o solo dati + voce non è garantito.

    **3.2** Alcune schede SIM devono prima essere attivate. Assicurati che la SIM possa accedere a Internet quando è inserita in un telefono, quindi spostala nel router.

    **3.3** Alcune schede SIM personalizzate possono essere usate solo su telefoni cellulari o dispositivi specifici. Verifica se la scheda SIM è bloccata su un dispositivo particolare.

    **3.4** In alcuni stati o città degli Stati Uniti (ad esempio AT&T a Seattle), potrebbe essere necessario registrare l'IMEI del dispositivo presso il tuo operatore. Se non sei sicuro della registrazione, contatta il tuo operatore.

    **3.5** Se il pannello di amministrazione web mostra "SIM card not registered", prova prima i passaggi sopra.

    Ti consigliamo di spegnere il router, inserire la scheda SIM e poi riavviare il router. Alcuni modelli non supportano l'hot swap e potrebbero non rilevare la scheda SIM se viene inserita mentre sono accesi.

    Assicurati che tutte le antenne siano installate correttamente, quindi riprova in un'area esterna con segnale cellulare forte. Un segnale debole può impedire alla scheda SIM di registrarsi sulla rete.

    Se il problema persiste, la scheda SIM potrebbe non essere compatibile con il router. Contatta il tuo operatore di rete per ulteriore assistenza.

    Se il tuo operatore conferma che il problema non è legato alla scheda SIM, contatta il nostro team di supporto all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Se la scheda SIM riesce a registrarsi e a ottenere un indirizzo IP ma non può accedere a Internet (l'upload funziona ma il download no), molto probabilmente la SIM è soggetta a restrizioni da parte del tuo operatore. Contatta l'operatore per rimuovere la restrizione oppure imposta TTL a 65 e riprova come mostrato di seguito.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    Quando contatti il tuo operatore di rete, fornisci il nome del modem del dispositivo, l'IMEI, il SIM ICCID e il modello del router.

Se nessuno dei passaggi sopra risolve il problema, contatta il nostro team di supporto all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).
