# Statistiche dei dati

Data Statistics offre una dashboard intelligente di analisi del traffico che categorizza e visualizza l'utilizzo della rete per applicazione, aiutandoti a monitorare il traffico in tempo reale e storico per ottenere maggiore consapevolezza e controllo della rete.

**Nota**:

1. Questa funzione e' attualmente disponibile solo su **GL-MT5000 (Brume 3)**.

2. Questa funzione non puo' funzionare con Network Acceleration. Abilitandola, Network Acceleration verra' disabilitato automaticamente per garantire il corretto funzionamento.

---

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** > **Data Statistics**.

Attiva l'interruttore nell'angolo superiore destro per visualizzare **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage**: presenta un grafico di tendenza basato sul tempo, ad esempio per il giorno precedente, per mostrare il consumo di banda delle 10 applicazioni principali nel periodo selezionato.

    Se necessario, cambia la timeline tra Past Hour, Past Day e Past Week.

- **App Traffic Statistics**: mostra metriche dettagliate del traffico per ogni applicazione, inclusi i dati di Download, Upload e Total Bandwidth.

    Se necessario, cerca applicazioni specifiche nella barra di ricerca.

## Regole di archiviazione dei dati

1. Le statistiche del traffico vengono salvate nella RAM ogni 15 secondi e archiviate nella flash ogni 1 ora. Le scritture frequenti sulla flash vengono evitate per proteggere la durata della memoria flash.

2. Un soft reboot non causa perdita di dati. Prima del riavvio, il sistema scrive i dati dalla RAM alla flash.

3. Un hard reboot (scollegare e ricollegare l'alimentazione) o un aggiornamento del firmware (mantenendo le impostazioni) possono causare la perdita dei dati fino all'ultima ora piu' recente.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
