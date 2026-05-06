# Statistiche dei dati

Data Statistics offre una dashboard intuitiva del traffico che identifica l'utilizzo della rete per applicazione e protocollo. Supporta la visualizzazione delle tendenze storiche dell'ultima ora, dell'ultimo giorno e degli ultimi 7 giorni, mostra le classifiche di utilizzo, monitora il traffico per dispositivo e consente di bloccare con un clic le app indesiderate.

**Nota**:

1. Data Statistics non ha effetto quando il router è in modalità Drop-in Gateway.
2. Data Statistics non può funzionare con Network Acceleration. L'abilitazione di Data Statistics disattiva automaticamente Network Acceleration per garantire prestazioni stabili.

## Modelli supportati

!!! note "Modelli supportati"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **Data Statistics**.

Attiva l'interruttore nell'angolo superiore destro per visualizzare **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Questa pagina è composta da due parti:

- **Top 10 Apps by Bandwidth Usage**: presenta un grafico temporale, ad esempio relativo all'ultimo giorno, che mostra il consumo di banda delle 10 applicazioni principali nel periodo selezionato.

    Passa il mouse sul grafico per visualizzare il consumo dei dati delle 10 applicazioni che usano più banda in un momento specifico.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: mostra metriche dettagliate del traffico per ogni applicazione, inclusi Download, Upload e Total Bandwidth. Se necessario, cerca applicazioni specifiche nella barra di ricerca.

    Fai clic sulla freccia di ordinamento accanto all'intestazione della colonna per ordinare l'elenco in modo crescente o decrescente.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## Regole di archiviazione dei dati

1. Le statistiche del traffico vengono salvate nella RAM ogni 15 secondi e scritte nella memoria flash ogni 1 ora. Le scritture frequenti sulla flash vengono evitate per proteggere la durata della memoria.

2. Un soft reboot non causa perdita di dati. Prima del riavvio, il sistema scrive i dati dalla RAM alla flash.

3. Un hard reboot, scollegando e ricollegando l'alimentazione, o un aggiornamento del firmware mantenendo le impostazioni, possono causare la perdita dei dati fino all'ora più recente.

## Cambiare intervallo di tempo

Puoi passare da Past hour a Past day e Past week secondo necessità.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

L'intervallo di tempo scelto determina il modo in cui i dati vengono visualizzati:

- **Per un'analisi più dettagliata, ad esempio Past Hour**: il grafico mostra fluttuazioni in tempo reale e con maggiore granularità. I picchi sono più alti e i cali più netti, così è più facile individuare improvvisi aumenti dell'uso di banda.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Per una panoramica generale, ad esempio Past Day o Past Week**: il grafico condensa i dati su una timeline più lunga. Le curve risultano più uniformi e mostrano l'andamento generale del traffico invece di ogni piccola variazione.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

## Cancellare le statistiche

Fai clic sull'icona della scopa in alto a sinistra per cancellare le statistiche quando necessario.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Dopo la cancellazione, la pagina si aggiornerà come mostrato di seguito. Potrebbe essere necessario attendere qualche istante affinché inizino a caricarsi nuove statistiche.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
