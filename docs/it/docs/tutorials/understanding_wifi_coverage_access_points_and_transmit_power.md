---
title: Comprendere copertura Wi-Fi, access point e potenza di trasmissione
---

# Comprendere copertura Wi-Fi, access point e potenza di trasmissione

Molti utenti presumono che aumentare la potenza di trasmissione di un router migliori sempre copertura e prestazioni Wi-Fi.

Sebbene una potenza di trasmissione piu' elevata aumenti generalmente la copertura di un singolo router, la potenza massima non e' sempre ideale nelle reti con piu' access point (AP), nodi mesh o implementazioni Wi-Fi aziendali.

Comprendere celle di copertura, roaming, pianificazione dei canali e potenza di trasmissione puo' aiutare a migliorare le prestazioni wireless.

## Router singolo rispetto a piu' access point

### Router singolo

Se hai un solo router che fornisce copertura Wi-Fi:

- Una potenza di trasmissione piu' elevata aumenta generalmente la copertura.
- I dispositivi client possono mantenere una connessione utilizzabile a distanze maggiori.
- Ridurre la potenza di trasmissione normalmente riduce il segnale ricevuto e il rapporto segnale-rumore (SNR) in downlink.

Per la maggior parte degli utenti con un solo router, e' consigliabile lasciare la potenza di trasmissione sull'impostazione predefinita o automatica.

Ridurre la potenza di trasmissione del router non riduce l'energia RF trasmessa dalle reti Wi-Fi vicine. I loro router e AP continuano a trasmettere alla stessa potenza.

### Piu' access point

Quando vengono distribuiti piu' AP, l'obiettivo non e' necessariamente massimizzare l'area di copertura di ogni AP.

L'obiettivo e' invece creare piu' celle di copertura piu' piccole e ben definite, che si sovrappongano solo quanto basta per fornire copertura continua e roaming affidabile.

Posizionamento adeguato degli AP, potenza di trasmissione e selezione dei canali sono tutti aspetti importanti.

## Sovrapposizione delle celle di copertura

Se ogni AP trasmette alla potenza massima, le rispettive aree di copertura possono sovrapporsi eccessivamente.

Un dispositivo client puo' rimanere connesso a un AP distante anche quando un AP piu' vicino offre un segnale piu' forte. Questo fenomeno e' comunemente chiamato **sticky client**.

Un client connesso all'AP sbagliato puo' riscontrare:

- SNR piu' basso
- Tassi di modulazione e codifica piu' bassi
- Piu' ritrasmissioni
- Throughput ridotto
- Latenza maggiore

Ridurre la potenza di trasmissione degli AP puo' restringere le celle di copertura e incoraggiare i dispositivi client a effettuare il roaming prima.

## Comprendere il roaming dei client

Nella maggior parte delle reti Wi-Fi, e' il dispositivo client a decidere quando effettuare il roaming.

Il router o l'AP puo' fornire assistenza al roaming, ma telefono, laptop, tablet o altro client normalmente prendono la decisione finale di lasciare un AP e collegarsi a un altro.

Dispositivi client diversi utilizzano soglie e algoritmi di roaming diversi. Un dispositivo puo' quindi restare connesso a un AP finche' considera la connessione utilizzabile, anche quando un altro AP offre un segnale piu' forte.

Ridurre una sovrapposizione eccessiva della copertura puo' aiutare i client a prendere decisioni di roaming migliori.

## Riutilizzo spaziale

Wi-Fi e' un mezzo condiviso.

Prima di trasmettere, i dispositivi Wi-Fi ascoltano per determinare se il canale e' gia' in uso. Se AP che usano lo stesso canale riescono a sentirsi tra loro su un'area estesa, possono passare piu' tempo in attesa che il canale diventi disponibile.

Questo riduce il tempo di trasmissione utilizzabile e il throughput complessivo.

Una riduzione appropriata della potenza di trasmissione puo' consentire ad AP che usano lo stesso canale in aree fisiche diverse di operare in modo piu' indipendente. Questo e' noto come **riutilizzo spaziale**.

Il riutilizzo spaziale non significa che ridurre la potenza di trasmissione dell'AP riduca le interferenze trasmesse dalle reti vicine. Celle di copertura dimensionate correttamente possono invece ridurre la contesa non necessaria e consentire il riutilizzo dello stesso canale in aree sufficientemente separate.

## Pianificazione dei canali

Potenza di trasmissione e selezione dei canali devono essere considerate insieme.

### 2,4 GHz

La banda a 2,4 GHz ha relativamente pochi canali non sovrapposti.

In molte regioni normative, i canali 1, 6 e 11 sono comunemente usati con larghezza di canale di 20 MHz.

Quando possibile, AP vicini dovrebbero usare canali diversi non sovrapposti.

### 5 GHz e 6 GHz

Le bande a 5 GHz e 6 GHz offrono piu' canali disponibili, rendendo piu' semplice assegnare canali diversi ad AP vicini.

L'uso di canali non sovrapposti riduce la contesa co-canale, anche se una sovrapposizione eccessiva della copertura puo' comunque influire sul comportamento di roaming.

I canali disponibili dipendono dal modello del router, dal Paese o regione, dalla larghezza del canale e dalle normative locali.

## AP cablati e reti mesh

### Access point cablati

Una connessione Ethernet cablata tra il router principale e gli AP aggiuntivi e' generalmente la distribuzione preferita.

Poiche' la connessione cablata trasporta il traffico di backhaul, la potenza di trasmissione Wi-Fi puo' essere regolata principalmente per copertura dei client, roaming e riutilizzo spaziale.

### Mesh con backhaul cablato

I nodi mesh che usano backhaul cablato possono essere ottimizzati in modo simile agli AP cablati.

La potenza di trasmissione puo' essere regolata per ridurre la sovrapposizione eccessiva delle celle mantenendo al contempo una copertura continua.

### Mesh con backhaul wireless

In una distribuzione mesh wireless, le radio Wi-Fi possono anche trasportare traffico tra nodi mesh.

Ridurre la potenza di trasmissione in modo troppo aggressivo puo' indebolire la connessione di backhaul wireless e ridurre le prestazioni complessive.

Quando usi backhaul wireless, assicurati che i nodi mesh mantengano tra loro una connessione forte e stabile.

## Esempio di distribuzione multi-AP

Considera due router GL.iNet collegati via Ethernet:

- Il router principale fornisce servizi di routing, DHCP, NAT e firewall.
- Il secondo router opera in modalita' Access Point.
- Entrambi i dispositivi trasmettono lo stesso nome di rete Wi-Fi e le stesse impostazioni di sicurezza.
- Gli AP vicini usano canali diversi non sovrapposti.
- La potenza di trasmissione e' regolata in modo che le celle di copertura si sovrappongano abbastanza per il roaming, ma non eccessivamente.

La potenza di trasmissione ideale dipende da materiali dell'edificio, posizionamento degli AP, dispositivi client, reti Wi-Fi vicine e area di copertura desiderata.

Non esiste un singolo valore di potenza di trasmissione corretto per ogni distribuzione.

## Idee errate comuni

### La potenza massima fornisce sempre il Wi-Fi migliore

La potenza massima generalmente fornisce l'area di copertura piu' ampia, ma puo' creare sovrapposizione eccessiva e comportamento di roaming scadente nelle distribuzioni multi-AP.

### Una potenza di trasmissione piu' bassa riduce le interferenze in ingresso

Ridurre la potenza di trasmissione del tuo AP riduce il segnale generato dal tuo AP. Non riduce la potenza trasmessa da router o AP vicini.

### Una potenza di trasmissione piu' bassa rende il ricevitore dell'AP piu' sensibile

Potenza di trasmissione e sensibilita' del ricevitore sono caratteristiche separate. Ridurre la potenza di trasmissione non migliora intrinsecamente la capacita' dell'AP di ricevere trasmissioni dai client.

### I dispositivi client si collegano sempre all'AP piu' vicino

I dispositivi client normalmente selezionano gli AP ed effettuano il roaming tra essi usando i propri algoritmi interni. Possono rimanere connessi a un AP piu' distante anche quando e' disponibile un AP piu' vicino.

## Punti di partenza consigliati

| Distribuzione | Raccomandazione |
| --- | --- |
| Router singolo | Lascia la potenza di trasmissione sull'impostazione predefinita o automatica. |
| Due o piu' AP cablati | Usa canali non sovrapposti e regola la potenza di trasmissione per ridurre la sovrapposizione eccessiva. |
| Mesh con backhaul cablato | Ottimizza le celle di copertura per un roaming affidabile. |
| Mesh con backhaul wireless | Evita di ridurre la potenza abbastanza da indebolire la connessione di backhaul. |

Dopo aver apportato modifiche, testa le prestazioni in piu' posizioni e verifica:

- Potenza del segnale
- Throughput in upload e download
- Latenza
- Roaming tra AP
- Qualita' del backhaul wireless, se applicabile

Modifica un'impostazione alla volta in modo da poterne misurare accuratamente l'effetto.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com) o [contattaci](https://www.gl-inet.com/contact-us/).
