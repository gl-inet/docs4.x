# Qualità della rete

**Nota**: questa funzione è stata introdotta nel firmware v4.11.

---

Sul lato sinistro del pannello di amministrazione web, vai a **FLOW CONTROL** -> **Network Quality**.

La dashboard Qualità della rete monitora in tempo reale la qualità della connessione Internet. Valuta reattività, latenza e prestazioni DNS e rileva interruzioni della connessione e perdita di pacchetti. Queste metriche aiutano a individuare instabilità e problemi di connettività che i soli test della larghezza di banda potrebbero non evidenziare.

In questa pagina puoi valutare la connessione Internet tramite il punteggio della qualità della rete ed eseguire test di velocità locali quando necessario.

**Nota**:

1. Il punteggio complessivo della qualità della rete GL.iNet viene calcolato con la formula ponderata:

    `Punteggio complessivo = Punteggio di risposta × 60% + Punteggio di affidabilità × 40%`.

2. Speedtest è un test di velocità locale eseguito sul router ed è soggetto alle regole di limitazione della velocità di funzioni quali SQM e QoS.

## Punteggio della qualità della rete

Questa sezione mostra il punteggio complessivo della qualità della rete, calcolato in base al punteggio di risposta e al punteggio di affidabilità. Puoi visualizzare separatamente ogni punteggio. Il pannello mostra inoltre metriche correlate, tra cui latenza, jitter e perdita di pacchetti, insieme alle velocità di download e upload in tempo reale espresse in KB/s. Per impostazione predefinita, la dashboard usa `google.com` come destinazione per i controlli della connettività Internet e i test di risoluzione DNS.

Fai clic sull'icona delle impostazioni per configurare le destinazioni di verifica.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Puoi selezionare le destinazioni di verifica per la raggiungibilità Internet e la risoluzione DNS, tra cui Baidu, Tencent, Alibaba, Google, Microsoft o Cloudflare. Puoi anche inserire manualmente un dominio personalizzato.

Le destinazioni configurate vengono utilizzate per eseguire i test di connettività e DNS e calcolare il punteggio della qualità della rete.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: utilizzata per verificare la connettività Internet e misurare la latenza end-to-end (destinazione ping Hop2).

- **DNS Resolution Target**: il dominio risolto durante le verifiche DNS. Vengono interrogati sia i record A (IPv4) sia AAAA (IPv6).

## Speedtest

Questo test di velocità integrato usa Cloudflare Speed Test per misurare le velocità di download e upload, la latenza ping e il bufferbloat. Durante il test vengono visualizzati grafici della velocità in tempo reale.

Fai clic su **Run Speedtest** per avviare il test.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Al termine del test, la pagina ne mostra i risultati.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
