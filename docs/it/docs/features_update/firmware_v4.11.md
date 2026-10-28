# Firmware v4.11 {#firmware-v411}

Questa versione migliora il monitoraggio della qualità della rete e la valutazione della sicurezza, aiutandoti a identificare problemi di connessione e potenziali rischi di sicurezza. Migliora inoltre DNS, QoS, SQM e le statistiche dei dati per una gestione della rete e un controllo del traffico più flessibili.

Scarica il firmware più recente dal [centro di download del firmware](https://dl.gl-inet.com/){target="_blank"}.

## Qualità della rete {#network-quality}

[Network Quality](../interface_guide/network_quality.md) è una nuova funzione che monitora la connessione Internet in tempo reale. Valuta reattività, latenza e prestazioni DNS, rilevando interruzioni della connessione e perdita di pacchetti per aiutarti a identificare instabilità della rete e problemi di connessione che i soli test della larghezza di banda potrebbero non evidenziare.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Scansione di sicurezza {#security-scan}

[Security Scan](../interface_guide/security_scan.md) è una nuova funzione che valuta le impostazioni di sicurezza del router e fornisce un punteggio di sicurezza, avvisi sui rischi e suggerimenti di ottimizzazione. Controlla elementi quali sicurezza Wi-Fi, ping WAN, accesso SSH remoto, port forwarding e protezione dei contenuti tramite DPI, aiutandoti a identificare e risolvere potenziali rischi di sicurezza. La scansione si avvia automaticamente quando apri la pagina. Puoi anche fare clic sull'icona del punteggio per azzerare e ripetere la scansione.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## UPnP {#upnp}

[UPnP](../interface_guide/upnp.md) consente ai dispositivi LAN e alle applicazioni compatibili di richiedere automaticamente mappature delle porte senza configurare manualmente il port forwarding. Questo semplifica la connettività per giochi online, condivisione di file peer-to-peer e accesso remoto. Nella pagina UPnP puoi visualizzare le mappature attive, controllare la durata residua del lease ed eliminare le mappature quando necessario.

![UPnP](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/upnp.png){class="glboxshadow"}

## DNS {#dns}

Questa versione migliora la configurazione [DNS](../interface_guide/dns_v4.11.md) riunendo WAN DNS, VPN DNS e Manual DNS in un'unica pagina. Puoi visualizzare facilmente lo stato DNS di ogni tipo di connessione, configurare server DNS personalizzati e scegliere se le impostazioni DNS manuali si applicano ai tunnel VPN o al router stesso.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) offre l'opzione **Run Speedtest** per la larghezza di banda WAN, che misura le velocità di download e upload e compila automaticamente i campi corrispondenti. Oltre ad Application Priority, questa versione aggiunge due criteri di pianificazione: **Device Priority** e **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: i client locali selezionati ricevono una priorità di rete più alta durante la congestione della WAN.

- **Application Priority**: imposta priorità personalizzate per le diverse applicazioni; il router assegnerà la larghezza di banda di conseguenza.

- **Advanced QoS**: crea regole QoS avanzate per il traffico ad alta priorità.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) offre un'opzione **Run Speedtest** per la larghezza di banda WAN, che misura le velocità di download e upload e compila automaticamente i campi corrispondenti. Sono disponibili due discipline di accodamento: **cake** e **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: gestione intelligente e automatica del traffico con il miglior controllo complessivo della latenza (consigliata).

    Per questa disciplina di accodamento, la nuova opzione **Cake Autorate** regola dinamicamente la larghezza di banda configurata in base all'RTT delle sonde. Usa ping leggeri anziché test di velocità attivi ed è consigliata per le connessioni WAN con larghezza di banda variabile.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: accodamento equo semplice ed efficiente, con una riduzione di base della latenza.

## Statistiche dei dati {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) ora supporta il filtraggio del traffico per client e introduce nuove visualizzazioni, tra cui grafici a barre e a torta. In App Traffic Statistics puoi selezionare un client specifico e passare da una visualizzazione all'altra per un'analisi più chiara dell'utilizzo del traffico.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
