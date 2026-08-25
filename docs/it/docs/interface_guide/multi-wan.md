# Multi-WAN

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Multi-WAN**.

Puoi configurare il router con piu' metodi di accesso a Internet, in modo che quando un tipo di accesso a Internet non e' disponibile possa passare automaticamente a un altro in breve tempo. Oppure puoi usare piu' metodi di accesso a Internet contemporaneamente, assegnando le connessioni di rete ai diversi metodi secondo un determinato rapporto.

I router GL.iNet possono connettersi a Internet in diversi modi, come [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md), [Cellular](internet_cellular.md).

!!! Note

    1. I modelli privi di funzionalita' Wi-Fi, ad esempio GL-MT2500/GL-MT2500A, supportano solo l'accesso di rete tramite Ethernet, Tethering e Cellular.

    2. I modelli senza porta USB, ad esempio GL-B3000, supportano solo l'accesso di rete tramite Ethernet e Repeater.

    3. Alcuni modelli supportano [Dual-Ethernet WAN](ethernet_port.md#dual-ethernet-wan), che aggiungera' un'ulteriore interfaccia Ethernet nell'interfaccia utente.

## Tracciamento dello stato dell'interfaccia

I router GL.iNet supportano fino a 5 interfacce di rete virtuali, anche se il numero esatto puo' variare in base al modello. Ad esempio, GL-MT6000 dispone di **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** e **Cellular**, ciascuna con funzioni di rete distinte in configurazioni definite via software.

I router usano il comando **ping** o **httping** (solo per v4.3 e precedenti) per monitorare lo stato della connessione verso l'IP di destinazione e determinare se l'interfaccia e' disponibile.

Se l'interfaccia e' disponibile, sul lato sinistro verra' visualizzato un punto verde; altrimenti sara' grigio.

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Impostazioni di tracciamento dello stato

Fai clic sull'icona a forma di ingranaggio per accedere alle impostazioni di tracciamento dello stato di ciascuna interfaccia di rete.

Ad esempio, questa e' l'impostazione di tracciamento dello stato per l'interfaccia Ethernet e lo stesso vale per le altre interfacce.

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: e' abilitato per impostazione predefinita. Puoi disabilitare il tracciamento dello stato dell'interfaccia; in tal caso il router determinera' lo stato dell'interfaccia in base allo stato fisico, ad esempio se il cavo di rete e' collegato o meno.

- **Detection Mode**: questa funzione e' stata introdotta come Low Data Mode nella v4.5 e rinominata Detection Mode nella v4.7. Sono disponibili tre modalita': Normal Mode, Low Data Mode e Strict Mode.

    La modalita' Normal viene usata per impostazione predefinita; la modalita' Low Data esegue il tracciamento solo quando si verifica un errore di rete dell'interfaccia, mentre la modalita' Strict determina lo stato dell'interfaccia solo in base al risultato di un comando di rilevamento verso un IP pubblico.

    Puoi usare Low Data Mode quando hai un piano dati limitato. Tuttavia, uno svantaggio e' che la riconnessione dopo una disconnessione di rete potrebbe essere leggermente piu' lenta rispetto alla modalita' normale e, per impostazione predefinita, verra' attivata solo l'interfaccia cellular.

- **Track Command**: il comando ping viene usato per monitorare lo stato della connessione verso l'IP di destinazione e determinare se l'interfaccia e' disponibile. Per il firmware v4.3 e precedenti e' disponibile anche il comando httping.

- **IPv4 Track IP**: qui puoi personalizzare l'IPv4 Track IP.

!!! Note

    Alcuni firmware meno recenti, come la v4.3, forniscono impostazioni come **Track Interval**, **Change to Failure Condition** e **Change to Available Condition**. Queste impostazioni sono state rimosse dalla v4.5 e sostituite da Detection Mode e Sensitivity Options.

### Opzioni di sensibilita'

Questa funzione e' disponibile dalla v4.5.

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

Questa sensibilita' determina l'intervallo di tempo per il rilevamento dello stato di Internet.

- Se la rete e' stabile e ti trovi in scenari come visione di video o live streaming, oppure gaming, si consiglia di usare un'alta sensibilita' per un passaggio rapido in caso di disconnessione della rete.
- Se la rete e' instabile e stai scaricando file in cache, si consiglia di usare una bassa sensibilita' per evitare continui cambi di rete e rilevamenti di connessioni non riuscite.

**Suggerimenti**: passare a un'alta sensibilita' puo' causare disconnessioni di rete; regolala con cautela.

## Modalità Multi-WAN

Multi-WAN offre due modalità: **Failover** e **Load Balance**. Le due modalità si escludono a vicenda ed è possibile utilizzarne una sola.

### Failover

Failover è la modalità predefinita quando sono presenti connessioni Multi-WAN. Se il collegamento attivo si interrompe, il router passa automaticamente a un'altra interfaccia di rete per accedere a Internet.

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

È possibile impostare la priorità di ogni interfaccia: quando l'interfaccia in uso si interrompe, il router passa alla successiva interfaccia disponibile con la priorità più alta. Quando viene ripristinata una connessione con priorità superiore, il router torna automaticamente a utilizzarla.

### Load Balance

Load Balance consente di utilizzare contemporaneamente più collegamenti di rete, aumentando la larghezza di banda e migliorando il throughput complessivo.

Il **Load Ratio** determina la distribuzione del traffico tra le interfacce: il sistema assegna le nuove connessioni a ciascuna interfaccia in base al rapporto configurato.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

È possibile configurare i due rapporti di carico seguenti:

- **Default Load Ratio**

    Se il router è connesso contemporaneamente a quattro reti (Ethernet, Repeater, Tethering e Cellular) e tutte e quattro le interfacce possono accedere a Internet, abilitando Load Balance e impostando il rapporto su 1:1:1:1 la larghezza di banda viene distribuita in modo uniforme. Il sistema assegna infatti le nuove connessioni alle quattro interfacce secondo il rapporto 1:1:1:1.

- **Customize Load Ratio**

    Se la larghezza di banda Ethernet è 200 Mbps, quella Wi-Fi del Repeater è 100 Mbps e non sono attive connessioni Tethering o Cellular, è possibile impostare il rapporto su 2 per Ethernet, 1 per Repeater e 0 per Tethering/Cellular. Il sistema assegna le nuove connessioni secondo il rapporto 2:1, consentendo a Ethernet di gestire circa il doppio delle connessioni del Repeater. Rispetto alla modalità Failover, questa configurazione ottimizza il throughput complessivo bilanciando il carico tra le interfacce disponibili.

**Nota:** non e' garantito che le connessioni o il traffico gia' attivi corrispondano al rapporto di carico. Il comportamento si avvicina maggiormente a questo rapporto se viene usato per un periodo piu' lungo.

## Scenari di utilizzo

* Il sistema di cassa di un negozio usa una connessione cablata a Internet, mentre Repeater verso il Wi-Fi di negozi vicini, oppure una scheda SIM per abilitare la rete cellulare, come metodo di accesso a Internet di backup, cosi' da evitare che i pagamenti mobili si interrompano quando il cavo di rete non e' disponibile.

* Il router si collega tramite Repeater a un Wi-Fi pubblico, ma la velocita' di rete non e' sufficiente; in questo caso puoi usare contemporaneamente Mobile Tethering per il load balance in modo da migliorare la larghezza di banda complessiva.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
