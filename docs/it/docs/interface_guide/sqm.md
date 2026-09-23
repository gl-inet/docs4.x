# SQM (Smart Queue Management)

**Nota**: questa funzionalità è stata introdotta nel firmware v4.9.

Alcuni modelli, come Mango 2 (GL-MG1300), non supportano SQM a causa della memoria insufficiente, anche con firmware v4.9 o successivo.

---

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **SQM**.

SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", garantendo giochi e chiamate vocali più fluidi.

**Nota**:

1. Questa funzionalità influisce solo sul traffico che passa attraverso il router quando funziona come gateway, incluso il traffico client locale e il traffico client VPN. Non si applica al traffico in entrata quando il router funge da server VPN.
2. Poiché SQM richiede molte risorse, funziona meglio per reti con larghezza di banda ridotta o congestionate. Abilitarlo su connessioni ad alta velocità può ridurre il picco di throughput.
3. SQM non avrà effetto quando il router è in modalità Drop-in Gateway.
4. SQM e QoS non possono essere abilitati contemporaneamente.
5. SQM non può funzionare con l'accelerazione di rete. L'abilitazione di SQM disabiliterà automaticamente l'accelerazione di rete per garantire prestazioni stabili.

## Modelli supportati {#supported-models}

??? "Modelli supportati"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Modelli non supportati"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Per firmware v4.11 e versioni successive

Attiva l'interruttore per abilitare SQM, quindi completa la configurazione seguendo i passaggi seguenti.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Inserisci manualmente le velocità di caricamento e download della WAN (intervallo di immissione: 1-10000) oppure fai clic su **Run Speedtest** per misurarle e compilare automaticamente i campi. Per eseguire il test di velocità è necessaria una connessione Internet attiva.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Nota**: i valori immessi nel campo di immissione sono in **Mbps** (megabit al secondo). L'equivalente **MB/s** (megabyte al secondo) viene visualizzato come riferimento.

2. **Queue Discipline**

    Seleziona una regola di accodamento per gestire il traffico e ridurre la latenza sotto carico.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: modellazione del traffico intelligente e automatica con controllo della latenza generale superiore (consigliato).

        Quando viene selezionato **cake** come disciplina della coda, **Cake Autorate** è disponibile come funzionalità opzionale.

        Cake Autorate è uno shaper basato sulla latenza che riduce o aumenta la larghezza di banda CAKE in tempo reale in base alla sonda RTT. Non vengono eseguiti test di velocità attivi; vengono utilizzati solo ping leggeri. Consigliato ogni volta che la larghezza di banda WAN fluttua; non necessario sui collegamenti stabili.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Nota**: Cake Autorate genera traffico sonda in background continuo. Considera questo ulteriore utilizzo dei dati quando utilizzi una connessione a consumo.

        Le impostazioni predefinite sono adatte per la maggior parte delle connessioni. Modifica i seguenti parametri solo se comprendi come influenzano Cake Autorate. Se necessario, fare clic su **Reset to Default** per ripristinare le impostazioni predefinite della sonda e della soglia.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: un elenco di indirizzi IP separati da virgole, utilizzato per il sondaggio della qualità della rete.

        - **Probe Interval**: intervalli più brevi consentono una risposta più rapida ma consumano più risorse della CPU.

        - **Concurrent Probes**: il numero di sondaggi simultanei non deve superare il numero di server di sonda; valori più alti aumentano il carico della CPU.

        - **Idle Detection Threshold**: quando la velocità di trasferimento scende al di sotto di questo valore, la connessione verrà considerata inattiva. Questo valore non deve superare il 25% del limite di velocità configurato.

        - **Download Latency Threshold**: quando la latenza del download supera questa soglia, viene attivata la riduzione della larghezza di banda.

        - **Upload Latency Threshold**: quando la latenza di caricamento supera questa soglia, viene attivata la riduzione della larghezza di banda.

    - **fq_codel**: accodamento semplice ed efficiente con riduzione della latenza di base.

## Per firmware da v4.9 a v4.10

Attiva l'interruttore per abilitare SQM e imposta la velocità massima di upload e download (intervallo di immissione: 1-10000) per la pianificazione del traffico. Abbinali alla tua effettiva larghezza di banda Internet per ottenere i migliori risultati.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Nota**: i valori immessi nel campo di immissione sono in **Mbps** (megabit al secondo). L'equivalente **MB/s** (megabyte al secondo) viene visualizzato come riferimento.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Per la regola della coda sono disponibili due opzioni:

- **cake**: modellazione del traffico intelligente e automatica con controllo della latenza generale superiore (consigliato).

- **fq_codel**: accodamento equo semplice ed efficiente con riduzione della latenza di base.

!!! tip

    Una differenza tra le impostazioni QoS e SQM è che QoS consente di impostare le priorità dell'applicazione, con il router che alloca la larghezza di banda di conseguenza; mentre SQM ti consente di selezionare una regola di coda.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
