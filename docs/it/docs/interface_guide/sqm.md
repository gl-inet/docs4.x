# SQM (Smart Queue Management)

SQM, Smart Queue Management, gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il "bufferbloat", garantendo gaming e chiamate vocali piu' fluidi.

**Nota**:

1. Questa funzione e' attualmente disponibile solo su **GL-MT5000 (Brume 3)**.

2. Questa funzione influisce sul traffico che passa attraverso il router come gateway, incluso il traffico dei client locali e il traffico del client VPN, ma non sul traffico in ingresso quando il router agisce come VPN Server.

3. Poiche' SQM richiede molte risorse, funziona al meglio su reti a bassa larghezza di banda o congestionate. Abilitarlo su connessioni ad alta velocita' puo' ridurre il throughput massimo.

---

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** > > **SQM**.

Imposta prima la velocita' massima di upload e download, intervallo di input: 1 - 10000, per la pianificazione del traffico. Per ottenere i migliori risultati, falle corrispondere alla tua effettiva larghezza di banda Internet.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

Per Queue Rule sono disponibili due opzioni:

- **cake**: traffic shaping intelligente e automatico con controllo complessivo superiore della latenza, consigliato.

- **fq_codel**: fair queueing semplice ed efficiente con riduzione di base della latenza.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
