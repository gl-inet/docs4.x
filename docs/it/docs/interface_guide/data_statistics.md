# Statistiche dei dati

**Nota**: questa funzionalità è stata introdotta nel firmware v4.9. Alcuni modelli, come Mango 2 (GL-MG1300), non supportano le statistiche dei dati a causa della memoria insufficiente, anche quando si esegue il firmware v4.9 o successivo.

---

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **Data Statistics**.

Data Statistics fornisce un dashboard intuitivo sul traffico che identifica l'utilizzo della rete in base all'applicazione e al protocollo. Supporta la visualizzazione delle tendenze storiche di 1 ora, 1 giorno e 7 giorni, visualizza le classifiche di utilizzo, monitora il traffico per dispositivo e consente il blocco con un clic delle app indesiderate.

**Nota**:

1. Le statistiche dei dati non avranno effetto quando il router è in modalità Drop-in Gateway.
2. Le statistiche dei dati non possono funzionare con l'accelerazione di rete. L'abilitazione delle statistiche sui dati disabiliterà automaticamente l'accelerazione della rete per garantire prestazioni stabili.
3. Le statistiche dei dati tengono traccia solo dell'utilizzo del traffico per i dispositivi elencati nella pagina Client. Se un dispositivo si connette al router tramite un'interfaccia tunnel (ad esempio client VPN, Tailscale o AstroWarp), il traffico proveniente da quel dispositivo e inoltrato attraverso il router è escluso da queste statistiche.

## Per firmware v4.11 e versioni successive

Attiva l'interruttore nell'angolo in alto a destra per visualizzare **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Questa pagina è composta da due parti:

- **Top 10 Apps by Bandwidth Usage**: presenta un grafico di tendenza basato sul tempo (ad esempio per l'ultimo giorno) per mostrare il consumo di larghezza di banda delle 10 principali applicazioni nel periodo selezionato.

    Passa il mouse sul grafico per visualizzare l'utilizzo dei dati delle 10 principali app che consumano larghezza di banda in un momento specifico.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: visualizza metriche dettagliate sul traffico per ciascuna applicazione, inclusi download, caricamento e larghezza di banda totale. Se necessario, cerca app specifiche nella barra di ricerca.

    Fare clic sulla freccia di ordinamento accanto all'intestazione della colonna per ordinare l'elenco in ordine crescente o decrescente.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Regole di archiviazione dei dati

1. Le statistiche sul traffico vengono salvate nella RAM ogni 15 secondi e archiviate nella flash ogni 1 ora. Vengono evitate frequenti scritture flash per proteggere la durata della memoria flash.

2. Un riavvio graduale non causerà la perdita di dati. Il sistema scrive innanzitutto i dati dalla RAM alla memoria flash prima di riavviarsi.

3. Un riavvio forzato (scollegando e ricollegando l'alimentazione) o un aggiornamento del firmware (mantenendo le impostazioni) potrebbero causare la perdita di dati fino all'ora più recente.

### Selettore cliente

Il Selettore cliente consente di selezionare un cliente specifico o di mantenere l'impostazione predefinita Tutti i clienti. Il grafico e la tabella delle statistiche si aggiorneranno automaticamente per visualizzare i dati sul traffico solo per il dispositivo selezionato.

**Nota**: questa funzionalità è stata introdotta nel firmware v4.11.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Cambia visualizzazione grafico

Puoi cambiare il tipo di grafico secondo necessità quando visualizzi le statistiche sul traffico dell'app.

**Nota**: questa funzionalità è stata introdotta nel firmware v4.11.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: il grafico tiene traccia dell'utilizzo della larghezza di banda nell'intervallo di tempo selezionato. Le curve continue rivelano come il traffico cambia nel tempo, rendendolo ideale per individuare tendenze di utilizzo in aumento e in diminuzione.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: il grafico confronta l'utilizzo della larghezza di banda tra le applicazioni affiancate. Le singole barre mostrano chiaramente a colpo d'occhio quali app consumano più larghezza di banda.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: il grafico suddivide l'utilizzo totale della larghezza di banda in quote percentuali. Le sezioni visualizzano la proporzione relativa del traffico utilizzato da ciascuna applicazione.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Cambia intervallo di tempo

È possibile modificare l'intervallo di tempo tra Ultima ora, Ultimo giorno e Ultima settimana in base alle esigenze.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

L'intervallo di tempo scelto determina la modalità di visualizzazione dei dati:

- **For a closer look (ad esempio Ultima ora)**: il grafico mostra fluttuazioni dettagliate e in tempo reale. I picchi sono più alti e i cali più ripidi, rendendo facile individuare picchi improvvisi nell’utilizzo della larghezza di banda.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **For a broad overview (ad esempio Ultimo giorno o Ultima settimana)**: il grafico condensa i dati in una sequenza temporale più lunga. Le curve diventano più morbide, mostrando l'andamento generale del traffico piuttosto che ogni piccola variazione.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Cancella statistiche

Fai clic sull'icona della scopa nell'angolo in alto a sinistra per cancellare le statistiche secondo necessità.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Dopo la cancellazione, la pagina verrà aggiornata come mostrato di seguito. Potrebbe essere necessario attendere qualche istante affinché le nuove statistiche inizino a caricarsi.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## Per firmware da v4.9 a v4.10

Attiva l'interruttore nell'angolo in alto a destra per visualizzare **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Questa pagina è composta da due parti:

- **Top 10 Apps by Bandwidth Usage**: presenta un grafico di tendenza (ad esempio per l'ultimo giorno) basato sul tempo per mostrare il consumo di larghezza di banda delle 10 principali applicazioni nel periodo selezionato.

    Passa il mouse sul grafico per visualizzare l'utilizzo dei dati delle 10 principali app che consumano larghezza di banda in un momento specifico.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: visualizza metriche dettagliate sul traffico per ciascuna applicazione, inclusi download, caricamento e larghezza di banda totale. Se necessario, cerca app specifiche nella barra di ricerca.

    Fare clic sulla freccia di ordinamento accanto all'intestazione della colonna per ordinare l'elenco in ordine crescente o decrescente.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Regole di archiviazione dei dati

1. Le statistiche sul traffico vengono salvate nella RAM ogni 15 secondi e archiviate nella flash ogni 1 ora. Vengono evitate frequenti scritture flash per proteggere la durata della memoria flash.

2. Un riavvio graduale non causerà la perdita di dati. Il sistema scrive innanzitutto i dati dalla RAM alla memoria flash prima di riavviarsi.

3. Un riavvio forzato (scollegando e ricollegando l'alimentazione) o un aggiornamento del firmware (mantenendo le impostazioni) potrebbero causare la perdita di dati fino all'ora più recente.

### Cambia intervallo di tempo

È possibile modificare l'intervallo di tempo tra Ultima ora, Ultimo giorno e Ultima settimana in base alle esigenze.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

L'intervallo di tempo scelto determina la modalità di visualizzazione dei dati:

- **For a closer look (ad esempio Ultima ora)**: il grafico mostra fluttuazioni dettagliate e in tempo reale. I picchi sono più alti e i cali più ripidi, rendendo facile individuare picchi improvvisi nell’utilizzo della larghezza di banda.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **For a broad overview (ad esempio Ultimo giorno o Ultima settimana)**: il grafico condensa i dati in una sequenza temporale più lunga. Le curve diventano più morbide, mostrando l'andamento generale del traffico piuttosto che ogni piccola variazione.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Cancella statistiche

Fai clic sull'icona della scopa nell'angolo in alto a sinistra per cancellare le statistiche secondo necessità.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Dopo la cancellazione, la pagina verrà aggiornata come mostrato di seguito. Potrebbe essere necessario attendere qualche istante affinché le nuove statistiche inizino a caricarsi.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
