# QoS (Quality of Service)

**Nota**: questa funzionalità è stata introdotta nel firmware v4.9. Alcuni modelli, come Mango 2 (GL-MG1300), non supportano QoS a causa di memoria insufficiente, anche quando si esegue il firmware v4.9 o successivo.

---

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service) ottimizza l'allocazione della larghezza di banda dando priorità alle attività critiche (ad esempio videochiamate e giochi) durante la congestione della rete, riducendo la latenza e migliorando le prestazioni complessive della rete.

**Nota**:

1. Questa funzionalità influisce solo sul traffico che passa attraverso il router quando funziona come gateway, incluso il traffico client locale e il traffico client VPN. Non si applica al traffico in entrata quando il router funge da server VPN.
2. QoS non avrà effetto quando il router è in modalità Drop-in Gateway.
3. QoS e SQM non possono essere abilitati contemporaneamente.
4. QoS non può funzionare con l'accelerazione di rete. L'abilitazione di QoS disabiliterà automaticamente l'accelerazione di rete per garantire prestazioni stabili.

## Per firmware v4.11 e versioni successive

Attiva l'interruttore per abilitare QoS, quindi completa la configurazione seguendo i passaggi seguenti.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Inserisci manualmente le velocità di caricamento e download della WAN (intervallo di immissione: 1-10000) oppure fai clic su **Run Speedtest** per misurarle e compilare automaticamente i campi. Per eseguire il test di velocità è necessaria una connessione Internet attiva.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Nota**: i valori immessi nel campo di immissione sono in **Mbps** (megabit al secondo). L'equivalente **MB/s** (megabyte al secondo) viene visualizzato come riferimento.

2. **Scheduling Policy**

    È possibile selezionare una modalità policy. Le regole avanzate sostituiscono la policy di base per il traffico corrispondente.

    - **Device Priority**

        In questa modalità, i client locali selezionati ricevono una priorità di rete più elevata quando la connessione WAN è congestionata. Fare clic su **Add Device** e selezionare i dispositivi per ottenere la priorità della larghezza di banda durante il carico WAN intenso.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Puoi cercare i dispositivi per nome client, indirizzo MAC o indirizzo IP. Selezionare i dispositivi di destinazione e fare clic su **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        In questa modalità è possibile impostare le priorità per diverse applicazioni. Il router assegnerà la larghezza di banda di conseguenza.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Per personalizzare la priorità dell'applicazione, selezionare **Customize** e fare clic su **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        Nella finestra pop-up, tutte le categorie sono impostate su Priorità media per impostazione predefinita.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Trascina le categorie per modificarne la priorità secondo necessità, quindi fai clic su **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        In questa modalità è possibile creare regole QoS avanzate per il traffico ad alta priorità. Fare clic su **Add Rule** per definire le regole basate su protocollo, porta e IP di origine.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Specificare nome, protocollo, indirizzo di origine e porta di destinazione, quindi fare clic su **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Per firmware da v4.9 a v4.10

Attivare l'interruttore per abilitare QoS e la pagina verrà visualizzata come segue.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Imposta la velocità massima di upload e download (intervallo di immissione: 1-10000) per la pianificazione del traffico. Abbinali alla tua effettiva larghezza di banda Internet per ottenere i migliori risultati.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Nota**: i valori immessi nel campo di immissione sono in **Mbps** (megabit al secondo). L'equivalente **MB/s** (megabyte al secondo) viene visualizzato come riferimento.

Quindi impostare le priorità per le diverse applicazioni. Il router assegnerà la larghezza di banda di conseguenza.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Per personalizzare la priorità dell'applicazione, selezionare **Customize** e fare clic su **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

Nella finestra pop-up, tutte le categorie sono impostate su Priorità media per impostazione predefinita.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Trascina le categorie per modificarne la priorità secondo necessità, quindi fai clic su **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
