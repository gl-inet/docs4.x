# Firmware v4.11

Questa versione migliora il monitoraggio della qualità della rete e la valutazione della sicurezza, aiutandoti a identificare problemi di connessione e potenziali rischi di sicurezza. Introduce inoltre nuove funzioni Mesh, GL.iNet Account e VLAN, oltre a importanti miglioramenti a DNS, SQM, QoS e statistiche del traffico.

Scarica il firmware più recente dal [centro di download del firmware](https://dl.gl-inet.com/){target="_blank"}.

## Qualità della rete

[Network Quality](../interface_guide/network_quality.md) è una nuova funzione che monitora la connessione Internet in tempo reale. Valuta reattività, latenza e prestazioni DNS, rilevando interruzioni della connessione e perdita di pacchetti per aiutarti a identificare instabilità della rete e problemi di connessione che i soli test della larghezza di banda potrebbero non evidenziare.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Scansione di sicurezza

[Security Scan](../interface_guide/security_scan.md) è una nuova funzione che valuta le impostazioni di sicurezza del router e fornisce un punteggio di sicurezza, avvisi sui rischi e suggerimenti di ottimizzazione. Controlla elementi quali sicurezza Wi-Fi, ping WAN, accesso SSH remoto, port forwarding e protezione dei contenuti tramite DPI, aiutandoti a identificare e risolvere potenziali rischi di sicurezza. La scansione si avvia automaticamente quando apri la pagina. Puoi anche fare clic sull'icona del punteggio per azzerare e ripetere la scansione.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## Mesh

[Mesh](../interface_guide/mesh.md) è una funzione basata sullo standard Wi-Fi EasyMesh™ che estende la copertura Wi-Fi a tutta la casa e consente un roaming senza interruzioni. Se disponi di più router GL.iNet, configurane uno come router principale e gli altri come nodi mesh per un roaming Wi-Fi senza interruzioni in tutta la casa.

**Nota**: questa funzione è stata inizialmente rilasciata su alcuni modelli ed estesa ad altri modelli nella versione firmware 4.11.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/mesh.png){class="glboxshadow"}

## Account GL.iNet

Un [account GL.iNet](../interface_guide/glinet_account.md) offre un accesso unificato ai dispositivi e ai servizi cloud. Con un unico account GL.iNet puoi accedere a GoodCloud e all'app GL.iNet per gestire più comodamente la rete e i dispositivi. Inoltre, puoi usare GoodPAS per stabilire rapidamente una connessione sicura tra il router da viaggio e la rete domestica, consentendo un accesso remoto senza interruzioni quando sei fuori casa.

**Nota**: questa funzione è stata inizialmente rilasciata su alcuni modelli ed estesa ad altri modelli nella versione firmware 4.11.

![GL.iNet Account](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/glinet_account.png){class="glboxshadow"}

## GoodPAS

[GoodPAS](../interface_guide/goodpas.md) è una soluzione di accesso remoto basata sul protocollo AmneziaWG con offuscamento del traffico integrato. Consente di collegare in modo sicuro il router da viaggio alla rete domestica tramite un codice di accesso dinamico, senza registrazione né accesso a un account.

**Nota**: questa funzione è stata inizialmente rilasciata su alcuni modelli ed estesa ad altri modelli nella versione firmware 4.11.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodpas.png){class="glboxshadow"}

## GoodCloud

[GoodCloud](../interface_guide/cloud.md) consente l'accesso remoto e la gestione centralizzata dei router GL.iNet. Puoi gestire i dispositivi in gruppo, distribuire configurazioni di rete, aggiornare il firmware e accedere da remoto al pannello di amministrazione web o al terminale SSH del router.

**Nota**: questa funzione è stata inizialmente rilasciata su alcuni modelli ed estesa ad altri modelli nella versione firmware 4.11.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodcloud.png){class="glboxshadow"}

## Porta Ethernet

La pagina [Ethernet Port](../interface_guide/ethernet_port_v4.10.md) mostra tutte le interfacce del router. Puoi visualizzare lo stato di connessione di ogni interfaccia, gestire il ruolo delle porte Ethernet (WAN o LAN) e consultare dettagli come indirizzo MAC, velocità negoziata e stato attuale del collegamento. Inoltre, puoi assegnare le interfacce fisiche a qualsiasi sottorete che hai creato.

**Nota**: questa funzione è stata inizialmente rilasciata su alcuni modelli ed estesa ad altri modelli nella versione firmware 4.11.

La figura seguente mostra la pagina Ethernet Port di Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/ethernet_port.png){class="glboxshadow"}

## DNS

Questa versione migliora la configurazione [DNS](../interface_guide/dns_v4.11.md) riunendo WAN DNS, VPN DNS e Manual DNS in un'unica pagina. Puoi visualizzare facilmente lo stato DNS di ogni tipo di connessione, configurare server DNS personalizzati e scegliere se le impostazioni DNS manuali si applicano ai tunnel VPN o al router stesso.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns_v4.11.png){class="glboxshadow"}

## QoS

La [QoS](../interface_guide/qos.md) (qualità del servizio) è stata migliorata in questo firmware. È stata aggiunta l'opzione **Run Speedtest** per la larghezza di banda WAN, che misura la larghezza di banda in download e upload e compila automaticamente i campi corrispondenti. Sono disponibili tre criteri di pianificazione, tra cui le nuove opzioni **Device Priority** e **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: i client locali selezionati ricevono una priorità di rete più alta durante la congestione della WAN.

- **Application Priority**: imposta priorità personalizzate per le diverse applicazioni; il router assegnerà la larghezza di banda di conseguenza.

- **Advanced QoS**: crea regole QoS avanzate per il traffico ad alta priorità.

## SQM

[SQM](../interface_guide/sqm.md) (Smart Queue Management) offre un'opzione **Run Speedtest** per la larghezza di banda WAN, che misura le velocità di download e upload e compila automaticamente i campi corrispondenti. Per la disciplina di accodamento **cake**, la nuova opzione **Cake Autorate** regola dinamicamente la larghezza di banda configurata in base all'RTT delle sonde. Usa ping leggeri anziché test di velocità attivi ed è consigliata per le connessioni WAN con larghezza di banda variabile.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_v4.11.png){class="glboxshadow" width=600}

![cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/cake_autorate.png){class="glboxshadow" width=600}

## Statistiche dei dati

[Data Statistics](../interface_guide/data_statistics.md) ora supporta il filtraggio del traffico per client e introduce nuove visualizzazioni, tra cui grafici a barre e a torta. In App Traffic Statistics puoi selezionare un client specifico e passare da una visualizzazione all'altra per un'analisi più chiara dell'utilizzo del traffico.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
