# SQM (Smart Queue Management)

SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", garantendo gaming e chiamate vocali più fluidi.

**Nota**:

1. Questa funzione influisce solo sul traffico che attraversa il router quando opera come gateway, incluso il traffico dei client locali e quello del client VPN. Non si applica al traffico in ingresso quando il router agisce come server VPN.

2. Poiché SQM richiede molte risorse, funziona al meglio su reti a bassa larghezza di banda o congestionate. Abilitarlo su connessioni ad alta velocità può ridurre il throughput massimo.
3. SQM non ha effetto quando il router è in modalità Drop-in Gateway.
4. SQM e QoS non possono essere abilitati contemporaneamente.
5. SQM non può funzionare con Network Acceleration. L'abilitazione di SQM disattiva automaticamente Network Acceleration per garantire prestazioni stabili.

## Modelli supportati

!!! note "Modelli supportati"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Nota: i modelli contrassegnati con ※ supportano SQM a partire dal firmware v4.9.

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **SQM**.

Attiva l'interruttore per abilitare SQM, quindi imposta la velocità massima di upload e download, intervallo di input 1 - 10000, per la pianificazione del traffico. Per ottenere i migliori risultati, falle corrispondere alla tua effettiva larghezza di banda Internet.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Nota**: i valori inseriti nel campo di input sono espressi in **Mbps** (megabit al secondo). L'equivalente in **MB/s** (megabyte al secondo) viene mostrato come riferimento.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Per Queue Rule sono disponibili due opzioni:

- **cake**: traffic shaping intelligente e automatico con un controllo complessivo della latenza superiore, consigliato.

- **fq_codel**: fair queueing semplice ed efficiente con riduzione di base della latenza.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
